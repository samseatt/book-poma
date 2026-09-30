#!/usr/bin/env python3
"""Build derived Quarto teaser sources from canonical manuscript Markdown."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
REPO = PROJECT.parent
MANUSCRIPTS = REPO / "manuscripts"
CONTENT = PROJECT / "content"
MARKER = "<!-- Generated from canonical manuscripts; do not edit here. -->"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def generated(*blocks: str) -> str:
    return "\n\n".join([MARKER, *(block.strip() for block in blocks if block.strip())]) + "\n"


def front_matter(text: str) -> str:
    return generated("# Title Page {.unnumbered .visually-hidden}", text)


def contents(text: str) -> str:
    # A source H1 denotes a Part. It must not become another book chapter.
    body = re.sub(r"(?m)^# ", "## ", text)
    return generated("# Contents {.unnumbered}", body)


def introduction(text: str) -> str:
    lines = text.splitlines()
    nonblank = [i for i, line in enumerate(lines) if line.strip()]
    if len(nonblank) < 3:
        raise ValueError("Introduction opening is incomplete")
    image_i, label_i, title_i = nonblank[:3]
    if not lines[image_i].lstrip().startswith("!") or lines[label_i].strip().upper() != "INTRODUCTION":
        raise ValueError("Introduction opening no longer matches the publishing adapter")
    title = lines[title_i].strip()
    rest = "\n".join(lines[title_i + 1 :]).strip()
    opening = "\n\n".join([
        "::: {.chapter-opening}",
        lines[image_i].strip(),
        "[Introduction]{.smallcaps}",
        ":::",
    ])
    return generated(opening, f"# {title} {{.unnumbered}}", rest)


def prologue(text: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.lstrip().startswith("!"):
            lines[i] = f"::: {{.chapter-opening}}\n\n{line.strip()}\n\n:::"
    return generated("# Prologue {.unnumbered}", "\n".join(lines))


SOURCES = [
    ("front-matter/front-matter.md", "front-matter/front-matter.qmd", front_matter),
    ("front-matter/index.md", "front-matter/content-summary.qmd", contents),
    ("front-matter/introduction.md", "front-matter/introduction.qmd", introduction),
    ("volume-1/prologue.md", "volume-1/prologue.qmd", prologue),
]


def resolve_images(markdown: Path) -> list[str]:
    missing = []
    for ref in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", markdown.read_text()):
        target = (markdown.parent / ref.split()[0]).resolve()
        if not target.is_file():
            missing.append(f"{markdown.relative_to(PROJECT)} -> {ref}")
    return missing


def main() -> int:
    if not MANUSCRIPTS.is_dir():
        raise SystemExit(f"Canonical manuscript root is missing: {MANUSCRIPTS}")

    # Only publication derivatives are replaced. Canonical manuscripts are read only.
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir(parents=True)

    records = []
    for source_rel, output_rel, adapter in SOURCES:
        source = MANUSCRIPTS / source_rel
        output = CONTENT / output_rel
        if not source.is_file():
            raise SystemExit(f"Canonical source is missing: {source}")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(adapter(source.read_text()), encoding="utf-8")
        records.append({
            "source": str(source.relative_to(REPO)),
            "source_sha256": sha256(source),
            "output": str(output.relative_to(PROJECT)),
            "output_sha256": sha256(output),
        })

    # Preserve the canonical relative asset layout used by the selected sources.
    asset_sources = [
        (MANUSCRIPTS / "front-matter/assets", CONTENT / "front-matter/assets"),
        (MANUSCRIPTS / "volume-1/assets/prologue", CONTENT / "volume-1/assets/prologue"),
    ]
    for source, target in asset_sources:
        if not source.is_dir():
            raise SystemExit(f"Canonical asset directory is missing: {source}")
        shutil.copytree(source, target, dirs_exist_ok=True)

    missing = []
    for qmd in CONTENT.rglob("*.qmd"):
        missing.extend(resolve_images(qmd))
    if missing:
        raise SystemExit("Broken derived image references:\n" + "\n".join(missing))

    manifest = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "canonical_baseline": "3cb7dfcd125b1fed39088282cd75a75b2fec7eec",
        "scope": "POMA teaser edition",
        "records": records,
        "broken_image_references": 0,
    }
    (PROJECT / "content-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Generated {len(records)} Quarto sources from canonical Markdown.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
