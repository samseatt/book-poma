#!/usr/bin/env python3
"""Build three independent 6 x 9 POMA volumes and matching Letter proofs."""
from __future__ import annotations

from pathlib import Path
import argparse
import os
import re
import shutil
import subprocess
import sys

PROJECT = Path(__file__).resolve().parent.parent
CONTENT = PROJECT / "content"
PRINT = PROJECT / "print"
BUILD = PROJECT / "tmp" / "print-build"
OUTPUT = PROJECT / "output" / "pdf"
MARKER = "<!-- Generated from canonical manuscripts; do not edit here. -->"

VOLUMES = {
    1: {"roman": "One", "part": "The First Archers", "symbol": "00", "numbers": range(1, 12)},
    2: {"roman": "Two", "part": "The Still Arrow", "symbol": "00", "numbers": range(12, 23)},
    3: {"roman": "Three", "part": "The Basket We Weave", "symbol": "00", "numbers": range(23, 34)},
}


def q(path: str) -> str:
    return f"    - {path}"


def reading_order(volume: int) -> list[str]:
    cfg = VOLUMES[volume]
    base = f"content/volume-{volume}"
    paths = ["index.qmd", "print/publisher-notes/volume-%d-opening.qmd" % volume]
    if volume == 1:
        paths.append(f"{base}/prologue.qmd")
    else:
        paths.append(f"{base}/overture-{volume}.qmd")
    paths.append(f"{base}/part-{volume}.qmd")
    paths.extend(f"{base}/{kind}-00.qmd" for kind in ("open", "chapter", "interlude"))
    for number in cfg["numbers"]:
        paths.extend(f"{base}/{kind}-{number:02d}.qmd" for kind in ("open", "chapter", "interlude"))
    if volume in (1, 2):
        paths.append(f"{base}/coda-{volume}.qmd")
    else:
        paths.append("content/back-matter/epilogue.qmd")
    paths.append("print/publisher-notes/volume-%d-closing.qmd" % volume)
    if volume == 3:
        paths.append("content/back-matter/glossary.qmd")
    return paths


def config(volume: int) -> str:
    cfg = VOLUMES[volume]
    chapters = "\n".join(q(path) for path in reading_order(volume))
    return f'''project:
  type: book
  output-dir: _book

book:
  title: "The Path of Many Arrows"
  subtitle: "Volume {cfg['roman']}: {cfg['part']}"
  author: "Sam Seatt, with Carbon and Silicon"
  output-file: poma-volume-{volume}-interior
  chapters:
{chapters}

bibliography: references.bib

execute:
  enabled: false

format:
  pdf:
    documentclass: book
    classoption:
      - twoside
      - openright
    pdf-engine: lualatex
    latex-max-runs: 14
    latex-clean: false
    keep-tex: true
    toc: true
    toc-depth: 1
    number-sections: false
    mainfont: "STIX Two Text"
    mathfont: "STIX Two Math"
    colorlinks: false
    linkcolor: black
    urlcolor: black
    citecolor: black
    include-in-header:
      - print/latex/poma-print.tex
    filters:
      - print/filters/print-images.lua
'''


def run(command: list[str], cwd: Path, env: dict[str, str] | None = None) -> None:
    print("+", " ".join(command), flush=True)
    process_env = os.environ.copy() if env is None else dict(env)
    # LuaLaTeX rejects the bare C locale inherited by some automated shells.
    process_env["LANG"] = "en_US.UTF-8"
    process_env["LC_ALL"] = "en_US.UTF-8"
    subprocess.run(command, cwd=cwd, env=process_env, check=True)


def latex_escape(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "#": r"\#",
        "$": r"\$", "%": r"\%", "&": r"\&", "_": r"\_",
        "^": r"\textasciicircum{}", "~": r"\textasciitilde{}",
        "∅": r"\ensuremath{\varnothing}",
    }
    return "".join(replacements.get(char, char) for char in value)


def plain_inline(value: str) -> str:
    value = value.strip().strip("*").strip()
    match = re.fullmatch(r"\[([^]]+)]\{\.smallcaps}", value)
    return (match.group(1) if match else value).strip()


def wrap_leading_epigraph(body: str) -> str:
    if not body.startswith(">"):
        return body
    quote, separator, rest = body.partition("\n\n")
    lines = [re.sub(r"^> ?", "", line) for line in quote.splitlines()]
    return (
        "```{=latex}\n\\begin{pomaepigraph}\n```\n\n"
        + "\n".join(lines)
        + "\n\n```{=latex}\n\\end{pomaepigraph}\n```\n\n"
        + (rest if separator else "")
    )


