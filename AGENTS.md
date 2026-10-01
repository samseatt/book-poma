# Editorial working instructions

This is the working repository for Sam Seatt's *The Path of Many Arrows*. The author's current instructions take precedence over inherited handoff documents and these notes.

## Before working on manuscript text

- Read `work/EDITORIAL_CONTEXT.md` for the decisions established in the current editorial session.
- At the start of each editorial run, read `work/journal/README.md`, `inbox.md`, `book.md` and the relevant unit notes (currently `volume-2.md` and `volume-3.md`). Inspect the current manuscript diff and scan scoped files for inline annotations. Read `work/journal/publisher.md` before publishing-related/shared-file work. Do not treat journal intake as completion of deferred work.
- Consult `work/manuscript-manifest.json` for the active source of each manuscript unit. It records original chapter identities, actual source paths, design packet mappings, and the competing Volume III orders.
- Apply the author's writing guide at `/Users/samseatt/projects/book_poma/_GPT_session_outputs/GPT_writing_and_style_guide.md`. The handoff beside it adds context but does not define this session's entire scope or lock the final order.
- Treat `/Users/samseatt/projects/book_poma` as read-only provenance. Do not edit, rename, delete, or save changes into it. Ignore PDF counterparts, Word lock files, and copy variants, including names ending in `copy`, `_copy`, `copy 2`, etc.

## Manuscript authority and publishing workflow

- The author has replaced the earlier progressive `draft/` migration with a one-time publisher-led conversion into `manuscripts/`. Follow `work/publish_process/Manuscript_Workflow_Brief.md` and the root `MANUSCRIPT-WORKFLOW.md` when established, subject to the author's latest directions. `draft/` is retired as a manuscript destination.
- The author confirmed the full source-of-truth transition on 2026-09-29. Markdown under `manuscripts/` is canonical. Edit canonical files under `manuscripts/front-matter/`, `manuscripts/volume-1/`, `manuscripts/volume-2/`, `manuscripts/volume-3/` and `manuscripts/back-matter/`; preserve their media references and structural conventions.
- Word sources under `archive/docx-originals/` and the old `book_poma` tree are frozen provenance. Never reconvert them over canonical Markdown. Consult them only for historical comparison or an explicitly requested recovery.
- `work/manuscript-manifest.json` has been reconciled to the canonical Markdown paths. Its `legacy_planned_markdown_path` values preserve obsolete `draft/` planning history and are not write instructions. The formal declaration is `archive/SOURCE-OF-TRUTH-DECLARATION.md`.
- Follow `work/REFERENCE_WORKFLOW.md` for source notes, bibliographic evidence and edition-specific reference presentation. The editor owns bibliographic content in the already configured `quarto/references.bib` as a deliberate exception within publisher-owned infrastructure; the publisher owns citation configuration, transformations and rendering. Citation migration and grouped print endnotes remain pending until separately implemented and verified.
- The drafting/editorial process owns substantive manuscript changes. The publishing process reads `manuscripts/` after transition and owns Quarto representations, styles, validation and deployment. It reports manuscript problems for correction instead of silently rewriting canonical prose.
- After the initial conversion baseline, the editor commits manuscripts and substantive editorial records; the publisher commits publishing infrastructure. Coordinate changes to shared files such as `README.md`, `AGENTS.md` and workflow manifests, with only one session editing each shared file at a time.
- Only one session may stage or commit in the shared checkout at a time, even when file assignments are disjoint. Check the branch and working tree before starting and preserve other sessions' uncommitted work.
- Concurrent drafting sessions must have disjoint assigned files or an explicit handoff. Read the current Markdown immediately before editing, preserve the author's intervening edits, and commit coherent editorial milestones with messages identifying the affected unit. Commit messages document changes but do not prevent simultaneous-write conflicts.
- Recommended publishing handoff: identify and freeze the source revision for each build, preferably a named commit. If the author requests publication of current uncommitted changes, explicitly include those in a fixed snapshot and record it. Publishing remains manually invoked by the author; a commit does not itself authorize publication.
- Preserve epigraphs, notes, citations, tables, equations, artwork and meaningful emphasis through conversion. Exclude struck-through/deleted material. Consult the reading review for appended legacy text inside otherwise current Word documents, particularly Theta interlude and the Chapter 33 pair; retain valuable excluded material as working provenance.

## Author annotations and publication

- The author may make direct edits, embed raw additions as `[[ADD: ...]]` (or plain `[[...]]`), and instructions as `[[NOTE: ...]]` (or legacy `[[<...>]]`). Accept multiline and escaped forms. Preserve original note text and its source anchor before clearing a block; process only within the current authorized scope.
- The author approved publication-only omission of all complete `[[...]]` annotation blocks on 2026-10-01, including ADD, NOTE, untagged, legacy angle-bracket and escaped forms. Keep canonical Markdown and journal notes unchanged; omission does not resolve editorial work. Remove annotations before Quarto formatting, tidy only the removal boundaries, and stop on malformed/unclosed/nested delimiters before changing generated output. No HTML passthrough is authorized. Journal files stay outside publication. Implementation is tracked in `work/journal/publisher.md` (P-003). Existing single-bracket placeholders are outside this rule.
- Historical integration, design/voice condensation, and future-vignette reconstruction are separate passes. Preserve factual São Paulo and South Health Campus recollections, authored Mirror/Breadboard ideas, and implicit Overture/Epilogue threads. Consult the journal for details.

## Identity and editorial work

- Historical Word-selection rules remain provenance only. Leading 5/6/7 was a book-component prefix, not a volume number. Never use Word duplicate selection to override canonical Markdown. Chapter 24's replacement and corrected titles are already represented in the canonical files.
- Volume III was renumbered with author approval on 2026-09-30. Current filenames and chapter/interlude labels run sequentially from 23 to 33. Original identities 23,24,25,31,27,29,26,30,28,32,33 map to those current numbers. Preserve `unit_id` and `original_chapter_id` as stable provenance; use `current_chapter_number` and `active_source` for current numbers and files. Design packets, conversion reports, archived Word files and asset directories retain their original identities. See `work/provenance/volume-iii-renumbering-2026-09-30.json`.
- A chapter, its cold open, and its paired interlude move together. Filenames and source headings may retain earlier titles; do not silently renumber or infer a new chapter identity from a stale title.
- Historical anchors, future gates, and source quotations require verification before being represented as established facts. Keep researched conditions, proposed design responses, and invented future scenes distinguishable.
- Preserve factual autobiography without inventing details. Future vignettes are conjectural, with plausible dates, places, capabilities, and personal circumstances.
- Preserve the author's voice while compressing repetition and prose that adds no thought, mechanism, evidence, scene, rhythm, or emotional development.
- Keep all research and manuscript editing local unless the author requests publication or communication to others.

- Descriptive filename titles may change without changing manuscript identity. If a stored Word path is missing, rediscover the eligible source by its stable prefix (for example `7 24c -`), update the recorded path, and retain provenance. Archived Word prefixes remain frozen; canonical Markdown now uses the author-approved current numbering.
