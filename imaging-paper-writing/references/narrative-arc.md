# Narrative arc: the job of each section

The arc: clinical motivation, then methods with the reason for each choice, then results with their meaning, then discussion of utility for others in the field. Every section must hand the reader to the next with the same terms and the same question in view.

## Contents
1. Abstract
2. Introduction
3. Related work (when it is a separate section)
4. Methods
5. Results
6. Discussion
7. Conclusion
8. Flow techniques
9. Repetition budget

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
- Plain words only. The abstract must be readable by someone who knows the clinical field and has not read the paper. Any label you coined while working (a name for a quantity, a step, a property) is unknown to that reader; replace it with a short description of what it is. If the author says they "get lost" in the abstract, count the coined nouns.
- One number per finding. Three or four findings with one number each are read; a Results block with twelve numbers is not.
- Check the word limit with a script, not by eye.

## 2. Introduction

Job: make the reader care about a specific clinical problem, show exactly where current approaches stop, and state what this paper does about it.

Paragraph plan (3-5 paragraphs, usually under 700 words for a method paper):

1. Clinical stake. Who is affected, which decision or workflow, what it costs (time, missed findings, variability, access). One or two sentences of epidemiology or workflow are enough. Cite a source.
2. Limits of current practice. Name what fails: inter-reader variability, scan time, label scarcity, scanner differences, interpretability. A number if one exists.
3. Prior AI work, grouped by what it leaves open, not chronologically. Template: "Approaches based on X reach Y but need Z [refs]. Approaches based on W avoid Z but [limit] [refs]." Close with the gap in clinical terms.
4. This work. Aim or hypothesis, approach in a sentence, why it targets the gap. Whether the headline finding is stated here depends on the venue (see below).
5. Optional contributions, at most four short items, as a numbered list when the journal's papers use one. Each must add information beyond the abstract: name the specific thing (a framework, a dataset, a design choice, an analysis).

**Findings in the introduction: check the convention.** Nature-style journals expect the headline here ("Here we show..."). Engineering-style imaging journals (SPIE, IEEE, many JBO and JMI papers) and many senior authors expect the introduction to introduce the problem and the approach lightly and to contain no results at all: no numbers, no "we found", no worked example taken from the Results. In that convention, say what the experiments ask, as questions, and list contributions as what the paper does. If you do not know which convention applies, ask; if you cannot ask, keep findings out of the introduction of an engineering-style journal.

**Explain, then name.** Introduce each concept in plain words first and give its term afterwards ("the network is run several times with small random changes, and the spread of its outputs shows how unsure it is; we call this spread the uncertainty of the voxel"). A reader who meets the term first has to hold an empty label until the explanation arrives. Terms that the clinical audience already uses ("negative control", "ground truth", "favors") cost nothing; use them in place of statistical or machine-learning jargon where they are accurate.

Failures to avoid: starting with the history of deep learning; a roll-call of papers ("Smith et al. proposed... Jones et al. proposed..."); a gap defined in technical terms only; an example or result borrowed from later sections; ending with a table-of-contents paragraph ("The rest of this paper is organized as...") unless the journal's papers have one, in which case include it.

## 3. Related work (when it is a separate section)

Job: show what exists, what each line of work leaves open, and where the present study stands.

- Open with one sentence that says what the section covers. A heading followed directly by the first group of citations reads as a jump.
- Group by what each line of work does and leaves open, one short paragraph per group, with a named subject for every sentence ("Method A builds this property into the model"), not chains of "their" and "it".
- Describe other people's work only. The paper's own method must never be introduced here for the first time ("in this study, X is used to...") ; that belongs in the Introduction and Methods.
- End with a paragraph on the relation to the present study: what the reviewed work has not measured or provided, and how the present study compares with it. State which methods were run on the same data, which were included in adapted form, and which were not run (see `findings-papers.md`, section 7). Verify this against the experiment record.
- If a comparison table of method properties is used, mark the row for the present work and keep the caption formal.

## 4. Methods

Job: let another group reproduce the work and let a reviewer see that the evaluation was fair.

Order: ethics and data, reference standard, preprocessing, model, training, evaluation protocol (splits, leakage controls, metrics, statistics), baselines. When the paper's contribution is a method or framework, present it first, as a whole, before data and experiments: open the section with its steps as a short numbered list, each tied to a subsection and its equations, so that a reader can see the approach before reading its parts.

