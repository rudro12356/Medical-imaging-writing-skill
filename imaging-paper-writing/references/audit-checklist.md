# Audit checklist

Run after drafting or revising. Items marked (script) have a mechanical lead from `scripts/`. Everything else needs judgment.

## Contents
1. Spine fidelity
2. Claim-evidence ledger
3. Numerical consistency
3a. Provenance and integrity (experiment write-ups)
4. Statistics
5. Overclaim words
6. Flow audit
7. Readability and bloat audit
7a. Reader-load audit
8. Reporting checklists
9. Final report to the user

---

## 1. Spine fidelity

- Does the abstract state the clinical problem, approach, headline and scope from the spine?
- Does the end of the introduction state the same gap the Discussion answers?
- Is the paper written in the register the author confirmed (method, clinical evaluation, or findings)? Does the conclusion, read alone, convey what the work is?
- Is any paragraph unable to point to a spine line? Cut or justify.
- Is any spine line missing from the paper (for example utility for others)?

## 2. Claim-evidence ledger

Build a table of every claim in Abstract, Introduction end, Discussion and Conclusion.

| Claim | Where stated | Evidence (table/figure/number) | Scope of evidence | Status |
|---|---|---|---|---|

Status: supported / supported narrower / unsupported / only in abstract. Fix by scoping the claim down, adding the missing evidence (ask the user), or deleting. Claim creep, where a claim gets wider as it moves from Results to Abstract to Conclusion, is the most common finding.

## 3. Numerical consistency (script: number_audit.py)

- Every number in the text appears in a table or figure, or is derivable from one.
- Abstract numbers match Results to the same precision.
- Same metric uses the same rounding everywhere.
- Percent changes: state relative or absolute. Check the arithmetic by running it.
- n in text, table headers and captions agree.
- Do not "fix" a mismatch by choosing one number. Report it to the user and ask which is right.

## 3a. Provenance and integrity (experiment write-ups)

- Every number in the paper traces to a ledger row (run, commit, config, result file). Tables came from `results_to_table.py` or an equivalent script, not retyping.
- No experiment is described that is not completed in the ledger. Planned work appears only as future work.
- No completed experiment is described as "not run". Comparisons with existing methods are labeled run, adapted, or not run, after checking results folders, protocols and earlier manuscript versions, not only the current draft.
- Known confounds and failed expectations are still disclosed somewhere after every round of cuts.
- Methods text matches the code: split key, preprocessing, augmentation, loss, metrics, seeds (see `experiment-to-paper.md`, section 4).
- Test set not used for checkpoint, threshold or hyperparameter selection; number of test evaluations during development disclosed.
- Seeds: all completed seeds aggregated; no best-seed reporting; discarded runs documented and discarded for all arms.
- Tuning budget stated for the proposed method and for baselines.
- Every baseline run under the same protocol is reported or its omission explained.
- Negative, null and failure results from the record are reported in the main text or Supplement.
- Exploratory or post-hoc analyses are labeled.
- Dirty git tree or missing commit hash is disclosed or resolved.
- Reproducibility statement is true as written (code, data, environment availability).

## 4. Statistics

- Unit of analysis stated and independent (patient, not slice, patch, voxel or spot). Very small p-values (< 1e-10) usually mean pseudo-replication. (script flags)
- Paired data use paired tests.
- Multiple comparisons handled or acknowledged.
- CI or SD reported with the headline numbers; effect size before p.
- p reported as p < 0.001, not exponent form.
- "Comparable" or "no difference detected" when the difference is within SD/CI. Ablation prose must not describe in-noise deltas as improvements.
- Test set not used for tuning or model selection; say how selection was done.
- Baselines tuned with the same effort and budget as the proposed method, or the asymmetry stated.
- Seed variance reported or acknowledged for small differences.
- External validation: separate site/scanner/time period, or the limitation stated.

## 5. Overclaim words

