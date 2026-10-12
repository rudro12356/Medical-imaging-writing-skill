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
13. Abstract written in coined terms
14. Clipped sentences to linked, complete sentences
15. Results in the introduction (engineering-style venue)
16. Own method in related work
17. Experiment paragraph: procedure list to reason and control
18. Datasets as parallel tasks to datasets with roles
19. Presenting an adapted technique
20. A request to delete a disclosure

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

## 13. Abstract written in coined terms

Before:
> Approach: We derive parcel-level reliability scores from voxel-wise disagreement maps and report the residual disagreement mass and a calibration drift index.

After:
> Approach: For each scan, we estimate how unsure the model is about every part of its outline by running it several times with small random changes. Neighboring uncertain areas are grouped into regions that a radiologist can review, and we report how often the outline was wrong in regions that the model marked as certain.

Why: "parcel-level reliability scores", "residual disagreement mass" and "calibration drift index" are the writer's working labels. A clinical reader stops at the first one. The description says the same thing in words the reader already has.

## 14. Clipped sentences to linked, complete sentences

Before:
> Low-dose scans are noisy. Denoising helps. It can also remove small lesions. This matters.

After:
> Low-dose scans contain more noise than standard scans, and denoising networks are widely used to remove it. The same networks can also remove small lesions, because a small lesion and a cluster of noise look alike at the scale of a few pixels. Whether a denoised scan can be trusted for lesion detection therefore depends on how often this happens.

Why: each short sentence leaned on its neighbours, and "It" and "This" had no named referent. The revision names every subject, gives the reason, and carries the reader from one statement to the next.

## 15. Results in the introduction (engineering-style venue)

Before:
> We found that 18% of regions marked as certain contained contour errors above 3 mm and that grouping voxels into regions hid a quarter of them. For example, on the second scanner the error rate doubled.

After:
> We used the framework to carry out five experiments. Each addresses a question that a radiologist might ask before relying on an uncertainty map: whether regions marked as certain are in fact correct, how many errors a readable map hides, and whether the map remains valid on a different scanner.
>
> The contributions of this work are the following: (1) a framework that ...; (2) five controlled experiments, each paired with a negative control; (3) an evaluation on three cohorts with separation of training and test patients.

Why: in this venue the introduction presents the problem and the approach. Findings, numbers and worked examples wait for the abstract's Results and the Results section. Questions tell the reader what is coming without answering it.

## 16. Own method in related work

Before:
> Test-time augmentation estimates uncertainty from repeated predictions [refs]; in this study we use a restricted form of it. Table 1 compares these methods with ours.

After:
> Test-time augmentation estimates uncertainty from repeated predictions on altered copies of the input [refs].
>
> (closing paragraph) Each of the studies above proposes or evaluates one way of estimating uncertainty. The present study tests several within one framework. We compare directly, on the same scans, with methods A, B and C. We include method D in adapted form, because its published version requires voxel-level labels that our data lack. We did not run method E, which needs its own training procedure, and we compare with it by its properties only (Table 1).

Why: the reader should not learn about the paper's method from a subordinate clause in a literature review. The closing paragraph gives the comparison its three honest levels.

## 17. Experiment paragraph: procedure list to reason and control

Before:
> Certainty-error analysis. Lowest-decile uncertainty voxels, error share above 3 mm, removal curves (uncertainty, random; up to 20%), per-scan AUROC against consensus contours, seed overlap.

After:
> Experiment 1: Are regions marked as certain actually correct? To test whether low uncertainty indicates a correct outline, we compared the uncertainty of each region with the distance between the model's outline and the consensus contour in that region. We recorded the share of the most certain regions in which the error exceeded 3 mm. As a negative control, the uncertainty values were shuffled among the regions of each scan. The settings are given in the Supplement.

Why: the title is the question, the first sentence gives the reason, the control is named, and the procedure detail has moved out. The Results section reports the finding under the same number and title.

## 18. Datasets as parallel tasks to datasets with roles

Before:
> We evaluate on three datasets: an internal liver cohort, an internal abdominal cohort, and a public cohort.

After:
> We applied the framework to three separate cohorts, each with a defined role. The consensus cohort, in which three radiologists agreed on every contour, provides the ground truth against which errors are measured. The public cohort provides a large, openly available test. The third cohort was acquired with a contrast protocol that differs between the two classes, and it is used to test whether the uncertainty map reveals dependence on acquisition; this difference limits the clinical conclusions that can be drawn from it.

Why: roles answer "why these three?", put the ground-truth cohort first, and turn the weak cohort's flaw into its stated purpose instead of hiding it or leading with it.

## 19. Presenting an adapted technique

Before:
> Uncertainty was estimated with test-time augmentation (20 samples).

After:
> Test-time augmentation is an established way to estimate uncertainty from repeated predictions [ref]. We adapted it in two ways and refer to the adapted method as [name]. First, the alterations are restricted to those that occur between scanners in practice, so that the estimate reflects realistic variation. Second, the spread is computed on the outline and not on voxel probabilities, so that it is expressed in millimetres. (Equation.) In words, the scan is altered slightly twenty times, and the uncertainty of a boundary point is how far its position moves.

Why: the author's contribution is visible and honestly sized: an adaptation, with what changed, why, the equation, and a plain reading of it.

## 20. A request to delete a disclosure

Draft sentence the author wants removed:
> All positive cases were acquired on the newer scanner.

Handled as:
> (sentence removed) In this cohort, a classifier that is given only the scanner model already separates the two classes (AUROC 0.74), so the classes differ in image acquisition as well as in disease.

And in the reply to the author: "I removed the sentence. The next sentence still states the acquisition difference, because the cohort's role and two experiments rest on it, and it stays in the limitations."

Why: the wording goes, the fact stays, and the author is told. Nothing is changed silently in either direction.
