"""Original grayscale teaching plot, not experimental data. Requires an explicit destination."""
from pathlib import Path
import argparse,html,json,math,xml.etree.ElementTree as ET
p=argparse.ArgumentParser();p.add_argument('output',type=Path);a=p.parse_args()
a.output.parent.mkdir(parents=True,exist_ok=True)
# Two independent coordinates produce three correlated, centered activity values.
# Basis vectors u=(1,0,.5), v=(0,1,.5) have rank 2.
points=[(-.85,-.65),(-.7,.10),(-.65,.72),(-.32,-.42),(-.25,.35),(-.08,-.83),(.06,.05),(.22,.63),(.35,-.34),(.58,.17),(.75,-.72),(.83,.70)]
def rates(u,v):return(u,v,(u+v)/2)
def project(r):
 x,y,z=r;return(290+135*x-95*y,260+42*x+48*y-125*z)
def P(u,v):return project(rates(u,v))
def Q(u,v):return(850+125*u,248-112*v)
s=['''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="485" viewBox="0 0 1200 485" role="img" aria-labelledby="title desc">
<title id="title">Many neurons, fewer independent changes</title>
<desc id="desc">Original synthetic example of a two-dimensional activity manifold. Three neurons have centered firing-rate changes r1=u, r2=v, r3=(u+v)/2. Their joint states occupy a plane in the three-neuron coordinate space. The same twelve states are shown on the right using u and v. Each dot is a population state, not an individual neuron. Unvisited states are not claimed to be forbidden. All activity units are arbitrary.</desc>
<rect width="1200" height="485" fill="white"/>
<style>text{font-family:Arial,Helvetica,sans-serif;fill:#171717;text-anchor:middle}.title{font-size:30px;font-weight:700}.head{font-size:23px;font-weight:700}.label{font-size:20px}.small{font-size:18px}.axis{stroke:#555;stroke-width:1.6;fill:none}.grid{stroke:#b8b8b8;stroke-width:1;fill:none}.pt{fill:#333;stroke:white;stroke-width:1.6}</style>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#555"/></marker></defs>
<text x="600" y="39" class="title">Many neurons, fewer independent changes</text>
<text x="280" y="85" class="head">A   One axis per neuron</text>
<text x="850" y="85" class="head">B   Two coordinates on the plane</text>
''']
def line(x1,y1,x2,y2,cl='axis',arrow=False):s.append(f'<line class="{cl}" x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def text(x,y,msg,cl='label',anchor=None):s.append(f'<text x="{x}" y="{y}" class="{cl}"'+(f' style="text-anchor:{anchor}"' if anchor else '')+'>'+html.escape(msg)+'</text>')
def poly(pts,fill,stroke):s.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+f'" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>')
# Draw a translucent-looking flat gray domain with a regular coordinate mesh.
poly([P(-1,-1),P(1,-1),P(1,1),P(-1,1)],'#e9e9e9','#aaa')
for v in [-.5,0,.5]:line(*P(-1,v),*P(1,v),'grid')
for u in [-.5,0,.5]:line(*P(u,-1),*P(u,1),'grid')
# The actual three axes are not the two-dimensional plane's coordinate lines.
for r in [(1.35,0,0),(0,1.35,0),(0,0,1.17)]:line(*project((0,0,0)),*project(r),arrow=True)
text(489,329,'Neuron 1')
text(145,348,'Neuron 2')
text(290,106,'Neuron 3')
# Corresponding flat chart.
poly([Q(-1,-1),Q(1,-1),Q(1,1),Q(-1,1)],'#f4f4f4','#aaa')
for v in [-.5,0,.5]:line(*Q(-1,v),*Q(1,v),'grid')
for u in [-.5,0,.5]:line(*Q(u,-1),*Q(u,1),'grid')
line(710,360,995,360,arrow=True);line(725,373,725,116,arrow=True)
text(850,390,'Coordinate u')
s.append('<text x="694" y="248" class="label" transform="rotate(-90 694 248)">Coordinate v</text>')
for i,(u,v) in enumerate(points):
 for fx in [P,Q]:
  x,y=fx(u,v);s.append(f'<circle class="pt" cx="{x:.2f}" cy="{y:.2f}" r="5.5"/>')
# A single labeled state appears in both charts.
x,y=P(*points[7]);text(round(x+17,2),round(y-12,2),'a','small')
x,y=Q(*points[7]);text(round(x+17,2),round(y-8,2),'a','small')
line(548,240,652,240,arrow=True)
text(600,207,'Same states,','small');text(600,228,'new coordinates','small')
text(280,389,'Gray plane: correlated population activity','small')
text(600,433,'Each dot is a state of all three neurons together.','label')
text(600,462,'Synthetic illustration • arbitrary activity units • real manifolds can be curved, noisy and task dependent','small')
s.append('</svg>');svg='\n'.join(s)+'\n';ET.fromstring(svg);a.output.write_text(svg)
# Independent construction checks, retained with the generator.
assert all(abs(rates(u,v)[2]-(rates(u,v)[0]+rates(u,v)[1])/2)<1e-12 for u,v in points)
assert all(-1<u<1 and -1<v<1 for u,v in points)
# Determinant of the first two rows of basis [u v] = 1: two independent modes.
assert 1*1-0*0==1
print(json.dumps({'svg':str(a.output),'states':len(points),'basis_rank':2,'plane_relation':'r3=(r1+r2)/2','scientific_status':'synthetic illustration, no experimental measurements'},indent=2))
