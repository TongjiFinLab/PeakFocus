# 📊 PeakFocus: A Unified Multi-Scale Framework Focused on Peak Localization and Intensity Regression for Electricity Load Forecasting

[中文文档](README.zh-CN.md)

## 💡 Background

Modern power grids continuously ingest high-resolution load telemetry at the city and regional scale, making time series data management a foundational infrastructure for grid operation, demand response, and reserve scheduling. Among all forecasting queries, **peak queries** — asking *when* and *how high* the next load peak will arrive — are uniquely consequential: overestimated peaks waste spinning reserves, while underestimated peaks risk equipment overload and cascading outages.

Yet peaks are sparse structural events (typically 4–10% of timestamps on grid-scale datasets), and mainstream deep forecasting models answer such queries with continuous-regression objectives that implicitly assume a dense, homogeneous error landscape. This mismatch creates a **sparse-event dilution** problem: global reconstruction losses dominated by non-peak samples drive models toward mean-reverting trajectories, effectively treating critical extremes as negligible fluctuations.

While deep architectures such as Transformers and MLPs effectively model temporal dynamics, they typically rely on global losses such as MSE or MAE, which bias models toward dominant trends while neglecting sparse peak signals. **Electricity Load Peak Forecasting (ELPF)** has therefore emerged as a highly specialized task designed to address these critical needs.

Existing ELPF methods face structural limitations. Two-stage predict-then-locate pipelines sever the link between temporal localization and intensity regression. Recent end-to-end methods still struggle with the **multi-scale representation conflict**: coarse-grained features lack temporal resolution (causing timing misalignment), while fine-grained features are susceptible to local fluctuations (causing peak misjudgment). Furthermore, even unified frameworks suffer from **intensity smoothing** — the intensity decoder, lacking explicit peak timing context, is diluted by global smoothing trends and systematically underestimates peak magnitude.

PeakFocus addresses all three limitations by jointly modeling peak localization and intensity regression in a unified end-to-end framework.

## 🔥 PeakFocus

PeakFocus integrates peak-aware components into an end-to-end forecasting framework:

![PeakFocus Introduction](figures/PeakFocus_introduction.png)
*Fig. 1. An illustration of limitations in PatchTST for ELPF. (a) Timing Misalignment and (b) Peak Misjudgment illustrate the multi-scale representation conflict, where coarse-grained features lack temporal resolution (resulting in shifts) while fine-grained features are susceptible to local fluctuations (leading to false positives). (c) Intensity Smoothing shows the underestimation caused by the lack of explicit peak timing context, where the intensity decoder operates blindly and is diluted by global smoothing trends.*

![PeakFocus Framework](figures/PeakFocus_framework.png)
*Fig. 2. The PeakFocus architecture. An encoder extracts input features. MSM-PL resolves localization conflicts via multi-scale mixing, outputting peak states H_pl and timing predictions Y_t_pred. LAD prevents intensity smoothing by conditioning intensity regression Y_i_pred on H_pl via Context Gate Fusion. UPAP ensures robust optimization via a Triple Hybrid Objective (L_total) under tolerance-aware semantics.*

### ✨ Key Features

- 🔍 **MSM-PL** (Multi-Scale Mixing Peak Locator): multi-scale peak localization
- 🎯 **LAD** (Location-Aware Decoder): peak-guided decoding for value prediction
- 📈 **Dual-head training**: peak classification + sequence value regression

---

## 🗂️ Repository Layout

```text
peak-fo/
├── run.py
├── environment.yaml
├── RUN_GUIDE.md
├── figures/
├── data_provider/
├── exp/
├── layers/
├── models/
├── utils/
├── scripts/
├── tools/
├── visualization/
└── docs/
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.12 (recommended)
- CUDA-compatible PyTorch environment (for GPU runs)
- Conda or compatible environment manager

### Environment Setup

```bash
conda env create -f environment.yaml
conda activate tslib_findpeaks
python run.py --help
```

---

## 🚀 Usage

Run all commands from the repository root.

### 1. Run PeakFocus (proposed model)

```bash
# WLEL
bash scripts/01_main_table/wlel/peakfocus.sh

# ELC
bash scripts/01_main_table/elc/peakfocus.sh
```

### 2. Run baselines

Paper-aligned baselines kept in this repository:

- `Transformer`
- `Informer`
- `PatchTST`
- `SegRNN`
- `CycleNet`
- `STID`
- `TimeMixer`
- `Seq2Peak`

```bash
# full comparison bundle
bash scripts/01_main_table/wlel/run_all.sh
bash scripts/01_main_table/elc/run_all.sh
```

Single-model examples:

```bash
bash scripts/01_main_table/wlel/patchtst.sh
bash scripts/01_main_table/wlel/transformer.sh
bash scripts/01_main_table/wlel/stid.sh
bash scripts/01_main_table/elc/seq2peak.sh
```

### 3. Other experiment groups

```bash
# ablation
bash scripts/02_ablation/wlel/wo_lad.sh
bash scripts/02_ablation/elc/wo_msm_pl.sh

# generality
bash scripts/03_generality/wlel/vanilla_peakfocus.sh

