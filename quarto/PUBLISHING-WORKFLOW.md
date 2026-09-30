# POMA publishing workflow

`../manuscripts/` is the canonical editorial source. Files under `content/` are generated Quarto representations and must not be edited by hand.

The current deployment remains the established Guten Cloudflare Pages project at `guten.pages.dev`. Its deployable files live in the separate `launch-pages` repository so that `/poma/` and `/livingstack/` remain under one Pages hostname.

The sync script generates only manuscript roles that have an explicit publication adapter. To add a supported item, enable its path in `_quarto.yml`, run the sync command, and render. If an enabled path is reported missing, the publishing adapter must first be extended for that role; do not copy or edit generated QMD by hand.

To prepare and review the selected POMA reading edition:

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
