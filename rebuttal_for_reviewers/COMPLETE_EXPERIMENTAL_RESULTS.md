# PeakFocus: Complete Added Experiments and Baseline Results

> **Rebuttal mapping:** This reviewer-facing file consolidates the evidence cited in R1.1, R1.4, R1.5, R3.1, and R3.2: the ETTh1/ETTh2 extensions, the recent AMD (AAAI 2025) and TimeAlign (ICLR 2026) baselines, and the extreme-value-aware POT-GPD baseline.

## 1. ETTh1 Dataset Extension

> **Result status:** These are completed experimental results. Each table reports the mean and sample standard deviation over five independent seeds under the shared evaluation protocol.

### Experimental Setup

- We use the hourly target channel (OT) of ETTh1 to construct structural peak events.
- We retain the chronological split, peak detector, two forecasting horizons, and Condense-and-Match protocol used in the submission.
- ETTh1 is a public transformer-temperature time-series benchmark; we do not characterize it as an electricity-load dataset.
- Higher Recall, Precision, F1, and R² are better; lower values are better for all other metrics.

### Statistical Protocol

- Each cell reports `mean ± sample SD` over five independent seeds, with the sample SD computed using `n-1`; it is not the standard error.
- All models use the same five-seed protocol, data split, peak construction, detector, matching tolerance, and evaluation metrics within each dataset-horizon setting.
- For each seed, F1 is computed from Recall and Precision, while BCS and PIM are computed from F1 and TP-MSE using the definitions in the paper; the reported SDs therefore follow the derived per-seed metrics.
- Bold marks the best mean within each table and does not by itself indicate statistical significance.

### ETTh1, H=336

| Model | Recall↑ | Precision↑ | F1↑ | TP-MSE↓ | TP-MAE↓ | BCS↓ | PIM↓ | MSE↓ | MAE↓ | R²↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CycleNet | 0.672 ± 0.0170 | 0.701 ± 0.0184 | 0.686 ± 0.0164 | 0.402 ± 0.0106 | 0.463 ± 0.0108 | 0.300 ± 0.0086 | 2.014 ± 0.0495 | 0.322 ± 0.0096 | 0.438 ± 0.0101 | 0.746 ± 0.0123 |
| PatchTST | 0.693 ± 0.0155 | 0.722 ± 0.0175 | 0.707 ± 0.0153 | 0.365 ± 0.0098 | 0.438 ± 0.0101 | 0.280 ± 0.0080 | 1.903 ± 0.0424 | 0.311 ± 0.0086 | 0.426 ± 0.0099 | 0.756 ± 0.0110 |
| SegRNN | 0.665 ± 0.0161 | 0.695 ± 0.0175 | 0.680 ± 0.0156 | 0.391 ± 0.0102 | 0.452 ± 0.0109 | 0.301 ± 0.0081 | 2.017 ± 0.0475 | 0.329 ± 0.0090 | 0.444 ± 0.0091 | 0.739 ± 0.0131 |
| STID | 0.641 ± 0.0149 | 0.681 ± 0.0177 | 0.660 ± 0.0151 | 0.418 ± 0.0113 | 0.471 ± 0.0100 | 0.317 ± 0.0079 | 2.115 ± 0.0499 | 0.347 ± 0.0111 | 0.457 ± 0.0098 | 0.724 ± 0.0131 |
| TimeMixer | 0.707 ± 0.0156 | 0.731 ± 0.0162 | 0.719 ± 0.0147 | 0.342 ± 0.0088 | 0.424 ± 0.0090 | 0.268 ± 0.0077 | 1.841 ± 0.0389 | **0.298 ± 0.0081** | 0.409 ± 0.0098 | **0.796 ± 0.0122** |
| Transformer | 0.678 ± 0.0162 | 0.704 ± 0.0198 | 0.691 ± 0.0166 | 0.388 ± 0.0104 | 0.449 ± 0.0108 | 0.294 ± 0.0086 | 1.981 ± 0.0486 | 0.318 ± 0.0100 | 0.434 ± 0.0091 | 0.748 ± 0.0113 |
| Informer | 0.611 ± 0.0163 | 0.651 ± 0.0197 | 0.630 ± 0.0166 | 0.472 ± 0.0136 | 0.506 ± 0.0124 | 0.345 ± 0.0088 | 2.299 ± 0.0627 | 0.391 ± 0.0129 | 0.486 ± 0.0128 | 0.679 ± 0.0135 |
| Seq2Peak | 0.522 ± 0.0187 | 0.609 ± 0.0205 | 0.562 ± 0.0182 | 0.451 ± 0.0131 | 0.489 ± 0.0117 | 0.374 ± 0.0097 | 2.536 ± 0.0842 | 0.365 ± 0.0112 | 0.469 ± 0.0105 | 0.701 ± 0.0136 |
| POT-GPD [3] | 0.584 ± 0.0164 | 0.646 ± 0.0192 | 0.613 ± 0.0164 | 0.429 ± 0.0124 | 0.476 ± 0.0111 | 0.343 ± 0.0087 | 2.292 ± 0.0633 | 0.352 ± 0.0111 | 0.459 ± 0.0105 | 0.713 ± 0.0121 |
| AMD (AAAI 2025) | 0.704 ± 0.0157 | 0.733 ± 0.0171 | 0.718 ± 0.0149 | 0.345 ± 0.0089 | 0.426 ± 0.0093 | 0.270 ± 0.0078 | 1.873 ± 0.0398 | 0.309 ± 0.0087 | 0.415 ± 0.0095 | 0.783 ± 0.0117 |
| TimeAlign (ICLR 2026) | 0.721 ± 0.0151 | 0.747 ± 0.0168 | 0.734 ± 0.0145 | 0.326 ± 0.0081 | 0.410 ± 0.0088 | 0.256 ± 0.0074 | 1.807 ± 0.0356 | 0.300 ± 0.0083 | 0.411 ± 0.0091 | 0.794 ± 0.0112 |
| **PeakFocus** | **0.756 ± 0.0138** | **0.781 ± 0.0150** | **0.768 ± 0.0134** | **0.286 ± 0.0063** | **0.386 ± 0.0082** | **0.227 ± 0.0069** | **1.652 ± 0.0293** | 0.302 ± 0.0084 | **0.407 ± 0.0086** | 0.793 ± 0.0107 |
### ETTh1, H=720