def transform_labelled(text: str, path: Path) -> str:
    pattern = re.compile(
        r"^" + re.escape(MARKER) + r"\n\n"
        r"::: \{\.chapter-opening}\n\n(?P<image>!\[[^]]*]\([^)]+\))\n\n"
        r"\[(?P<label>[^]]+)]\{\.smallcaps}\n\n:::\n\n"
        r"# (?P<title>.+?) \{\.unnumbered}\n\n"
        r"::: \{\.chapter-opening}\n\n(?P<meta>.*?)\n\n:::\n\n(?P<body>.*)$",
        re.DOTALL,
    )
    match = pattern.match(text)
    if not match:
        raise SystemExit(f"Print opening not recognized: {path}")
    meta = match.group("meta").split("\n\n")
    subtitle = plain_inline(meta[0]) if meta else ""
    discipline = plain_inline(meta[1]) if len(meta) > 1 else ""
    toc_title = match.group("title")
    display_title = re.sub(r"^\d+\s+", "", toc_title)
    opening = (
        f"{MARKER}\n\n# {toc_title} {{.unnumbered}}\n\n"
        "```{=latex}\n\\begin{pomaunitopening}\n```\n\n"
        f"{match.group('image')}\n\n"
        "```{=latex}\n"
        f"\\pomaunitlabel{{{latex_escape(match.group('label'))}}}\n"
        f"\\pomaunittitle{{{latex_escape(display_title)}}}\n"
        f"\\pomaunitsubtitle{{{latex_escape(subtitle)}}}\n"
        f"\\pomaunitdiscipline{{{latex_escape(discipline)}}}\n"
        "\\end{pomaunitopening}\n```\n\n"
    )
    return opening + wrap_leading_epigraph(match.group("body"))


def transform_open(text: str, path: Path) -> str:
    pattern = re.compile(
        r"^(?P<prefix>" + re.escape(MARKER) + r"\n\n# (?P<title>Open .+?) \{\.unnumbered}\n\n)"
        r"::: \{\.book-open}\n\n(?P<body>.*)\n\n:::\s*$",
        re.DOTALL,
    )
    match = pattern.match(text)
    if not match:
        raise SystemExit(f"Print Open not recognized: {path}")
    return (
        match.group("prefix")
        + "```{=latex}\n\\thispagestyle{empty}\n\\begin{book-open}\n```\n\n"
        + match.group("body")
        + "\n\n```{=latex}\n\\end{book-open}\n\\clearpage\n```\n"
    )


def transform_title_plate(text: str, path: Path) -> str:
    heading = re.search(r"^# (?P<title>.+?) \{\.unnumbered}\s*$", text, re.MULTILINE)
    image = re.search(r"!\[[^]]*]\([^)]+\)", text)
    if not heading or not image:
        raise SystemExit(f"Print title plate not recognized: {path}")
    # Remove only the wrapper around the first image; later artwork remains in place.
    start = text.find("::: {.chapter-opening}", 0, image.start())
    if start >= 0:
        end = text.find(":::", image.end())
        if end < 0:
            raise SystemExit(f"Unclosed title-plate wrapper: {path}")
        end += 3
        before, after = text[:start], text[end:]
    else:
        before, after = text[:image.start()], text[image.end():]
    plate = (
        "```{=latex}\n\\begin{pomatitleplate}\n```\n\n"
        + image.group(0)
        + "\n\n```{=latex}\n\\end{pomatitleplate}\n\\clearpage\n```"
    )
    return before.rstrip() + "\n\n" + plate + "\n\n" + after.lstrip()


def transform_prologue(text: str, path: Path) -> str:
    pattern = re.compile(
        r"^" + re.escape(MARKER) + r"\n\n# Prologue \{\.unnumbered}\n\n"
        r"::: \{\.chapter-opening}\n\n(?P<image>!\[[^]]*]\([^)]+\))\n\n:::\n\n"
        r"(?P<body>.*)$",
        re.DOTALL,
    )
    match = pattern.match(text)
    if not match:
        raise SystemExit(f"Print Prologue opening not recognized: {path}")
    blocks = match.group("body").split("\n\n")
    if len(blocks) < 4 or not blocks[2].startswith(">"):
        raise SystemExit(f"Print Prologue epigraph not recognized: {path}")
    attribution = "\n".join(re.sub(r"^> ?", "", line) for line in blocks[2].splitlines())
    epigraph = "\n\n".join([blocks[0], blocks[1], attribution])
    rest = "\n\n".join(blocks[3:])
    return (
        f"{MARKER}\n\n# Prologue {{.unnumbered}}\n\n"
        "```{=latex}\n\\begin{pomanamedopening}\n```\n\n"
        f"{match.group('image')}\n\n"
        "```{=latex}\n\\pomanamedtitle{The Basket in the Sky}\n"
        "\\pomanamedlabel{Prologue}\n"
        "\\end{pomanamedopening}\n\\begin{pomaepigraph}\n```\n\n"
        + epigraph
        + "\n\n```{=latex}\n\\end{pomaepigraph}\n```\n\n"
        + rest
    )


def transform_part(text: str, path: Path) -> str:
    heading = re.search(r"^# Part \d+ \{\.unnumbered}\s*$", text, re.MULTILINE)
    image = re.search(r"!\[[^]]*]\([^)]+\)", text)
    if not heading or not image:
        raise SystemExit(f"Print Part opening not recognized: {path}")
    plate = (
        "```{=latex}\n\\begin{pomatitleplate}\n```\n\n"
        + image.group(0)
        + "\n\n```{=latex}\n\\end{pomatitleplate}\n\\clearpage\n```"
    )
    return text[:image.start()] + plate + text[image.end():]


