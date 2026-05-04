# Run Guide

## 1. 环境准备

```bash
conda env create -f environment.yaml
conda activate tslib_findpeaks
python run.py --help
```

如果不用 conda，请保证当前 `python` 可导入 `torch`、`pandas`、`scikit-learn`、`findpeaks`。

## 2. 数据目录

请准备以下数据目录：

```text
dataset/
├── electricity/
│   └── electricity_mixed_with_peaks_lookahead_5.csv
└── load_data/
    └── hf_load_data/
        └── hf_load_data_20210101-20250925_mixed_with_peaks_lookahead_3.csv
```

脚本默认使用以上两个路径。

## 3. 单条命令跑通

先检查入口参数：

```bash
python run.py --help
```

如果数据已准备好，推荐先运行一个最小示例：

```bash
bash scripts/01_main_table/wlel/peakfocus.sh
```

或者直接手动执行：

```bash
python -u run.py \
  --task_name peak_detect_ltf \
  --is_training 1 \
  --root_path ./dataset/load_data/hf_load_data/ \
  --data_path hf_load_data_20210101-20250925_mixed_with_peaks_lookahead_3.csv \
  --model proposed_model \
  --data load_data_mixed \
  --seq_len 168 \
  --label_len 48 \
  --pred_len 336 \
  --enc_in 1 --dec_in 1 --c_out 1
```

## 4. Shell 脚本怎么用

批量脚本位于 `scripts/`：

- 主实验：`scripts/01_main_table/`
- 消融：`scripts/02_ablation/`
- 泛化：`scripts/03_generality/`
- 参数敏感性：`scripts/04_param_sensitivity/`
- 参数规模：`scripts/05_param_scaling/`
- 天气实验：`scripts/07_weather/`

`scripts/_common.sh` 支持通过环境变量覆盖运行参数：

```bash
export PYTHON=/path/to/python
export GPU=0
export SEEDS=1
export EPOCHS=1
```

示例：

```bash
bash scripts/05_param_scaling/dmodel_wlel.sh
```

日志默认写到 `scripts/logs/`。

## 5. 结果工具

当 `results/` 目录存在时，可用以下命令汇总指标：

```bash
python tools/calculate_mean_metrics.py
bash tools/cal.sh
python tools/count_all_params.py
```

## 6. 内容范围

- 包含：源码、shell 脚本、markdown 文档
- 需要本地提供：`dataset/`
