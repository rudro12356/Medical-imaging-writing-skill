---
name: imaging-paper-writing
description: Draft, rewrite, polish or critique any section of an applied machine-learning paper in medical imaging or clinical AI (abstract, introduction, methods, results, discussion, conclusion, cover letter, rebuttal), so it reads clearly, flows from clinical problem to utility for the field, and carries one graspable message instead of a pile of metrics. Use whenever the user is writing or editing a manuscript for journals such as Nature Communications, Communications Medicine, Frontiers in Radiology, JBO, or SPIE JMI, or says a draft "sounds like AI", "is slop", "doesn't flow", "is bloated", "has too many results/metrics", or asks to tighten, restructure or sanity-check a paper. Also use when the user has completed coding experiments (repo, configs, logs, result files) and wants them written up end to end honestly, with every claim traced to a real run. Builds on stop-slop with rules adapted for scientific prose. Use it even when the user only pastes a paragraph and says "improve this".
---

# Imaging paper writing

A good applied imaging paper can be skimmed in two minutes and the reader leaves knowing one thing: what clinical problem was addressed, what was done about it, whether it worked, and who else can use it. Most AI-drafted manuscripts fail in two ways. The sentences are slop (inflated, generic, hedged). The paper has no spine, so each section is locally fine and the whole does not cohere. This skill fixes both, and it holds the line on a third failure: bloat.

