# Medical-imaging-writing-skill

A Claude skill for writing applied machine-learning papers in medical imaging and clinical AI. It targets four failures of AI-assisted drafts: sentence-level slop, papers whose sections do not connect, bloat, and the opposite of slop: tidy drafts written in private jargon and clipped sentences that the author and the senior reader cannot follow.

It builds on [stop-slop](https://github.com/hardikpandya/stop-slop) (MIT, Hardik Pandya), with rules adapted for scientific prose. See `imaging-paper-writing/NOTICE`.

## What it does

- Builds a short **paper spine** first: clinical problem, gap, approach and why, data, headline result, meaning, limits, utility for others.
- Enforces the arc: clinical motivation, methods with the reason for each choice, results with their meaning, discussion of utility for the field.
- Enforces **readability and restraint**: one message per paper, a skim path, primary metric first, secondary results to the Supplement, no metric dumps.
- Audits claims against evidence, numerical consistency, provenance, statistics, overclaim words, flow, and bloat.
- **Writes up completed experiments honestly.** It inventories your code, configs, logs and result files, builds an experiment ledger (run, commit, config, split, seeds, status, selection rule), checks the code against what the Methods will claim, and traces every reported number to a completed run. It reports negative results, tuning budgets and test-set reuse, and declines cherry-picking seeds, baselines or checkpoints while offering the honest alternative.
- **Works with co-author and reviewer comments.** It extracts every comment from a commented Word file or an annotated PDF, diagnoses whether the problem is the paper's identity, its structure or its sentences, and agrees the story with the author before drafting. Whole-manuscript rewrites are done in stages, with a review build after each.
- **Supports findings papers.** Frameworks, audits, evaluation protocols and interpretability studies are treated as their own kind of paper: the framework is presented as a whole with its equations, experiments are numbered and written in one repeated pattern (why, what was done, control, finding, meaning), each dataset has a stated role, and comparisons with existing methods are labeled as run, adapted or not run.
- Guards against **over-compression**: plain words before terms, complete sentences, a linking sentence between paragraphs, and a reader-load audit of the abstract and introduction.
- Ships six helper scripts: `docx_comments.py` and `pdf_comments.py` (extract a reviewer's comments, the passages they mark, and tracked changes), `slop_scan.py` (phrase and structure scan, including clipped and colon-joined sentences), `number_audit.py` (text vs. table number check), `experiment_inventory.py` (read-only project inventory with ledger skeleton) and `results_to_table.py` (tables from per-run CSVs, with SD or bootstrap CI across patients).

## Layout

```
imaging-paper-writing/
  SKILL.md
  NOTICE
  references/
    working-with-authors.md
    findings-papers.md
    narrative-arc.md
    slop-sci.md
    venue-registers.md
    audit-checklist.md
    examples.md
    experiment-to-paper.md
  scripts/
    docx_comments.py
    pdf_comments.py
    slop_scan.py
    number_audit.py
    experiment_inventory.py
    results_to_table.py
```

## Install

Copy the `imaging-paper-writing` folder into your Claude skills directory (for Claude Code, `~/.claude/skills/`), or zip the folder and upload it as a skill in Claude settings.

## Scripts

```
python imaging-paper-writing/scripts/docx_comments.py manuscript.docx
python imaging-paper-writing/scripts/pdf_comments.py annotated.pdf        # needs PyMuPDF: pip install pymupdf
python imaging-paper-writing/scripts/slop_scan.py draft.md
python imaging-paper-writing/scripts/number_audit.py draft.md --tables tables.md
python imaging-paper-writing/scripts/experiment_inventory.py path/to/your/project
python imaging-paper-writing/scripts/results_to_table.py results.csv --group method --metrics dice --unit-col patient --ci
```

The comment scripts only read their input. The scan and audit scripts print leads for a human to check, not verdicts.

## Caveats

The venue guidance rests on a close reading of about eight open-access papers and on one research group's experience with a journal submission. Check the target journal's author guidelines, and the preferences of your senior co-authors, which always take precedence.