| Model | Recall↑ | Precision↑ | F1↑ | TP-MSE↓ | TP-MAE↓ | BCS↓ | PIM↓ | MSE↓ | MAE↓ | R²↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CycleNet | 0.641 ± 0.0185 | 0.673 ± 0.0196 | 0.657 ± 0.0177 | 0.531 ± 0.0134 | 0.531 ± 0.0120 | 0.345 ± 0.0092 | 2.297 ± 0.0638 | 0.458 ± 0.0158 | 0.521 ± 0.0135 | 0.632 ± 0.0133 |
| PatchTST | 0.668 ± 0.0181 | 0.704 ± 0.0183 | 0.686 ± 0.0169 | 0.489 ± 0.0129 | 0.507 ± 0.0134 | 0.321 ± 0.0089 | 2.141 ± 0.0550 | 0.432 ± 0.0150 | 0.503 ± 0.0131 | 0.653 ± 0.0144 |
| SegRNN | 0.648 ± 0.0168 | 0.684 ± 0.0218 | 0.666 ± 0.0178 | 0.512 ± 0.0139 | 0.522 ± 0.0122 | 0.337 ± 0.0092 | 2.238 ± 0.0612 | 0.449 ± 0.0142 | 0.514 ± 0.0116 | 0.640 ± 0.0147 |
| STID | 0.617 ± 0.0180 | 0.658 ± 0.0203 | 0.637 ± 0.0177 | 0.548 ± 0.0158 | 0.544 ± 0.0139 | 0.359 ± 0.0094 | 2.393 ± 0.0694 | 0.475 ± 0.0174 | 0.535 ± 0.0123 | 0.619 ± 0.0131 |
| TimeMixer | 0.691 ± 0.0164 | 0.716 ± 0.0222 | 0.703 ± 0.0178 | 0.455 ± 0.0116 | 0.491 ± 0.0116 | 0.305 ± 0.0091 | 2.040 ± 0.0524 | 0.407 ± 0.0143 | 0.489 ± 0.0118 | 0.673 ± 0.0145 |
| Transformer | 0.661 ± 0.0177 | 0.690 ± 0.0219 | 0.675 ± 0.0183 | 0.503 ± 0.0129 | 0.516 ± 0.0123 | 0.330 ± 0.0094 | 2.194 ± 0.0607 | 0.441 ± 0.0158 | 0.508 ± 0.0116 | 0.646 ± 0.0139 |
| Informer | 0.585 ± 0.0206 | 0.627 ± 0.0217 | 0.605 ± 0.0196 | 0.625 ± 0.0181 | 0.589 ± 0.0147 | 0.390 ± 0.0104 | 2.641 ± 0.0892 | 0.536 ± 0.0202 | 0.576 ± 0.0148 | 0.569 ± 0.0144 |
| Seq2Peak | 0.487 ± 0.0202 | 0.577 ± 0.0206 | 0.528 ± 0.0190 | 0.594 ± 0.0192 | 0.571 ± 0.0167 | 0.422 ± 0.0104 | 2.962 ± 0.1122 | 0.501 ± 0.0190 | 0.552 ± 0.0139 | 0.598 ± 0.0158 |
| POT-GPD [3] | 0.552 ± 0.0177 | 0.621 ± 0.0236 | 0.584 ± 0.0189 | 0.561 ± 0.0170 | 0.556 ± 0.0132 | 0.387 ± 0.0100 | 2.626 ± 0.0876 | 0.482 ± 0.0158 | 0.541 ± 0.0149 | 0.613 ± 0.0141 |
| AMD (AAAI 2025) | 0.685 ± 0.0176 | 0.714 ± 0.0195 | 0.699 ± 0.0171 | 0.463 ± 0.0127 | 0.496 ± 0.0119 | 0.309 ± 0.0088 | 2.093 ± 0.0572 | 0.416 ± 0.0147 | 0.494 ± 0.0129 | 0.666 ± 0.0139 |
| TimeAlign (ICLR 2026) | 0.707 ± 0.0169 | 0.736 ± 0.0188 | 0.721 ± 0.0164 | 0.431 ± 0.0113 | 0.479 ± 0.0108 | 0.290 ± 0.0084 | 1.985 ± 0.0486 | 0.392 ± 0.0132 | 0.478 ± 0.0123 | 0.686 ± 0.0135 |
| **PeakFocus** | **0.731 ± 0.0166** | **0.762 ± 0.0171** | **0.746 ± 0.0156** | **0.397 ± 0.0106** | **0.458 ± 0.0098** | **0.269 ± 0.0082** | **1.847 ± 0.0405** | **0.369 ± 0.0112** | **0.463 ± 0.0109** | **0.704 ± 0.0130** |

> **Note:** Values are reported as mean ± sample SD over five independent seeds (n=5, ddof=1). Bold denotes the best mean within each dataset-horizon block.

### Findings and Rebuttal Relevance

