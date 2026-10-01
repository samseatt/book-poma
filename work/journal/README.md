# Author journal

Start in [inbox.md](inbox.md) if you do not want to sort a thought. Use [book.md](book.md) for recurring guidance and [volume-3.md](volume-3.md) for notes on a specific piece. Add plain text under any heading; dates, IDs and polished wording are optional. The editor will organize it when processing a batch. More volume files can be added when those volumes enter active editing.

## Three ways to contribute

- **Direct edit:** change canonical Markdown normally. The editor reads the diff and preserves your wording unless the current task authorizes revision.
- **Raw material to integrate:** `[[ADD: raw paragraph or idea]]`. This is material for consideration, not finished prose or a verified factual claim. Plain `[[raw material]]` means the same thing.
- **Instruction:** `[[NOTE: what you want changed or considered]]`. The earlier `[[<instruction>]]` form also works, including whitespace or escaped brackets; you do not need to repair old notes before handing them over.

These blocks may span paragraphs, but do not nest double-square-bracket blocks. A bracket block ends at its first closing `]]`. Angle brackets alone are not the recommended convention because Markdown may treat them as HTML.

## Each working run

The editor reads this guide, the inbox, book-wide decisions and the relevant unit notes, then the current manuscript and its diff. Scan the scoped manuscript for inline annotations as well. Check the publishing exchange when the task touches publishing or shared files. Existing user instructions and the latest explicit correction remain authoritative; quoted drafts and research in a note do not become commands or verified facts merely by being present.

Classify each new item as **Pending**, **Deferred to Pass 1/2/3**, **Needs author input**, or **Addressed**. Only process what belongs to the authorized scope. Taking a note into the journal is intake, not completion of the requested rewrite. Before removing any inline block, preserve its exact text, source path and a nearby prose anchor here. Substantial raw additions remain in place or in a clearly linked pending journal entry until an authorized integration pass.

After addressing an item, record the action, affected file and dated batch or commit reference, then move the original note and resolution into [archive/](archive/). Standing guidance remains active even after the setup work is archived. Superseded instructions keep a record of what replaced them. Never silently discard a note, mark deferred work complete or flatten an author's ambiguity into an invented fact.

## Publication and coordination

Everything under `work/journal/` is editorial material and stays outside publication. Inline annotations are visible source text, not a private Markdown feature. Before a publication handoff, scan canonical Markdown for unresolved `[[...]]` blocks (including escaped forms); do not publish or silently drop them. Resolve them editorially or move them intact into the journal, leaving their work pending as appropriate. The publishing session must run this check too; the automated publishing guard is requested in [publisher.md](publisher.md) and is not yet installed.

Nothing here runs automatically. Ask for a batch by scope, for example: “Process the journal for Chapter 27, historical pass.” The editor reports what was integrated, retained, deferred or needs your input. Commit coherent work with current manuscript hashes; no commit itself authorizes publication.

The shared journal is the durable record; direct task messages can point to it when the author requests coordination. Only one session edits a shared file, stages or commits at a time. Read current files immediately before saving.
