#!/usr/bin/env python3
"""Generate the offline structural-peak labels used by PeakFocus.

The paper defines a structural peak with the ``peakdetect`` method from the
third-party ``findpeaks`` package.  The detector is applied to the complete
chronological load series before the train/validation/test split.  We use a
sensitivity threshold of 0 and lookahead windows of 5 for ELC and 3 for WLEL.

The script preserves every input column and appends (or replaces) the binary
``is_peak`` column.  It does not normalize, shuffle, split, or otherwise alter
the load series.

Examples
--------
Reproduce the ELC labels from the public Informer electricity file::

    python preprocess_peak_labels.py electricity.csv elc_with_peaks.csv \
        --value-column OT --timestamp-column date --lookahead 5 \
        --expected-peaks 1429

Reproduce the WLEL labels from its chronological hourly-maximum series::

    python preprocess_peak_labels.py wlel_hourly_max.csv wlel_with_peaks.csv \
        --value-column value --timestamp-column date --lookahead 3 \
        --expected-peaks 2944

To audit a CSV that already contains labels, add
``--verify-existing-labels``.  The command then fails if any regenerated label
differs from the existing label column.
"""

from __future__ import annotations

import argparse
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Sequence

import numpy as np
import pandas as pd
from findpeaks import findpeaks


def positive_integer(text: str) -> int:
    """Parse a strictly positive integer for argparse."""
    value = int(text)
    if value <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return value


def nonnegative_float(text: str) -> float:
    """Parse a finite, nonnegative floating-point value for argparse."""
    value = float(text)
    if not np.isfinite(value) or value < 0:
        raise argparse.ArgumentTypeError("must be a finite nonnegative number")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate PeakFocus structural-peak labels with findpeaks/peakdetect."
        )
    )
    parser.add_argument("input_csv", type=Path, help="Chronological input CSV.")
    parser.add_argument("output_csv", type=Path, help="Labeled output CSV.")
    parser.add_argument(
        "--value-column",
        required=True,
        help="Load column passed to findpeaks (for example, OT or value).",
    )
    parser.add_argument(
        "--timestamp-column",
        help="Optional timestamp column to validate for chronological order.",
    )
    parser.add_argument(
        "--lookahead",
        required=True,
        type=positive_integer,
        help="Peak lookahead window: 5 for ELC and 3 for WLEL.",
    )
    parser.add_argument(
        "--sensitivity-threshold",
        type=nonnegative_float,
        default=0.0,
        help="findpeaks limit (paper notation: eta); default: 0.",
    )
    parser.add_argument(
        "--label-column",
        default="is_peak",
        help="Output label column; default: is_peak.",
    )
    parser.add_argument(
        "--expected-peaks",
        type=positive_integer,
        help="Optional assertion on the total detected peak count.",
    )
    parser.add_argument(
        "--verify-existing-labels",
        action="store_true",
        help="Require regenerated labels to match an existing label column.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow replacement of an existing output file.",
    )
    return parser


def validate_timestamps(frame: pd.DataFrame, column: str) -> None:
    """Require parseable, unique, and strictly increasing timestamps."""
    if column not in frame.columns:
        raise ValueError(f"timestamp column {column!r} is absent from the input")

    timestamps = pd.to_datetime(frame[column], errors="coerce")
    invalid = int(timestamps.isna().sum())
    if invalid:
        raise ValueError(f"timestamp column {column!r} contains {invalid} invalid values")
    if timestamps.duplicated().any():
        raise ValueError(f"timestamp column {column!r} contains duplicate values")
    if not timestamps.is_monotonic_increasing:
        raise ValueError(f"timestamp column {column!r} is not chronologically ordered")


def load_values(frame: pd.DataFrame, column: str) -> np.ndarray:
    """Return the selected load column as a validated float array."""
    if column not in frame.columns:
        raise ValueError(f"value column {column!r} is absent from the input")

    numeric = pd.to_numeric(frame[column], errors="coerce")
    values = numeric.to_numpy(dtype=np.float64)
    invalid = int((~np.isfinite(values)).sum())
    if invalid:
        raise ValueError(f"value column {column!r} contains {invalid} non-finite values")
    return values


def detect_structural_peaks(
    values: np.ndarray, lookahead: int, sensitivity_threshold: float
) -> np.ndarray:
    """Return one uint8 peak label per input observation."""
    detector = findpeaks(
        method="peakdetect",
        lookahead=lookahead,
        limit=sensitivity_threshold,
        verbose="silent",
    )
    result = detector.fit(values)
    result_frame = result.get("df") if isinstance(result, dict) else None
    if result_frame is None or "peak" not in result_frame.columns:
        raise RuntimeError("findpeaks did not return the expected result['df']['peak']")

    labels = result_frame["peak"].fillna(False).astype(bool).to_numpy(dtype=np.uint8)
    if labels.shape != values.shape:
        raise RuntimeError(
            f"findpeaks returned {labels.size} labels for {values.size} observations"
        )
    return labels


def validate_existing_labels(
    frame: pd.DataFrame, label_column: str, regenerated: np.ndarray
) -> None:
    """Assert exact equality with a pre-existing binary label column."""
    if label_column not in frame.columns:
        raise ValueError(
            f"cannot verify labels: column {label_column!r} is absent from the input"
        )

    existing_numeric = pd.to_numeric(frame[label_column], errors="coerce")
    if existing_numeric.isna().any() or not existing_numeric.isin([0, 1]).all():
        raise ValueError(f"existing label column {label_column!r} is not binary")

    existing = existing_numeric.to_numpy(dtype=np.uint8)
    differing = np.flatnonzero(existing != regenerated)
    if differing.size:
        preview = ", ".join(map(str, differing[:10]))
        raise ValueError(
            f"regenerated labels differ at {differing.size} rows; "
            f"first differing indices: {preview}"
        )


def package_version() -> str:
    try:
        return version("findpeaks")
    except PackageNotFoundError:
        return "unknown"


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    input_path = args.input_csv.expanduser().resolve()
    output_path = args.output_csv.expanduser().resolve()

    if not input_path.is_file():
        raise FileNotFoundError(f"input CSV does not exist: {input_path}")
    if input_path == output_path and not args.overwrite:
        raise ValueError("input and output paths are identical; add --overwrite to proceed")
    if output_path.exists() and not args.overwrite:
        raise FileExistsError(f"output already exists: {output_path}")

    frame = pd.read_csv(input_path)
    if frame.empty:
        raise ValueError("input CSV is empty")
    if args.timestamp_column:
        validate_timestamps(frame, args.timestamp_column)

    values = load_values(frame, args.value_column)
    labels = detect_structural_peaks(
        values=values,
        lookahead=args.lookahead,
        sensitivity_threshold=args.sensitivity_threshold,
    )
    peak_count = int(labels.sum())

    if args.expected_peaks is not None and peak_count != args.expected_peaks:
        raise ValueError(
            f"expected {args.expected_peaks} peaks, but detected {peak_count}"
        )
    if args.verify_existing_labels:
        validate_existing_labels(frame, args.label_column, labels)

    frame[args.label_column] = labels
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False)

    print(f"findpeaks version: {package_version()}")
    print(f"records: {len(frame)}")
    print(f"lookahead: {args.lookahead}")
    print(f"sensitivity threshold: {args.sensitivity_threshold:g}")
    print(f"detected peaks: {peak_count} ({peak_count / len(frame):.2%})")
    if args.verify_existing_labels:
        print(f"existing {args.label_column!r} labels: exact match")
    print(f"output: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