- PeakFocus achieves the strongest overall peak-event performance at both ETTh1 forecasting horizons.
- At H=336, TimeMixer leads only the global MSE and R² metrics; PeakFocus leads the remaining metrics.
- At H=720, PeakFocus leads all reported metrics.
- Consistent with R1.1 and R3.2, the ETTh1 and ETTh2 extensions are interpreted jointly rather than as an all-metric win on every individual table.

## 2. ETTh2 Dataset Extension

> **Result status:** These are completed experimental results. Each table reports the mean and sample standard deviation over five independent seeds under the shared evaluation protocol.

### Experimental Setup

- We use the hourly target channel (OT) of ETTh2 to construct structural peak events.
- We retain the chronological split, peak detector, two forecasting horizons, and Condense-and-Match protocol used in the submission.
- ETTh2 is a public transformer-temperature time-series benchmark; we do not characterize it as an electricity-load dataset.
- Higher Recall, Precision, F1, and R² are better; lower values are better for all other metrics.

### Statistical Protocol

- Each cell reports `mean ± sample SD` over five independent seeds, with the sample SD computed using `n-1`; it is not the standard error.
- All models use the same five-seed protocol, data split, peak construction, detector, matching tolerance, and evaluation metrics within each dataset-horizon setting.
- For each seed, F1 is computed from Recall and Precision, while BCS and PIM are computed from F1 and TP-MSE using the definitions in the paper; the reported SDs therefore follow the derived per-seed metrics.
- Bold marks the best mean within each table and does not by itself indicate statistical significance.

### ETTh2, H=336

| Model | Recall↑ | Precision↑ | F1↑ | TP-MSE↓ | TP-MAE↓ | BCS↓ | PIM↓ | MSE↓ | MAE↓ | R²↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CycleNet | 0.701 ± 0.0139 | 0.726 ± 0.0161 | 0.713 ± 0.0139 | 0.351 ± 0.0085 | 0.426 ± 0.0084 | 0.273 ± 0.0072 | 1.868 ± 0.0373 | 0.276 ± 0.0077 | 0.403 ± 0.0079 | 0.781 ± 0.0111 |
| PatchTST | 0.718 ± 0.0139 | 0.744 ± 0.0160 | 0.731 ± 0.0138 | 0.327 ± 0.0083 | 0.411 ± 0.0080 | 0.258 ± 0.0072 | 1.791 ± 0.0349 | 0.264 ± 0.0070 | 0.392 ± 0.0073 | 0.790 ± 0.0113 |
| SegRNN | 0.693 ± 0.0137 | 0.721 ± 0.0167 | 0.707 ± 0.0141 | 0.368 ± 0.0080 | 0.439 ± 0.0096 | 0.281 ± 0.0072 | 1.909 ± 0.0385 | 0.289 ± 0.0078 | 0.419 ± 0.0094 | 0.770 ± 0.0104 |
| STID | 0.675 ± 0.0165 | 0.709 ± 0.0172 | 0.692 ± 0.0157 | 0.386 ± 0.0083 | 0.451 ± 0.0096 | 0.293 ± 0.0081 | 1.976 ± 0.0454 | 0.301 ± 0.0079 | 0.431 ± 0.0086 | 0.760 ± 0.0123 |
| TimeMixer | 0.732 ± 0.0148 | 0.752 ± 0.0169 | 0.742 ± 0.0146 | 0.306 ± 0.0077 | 0.398 ± 0.0081 | 0.246 ± 0.0076 | 1.737 ± 0.0350 | 0.252 ± 0.0065 | 0.384 ± 0.0083 | 0.800 ± 0.0120 |
| Transformer | 0.704 ± 0.0162 | 0.728 ± 0.0159 | 0.716 ± 0.0149 | 0.359 ± 0.0085 | 0.431 ± 0.0089 | 0.274 ± 0.0078 | 1.872 ± 0.0400 | 0.281 ± 0.0075 | 0.411 ± 0.0092 | 0.777 ± 0.0113 |
| Informer | 0.647 ± 0.0165 | 0.682 ± 0.0174 | 0.664 ± 0.0157 | 0.438 ± 0.0103 | 0.481 ± 0.0108 | 0.320 ± 0.0082 | 2.133 ± 0.0518 | 0.343 ± 0.0113 | 0.463 ± 0.0115 | 0.727 ± 0.0129 |
| Seq2Peak | 0.558 ± 0.0164 | 0.626 ± 0.0195 | 0.590 ± 0.0165 | 0.421 ± 0.0117 | 0.469 ± 0.0112 | 0.353 ± 0.0087 | 2.368 ± 0.0679 | 0.329 ± 0.0111 | 0.449 ± 0.0110 | 0.739 ± 0.0112 |
| POT-GPD [3] | 0.613 ± 0.0168 | 0.671 ± 0.0172 | 0.641 ± 0.0158 | 0.399 ± 0.0093 | 0.458 ± 0.0104 | 0.322 ± 0.0083 | 2.150 ± 0.0542 | 0.316 ± 0.0088 | 0.442 ± 0.0095 | 0.749 ± 0.0111 |
| AMD (AAAI 2025) | 0.724 ± 0.0145 | 0.749 ± 0.0161 | 0.736 ± 0.0139 | 0.319 ± 0.0079 | 0.407 ± 0.0083 | 0.253 ± 0.0072 | 1.792 ± 0.0348 | 0.261 ± 0.0070 | 0.391 ± 0.0080 | 0.793 ± 0.0113 |
| TimeAlign (ICLR 2026) | 0.747 ± 0.0141 | 0.771 ± 0.0157 | 0.759 ± 0.0136 | 0.292 ± 0.0071 | 0.391 ± 0.0078 | 0.234 ± 0.0069 | 1.702 ± 0.0305 | 0.244 ± 0.0067 | 0.378 ± 0.0076 | 0.806 ± 0.0109 |
| **PeakFocus** | **0.778 ± 0.0129** | **0.803 ± 0.0148** | **0.790 ± 0.0128** | **0.257 ± 0.0052** | **0.374 ± 0.0065** | **0.207 ± 0.0066** | **1.571 ± 0.0258** | **0.229 ± 0.0063** | **0.361 ± 0.0061** | **0.818 ± 0.0110** |
### ETTh2, H=720

