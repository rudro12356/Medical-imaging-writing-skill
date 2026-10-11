#!/usr/bin/env python3
"""Build a results table from a per-run CSV so reported numbers come from files, not memory.

Usage:
    python results_to_table.py results.csv --group method --metrics dice hd95 \
        [--unit-col patient] [--decimals 2] [--ci] [--out table.md]

Input: one row per measurement (e.g. method, seed, patient, dice, hd95).
- --group: columns that define a table row (e.g. method, or method dataset).
- --unit-col: independent unit (e.g. patient). Values are averaged within each unit
  first, so the SD or CI is across patients, not slices or voxels.
- --ci: add a 95% percentile bootstrap CI over units (2000 resamples, fixed seed).
Rows with missing or non-numeric metric values are counted and reported, never silently dropped.
"""
import argparse
import csv
import math
import random
import statistics as st
from collections import defaultdict


def num(x):
    try:
        v = float(x)
        return None if math.isnan(v) else v
    except (TypeError, ValueError):
        return None


def boot_ci(vals, n=2000, seed=0):
    rng = random.Random(seed)
    means = sorted(sum(rng.choices(vals, k=len(vals))) / len(vals) for _ in range(n))
    return means[int(0.025 * n)], means[int(0.975 * n) - 1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("csv")
    ap.add_argument("--group", nargs="+", required=True)
    ap.add_argument("--metrics", nargs="+", required=True)
    ap.add_argument("--unit-col")
    ap.add_argument("--decimals", type=int, default=2)
    ap.add_argument("--ci", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.csv, newline="", encoding="utf-8")))
    cols = rows[0].keys() if rows else []
    for c in a.group + a.metrics + ([a.unit_col] if a.unit_col else []):
        if c not in cols:
            raise SystemExit(f"column '{c}' not in {list(cols)}")

    dropped = defaultdict(int)
    # data[group][metric][unit] -> list of values
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for i, r in enumerate(rows):
        g = tuple(r[c] for c in a.group)
        unit = r[a.unit_col] if a.unit_col else i
        for m in a.metrics:
            v = num(r[m])
            if v is None:
                dropped[(g, m)] += 1
            else:
                data[g][m][unit].append(v)

    d = a.decimals
    head = a.group + ["n"] + [f"{m} (mean ± SD{', 95% CI' if a.ci else ''})" for m in a.metrics]
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for g in sorted(data):
        cells = list(g)
        ns = {len(u) for u in data[g].values()}
        cells.append("/".join(map(str, sorted(ns))))
        for m in a.metrics:
            units = [sum(v) / len(v) for v in data[g][m].values()]
            if not units:
                cells.append("n/a")
                continue
            sd = f"{st.stdev(units):.{d}f}" if len(units) > 1 else "single value, no SD"
            s = f"{st.mean(units):.{d}f} ± {sd}"
            if a.ci and len(units) > 1:
                lo, hi = boot_ci(units)
                s += f", [{lo:.{d}f}, {hi:.{d}f}]"
            cells.append(s)
        lines.append("| " + " | ".join(cells) + " |")
    out = "\n".join(lines)
    unit_note = f"n = number of {a.unit_col} units" if a.unit_col else "n = number of rows; no unit column given, so SD treats every row as independent"
    notes = [f"\nNote: {unit_note}. Source: {a.csv}."]
    if dropped:
        notes.append("WARNING: missing or non-numeric values excluded: " +
                     "; ".join(f"{'/'.join(g)} {m}: {n}" for (g, m), n in dropped.items()) + ". Ask why before reporting.")
    out += "\n" + "\n".join(notes)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(out + "\n")
    print(out)


if __name__ == "__main__":
    main()
