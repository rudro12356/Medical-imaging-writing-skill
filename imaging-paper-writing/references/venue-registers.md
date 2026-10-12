# Registers and venues

Based on a close reading of roughly eight open-access applied deep-learning imaging papers (Nature Communications, Communications Medicine, Frontiers in Radiology, JBO, SPIE JMI, including two 2026 JMI method papers). This is a small sample. Use it as guidance, then check the target journal's current author guidelines, which always win.

## Contents
1. Three registers
2. Journal formats
3. Habits to borrow from clinical papers into method papers
4. Caveats

---

## 1. Three registers

**Clinical-evaluation register** (tool validated on patients, reader studies, trials).
- Opens with the clinical question and the cohort.
- Methods fix the protocol before testing (pre-specified endpoints, splits, reference standard).
- Results report confidence intervals on headline numbers, subgroup and failure analyses.
- Discussion compares with clinician performance and states the intended use and its limits.
- Abstract claims are scoped to the table.

**Method register** (new architecture, loss, reconstruction, acquisition).
- Opens with the clinical bottleneck, then moves quickly to the technical gap.
- Methods are heavier: architecture, loss, training detail, and why each component exists.
- Results are comparison tables against baselines plus ablations.
- Weaker spots seen in the sample: baselines tuned less than the proposed method, ablation prose that overstates differences inside the SD, p-values computed on pooled voxels or spots as if independent, abstract claims wider than the Results, close prior work cited but not compared, thin limitations, promotional wording ("consistently", "robust", "seamlessly", "exceptional", "pressing need").
- The 2026 JMI method papers followed the problem, method, results, discussion arc only loosely. The clinical papers followed it tightly. Do not assume a method paper in a good journal meets the arc; write to it deliberately.

**Findings register** (a framework, audit, evaluation protocol or interpretability study, and what it revealed).
- The components are established; the contribution is their combination into one controlled procedure and the findings it produced, including negative ones.
- Opens with the clinical user and what they are asked to rely on, then why it should be tested, then the framework.
- Methods present the framework as numbered steps with their equations, then a numbered set of experiments, each with a reason and a control.
- Results follow the same numbering; each finding is followed by its meaning for the user.
- The risk is not overclaiming a method but burying the work: a list of analyses with coined names, or a paper reduced to one result so that the rest looks like padding. See `findings-papers.md`.

Journals between the registers (for example JBO): optics or device paper with a clinical use case. Lead with the use case, then the device or method, then evaluation.

Ask the author which register the paper is in before outlining. A paper pushed into the wrong register reads as either inflated or shallow, and no amount of sentence work fixes that.

## 2. Journal formats

Verify before writing; formats change.

| Venue | Notes seen in the sample |
|---|---|
| Nature Communications | Results before Methods. Introduction ends with "Here we show..." and the headline. Short, declarative Results subsections with claim-style headings. Methods at the end, detailed. Supplement used heavily. |
| Communications Medicine | Plain-language summary alongside abstract. Clinical framing prominent. Reporting-guideline statements. |
| Frontiers in Radiology | Structured sections, CRediT author contributions, data availability, ethics statement, often an impact or significance statement. |
| JBO (Journal of Biomedical Optics) | Structured abstract with Significance, Aim, Approach, Results, Conclusions. Optics-forward Methods. |
| SPIE JMI (Journal of Medical Imaging) | Structured abstract Purpose, Approach, Results, Conclusions (check the word limit). Conventional order: Introduction, optional Related Work, Methods, Results, Discussion, Conclusion. Disclosures, Code and Data Availability, Acknowledgments; optional author biographies; a caption list in the submission file. Method papers dominate; Methods heavy, with equations. In one group's experience (2026), senior authors expected no results in the Introduction, a roadmap sentence at its end, US spelling, and a formal register without colon-joined sentences. |

When the user names a journal, ask them to paste the section list or guideline summary if it is not obvious. Do not invent journal requirements.

## 3. Habits worth borrowing from clinical papers into method papers

1. Fix the evaluation protocol before looking at test results and say so.
2. Put confidence intervals on the headline numbers.
3. Analyze failure cases and report where the method does not help.
4. Make the limitation concrete: attach a number or a specific untested condition.
5. Scope abstract claims to what the tables show.
6. Name the unit of analysis and its independence.
7. State intended use: who would run this, on what input, and what decision it informs.
8. Describe the reference standard and its uncertainty.

## 4. Caveats

- The sample is small and skewed to open-access papers; closed-access SPIE content could not be read in full.
- Journals vary by editor and subfield. The register recommendation is a default, not a rule.
- Conventions also vary by research group. A senior co-author's tracked edits and comments show the house style better than any guideline; follow them, and record them as a list for later sections.
- If the user's field is not imaging (for example pathology, genomics, clinical NLP), the arc still holds but the journal formats above may not.