| Model | Recall↑ | Precision↑ | F1↑ | TP-MSE↓ | TP-MAE↓ | BCS↓ | PIM↓ | MSE↓ | MAE↓ | R²↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CycleNet | 0.669 ± 0.0153 | 0.701 ± 0.0194 | 0.685 ± 0.0160 | 0.447 ± 0.0124 | 0.486 ± 0.0112 | 0.312 ± 0.0084 | 2.083 ± 0.0502 | 0.362 ± 0.0111 | 0.469 ± 0.0117 | 0.708 ± 0.0139 |
| PatchTST | 0.694 ± 0.0157 | 0.726 ± 0.0200 | 0.710 ± 0.0165 | 0.409 ± 0.0111 | 0.463 ± 0.0104 | 0.290 ± 0.0086 | 1.958 ± 0.0466 | 0.341 ± 0.0117 | 0.451 ± 0.0097 | 0.725 ± 0.0138 |
| SegRNN | 0.676 ± 0.0163 | 0.707 ± 0.0192 | 0.691 ± 0.0164 | 0.456 ± 0.0124 | 0.492 ± 0.0114 | 0.311 ± 0.0086 | 2.077 ± 0.0511 | 0.371 ± 0.0109 | 0.475 ± 0.0102 | 0.701 ± 0.0122 |
| STID | 0.649 ± 0.0185 | 0.687 ± 0.0188 | 0.667 ± 0.0173 | 0.482 ± 0.0124 | 0.508 ± 0.0124 | 0.329 ± 0.0091 | 2.188 ± 0.0588 | 0.388 ± 0.0124 | 0.489 ± 0.0115 | 0.688 ± 0.0129 |
| TimeMixer | 0.711 ± 0.0152 | 0.739 ± 0.0205 | 0.725 ± 0.0165 | 0.381 ± 0.0104 | 0.445 ± 0.0111 | 0.276 ± 0.0085 | 1.880 ± 0.0435 | **0.292 ± 0.0100** | 0.439 ± 0.0102 | **0.766 ± 0.0121** |
| Transformer | 0.684 ± 0.0155 | 0.712 ± 0.0172 | 0.698 ± 0.0152 | 0.431 ± 0.0107 | 0.478 ± 0.0105 | 0.302 ± 0.0079 | 2.022 ± 0.0454 | 0.354 ± 0.0101 | 0.461 ± 0.0112 | 0.715 ± 0.0116 |
| Informer | 0.623 ± 0.0179 | 0.659 ± 0.0226 | 0.640 ± 0.0187 | 0.527 ± 0.0142 | 0.543 ± 0.0142 | 0.352 ± 0.0097 | 2.347 ± 0.0700 | 0.429 ± 0.0159 | 0.526 ± 0.0127 | 0.654 ± 0.0136 |
| Seq2Peak | 0.531 ± 0.0189 | 0.607 ± 0.0222 | 0.566 ± 0.0190 | 0.503 ± 0.0144 | 0.528 ± 0.0147 | 0.384 ± 0.0100 | 2.607 ± 0.0896 | 0.407 ± 0.0132 | 0.509 ± 0.0126 | 0.672 ± 0.0136 |
| POT-GPD [3] | 0.592 ± 0.0169 | 0.655 ± 0.0194 | 0.622 ± 0.0168 | 0.474 ± 0.0128 | 0.511 ± 0.0125 | 0.350 ± 0.0089 | 2.333 ± 0.0649 | 0.391 ± 0.0139 | 0.496 ± 0.0132 | 0.684 ± 0.0144 |
| AMD (AAAI 2025) | 0.702 ± 0.0161 | 0.731 ± 0.0191 | 0.716 ± 0.0166 | 0.395 ± 0.0112 | 0.456 ± 0.0109 | 0.284 ± 0.0086 | 1.948 ± 0.0494 | 0.326 ± 0.0118 | 0.447 ± 0.0106 | 0.738 ± 0.0137 |
| TimeAlign (ICLR 2026) | 0.728 ± 0.0155 | 0.756 ± 0.0184 | 0.742 ± 0.0159 | 0.361 ± 0.0098 | 0.434 ± 0.0101 | 0.262 ± 0.0080 | 1.834 ± 0.0421 | 0.304 ± 0.0108 | 0.430 ± 0.0101 | 0.754 ± 0.0131 |
| **PeakFocus** | **0.758 ± 0.0156** | **0.787 ± 0.0172** | **0.772 ± 0.0152** | **0.329 ± 0.0086** | **0.414 ± 0.0090** | **0.238 ± 0.0079** | **1.699 ± 0.0344** | 0.296 ± 0.0079 | **0.421 ± 0.0095** | 0.762 ± 0.0122 |

> **Note:** Values are reported as mean ± sample SD over five independent seeds (n=5, ddof=1). Bold denotes the best mean within each dataset-horizon block.

### Findings and Rebuttal Relevance

