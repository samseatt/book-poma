# Prologue — approved Fable adoption

15 November 2026. Stage 1 compared canonical, root Claude and Fable sources. Sam approved all five recommendations, specified a deep rectangular basket with a central handle, and authorized Publisher coordination for page breaks.

## Change log

| Kind | Before | After / disposition |
| --- | --- | --- |
| C — author approved | Opening's “loud, groaning,” “strange path,” “shuddering and complaining,” and “grinding against an unrest” | Adopt Fable's tighter opening verbatim. |
| C — author approved | “the persistence that had been his whole small world” | “the sameness that had been his whole small world.” |
| C — author approved | Displacement paragraph ends “and the discovery of how thin the familiar really is.” | Accept Fable's deletion; the scene already performs that work. |
| C — author approved | Crossings paragraph ends with the question about reality. | Retain Fable's new “And, as on that plane, the answer was usually stowed somewhere I couldn't see from my seat.” with both AI markers. |
| B — author approved | Fable's “the first spark of whatever became my conscious self” | Restore “the first recorded spark…” from canonical. No other body rewriting. |
| C — author approved visual replacement | Round basket illustration | Deep rectangular woven basket, centered handle across the short span, grayscale ink on white. Same asset path and icon role. |
| A — production repair | Canonical `[[PUB: PAGE-BREAK]]`; incoming comment plus `---` | Preserve incoming comment and replace rule with native `{{< pagebreak >}}`. Publisher owns rendering and epigraph parser repair. |
| A — attribution completion | Epigraph has no source bookmark | Add `v1-prologue-patmos`, identifying the German original, opening stanza lines 3–4, with Hölderlinturm source. English wording unchanged; translator provenance not invented. |
| B — markup alignment | Image alt text “232”; canonical single blockquoted epigraph | Adopt incoming empty decorative alt and three-paragraph epigraph formatting; preserve leading AI-assisted comment. |

No D/thesis alteration was proposed or applied. The exact final sentence and all memoir uncertainties are unchanged. No new scene, joke or philosophical explanation was added.

## Archived annotation

Original canonical path: `manuscripts/volume-1/prologue.md`.

After “The basket was still there.” and before “That boy was me.” the exact block was:

```
[[PUB: PAGE-BREAK]]
```

Its intent is now implemented through a native shortcode, with the incoming comment retained verbatim. It was not silently discarded.

## Source and reader checks

The German epigraph was checked against the opening of Hölderlin's *Patmos* as reproduced with manuscript context by Hölderlinturm Tübingen: https://hoelderlinturm.de/aus-dem-archiv-geholt/band-05-patmos/ (checked 15 November 2026). The exact source/translator of the English wording is not established; it is retained from the author's draft rather than credited to an invented translator. This remaining attribution question does not call for replacing the accepted poem or burdening the opening with publishing commentary.

Memoir details remain the author's recollection, not externally authenticated history. No hard aircraft model, calendar date or physical gesture was added. The Prologue establishes loss of familiar reality and the basket's emotional necessity before Φ's philosophical treatment. Its roughly 512-word scale needs no new explanatory apparatus.

## Artwork and handoff

Generated with the built-in image-generation tool using the old illustration as style reference; inspected at full size and at its small placement in the actual-source print specimen. The deep rectangular shape and central handle remain legible at icon size. The prompt and file hashes are in `audit.json`. The original round asset remains in Git history. The source of the generated file remains in the tool's output directory; the canonical copy is inside the repository.

Publisher task: `DEVOPS - Cloudflare Publisher`, `01a08884-7b6d-70e1-971e-fb2a4af80b69` (local). See P-007 for status. Source and publisher commits are separate; no deployment is authorized.

## Local publication proof

The editorial adoption is committed as `f32dfe1`. The Publisher rendered the actual committed Prologue to HTML and to an isolated PDF using the production opening treatment. The editor independently inspected both story pages: the basket, epigraph and opening fit on recto iii; “The basket was still there.” closes that page, and “That boy was me.” opens verso iv. The final sentence is intact. HTML retains the intended order and an invisible native page-break element; editorial comments do not become visible. This is a local specimen, not a newly published or fully rebuilt book. Publisher implementation completion is tracked in P-007.

Publisher completion commit: `22df859` — `Harden Prologue print transformation`. All 11 automated publishing tests pass. Publisher also rebuilt the complete existing Volume I layout (408 pages); the editor independently inspected physical pages 7–8, printed pages 1–2. The scene fits on recto 1 and the reveal begins verso 2. Geometry, recto, Open and pagination checks passed. Full synchronization remains blocked by seven unrelated missing Volume III SVGs, so Publisher inserted only the exact committed Prologue and basket into the existing ignored generated tree and used `--skip-sync`. This proves the Prologue in the full book layout without claiming that every other current manuscript was freshly synchronized. No push or deployment.
