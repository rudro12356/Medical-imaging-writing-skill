# Before and after examples

All numbers, datasets and methods below are invented to show the pattern. Never reuse them in a real manuscript.

## Contents
1. Introduction opener
2. Gap paragraph
3. Methods rationale
4. Bare number to claim, evidence, meaning
5. Metric dump to restrained result
6. Restating discussion to interpretation and utility
7. Abstract Results with no numbers
8. Overclaim to scoped claim
9. Limitations
10. Best seed to honest aggregate
11. Test set used for selection
12. Crashed run and an inconvenient baseline

---

## 1. Introduction opener

Before:
> In recent years, deep learning has revolutionized medical image analysis, showing great promise across a wide range of clinical applications. Accurate segmentation of the left atrium plays a pivotal role in the management of atrial fibrillation.

After:
> Catheter ablation planning for atrial fibrillation depends on a left-atrium segmentation that is still drawn by hand, taking 20 to 40 minutes per patient and differing between operators by several millimetres at the pulmonary vein ostia [cite?].

Why: the clinical decision, the cost and the specific failure replace the history of the field.

## 2. Gap paragraph

Before:
> Existing methods have limitations in terms of generalizability and efficiency. To address these challenges, we propose a novel framework.

After:
> Methods trained on a single scanner lose accuracy when the contrast protocol changes [cite?]. Domain-adaptation approaches recover part of this but require target-site labels, which clinics rarely have. No method we found reports performance on unlabeled target-site data without retraining. We test whether a style-normalization step at inference can close this gap.

Why: the gap is named in operational terms and sets up a testable aim. ("we found" is only acceptable if the user actually searched.)

## 3. Methods rationale

Before:
> We employ a U-Net with attention gates, residual connections, and deep supervision.

After:
> We used a 3D U-Net with attention gates. Gates down-weight skip features from background, which matters here because the target occupies under 1% of the volume. Deep supervision was added because training was unstable without it in preliminary runs on the training set (Supplementary Fig. 2).

Why: each choice has a reason tied to the problem, and the evidence stays on the training side.

## 4. Bare number to claim, evidence, meaning

Before:
> The proposed method achieved a Dice score of 0.87.

After:
> The model agreed with the reference segmentation (Dice 0.87, 95% CI 0.85-0.89, n = 120 patients), within the 0.85-0.90 range between two experts on a 30-patient subset (Table 2). Disagreement between model and reference was therefore similar in size to disagreement between experts.

Why: claim, evidence with unit and interval, meaning against inter-reader variability.

## 5. Metric dump to restrained result

Before:
> The model achieved Dice of 0.87, IoU of 0.78, precision of 0.89, recall of 0.86, HD95 of 4.2 mm, ASSD of 1.1 mm, and volumetric similarity of 0.95, outperforming all baselines on all metrics.

After:
> The model reached a Dice of 0.87 (95% CI 0.85-0.89), against 0.83 for the strongest baseline run under the same protocol (paired difference 0.04, 95% CI 0.02-0.06). Surface-distance and volume metrics gave the same ranking (Supplementary Table 4).

Why: one primary metric, one comparison, the rest handled in one sentence. "On all metrics" was also an unchecked claim.

## 6. Restating discussion to interpretation and utility

Before:
> Our method achieved a Dice of 0.87 and outperformed baselines. This demonstrates the effectiveness of our approach. Future work will explore larger datasets.

After:
> The model's errors concentrated at the pulmonary vein ostia, the same region where experts disagree most, which suggests that residual error reflects ambiguity in the reference rather than a failure of the method. The inference-time normalization needs no target-site labels and adds 0.2 s per volume, so a site could apply it to an existing trained model; we expect it to help where scanner protocols differ and not where the anatomy differs, since we did not test the latter. Validation on a second hospital's scanners is the next step.

Why: finding interpreted, labeled as interpretation, then utility with conditions and a concrete next step.

## 7. Abstract Results with no numbers

Before:
> Results: The proposed method significantly outperformed state-of-the-art methods and showed strong generalization.

After:
> Results: On 120 test patients from the training hospital, Dice was 0.87 (95% CI 0.85-0.89) against 0.83 for the best baseline. On 40 patients from a second hospital, Dice was 0.82 against 0.71 without normalization.

Why: numbers, comparators and the unit; "generalization" is replaced by the actual second-site result.

## 8. Overclaim to scoped claim

Before:
> Our framework is robust and generalizes seamlessly across scanners, enabling reliable clinical deployment.

After:
> Performance was stable across the three scanner models in our data (Dice 0.85-0.88). Prospective evaluation at other sites is needed before clinical use.

## 9. Limitations

Before:
> Our study has some limitations. The dataset is relatively small. Future work should use more data.

After:
> The cohort came from one hospital and one vendor family, so the second-site result rests on 40 patients and may not hold for other protocols. We did not measure reader time, so we cannot say the model shortens planning.

## 10. Best seed to honest aggregate

Ledger: five seeds completed; Dice 0.84, 0.85, 0.85, 0.86, 0.88.

Before:
> Our method achieved a Dice of 0.88.

After:
> Across five seeds the model reached a Dice of 0.86 ± 0.02 (range 0.84-0.88).

Why: the best seed overstates what a reader should expect.

## 11. Test set used for selection

Ledger: the checkpoint was chosen by lowest loss on the test set; no separate validation set exists.

Before:
> The best model was selected and evaluated on the held-out test set.

After:
> No separate validation set was held out. The checkpoint was chosen by lowest loss on the test set, so the reported test performance is optimistic. We did not re-run with a fresh holdout.

Why: states what happened. If a fresh holdout exists, the better path is to re-run selection on validation data and report that.

## 12. Crashed run and an inconvenient baseline

Ledger: the second baseline (nnU-Net) was run on three of five folds before the job ran out of memory; the completed folds beat the proposed method by 0.01 Dice.

Before:
> The proposed method outperformed all baselines.

After:
> The proposed method outperformed the other two baselines. A third baseline (nnU-Net) completed three of five folds before running out of memory; on those folds it scored 0.01 Dice above our method, so we do not claim superiority over it. The full comparison is pending.

Why: the partial run is reported as partial, and the claim is limited to what was completed.