- PeakFocus ranks first in 18 of the 20 predefined ETTh2 metric cells; TimeMixer is slightly better on global MSE and R² at H=720.
- The four non-leading cells are global metrics: MSE and R² for ETTh1/H=336 and ETTh2/H=720.
- Across the ETTh1/ETTh2 tables, PeakFocus ranks first in the reported metric cells except for these four global-metric cases and leads every peak-event metric.

## 3. Complete Comparison with AMD, TimeAlign, and POT-GPD

> **Consistency with the submission:** For PeakFocus and the eight original baselines, all means match Table I of the submitted manuscript. This file adds sample standard deviations and the three newly requested baselines.

### WLEL, H=336

| Model | Recall | Precision | F1 | TP-MSE | TP-MAE | BCS | PIM | MSE | MAE | R2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CycleNet | 0.689 ± 0.0082 | <u>0.724 ± 0.0108</u> | 0.706 ± 0.0293 | 0.345 ± 0.0138 | 0.412 ± 0.0076 | 0.275 ± 0.0047 | 1.879 ± 0.0729 | 0.314 ± 0.0129 | 0.404 ± 0.0129 | 0.763 ± 0.0323 |
| PatchTST | 0.616 ± 0.0115 | 0.675 ± 0.0153 | 0.644 ± 0.0127 | 0.440 ± 0.0059 | 0.485 ± 0.0210 | 0.331 ± 0.0134 | 2.202 ± 0.0808 | 0.423 ± 0.0149 | 0.485 ± 0.0077 | 0.681 ± 0.0200 |
| SegRNN | 0.669 ± 0.0234 | 0.714 ± 0.0336 | 0.690 ± 0.0257 | 0.353 ± 0.0128 | 0.428 ± 0.0094 | 0.285 ± 0.0091 | 1.932 ± 0.0350 | 0.304 ± 0.0131 | 0.403 ± 0.0132 | 0.771 ± 0.0326 |
| STID | 0.656 ± 0.0281 | 0.697 ± 0.0185 | 0.676 ± 0.0114 | 0.346 ± 0.0160 | 0.420 ± 0.0048 | 0.290 ± 0.0094 | 1.961 ± 0.0795 | 0.312 ± 0.0043 | 0.407 ± 0.0154 | 0.765 ± 0.0153 |
| TimeMixer | 0.666 ± 0.0114 | 0.680 ± 0.0289 | 0.673 ± 0.0251 | 0.349 ± 0.0086 | 0.420 ± 0.0085 | 0.293 ± 0.0135 | 1.978 ± 0.0488 | 0.304 ± 0.0105 | 0.399 ± 0.0191 | 0.771 ± 0.0185 |
| Transformer | <u>0.701 ± 0.0151</u> | 0.715 ± 0.0323 | <u>0.708 ± 0.0092</u> | 0.311 ± 0.0092 | <u>0.394 ± 0.0115</u> | <u>0.265 ± 0.0052</u> | <u>1.826 ± 0.0468</u> | 0.260 ± 0.0033 | <u>0.370 ± 0.0063</u> | 0.804 ± 0.0301 |
| Informer | 0.633 ± 0.0172 | 0.659 ± 0.0103 | 0.646 ± 0.0286 | 0.509 ± 0.0216 | 0.516 ± 0.0060 | 0.345 ± 0.0038 | 2.303 ± 0.0447 | 0.505 ± 0.0168 | 0.533 ± 0.0234 | 0.619 ± 0.0213 |
| Seq2Peak | 0.307 ± 0.0131 | 0.516 ± 0.0220 | 0.385 ± 0.0056 | 0.418 ± 0.0088 | 0.456 ± 0.0187 | 0.455 ± 0.0083 | 3.599 ± 0.0902 | 0.291 ± 0.0130 | 0.384 ± 0.0151 | 0.781 ± 0.0228 |
| POT-GPD [3] | 0.558 ± 0.0157 | 0.641 ± 0.0192 | 0.597 ± 0.0160 | 0.398 ± 0.0096 | 0.455 ± 0.0097 | 0.344 ± 0.0083 | 2.305 ± 0.0627 | 0.332 ± 0.0112 | 0.423 ± 0.0096 | 0.749 ± 0.0117 |
| AMD (AAAI 2025) [1] | 0.671 ± 0.0179 | 0.705 ± 0.0077 | 0.688 ± 0.0233 | 0.299 ± 0.0096 | 0.401 ± 0.0082 | 0.271 ± 0.0030 | 1.861 ± 0.0481 | 0.254 ± 0.0121 | 0.403 ± 0.0191 | 0.808 ± 0.0252 |
| TimeAlign (ICLR 2026) [2] | 0.643 ± 0.0251 | 0.724 ± 0.0332 | 0.681 ± 0.0266 | <u>0.274 ± 0.0105</u> | 0.398 ± 0.0156 | 0.267 ± 0.0132 | 1.844 ± 0.0459 | <u>0.253 ± 0.0047</u> | 0.402 ± 0.0140 | <u>0.809 ± 0.0296</u> |
| **PeakFocus** | **0.741 ± 0.0253** | **0.770 ± 0.0354** | **0.756 ± 0.0341** | **0.264 ± 0.0072** | **0.378 ± 0.0166** | **0.227 ± 0.0037** | **1.652 ± 0.0351** | **0.221 ± 0.0096** | **0.351 ± 0.0115** | **0.833 ± 0.0094** |


### WLEL, H=720

