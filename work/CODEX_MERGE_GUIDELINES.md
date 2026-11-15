# Merge guidelines for Codex: *The Path of Many Arrows*

*For the final pass that merges Claude-drafted chapters and interludes into the manuscript. Written 2026-11-15, after the Chapter 1 and Chapter Φ merges.*

---

## 1. What this book is doing

The book looks at every domain (physics, biology, brains, economics, politics, ideology, ecology, information) through **many windows**. It takes each discipline's settled account seriously, then nudges it with a twist of its own to see how the account responds. The Introduction and Chapter Φ say this to the reader up front.

So the book contains **bold claims on purpose**. Your job is to keep them honest, not to make them conventional.

- **A bold claim is not an error.** An error is a claim that is false, or that states something established when it isn't.
- **Don't collapse an alternative view into the one window your training knows best.** When the mainstream view differs from the book's reading, keep the book's reading. Add the mainstream window beside it (a clause, a footnote, or an "on the usual reading…") rather than replacing one with the other.
- **Why this matters to the author.** A bold idea that runs slightly hot is still worth keeping. On review, the author can adjust it or run with it. Left for the reader, it may become a question she researches, tests or turns into a discovery of her own, which is the highest honor an idea can have in any good discipline. Your pass remains essential, because it exposes real errors and gaps. It shouldn't become a bottleneck that sands every idea down to the textbook version.
- **Check facts with an open mind.** Verify every factual statement. Interpretations need only be internally consistent, honestly labeled and not contradicted by established results.

---

## 2. Sort every change you'd make into one of four kinds

| Kind | What it is | What to do |
|---|---|---|
| **A. Error** | A false fact, a wrong date or number, a misattributed quotation, a claim presented as established that isn't | **Fix it** in the text. Log it. |
| **B. Precision** | True in spirit but loose: a missing condition, an overclaim that a word or clause can repair | **Repair it with the smallest change that makes it true.** Prefer adding a hedge to deleting the sentence. Edge cases (ionization, gauge conventions, model assumptions, "in AdS but not de Sitter") go in a **footnote**, not the body. |
| **C. Style or vividness** | A line you'd cut because it's colorful, playful, emphatic or "unscientific" in tone, but isn't false | **Don't change it.** If you think it misleads, propose a repair in the review log. |
| **D. Thesis or interpretation** | The author's (or Claude's) reading, a conjecture, a speculative bridge between domains | **Don't delete or neutralize it.** If it isn't labeled, add a light label ("my reading is…", "I'd wager…"). If you think it's wrong, say why in the review log; the author decides. |

**When unsure between kinds, choose the more conservative action**: log it rather than change it.

---

## 3. Never change these

- **Comments and markers.** Keep every `OVERLAP`, `DIAGRAM (greyscale)`, `AI draft … / End AI draft` and source-note comment. The author's second pass depends on them.
- **Closing lines** of chapters, interludes, Opens and codas. Keep them exactly; they are meant to drop hard.
- **Signature terms:**
  - possibility space;
  - the four questions (what is possible, what is cheap, where is the sameness, where is the break);
  - castle, monster, upheaval;
  - the thick arrow and the thin arrow;
  - scaling story;
  - each chapter's amendment line ("In a society, a thing becomes real when…");
  - the anthropic seat;
  - Alice / Bob section headings;
  - recipe and address (Chapter 1);
  - the Neusphere.
- **Forward and backward pointers** ("Interlude 12 will collect on that"), unless the target doesn't exist. If you find one that points at nothing, **add the missing material at the target or flag it**; don't delete the pointer.
- **Deliberate silences.**
  - The snake / ouroboros, the fold and the Neusphere are first revealed in **Coda I**. Don't add references to them in Chapters 1–11 or their interludes.
  - Neuma appears only in Volume III, and sparingly.
- **Personal material:** vignettes, the author's voice, idiosyncratic phrasing, parentheses used as a "second dimension," and humor.

---

## 4. Footnotes marked "(AI-added, from memory; to be verified.)"

