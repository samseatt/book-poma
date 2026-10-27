"""Original conceptual figure; no source artwork reproduced. Python stdlib SVG."""
from pathlib import Path
from html import escape
P=Path(__file__).parent
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="1040" viewBox="0 0 1120 1040" role="img" aria-labelledby="title desc">
<title id="title">Remembering is reconstruction and source judgment</title>
<desc id="desc">A partial cue recruits linked features from overlapping traces. Reconstructed content can be familiar while its origin remains uncertain. Source judgments use context, sensory details, and evidence of imagining or thinking. The outcome can be accurate recall, uncertainty, or misattribution. This is a conceptual illustration, not a fixed serial neural circuit.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 1 L 9 5 L 0 9 Z" fill="#333"/></marker></defs>
<style>text{font-family:Arial,Helvetica,sans-serif;font-size:25px;fill:#171717}.title{font-size:30px;font-weight:bold}.head{font-size:26px;font-weight:bold}.small{font-size:23px}.line{fill:none;stroke:#333;stroke-width:2.4;stroke-linecap:round}.panel{fill:#fafafa;stroke:#888;stroke-width:1.2}.hint{fill:none;stroke:#777;stroke-width:2;stroke-dasharray:6 5}</style>
<rect width="1120" height="1040" fill="white"/>
''']
def add(s):parts.append(s)
def text(x,y,t,c='',anchor='start'):
    add(f'<text x="{x}" y="{y}" class="{c}" text-anchor="{anchor}">{escape(t)}</text>')
def box(x,y,w,h,fill='#fafafa',stroke='#888',rx=8):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
def line(d,arrow=False,cls='line'):
    add(f'<path d="{d}" class="{cls}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def circle(x,y,r,filled=False,dashed=False):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="'+('#444' if filled else 'white')+'" stroke="#444" stroke-width="2.4"'+(' stroke-dasharray="5 4"' if dashed else '')+'/>')
text(32,46,'A   A fragment can reinstate linked details','title')
box(32,68,1056,334)
text(170,110,'PARTIAL CUE','head','middle')
for x,y in [(132,172),(202,172),(167,234)]:circle(x,y,15,True)
line('M 132 172 L 202 172 L 167 234 Z')
text(170,293,'A smell, a word,','small','middle');text(170,324,'a piece of a scene','small','middle')
line('M 278 204 L 369 204',True)
text(540,110,'RECONSTRUCTION','head','middle')
points=[(460,175),(552,157),(635,196),(604,274),(498,267),(550,218)]
for a,b in [(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(1,5),(2,5),(3,5),(4,5)]:
    line(f'M {points[a][0]} {points[a][1]} L {points[b][0]} {points[b][1]}',cls='hint' if a==3 else 'line')
for i,(x,y) in enumerate(points):circle(x,y,14,i in [0,1,5],i==3)
text(540,331,'Learned associations','small','middle');text(540,363,'help complete the pattern.','small','middle')
line('M 692 204 L 763 204',True)
text(920,146,'A recovered episode?','head','middle')
text(920,203,'A related episode?','small','middle')
text(920,246,'A blend of traces?','small','middle')
text(920,320,'A completed pattern','small','middle');text(920,352,'can still be wrong.','small','middle')
text(32,454,'B   Familiarity does not establish origin','title')
box(32,476,1056,274)
box(62,509,317,192,'#eee','#999')
text(220,548,'“I know this.”','head','middle')
text(220,598,'Felt familiarity','', 'middle');text(220,641,'is one cue,','small','middle');text(220,674,'not a source certificate.','small','middle')
line('M 402 606 L 456 606',True)
text(492,532,'SOURCE JUDGMENT','head')
text(492,579,'What context and sensory detail return?')
text(492,623,'Do I recall seeing, reading or imagining it?')
text(492,667,'Does that origin fit what else I know?')
text(492,714,'Reconstruction and checking can interact.','small')
line('M 560 753 L 560 802',True)
text(32,803,'C   Possible outcomes','title')
for x,title,sub in [(32,'Placed accurately','“I witnessed that.”'),(392,'Origin uncertain','“It feels familiar.”'),(752,'Misattributed','“I saw it”—but only read it.')]:
    box(x,831,336,116,'#fff','#777')
    text(x+168,874,title,'head','middle');text(x+168,918,sub,'small','middle')
text(560,993,'Confidence can accompany any of these outcomes.','head','middle')
parts.append('</svg>')
(P/'memory-reconstruction.svg').write_text('\n'.join(parts))
print(P/'memory-reconstruction.svg')
