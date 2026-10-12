---
name: imaging-paper-writing
description: Draft, rewrite, polish or critique any section of an applied machine-learning paper in medical imaging or clinical AI (abstract through conclusion, cover letter, rebuttal) so it reads clearly, flows from clinical problem to utility, and carries a graspable message instead of metrics or private jargon. Use for manuscripts aimed at journals such as Nature Communications, Communications Medicine, JBO or SPIE JMI; when a draft "sounds like AI", "is slop", "is bloated", "is shallow", "doesn't flow", or the user, a supervisor or a reviewer "can't follow it"; when the user brings a commented Word file or annotated PDF from a co-author; when rewrites keep failing; and when they want to brainstorm the story, title or outline before writing. Also use to write up completed experiments (repo, configs, logs, results) honestly, with every claim traced to a real run, including findings, interpretability, audit or evaluation-framework papers. Use it even when the user only pastes a paragraph and says "improve this".
---

# Imaging paper writing

A good applied imaging paper can be skimmed in two minutes and the reader leaves knowing what clinical problem was addressed, what was done about it, what was found, and who else can use it. AI-drafted manuscripts fail in four ways, and this skill addresses all of them:

1. **Slop.** Inflated, generic, hedged sentences.
2. **No spine.** Each section is locally fine and the whole does not cohere.
3. **Bloat.** Everything measured is reported, so the message is buried.
4. **Over-compression and wrong identity.** The draft is tidy but written in the writer's private labels and clipped sentences, or the work is squeezed into the wrong kind of paper, so the author and the senior reader "get lost" or find it "shallow". Fixing slop tends to cause this failure. A human reader's verdict outranks any scan or score.