- Open every subsection with one or two sentences that say what it covers and why it follows the previous one. A subsection that starts with a definition or an equation reads as a jump.
- Include the equations that define the method. Applied journals expect them. Put one plain sentence before each equation (what is being computed) and one after (what the symbols mean for the reader). When a quantity has a common name and a formal one (probability and score, for example), say how they relate and which one the method works on.
- Describe experiments under the same numbers and names that the Results will use. Open each with its reason ("To test whether ..., we ...") and name its control or comparator.
- For your own terms write "we refer to X as ..." or "we call X ...". "X is called ..." implies an established term and invites a request for a citation.
- State safeguards against data leakage together, in one short paragraph, and keep them separate from the statement of which analysis choices depended on the data (see `findings-papers.md`, section 9).

- For every design choice that is not standard, one sentence of reason tied to the problem: what it does, why the problem needs it, what it costs. "A frequency-domain branch was added because the artifact is periodic in k-space; it adds 12% parameters."
- Say what the split unit is (patient, not slice) and how leakage was prevented.
- Say how hyperparameters were chosen for the proposed method and for baselines, and give baselines equal effort. If not equal, say so.
- Metrics: define each once, say which is primary. Do not define metrics you will not report in the main text.
- Statistics: test, unit of analysis, multiple-comparison handling, CI method.
- Put detail that only a replicator needs (full hyperparameter table, augmentation parameters) in the Supplement or code repository, with a pointer.

## 5. Results

Job: show whether the approach works, how much, where it fails, and what that means.

Order: cohort and data description; headline result; what drives it (ablation or analysis, only those that matter); where it fails; robustness or external validation; comparison with human readers if relevant; qualitative examples. When Methods numbered the experiments, report them under the same numbers, names and order. For a paper whose output is new to the reader, begin with one worked example on real data before any statistics.

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

## 6. Discussion

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

## 7. Conclusion

Two to four sentences. What was found, in scoped terms. What it allows. What remains. No new claims, no slogan. Read it alone, as a skimming reviewer will: it should convey what the work is and why it matters, not only list defects of an existing practice.

## 8. Flow techniques

Coherence comes from structure first: a paragraph in the wrong place cannot be saved by a connective. Once the order is right, the links still have to be written down. A reader who is new to the work cannot infer why one paragraph follows another, and prose that has been compressed to bare claims reads to them as abrupt and unfinished.

- **Link sentences.** Open each paragraph with a sentence that carries the reader from the previous one: what was just established, and what question it raises ("These limits cannot be measured at the training hospital alone. Measuring them requires ..."). This is a full sentence with content, not a connective word.
- **Complete sentences.** Every sentence names its subject and says what it refers to. Avoid clipped declaratives that lean on the previous sentence ("Such a dataset exists." "The results are mixed."), sentences that begin with a bare "This" or "It", and two clauses joined by a colon in running text. Colons introduce lists and equations. Authors and senior readers in applied journals read clipped constructions as informal or incomplete.
- **One idea per sentence, in the order subject, verb, object.** Purpose clauses stacked in front of the subject ("So that a reader can verify X, the output is usually accompanied by Y") are harder to parse than the plain order.

- **Spine.** The 12-line spine from SKILL.md. Every paragraph should serve a spine line. A paragraph that serves none is a cut candidate.
- **Reverse outline.** After drafting, write one sentence per paragraph stating its point. Read only those sentences. They should read as an argument. Gaps, duplicates and non sequiturs show up immediately.
- **Term sheet.** List every key concept (task, dataset, reference standard, method name, metric) with the single term used. Search the draft for drift. AI drafts alternate "ground truth", "gold standard", "reference", "labels".
- **Transition test.** For each paragraph, ask what question the previous paragraph left open and whether this one answers it. If not, either the order is wrong or a link sentence is missing. Fix the order first, then write the link. A "Moreover" is neither.
- **Old to new.** Open sentences with information the reader already has (the previous finding, the term just defined) and end with the new information.
- **Mirrored sections.** The same items in the same order with the same names in Introduction (questions), Methods (experiments) and Results (findings). A reader who meets an analysis in Results that Methods did not announce feels that things arrive unannounced.
- **Gap to answer.** Intro gap and Discussion answer use the same words.
- **Figure and table pointers.** Introduce each figure with the claim it supports, not with "Figure 3 shows the results".

## 9. Repetition budget

The same finding appears at most five times, each with a different job:

| Place | Job |
|---|---|
| Abstract | Message with numbers |
| End of introduction | Headline, one clause (Nature-style venues); aim and contributions without results (engineering-style venues) |
| Results | Full evidence |
| Discussion, first paragraph | Meaning in clinical terms |
| Conclusion | Scoped takeaway |

If two places say the same thing in the same way, rewrite or remove one. Restating the Results paragraph at the start of the Discussion is the most common waste.
