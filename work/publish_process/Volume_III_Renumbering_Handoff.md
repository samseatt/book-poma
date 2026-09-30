# Volume III renumbering handoff — 30 September 2026

The author approved normalizing the already accepted reading sequence. This is an editorial numbering change, with no substantive redraft. The source revision before renumbering is `8a432f7e31196d1973b4d1986432cc5e405302bc`; the commit containing this handoff supplies the new canonical baseline.

| Original identity | Current number | Chapter |
| --- | --- | --- |
| 23 | 23 | The Loom of Renewal |
| 24 | 24 | The Citizen's Dilemma |
| 25 | 25 | Beyond the Invisible Hand |
| 31 | 26 | Minds in Harmony |
| 27 | 27 | The Reclaimed Commons |
| 29 | 28 | The Reimagined Workshop |
| 26 | 29 | The Steward's Edge |
| 30 | 30 | Justice Before Judgement |
| 28 | 31 | The Flow of Care |
| 32 | 32 | The Threads of Continuity |
| 33 | 33 | The Arrow's Release |

Canonical filenames and chapter/interlude labels now use current numbers. Opens travel with their chapters; their prose has no added number. Three in-body chapter/interlude references and the contents listing received the corresponding mechanical number corrections. Existing titles and descriptions were preserved, including any older title differences in the contents listing that need a later editorial review.

## Manifest and provenance

`work/manuscript-manifest.json` now has `current_chapter_number` on the 33 numbered Volume III units. `active_source`, its hash, `canonical_markdown_path` and `planned_markdown_path` point to the current files. `unit_id` and `original_chapter_id` retain their stable historical meanings. The `volume_iii_orders_by_original_chapter_id.final_order` array therefore still contains original IDs; `volume_iii_renumbering.current_reading_order` contains current numbers 23–33. Original design packets, archived Word sources, conversion reports and asset directories are unchanged. Image links intentionally retain their original asset-directory names and still resolve.

The complete per-unit path/hash map is `work/provenance/volume-iii-renumbering-2026-09-30.json`. Conversion reports describe the conversion baseline and should not be rewritten to masquerade as current editorial checksums.

## Publisher follow-up before regeneration

1. In `quarto/scripts/sync-manuscripts.py`, use `current_chapter_number` where present, falling back to `original_chapter_id` for other units. Apply this to the numbered chapter heading in `labelled`, the Roman-numbered Open in `opened`, and output filenames in `out`. Keep stable `unit_id` values for provenance.
2. Change the Volume III numbered triplets in `quarto/_quarto.yml` to current order 23–33. Keep the Theta triplet, overture, part-opening and epilogue in their existing positions. Preserve or explicitly label original-identity order metadata in the generated content manifest.
3. Regenerate from the canonical files, render and check titles, navigation and images. Do not hand-edit generated QMD. The old generated output and live site still describe the preceding publishing revision until this follow-up is done.
4. Publish only when the author invokes the publishing process. This editorial commit does not authorize deployment.