Prose rules here are adapted from [stop-slop](https://github.com/hardikpandya/stop-slop) (MIT, Hardik Pandya). See `NOTICE`. Stop-slop's blanket rules would damage scientific writing (it bans all adverbs, passive voice and hedging), so `references/slop-sci.md` keeps what transfers and relaxes what does not.

## Hard boundaries (read first)

- Never invent numbers, citations, cohort details, p-values, hardware, ethics approvals or dataset names. If the spine or draft lacks something, insert `[TODO: what is needed]` or `[cite?]` and list it at the end.
- Describe only what was actually run. A planned, crashed, partial or abandoned experiment is not a result. Every reported number traces to a completed run, a config and a result file. Report negative and null results, the selection procedure, and the tuning budget. Never cherry-pick seeds, baselines or checkpoints, never select on the test set, and decline requests to do so (see `references/experiment-to-paper.md`, section 8) while offering the honest alternative.
- Polishing must not strengthen a claim. If an edit changes technical meaning, scope or a number, flag it explicitly.
- Do not rename the author's method, metrics or terms unless the term sheet shows drift.
- The author's target journal guidelines override anything here.

## Workflow

### 0. Ground the paper in the experiment record (when code or results exist)

If the user has completed experiments, the paper is written from the record, not from memory or from an earlier draft. Follow `references/experiment-to-paper.md`:

1. Inventory the project: `python scripts/experiment_inventory.py PROJECT_DIR`.
2. Build the experiment ledger: one row per run with commit, config, split, seeds, status (completed / partial / crashed / abandoned / exploratory), selection rule and result file. Ask the user about anything the files do not show.
3. Read the code behind each Methods claim (patient-level split, test set untouched, preprocessing, baselines, metrics, seeds). If the code contradicts the intended story, stop and tell the user before drafting. Offer: describe it as it is, re-run, or narrow the claim.
4. Generate tables from result files: `python scripts/results_to_table.py results.csv --group method --metrics dice --unit-col patient --ci`.
5. Set the claim ceiling at the weakest link (single seed, test reuse, unequal tuning, random split, one site).

Skip this step only when there is no experiment record and the user is editing prose they wrote.

### 1. Build the paper spine before writing anything

Without a spine, the model produces plausible paragraphs that do not answer each other. Get these from the user (or from their draft) and write them out in at most 12 lines. Ask only for what is missing; never fill gaps by guessing.

1. Clinical problem: who, what decision or workflow, what it costs today.
2. What current practice or prior AI work fails to do, in concrete terms.
3. Approach in one sentence, and why it addresses that failure.
4. Data: source, size, unit of analysis (patient, scan, region), reference standard.
5. Headline result: one sentence with the numbers that matter and the comparator (taken from the ledger when experiments exist).
6. What the result means in clinical or practical units.
7. Main limits.
8. Utility for others: what they can reuse, when it will help, when it will not.
9. Target journal and register (see `references/venue-registers.md`).

The headline (item 5 and 6) is the paper's message. Everything else serves it.

### 2. Pick the register

Clinical-evaluation papers (reader studies, validation, trials of a tool) lead with the clinical question and the cohort. Method papers (new architecture, loss, acquisition or reconstruction approach) lead with the clinical bottleneck, then the technical idea. Both must close the loop to clinical or field utility. Details in `references/venue-registers.md`.

### 3. Draft or revise section by section

Follow the job of each section in `references/narrative-arc.md`. Short version:

| Section | Job | Common AI failure |
|---|---|---|
| Abstract | Message plus key numbers, scoped | Results block with no numbers; claims wider than the data |
| Introduction | Clinical stake, concrete gap, aim | Generic "deep learning has revolutionized"; chronological roll-call of prior work |
| Methods | What was done and why each choice | Method list with no reason; unequal baseline treatment |
| Results | Claim, evidence, meaning | Bare numbers; every metric reported |
| Discussion | Meaning, comparison, utility, limits | Restating results; no limitations with consequences |
| Conclusion | 2-4 scoped sentences | Quotable closer; new claims |

### 4. Run the audits

Run deterministic checks, then judgment checks.

```
python scripts/slop_scan.py draft.md
python scripts/number_audit.py draft.md --tables tables.md   # tables file optional
```

These give leads, not verdicts. Then work through `references/audit-checklist.md`: spine fidelity, claim-evidence ledger, numbers, provenance and integrity, statistics, flow, and the readability/bloat audit.

### 5. Score and report

Score the revised text 1-10 on each dimension:

| Dimension | Question |
|---|---|
| Directness | Does each paragraph open with its point? |
| Specificity | Named datasets, numbers, comparators instead of "recent methods", "good performance"? |
| Evidence tie | Is every claim followed by evidence and, where it matters, meaning? |
| Flow | Does each paragraph answer the question the previous one raised? Same term for the same thing? |
| Calibration | One hedge per claim at most; no overclaim words without support? |
| Human voice | Varied rhythm, an author who made choices, no template smell? |

Below 42/60, revise again. The score is a forcing function, not a measurement; do not present it as objective.

Report to the user briefly: what changed structurally, what you could not verify, `[TODO]` items, any edit that touched technical meaning, and open questions. When the paper came from experiments, add the integrity report: runs used and runs left out with reasons, flags found and how each is handled in the text, claims narrowed, and requests declined. Do not narrate every sentence edit.

## Readability and restraint

Good journals are easy to read. The reader should grasp the message quickly and not wade through everything the authors measured. Bloat is as harmful as slop and AI drafts produce it by default, because every number is available and nothing is costly to include.

Rules:

- One paper, one message. State it in the abstract's first lines, the last paragraph of the introduction, and the first paragraph of the discussion, each in different words and doing a different job.
- The main text carries only results that support or honestly qualify the message. Everything else goes to the Supplement: secondary metrics, per-structure or per-class tables, extra ablations, hyperparameter sweeps, additional visualizations.
- Name the primary metric and the primary comparison before drafting Results. Report secondary metrics in one sentence ("secondary metrics agreed; Supplementary Table 3") unless one changes the conclusion.
- No metric dumps. If a sentence lists four or more numbers, ask which one the reader needs and whether a table or figure should carry the rest.
- Each table and figure must be self-contained (caption says what is shown, the unit, the n, the takeaway) and earn its place. If removing it changes nothing in the argument, move it.
- Prefer one clear figure showing the headline over five figures showing everything.
- Skim path: a reader who reads only the abstract, the last intro paragraph, figure captions and the first discussion paragraph should be able to state the message in two sentences. Check this explicitly.
- Length is a cost to the reader. When trimming, cut in this order: repeated restatements, hedges and throat-clearing, secondary results, background the target reader knows. Do not cut limitations or the reason behind a design choice.

## Integrity when writing up experiments

Honest write-up is also what makes a paper credible and easy to trust at a glance. Core habits:

- The ledger decides what exists. If a run is not in the ledger as completed, the paper does not claim it.
- Report the aggregate over all completed seeds, with spread. Not the best seed.
- Select checkpoints, thresholds and hyperparameters on validation data only. If the test set was used for any of that, say so and treat the test result as optimistic.
- Give baselines the same data, split, preprocessing and comparable tuning effort, or state the asymmetry.
- State the unit of analysis; compute SDs and CIs across patients.
- Write limitations from the flags actually found in the record (single site, test reuse, single seed, no external set), each with its consequence.
- Label analyses not pre-specified as exploratory. Keep exploratory detail in the Supplement, not hidden and not in the headline.
- Honest does not mean bloated: the main text still carries the primary result and anything that changes the conclusion; the rest is disclosed in the Supplement.

## Voice rules (summary; full lists in references)

- Lead with the point. Cut openers that announce ("It is important to note that", "Importantly,", "Notably,").
- Use the specific noun and the number. "Segmentation error in the left ventricle fell from 4.1 to 2.9 mm" beats "substantially improved performance".
- Claim verbs need subjects that can act: authors, data, models. "Results confirm" is false agency; write "The model reached X on the held-out site."
- Use "show" over "demonstrate", "use" over "leverage", "help" over "facilitate".
- No em dashes. Use commas, parentheses, colons or a new sentence.
- No promotional vocabulary: robust, seamless, novel (unless truly the first, and say what), state-of-the-art (unless you name the comparator and protocol), superior, exceptional, pivotal, paradigm shift, pressing need.
- Intensifiers and softeners are out ("very", "highly", "quite", "somewhat"). Measurement and method adverbs are fine ("retrospectively", "independently", "approximately"). "Significantly" only with a test result nearby.
- Passive voice is fine for procedures where the actor is irrelevant ("Images were resampled to 1 mm isotropic"). It is not fine for claims or to hide who decided something.
- Hedge once and calibrate: "suggests" when the evidence is indirect; no "may potentially possibly".
- Use "we" for authors' choices and claims. Never "you".
- Vary rhythm. Do not end every paragraph with a one-line restatement. No dramatic fragments, no rhetorical question setups.
- Term sheet: one name per concept for the whole paper (for example "reference segmentation", not alternating with "ground truth", "gold standard", "label").

## Editing mode

When the user supplies text and asks to improve it:

1. Diagnose first in a few lines: what the paragraph is trying to do, where it stalls (slop, missing reason, missing meaning, wrong place, bloat).
2. Preserve the author's voice and technical content. If they asked to "polish", make minimal edits and say so.
3. If the problem is structural (sections do not connect), say that plainly and propose the structural fix before touching sentences. Polishing sentences cannot rescue a missing spine.
4. Return the revised text, then a short list of changes that matter and any flags. Use `references/examples.md` for the before/after pattern.

## Drafting from scratch

Write from the spine and the user's actual data. Where the user has given results, use exactly their numbers. Where the paper needs something they have not given, mark it. Start with the abstract's first sentence and the introduction's last paragraph, because they fix the message; then write the rest around them.

## Reference files

- `references/narrative-arc.md`: job of each section, paragraph templates, flow techniques (reverse outline, term sheet, transition test, repetition budget).
- `references/slop-sci.md`: adapted phrase and structure lists, with replacements; AI-draft incoherence patterns.
- `references/venue-registers.md`: two registers, per-journal formats, habits worth borrowing across registers. Based on a small sample (about eight papers); treat as guidance and check author guidelines.
- `references/audit-checklist.md`: claim-evidence ledger, numbers, statistics, overclaim words, flow audit, readability/bloat audit.
- `references/examples.md`: before and after pairs in imaging contexts (numbers are invented for illustration).
- `references/experiment-to-paper.md`: writing up completed experiments end to end: inventory, ledger, code-versus-story checks, what to report and disclose, requests to decline.
- `scripts/slop_scan.py`, `scripts/number_audit.py`: mechanical prose and number checks.
- `scripts/experiment_inventory.py`: read-only inventory of a project's configs, logs, results, checkpoints and code-level leads, with a ledger skeleton.
- `scripts/results_to_table.py`: markdown results table from a per-run CSV (mean ± SD or bootstrap CI across independent units).
