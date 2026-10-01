# Editor–publisher exchange

A shared local record, not an automatic message queue. This file is outside the publication sources. Read it before publishing-related work and update an entry only after its action has actually occurred. Direct messages, when requested by the author, should point to the file and a source commit rather than duplicating book context.

## Participants and ownership

- Editor: **POMA - Master Editor**, task `01a0e374-125a-7b93-a950-e125ddd03731` on `local`.
- Publisher: **DEVOPS - Cloudflare Publisher**, task `01a08884-7b6d-70e1-971e-fb2a4af80b69` on `local`.
- Editor owns canonical manuscript corrections and editorial notes. Publisher owns Quarto generation, formatting, build checks and deployment work.
- Read current branch/status and current files first. One writer per shared file and one session staging/committing at a time. Include the exact source revision in a handoff; a file notification or commit is not publication authorization.

## P-001 — Superseded: initially proposed annotation blocker

The 30 September proposal would have stopped publication on every unresolved annotation. The author's 1 October direction supersedes that behavior: complete annotations are omitted from publication copies, while malformed annotations stop generation. See P-003. Earlier intake records remain historical provenance.

## P-002 — Current editorial handoff

**Status:** Journal process established; author edits reviewed. Source revision is the commit containing the initial journal, followed by any newer deliberately handed-off commit.

Three author instruction blocks were preserved verbatim in `volume-3.md` and removed from Chapters 26, 27 and 31; their rewrite tasks remain pending. The Overture retains the author's changes with one term adjusted, falsework → shoring. The Chapter 23 local pharmacy naming change is retained. Existing older single-bracket placeholders/TODOs were not reclassified as this new annotation format.

A routine future author-invoked regeneration will pick up the latest canonical text. No publication is requested by this journal entry.

## Publisher replies / new items

<!-- Append a dated response here when this process is adopted or a new issue is found. -->

## P-003 — Authorized publisher implementation: annotation omission and validation

**From:** Editor, 1 October 2026, following the author's explicit request to coordinate with DEVOPS - Cloudflare Publisher. **Status:** Implemented and locally validated by the publisher on 1 October 2026; not deployed. This entry supersedes P-001.

### Desired behavior

- Treat every complete `[[...]]` block in canonical manuscript text as editorial-only: ADD, NOTE, untagged, unknown future tags, multiline blocks, legacy `[[<...>]]` and escaped bracket forms such as `\[\[NOTE: ...\]\]`. No new tag is needed. Do not execute or pass HTML through; remove the whole block from the derived copy.
- Leave canonical `manuscripts/` and `work/manuscript-manifest.json` untouched. Preserve source hashes as hashes of the actual annotated canonical files. Omission is rendering behavior, not editorial completion; the notes remain available to the editor.
- Run the transformation on source text before the existing opening/title/subtitle parsers and Quarto generation. Use the cleaned derived source for every supported output format, including future print. Keep all `work/journal/` files out of publication.
- Handle adjacent blocks and blocks at line/file boundaries. Inline removal must not create doubled boundary spaces; example `one [[NOTE: x]] two` becomes `one two`. Avoid a stray boundary space before punctuation. An annotation-only paragraph disappears without joining two surrounding prose paragraphs. Do not globally normalize whitespace or alter intentional Markdown hard breaks, indentation, lists, code fences, tables or unrelated text. The author reserves double brackets for annotations; examples containing literal double brackets inside manuscript code are not a current use case.
- Nesting is unsupported. Unclosed openers, unmatched closers, nested/malformed blocks or ambiguous boundary cases that cannot be removed safely must produce a clear source path/line error, not silently eat neighboring text or leak markers. Preflight all units before deleting or writing any generated content, so failure preserves the prior build. Verify no annotation delimiters remain in generated publication text.
- Record omitted-block counts and file locations in local validation output or existing provenance records where useful; do not copy note bodies into generated pages or publicly shipped metadata.

