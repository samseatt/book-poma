#!/usr/bin/env python3
"""Place finished 6 x 9 trim pages unchanged on US Letter carrier sheets."""
from pathlib import Path
import argparse
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject

LETTER_W, LETTER_H = 612.0, 792.0
TRIM_W, TRIM_H = 432.0, 648.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()

    reader = PdfReader(str(args.source))
    writer = PdfWriter()
    dx = (LETTER_W - TRIM_W) / 2
    dy = (LETTER_H - TRIM_H) / 2

    for number, source_page in enumerate(reader.pages, start=1):
        width = float(source_page.mediabox.width)
        height = float(source_page.mediabox.height)
        if abs(width - TRIM_W) > 1 or abs(height - TRIM_H) > 1:
            raise SystemExit(
                f"Page {number} is {width:.2f} x {height:.2f} pt; expected 6 x 9 inches. "
                "Refusing to scale a canonical trim page."
            )
        page = writer.add_blank_page(width=LETTER_W, height=LETTER_H)
        source_page.add_transformation(Transformation().translate(tx=dx, ty=dy))
        source_page.mediabox = RectangleObject((0, 0, LETTER_W, LETTER_H))
        page.merge_page(source_page)

    args.destination.parent.mkdir(parents=True, exist_ok=True)
    with args.destination.open("wb") as handle:
        writer.write(handle)
    print(f"Wrote {len(reader.pages)} unchanged trim pages to {args.destination}")


if __name__ == "__main__":
    main()