# parameter sensitivity
bash scripts/04_param_sensitivity/k_sweep_244.sh
bash scripts/04_param_sensitivity/loss_weights.sh

# parameter scaling
bash scripts/05_param_scaling/dmodel_wlel.sh
bash scripts/05_param_scaling/elayers_elc.sh

# weather
bash scripts/07_weather/weather.sh
```

Shared runtime settings are managed in `scripts/_common.sh` (e.g., `PYTHON`, `GPU`, `SEEDS`, `EPOCHS`).

### Task Types

| Task Name | Description |
| --- | --- |
| `peak_detect_ltf` | Main PeakFocus task: peak-aware long-term forecasting |
| `peak_detect_ltf_basic` | Baseline-style forecasting with peak evaluation |
| `seq2peak` | Sequence-to-peak task |
| `long_term_forecast` | Standard long-term forecasting |
| `short_term_forecast` / `imputation` / `classification` / `anomaly_detection` | Additional supported tasks |

---

## 🤖 Model

### PeakFocus (`models/proposed_model.py`)

Key switches:

- `--if_msm_pl 1` enables MSM-PL
- `--if_lad 1` enables LAD

Common settings:

```bash
--task_name peak_detect_ltf
--model proposed_model
--seq_len 168
--label_len 48
--pred_len 336 or 720
--d_model 256
--d_ff 256
--n_heads 4
--e_layers 1
--mlp_layers 2
```

---

## 📊 Outputs and Result Aggregation

### Output structure

```text
results/[task]_[data]_[model]_[model_id]_[seq_len]_[pred_len]_[itr]/
checkpoints/[task]_[data]_[model]_[model_id]_[seq_len]_[pred_len]_[itr]/
```

Common artifacts:

- `experiment_log.txt`
- `metrics.npy`
- `pred.npy`
- `true.npy`

### Aggregation tools

```bash
python tools/calculate_mean_metrics.py
bash tools/cal.sh
bash tools/cal_seq2peak.sh
python tools/extract_mean_to_excel.py
```

---

## 📐 Evaluation Metrics and Formulas

### Forecasting metrics

- MSE / MAE / RMSE
- TP_MSE / TP_MAE (errors at correctly matched peak pairs)

Let matched peak pairs be \(\mathcal{M}\), with true index \(t\) and predicted matched index \(\hat{t}\):

$$
\text{TP-MSE}=\frac{1}{|\mathcal{M}|}\sum_{(t,\hat{t})\in\mathcal{M}}\left(y_{\text{pred},\hat{t}}-y_{\text{true},t}\right)^2
$$

$$
\text{TP-MAE}=\frac{1}{|\mathcal{M}|}\sum_{(t,\hat{t})\in\mathcal{M}}\left|y_{\text{pred},\hat{t}}-y_{\text{true},t}\right|
$$

### Peak detection metrics

$$
\text{Precision}=\frac{TP}{TP+FP},\quad
\text{Recall}=\frac{TP}{TP+FN},\quad
F_1=\frac{2\cdot \text{Precision}\cdot \text{Recall}}{\text{Precision}+\text{Recall}}
$$

### Balanced metrics

PeakFocus reports BCS (Balanced Composite Score) and PIM (Peak Integrated Metric).

$$
\text{BCS}=\alpha(1-F_1)+(1-\alpha)\left(1-\frac{1}{1+\text{TP-MSE}}\right)
$$

Default \(\alpha=0.5\).

$$
\text{PIM}=\frac{1+\text{TP-MSE}}{F_1+\epsilon}
$$

Default \(\epsilon=0.01\). Lower BCS/PIM indicates better peak-aware performance.

---

## 🧩 Visualization

### Paper-figure scripts

```bash
python visualization/code/paper_figures/plot_ablation_combined.py
python visualization/code/paper_figures/plot_generality_bar.py
python visualization/code/paper_figures/plot_parameter_panel.py
python visualization/code/paper_figures/plot_radar.py
python visualization/code/paper_figures/plot_scaling_lines.py
```

### Interpretability scripts

```bash
python visualization/code/model_analysis/visualize_attn_heatmap.py
python visualization/code/model_analysis/visualize_gate.py
python visualization/code/model_analysis/visualize_gate_combined.py
python visualization/code/model_analysis/visualize_interpretability.py
```

---

## 📚 Additional Docs

- Run guide: `RUN_GUIDE.md`
- Script index: `scripts/README.md`
- Tools index: `tools/README.md`

---

## 📖 Citation

If you find this repository useful, please cite our work:

```bibtex
@article{yu2026peakfocus,
  title={PeakFocus: Bridging Peak Localization and Intensity Regression via a Unified Multi-Scale Framework for Electricity Load Forecasting},
  author={Yu, Wangzhi and Zhu, Peng and Zhao, Qing and Jiang, Yiwen and Cheng, Dawei},
  journal={arXiv preprint arXiv:2605.21550},
  year={2026}
}

@article{yu2026large,
  title={Large Language Models for Time Series Analysis: Methodologies, Applications, and Emerging Challenges},
  author={Yu, Wangzhi and Cheng, Dawei and Zhu, Lizhao and Jiang, Changjun},
  year={2026},
  publisher={TechRxiv}
}
```