def transform_named(text: str, path: Path) -> str:
    pattern = re.compile(
        r"^" + re.escape(MARKER) + r"\n\n"
        r"::: \{\.chapter-opening}\n\n(?P<image>!\[[^]]*]\([^)]+\))\n\n"
        r"\[(?P<label>[^]]+)]\{\.smallcaps}\n\n:::\n\n"
        r"# (?P<title>.+?) \{\.unnumbered}\n\n(?P<body>.*)$",
        re.DOTALL,
    )
    match = pattern.match(text)
    if not match:
        raise SystemExit(f"Print named opening not recognized: {path}")
    label = match.group("label").replace(" Ii", " II").replace(" Iii", " III")
    opening = (
        f"{MARKER}\n\n# {match.group('title')} {{.unnumbered}}\n\n"
        "```{=latex}\n\\begin{pomanamedopening}\n```\n\n"
        f"{match.group('image')}\n\n"
        "```{=latex}\n"
        f"\\pomanamedtitle{{{latex_escape(match.group('title'))}}}\n"
        f"\\pomanamedlabel{{{latex_escape(label)}}}\n"
        "\\end{pomanamedopening}\n```\n\n"
    )
    return opening + wrap_leading_epigraph(match.group("body"))


def transform_generic(text: str, path: Path) -> str:
    heading = re.search(r"^# (?P<title>.+?) \{\.unnumbered[^}]*}\s*$", text, re.MULTILINE)
    if not heading:
        raise SystemExit(f"Generic print heading not recognized: {path}")
    insertion = (
        "\n\n```{=latex}\n"
        f"\\pomagenericchapter{{{latex_escape(heading.group('title'))}}}\n"
        "```"
    )
    return text[:heading.end()] + insertion + text[heading.end():]


def prepare_print_sources(root: Path, volume: int) -> None:
    paths = [(relative, root / relative) for relative in reading_order(volume) if relative != "index.qmd"]
    for relative, path in paths:
        name = path.name
        text = path.read_text()
        if name.startswith(("chapter-", "interlude-")):
            text = transform_labelled(text, path)
        elif name.startswith("open-"):
            text = transform_open(text, path)
        elif name.startswith("part-"):
            text = transform_part(text, path)
        elif name == "prologue.qmd":
            text = transform_prologue(text, path)
        elif name.startswith(("coda-", "overture-")) or name == "epilogue.qmd":
            text = transform_named(text, path)
        else:
            text = transform_generic(text, path)
        path.write_text(text)


def prepare(volume: int) -> Path:
    root = BUILD / f"volume-{volume}"
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    shutil.copytree(CONTENT, root / "content")
    shutil.copytree(PRINT, root / "print")
    shutil.copy2(PROJECT / "references.bib", root / "references.bib")
    prepare_print_sources(root, volume)
    cfg = VOLUMES[volume]
    (root / "index.qmd").write_text(
        "# The Path of Many Arrows {.unnumbered .unlisted}\n"
    )
    (root / "_quarto.yml").write_text(config(volume))
    return root


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", type=int, choices=(1, 2, 3), action="append")
    parser.add_argument("--skip-sync", action="store_true")
    args = parser.parse_args()
    volumes = args.volume or [1, 2, 3]

    if not args.skip_sync:
        run([sys.executable, str(PROJECT / "scripts" / "sync-manuscripts.py")], PROJECT)

    runtime_python = os.environ.get("POMA_PDF_PYTHON", sys.executable)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for volume in volumes:
        root = prepare(volume)
        run([runtime_python, str(PROJECT / "scripts" / "grayscale-print-assets.py"), str(root / "content")], PROJECT)
        run(["quarto", "render", "--to", "pdf"], root)
        logs = list(root.glob("*.log"))
        if not logs:
            raise SystemExit(f"Expected a retained LuaLaTeX log in {root}")
        missing = [log for log in logs if "Missing character:" in log.read_text(errors="replace")]
        if missing:
            raise SystemExit("LaTeX reported missing glyphs in " + ", ".join(map(str, missing)))
        source = root / "_book" / f"poma-volume-{volume}-interior.pdf"
        if not source.is_file():
            candidates = list((root / "_book").glob("*.pdf"))
            if len(candidates) != 1:
                raise SystemExit(f"Expected one rendered PDF in {root / '_book'}, found {len(candidates)}")
            source = candidates[0]
        interior = OUTPUT / source.name
        shutil.copy2(source, interior)
        proof = OUTPUT / f"poma-volume-{volume}-home-letter.pdf"
        run([runtime_python, str(PROJECT / "scripts" / "make-letter-proof.py"), str(interior), str(proof)], PROJECT)
        run([runtime_python, str(PROJECT / "scripts" / "validate-print.py"), str(interior), str(proof)], PROJECT)

    print(f"Print artifacts are in {OUTPUT}")


if __name__ == "__main__":
    main()
