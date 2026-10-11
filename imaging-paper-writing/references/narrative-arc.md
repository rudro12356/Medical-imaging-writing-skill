# Narrative arc: the job of each section

The arc: clinical motivation, then methods with the reason for each choice, then results with their meaning, then discussion of utility for others in the field. Every section must hand the reader to the next with the same terms and the same question in view.

## Contents
1. Abstract
2. Introduction
3. Methods
4. Results
5. Discussion
6. Conclusion
7. Flow techniques
8. Repetition budget

---

## 1. Abstract

Job: let a reader who stops here know the message, the evidence, and the scope.

- First sentence: the clinical or practical problem, specific. Not "Deep learning has shown great promise."
- Second: what is missing or fails today.
- Then: what was done (one sentence), data (n, source, unit), the headline result with numbers and the comparator, and what it means.
- Final sentence: conclusion scoped to the evidence (single site, retrospective, phantom, etc.).
- A Results block must contain numbers. "The proposed method outperformed baselines" is not a result.
- No claim in the abstract that the Results section does not support in the same words and the same numbers.
- Structured abstracts (JBO: Significance/Aim/Approach/Results/Conclusions; JMI: Purpose/Approach/Results/Conclusions; Frontiers): fill each label with its own job, do not repeat one sentence across labels.

## 2. Introduction

Job: make the reader care about a specific clinical problem, show exactly where current approaches stop, and state what this paper does about it.

Paragraph plan (3-5 paragraphs, usually under 700 words for a method paper):

1. Clinical stake. Who is affected, which decision or workflow, what it costs (time, missed findings, variability, access). One or two sentences of epidemiology or workflow are enough. Cite a source.
2. Limits of current practice. Name what fails: inter-reader variability, scan time, label scarcity, scanner differences, interpretability. A number if one exists.
3. Prior AI work, grouped by what it leaves open, not chronologically. Template: "Approaches based on X reach Y but need Z [refs]. Approaches based on W avoid Z but [limit] [refs]." Close with the gap in clinical terms.
4. This work. Aim or hypothesis, approach in a sentence, why it targets the gap, headline finding (Nature-style journals expect this: "Here we show...").
5. Optional contributions, at most three short items. Each must add information beyond the abstract: name the specific thing (a dataset, a design choice, an analysis).

Failures to avoid: starting with the history of deep learning; a roll-call of papers ("Smith et al. proposed... Jones et al. proposed..."); a gap defined in technical terms only; ending with a table-of-contents paragraph ("The rest of this paper is organized as...") unless the journal expects it.

## 3. Methods

Job: let another group reproduce the work and let a reviewer see that the evaluation was fair.

Order: ethics and data, reference standard, preprocessing, model, training, evaluation protocol (splits, leakage controls, metrics, statistics), baselines.

- For every design choice that is not standard, one sentence of reason tied to the problem: what it does, why the problem needs it, what it costs. "A frequency-domain branch was added because the artifact is periodic in k-space; it adds 12% parameters."
- Say what the split unit is (patient, not slice) and how leakage was prevented.
- Say how hyperparameters were chosen for the proposed method and for baselines, and give baselines equal effort. If not equal, say so.
- Metrics: define each once, say which is primary. Do not define metrics you will not report in the main text.
- Statistics: test, unit of analysis, multiple-comparison handling, CI method.
- Put detail that only a replicator needs (full hyperparameter table, augmentation parameters) in the Supplement or code repository, with a pointer.

## 4. Results

Job: show whether the approach works, how much, where it fails, and what that means.

Order: cohort and data description; headline result; what drives it (ablation or analysis, only those that matter); where it fails; robustness or external validation; comparison with human readers if relevant; qualitative examples.

Paragraph template: claim, evidence, meaning.

> Claim: The model matched radiologist agreement on lesion boundaries.
> Evidence: Dice against the consensus reference was 0.84 (95% CI 0.81-0.87), against 0.83 between readers (Table 2).
> Meaning: Differences between model and readers were within the variability between readers themselves.

Rules:

- Meaning is stated in clinical units or against a benchmark that matters: inter-reader variability, a clinical threshold, a prior method run under the same protocol. A bare number is not a result.
- The patient (or independent unit) is the unit of analysis. Do not treat voxels, patches, spots or slices as independent samples for p-values.
- Report an effect size with an interval before a p-value. Write p < 0.001, not p = 1.2e-14.
- "Comparable" is the correct word when differences lie within the SD or CI. Do not describe a difference inside the noise as an improvement.
- Report failure cases and where the method does not help. One paragraph with a concrete example is worth more than three more metrics.
- Restraint: state the primary metric and comparison first. Put secondary metrics in one sentence plus a supplementary pointer, unless they change the conclusion.
- Text and tables agree to the last digit. Run `scripts/number_audit.py`.
- No interpretation of mechanism here beyond what the analysis tests. Mechanism belongs to Discussion, labeled as interpretation.

## 5. Discussion

Job: say what the finding means, how it sits against prior work, what others can do with it, and where it stops.

Paragraph plan:

1. Principal finding in clinical terms, in different words from the abstract. No new results.
2. Comparison with prior work under comparable protocols. Be exact about what is and is not comparable. If close prior work was not compared, say why.
3. Interpretation of why it works, labeled as interpretation ("We interpret this as...", "One explanation is..."), with the evidence for and against.
4. Utility for others: what can be reused (code, data, protocol, design principle), under which conditions it helps, when it will not (different scanner, anatomy, prevalence). This is the paragraph journals look for and AI drafts omit.
5. Limitations, ordered by how much they threaten the main claim. Each with its consequence ("single-site, so performance on other scanners is unknown") and, where possible, a number or planned test.
6. Concrete next step (a prospective study, a second site, a specific ablation), not "future work will explore more datasets".
7. Closing sentence that states the scope, not a quotable slogan.

Link back: the gap named at the end of the introduction should be answered in the same words in the Discussion's first paragraph.

## 6. Conclusion

Two to four sentences. What was found, in scoped terms. What it allows. What remains. No new claims, no slogan.

## 7. Flow techniques

Coherence comes from structure, not from transitions sprinkled onto paragraphs.

- **Spine.** The 12-line spine from SKILL.md. Every paragraph should serve a spine line. A paragraph that serves none is a cut candidate.
- **Reverse outline.** After drafting, write one sentence per paragraph stating its point. Read only those sentences. They should read as an argument. Gaps, duplicates and non sequiturs show up immediately.
- **Term sheet.** List every key concept (task, dataset, reference standard, method name, metric) with the single term used. Search the draft for drift. AI drafts alternate "ground truth", "gold standard", "reference", "labels".
- **Transition test.** For each paragraph, ask what question the previous paragraph left open and whether this one answers it. If not, either the order is wrong or a bridging sentence is missing. Prefer reordering over a "Moreover".
- **Old to new.** Open sentences with information the reader already has (the previous finding, the term just defined) and end with the new information. This gives momentum without connectives.
- **Gap to answer.** Intro gap and Discussion answer use the same words.
- **Figure and table pointers.** Introduce each figure with the claim it supports, not with "Figure 3 shows the results".

## 8. Repetition budget

The same finding appears at most five times, each with a different job:

| Place | Job |
|---|---|
| Abstract | Message with numbers |
| End of introduction | Headline, one clause |
| Results | Full evidence |
| Discussion, first paragraph | Meaning in clinical terms |
| Conclusion | Scoped takeaway |

If two places say the same thing in the same way, rewrite or remove one. Restating the Results paragraph at the start of the Discussion is the most common waste.
