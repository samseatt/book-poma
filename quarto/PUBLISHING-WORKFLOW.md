# POMA publishing workflow

`../manuscripts/` is the canonical editorial source. Files under `content/` are generated Quarto representations and must not be edited by hand.

The current deployment remains the established Guten Cloudflare Pages project at `guten.pages.dev`. Its deployable files live in the separate `launch-pages` repository so that `/poma/` and `/livingstack/` remain under one Pages hostname.

The sync script generates all 121 canonical manuscript units and their assets. `_quarto.yml` is the authoritative publication order and inclusion list. Routine manuscript revisions require no script change: synchronize, render, review, and stage. Never copy or edit generated QMD by hand.

Before any generated output is replaced, synchronization preflights every canonical source for author annotations. Complete raw or escaped `[[...]]` blocks are omitted only from the derived publication copy, before title and opening parsing; canonical Markdown and its recorded source hashes remain unchanged. Annotation-only paragraphs and list items are removed without collapsing surrounding Markdown structure, and inline boundaries retain punctuation, paragraph breaks, indentation and two-space hard breaks. Malformed, unmatched, nested or mismatched delimiters stop synchronization with a source path and line/column while preserving the previous generated build. Omission counts and source paths are recorded without note bodies in `content-manifest.json`. The same generated QMD feeds every Quarto output format.

Volume III uses the accepted sequential publication numbers 23–33 as of canonical revision `31922e9`. The stable `unit_id` and `original_chapter_id` fields remain provenance identifiers; `current_chapter_number` controls generated filenames, chapter labels, Open numerals, and navigation. The generated `content-manifest.json` records both the original-identity order and current reading order. Future renumbering must update the canonical filenames and labels, editorial manifest, `_quarto.yml`, and all numbering consumers in the sync script together.

To prepare and review the complete POMA reading edition:

```sh
cd /Users/samseatt/projects/book-poma/quarto
./scripts/sync-manuscripts.py
quarto preview
```

Focused filter regressions can be run with:

```sh
cd /Users/samseatt/projects/book-poma
python3 -m unittest discover -s quarto/tests -v
```

To produce a checked HTML build:

```sh
./scripts/sync-manuscripts.py
quarto render --to html
```

After reviewing `_book/`, stage a freshly synchronized and rendered copy into the existing deployment repository:

```sh
./scripts/stage-guten.sh
```

The staging command synchronizes and renders again to prevent stale output. It does not publish by itself. Review the changes in `/Users/samseatt/projects/launch-pages`, then commit and push that repository. Cloudflare deploys the pushed `guten/` tree to `guten.pages.dev`.

Custom domains are independent aliases. Removing `guten.ink` from this Pages project does not affect `guten.pages.dev` or this workflow.

## Print editions

The print path is independent of the Guten deployment. It produces three physical volumes at 6 x 9 inches and a matching Letter proof for each. Every top-level manuscript unit starts on a recto page. Roman front-matter numbering and Arabic body numbering restart in each physical volume. Copied raster assets are converted to actual grayscale pixels inside the temporary print project; canonical color assets remain unchanged.

Publisher-authored opening and closing notes live under `print/publisher-notes/`. They are print-edition matter and do not modify the canonical manuscript. Volume I contains the Prologue; Volume III contains the Epilogue. Covers remain a later printer-specific workflow.

Install a TeX engine once through Quarto, then build with the bundled Python runtime that supplies `pypdf`:

```sh
quarto install tinytex
cd /Users/samseatt/projects/book-poma/quarto
POMA_PDF_PYTHON=/Users/samseatt/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  ./scripts/build-print.py
```

Use `--volume 1`, `--volume 2`, or `--volume 3` for a focused proof. The script synchronizes canonical manuscripts, renders the 6 x 9 commercial interior, and then places those exact pages without scaling on Letter carrier sheets. Print the Letter file at **Actual size / 100 percent**; never use Fit to page.

Final files are written to `output/pdf/` and ignored by Git. Temporary Quarto projects are written under `tmp/print-build/` and are also ignored. The printer-facing PDF remains provisional until a printer supplies its written PDF, margin, paper, binding, and cover requirements.

The current print pipeline preserves native manuscript notes. Grouped unit endnotes, volume-specific Works Cited, and an editor-supplied index remain future work governed by `../work/REFERENCE_WORKFLOW.md`.

Equations can be authored with ordinary Pandoc/Quarto math syntax, including
inline `$...$` and display `$$...$$` expressions. STIX Two Math supplies the
print mathematics, so a future Schrödinger equation or comparable notation
does not require a pipeline change. The print filter also routes the limited
semantic Unicode mathematics already present in prose through that math font.

Persian text is preserved as joined right-to-left text in Noto Nastaliq Urdu,
using explicit HarfBuzz Persian-script shaping;
German quotation marks, diacritics, and prose remain in the main text face.
These are content and must not be removed as decoration. Emoji-era checkmarks,
pointing hands, pins, warning marks, and similar decorative icons are omitted
or normalized to a plain typographic bullet in the generated print edition.
This transformation does not modify canonical Markdown.

Print opening pages are prepared only inside each temporary print project.
Chapters and interludes use centered composite headers; their Quarto chapter
heads remain in navigation but are suppressed on the printed page. Chapter
epigraphs, and optional interlude epigraphs, use a narrow ruled block. Opens
carry no visible title, use a reduced ornament, and must fit one recto page;
validation fails if the next unit does not begin two physical pages later.
Raster diamond separators and Markdown thematic breaks become the same centered,
thin partial-width rule. Authors should add a separator as `---` on its own line,
with a blank line before and after it. Coda and Overture ornaments render at 60
percent of their earlier proof size.

Parts I, II, and III reserve a complete recto for their title-plate graphic and
begin prose on the verso. Prologue and Epilogue instead use the named-opening
hierarchy shared with Codas and Overtures: title, reduced ornament, label,
epigraph when present, and prose on the same recto. Quarto's required home page
is retained as a contentless build entry, so it adds no duplicate half-title
pages. The Publisher's Note therefore begins on Roman page v, followed by the
blank verso required for the recto body opening. Print and web metadata identify
the author as **Sam Seatt, with Carbon and Silicon**.

The generated print configuration disables computation. Indented or code-like
manuscript prose is therefore typeset as text and cannot accidentally cause
Quarto to launch a Jupyter kernel.