Prose rules here are adapted from [stop-slop](https://github.com/hardikpandya/stop-slop) (MIT, Hardik Pandya). See `NOTICE`. Stop-slop's blanket rules would damage scientific writing (it bans all adverbs, passive voice and hedging), so `references/slop-sci.md` keeps what transfers and relaxes what does not.

## Hard boundaries (read first)

- Never invent numbers, citations, cohort details, p-values, hardware, ethics approvals or dataset names. If the spine or draft lacks something, insert `[TODO: what is needed]` or `[cite?]` and list it at the end. Verify a citation before adding it.
- Describe only what was actually run. A planned, crashed, partial or abandoned experiment is not a result. Every reported number traces to a completed run, a config and a result file. Report negative and null results, the selection procedure, and the tuning budget. Never cherry-pick seeds, baselines or checkpoints, never select on the test set, and decline requests to do so (see `references/experiment-to-paper.md`, section 8) while offering the honest alternative.
- The current manuscript is not the record. Before saying an experiment or comparison was not run, check the results, the protocols and earlier manuscript versions.
- Polishing must not strengthen a claim. If an edit changes technical meaning, scope or a number, flag it explicitly. If asked to delete a sentence that discloses a confound or limitation, keep the fact disclosed somewhere and tell the author.
- Do not rename the author's method, metrics or terms unless the term sheet shows drift or the author agrees.
- The author decides what kind of paper this is and what its contribution is. Do not shrink the work to fit a template.
- The author's target journal guidelines, and the house style shown by a senior co-author's edits, override anything here.

## Workflow

### 0. Ground the paper in the experiment record (when code or results exist)

If the user has completed experiments, the paper is written from the record, not from memory or from an earlier draft. Follow `references/experiment-to-paper.md`:

1. Inventory the project: `python scripts/experiment_inventory.py PROJECT_DIR`.
2. Build the experiment ledger: one row per run with commit, config, split, seeds, status (completed / partial / crashed / abandoned / exploratory), selection rule and result file. Ask the user about anything the files do not show.
3. Read the code behind each Methods claim (patient-level split, test set untouched, preprocessing, baselines, metrics, seeds). If the code contradicts the intended story, stop and tell the user before drafting. Offer: describe it as it is, re-run, or narrow the claim.
4. Generate tables from result files: `python scripts/results_to_table.py results.csv --group method --metrics dice --unit-col patient --ci`.
5. Set the claim ceiling at the weakest link (single seed, test reuse, unequal tuning, random split, one site).

Skip this step only when there is no experiment record and the user is editing prose they wrote.

### 1. Read the comments and find the level that is broken

If the user brings co-author or reviewer comments, extract all of them before forming a view:

```
python scripts/docx_comments.py manuscript.docx     # comments, anchors, tracked changes
python scripts/pdf_comments.py annotated.pdf        # highlights and notes with their text (needs PyMuPDF)
```

A rendered PDF page shows a highlight but not the note typed into it, so always run the script on the file itself, and run it again each time the author says they commented.

Then diagnose in this order, and tell the user which level you think is broken before changing anything: **identity** (is this being written as the right kind of paper?), **structure** (is there a sequence the reader can hold?), **sentences**. If an earlier rewrite fixed sentences and the complaint remained, the problem is one level up.

When the user is stuck in a loop of rewrites, wants to brainstorm, or asks for a whole-manuscript rewrite, do not deliver a full new draft in one pass. Agree the throughline, the approach in two sentences, the purpose of each experiment, the vocabulary and the outline first, then draft in stages with a review build after each. `references/working-with-authors.md` describes this process, including how to answer a round of comments and what to do when the author's hopes and the results disagree.

### 2. Build the paper spine before writing anything

Without a spine, the model produces plausible paragraphs that do not answer each other. Get these from the user (or from their draft) and write them out in at most 12 lines. Ask only for what is missing; never fill gaps by guessing.

1. Clinical problem: who, what decision or workflow, what it costs today.
2. What current practice or prior AI work fails to do, in concrete terms.
3. Approach in one or two sentences, and why it addresses that failure.
4. Data: source, size, unit of analysis (patient, scan, region), reference standard, and the role of each dataset when there are several.
5. Headline result: one sentence with the numbers that matter and the comparator (taken from the ledger when experiments exist). For a findings paper, three or at most four headline findings, with the other experiments as support.
6. What the result means in clinical or practical units.
7. Main limits.
8. Utility for others: what they can reuse, when it will help, when it will not.
9. Target journal and register (see `references/venue-registers.md`).

The headline (items 5 and 6) is the paper's message. Everything else serves it.

### 3. Pick the register

- **Clinical evaluation** (reader studies, validation, trials of a tool): lead with the clinical question and the cohort.
- **Method** (new architecture, loss, acquisition or reconstruction approach): lead with the clinical bottleneck, then the technical idea.
- **Findings** (a framework, audit, evaluation protocol or interpretability study, and what it revealed): the parts are established, and the contribution is the controlled procedure and its findings. Lead with what the clinical user is asked to rely on and why it should be tested. Keep every experiment, in one repeated pattern. See `references/findings-papers.md`.

All three must close the loop to clinical or field utility. Confirm the register with the author; details in `references/venue-registers.md`.

### 4. Draft or revise section by section

Follow the job of each section in `references/narrative-arc.md`. Short version:

| Section | Job | Common AI failure |
|---|---|---|
| Abstract | Message plus key numbers, scoped, in plain words | No numbers; claims wider than the data; coined terms the reader has never seen |
| Introduction | Clinical stake, concrete gap, aim and approach | Generic "deep learning has revolutionized"; roll-call of prior work; results placed here in a venue whose introductions carry none |
| Related work | What exists, what it leaves open, where this study stands | The paper's own method first introduced here; no closing statement of what was compared and how |
| Methods | The approach as a whole, then what was done and why each choice | Method list with no reason; no equations; framework never presented as one thing; unequal baseline treatment |
| Results | Claim, evidence, meaning, in the order Methods announced | Bare numbers; every metric reported; analyses that Methods never introduced |
| Discussion | Meaning, comparison, utility, limits | Restating results; no limitations with consequences |
| Conclusion | 2-4 scoped sentences on what the work is and allows | Quotable closer; new claims; a list of defects that makes the work look shallow |

For anything longer than a section, draft the abstract and introduction first and get the author's reaction before continuing. They fix the register and the message and are cheap to redo.

### 5. Run the audits

Run deterministic checks, then judgment checks.

```
python scripts/slop_scan.py draft.md
python scripts/number_audit.py draft.md --tables tables.md   # tables file optional
```

These give leads, not verdicts. A clean scan does not mean a readable paper. Then work through `references/audit-checklist.md`: spine fidelity, claim-evidence ledger, numbers, provenance and integrity, statistics, flow, the readability and bloat audit, and the reader-load audit.

### 6. Score and report

Score the revised text 1-10 on each dimension:

| Dimension | Question |
|---|---|
| Directness | Does each paragraph state its point early? |
| Specificity | Named datasets, numbers, comparators instead of "recent methods", "good performance"? |
| Evidence tie | Is every claim followed by evidence and, where it matters, meaning? |
| Flow | Does each paragraph say why it follows the previous one? Same term for the same thing? |
| Calibration | One hedge per claim at most; no overclaim words without support? |
| Reader load | Could a clinician outside the project read the abstract and introduction without stopping at a term or a clipped sentence? |
| Human voice | Varied rhythm, an author who made choices, no template smell? |

Below 49/70, revise again. The score is a forcing function, not a measurement; do not present it as objective, and do not treat a high score as a reason to doubt an author who says the text is unclear.

Report to the user briefly: what changed structurally, what you could not verify, `[TODO]` items, any edit that touched technical meaning, anything you did differently from what a comment asked, and open questions. When the paper came from experiments, add the integrity report: runs used and runs left out with reasons, flags found and how each is handled in the text, claims narrowed, and requests declined. Do not narrate every sentence edit.

## Readability and restraint

Good journals are easy to read. The reader should grasp the message quickly and not wade through everything the authors measured. Bloat is as harmful as slop and AI drafts produce it by default, because every number is available and nothing is costly to include.

Rules:

- One paper, one message. State it in the abstract's first lines and the first paragraph of the discussion, each in different words. State the aim, and in Nature-style venues the headline, at the end of the introduction.
- The main text carries the results that support or honestly qualify the message. Secondary metrics, per-structure or per-class tables, extra ablations, hyperparameter sweeps and procedure settings go to the Supplement. Move detail, not contributions: when the set of experiments is itself the contribution, every experiment stays in the main text in a short, repeated form, and only its detail moves. Ask before demoting something the author ran on purpose.
- Name the primary metric and the primary comparison before drafting Results. Report secondary metrics in one sentence ("secondary metrics agreed; Supplementary Table 3") unless one changes the conclusion.
- No metric dumps. If a sentence lists four or more numbers, ask which one the reader needs and whether a table or figure should carry the rest.
- Each table and figure must be self-contained (caption says what is shown, the unit, the n, the takeaway) and earn its place. If removing it changes nothing in the argument, move it.
- Prefer one clear figure showing the headline over five figures showing everything. Make figures after the text they illustrate is agreed, so labels match the final wording.
- Skim path: a reader who reads only the abstract, the last intro paragraph, figure captions and the first discussion paragraph should be able to state the message in two sentences. Check this explicitly.
- Length is a cost to the reader. When trimming, cut in this order: repeated restatements, hedges and throat-clearing, secondary results, background the target reader knows. Do not cut limitations, the reason behind a design choice, the explanation of a term, or the sentence that links two paragraphs. Restraint is not compression.

## Integrity when writing up experiments

Honest write-up is also what makes a paper credible and easy to trust at a glance. Core habits:

- The ledger decides what exists. If a run is not in the ledger as completed, the paper does not claim it; if it is, the paper does not deny it.
- Report the aggregate over all completed seeds, with spread. Not the best seed.
- Select checkpoints, thresholds and hyperparameters on validation data only. If the test set was used for any of that, say so and treat the test result as optimistic.
- Give baselines the same data, split, preprocessing and comparable tuning effort, or state the asymmetry. Label each comparison with an existing method as run, adapted, or not run.
- State the unit of analysis; compute SDs and CIs across patients.
- State safeguards against data leakage together, and separately state which analysis choices depended on the data.
- Write limitations from the flags actually found in the record (single site, test reuse, single seed, no external set, a confounded cohort), each with its consequence.
- Label analyses not pre-specified as exploratory. Keep exploratory detail in the Supplement, not hidden and not in the headline.
- Honest does not mean bloated: the main text still carries the primary result and anything that changes the conclusion; the rest is disclosed in the Supplement.

## Voice rules (summary; full lists in references)

- Explain in plain words first, then give the term, and use terms sparingly. A label you coined while working is unknown to the reader. The abstract and introduction should be readable without any of them.
- Write complete sentences that name their subject. No clipped declaratives that lean on their neighbours, no bare "this" or "it", no two clauses joined by a colon in running text.
- Lead with the point, and when a paragraph depends on the previous one, let its first sentence say how. Open each section and subsection with a sentence that says what it covers. Cut openers that only announce ("It is important to note that", "Importantly,", "Notably,").
- Use the specific noun and the number. "Segmentation error in the left ventricle fell from 4.1 to 2.9 mm" beats "substantially improved performance".
- Claim verbs need subjects that can act: authors, data, models. "Results confirm" is false agency; write "The model reached X on the held-out site."
- Use "show" over "demonstrate", "use" over "leverage", "help" over "facilitate". Prefer words the clinical reader already uses ("negative control", "ground truth") to statistical or machine-learning jargon when they are accurate.
- No em dashes. Use commas, parentheses or a new sentence.
- No promotional vocabulary: robust, seamless, novel (unless truly the first, and say what), state-of-the-art (unless you name the comparator and protocol), superior, exceptional, pivotal, paradigm shift, pressing need.
- Intensifiers and softeners are out ("very", "highly", "quite", "somewhat"). Measurement and method adverbs are fine ("retrospectively", "independently", "approximately"). "Significantly" only with a test result nearby.
- Passive voice is fine for procedures where the actor is irrelevant ("Images were resampled to 1 mm isotropic"). It is not fine for claims or to hide who decided something.
- Hedge once and calibrate: "suggests" when the evidence is indirect; no "may potentially possibly".
- Use "we" for authors' choices and claims, and "we refer to X as ..." for the paper's own terms. Never "you".
- Vary rhythm. Do not end every paragraph with a one-line restatement. No dramatic fragments, no rhetorical question setups.
- Term sheet: one name per concept for the whole paper (for example "reference segmentation", not alternating with "ground truth", "gold standard", "label"). Keep a second list of the author's wording preferences as they emerge from comments, and apply it everywhere.

## Editing mode

When the user supplies text and asks to improve it:

1. Diagnose first in a few lines: what the paragraph is trying to do, where it stalls (slop, missing reason, missing meaning, wrong place, bloat, undefined terms, missing links).
2. Preserve the author's voice and technical content. If they asked to "polish", make minimal edits and say so.
3. If the problem is structural (sections do not connect) or one of identity (the paper is written as the wrong kind of paper), say that plainly and propose the fix before touching sentences. Polishing sentences cannot rescue a missing spine.
4. Return the revised text, then a short list of changes that matter and any flags. Use `references/examples.md` for the before/after pattern.

## Drafting from scratch

Write from the spine and the user's actual data. Where the user has given results, use exactly their numbers. Where the paper needs something they have not given, mark it. Start with the abstract and the introduction, because they fix the message and the register, and show them to the author before writing the rest.

## Reference files

- `references/working-with-authors.md`: reading co-author and reviewer comments, diagnosing a rewrite loop, agreeing the story before drafting, staged drafts with review builds, and handling disagreement between an author's hopes and the results. Read it whenever comments, repeated dissatisfaction or a whole-manuscript rewrite are involved.
- `references/findings-papers.md`: the findings register: frameworks, audits, evaluation and interpretability papers. Throughline, presenting the framework with its equations, numbered experiments with controls, dataset roles, positioning against existing methods, clinical meaning without overclaiming.
- `references/narrative-arc.md`: job of each section including related work, paragraph templates, flow techniques (link sentences, reverse outline, term sheet, transition test, mirrored sections), repetition budget.
- `references/slop-sci.md`: adapted phrase and structure lists, with replacements; over-compression patterns; AI-draft incoherence patterns.
- `references/venue-registers.md`: three registers, per-journal formats and conventions, habits worth borrowing across registers. Based on a small sample; treat as guidance and check author guidelines.
- `references/audit-checklist.md`: claim-evidence ledger, numbers, statistics, overclaim words, flow audit, readability and bloat audit, reader-load audit.
- `references/examples.md`: before and after pairs in imaging contexts (numbers are invented for illustration).
- `references/experiment-to-paper.md`: writing up completed experiments end to end: inventory, ledger, code-versus-story checks, what to report and disclose, requests to decline.
- `scripts/docx_comments.py`, `scripts/pdf_comments.py`: extract a reviewer's comments, their anchors and tracked changes from Word and PDF files.
- `scripts/slop_scan.py`, `scripts/number_audit.py`: mechanical prose and number checks.
- `scripts/experiment_inventory.py`: read-only inventory of a project's configs, logs, results, checkpoints and code-level leads, with a ledger skeleton.
- `scripts/results_to_table.py`: markdown results table from a per-run CSV (mean ± SD or bootstrap CI across independent units).
