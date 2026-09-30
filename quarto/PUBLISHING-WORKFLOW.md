# POMA publishing workflow

`../manuscripts/` is the canonical editorial source. Files under `content/` are generated Quarto representations and must not be edited by hand.

The current deployment remains the established Guten Cloudflare Pages project at `guten.pages.dev`. Its deployable files live in the separate `launch-pages` repository so that `/poma/` and `/livingstack/` remain under one Pages hostname.

The sync script generates all 121 canonical manuscript units and their assets. `_quarto.yml` is the authoritative publication order and inclusion list. Routine manuscript revisions require no script change: synchronize, render, review, and stage. Never copy or edit generated QMD by hand.

Volume III uses the accepted sequential publication numbers 23–33 as of canonical revision `31922e9`. The stable `unit_id` and `original_chapter_id` fields remain provenance identifiers; `current_chapter_number` controls generated filenames, chapter labels, Open numerals, and navigation. The generated `content-manifest.json` records both the original-identity order and current reading order. Future renumbering must update the canonical filenames and labels, editorial manifest, `_quarto.yml`, and all numbering consumers in the sync script together.

To prepare and review the complete POMA reading edition:

```sh
cd /Users/samseatt/projects/book-poma/quarto
./scripts/sync-manuscripts.py
quarto preview
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
