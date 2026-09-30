# POMA publishing workflow

`../manuscripts/` is the canonical editorial source. Files under `content/` are generated Quarto representations and must not be edited by hand.

The current deployment remains the established Guten Cloudflare Pages project at `guten.pages.dev`. Its deployable files live in the separate `launch-pages` repository so that `/poma/` and `/livingstack/` remain under one Pages hostname.

To prepare and review the POMA teaser edition:

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
