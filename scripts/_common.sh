#!/usr/bin/env bash
# Shared settings sourced by every experiment script.
# Source this file from any script under scripts/ and it will switch to the
# repository root automatically.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

export PYTHONUNBUFFERED=1

PYTHON="${PYTHON:-python}"
GPU="${GPU:-0}"
SEEDS="${SEEDS:-5}"           # --itr
EPOCHS="${EPOCHS:-20}"
PATIENCE="${PATIENCE:-5}"
BATCH="${BATCH:-128}"
LR="${LR:-0.001}"
LRADJ="${LRADJ:-type3}"
LOOKAHEAD_WLEL="${LOOKAHEAD_WLEL:-3}"
LOOKAHEAD_ELC="${LOOKAHEAD_ELC:-5}"

WLEL_ROOT=./dataset/load_data/hf_load_data/
WLEL_FILE=hf_load_data_20210101-20250925_mixed_with_peaks_lookahead_3.csv
WLEL_DATA=load_data_mixed

ELC_ROOT=./dataset/electricity
ELC_FILE=electricity_mixed_with_peaks_lookahead_5.csv
ELC_DATA=electricity_mixed

# Both datasets now use the same loss weights: 244 = (V=0.2, P=0.4, T=0.4).
# This matches the run.py defaults, so no explicit override is needed.
# The old ELC-specific (V=0.4, P=0.4, T=0.2) = 424 was deprecated in favour
# of uniform weights across datasets (see TODO.md for justification).
# Kept as comments for reference:
#   OLD: ELC_V=0.4  ELC_P=0.4  ELC_T=0.2   (424, deprecated)
ELC_V=0.2
ELC_P=0.4
ELC_T=0.4

# Per-run timestamped stdout log dir
LOG_DIR="${LOG_DIR:-scripts/logs}"
mkdir -p "$LOG_DIR"
