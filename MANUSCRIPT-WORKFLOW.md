# The Path of Many Arrows — Manuscript Workflow

The `book-poma` repository is the canonical home of *The Path of Many Arrows*. It separates authoritative manuscript content, temporary drafting work, archived Word sources, and the Quarto publishing system.

## Expected structure

```text
book-poma/
├── README.md
├── MANUSCRIPT-WORKFLOW.md
├── manuscripts/
│   ├── front-matter/
│   ├── volume-1/
│   ├── volume-2/
│   ├── volume-3/
│   ├── back-matter/
│   └── assets/
├── archive/
│   ├── docx-originals/
│   └── conversion-manifest.*
├── quarto/
│   ├── _quarto.yml
│   ├── content/
│   ├── scripts/
│   ├── styles/
│   └── _book/
├── work/
│   ├── volume-3-drafting/
│   ├── research/
│   └── imports/
└── .gitignore
```

## Completed conversion preparation

The publishing/DevOps session completed the one-time migration from `book_poma`:

1. Inventory the authoritative DOCX files across all volumes.
2. Ignore PDFs, obvious copies, obsolete versions, and unrelated notes.
3. Flag ambiguous alternatives for review.
4. Copy and freeze the selected DOCX files as conversion provenance.
5. Convert their contents into the planned Markdown structure.
6. Extract and correctly locate embedded images and other media.
7. Verify sequence, headings, epigraphs, notes, special characters, and media.
8. Record the relationship between each original DOCX and its converted manuscript.
9. Present the conversion for confirmation.

That process is complete. The author confirmed the transition on 2026-09-29, and drafting now occurs directly in canonical files under `manuscripts/`.

## Source-of-truth transition

The converted manuscripts were reviewed and the author explicitly confirmed the source-of-truth transition on 2026-09-29. Therefore:

- `book-poma/manuscripts/` is the source of truth.
- The original DOCX files are frozen historical archives.
- No session should reconvert an archived DOCX over an existing manuscript.
- Future prose, structural, and editorial work occurs in the canonical Markdown.
- The old `book_poma` directory is no longer an active writing location.

## Responsibilities after the transition

The book-drafting session may edit the canonical Markdown under `manuscripts/`, particularly its assigned Volume III files. It should preserve filenames, structural conventions, metadata, media references, and established Markdown patterns unless a coordinated structural change is required.

The drafting session owns substantive writing and editorial changes. It should commit coherent revisions with messages that identify the affected chapter, interlude, or section.

The publishing/DevOps session treats `manuscripts/` as read-only after the transition. It owns:

- the generated publication representation under `quarto/`;
- Quarto configuration and ordering;
- conversion and normalization scripts;
- styles, rendering, validation, and staging;
- deployment into the Guten publication site.

If the publishing process exposes a problem in a canonical manuscript, the publishing session reports it rather than silently altering the manuscript.

## Interaction between the two sessions

The formal handoff point is the canonical Markdown manuscript.

```text
Drafting session
edits book-poma/manuscripts/
        ↓
commits an editorial milestone
        ↓
Publishing session
reads the canonical manuscript
        ↓
generates, validates, and publishes the Quarto representation
```

The drafting session does not need to manage Quarto output or Cloudflare deployment. It only needs to leave the canonical manuscript structurally valid and notify the publishing session when a revision is ready to be rendered.

If multiple drafting sessions are active, each should have an assigned volume or explicit file set. Two sessions should not edit the same manuscript file concurrently. Git commits serve as the handoff and provenance boundary.

The editor makes the initial commit containing the canonical conversion, archives, manifests, workflow documents and related repository work. The author then supplies that revision to the publishing session. After this baseline, the editor commits manuscript changes and substantive editorial records, while the publisher commits publishing infrastructure. Coordinate shared files such as `README.md`, `AGENTS.md` and workflow manifests; only one session should edit each shared file at a time.

Only one session may stage or commit in the shared checkout at a time, even when editing separate files. Before starting, check the current branch, working tree and latest canonical files, and preserve other sessions' unfinished work. Build from an identified commit or an explicitly requested fixed snapshot. Publishing remains manually invoked by the author; a commit does not authorize a push or publication.

The author retains final authority over manuscript content, structural decisions, and the declaration that a conversion or revision is authoritative.
## Author journal and annotation intake

Use [the author journal](work/journal/README.md) for the current collaboration process. Direct author edits remain in canonical Markdown. Raw additions use `[[ADD: ...]]`; instructions use `[[NOTE: ...]]`; plain double brackets and the earlier angle-bracket form remain accepted. Journal intake preserves original text, location and status, and separates deferred work from completed integration. Before each scoped editorial run, read the inbox, standing book guidance and relevant piece notes, then inspect current files and their diffs.

The journal and publisher exchange are outside publication. As authorized on 2026-10-01, the publisher omits all complete double-square-bracket annotations from derived publication text while leaving canonical files unchanged. This includes ADD, NOTE, untagged, legacy angle-bracket and escaped forms. Clean up only whitespace at omission boundaries and preserve meaningful Markdown structure. Malformed, unclosed or nested delimiters stop the build before generated output is changed. No annotation is an HTML passthrough. Omission does not complete the underlying editorial work. The implementation handoff is [P-003 in the shared exchange](work/journal/publisher.md). Task messages can carry a concise handoff when the author requests one. Journal entries do not wake tasks, initiate publication or permit simultaneous edits to shared files.
