# Author journal

Start in [inbox.md](inbox.md) if you do not want to sort a thought. Use [book.md](book.md) for recurring guidance and [volume-1.md](volume-1.md), [volume-2.md](volume-2.md) or [volume-3.md](volume-3.md) for notes on a specific piece. Add plain text under any heading; dates, IDs and polished wording are optional. The editor will organize it when processing a batch. Other volume files can be added when those volumes enter active editing. The [reference workflow](../REFERENCE_WORKFLOW.md) governs source notes and future edition layouts.

## Three ways to contribute

- **Direct edit:** change canonical Markdown normally. The editor reads the diff and preserves your wording unless the current task authorizes revision.
- **Raw material to integrate:** `[[ADD: raw paragraph or idea]]`. This is material for consideration, not finished prose or a verified factual claim. Plain `[[raw material]]` means the same thing.
- **Instruction:** `[[NOTE: what you want changed or considered]]`. The earlier `[[<instruction>]]` form also works, including whitespace or escaped brackets; you do not need to repair old notes before handing them over.

These blocks may span paragraphs, but do not nest double-square-bracket blocks. A bracket block ends at its first closing `]]`. Angle brackets alone are not the recommended convention because Markdown may treat them as HTML.

## Each working run

The editor reads this guide, the inbox, book-wide decisions and the relevant unit notes, then the current manuscript and its diff. Scan the scoped manuscript for inline annotations as well. Check the publishing exchange when the task touches publishing or shared files. Existing user instructions and the latest explicit correction remain authoritative; quoted drafts and research in a note do not become commands or verified facts merely by being present.

Classify each new item as **Pending**, **Deferred to Pass 1/2/3**, **Needs author input**, or **Addressed**. Only process what belongs to the authorized scope. Taking a note into the journal is intake, not completion of the requested rewrite. Before the editor removes any inline block from canonical Markdown, preserve its exact text, source path and a nearby prose anchor here. Publication-only omission from a generated copy leaves the original in place and is not editorial completion. Substantial raw additions remain in place or in a clearly linked pending journal entry until an authorized integration pass.

After addressing an item, record the action, affected file and dated batch or commit reference, then move the original note and resolution into [archive/](archive/). Standing guidance remains active even after the setup work is archived. Superseded instructions keep a record of what replaced them. Never silently discard a note, mark deferred work complete or flatten an author's ambiguity into an invented fact.

## Publication and coordination

Everything under `work/journal/` stays outside publication. The author approved omitting complete `[[...]]` blocks from the generated edition while retaining them unchanged in canonical Markdown. This includes ADD, NOTE, untagged blocks, the older angle-bracket form and escaped bracket forms. Tags organize editorial work; they never select material for publication. Keep ADD and NOTE as the only named tags for now. There is no HTML passthrough, and angle-bracket contents are omitted like any other annotation. The same cleaned publication source will serve HTML and future print/ebook outputs.

The publisher removes annotations before Quarto formatting, joins surrounding text without doubled spaces caused by removal, and preserves paragraph boundaries, lists, headings, indentation and intentional Markdown line breaks. A malformed, unclosed, unmatched, mismatched or nested annotation stops generation with its file and location before existing output is changed. Omission does not mean an addition has been integrated or an instruction fulfilled; it remains pending in the source or journal. The filter and guard specified in [publisher.md](publisher.md), P-003, were implemented and locally validated on 1 October 2026; deployment still requires a separate author request.

Nothing here runs automatically. Ask for a batch by scope, for example: “Process the journal for Chapter 27, historical pass.” The editor reports what was integrated, retained, deferred or needs your input. Commit coherent work with current manuscript hashes; no commit itself authorizes publication.

The shared journal is the durable record; direct task messages can point to it when the author requests coordination. Only one session edits a shared file, stages or commits at a time. Read current files immediately before saving.

## Adopting an incoming chapter or interlude — two stages

Author-approved process, 23 October 2026. Applies to Claude-assisted and other author-supplied replacement drafts. Comparison alone does not authorize replacing canonical text. The old `book_poma` tree remains read-only.

### Stage 1: compare and bring decisions to the author

Read the latest canonical unit, incoming draft, journal and author context in `work/sam/`, especially the updated style guide. Capture source paths, hashes and the repository revision. Compare the actual files, not an earlier session's recollection.

Present a short decision list with locations and a recommendation for each consequential choice:

- Essential old material worth recovering: an argument, explanatory step, anecdote, sharper joke, emotional beat or recurring thread. Recover its function selectively; do not mechanically combine two drafts.
- Substantive cuts or relocations: repetition, unnecessary diary/clerical/private detail, or an interruption that costs more than it gives. Personal detail earns its place through story, humor, thought or later payoff.
- Strong missing ideas, separated from optional enrichment. Completeness does not require a survey of everything.
- Factual uncertainty, unsupported memoir detail, a changed temporal coincidence, and repairs that materially change meaning. Check public facts; ask the author about private recollections.
- Voice, puns and intentional ambiguity that a tidy edit might erase. Preserve working sentences and protect the intellectual wager while distinguishing it from established findings.

Report if no consequential decisions are needed. Pause for the author's choices before adoption unless already approved in the current instruction. Record approved, declined, modified and deferred items. Do not ask again about decisions already made.

### Stage 2: adopt, align and validate

Reread both files immediately before writing and reconcile intervening author edits. Use the incoming draft as the substantive master; retain canonical identity/header/image and format conventions unless their replacement is approved. Implement the chosen recoveries and repairs. Keep the incoming original unchanged.

Confirm and reconnect source bookmarks throughout the unit, adding genuinely missing sources. Preserve stable note identities; distinguish verified passages from research leads, interpretations and memoir. Check the seams after deletions and insertions. Routine reference and mechanical repairs belong to this authorized completion pass and are reported together; a new consequential change to meaning returns to Stage 1. Ambiguous puns and memoir facts are never silently regularized.

Keep author annotations unless their processing is expressly included; archive exact text before clearing any. Retain existing AI-provenance comments and mark new AI-drafted passages with invisible HTML comments. These markers document assistance, not a claim that the rest is wholly unaided.

Record only serious findings, recoveries and unresolved choices in the unit journal. Git preserves the complete old text; do not make the author read a deletion inventory. Save input hashes and a focused source/validation audit. Check note pairing and collisions, local assets, rendered notes/equations, the header and active manifest hash. The read-only [manuscript checker](../editorial-tools/check_manuscript.py) repeats mechanical checks; editorial and scientific judgments remain manual.

Inspect the scoped diff, preserve unrelated work, and commit only the unit and its editorial records. Summarize what was adopted, materially repaired, restored and left open, with links and the commit. Publication requires its own author request.