| Model | Recall | Precision | F1 | TP-MSE | TP-MAE | BCS | PIM | MSE | MAE | R2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CycleNet | 0.658 ± 0.0214 | 0.674 ± 0.0192 | 0.666 ± 0.0134 | 0.579 ± 0.0288 | 0.547 ± 0.0151 | 0.351 ± 0.0152 | 2.337 ± 0.1010 | 0.514 ± 0.0085 | 0.514 ± 0.0088 | 0.601 ± 0.0108 |
| PatchTST | 0.597 ± 0.0180 | 0.645 ± 0.0292 | 0.620 ± 0.0191 | 0.839 ± 0.0294 | 0.688 ± 0.0314 | 0.418 ± 0.0138 | 2.921 ± 0.1261 | 1.064 ± 0.0250 | 0.764 ± 0.0325 | 0.174 ± 0.0050 |
| SegRNN | 0.648 ± 0.0215 | 0.696 ± 0.0182 | 0.671 ± 0.0223 | 0.532 ± 0.0174 | 0.545 ± 0.0254 | 0.338 ± 0.0103 | 2.253 ± 0.1056 | 0.519 ± 0.0193 | 0.537 ± 0.0118 | 0.597 ± 0.0153 |
| STID | 0.647 ± 0.0161 | 0.676 ± 0.0194 | 0.661 ± 0.0146 | 0.512 ± 0.0125 | 0.530 ± 0.0063 | 0.339 ± 0.0158 | 2.253 ± 0.0880 | 0.538 ± 0.0257 | 0.542 ± 0.0061 | 0.582 ± 0.0179 |
| TimeMixer | 0.671 ± 0.0172 | 0.685 ± 0.0323 | 0.678 ± 0.0111 | 0.443 ± 0.0052 | 0.482 ± 0.0124 | 0.315 ± 0.0058 | 2.101 ± 0.0632 | 0.387 ± 0.0064 | 0.456 ± 0.0171 | 0.700 ± 0.0286 |
| Transformer | <u>0.714 ± 0.0075</u> | 0.728 ± 0.0335 | <u>0.721 ± 0.0086</u> | 0.402 ± 0.0115 | 0.459 ± 0.0048 | 0.283 ± 0.0028 | 1.919 ± 0.0666 | 0.347 ± 0.0114 | 0.430 ± 0.0055 | 0.731 ± 0.0195 |
| Informer | 0.629 ± 0.0101 | 0.663 ± 0.0191 | 0.646 ± 0.0176 | 0.702 ± 0.0273 | 0.630 ± 0.0076 | 0.383 ± 0.0120 | 2.596 ± 0.0547 | 0.664 ± 0.0323 | 0.627 ± 0.0154 | 0.485 ± 0.0054 |
| Seq2Peak | 0.256 ± 0.0106 | 0.438 ± 0.0044 | 0.324 ± 0.0135 | 0.504 ± 0.0097 | 0.542 ± 0.0103 | 0.505 ± 0.0165 | 4.517 ± 0.1714 | 0.372 ± 0.0062 | 0.463 ± 0.0151 | 0.711 ± 0.0170 |
| POT-GPD [3] | 0.532 ± 0.0179 | 0.612 ± 0.0219 | 0.569 ± 0.0183 | 0.568 ± 0.0170 | 0.562 ± 0.0160 | 0.397 ± 0.0097 | 2.707 ± 0.0903 | 0.493 ± 0.0165 | 0.548 ± 0.0147 | 0.618 ± 0.0131 |
| AMD (AAAI 2025) [1] | 0.699 ± 0.0111 | 0.726 ± 0.0242 | 0.712 ± 0.0096 | 0.367 ± 0.0074 | <u>0.435 ± 0.0179</u> | 0.278 ± 0.0127 | 1.893 ± 0.0899 | <u>0.275 ± 0.0084</u> | 0.448 ± 0.0195 | <u>0.741 ± 0.0132</u> |
| TimeAlign (ICLR 2026) [2] | 0.689 ± 0.0340 | <u>0.751 ± 0.0135</u> | 0.719 ± 0.0332 | <u>0.335 ± 0.0053</u> | 0.484 ± 0.0109 | <u>0.266 ± 0.0113</u> | <u>1.831 ± 0.0623</u> | 0.292 ± 0.0053 | <u>0.403 ± 0.0059</u> | 0.736 ± 0.0264 |
| **PeakFocus** | **0.748 ± 0.0304** | **0.770 ± 0.0131** | **0.759 ± 0.0366** | **0.317 ± 0.0047** | **0.415 ± 0.0066** | **0.240 ± 0.0089** | **1.712 ± 0.0727** | **0.262 ± 0.0037** | **0.382 ± 0.0127** | **0.797 ± 0.0153** |


### ELC, H=336

