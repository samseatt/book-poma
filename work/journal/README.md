# Author journal

Start in [inbox.md](inbox.md) if you do not want to sort a thought. Use [book.md](book.md) for recurring guidance and [volume-3.md](volume-3.md) for notes on a specific piece. Add plain text under any heading; dates, IDs and polished wording are optional. The editor will organize it when processing a batch. More volume files can be added when those volumes enter active editing.

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

The publisher will remove annotations before Quarto formatting, join surrounding text without doubled spaces caused by removal, and preserve paragraph boundaries, lists, headings, indentation and intentional Markdown line breaks. A malformed, unclosed or nested annotation stops generation with its file and location before existing output is changed. Omission does not mean an addition has been integrated or an instruction fulfilled; it remains pending in the source or journal. The filter and guard are specified in [publisher.md](publisher.md), P-003, and remain pending implementation until the publisher records completion.

Nothing here runs automatically. Ask for a batch by scope, for example: “Process the journal for Chapter 27, historical pass.” The editor reports what was integrated, retained, deferred or needs your input. Commit coherent work with current manuscript hashes; no commit itself authorizes publication.

The shared journal is the durable record; direct task messages can point to it when the author requests coordination. Only one session edits a shared file, stages or commits at a time. Read current files immediately before saving.
