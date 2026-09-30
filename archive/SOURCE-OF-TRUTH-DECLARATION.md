# Source-of-Truth Declaration

Effective **2026-09-29**, the author has explicitly confirmed the completed Word-to-Markdown conversion of *The Path of Many Arrows*.

The files under `manuscripts/` are now the canonical editorial source for all 121 converted units and their current assets. This declaration follows editor confirmation of Volume III and the author's spot checks across Volumes I, II, and the other manuscript folders.

The author specifically accepted:

- removal of struck-through draft text from Coda II;
- the documented trimming of legacy trailing material, including the residual extra page;
- use of the shared `separator.png` for Opens; and
- the resized front-matter image as the current canonical asset, without reconciling it back to `book_poma`.

The DOCX files under `archive/docx-originals/` and the old `book_poma` directory are frozen provenance. They must not be reconverted over canonical Markdown. Future manuscript editing occurs in `manuscripts/`; publishing systems read from that canonical source.

The detailed unit mapping, source hashes, transformations, and verification results are recorded in `archive/conversion-manifest.json` and `manuscripts/_conversion-reports/`.
