#!/usr/bin/env python3
"""Validate trim geometry, page parity, labels, and Letter proof fidelity."""
from pathlib import Path
import argparse
from pypdf import PdfReader

TRIM = (432.0, 648.0)
LETTER = (612.0, 792.0)


def size(page) -> tuple[float, float]:
    return float(page.mediabox.width), float(page.mediabox.height)


def destinations(reader: PdfReader):
    for item in reader.outline:
        if isinstance(item, list):
            continue
        try:
            yield reader.get_destination_page_number(item) + 1, item.title
        except Exception:
            continue


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("interior", type=Path)
    parser.add_argument("proof", type=Path)
    args = parser.parse_args()
    interior = PdfReader(str(args.interior))
    proof = PdfReader(str(args.proof))
    if len(interior.pages) != len(proof.pages):
        raise SystemExit("Interior and Letter proof page counts differ")
    for number, page in enumerate(interior.pages, 1):
        if any(abs(a - b) > 1 for a, b in zip(size(page), TRIM)):
            raise SystemExit(f"Interior page {number} is not 6 x 9 inches: {size(page)}")
    for number, page in enumerate(proof.pages, 1):
        if any(abs(a - b) > 1 for a, b in zip(size(page), LETTER)):
            raise SystemExit(f"Proof page {number} is not Letter: {size(page)}")
    wrong = [(page, title) for page, title in destinations(interior) if page % 2 == 0]
    if wrong:
        raise SystemExit("Top-level units not on recto pages: " + repr(wrong[:10]))
    outline = list(destinations(interior))
    overflowing_opens = []
    for index, (page, title) in enumerate(outline[:-1]):
        if title.startswith("Open ") and outline[index + 1][0] != page + 2:
            overflowing_opens.append((page, title, outline[index + 1][0]))
    if overflowing_opens:
        raise SystemExit(
            "Open must occupy one recto followed by one blank verso: "
            + repr(overflowing_opens[:10])
        )
    labels = interior.page_labels
    first_arabic = next((i for i, value in enumerate(labels) if value == "1"), None)
    if first_arabic is None or not any(value.lower() == "i" for value in labels[:first_arabic]):
        raise SystemExit("Expected Roman prelims followed by Arabic body pagination")
    # Actual missing glyphs are rejected from the LuaLaTeX log by the build
    # driver. PDF text extractors can still emit U+FFFD for correctly embedded
    # complex-script glyph runs, so extraction alone is not a sound failure
    # signal for Persian.
    print(
        f"Validated {len(interior.pages)} pages: 6 x 9 trim, Letter carrier parity, "
        f"all top-level units recto, all Opens one page, "
        f"Arabic body begins on physical page {first_arabic + 1}."
    )


if __name__ == "__main__":
    main()
