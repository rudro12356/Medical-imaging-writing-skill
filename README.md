# Medical-imaging-writing-skill

A Claude skill for writing applied machine-learning papers in medical imaging and clinical AI. It targets two failures of AI-assisted drafts: sentence-level slop, and papers whose sections do not connect.

It builds on [stop-slop](https://github.com/hardikpandya/stop-slop) (MIT, Hardik Pandya), with rules adapted for scientific prose. See `imaging-paper-writing/NOTICE`.

## What it does

- Builds a short **paper spine** first: clinical problem, gap, approach and why, data, headline result, meaning, limits, utility for others.
- Enforces the arc: clinical motivation, methods with the reason for each choice, results with their meaning, discussion of utility for the field.
- Enforces **readability and restraint**: one message per paper, a skim path, primary metric first, secondary results to the Supplement, no metric dumps.
- Audits claims against evidence, numerical consistency, statistics, overclaim words, flow, and bloat.
- Ships two helper scripts: `slop_scan.py` (phrase and structure scan) and `number_audit.py` (text vs. table number check).

## Layout

```
imaging-paper-writing/
  SKILL.md
  NOTICE
  references/
    narrative-arc.md
    slop-sci.md
    venue-registers.md
    audit-checklist.md
    examples.md
  scripts/
    slop_scan.py
    number_audit.py
```

## Install

Copy the `imaging-paper-writing` folder into your Claude skills directory (for Claude Code, `~/.claude/skills/`), or zip the folder and upload it as a skill in Claude settings.

## Scripts

```
python imaging-paper-writing/scripts/slop_scan.py draft.md
python imaging-paper-writing/scripts/number_audit.py draft.md --tables tables.md
```

Both print leads for a human to check, not verdicts.

## Caveats

The venue guidance rests on a close reading of about eight open-access papers. Check the target journal's author guidelines, which always take precedence.
