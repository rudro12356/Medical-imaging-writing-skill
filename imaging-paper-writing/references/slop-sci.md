# Slop patterns for scientific prose

Adapted from stop-slop by Hardik Pandya (MIT License, Copyright (c) 2025). The original is written for general prose. Scientific writing needs passive voice for procedures, measurement adverbs, calibrated hedging and the first person plural, so those rules are relaxed here. Rules that transfer unchanged are marked **Keep**; rules changed are marked **Relaxed**.

## Contents
1. Rule status vs stop-slop
2. Phrases to cut or replace
3. Structures to avoid
4. AI-draft incoherence patterns
5. Quick replacement table

---

## 1. Rule status vs stop-slop

| stop-slop rule | Status | Scientific version |
|---|---|---|
| Cut throat-clearing openers | Keep | No "It is worth noting that", "Importantly,", "Notably,", "Interestingly," |
| Cut emphasis crutches | Keep | No "Crucially", "Needless to say" |
| Cut business/AI jargon | Keep | Plus the ML-paper list below |
| Avoid binary contrasts ("not X, but Y") | Keep | Allowed only when X is a real competing hypothesis the data rule out |
| Avoid negative listing | Keep | |
| Avoid dramatic fragmentation | Keep | |
| Avoid rhetorical setups | Keep | No "So what does this mean?" |
| Avoid vague declaratives ("The implications are significant") | Keep | State the implication |
| No em dashes | Keep | |
| Cut quotable closers | Keep | |
| False agency ("the data tells us") | Keep | "Results confirm", "findings emphasize", "this bridges" are false agency |
| No adverbs | Relaxed | Ban intensifiers/softeners. Keep measurement and method adverbs |
| No passive voice | Relaxed | Fine for procedures; not for claims |
| No hedging | Relaxed | Calibrated hedging is required; stacked hedging is banned |
| No Wh- sentence starters | Dropped | Not a scientific-writing problem |
| No triads | Relaxed | Ban triads of abstract nouns ("robust, scalable, and generalizable"); lists of concrete items are fine |
| Use "you" | Replaced | Use "we" for authors; never "you" |

## 2. Phrases to cut or replace

**Inflated adjectives.** robust, comprehensive, novel, powerful, remarkable, exceptional, superior, intricate, cutting-edge, groundbreaking, compelling, significant (without a test).
- "robust" needs the perturbation named: robust to what, by how much.
- "novel" is for reviewers to say. If needed, say what is new: "first to X under Y".
- "state-of-the-art" needs a named comparator, dataset and protocol.

**Weak or inflated verbs.** leverage, harness, unlock, showcase, underscore, highlight, delve into, foster, facilitate, bridge the gap, pave the way, shed light on, address (as filler), demonstrate (when "show" does).
- leverage / harness / utilize -> use
- facilitate -> help, allow
- showcase / highlight / underscore -> show
- demonstrate -> show (keep "demonstrate" for formal proof or demonstration of feasibility)

**Frames and clichés.**
- "In recent years, deep learning has revolutionized..." Start with the clinical problem.
- "plays a pivotal / crucial / vital role"
- "holds great promise", "has shown great potential"
- "there is a pressing / urgent need for"
- "paradigm shift", "game changer"
- "seamlessly integrates", "effortlessly"
- "consistently outperforms" (needs the number of settings and the margin)
- "to the best of our knowledge, this is the first" (rarely verifiable; delete unless you searched)
- "a comprehensive evaluation" (say what was evaluated)
- "extensive experiments demonstrate" (say which experiments)
- "In the era of..."
- "It is worth noting that", "It should be noted that", "It is important to highlight"
- "Overall," "Taken together," "Together, these results indicate" repeated every paragraph
- "This highlights the importance of"
- "plays an increasingly important role"

**Hedge stacks.** "may potentially suggest", "could possibly indicate", "appears to somewhat". One hedge per claim, matched to the evidence.

**Empty intensifiers/softeners.** very, highly, extremely, quite, rather, fairly, somewhat, relatively (unless relative to something named), substantially (without a number), drastically, dramatically.

## 3. Structures to avoid

- **Not only... but also...** and "not just X, but Y". Say Y.
- **Participial tails** that claim a benefit without evidence: ", thereby improving accuracy", ", enabling more reliable diagnosis", ", ensuring robustness". If the benefit is real, give it its own sentence with a number; if not, cut.
- **Benefit triads**: "improving accuracy, efficiency, and generalizability". Name which one was measured.
- **Paragraph-ending restatements**: a final sentence that repeats the paragraph's point in grander terms.
- **Chronological prior-work roll-calls** instead of grouping by what is left open.
- **Boilerplate future work**: "Future work will explore larger datasets and other modalities." Replace with a specific next test and why.
- **Method name as subject doing everything**: "Our framework learns, adapts, and generalizes." Use the verb for what was measured.
- **Colon-and-list teasers**: "The result? A faster pipeline."
- **Sentence-initial connective chains**: Moreover, Furthermore, Additionally, In addition at the start of consecutive sentences. Reorder or remove.
- **Uniform sentence length and a three-beat rhythm** in every paragraph.
- **Dramatic one-line paragraphs.**

## 4. AI-draft incoherence patterns

These are the reason a draft "goes here and there". Check for them in the reverse outline.

1. Introduction with no clinical stake: opens with ML history.
2. Gap stated in generic terms ("existing methods have limitations").
3. Methods list with no reason for any choice.
4. Results listing metrics with no statement of what they mean.
5. Discussion restating Results in the same order.
6. Term drift: the same concept under three names, or one name used for two concepts.
7. Abstract claims not backed in Results (scope creep as the text moves from Results to Abstract to Conclusion).
8. Numbers differing between text, tables, abstract.
9. Close prior work cited but never compared and never explained.
10. Limitations section of generic boilerplate (small data, more work needed) with no consequence for the claim.
11. Each paragraph locally fine, but no paragraph answers the one before.
12. Everything measured is reported (bloat), so the message is buried.

## 5. Quick replacement table

| Slop | Replace with |
|---|---|
| leverages a transformer backbone | uses a transformer backbone |
| a robust framework | state what was robust to what: "stable across three scanners" |
| significantly improves | improves by 3.1 points (95% CI 1.8-4.4) / or "improves (p < 0.01, paired Wilcoxon)" |
| demonstrates the potential of | state the measured result |
| comprehensive evaluation on multiple datasets | evaluation on three public datasets (A, B, C) |
| addresses the challenge of | reduces / handles / avoids; name the challenge |
| paves the way for clinical translation | name the step still needed: "prospective validation is needed before clinical use" |
| it is worth noting that X | X |
| bridging the gap between | connecting; or cut |
