# POMA publishing workflow

`../manuscripts/` is the canonical editorial source. Files under `content/` are generated Quarto representations and must not be edited by hand.

The current deployment remains the established Guten Cloudflare Pages project at `guten.pages.dev`. Its deployable files live in the separate `launch-pages` repository so that `/poma/` and `/livingstack/` remain under one Pages hostname.

The sync script generates all 121 canonical manuscript units and their assets. `_quarto.yml` is the authoritative publication order and inclusion list. Routine manuscript revisions require no script change: synchronize, render, review, and stage. Structural changes such as renumbering Volume III require coordinated updates to canonical filenames and labels, the editorial manifest, and `_quarto.yml`. Never copy or edit generated QMD by hand.

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
