# From completed experiments to an honest paper

Use this when the user has run experiments (code, configs, logs, result files) and wants them written up. The paper describes what was run, not what was planned or what would look best. The code and its outputs are the source of truth; the user's memory and the existing draft are secondary and get checked against them.

## Contents
1. Principles
2. Step A: inventory the record
3. Step B: build the experiment ledger
4. Step C: check the code against the story
5. Step D: decide what is reported, and how
6. Step E: write from the ledger
7. What to disclose
8. Requests to decline, and what to offer
9. What the code cannot tell you
10. Final integrity report

---

## 1. Principles

1. **Describe what was run.** No experiment appears in the paper unless a completed run backs it. Planned, crashed, partial or abandoned runs are not results.
2. **Every number has provenance.** Each reported number traces to a run, a config, a commit and a result file. Tables are generated from result files (`scripts/results_to_table.py`), not retyped from logs or memory.
3. **The claim ceiling is the weakest link.** A claim can be no stronger than the least rigorous step behind it: a single seed, a test set used for selection, an unequal tuning budget, a random split instead of a patient split.
4. **Disclose the path, not just the destination.** Reader-relevant history (how many configurations were tried, how the model was selected, which runs were discarded and why) belongs in the paper or Supplement.
5. **Negative and null results get written down.** If the proposed method did not beat the baseline on a dataset, or an ablation showed no effect, report it. A paper that says "improves" in four places and omits the fifth is misleading even if every sentence is true.
6. **Unknowns stay unknown.** If the record does not say something (reference standard details, ethics approval, which GPU), mark it `[TODO]` and ask. Do not infer.

## 2. Step A: inventory the record

Run the inventory script on the project root:

```
python scripts/experiment_inventory.py PROJECT_DIR > inventory.md
```

It lists git state, config files, result files, logs (with crash, NaN and test-evaluation flags), checkpoints, notebooks and code-level leads (random splits, missing seeds, test data near model selection). Treat every flag as a lead to check by reading the code or log, not as a finding.