| Word | Needs |
|---|---|
| generalizable / generalizes | at least two independent datasets or sites, not a random split of one |
| state-of-the-art / outperforms | named comparators, same protocol and data, margin with uncertainty |
| robust | the perturbation or shift named and tested |
| clinically useful / clinically relevant | a clinical metric, reader comparison, or threshold; or "may be useful, pending X" |
| novel / first | what is new, specifically, after a literature check |
| significant | a test, or use "large" / "clear" with the number |
| consistently | the number of settings and the exceptions |
| real-time | measured latency and hardware |
| interpretable / explainable | what was shown to a user and how validated |
| improves diagnosis / outcome | a diagnostic or outcome study; otherwise "improves segmentation accuracy" |

## 6. Flow audit

- Reverse outline written and read as an argument.
- Each paragraph answers the question the previous one raised.
- Term sheet applied: no drift, no one term doing two jobs.
- Figure and table callouts introduce a claim.
- Repetition budget: abstract, intro end, Discussion start, Conclusion do different jobs.
- No sentence-initial connective chains. Transitions come from ordering first, and then from link sentences that say why a paragraph follows the previous one.
- Every section and subsection opens with a sentence that says what it covers.
- Introduction (questions), Methods (experiments) and Results (findings) use the same items, names, numbers and order.

## 7. Readability and bloat audit

The reader must grasp the message fast. A paper that reports everything measured fails even when each sentence is clean.

- Can a skimmer who reads only the abstract, last intro paragraph, figure captions and first Discussion paragraph state the message in two sentences? If not, the message is buried or missing.
- Primary metric and primary comparison named in Methods and Results opening.
- Any sentence with four or more numbers: which does the reader need? Move the rest to a table or Supplement.
- Every table and figure earns its place. Test: remove it; does the argument change? If not, move to the Supplement.
- Per-structure, per-class, per-site detail is in the Supplement unless it is the finding.
- Extra ablations: keep those that test a claim in the paper; move the rest.
- Each figure caption is self-contained (what, n, unit, takeaway).
- Background the target reader already knows is cut.
- Count of main-text tables and figures is the smallest that carries the message.
- Cut order if long: repeated restatements, hedges and throat-clearing, secondary results, known background. Keep limitations and design reasons.

## 7a. Reader-load audit

Run this when an author or co-author says they "get lost", or after any tightening pass. It catches over-compression (see `slop-sci.md`, section 4).

- Abstract: list every noun phrase a clinician outside the project would not know. Each is replaced by a description or removed.
- Every term is explained in plain words before or at its first use. A glossary table does not excuse a term used before its explanation.
- No sentence carries more than one new term.
- No clipped declaratives, colon-joined sentences in running text, or bare "this" and "it".
- Each experiment states why it was run and what its control or comparison is.
- The method or framework is presented as a whole before its parts, and equations appear where the method is defined.
- The paper's own method does not first appear in related work; related work ends with the relation to the present study.
- The introduction contains no results if the venue's introductions carry none.
- Each dataset has a stated role and one name; the paper says whether datasets share patients.
- One default per method setting across Methods, figures and Discussion.
- Co-author comments: every comment has a response; tracked edits (spelling variant, names, word choices) are applied throughout; highlights without notes were asked about.
- Headings name the question answered, not an abstract noun.

## 8. Reporting checklists

Ask the user which applies and whether the journal requires it. Common ones: CLAIM (imaging AI), TRIPOD+AI (prediction models), STARD (diagnostic accuracy), CONSORT-AI (trials), MI-CLAIM. Check that the manuscript text contains the items they ask for, such as data source, split method, reference standard and performance with CI. Do not assert compliance.

## 9. Final report to the user

Short. Include: a comment-by-comment table when the author supplied comments, with anything you did differently from what was asked in its own section; runs used and runs excluded with reasons; integrity flags and how each was handled; structural changes made; claims narrowed; `[TODO]` and `[cite?]` items; numerical mismatches needing a decision; statistics concerns; material moved to the Supplement (list); any edit that touched technical meaning; open questions (register, target journal). Offer the claim ledger if it is long.
