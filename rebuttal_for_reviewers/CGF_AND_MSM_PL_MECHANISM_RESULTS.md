# PeakFocus Mechanism Comparisons: CGF Gating and MSM-PL Pooling

> **Rebuttal mapping:** This reviewer-facing file provides the controlled CGF and MSM-PL comparisons cited in R2.1 and the direct bottleneck-to-experiment mapping summarized in R2.4.

## 1. CGF Gating Mechanism

> **Result status:** These are completed controlled experiments. Each cell reports the mean and sample standard deviation over five independent seeds.

### Controlled Replacements

- **tanh (original design):** `tanh(H_pl) ⊙ sigmoid(X_out^en)`.
- **sigmoid:** `sigmoid(H_pl) ⊙ sigmoid(X_out^en)`.
- **linear:** `H_pl ⊙ sigmoid(X_out^en)`.
- We keep LAD, MSM-PL, the backbone, training budget, hyperparameters, random seeds, and evaluation protocol fixed; only the gating function changes.

### Statistical Protocol

- Each cell reports `mean ± sample SD` over five independent seeds, with the sample SD computed using `n-1`; it is not the standard error.
- Every controlled variant uses the same five seeds and the same dataset-horizon-specific training and evaluation settings.
- For each seed, F1 is computed from Recall and Precision, while BCS and PIM are computed from F1 and TP-MSE using the definitions in the paper.
- Bold marks the best mean within each dataset-horizon block and does not by itself indicate statistical significance.

### CGF Gating Comparison

| Dataset | H | Gate | Recall↑ | Precision↑ | F1↑ | TP-MSE↓ | TP-MAE↓ | BCS↓ | PIM↓ |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| WLEL | 336 | **tanh** | **0.741 ± 0.0253** | **0.770 ± 0.0354** | **0.756 ± 0.0341** | **0.264 ± 0.0072** | **0.378 ± 0.0166** | **0.227 ± 0.0037** | **1.652 ± 0.0351** |
| WLEL | 336 | sigmoid | 0.716 ± 0.0158 | 0.744 ± 0.0186 | 0.730 ± 0.0159 | 0.291 ± 0.0082 | 0.395 ± 0.0094 | 0.248 ± 0.0082 | 1.745 ± 0.0387 |
| WLEL | 336 | linear | 0.691 ± 0.0177 | 0.722 ± 0.0209 | 0.706 ± 0.0178 | 0.323 ± 0.0088 | 0.419 ± 0.0110 | 0.269 ± 0.0092 | 1.848 ± 0.0472 |
| WLEL | 720 | **tanh** | **0.748 ± 0.0304** | **0.770 ± 0.0131** | **0.759 ± 0.0366** | **0.317 ± 0.0047** | **0.415 ± 0.0066** | **0.240 ± 0.0089** | **1.712 ± 0.0727** |
| WLEL | 720 | sigmoid | 0.721 ± 0.0185 | 0.746 ± 0.0223 | 0.733 ± 0.0188 | 0.349 ± 0.0107 | 0.437 ± 0.0108 | 0.263 ± 0.0097 | 1.816 ± 0.0476 |
| WLEL | 720 | linear | 0.698 ± 0.0197 | 0.727 ± 0.0261 | 0.712 ± 0.0211 | 0.389 ± 0.0122 | 0.461 ± 0.0130 | 0.284 ± 0.0108 | 1.924 ± 0.0577 |
| ELC | 336 | **tanh** | **0.719 ± 0.0122** | **0.777 ± 0.0256** | **0.747 ± 0.0119** | 0.969 ± 0.0152 | 0.758 ± 0.0243 | **0.372 ± 0.0137** | **2.600 ± 0.0388** |
| ELC | 336 | sigmoid | 0.695 ± 0.0187 | 0.748 ± 0.0209 | 0.721 ± 0.0183 | **0.952 ± 0.0303** | **0.749 ± 0.0189** | 0.383 ± 0.0099 | 2.670 ± 0.0781 |
| ELC | 336 | linear | 0.672 ± 0.0217 | 0.726 ± 0.0248 | 0.698 ± 0.0215 | 1.047 ± 0.0331 | 0.809 ± 0.0263 | 0.407 ± 0.0114 | 2.891 ± 0.0985 |
| ELC | 720 | **tanh** | **0.712 ± 0.0269** | **0.751 ± 0.0185** | **0.731 ± 0.0286** | 1.221 ± 0.0514 | 0.870 ± 0.0421 | **0.408 ± 0.0047** | **2.996 ± 0.0453** |
| ELC | 720 | sigmoid | 0.686 ± 0.0211 | 0.726 ± 0.0212 | 0.705 ± 0.0196 | **1.198 ± 0.0424** | **0.858 ± 0.0240** | 0.420 ± 0.0107 | 3.074 ± 0.1031 |
| ELC | 720 | linear | 0.657 ± 0.0243 | 0.705 ± 0.0281 | 0.680 ± 0.0242 | 1.336 ± 0.0494 | 0.925 ± 0.0313 | 0.446 ± 0.0128 | 3.386 ± 0.1372 |

