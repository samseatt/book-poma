#!/usr/bin/env python3
"""Convert copied print-project raster assets to actual grayscale pixels."""
from pathlib import Path
import argparse
from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    converted = 0
    for path in args.root.rglob("*"):
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        with Image.open(path) as source:
            if source.mode in {"1", "L", "LA"}:
                continue
            if "A" in source.getbands():
                alpha = source.getchannel("A")
                target = Image.merge("LA", (source.convert("L"), alpha))
            else:
                target = source.convert("L")
            options = {"quality": 95} if path.suffix.lower() in {".jpg", ".jpeg"} else {}
            target.save(path, **options)
            converted += 1
    print(f"Converted {converted} print assets to grayscale pixels")


if __name__ == "__main__":
    main()