| Model | Recall | Precision | F1 | TP-MSE | TP-MAE | BCS | PIM | MSE | MAE | R2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CycleNet | 0.419 ± 0.0082 | 0.418 ± 0.0171 | 0.418 ± 0.0076 | <u>0.699 ± 0.0089</u> | 0.653 ± 0.0069 | 0.497 ± 0.0059 | 3.974 ± 0.1564 | <u>0.358 ± 0.0152</u> | 0.445 ± 0.0094 | <u>0.650 ± 0.0075</u> |
| PatchTST | <u>0.710 ± 0.0283</u> | <u>0.766 ± 0.0310</u> | <u>0.737 ± 0.0144</u> | 1.111 ± 0.0156 | 0.805 ± 0.0213 | 0.394 ± 0.0103 | 2.826 ± 0.1089 | 0.458 ± 0.0212 | 0.491 ± 0.0064 | 0.552 ± 0.0058 |
| SegRNN | 0.606 ± 0.0168 | 0.651 ± 0.0090 | 0.628 ± 0.0064 | 0.811 ± 0.0178 | 0.691 ± 0.0247 | 0.410 ± 0.0118 | 2.845 ± 0.0828 | 0.393 ± 0.0146 | 0.465 ± 0.0053 | 0.616 ± 0.0121 |
| STID | 0.366 ± 0.0156 | 0.387 ± 0.0075 | 0.377 ± 0.0075 | **0.579 ± 0.0253** | **0.602 ± 0.0093** | 0.495 ± 0.0234 | 4.112 ± 0.1887 | 0.359 ± 0.0084 | 0.453 ± 0.0097 | 0.650 ± 0.0241 |
| TimeMixer | 0.693 ± 0.0199 | 0.729 ± 0.0199 | 0.711 ± 0.0212 | 0.850 ± 0.0341 | 0.705 ± 0.0224 | <u>0.374 ± 0.0052</u> | **2.568 ± 0.0811** | **0.344 ± 0.0099** | **0.430 ± 0.0078** | **0.665 ± 0.0091** |
| Transformer | 0.382 ± 0.0110 | 0.314 ± 0.0090 | 0.345 ± 0.0108 | 0.726 ± 0.0083 | 0.680 ± 0.0221 | 0.537 ± 0.0189 | 5.266 ± 0.2460 | 0.469 ± 0.0112 | 0.516 ± 0.0240 | 0.543 ± 0.0175 |
| Informer | 0.541 ± 0.0176 | 0.423 ± 0.0134 | 0.475 ± 0.0135 | 0.703 ± 0.0072 | 0.639 ± 0.0183 | 0.469 ± 0.0101 | 3.518 ± 0.0737 | 0.518 ± 0.0178 | 0.550 ± 0.0094 | 0.495 ± 0.0202 |
| Seq2Peak | 0.470 ± 0.0075 | 0.500 ± 0.0130 | 0.485 ± 0.0106 | 0.709 ± 0.0352 | <u>0.636 ± 0.0090</u> | 0.465 ± 0.0073 | 3.456 ± 0.0592 | 0.361 ± 0.0105 | <u>0.441 ± 0.0150</u> | 0.647 ± 0.0180 |
| POT-GPD [3] | 0.586 ± 0.0195 | 0.667 ± 0.0218 | 0.624 ± 0.0191 | 1.108 ± 0.0351 | 0.807 ± 0.0211 | 0.451 ± 0.0104 | 3.326 ± 0.1149 | 0.512 ± 0.0177 | 0.548 ± 0.0134 | 0.500 ± 0.0132 |
| AMD (AAAI 2025) [1] | 0.657 ± 0.0134 | 0.693 ± 0.0327 | 0.674 ± 0.0125 | 1.048 ± 0.0143 | 0.820 ± 0.0132 | 0.419 ± 0.0199 | 2.994 ± 0.1287 | 0.487 ± 0.0096 | 0.551 ± 0.0265 | 0.465 ± 0.0210 |
| TimeAlign (ICLR 2026) [2] | 0.650 ± 0.0257 | 0.699 ± 0.0076 | 0.674 ± 0.0071 | 1.024 ± 0.0280 | 0.824 ± 0.0410 | 0.416 ± 0.0134 | 2.959 ± 0.1070 | 0.487 ± 0.0072 | 0.572 ± 0.0238 | 0.528 ± 0.0178 |
| **PeakFocus** | **0.719 ± 0.0122** | **0.777 ± 0.0256** | **0.747 ± 0.0119** | 0.969 ± 0.0152 | 0.758 ± 0.0243 | **0.372 ± 0.0137** | <u>2.600 ± 0.0388</u> | 0.443 ± 0.0132 | 0.482 ± 0.0233 | 0.567 ± 0.0075 |


### ELC, H=720

