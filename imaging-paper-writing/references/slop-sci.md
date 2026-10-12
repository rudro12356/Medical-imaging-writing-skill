# Slop patterns for scientific prose

Adapted from stop-slop by Hardik Pandya (MIT License, Copyright (c) 2025). The original is written for general prose. Scientific writing needs passive voice for procedures, measurement adverbs, calibrated hedging and the first person plural, so those rules are relaxed here. Rules that transfer unchanged are marked **Keep**; rules changed are marked **Relaxed**.

## Contents
1. Rule status vs stop-slop
2. Phrases to cut or replace
3. Structures to avoid
4. Over-compression: the opposite failure
5. AI-draft incoherence patterns
6. Quick replacement table

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

## 4. Over-compression: the opposite failure

Cutting slop can go too far. A draft stripped to bare claims, short declaratives and private labels is as hard to read as an inflated one, and authors describe it as "sloppy", "incomplete sentences", "shallow" or "I get lost". Check for these after every tightening pass.

- **Coined labels.** Names invented while working (for a quantity, a step, a property, a kind of map) used as if the reader knew them. Three or more in one sentence is unreadable. Replace with a description in the abstract and introduction; define once, after the plain explanation, where the term is needed.
- **Term before explanation.** The label arrives, and its meaning arrives a paragraph later or only in a glossary table. A glossary helps locally but does not fix the order.
- **Clipped declaratives.** "Such a dataset exists." "The results are mixed." "The study had four steps." Each depends on its neighbours for meaning. Merge it into a sentence that says what and why.
- **Colon-joined sentences in running text.** "X is the question of this paper: Y." Write two sentences or a subordinate clause. Keep colons for lists and equations.
- **Bare pronouns and demonstratives.** "This shows", "it fixed its design", "their features". Name the thing.
- **Missing links.** Paragraphs that are each clear but do not say why one follows the other. Add a link sentence (see `narrative-arc.md`, flow techniques).
- **Stacked qualifications from the audit trail.** Statements about how the study was planned, which tests were corrected, or what was prespecified, placed before the reader knows what was studied. Move them after the analyses they qualify, and say them in plain words ("we wrote down the expected result before each experiment").
- **Abstract nouns for sections and labels.** Headings such as "Robustness", "Completeness", "The six analyses" tell the reader nothing. Use the question the section answers.
- **Product-like names for small things.** A catchy name for a display or a helper can make the whole work look lightweight. Describe the function first; name it only if the author wants the name.

The target register is plain and complete: full sentences, ordinary words, the same word for the same thing, and every step of the reasoning written down.

## 5. AI-draft incoherence patterns

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
13. Analyses, cohorts or tools that appear without having been introduced, so the reader "does not know when they arrived".
14. The paper's own method first mentioned in the related-work section.
15. Results or worked examples from the Results section used in the introduction of a journal whose introductions carry none.
16. One default named in Methods, another shown in the figures, a third recommended in the Discussion.
17. Datasets with overlapping names and no stated role.
18. The contribution reduced to its smallest visible product, so the abstract and conclusion make careful work look shallow.

## 6. Quick replacement table

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
| a sentence built on three coined terms | the same content in ordinary words, one idea per sentence |
| X is called Y (for your own term) | we refer to X as Y |
| Such a dataset exists. | The [named dataset] meets this requirement, because [reason]. |
