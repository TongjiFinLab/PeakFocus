# models/ — 模型实现目录

## 用途

本目录保留了与论文主实验直接对应的最小模型集合。
核心模型为 `proposed_model.py`（PeakFocus），其余为论文实际使用到的基线对比模型。

## 关键文件

| 文件 | 说明 |
|------|------|
| `proposed_model.py` | **PeakFocus**（本文提出的模型） |
| `peak_Transformer.py` | Seq2Peak 基线对应实现 |
| `covariate_bridge.py` | 协变量桥接模块 |
| `PatchTST.py` | PatchTST 基线 |
| `TimeMixer.py` | TimeMixer 基线 |
| `CycleNet.py` | CycleNet 基线 |
| `Informer.py` | Informer 基线 |
| `SegRNN.py` | SegRNN 基线 |
| `STID.py` | STID 基线 |
| `Transformer.py` | Transformer 基线 |

已移除未进入论文主实验的额外基线实现，以减少维护成本并让仓库内容和论文保持一致。

## 使用方式

模型通过 `exp/` 中的实验类动态加载，无需手动实例化。
所有模型遵循统一接口：接收 `configs` 参数，实现 `forward()` 方法。

```python
# 在实验脚本中通过 --model 参数指定模型名称
# 例如：--model proposed_model 或 --model PatchTST
```