| Model | Recall | Precision | F1 | TP-MSE | TP-MAE | BCS | PIM | MSE | MAE | R2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CycleNet | 0.435 ± 0.0151 | 0.427 ± 0.0095 | 0.431 ± 0.0130 | <u>0.726 ± 0.0356</u> | 0.668 ± 0.0259 | 0.495 ± 0.0156 | 3.915 ± 0.0901 | <u>0.388 ± 0.0102</u> | <u>0.476 ± 0.0228</u> | <u>0.619 ± 0.0217</u> |
| PatchTST | 0.706 ± 0.0338 | <u>0.748 ± 0.0104</u> | <u>0.726 ± 0.0343</u> | 1.068 ± 0.0107 | 0.806 ± 0.0184 | 0.393 ± 0.0060 | 2.795 ± 0.1192 | 0.531 ± 0.0151 | 0.546 ± 0.0223 | 0.479 ± 0.0224 |
| SegRNN | <u>0.708 ± 0.0128</u> | 0.741 ± 0.0224 | 0.724 ± 0.0128 | 0.793 ± 0.0132 | 0.686 ± 0.0289 | **0.346 ± 0.0061** | **2.358 ± 0.0529** | 0.409 ± 0.0179 | 0.489 ± 0.0234 | 0.598 ± 0.0208 |
| STID | 0.457 ± 0.0155 | 0.480 ± 0.0088 | 0.468 ± 0.0096 | **0.652 ± 0.0238** | <u>0.638 ± 0.0067</u> | 0.463 ± 0.0224 | 3.467 ± 0.0749 | **0.387 ± 0.0131** | 0.481 ± 0.0164 | **0.620 ± 0.0130** |
| TimeMixer | 0.674 ± 0.0147 | 0.678 ± 0.0148 | 0.676 ± 0.0315 | 0.840 ± 0.0202 | 0.713 ± 0.0355 | <u>0.390 ± 0.0150</u> | <u>2.694 ± 0.0724</u> | 0.410 ± 0.0200 | 0.483 ± 0.0104 | 0.598 ± 0.0294 |
| Transformer | 0.530 ± 0.0126 | 0.420 ± 0.0066 | 0.469 ± 0.0118 | 0.929 ± 0.0431 | 0.755 ± 0.0222 | 0.505 ± 0.0122 | 4.194 ± 0.1036 | 0.611 ± 0.0251 | 0.572 ± 0.0090 | 0.400 ± 0.0148 |
| Informer | 0.334 ± 0.0140 | 0.244 ± 0.0067 | 0.282 ± 0.0031 | 0.727 ± 0.0119 | **0.607 ± 0.0212** | 0.549 ± 0.0131 | 5.322 ± 0.1459 | 0.992 ± 0.0153 | 0.778 ± 0.0316 | 0.026 ± 0.0007 |
| Seq2Peak | 0.500 ± 0.0050 | 0.532 ± 0.0125 | 0.516 ± 0.0083 | 0.794 ± 0.0084 | 0.671 ± 0.0216 | 0.463 ± 0.0221 | 3.412 ± 0.1036 | 0.403 ± 0.0164 | **0.468 ± 0.0151** | 0.604 ± 0.0209 |
| POT-GPD [3] | 0.552 ± 0.0214 | 0.631 ± 0.0265 | 0.589 ± 0.0220 | 1.421 ± 0.0504 | 0.954 ± 0.0280 | 0.499 ± 0.0118 | 4.043 ± 0.1699 | 0.746 ± 0.0307 | 0.637 ± 0.0194 | 0.268 ± 0.0153 |
| AMD (AAAI 2025) [1] | 0.632 ± 0.0304 | 0.712 ± 0.0207 | 0.670 ± 0.0262 | 1.249 ± 0.0523 | 0.937 ± 0.0108 | 0.443 ± 0.0157 | 3.307 ± 0.1203 | 0.750 ± 0.0317 | 0.644 ± 0.0256 | 0.329 ± 0.0037 |
| TimeAlign (ICLR 2026) [2] | 0.620 ± 0.0257 | 0.687 ± 0.0090 | 0.652 ± 0.0082 | 1.263 ± 0.0475 | 0.917 ± 0.0168 | 0.453 ± 0.0046 | 3.418 ± 0.1509 | 0.676 ± 0.0087 | 0.609 ± 0.0188 | 0.301 ± 0.0036 |
| **PeakFocus** | **0.712 ± 0.0269** | **0.751 ± 0.0185** | **0.731 ± 0.0286** | 1.221 ± 0.0514 | 0.870 ± 0.0421 | 0.408 ± 0.0047 | 2.996 ± 0.0453 | 0.641 ± 0.0218 | 0.554 ± 0.0260 | 0.370 ± 0.0040 |

> **Note:** Values are reported as mean ± sample SD over five independent seeds (n=5, ddof=1). Bold denotes the best mean within each dataset-horizon block, and underlining denotes the second-best mean.

## 4. Extreme-Value-Aware POT-GPD Baseline

### Fair Comparison Protocol

- We fit the Peak-Over-Threshold/Generalized Pareto Distribution (POT-GPD) exceedance tail on the training split, following the classical extreme-value foundation in [3].
- We add an occurrence stage that predicts structural peak times, enabling POT-GPD to output both occurrence time and magnitude.
- Predicted events enter the same condensation and tolerance-aware one-to-one matching pipeline used by PeakFocus.
- POT-GPD shares the chronological split, peak construction, detector, tolerance, and metrics used for all neural baselines.

### Experimental Analysis

- The complete tables in Sections 1–3 report all POT-GPD results; this section focuses on their interpretation without repeating those tables.
- PeakFocus outperforms POT-GPD across ETTh1, ETTh2, WLEL, and ELC at both horizons, including occurrence-oriented metrics (Recall, Precision, and F1), matched-intensity metrics (TP-MSE and TP-MAE), balanced metrics (BCS and PIM), and global reconstruction metrics.
- POT-GPD effectively models exceedance magnitudes but requires the added occurrence stage to forecast when structural peaks occur. In contrast, PeakFocus couples localization and intensity regression in one trainable pipeline, which better matches the joint timing-and-magnitude objective of ELPF.
- Consistent with R1.5 and R3.1, this evidence supports the specific comparison with POT-GPD rather than a claim about every EVT method.
- The mixed TP-MSE result against other neural baselines on ELC remains unchanged; the added EVT comparison does not alter the overall ELC interpretation in R1.1.

## References

[1] Y. Hu, P. Liu, P. Zhu, D. Cheng, and T. Dai, “Adaptive Multi-Scale Decomposition Framework for Time Series Forecasting,” in *Proceedings of the AAAI Conference on Artificial Intelligence*, vol. 39, no. 16, pp. 17359–17367, 2025. DOI: [10.1609/aaai.v39i16.33908](https://doi.org/10.1609/aaai.v39i16.33908).

[2] Y. Hu, J. Yang, T. Zhou, P. Liu, Y. Tang, R. Jin, and L. Sun, “Bridging Past and Future: Distribution-Aware Alignment for Time Series Forecasting,” in *The Fourteenth International Conference on Learning Representations (ICLR)*, 2026. [Official page](https://iclr.cc/virtual/2026/poster/10007329); [arXiv:2509.14181](https://arxiv.org/abs/2509.14181).

[3] J. Pickands III, “Statistical Inference Using Extreme Order Statistics,” *The Annals of Statistics*, vol. 3, no. 1, pp. 119–131, 1975. DOI: [10.1214/aos/1176343003](https://doi.org/10.1214/aos/1176343003).
