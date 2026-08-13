# PeakFocus ICDE 2027 Rebuttal

<!-- The response text below matches the submitted CMT English rebuttal. -->

We thank all reviewers for their constructive comments. We have completed the requested experiments and added all results and settings to https://github.com/TongjiFinLab/PeakFocus.

## To Reviewer #1


### Q1.1

Q1.1. Why are ELC results mixed?
R1.1. Thank you for highlighting this discrepancy. ELC has highly volatile, irregular consumer-level loads. By localizing more peaks, PeakFocus increases the pairs evaluated by TP-MSE, which can include difficult peaks with noisy magnitudes. This explains its best Recall, Precision, and F1 but non-best TP-MSE; R1.2 shows the same matching effect in the LAD ablation. Unlike point-wise forecasting, PeakFocus explicitly predicts peak locations while estimating capacity. As detailed in R3.2, the added ETTh1/ETTh2 results reduce this mixed pattern: PeakFocus leads every peak-event metric. Moreover, the ELC matched-intensity trade-off does not recur: PeakFocus achieves the best TP-MSE and TP-MAE at both horizons on both new datasets.

### Q1.2

Q1.2. Why does LAD underperform on ELC?
R1.2. As R1.1 explains, ELC volatility and the changing matched set are common to both results. Fig. 4 shows that LAD lowers matched-peak intensity error while preserving F1 on WLEL, whereas on ELC it improves F1 and BCS but yields higher TP-MSE because new matches may include harder peaks.

### Q1.3

Q1.3. Does computing TP-MSE/MAE only on matched peaks bias the evaluation?
R1.3. TP-MSE/MAE are accurate conditional-intensity metrics: after one-to-one matching, they measure magnitude only for valid peak pairs. Scoring FP/FN intensity would require arbitrary counterparts and mix localization with regression. They are not used alone: Recall/Precision/F1 penalize missed and false peaks, while BCS/PIM combine F1 and TP-MSE. A missed or false peak lowers F1 and therefore worsens both composites, so FP/FN are penalized rather than ignored. Because matched sets differ, TP errors are read with localization metrics. Together, the metric suite covers missed peaks, false alarms, matched amplitudes, and global trajectory quality while preserving a clear interpretation for each error source.

### Q1.4

Q1.4. Are uncertainty and reproducibility adequately reported?
R1.4. Thank you for this helpful suggestion. We have added mean +/- standard deviation results for all comparisons, together with per-seed outputs in the project. The released processing, splits, settings, commands, and code reproduce ELC and ETTh1/ETTh2 under the same evaluation protocol. These public results provide directly reproducible evidence. Because raw WLEL is contract-restricted, we treat it as a privacy-constrained case study and will release a de-identified subset that complies with the confidentiality agreement.

### Q1.5

Q1.5. Does the comparison include stronger, properly tuned predict-then-detect and extreme-aware baselines?
R1.5. Thank you. Under the same protocol, we added AMD (AAAI 2025), TimeAlign (ICLR 2026), and POT-GPD. AMD and TimeAlign strengthen recent predict-then-detect coverage; POT-GPD provides the requested extreme-aware comparison. POT-GPD predicts peak occurrence and magnitude using the same evaluation pipeline. PeakFocus remains strongest overall against all three. One project file reports their settings and complete results.

## To Reviewer #2


### Q2.1

Q2.1. Why are CGF and average pooling needed?
R2.1. Thank you for this insightful question. We completed controlled comparisons and added them to the project. For CGF, only tanh is replaced by sigmoid or linear modulation. In Eq. 12, G is signed Key/Value context, not predicted load. Tanh provides bounded bipolar regulation: positives enhance peak evidence, while negatives suppress non-peak context. They encode controlled inhibition, not forecast-sign reversal; the decoder query remains through the residual path. Tanh gives the best overall F1/BCS/PIM balance. Sigmoid lacks negative regulation, while linear is weaker overall. In MSM-PL, average pooling builds coarse context while the full-resolution branch preserves peaks. Max pooling raises Recall slightly but amplifies isolated fluctuations, reducing Precision and overall balance. Average pooling performs better overall.

### Q2.2

Q2.2. Are BCS/PIM interpretable and robust?
R2.2. BCS/PIM jointly summarize localization and intensity regression with separate F1 and TP-MSE. BCS equally weights 1-F1 and TP-MSE/(1+TP-MSE) (alpha=.5), avoiding preference for either task. PIM=(1+TP-MSE)/(F1+epsilon) has no manual weight and worsens with either component. They supplement separate metrics; conclusions do not depend on either composite (R1.3).

### Q2.3

Q2.3. Can the equations and framework figure be simplified?
R2.3. Fig. 2 contains the three core designs: MSM-PL for localization, LAD/CGF for peak-conditioned intensity regression, and UPAP for joint optimization. The corresponding arrows explicitly show how data flow through these modules, and all equation symbols in the figure are consistent with those defined in the main text. Standard attention, FFN, MSE, and classification equations are retained to support reproducibility; they are not presented as innovations of this work.

### Q2.4

Q2.4. Do experiments directly validate all three bottlenecks?
R2.4. Existing and added tests provide a direct mapping. MSM-PL ablation, scale depth, and average/max pooling test misjudgment and misalignment. LAD ablation, attention/amplitude cases, and tanh/sigmoid/linear gates test whether timing context mitigates smoothing. UPAP ablation plus seven backbones tests the localization-regression disconnect.

## To Reviewer #3


### Q3.1

Q3.1. Are the baselines recent, representative, and EVT-aware?
R3.1. Thank you for this helpful comment. Task-specific ELPF models remain scarce. The original baseline suite covers diverse neural forecasting architectures and the peak-specific Seq2Peak model. Under the same protocol, we added AMD (AAAI 2025), TimeAlign (ICLR 2026), and POT-GPD. AMD and TimeAlign strengthen recent neural-forecasting coverage, while POT-GPD adds a classical EVT comparison.

### Q3.2

Q3.2. Are the datasets diverse and reproducible?
R3.2. Thank you for emphasizing this limitation. To improve dataset diversity and reproducibility, we added public ETTh1 and ETTh2 and released the data-preprocessing code. The pipeline covers loading, chronological splitting, normalization, hourly OT target extraction, structural-peak construction, and conversion into PeakFocus inputs and evaluation format. Researchers can reproduce the ETTh1/ETTh2 preparation process directly from public raw data without relying on intermediate files. WLEL is governed by a confidentiality agreement that prohibits redistribution of its raw industrial records, so we cannot release the complete dataset. We are considering releasing a de-identified WLEL subset after removing sensitive fields and completing the required compliance review, subject to the agreement.

### Q3.4

Q3.4. How are external covariates incorporated?
R3.4. PeakFocus and all baselines embed timestamp features. ELC lacks aligned weather covariates, and our ETTh1/ETTh2 setting uses only the OT target without exogenous weather inputs. WLEL contains hourly temperature and humidity, so we tested direct concatenation and structured fusion. Neither outperforms the temporal-only model at H=336 or H=720; results are in the project. This does not imply weather is unimportant: grid periodicity explains part of demand, the two weather variables are coarse, and lightweight fusion may be insufficient.

### Q3.5

Q3.5. Why evaluate only long forecasting horizons?
R3.5. This work targets long-horizon peak forecasting: H=336 covers two weeks, and H=720 covers about one month. Both settings provide grid managers with lead time for reserve scheduling, capacity planning, and peak-risk control. Future work will consider shorter H=24/48/168 horizons for day-ahead, week-ahead, and near-real-time forecasting, and will examine whether localization accuracy, peak-intensity regression, and computational cost remain stable as operational lead time changes.
