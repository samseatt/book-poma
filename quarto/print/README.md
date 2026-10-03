# POMA print editions

This directory contains publisher-owned material and typesetting configuration for the three physical volumes. Canonical prose remains under `../../manuscripts/`; generated publication QMD remains under `../content/`.

The commercial interior is a 6 x 9 inch, two-sided, grayscale book block. The Letter proof is made from that finished book block by centering each unchanged trim page on Letter paper at 100 percent. It therefore preserves the commercial edition's line endings and pagination.

Publisher's notes live here because they describe the physical editions rather than alter the authored journey. They are deliberately excluded from the web and EPUB editions.

Cover and jacket files are outside the current scope. They depend on the selected printer, paper stock, binding, final page count, and printer-supplied template.

The typesetting layer preserves equations, Persian right-to-left text, German
quotations and language-specific characters. Decorative Markdown-era icons are
removed or rendered as ordinary bullets in print without changing manuscript
source.

The print build creates a temporary representation for opening-page design:
chapter/interlude composite headers, optional opening epigraphs, title-plate
rectos, titleless one-page Opens, centered thematic rules, and reduced
Coda/Overture ornaments. These transformations do not enter `content/` or the
canonical manuscript. A Part volume must have approved title-plate artwork;
the build stops instead of silently substituting a different layout.
