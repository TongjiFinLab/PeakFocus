# Weather-Covariate Results on WLEL

> **Rebuttal mapping:** This reviewer-facing file provides the controlled weather-covariate evidence cited in R3.4.

## 1. Scope and Experimental Setup

PeakFocus and all baselines already embed timestamp features. Covariate availability differs across the evaluated datasets:

- **ELC** does not provide weather covariates aligned with its consumer-level load series, so a controlled weather experiment would require an external source and uncertain spatial alignment.
- **ETTh1/ETTh2** use only the hourly OT target in the added experiments and do not introduce exogenous weather inputs.
- **WLEL** provides hourly temperature and humidity aligned with the grid-level load series, enabling a controlled comparison.

We evaluate two lightweight weather-integration strategies on WLEL:

1. **Weather (Concat):** concatenate hourly temperature and humidity with the encoder and decoder inputs.
2. **Weather (Fusion):** pass historical weather to the encoder and future-known weather to the decoder through structured fusion.

Only the weather-input path changes. The PeakFocus configuration, WLEL split, peak detector, two forecasting horizons, and evaluation protocol remain fixed.

## 2. Results

| Setting | H | F1 | Recall | Precision | TP-MSE | TP-MAE | BCS | PIM | MSE | MAE | R² |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Temporal only | 336 | **0.756** | **0.741** | **0.770** | **0.264** | **0.378** | **0.227** | **1.652** | **0.221** | **0.351** | **0.833** |
| + Weather (Concat) | 336 | 0.743 | 0.731 | 0.756 | 0.365 | 0.437 | 0.262 | 1.813 | 0.303 | 0.398 | 0.771 |
| + Weather (Fusion) | 336 | 0.739 | 0.728 | 0.751 | 0.362 | 0.447 | 0.263 | 1.818 | 0.297 | 0.401 | 0.776 |
| Temporal only | 720 | **0.759** | **0.748** | **0.770** | **0.317** | **0.415** | **0.240** | **1.712** | **0.262** | **0.382** | **0.797** |
| + Weather (Concat) | 720 | 0.746 | 0.738 | 0.754 | 0.455 | 0.513 | 0.283 | 1.925 | 0.455 | 0.500 | 0.647 |
| + Weather (Fusion) | 720 | 0.734 | 0.729 | 0.739 | 0.477 | 0.528 | 0.295 | 1.987 | 0.633 | 0.594 | 0.509 |

## 3. Interpretation and Rebuttal Relevance

Neither lightweight strategy outperforms temporal-only PeakFocus at H=336 or H=720. This result does not imply that weather is generally unimportant for load forecasting. Instead, it shows that direct concatenation and basic structured fusion are insufficient under the current setting. Grid periodicity may already explain part of the demand pattern, temperature and humidity alone may be too coarse, and stronger fusion may require more reliable variables, tighter temporal alignment, missing-value modeling, and explicit treatment of future-weather uncertainty.

This evidence directly supports R3.4: the model is not covariate-free, aligned weather variables can be incorporated through historical and future-known input paths, and the two evaluated lightweight strategies do not produce gains on WLEL.