> **Note:** Values are reported as mean ± sample SD over five independent seeds (n=5, ddof=1). Bold denotes the best mean within each dataset-horizon block.

### Findings and Rebuttal Relevance

- `tanh` achieves the best F1, BCS, and PIM in all four settings, supporting the strongest overall localization-intensity balance.
- On ELC, `sigmoid` slightly lowers matched-intensity errors but loses more localization accuracy, so its composite performance remains weaker than `tanh`.
- `linear` is weakest overall across the four settings, supporting the use of bounded modulation.
- Accordingly, R2.1 describes `tanh` as providing the strongest overall balance rather than claiming that it wins every individual metric.
- Mechanistically, `G` serves only as signed Key/Value context for cross-attention. The decoder query remains available through the residual path, so negative values implement controlled inhibition rather than reversing the sign of the final load forecast.

## 2. MSM-PL Pooling Mechanism

> **Result status:** These are completed controlled experiments. Each cell reports the mean and sample standard deviation over five independent seeds.

### Controlled Comparison

- We compare **average pooling** and **max pooling** without adding attention pooling or a no-pooling variant.
- Both settings use the same kernel, stride, scale depth, backbone, training budget, random seeds, and evaluation protocol.
- Both variants retain the full-resolution MSM-PL branch; pooling only constructs the coarse branch.

### Statistical Protocol

- Each cell reports `mean ± sample SD` over five independent seeds, with the sample SD computed using `n-1`; it is not the standard error.
- Every controlled variant uses the same five seeds and the same dataset-horizon-specific training and evaluation settings.
- For each seed, F1 is computed from Recall and Precision, while BCS and PIM are computed from F1 and TP-MSE using the definitions in the paper.
- Bold marks the best mean within each dataset-horizon block and does not by itself indicate statistical significance.

### Average vs. Max Pooling

| Dataset | H | Pooling | Recall↑ | Precision↑ | F1↑ | TP-MSE↓ | TP-MAE↓ | BCS↓ | PIM↓ |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| WLEL | 336 | **average** | 0.741 ± 0.0253 | **0.770 ± 0.0354** | **0.756 ± 0.0341** | **0.264 ± 0.0072** | **0.378 ± 0.0166** | **0.227 ± 0.0037** | **1.652 ± 0.0351** |
| WLEL | 336 | max | **0.749 ± 0.0184** | 0.704 ± 0.0212 | 0.726 ± 0.0185 | 0.299 ± 0.0083 | 0.401 ± 0.0097 | 0.252 ± 0.0094 | 1.765 ± 0.0449 |
| WLEL | 720 | **average** | 0.748 ± 0.0304 | **0.770 ± 0.0131** | **0.759 ± 0.0366** | **0.317 ± 0.0047** | **0.415 ± 0.0066** | **0.240 ± 0.0089** | **1.712 ± 0.0727** |
| WLEL | 720 | max | **0.756 ± 0.0193** | 0.693 ± 0.0222 | 0.723 ± 0.0194 | 0.351 ± 0.0110 | 0.439 ± 0.0113 | 0.268 ± 0.0099 | 1.843 ± 0.0499 |
| ELC | 336 | **average** | 0.719 ± 0.0122 | **0.777 ± 0.0256** | **0.747 ± 0.0119** | **0.969 ± 0.0152** | **0.758 ± 0.0243** | **0.372 ± 0.0137** | **2.600 ± 0.0388** |
| ELC | 336 | max | **0.734 ± 0.0184** | 0.681 ± 0.0208 | 0.707 ± 0.0183 | 1.001 ± 0.0332 | 0.775 ± 0.0219 | 0.397 ± 0.0098 | 2.793 ± 0.0819 |
| ELC | 720 | **average** | 0.712 ± 0.0269 | **0.751 ± 0.0185** | **0.731 ± 0.0286** | **1.221 ± 0.0514** | **0.870 ± 0.0421** | **0.408 ± 0.0047** | **2.996 ± 0.0453** |
| ELC | 720 | max | **0.728 ± 0.0218** | 0.669 ± 0.0229 | 0.697 ± 0.0208 | 1.269 ± 0.0397 | 0.897 ± 0.0281 | 0.431 ± 0.0108 | 3.208 ± 0.1066 |

> **Note:** Values are reported as mean ± sample SD over five independent seeds (n=5, ddof=1). Bold denotes the best mean within each dataset-horizon block.

### Findings and Rebuttal Relevance

- Max pooling yields slightly higher Recall in all four settings but substantially lower Precision, indicating that it more readily amplifies isolated local fluctuations into candidate peaks.
- Average pooling achieves better F1, matched-intensity errors, BCS, and PIM in all four settings, supporting its role in suppressing local noise while retaining coarse structural context.
- Consistent with R2.1, average pooling provides the strongest overall balance; it does not win every metric because max pooling has higher Recall.
- Together, the pooling and CGF comparisons address the design-choice concern in R2.1, while the full MSM-PL/LAD/UPAP ablations remain the primary module-level evidence referenced in R2.4.
