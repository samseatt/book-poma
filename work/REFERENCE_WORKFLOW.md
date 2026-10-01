# References and editions

Editorial policy established 1 October 2026 under the author's instruction to formalize references and coordinate with the publisher. This document governs new source work and later retroactive citation passes. It does not authorize publishing or claim that the print implementation is complete.

## Reader experience

Keep the reading surface clear. Use unobtrusive numbered notes for sources, exact locators and useful qualifications. A note may simply identify evidence; it need not contain an essay. Put a qualification in the main text when omitting it would make the argument misleading. Give the full bibliographic record once in the edition's **Works Cited**.

| Edition | Notes | Works Cited |
|---|---|---|
| Web book | At the relevant chapter/interlude, with linked access and available HTML previews | One consolidated list for the web edition |
| EPUB | Linked notes with return navigation; presentation depends on the reader application | One list for that edition |
| One volume bound separately | At the back of that volume, grouped by manuscript unit | Only works cited in that volume |
| All three volumes bound together | At the back of the book, grouped first by volume, then manuscript unit | One consolidated list for the whole book |

The intended print numbering restarts within each chapter/interlude or other substantial unit, with explicit group headings. The publisher must validate that behavior; it is not the current print configuration. Essential qualifications must not depend on a reader consulting endnotes.

## Canonical Markdown and bibliography

Retain native Markdown notes: `[^stable-note-id]` in the prose and a matching `[^stable-note-id]:` definition. IDs are identities, not visible numbers; output numbering is generated. Make IDs unique across the whole book, including chapter/interlude distinctions. Existing IDs remain valid if a chapter moves. New IDs can use a form such as `v2-14c-record-provenance`; their embedded number must not later be treated as a renumbering instruction. Pandoc documents this distinction between identifiers and rendered numbering in its [footnote specification](https://www.pandoc.org/demo/example33/8.19-footnotes.html).

Use the already configured `quarto/references.bib` as the shared bibliographic database, with one stable ASCII citation key per work or materially distinct edition/translation. This file is an explicit **editor-owned bibliographic-content exception** within the publisher-owned Quarto directory. The publisher owns configuration, citation styling, transformations and rendering. Coordinate any shared-file operation before writing.

As verified on 1 October, that database contains a sample Knuth record rather than the book's researched bibliography. The existing 46 source-note definitions remain self-contained and usable. Populating the database and converting those notes is a separate, gradual migration; no source details are to be discarded before equivalent metadata and locators have been verified.

Use native citation keys and locators inside notes when a bibliographic entry exists. Quarto supports this through its [Pandoc citation syntax and bibliography handling](https://quarto.org/docs/authoring/footnotes-and-citations). Keep authored commentary in the note and repeated publication details in the database. For the initial migration, use an author-date citation style inside explicit notes so that citation processing does not introduce a competing note system. The publisher should preview the typography before it becomes the house rendering style. Direct author-date citations in unusually technical passages remain an editorial option where they improve readability.

Do not hand-number notes or move their definitions around for different bindings. Indent continuation paragraphs correctly. Keep ordinary editorial annotations `[[NOTE: ...]]` separate from source-note syntax; an omitted annotation does not become a reference or resolve a source question.

## Evidence standard

- Verify the passage that supports the claim, not just the existence of a book or web page. Record a page, section, chapter, document number or another recoverable locator where available. Never invent page numbers or missing metadata.
- Distinguish contemporary evidence, later scholarship, translation, contested interpretation and the author's own inference. Use primary records for what they establish and scholarship for interpretation and context.
- Check epigraphs and quotations for wording, attribution and translation. Treat memorable attributions as claims requiring verification.
- Personal recollections belong to the author. Externally checkable zeitgeist and public dates need sources; retrospective clinical or other causal explanations require evidence beyond the recollection itself.
- Future scenes are scenarios. Record their evidentiary baseline, date of assessment, key assumptions and important uncertainties without pretending that a citation proves a future outcome.
- Preserve the difference between a scientific analogy and an empirically established mechanism. Sources should support the specific work a claim does in the argument.

Research records under `work/` should retain the manuscript claim/anchor, source and locator, verification status, qualifications and access date for web material. These working records are not automatically published. The bibliography should contain verified author or institutional author, title, date, edition/translation where relevant, publication details and stable DOI or URL when available. Reuse an existing entry for the same work; use separate records when an edition or translation changes the cited evidence.

The author can continue to leave a source suggestion as `[[NOTE: source or citation to investigate]]`. The editor handles bibliographic syntax and verification. A suggestion is a pending lead until checked.

## Publisher assessment and implementation boundary

On 1 October, **DEVOPS - Cloudflare Publisher** performed a read-only assessment of revision `aae7296`. Its in-memory source-to-QMD comparison retained all 46 note definitions and 48 references across the 121 canonical units. Two repeat references account for the difference. This verifies preservation through that transformation, not a fresh rendered-edition inspection.

The current pipeline supports native notes in HTML and EPUB and already configures `references.bib` and a bibliography page. No PDF print edition is configured. Separate volume editions can be selected through [Quarto project profiles](https://quarto.org/docs/projects/profiles.html). Polished print endnotes grouped by chapter require additional implementation and testing; an ordinary note-location setting alone is not a promise of that layout.

The later publisher task should:

1. Validate a representative native note with a real bibliography citation, locator, repeated reference, multiple paragraphs and return links in HTML and EPUB.
2. Check unknown citation keys, unmatched notes and book-wide note-ID collisions; preserve canonical source and keep editorial annotations out of publication.
3. Establish separate-volume and combined-book profiles, including edition-appropriate cited works without an indiscriminate `nocite` list.
4. Prototype grouped print endnotes and unit numbering in a small print specimen before applying them to a whole volume.

No pipeline, bibliography, manuscript or deployed edition was changed during this policy task. Citation backfill and print construction remain separate work. A journal update, a commit or a message to the publisher does not authorize deployment.