### Scope and validation

Implement in publisher-owned pipeline files with focused tests for inline and standalone removal, multiline notes, adjacent blocks, escaped forms, legacy angle-bracket contents, spacing/punctuation, Markdown structural preservation and malformed/nested rejection. Verify the full current 121-unit source remains unchanged, sync all units and perform the relevant local render/build checks. Include a check that a bad annotation leaves existing generated output intact. Use temporary test fixtures rather than adding test annotations to the author's manuscript.

Commit the pipeline work and your completion entry here as a coherent publisher commit. The editor is handing off after committing the policy and will not edit or stage shared files while you work. You may update `work/journal/README.md`, `AGENTS.md` and `MANUSCRIPT-WORKFLOW.md` only as needed to mark the implementation complete and clarify actual behavior; no manuscript prose edits. Report the commit hash, validation and any remaining limitations back to the editor.

**No deployment or push is requested for this handoff.** The author requested the annotation feature and coordination; publication remains separately invoked. Do not alter the launch-pages repository.

### Publisher completion — 1 October 2026

Implemented publication-only omission in `quarto/scripts/sync-manuscripts.py` before all existing title/opening parsers. The preflight recognizes raw and escaped complete blocks, removes annotation-only paragraphs and structural list items, tidies only omission boundaries, retains Markdown hard breaks and indentation, and rejects unclosed, unmatched, mismatched or nested delimiters with source line/column diagnostics. All sources are preflighted before a temporary generated tree is built; a malformed fixture leaves the prior content tree and manifest byte-identical. Generated provenance records the count per source and aggregate locations without note bodies.

Validation covered eight focused regression groups using temporary fixtures, including malformed-build preservation. Full synchronization processed 121 canonical units and reported zero current annotations. Hash comparison confirmed all 302 files under `manuscripts/` remained byte-identical. HTML and EPUB rendering were then exercised locally; no deployment or push was performed. The publisher-owned implementation commit is the commit containing this completion entry.

## P-004 — References: editorial policy and read-only publisher assessment

**1 October 2026. Status:** Policy established; source migration and print implementation pending. The author explicitly requested reference formalization and authorized coordination with **DEVOPS - Cloudflare Publisher**. The editor requested an assessment only, with no repository writes, rendering, commits or deployment. The publisher completed that assessment against `aae7296` and reported the checkout unchanged.

The in-memory transformation of all 121 canonical units preserved 46 note definitions and 48 references. Native notes are compatible with the existing HTML/EPUB path; this assessment was not a fresh rendered proof. `quarto/references.bib` is already configured but still contains the Knuth sample record. No real bibliography migration was performed.

The adopted [reference workflow](../REFERENCE_WORKFLOW.md) retains stable semantic Markdown notes and the configured central bibliography. **Ownership clarification:** the editor owns bibliographic content in `quarto/references.bib`; the publisher owns its configuration, citation style, filters, rendering and validation. This is a deliberate exception within the otherwise publisher-owned Quarto directory. No simultaneous edits or commits.

Web notes remain local to their chapter/interlude. Print notes should collect at the back of the bound edition, grouped by unit, with volume groupings in the combined book and an edition-specific Works Cited. There is no PDF setup yet. Grouped print endnotes and unit numbering need a later implementation/proof; they are not accomplished by this policy entry. Separate-volume profiles also remain pending.

The next technical step, when separately commissioned, is a small representative citation/rendering specimen, followed by bibliography migration support and eventual print profiles/endnotes. The editor will supply verified bibliographic content and precise source locators. Preserve existing self-contained source notes until migration preserves their evidence. **No further implementation, regeneration, push or deployment is requested by this entry.**

**Publisher acknowledgment:** The publisher explicitly accepted this ownership division and edition policy on 1 October, confirmed the print work remains future implementation, and agreed to make no repository changes, renders, commits or deployments during this editorial commit.
