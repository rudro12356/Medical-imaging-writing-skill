#!/usr/bin/env python3
"""Scan a manuscript draft for slop patterns adapted to scientific prose.

Usage:
    python slop_scan.py draft.md [--json]

Findings are leads, not verdicts. Read each in context.
Adapted from the stop-slop idea by Hardik Pandya (MIT).
"""
import argparse
import json
import re
import sys
from collections import Counter

PHRASES = {
    "inflated": [
        "robust", "comprehensive", "novel", "powerful", "remarkable", "exceptional",
        "superior", "intricate", "cutting-edge", "groundbreaking", "compelling",
        "state-of-the-art", "seamless", "seamlessly", "effortless", "effortlessly",
    ],
    "weak-verb": [
        "leverage", "leverages", "leveraging", "harness", "harnesses", "harnessing",
        "utilize", "utilizes", "utilizing", "unlock", "showcase", "showcases",
        "underscore", "underscores", "delve", "delves", "foster", "fosters",
        "facilitate", "facilitates", "facilitating", "shed light on", "pave the way",
        "bridge the gap", "bridging the gap", "bridges the gap",
    ],
    "frame": [
        "in recent years", "revolutionized", "plays a pivotal", "plays a crucial",
        "plays a vital", "plays an important", "holds great promise", "great potential",
        "pressing need", "urgent need", "paradigm shift", "game changer", "game-changer",
        "in the era of", "to the best of our knowledge", "extensive experiments",
        "comprehensive evaluation", "consistently outperform", "it is worth noting",
        "it should be noted", "it is important to note", "it is important to highlight",
        "this highlights the importance", "taken together", "together, these results",
    ],
    "opener": ["importantly,", "notably,", "interestingly,", "crucially,", "overall,"],
    "intensifier": [
        "very", "highly", "extremely", "quite", "rather", "fairly", "somewhat",
        "drastically", "dramatically", "substantially",
    ],
}

ADVICE = {
    "inflated": "Name what is robust/novel/superior and to what; or cut.",
    "weak-verb": "Use plain verb (use, help, show).",
    "frame": "Cut the frame; start with the specific claim.",
    "opener": "Cut the announcing opener.",
    "intensifier": "Cut, or give the number.",
    "em-dash": "Replace with comma, colon, parentheses or new sentence.",
    "significantly": "Use only with a test/CI nearby; otherwise give the number.",
    "participial-tail": "Benefit claimed without evidence; give it its own sentence with a number or cut.",
    "not-only": "Say the second part directly.",
    "connective-chain": "Consecutive sentences opening with connectives; reorder or drop.",
    "hedge-stack": "One hedge per claim.",
    "benefit-triad": "Name which benefit was measured.",
    "long-number-list": "Four or more numbers in one sentence; keep the one the reader needs.",
    "clipped": "Very short sentence that leans on its neighbours; merge it into a sentence that says what and why.",
    "colon-join": "Two clauses joined by a colon in running text; write two sentences or a subordinate clause.",
    "bare-pronoun": "Sentence opens with a bare This/It; name the thing it refers to.",
}

CONNECTIVES = ("moreover", "furthermore", "additionally", "in addition", "however", "therefore", "thus", "consequently")
HEDGES = ("may", "might", "could", "potentially", "possibly", "perhaps", "appears to", "seems to", "suggest", "likely")
TEST_NEAR = re.compile(r"p\s*[<=>]|CI|confidence interval|Wilcoxon|t-test|ANOVA|Mann|permutation|bootstrap|DeLong", re.I)
TAIL = re.compile(r",\s+(thereby|thus|hence|enabling|ensuring|allowing|making|leading to|resulting in|improving|enhancing|facilitating|reducing)\b\s+\w+", re.I)
NOTONLY = re.compile(r"\bnot (only|just)\b.{0,80}\bbut( also)?\b", re.I)
TRIAD = re.compile(r"\b(\w+(?:ity|ness|ency|ance|ness|ion|ment)|robust|scalable|accurate|efficient|reliable),\s+(\w+),?\s+and\s+(\w+)\b", re.I)
NUMBER = re.compile(r"(?<![\w.])\d+(?:\.\d+)?%?(?![\w.])")
# Over-compression leads (see references/slop-sci.md, section 4). Prose lines only.
NOT_PROSE = re.compile(r"^\s*(#|\\|[-*] |\d+\. |\||>|%|Fig|Table|\$)")
COLON_JOIN = re.compile(r"\b[a-z]{3,}: (?:[a-z]+ ){1,8}?(?:is|are|was|were|has|have|does|did|can|cannot|should|must|will)\b")
BARE_PRONOUN = re.compile(r"^(This|It) (is|was|shows?|means?|suggests?|indicates?|makes?|allows?|gives?|leads?|does)\b")


