"""Update only the two data curves of a supplied feed-loop SVG.

Usage: python3 update_feed_figure.py /path/to/a/copy/of/feed-loop.svg
Data come from feed-results.json beside this script. No plotting package needed.
"""
import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

results = json.loads(Path(__file__).with_name('feed-results.json').read_text())
curve = next(r['curve'] for r in results['results']
             if r['habit'] and r['epsilon'] == 0)
target = Path(sys.argv[1])
svg = target.read_text()
matches = list(re.finditer(r'<path d="M600\.0[^"]*" stroke="(?:#111|#777)"', svg))
assert len(matches) == 2, 'Expected the two existing chart paths.'
paths = [f'M600.0 {460-curve[0][k]*350/.6:.1f} ' +
         ' '.join(f'L{600+3.5*t:.1f} {460-row[k]*350/.6:.1f}'
                  for t, row in enumerate(curve[1:], 1)) for k in (0, 1)]
for match, path in reversed(list(zip(matches, paths))):
    replacement = re.sub(r'd="[^"]*"', 'd="'+path+'"', match.group())
    svg = svg[:match.start()] + replacement + svg[match.end():]
ElementTree.fromstring(svg)
target.write_text(svg)
