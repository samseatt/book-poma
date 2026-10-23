#!/usr/bin/env python3
"""Read-only structural check for a canonical POMA manuscript.

Usage: python3 work/editorial-tools/check_manuscript.py manuscripts/volume-1/01-chapter.md
Prints JSON; never changes manuscript, manifest, bibliography or publishing files.
Checks native named footnotes, local Markdown images, active hash and Pandoc output.
Does not certify sources, memoir, prose, annotation handling or visual typography.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit


def note_inventory(text):
    # Work on literal native note syntax; annotations remain author material.
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    definitions = re.findall(r'^\[\^([^\]]+)\]:', text, re.M)
    refs = re.findall(r'\[\^([^\]]+)\](?!:)', text)
    duplicates = [k for k, n in collections.Counter(definitions).items() if n > 1]
    missing = sorted(set(refs) - set(definitions))
    unused = sorted(set(definitions) - set(refs))
    return definitions, refs, duplicates, missing, unused


def nodes(tree):
    if isinstance(tree, dict):
        if 't' in tree:
            yield tree
        for value in tree.values():
            yield from nodes(value)
    elif isinstance(tree, list):
        for value in tree:
            yield from nodes(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manuscript', type=Path)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--pandoc', default=shutil.which('pandoc') or '/Applications/quarto/bin/tools/pandoc')
    args = parser.parse_args()
    repo = args.repo.resolve()
    path = args.manuscript.resolve()
    text = path.read_text()
    definitions, refs, duplicates, missing, unused = note_inventory(text)
    errors, warnings = [], []
    for label, values in [('duplicate note definitions', duplicates), ('missing note definitions', missing), ('unreferenced note definitions', unused)]:
        if values:
            errors.append(f'{label}: {values}')
    if definitions != list(dict.fromkeys(refs)):
        warnings.append('Definitions are not in first-use order; legal Markdown, but review editorial ordering.')
    if '[[' in text:
        warnings.append('Author annotations are present and untouched; this is not the publication annotation guard.')
    if any(ord(c) < 32 and c not in '\n\t' for c in text):
        errors.append('Unexpected control characters.')
    collisions = []
    for other in (repo / 'manuscripts').rglob('*.md'):
        if other.resolve() == path:
            continue
        shared = set(definitions) & set(note_inventory(other.read_text())[0])
        if shared:
            collisions.append({'path': str(other.relative_to(repo)), 'ids': sorted(shared)})
    if collisions:
        errors.append(f'Book-wide note collisions: {collisions}')
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest = json.loads((repo / 'work/manuscript-manifest.json').read_text())
    entries = [d for d in manifest['documents'] if Path(d.get('active_source', {}).get('path', '')).resolve() == path]
    if len(entries) != 1 or entries[0]['active_source'].get('sha256') != digest:
        errors.append('Active manifest entry missing, ambiguous or hash does not match.')
    results = []
    for target in ['json', 'html']:
        command = [args.pandoc, '--from=markdown', '--to=' + target]
        if target == 'html':
            command.append('--mathjax')
        result = subprocess.run(command + [str(path)], capture_output=True, text=True, check=True)
        results.append(result.stdout)
        if result.stderr.strip():
            warnings.append(result.stderr.strip())
    parsed = list(nodes(json.loads(results[0])))
    parsed_notes = sum(n['t'] == 'Note' for n in parsed)
    if parsed_notes != len(refs):
        errors.append(f'Parsed note references: {parsed_notes}; literal references: {len(refs)}. Review literal examples or malformed syntax.')
    backlinks = len(re.findall(r'role="doc-backlink"', results[1]))
    if backlinks != parsed_notes:
        errors.append('Rendered footnote return links do not match parsed notes.')
    if re.search(r'\[\^[^\]]+\]', results[1]):
        errors.append('Unrendered footnote syntax in HTML.')
    for node in parsed:
        if node['t'] == 'Image':
            url = node['c'][-1][0]
            parts = urlsplit(url)
            if not parts.scheme and not parts.netloc and not (path.parent / unquote(parts.path)).exists():
                errors.append('Missing local image: ' + url)
    report = {'path': str(path), 'sha256': digest, 'defined_notes': len(definitions), 'note_references': len(refs), 'parsed_notes': parsed_notes, 'html_note_backlinks': backlinks, 'display_equations': sum(n['t'] == 'Math' and n['c'][0]['t'] == 'DisplayMath' for n in parsed), 'bookwide_note_collisions': collisions, 'warnings': warnings, 'errors': errors, 'passed': not errors}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == '__main__':
    sys.exit(main())