def split_sentences(line):
    return [s for s in re.split(r"(?<=[.!?])\s+", line) if s]


def scan(text):
    findings = []
    lines = text.splitlines()
    for ln, line in enumerate(lines, 1):
        if not line.strip() or line.lstrip().startswith(("```", "|---")):
            continue
        low = line.lower()
        for cat, words in PHRASES.items():
            for w in words:
                pat = r"(?<![\w-])" + re.escape(w) + (r"" if w.endswith(",") else r"(?![\w-])")
                for m in re.finditer(pat, low):
                    findings.append((ln, cat, w, line.strip()[:140]))
        if "—" in line or " -- " in line:
            findings.append((ln, "em-dash", "—", line.strip()[:140]))
        for m in re.finditer(r"significan(t|tly)", low):
            window = line[max(0, m.start() - 120): m.end() + 120]
            if not TEST_NEAR.search(window):
                findings.append((ln, "significantly", m.group(0), line.strip()[:140]))
        for m in TAIL.finditer(line):
            findings.append((ln, "participial-tail", m.group(0).strip(), line.strip()[:140]))
        if NOTONLY.search(line):
            findings.append((ln, "not-only", "not only ... but", line.strip()[:140]))
        if TRIAD.search(line):
            findings.append((ln, "benefit-triad", TRIAD.search(line).group(0), line.strip()[:140]))
        sents = split_sentences(line)
        if not NOT_PROSE.match(line):
            for s in sents:
                core = re.sub(r"\\\w+(\{[^}]*\})?|[~{}]", " ", s).strip()
                n_words = len(core.split())
                if 1 < n_words <= 5 and core.endswith(".") and core[0].isupper() and not re.search(r"\d", core):
                    findings.append((ln, "clipped", core[:50], line.strip()[:140]))
                if BARE_PRONOUN.match(core):
                    findings.append((ln, "bare-pronoun", " ".join(core.split()[:3]), s.strip()[:140]))
                m = COLON_JOIN.search(core)
                if m:
                    findings.append((ln, "colon-join", m.group(0)[:50], s.strip()[:140]))
        run = 0
        for s in sents:
            if s.lower().startswith(CONNECTIVES):
                run += 1
            else:
                run = 0
            if run >= 2:
                findings.append((ln, "connective-chain", s[:40], line.strip()[:140]))
                break
        for s in sents:
            sl = s.lower()
            if sum(1 for h in HEDGES if re.search(r"\b" + h, sl)) >= 3:
                findings.append((ln, "hedge-stack", s[:60], s.strip()[:140]))
            nums = NUMBER.findall(s)
            if len(nums) >= 6:
                findings.append((ln, "long-number-list", f"{len(nums)} numbers", s.strip()[:140]))
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8").read()
    f = scan(text)
    counts = Counter(c for _, c, _, _ in f)
    if a.json:
        print(json.dumps({"findings": [dict(line=l, category=c, match=m, context=x, advice=ADVICE.get(c, "")) for l, c, m, x in f],
                          "counts": counts}, indent=2))
        return
    for l, c, m, x in sorted(f):
        print(f"L{l:<4} [{c}] '{m}'  -> {ADVICE.get(c, '')}\n      {x}")
    words = len(text.split())
    print(f"\n{len(f)} findings in {words} words.")
    for c, n in counts.most_common():
        print(f"  {c}: {n}")
    print("These are leads. Read each in context; some uses are fine.")


if __name__ == "__main__":
    main()