- **Verified:** replace the tag with the verified citation (a link where possible), and correct any detail that differs.
- **Different number or wording:** correct the **text** to match the source and log the change.
- **No source found:** **don't delete the claim.** Flag it in the log with what you searched. The author decides.

---

## 5. Figures

- Figures that Claude proposed (via `DIAGRAM` comments) are drawn by Claude and delivered as SVGs at `assets/<chapter>/<name>.svg`.
- Your role is to **verify** them (curves against equations, labels against the text, file paths against the chapter) and to place them.
- If you draw a figure yourself, read its labels against the physics. One example: a circle of minima is a ring of equally low *potential energy*, not "equally low field values."

---

## 6. Before you hand back a file

- [ ] Every footnote reference has a definition, and every definition is referenced.
- [ ] No new typos: re-read every sentence you touched. (The Φ merge introduced "this kind of *reliably*.")
- [ ] Every comment and marker from section 3 is still present (`grep` for them).
- [ ] The review log lists each change by kind (A–D), with before and after text.
- [ ] Anything of kind C or D appears in the log as a *proposal*, not as an edit.

---

## 7. Case study: the Chapter 1 and Chapter Φ merges

**Where your pass was valuable** (keep doing this):

- **A real reasoning error.** The text claimed a brain that appears by chance needs a longer description than one that grew. That's false: identical objects have identical shortest descriptions. You moved the argument to the version that holds (which world keeps supplying coherent experience).
- **A physics subtlety.**
  - The Higgs field's "direction on the circle" is a choice of description (gauge), not a physical fact, so it can't be "address."
  - You swapped in a crystal's orientation, which works.
- **Precision repairs:**
  - "stationary," not "least," action;
  - the gauge *potential* needs its own dynamics before light appears;
  - Born's rule for particles versus light;
  - Weinberg's 1987 result as an upper bound;
  - de Sitter's few symmetries versus its horizon entropy;
  - Goldstone modes from global symmetries only;
  - graphene as "Dirac-like";
  - the corrected count of causally disconnected regions.
- **Source verification** with links, and **honest hedges** that fit the book ("my wager," "a bet, not a result").

**Where your pass overreached** (the kinds of changes to stop):

1. **A signature term changed.** "Possibility space" became "spaces of possibilities." *(Section 3.)*
2. **All seven OVERLAP markers deleted**, including the reminder to fix a sentence in Interlude 12. *(Section 3.)*
3. **Forward pointers deleted** ("Interlude 12 will pull hard on this thread"). *(Section 3.)*
4. **A thesis deleted as if it were an error.** The author's reading of time (the gap "is what we spend when we say time passes") was replaced with "doesn't yet explain time itself." It's an interpretation Interlude 12 is meant to earn. *(Kind D: label it, don't delete it.)*
5. **Correct, vivid lines replaced with referee-report prose:**
   - Dyson and Lenard's stability result, which is the original authors' own claim;
   - the cup-through-table odds ("more zeros than this book has letters," a safe understatement);
   - "an atom takes from light only the frequencies it can itself sing" (needed only "while it keeps its electrons");
   - "light is the cost of letting every electron keep its own clock" (needed a qualifying clause, not deletion).

   *(Kind C or B: the smallest repair, or none.)*
6. **The intuition removed and only the formalism kept.** Standish's head-count picture behind the simplicity formula. Novice readers need the picture; keep both.
7. **A thread broken by a deletion.** In Φ, cutting the anthropic-seat sentence orphaned later references to "the anthropic seat." Before deleting anything, `grep` the manuscript for words that refer back to it.
8. **An error introduced:** "equally low field values" in a figure and its caption. *(Section 5.)*
9. **A typo introduced:** "reliably" for "reliability." *(Section 6.)*

**The pattern to aim for.** Your best edits found the places where the reasoning was wrong and repaired the reasoning. Your weakest edits found places where the reasoning was *unusual* and replaced it with the usual. The book needs the first and not the second. Where its window shows something the standard window doesn't, keep both views and let the reader compare them.
