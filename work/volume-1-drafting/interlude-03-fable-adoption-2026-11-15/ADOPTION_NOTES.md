# Interlude 3 — Fable adoption

**15 November 2026.** Single-pass merge authorized by Sam; incoming `book_poma/sam/claude/fable/03-interlude.md` is the substantive master and remains read-only. Canonical destination: `manuscripts/volume-1/03-interlude.md`. Input hashes and baseline are in `provenance.json`.

## Adopted material and preservation

Added Fable’s switching-power equation, CUDA bridge, host/device explanation, matrix-work count, Roofline equation and B200 connection figures. These deepen the hardware prerequisite for the later software/ML spine. Bob gains the Chapter 3 manifold callback.

The original chapter is otherwise intact. No essential old prose, joke or technical explanation needed recovery. The Nature Inc. opening, uptime line, Moore–Good coincidence, computer-school and family scenes, instruction/memory teaching, brain rhythms, old Bob argument and final Milwaukee transition survive. Bob’s only local repair is to its newly added manifold sentence. All 25 incoming HTML comments, the two old diagram references, header and closing remain.

## Local repairs

Exact A–D classifications and before/after text are in `change-log.json`. These are B precision/reference repairs, not a new literary or philosophical draft.

- Defined the switching-power variables and activity-factor convention; added the primary derivation to the existing scaling note.
- Clarified that a kernel is a routine, not a batch of routines. The host/device account remains lively, with memory-placement and launch exceptions in its note.
- Changed the matrix count to **distinct elements**, since those values may cross a memory boundary more than once.
- Kept the Roofline formula, identifying it as a ceiling. Specified dense FP8 for the B200 ridge and confined the roughly two-operations-per-weight-byte example to streamed batch-one matrix work. The detailed assumptions remain in the note.
- Marked die-to-die and NVLink ratings as two-way aggregates. Preserved the locality lesson without ranking unlike links as a single descending memory hierarchy. Current 7.7 TB/s B200 HBM specifications justify the prose’s rounded “about 8.”
- Aligned Bob’s neural-manifold callback with the just-adopted Chapter 3: task-dependent activity near a low-dimensional structure. Kept the bands analogy and the wider abstraction-boundary wager.

The four incoming memory-only notes now have verified sources/locators. The 35 earlier notes retain their existing audits; 34 definitions are byte-identical, with only the scaling note extended. All 39 notes are mapped in `source-audit.json`, with inherited evidence distinguished from fresh checks. No unsupported reference is described as newly verified.

## Supplied B200 figure

Sam clarified that Claude constructed this from public sources, **not from NVIDIA artwork**. That provenance is recorded without inventing a list of Claude’s sources. I independently checked the depicted architecture against technical documentation and rendered the supplied SVG at full size.

The two-die package, eight HBM sites, SM/L2 representation, external host and separate die/NVLink connections are useful and legible. SM squares are illustrative, not a count; neither caption nor drawing claims a literal floor plan. **The SVG, including its metadata, is copied byte-for-byte.** No redraw or annotation was needed. Both existing canonical teaching figures also remain unchanged. The inspected preview is in `figure-previews/`.

## Reader value and open inquiry

The hardware now explains why abundant multipliers can still wait: execution requires software launches, usable data reuse, enough memory traffic and an appropriate arithmetic format. The instruction example, tile example and package drawing operate at different scales, so they complement one another. The new equation makes the bottleneck distinction usable rather than merely naming it. This is editorial assessment, not a reader-testing result.

Bob remains open for Sam’s original work. S021 records adaptive abstraction boundaries and the distinction between physical-computing demonstrations and a self-reorganizing architecture. No new claim of machine consciousness, demonstrated originality or solved interpretability was introduced. No substantive author decision blocks this merge.

Protected content, arithmetic and image review: `review-checks.json`. Canonical note/asset/manifest/Pandoc checks: `validation.json`. No publication or edits to another manuscript unit.
