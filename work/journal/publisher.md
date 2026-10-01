# Editor–publisher exchange

A shared local record, not an automatic message queue. This file is outside the publication sources. Read it before publishing-related work and update an entry only after its action has actually occurred. Direct messages, when requested by the author, should point to the file and a source commit rather than duplicating book context.

## Participants and ownership

- Editor: **POMA - Master Editor**, task `01a0e374-125a-7b93-a950-e125ddd03731` on `local`.
- Publisher: **DEVOPS - Cloudflare Publisher**, task `01a08884-7b6d-70e1-971e-fb2a4af80b69` on `local`.
- Editor owns canonical manuscript corrections and editorial notes. Publisher owns Quarto generation, formatting, build checks and deployment work.
- Read current branch/status and current files first. One writer per shared file and one session staging/committing at a time. Include the exact source revision in a handoff; a file notification or commit is not publication authorization.

## P-001 — Pending publisher adoption: annotations

**From:** Editor, 30 September 2026. **Status:** Prepared locally; no task message sent and no publisher acceptance recorded.

The author can now use `[[ADD: ...]]` for raw material and `[[NOTE: ...]]` for instructions. Accept plain `[[...]]` as additions and the older `[[<...>]]` as notes, including escaped bracket forms and multiline blocks. These are not private Markdown syntax and must not enter a public build unresolved. All journal files under `work/journal/` are editorial-only and must stay out of generated publication content.

Before syncing/staging for publication, scan canonical Markdown for unresolved annotation delimiters. Report file and location; do not silently strip or reinterpret the note. Ask the editor to integrate the material or preserve it in the journal and clear the source as appropriate. A pending journal item for a later pass does not by itself block publication of the current intentional draft once the marker has been safely removed from manuscript content.

**Requested pipeline improvement:** Add a read-only guard at the start of synchronization, before generated content is removed or written. Check opening and closing delimiters (including escaped forms) so malformed annotations are caught too. This remains a publisher task; no automated guard was installed in this editorial batch.

## P-002 — Current editorial handoff

**Status:** Journal process established; author edits reviewed. Source revision is the commit containing the initial journal, followed by any newer deliberately handed-off commit.

Three author instruction blocks were preserved verbatim in `volume-3.md` and removed from Chapters 26, 27 and 31; their rewrite tasks remain pending. The Overture retains the author's changes with one term adjusted, falsework → shoring. The Chapter 23 local pharmacy naming change is retained. Existing older single-bracket placeholders/TODOs were not reclassified as this new annotation format.

A routine future author-invoked regeneration will pick up the latest canonical text. No publication is requested by this journal entry.

## Publisher replies / new items

<!-- Append a dated response here when this process is adopted or a new issue is found. -->