If there is no script access (files on the user's computer, not in the workspace), read the project by hand in this order: README and run scripts, configs, training/eval code, logs, result files, git log.

## 3. Step B: build the experiment ledger

One row per run or run group. Fill from files; mark anything not in a file `[confirm]` and ask the user.

| Run ID | Purpose | Commit (dirty?) | Config | Data and split | Seeds | Status | Selection rule | Result file | In paper? |
|---|---|---|---|---|---|---|---|---|---|

Definitions:

- **Status**: completed / partial (stopped early on purpose) / crashed / abandoned / exploratory (run to look, not to test a hypothesis).
- **Selection rule**: how the reported checkpoint or configuration was chosen (last epoch, best validation metric, best test metric). "Best test metric" is a red flag; see Step C.
- **In paper?**: main text, Supplement, mentioned in limitations, or excluded with a reason the user can defend.
- **Pre-specified vs exploratory**: ask the user which comparisons and metrics were fixed before looking at test results. Label the rest as exploratory in the text.

Also record: tuning budget for the proposed method and for each baseline (number of configurations, epochs, learning-rate sweeps); number of times the test set was evaluated; seed counts; hardware and runtime if the paper will claim speed.

## 4. Step C: check the code against the story

Before writing the Methods, read the code that does each thing the Methods will claim. The Methods describe the code, not the other way around.

| The paper will say | Check in code |
|---|---|
| Split by patient | Split key is patient or subject ID, not slice, patch or file. No same patient in train and test (look for duplicates, longitudinal scans, multiple series). |
| Test set held out | Test data is not used in the training loop, early stopping, checkpoint choice, threshold choice, hyperparameter search or normalization statistics. |
| Preprocessing | The pipeline in the code (resampling, windowing, normalization, cropping) matches the text, and normalization statistics are computed on training data only. |
| Augmentation | Listed augmentations are actually enabled and applied to training only. |
| Loss and weights | Loss terms and weights in the config match the text. |
| Baselines | Baselines use the same data, split, preprocessing and comparable tuning effort. |
| Metrics | The metric implementation matches the definition (Dice with empty masks, Hausdorff units and spacing, AUC averaging, per-patient vs pooled). |
| Statistics | The test and its unit of analysis match the text; pairs are paired. |
| Seeds | Seeds are set and the number of seeds in the results matches the text. |
| External validation | The external set was never used for tuning, and was evaluated once for the reported model. |

If the code contradicts the intended story (for example the "patient split" is a random slice split), stop and tell the user before drafting around it. Offer: describe it as it is, re-run with the correct split, or narrow the claim. Do not write the intended version.

## 5. Step D: decide what is reported, and how

Decide with the user, using these defaults.

- **Primary result**: the pre-specified primary metric and comparison, from the completed runs, with its uncertainty. Mean and SD over seeds, or bootstrap CI over patients. If one run only, say "single run" in the table note.
- **Seeds**: report the aggregate over all seeds that completed. Do not report the best seed. If seeds were discarded, the reason must be documented (a bug fixed and re-run for all arms), not that the result looked bad.
- **Unit of analysis**: aggregate to patient first, then summarize. SDs and CIs are across patients (or independent units), not slices or voxels.
- **Comparisons with baselines**: report every baseline that was run under the same protocol, including those that beat the proposed method on some metric or dataset. If a baseline was run and left out, say why or include it.
- **Ablations**: report the ablations that were run and that test a claim in the paper. Do not describe an in-noise difference as an effect; say "no clear difference".
- **Secondary and exploratory results**: Supplement, labeled exploratory. Keep the main text restrained (see SKILL.md, readability and restraint) without hiding anything that changes the conclusion.
- **Failures and limits**: at least one concrete failure analysis (where the model does worse, which patients, which conditions) if the data allow it. If the record has none, say that this was not analyzed.
- **Test-set reuse**: if the test set was evaluated more than once during development, say so and report the number of times; consider treating the reported test result as optimistic, and recommend a fresh holdout if one exists.

## 6. Step E: write from the ledger

1. Spine first (SKILL.md), now with the headline taken from the ledger and the claim ceiling applied.
2. Methods from the code checks in Step C: data, split, preprocessing, model, training, selection rule, evaluation, statistics, baselines, tuning budgets.
3. Results from generated tables, in the claim, evidence, meaning order. Every number in the text is in a table or figure generated from a result file.
4. Discussion with limitations drawn from the flags found in Steps B and C (single site, test reuse, unequal tuning, single seed, no external validation) stated with their consequences.
5. Reproducibility statement: commit hash, environment, seeds, and code and data availability only as true. If the working tree was dirty at run time, say so or ask the user to commit and re-run.
6. Run the audit (`references/audit-checklist.md`), including provenance and integrity.

## 7. What to disclose

Short list to put in Methods, Supplement or Limitations as fits the venue:

- Number of hyperparameter configurations tried for the proposed method and for baselines.
- How the final model or checkpoint was selected, and on what data.
- Number of times the test set was evaluated.
- Number of seeds; whether results are mean ± SD or a single run.
- Runs that were excluded, why, and whether the exclusion applied to all arms.
- Deviations from any pre-specified plan, and post-hoc analyses labeled as post-hoc.
- Known data issues (duplicates, mislabeled cases, exclusions after inspection), and how many cases were excluded and why.
- Compute used, only if relevant to a claim.

## 8. Requests to decline, and what to offer

Decline politely and briefly. Do not lecture. Offer the honest alternative in the same message.

| Request | Why not | Offer |
|---|---|---|
| Report the best seed or best run | Overstates expected performance | Report mean ± SD, show the range, mention the best in a note |
| Choose the checkpoint or threshold using test results | Test leakage | Select on validation; if test was already used, disclose and treat as optimistic |
| Run more seeds or tweak until p < 0.05 | Optional stopping, p-hacking | Fix the number of seeds in advance; report the result as is |
| Drop baselines that beat the method | Selective reporting | Include them; frame the contribution honestly (cost, simplicity, a subgroup, interpretability) |
| Describe a planned or crashed experiment as done | Fabrication | Write it as limitation or future work; offer to list what is needed to run it |
| Fill table cells with estimates or "typical" numbers | Fabrication | Leave `[TODO]` and list the runs needed |
| Claim generalization from a random split of one dataset | Unsupported | Report as internal validation; suggest an external set or a site-wise split |
| Hide that tuning was unequal | Unfair comparison | Disclose, or give baselines an equal budget and re-run |
| Remove an inconvenient failure analysis | Selective reporting | Keep it concise and place it in the Supplement only if the main text still states the limit |

## 9. What the code cannot tell you

Ask the user, and do not infer: clinical motivation and intended use; patient population and inclusion/exclusion criteria; how the reference standard was made and by whom; ethics approval and consent wording; data licensing; funding; author contributions; which analyses were pre-specified; and whether any unrecorded runs exist (notebooks run and deleted, results from another machine). A short question list at the end of Step B is usually enough.

## 10. Final integrity report

End the task with a short report to the user:

- Runs used in the paper, and runs left out with reasons.
- Flags found (test reuse, split concerns, missing seeds, unequal tuning, dirty tree) and how each was handled in the text.
- Claims that were narrowed to fit the evidence.
- Items still `[TODO]`, and experiments that would strengthen the paper if time allows (specific ones, in order of value).
- Any request declined and the alternative offered.
