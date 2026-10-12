# Findings papers: a framework and what it revealed

Some applied imaging papers do not propose a method that beats baselines and do not validate a tool on patients. They build a careful procedure (a framework, an audit, an evaluation protocol, an interpretability analysis) and report what it revealed about existing models or practices. The components are usually established methods. The contribution is their combination into one controlled procedure, the honesty of the experiments, and the findings.

Writing such a paper as if it were a method paper makes it look thin ("it only adds three labels to a heatmap"). Writing it as a list of analyses makes it unreadable. This file describes the shape that works.

## Contents
1. Recognizing the type
2. The throughline
3. Presenting the framework
4. Experiments in one repeated pattern
5. Negative controls and comparisons
6. Several datasets: give each a role
7. Positioning against existing methods
8. Clinical meaning without overclaiming
9. Making rigor visible
10. Section notes
11. Names, title and keywords

---

## 1. Recognizing the type

- The author says "the individual parts are not new, but the work is carefully engineered and the experiments are honest".
- There are many experiments, each answering a different question, and no single accuracy number is the headline.
- Results include negative and null findings that the author considers valuable.
- A draft framed around one product or one figure "feels shallow" to the author.

Ask the author to confirm the type before outlining. Do not shrink the paper to one result plus a supplement; the breadth is the contribution, and the task is to make the breadth readable.

## 2. The throughline

Write two or three sentences of this form and get the author's agreement:

> [Clinical users] are asked to rely on [the thing studied], and whether it deserves that reliance has not been tested for [setting]. We built a framework that [does what, in plain words] and used it to test [what]. [What held and what did not.]

A simple model studied on purpose is a strength, not an apology. A model that can be taken apart exactly gives a complete account against which approximate explanations can be judged. Say this proudly and state the limits it brings.

Give the experiments a hierarchy: three (at most four) headline findings in plain language, with the remaining experiments stated as support or as limits. The abstract and the discussion lead with the headline findings. Every experiment still appears in Methods and Results.

## 3. Presenting the framework

Authors rightly complain when "our approach is not highlighted anywhere". Present the framework as one thing, early, and then in detail.

- Introduction: the framework in two or three sentences, as numbered steps in words, with the overview figure.
- Methods: open with the same steps as a numbered list, each tied to its subsection and its equations. Then one subsection per step.
- Give the equations that define the framework: what is computed, on what, and what is reported. An applied journal expects them, and they are what makes the method reproducible. Introduce each with one plain sentence before it and one after it that says what the symbols mean for the reader. Keep derivations and settings in the Supplement.
- When the framework adapts an existing technique, name the adaptation, say exactly what was changed and why, and cite the original. "Our adaptation of X, which we call Y" is honest and gives the reader a handle. Do not present an adaptation as a new algorithm, and do not hide it in a subordinate clause.
- If the framework has an optional step that the results did not favour, present it as an option and report the result as a finding.
- A tool that displays the output is the display, not the contribution. Describe what it shows before naming it, and check with the author whether a product-like name helps or makes the work look lightweight.

## 4. Experiments in one repeated pattern

Number the experiments and use the same numbers, names and order in the Methods, the Results, the table of experiments and the figures. Readers lose track when Methods lists analyses that Results reports under different headings.

For each experiment, across Methods and Results:

1. **Why**: the question, phrased as one a clinician or user would ask. Open the Methods paragraph with "To test whether ..., we ...".
2. **What was done**: one or two sentences. Settings go to the Supplement.
3. **Control or comparison**: what would produce the same number without the effect.
4. **Finding**: one sentence with the number that matters.
5. **Meaning**: what it implies for the reader's practice.
6. **Limit**: one clause when the finding rests on one cohort, one model, or a post-hoc measure.

Items 1 to 3 belong in Methods and items 4 to 6 in Results, unless the journal uses a combined section. A table with one row per experiment (question, what is measured, control) is worth its space. Phrase experiment titles as the questions themselves.

Keep each Methods paragraph to a handful of sentences. If a reader says "I did not feel like reading all the details", the details belong in the Supplement and the meaning is missing from the main text.

## 5. Negative controls and comparisons

A result about an explanation or an analysis can arise from the procedure itself. Pair each result with a control and say which kind it is.

