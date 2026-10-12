# Working with authors: review comments, rewrite loops, and staged drafting

Use this when an author brings co-author or reviewer comments, says a draft "still isn't clear" after one or more rewrites, or asks for a rewrite of a whole manuscript. The lesson behind it: a complete rewrite delivered in one pass usually repeats the previous failure, because the failure was never a sentence-level one and the author had no chance to stop it early.

## Contents
1. Read every comment before judging the draft
2. Diagnose in order: identity, structure, sentences
3. Agree before drafting
4. Draft in stages, with a review build each time
5. Answering a round of comments
6. When the author's hopes and the results disagree
7. Second opinions and corrections
8. How to talk during the loop

---

## 1. Read every comment before judging the draft

Comments are the best evidence of where a real reader stopped following. Get all of them, with their text.

- Word file: `python scripts/docx_comments.py manuscript.docx` lists each comment, the passage it is attached to, and tracked changes.
- PDF: `python scripts/pdf_comments.py annotated.pdf` lists each highlight or note with its text and the passage it marks. A rendered page image shows the highlight but not the note typed into it, so reading the pages is not enough.
- Run the script on the file on disk every time the author says they commented, even if a file of that name was there before. Authors save annotated copies over the build you made.
- A highlight with no note has no stated reason. Ask what it means. Do not decide for yourself whether it marks "unclear" or "emphasize this".
- Tracked edits are instructions. Spelling variant (US or UK), a corrected name, a changed word, an added comma all show how the co-author wants the whole paper written. Carry them through.
- Before rebuilding a file the author annotated, copy the annotated version to a dated name. Never overwrite their comments.

Then look at the pattern. Where do the comments cluster, and where do they stop? A senior reader who comments densely up to the first Methods paragraph and then goes silent did not approve the rest. They gave up. Comments such as "what is X?", "who is 'it'?" and "where did this come from?" are one complaint repeated: things appear before the reader has been introduced to them.

## 2. Diagnose in order: identity, structure, sentences

Fix the highest level that is broken. Work at a lower level is wasted while a higher one is wrong.

1. **Identity.** What kind of paper is this, in the author's own words? A method that beats baselines, a clinical evaluation, or a framework and the findings it produced (see `findings-papers.md`). If the draft is being forced into the wrong kind, no structure will rescue it. Signs: the author says the paper "feels shallow", "undersells the work", or "reads like it is only about X".
2. **Structure.** Is there a sequence the reader can hold? Do Methods and Results mirror each other? Does every analysis have a stated reason? Are there too many parallel items with no hierarchy?
3. **Sentences.** Undefined terms, coined labels, clipped or overloaded sentences, missing links between paragraphs.

Tell the author which level you think is broken and why, in a few lines, before changing anything. If a previous rewrite fixed sentences and the complaint did not go away, say so plainly: the problem is one level up.

Do not shrink the work to make it tidy. The readability rule in SKILL.md ("the main text carries only results that support the message") is about detail, not about contributions. When an author says that the set of experiments is the contribution, keep every experiment, give them a hierarchy and one repeated pattern, and move procedure and secondary numbers to the Supplement. Ask before demoting anything the author ran on purpose.

## 3. Agree before drafting

When the author is in a loop, or asks to "brainstorm", do not touch the draft. Come back with points and questions, and settle these in order. Each can be one short exchange.

1. **Throughline**, in two or three sentences, for the author to accept or correct.
2. **The approach or framework in one or two sentences.** If you cannot write it, the Methods cannot present it.
3. **What each experiment is for.** One table: experiment, why it was run, what it uncovered, what it means for the clinical reader.
4. **Vocabulary.** The words that lost the reader, each with a plain description that will replace it in the abstract and introduction, and the term (if any) that will be used later.
5. **Roles of the datasets** when there are several, and which one leads.
6. **Outline**, section by section, with figure and table assignments and a target length.
7. **Open decisions** that belong to the author: title, names, what goes to the Supplement, anything that changes a headline number.

Rules for this phase:

- Make a recommendation for every decision. Do not present a survey of options.
- Ask at most four or five questions per round, at the end, numbered.
- When the author points to a paper they consider a model, read it and say what you will borrow and what does not apply. A model for the genre is not a template for the journal: conventions such as "state the findings in the introduction" differ between venues and between research groups.
- Record decisions as they are made. Later instructions override earlier ones; when two conflict, name the conflict and ask which holds.

## 4. Draft in stages, with a review build each time

Draft the abstract and introduction first and stop. They fix the register and the message, and they are cheap to redo. Continue only after the author has read them. Then go section by section (related work and methods; results; discussion and conclusion), stopping after each.

For each stage:

- Build something the author can annotate: a PDF with line numbers containing everything approved so far plus the new part. Use a new file name for each round.
- In the message, give the abstract in full, a one-line map of longer sections, the things the author should know before reading (length, new terms, anything described differently from before), and what you need back.
- Keep the number check passing at every stage, and say what has and has not been verified.
- Figures come after the text they illustrate is agreed, so that labels and numbering match the final wording. The exception is the overview figure of the method, which can be drawn once Methods is agreed.

## 5. Answering a round of comments

- Extract the comments (section 1), then answer every one. A short table of comment and change is the clearest form.
- Fix the cause, not the instance. "What is X?" on one sentence usually means X is undefined everywhere.
- If you did something other than what a comment asked, say so in its own short section with the reason. Never apply a different change silently.
- If a comment explains that an earlier choice of yours was wrong, say why you made it in one sentence and move on. Do not defend it.
- Preserve the author's wording preferences as a list (for example "scan, not study"; "reference contour, not ground truth"; "experiments, not analyses") and apply it to every later section.

## 6. When the author's hopes and the results disagree

Authors are often proudest of a component that their own controls did not support in its strong form.

- Check the record first. State what the data support and what they do not, with the numbers.
- Offer the framing that is both true and favourable. A component that organizes the method can be its backbone even when one use of it did not improve the outcome, and the control that showed this is itself a finding.
- If asked to remove a sentence that discloses a confound, a failed expectation or a limitation, remove the wording if it is redundant, keep the fact disclosed somewhere in the paper, and tell the author what you kept and why. A reviewer who finds an undisclosed confound does more damage than the sentence did.
- If one default is named in the text, another is drawn in the figures and a third is recommended in the discussion, the reader is lost and the paper looks evasive. Choose one default with the author, and state which headline numbers change as a result.
- "Clinically relevant" needs an argument. "Clinically useful" needs a study with clinicians. Connect each finding to what a clinician would do differently, and say what has not been shown.

## 7. Second opinions and corrections

- When the author pastes another reviewer's or another model's assessment, check it against the record and against decisions already made. Report what to adopt, what is wrong or out of date, and what it missed. Do not adopt or dismiss it wholesale.
- The current manuscript is not the record. Before saying that an experiment or comparison "was not run", search the results folders, the protocols and earlier manuscript versions (see `experiment-to-paper.md`). Experiments are often dropped between versions and forgotten.
- When you were wrong, say so in the first sentence, give the corrected facts, and say what changes as a result.

## 8. How to talk during the loop

- Lead with the answer to what was asked. Then the points, then the questions.
- Keep each reply short enough to read in a few minutes. The author is also reading the draft.
- Use the author's plain words back to them. If you coined a label while working, do not use it in a reply without explaining it.
- State length honestly. Added explanation and transitions cost words; say what the paper's length will be and what could move to the Supplement.
