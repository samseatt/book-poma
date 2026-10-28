"""Original grayscale concept figure for Chapter 5; no borrowed artwork.

Usage: python3 build_figures.py --output /path/to/assets
Default output is this repository's canonical Chapter 5 asset directory.
"""
from pathlib import Path
from html import escape
import argparse

p=argparse.ArgumentParser()
p.add_argument('--output',type=Path)
a=p.parse_args()
out=a.output or Path(__file__).resolve().parents[3]/'manuscripts/volume-1/assets/05-chapter'
out.mkdir(parents=True,exist_ok=True)
svg=['''<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="740" viewBox="0 0 1040 740" role="img" aria-labelledby="title desc">
<title id="title">Bonds, bridges and authority</title>
<desc id="desc">The same six people appear in three panels. Solid lines join people within two groups. Dashed lines add cross-group ties in the second panel. The third adds a separate institution with directed authority links. These are different relations, not measurements of consciousness.</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#222"/></marker></defs>
<rect width="1040" height="740" fill="white"/>
<style>text{font-family:Arial,Helvetica,sans-serif;fill:#171717}.title{font-size:31px;font-weight:700}.head{font-size:27px;font-weight:700}.body{font-size:24px}.small{font-size:22px}.node{font-size:20px;font-weight:700}</style>''']
def text(x,y,t,cl='body',anchor='start'):
 svg.append(f'<text x="{x}" y="{y}" class="{cl}" text-anchor="{anchor}">{escape(t)}</text>')
def line(x1,y1,x2,y2,stroke='#333',width=3,dash='',arrow=False):
 svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
text(36,47,'Bonds, bridges and authority','title')
text(36,83,'The same people; different kinds of relationship.','body')
pts=[(55,250),(118,325),(55,400),(239,250),(176,325),(239,400)]
for i,(name,sub) in enumerate([('BONDS','Who trusts whom?'),('BRIDGES','Who reaches whom?'),('AUTHORITY','Who can decide?')]):
 x=28+i*340
 svg.append(f'<rect x="{x}" y="112" width="324" height="476" rx="8" fill="#fafafa" stroke="#b5b5b5" stroke-width="1.5"/>')
 text(x+162,153,name,'head','middle')
 text(x+162,187,sub,'small','middle')
 # Shift every panel's graph down equally to leave room for an institution.
 coords=[(x+15+px,py+45) for px,py in pts]
 for u,v in [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)]:
  line(*coords[u],*coords[v],stroke='#bbb' if i==2 else '#444',width=2.5)
 if i==1:
  for u,v in [(0,3),(1,4),(2,5)]:line(*coords[u],*coords[v],stroke='#111',width=3,dash='8 6')
 if i==2:
  svg.append(f'<rect x="{x+89}" y="213" width="146" height="42" rx="3" fill="#e4e4e4" stroke="#222" stroke-width="2"/>')
  text(x+162,242,'Institution','small','middle')
  line(x+105,255,coords[0][0]+8,coords[0][1]-20,arrow=True)
  line(x+219,255,coords[3][0]-8,coords[3][1]-20,arrow=True)
 for k,(nx,ny) in enumerate(coords):
  svg.append(f'<circle cx="{nx}" cy="{ny}" r="18" fill="white" stroke="#222" stroke-width="2.5"/>')
  text(nx,ny+7,chr(65+k),'node','middle')
 captions=[['Familiarity, reciprocity,','support within groups.','Insiders can exclude.'],['Access across groups;','new information or help.','A tie can remain unused.'],['Rules, allocation,','permission and sanctions.','Power can lack legitimacy.']][i]
 for j,t in enumerate(captions):text(x+162,500+j*32,t,'small','middle')
line(37,626,87,626);text(100,634,'Within-group tie','small')
line(365,626,415,626,dash='8 6');text(428,634,'Cross-group tie','small')
line(706,626,756,626,arrow=True);text(770,634,'Authority link','small')
text(36,684,'Layers can overlap. A denser graph does not tell us what its connections do.','small')
text(36,719,'Conceptual schematic • no measured network or causal score is implied','small')
svg.append('</svg>')
(out/'social-relations.svg').write_text('\n'.join(svg)+'\n')
print(out/'social-relations.svg')
