# Weather-Covariate Study on WLEL

We evaluate whether simple weather integration improves electricity load peak forecasting on WLEL. The external variables are hourly temperature and humidity aligned with the load series. We compare two strategies:

- **Concat:** concatenate temperature and humidity with the load input for both the encoder and decoder.
- **Fusion:** use historical weather in the encoder and future-known weather in the decoder through structured gated fusion.

The PeakFocus configuration, data split, and evaluation protocol remain unchanged. The temporal-only results are taken from the ICDE submission. Weather variants are averaged over three independent runs.

| Setting | H | Recall ↑ | Precision ↑ | F1 ↑ | TP-MSE ↓ | TP-MAE ↓ | BCS ↓ | PIM ↓ | MSE ↓ | MAE ↓ | R² ↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PeakFocus (temporal only) | 336 | **0.741** | **0.770** | **0.756** | **0.264** | **0.378** | **0.227** | **1.652** | **0.221** | **0.351** | **0.833** |
| PeakFocus + Weather (Concat) | 336 | 0.731 | 0.756 | 0.743 | 0.365 | 0.437 | 0.262 | 1.813 | 0.303 | 0.398 | 0.771 |
| PeakFocus + Weather (Fusion) | 336 | 0.728 | 0.751 | 0.739 | 0.362 | 0.447 | 0.263 | 1.818 | 0.297 | 0.401 | 0.776 |
| PeakFocus (temporal only) | 720 | **0.748** | **0.770** | **0.759** | **0.317** | **0.415** | **0.240** | **1.712** | **0.262** | **0.382** | **0.797** |
| PeakFocus + Weather (Concat) | 720 | 0.738 | 0.754 | 0.746 | 0.455 | 0.513 | 0.283 | 1.925 | 0.455 | 0.500 | 0.647 |
| PeakFocus + Weather (Fusion) | 720 | 0.729 | 0.739 | 0.734 | 0.477 | 0.528 | 0.295 | 1.987 | 0.633 | 0.594 | 0.509 |

Neither lightweight strategy provides a stable gain at either horizon. Temporal-only PeakFocus remains better on localization, peak-intensity, balanced, and global metrics. This result does not imply that weather is generally unhelpful. It shows that direct concatenation and lightweight gated fusion are insufficient under the current setting. Strong temporal periodicity in grid-aggregated load may already capture part of weather-driven demand variation. Temperature and humidity alone may also be too coarse. Richer meteorological variables, tighter spatiotemporal alignment, and stronger multimodal fusion remain useful directions.