- Shuffled data: the labels or metadata of interest are reassigned at random and the analysis repeated. State whether the shuffling is applied to training or test data and where the result is measured.
- Random values: the quantity of interest is replaced by random values that pass through the same pipeline.
- Chance level: an observed overlap or agreement is compared with what is expected by chance for objects of the same size.

"Negative control" is a term clinical readers already know. Use it instead of "null", "permutation baseline" or "matched control" in the introduction and abstract, and explain it in one sentence the first time.

Report what the control changed. A reading that looked plausible and did not survive its control is a finding, and often the most useful one in the paper.

## 6. Several datasets: give each a role

Three datasets presented as three parallel tasks invite the question "why these?" and confuse readers when their names overlap (for example a cohort named for one organ inside a study named for the wider region).

- State the role of each dataset in one phrase: the one with expert ground truth, the large public one, the one that stress-tests a known weakness.
- Lead everywhere with the dataset that has ground truth. It anchors the claims.
- A small or confounded dataset should not lead, and should not be hidden. Give it the role its weakness suits (for example a known acquisition difference makes it the test bed for acquisition sensitivity) and say what its results cannot support.
- Refer to datasets by role-based names, and say once whether they share patients.
- Before moving a dataset to the Supplement, list which experiments exist only on it. Moving the dataset moves those experiments.

## 7. Positioning against existing methods

Related work describes other people's work only. The paper's own method or framework must not first appear there. Open the section with a sentence that says what it covers, and end it with a paragraph that states how the present study relates to the work reviewed.

In that closing paragraph, separate three levels and never blur them:

- **Run**: methods executed on the same data under the same protocol.
- **Adapted**: methods whose idea was applied in a modified form because the published version needs different inputs or models. Say what was changed.
- **Not run**: methods compared by their properties only, with the reason.

A properties table (what each method provides) is useful when the author wants the comparison to be visible; mark the row for the present work and add a column that states run, adapted or not run. Check the experiment record before writing this paragraph. Do not rely on the current manuscript to know what was compared.

## 8. Clinical meaning without overclaiming

Applied journals want to know what the findings mean for the user. Give each finding one sentence of consequence for the clinician ("a region marked as certain is not necessarily a region where the outline is correct"), and keep these limits:

- No reader study means no claim of clinical benefit. The findings define what should be checked, and what a future reader study should test.
- Observations about individual cases (what a single example appears to show) are questions the framework exposed, to be reviewed systematically by experts. They are not biological conclusions.
- The framework shows how a model behaves. Naming the anatomical or tissue structures involved, and saying why they matter, requires an expert.

## 9. Making rigor visible

Careful engineering is a selling point of this kind of paper, and readers cannot see it unless it is stated.

- Put the safeguards against data leakage in one short paragraph, as a numbered list: split unit, which model produced each analyzed prediction, no selection on test data, models unchanged across experiments.
- Separate two things that drafts tend to blur. Separation of patients between training and testing is one thing, and it may be strict. Independence of the analysis choices from the data is another, and in iterative work it is usually limited: settings chosen on one cohort, experiments added after earlier results, measures defined post hoc. State both, in that order.
- Report expectations that were not met. If expectations were written down before each analysis, say so and point to the list.
- Put the hardware and software environment in the reproducibility statement if the journal expects it. Ask the author; do not guess.

## 10. Section notes

- **Abstract.** Readable by someone who knows the clinical field and not the method. No coined terms. One number per headline finding.
- **Introduction.** Problem, why current practice cannot be trusted or is incomplete, the idea, the framework in brief, what the experiments ask (as questions, without answers), contributions as a numbered list of what the paper does, and a roadmap if the journal's papers have one. In engineering-style imaging journals the introduction carries no results and no findings; confirm the convention with the author (see `venue-registers.md`).
- **Results.** Begin with one worked example on real data that shows the framework's output before any statistics.
- **Discussion.** Lead with the headline findings and what they mean for the user, then for researchers, then limits and next steps.
- **Conclusion.** Close on what the framework makes possible and what it showed. A conclusion that lists defects of an existing practice makes the work look like a critique of that practice and nothing more.

## 11. Names, title and keywords

- A framework name helps readers and citations if it is simple and says what the thing is. Search for collisions before committing, and make sure the title does not echo the title of a paper in the reference list.
- Titles: lead with the name or the action, include the terms people search for (the task, the model family, the anatomy or modality), and keep it under about fifteen words.
- Keywords: standard terms of the field, not coined ones.
