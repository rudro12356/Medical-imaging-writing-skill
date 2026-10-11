#!/usr/bin/env python3
"""Heuristic numerical-consistency check for a manuscript draft.

Usage:
    python number_audit.py draft.md [--tables tables.md] [--tol 0.05]

Without --tables: lists numbers in the draft that appear with different
rounding or inconsistent values across sections, and flags tiny p-values.
With --tables: also flags text numbers not found in the tables, and the
nearest table value within tolerance as a possible mismatch.

Output is a list of leads for a human to check, not verdicts.
"""
import argparse
import re
from collections import defaultdict

NUM = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?(?:[eE]-?\d+)?%?(?![\w])")
PVAL = re.compile(r"\bp\s*(?:=|<|>|≤)\s*(\d+(?:\.\d+)?(?:[eE]-?\d+)?)", re.I)


def numbers(text):
    out = []
    for ln, line in enumerate(text.splitlines(), 1):
        for m in NUM.finditer(line):
            tok = m.group(0)
            raw = tok.rstrip("%")
            try:
                val = float(raw)
            except ValueError:
                continue
            decimals = len(raw.split(".")[1]) if "." in raw and "e" not in raw.lower() else 0
            # skip citation-like integers, years, and small integers without decimals/percent
            if decimals == 0 and not tok.endswith("%"):
                continue
            if tok in ("90%", "95%", "99%"):  # confidence levels, not results
                continue
            out.append((ln, tok, val, decimals, line.strip()[:120]))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("draft")
    ap.add_argument("--tables")
    ap.add_argument("--tol", type=float, default=0.05, help="relative tolerance for near-match leads")
    a = ap.parse_args()

    draft = open(a.draft, encoding="utf-8").read()
    nums = numbers(draft)
    print(f"{len(nums)} decimal/percent numbers in draft.\n")

    # tiny p-values
    for ln, line in enumerate(draft.splitlines(), 1):
        for m in PVAL.finditer(line):
            try:
                v = float(m.group(1))
            except ValueError:
                continue
            if 0 < v < 1e-10:
                print(f"L{ln}: p={m.group(1)} is extremely small. Check the unit of analysis (patients, not voxels/spots/slices) and report as p < 0.001.")
            elif "e" in m.group(1).lower():
                print(f"L{ln}: p in exponent form ({m.group(1)}). Report as p < 0.001 unless the exact value matters.")

    # same value written with different precision
    # Same quantity written at different precision, e.g. 0.87 vs 0.873, or 87% vs 87.3%.
    # A pair is flagged when the finer value rounds to the coarser one but the strings differ.
    print("\nSame value written at different precision (check rounding is consistent):")
    found = False
    seen = set()
    uniq = {}
    for ln, tok, val, dec, ctx in nums:
        uniq.setdefault((tok, val, dec), ln)
    items = list(uniq.items())
    for i, ((t1, v1, d1), l1) in enumerate(items):
        for (t2, v2, d2), l2 in items[i + 1:]:
            if t1 == t2 or d1 == d2 or t1.endswith("%") != t2.endswith("%"):
                continue
            coarse, fine = ((v1, d1), v2) if d1 < d2 else ((v2, d2), v1)
            if round(fine, coarse[1]) == coarse[0] and (t1, t2) not in seen:
                seen.add((t1, t2))
                found = True
                print(f"  {t1} (L{l1}) and {t2} (L{l2})")
    if not found:
        print("  none")

    if a.tables:
        tables = open(a.tables, encoding="utf-8").read()
        tvals = [(tok, float(tok.rstrip("%"))) for _, tok, _, _, _ in numbers(tables)]
        tset = {t for t, _ in tvals}
        print("\nText numbers not found in tables:")
        any_flag = False
        for ln, tok, val, dec, ctx in nums:
            if tok in tset:
                continue
            near = [t for t, v in tvals if v != 0 and abs(v - val) / abs(v) <= a.tol and t != tok]
            if near:
                any_flag = True
                print(f"  L{ln}: {tok} not in tables; near {', '.join(sorted(set(near))[:4])} -> possible mismatch. {ctx}")
            else:
                any_flag = True
                print(f"  L{ln}: {tok} not in tables. {ctx}")
        if not any_flag:
            print("  none")
    print("\nThese are leads. Derived numbers (differences, means) will show as 'not in tables'; check them by hand.")


if __name__ == "__main__":
    main()
