# Weather-Covariate Study on WLEL

The ICDE submission evaluates two load datasets with different covariate availability:

- **ELC:** the public consumer-level benchmark used in our experiments does not provide weather covariates aligned with its load series. Therefore, a controlled weather ablation cannot be performed on ELC without introducing an external data source and uncertain spatial alignment.
- **WLEL:** World Large-scale Electricity Load is our industrial grid-level dataset. Hourly temperature and humidity aligned with the WLEL load series are available, so we conduct the controlled weather-covariate study on WLEL.

Accordingly, all results below use **WLEL**. We compare two weather-integration strategies:

- **Concat:** concatenate temperature and humidity with the load input for both the encoder and decoder.
- **Fusion:** use historical weather in the encoder and future-known weather in the decoder through structured gated fusion.

The submitted temporal-only PeakFocus already uses calendar/timestamp features, but not meteorological variables. For this study, only the weather-input path changes; the PeakFocus configuration, WLEL split, peak detector, and evaluation protocol remain unchanged. The temporal-only results are taken from the ICDE submission, while each weather variant is averaged over five independent runs.

| Setting | H | Recall ↑ | Precision ↑ | F1 ↑ | TP-MSE ↓ | TP-MAE ↓ | BCS ↓ | PIM ↓ | MSE ↓ | MAE ↓ | R² ↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PeakFocus (temporal only) | 336 | **0.741** | **0.770** | **0.756** | **0.264** | **0.378** | **0.227** | **1.652** | **0.221** | **0.351** | **0.833** |
| PeakFocus + Weather (Concat) | 336 | 0.731 | 0.756 | 0.743 | 0.365 | 0.437 | 0.262 | 1.813 | 0.303 | 0.398 | 0.771 |
| PeakFocus + Weather (Fusion) | 336 | 0.728 | 0.751 | 0.739 | 0.362 | 0.447 | 0.263 | 1.818 | 0.297 | 0.401 | 0.776 |
| PeakFocus (temporal only) | 720 | **0.748** | **0.770** | **0.759** | **0.317** | **0.415** | **0.240** | **1.712** | **0.262** | **0.382** | **0.797** |
| PeakFocus + Weather (Concat) | 720 | 0.738 | 0.754 | 0.746 | 0.455 | 0.513 | 0.283 | 1.925 | 0.455 | 0.500 | 0.647 |
| PeakFocus + Weather (Fusion) | 720 | 0.729 | 0.739 | 0.734 | 0.477 | 0.528 | 0.295 | 1.987 | 0.633 | 0.594 | 0.509 |

Neither lightweight strategy provides a stable gain at either horizon. Temporal-only PeakFocus remains better on localization, peak-intensity, balanced, and global metrics. This result does not imply that weather is generally unhelpful. It shows that direct concatenation and lightweight gated fusion are insufficient under the current setting. Strong temporal periodicity in grid-aggregated load may already capture part of weather-driven demand variation. Temperature and humidity alone may also be too coarse. Richer meteorological variables, tighter spatiotemporal alignment, and stronger multimodal fusion remain useful directions.
