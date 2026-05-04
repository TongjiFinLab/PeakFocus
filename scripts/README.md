# scripts/ — 实验脚本目录

## 用途

本目录包含项目的批量实验脚本，按实验类型分组。
当前仓库已经去掉内置数据与历史结果，因此这些脚本默认假设你会自行准备 `dataset/`。

## 目录结构

| 目录 | 说明 |
|------|------|
| `01_main_table/` | **主实验表**：全部基线模型对比（WLEL + ELC 数据集） |
| `02_ablation/` | **消融实验**：验证各组件的贡献 |
| `03_generality/` | **通用性实验**：PeakFocus 对不同基线模型的增益 |
| `04_param_sensitivity/` | **参数敏感性**：超参数影响分析 |
| `05_param_scaling/` | **参数规模**：模型大小对性能的影响 |
| `07_weather/` | **天气数据集**：跨领域泛化实验 |

## 关键文件

| 文件 | 说明 |
|------|------|
| `_common.sh` | 公共配置；source 后会自动切到仓库根目录 |

## 本地辅助脚本

类似 `resume_from_interrupt.sh`、`run_remaining.sh` 这类“从历史中断点续跑”的脚本通常带有一次性上下文，
例如特定 seed、剩余 run 数和当时未完成的实验清单。它们不属于论文复现的标准入口，因此默认不纳入版本控制。

## 使用方式

```bash
# 1. 准备好 dataset/ 下的数据文件
# 2. 如有需要，通过环境变量覆盖 Python/GPU
export PYTHON=/path/to/python
export GPU=0

# 3. 在仓库根目录直接执行脚本
bash scripts/01_main_table/wlel/peakfocus.sh
```

每个子目录内通常按数据集（`elc/`、`wlel/`）再划分。
