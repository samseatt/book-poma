"""Generate the Chapter 1 scalar-potential diagram as an editable grayscale SVG.
The dimensionless potential is V(r)=(r*r-1)**2-1: mu^2=2, lambda=1.
No spatial coordinates or literal Standard Model Higgs manifold are plotted.
Run with an optional output path; uses Python's standard library only.
"""
from pathlib import Path
import math,sys
out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[3] / 'manuscripts/volume-1/assets/01-chapter/symmetry-breaking.svg'
s=['''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="504" viewBox="0 0 1000 560" role="img" aria-labelledby="title desc">
<title id="title">One symmetric potential, two kinds of disturbance</title>
<desc id="desc">For a two-component scalar field, a circle of minima surrounds an unstable central maximum. A chosen vacuum lies on the circle. A radial displacement raises potential energy; a uniform rotation along the circle does not. A cross-section shows the same central hill and two valley intersections. Spatial gradients of orientation still cost energy.</desc>
<rect width="1000" height="560" fill="white"/>
<style>text{font-family:Arial,Helvetica,sans-serif;fill:#161616} .title{font-size:26px;font-weight:700} .head{font-size:22px;font-weight:700} .label{font-size:19px} .small{font-size:17px;fill:#444} .axis{stroke:#777;stroke-width:1.4;fill:none} .curve{stroke:#171717;stroke-width:3;fill:none} .guide{stroke:#aaa;stroke-width:1.2;stroke-dasharray:5 5;fill:none}</style>
<defs><marker id="arr" viewBox="0 0 10 10" markerWidth="7" markerHeight="7" refX="8" refY="5" orient="auto"><path d="M1 1 L9 5 L1 9" fill="none" stroke="#222" stroke-width="1.5"/></marker></defs>
<text x="500" y="34" text-anchor="middle" class="title">One symmetric potential, two kinds of disturbance</text>
<text x="40" y="81" class="head">A · Field values, viewed from above</text>
<text x="552" y="81" class="head">B · A slice through the same potential</text>
<!-- Contours are circles in field-value space, not a spatial landscape. -->
<circle cx="240" cy="270" r="164" fill="#f8f8f8" stroke="#bbb"/>
<circle cx="240" cy="270" r="142" fill="white" stroke="#aaa"/>
<circle cx="240" cy="270" r="116" fill="#e8e8e8" stroke="#222" stroke-width="3"/>
<circle cx="240" cy="270" r="87" fill="#f3f3f3" stroke="#aaa"/>
<circle cx="240" cy="270" r="51" fill="white" stroke="#bbb"/>
<path d="M58 270 H434 M240 448 V102" class="axis"/>
<text x="418" y="295" class="label">φ₁</text><text x="249" y="113" class="label">φ₂</text>
<circle cx="240" cy="270" r="5" fill="#777"/>
<text x="170" y="247" class="small">unstable center</text>
<circle cx="356" cy="270" r="6" fill="#111"/>
<rect x="297" y="313" width="177" height="27" fill="white"/><text x="302" y="333" class="label">chosen vacuum</text>
<path d="M366 270 H412" stroke="#222" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
<text x="366" y="244" class="small">radial</text>
<path d="M350.5 235 A116 116 0 0 0 298 169.5" stroke="#222" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
<text x="338" y="169" class="small">along valley</text>
<text x="91" y="454" class="small">ring of equally low field values</text>
''']
# B: V(q)=-2q^2+q^4, with q from -1.55 to 1.55.
x0,x1=567,951;y0,y1=410,136
xmin,xmax=-1.55,1.55;vmin,vmax=-1.24,1.25
def point(q,v):return (x0+(q-xmin)/(xmax-xmin)*(x1-x0), y0-(v-vmin)/(vmax-vmin)*(y0-y1))
def line(q1,v1,q2,v2,cl='guide'):
 a,b=point(q1,v1),point(q2,v2);s.append(f'<path d="M{a[0]:.2f} {a[1]:.2f} L{b[0]:.2f} {b[1]:.2f}" class="{cl}"/>')
line(xmin,0,xmax,0,'axis');line(0,vmin,0,vmax,'axis');line(xmin,-1,xmax,-1)
pts=[point(xmin+(xmax-xmin)*i/320, (xmin+(xmax-xmin)*i/320)**4-2*(xmin+(xmax-xmin)*i/320)**2) for i in range(321)]
s.append('<path class="curve" d="'+' '.join(('M' if i==0 else 'L')+f'{x:.3f} {y:.3f}' for i,(x,y) in enumerate(pts))+'"/>')
for q,fill in [(-1,'white'),(0,'#777'),(1,'#111')]:
 x,y=point(q,q**4-2*q*q);s.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{fill}" stroke="#222" stroke-width="1.5"/>')
s.append('''<text x="774" y="133" class="label">V</text>
<text x="943" y="293" class="label">φ₁</text>
<text x="780" y="252" class="small">central hill</text>
<text x="759" y="433" text-anchor="middle" class="small">two intersections with the same circular valley</text>
<text x="759" y="113" text-anchor="middle" class="small">dimensionless illustration: V = −2r² + r⁴</text>
<rect x="39" y="464" width="922" height="70" rx="5" fill="#f2f2f2"/>
<text x="59" y="490" class="label">Radial motion climbs. A uniform turn around the valley does not.</text>
<text x="59" y="517" class="small">Different orientations at neighboring places still cost gradient energy.</text>
</svg>''')
out.parent.mkdir(parents=True,exist_ok=True);out.write_text('\n'.join(s)+'\n');print(out)
assert abs((1**4-2*1**2)-(-1))<1e-12
assert abs(4*1**3-4*1)<1e-12
# Companion diagram: normalized free-particle states on a ring of circumference L.
# psi_n=exp(2*pi*i*n*x/L)/sqrt(L); p=1/L; E_n=(2*pi*hbar*n/L)^2/(2m).
p=out.with_name('phase-and-probability.svg')
t=['''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="468" viewBox="0 0 1000 520" role="img" aria-labelledby="title desc">
<title id="title">Same position probabilities, different energies</title>
<desc id="desc">A free particle on a ring can have a wavefunction whose phase winds once or twice around the ring. Real and imaginary components are plotted as solid and dashed curves. Both states have the same constant position probability density, but the second has four times the kinetic energy.</desc>
<rect width="1000" height="520" fill="white"/>
<style>text{font-family:Arial,Helvetica,sans-serif;fill:#171717}.title{font-size:26px;font-weight:700}.head{font-size:22px;font-weight:700}.label{font-size:19px}.small{font-size:17px;fill:#444}.axis{stroke:#999;stroke-width:1.3;fill:none}.real{stroke:#111;stroke-width:2.5;fill:none}.imag{stroke:#777;stroke-width:2.5;stroke-dasharray:7 5;fill:none}</style>
<text x="500" y="34" text-anchor="middle" class="title">Same position probabilities. Different energies.</text>
<text x="60" y="75" class="small">Free particle on a ring; position x runs from 0 to L and returns to its start.</text>
<path d="M300 101 H340" class="real"/><text x="349" y="107" class="small">real part</text>
<path d="M530 101 H570" class="imag"/><text x="579" y="107" class="small">imaginary part</text>
''']
for left,n in [(75,1),(565,2)]:
 right=left+350;mid=(left+right)/2;top=175;cy=235;amp=51
 t.append(f'<text x="{mid}" y="151" text-anchor="middle" class="head">Phase winds {"once" if n==1 else "twice"}</text>')
 t.append(f'<path d="M{left} {cy} H{right} M{left} {cy-amp-7} V{cy+amp+7}" class="axis"/>')
 for f,cl in [(math.cos,'real'),(math.sin,'imag')]:
  pts=[(left+350*i/240,cy-amp*f(2*math.pi*n*i/240)) for i in range(241)]
  t.append('<path class="'+cl+'" d="'+' '.join(('M' if i==0 else 'L')+f'{x:.2f} {y:.2f}' for i,(x,y) in enumerate(pts))+'"/>')
 t.append(f'<text x="{left}" y="312" text-anchor="middle" class="small">0</text><text x="{right}" y="312" text-anchor="middle" class="small">L</text><text x="{mid}" y="312" text-anchor="middle" class="small">position around ring</text>')
 t.append(f'<path d="M{left} 388 H{right} M{left} 350 V388" class="axis"/><path d="M{left} 357 H{right}" class="real"/>')
 t.append(f'<text x="{mid}" y="344" text-anchor="middle" class="label">same probability density: 1/L</text><text x="{mid}" y="416" text-anchor="middle" class="head">kinetic energy: {"E₁" if n==1 else "4E₁"}</text>')
t.append('''<rect x="44" y="447" width="912" height="55" rx="5" fill="#f2f2f2"/>
<text x="500" y="480" text-anchor="middle" class="label">Position probability loses the phase information that kinetic energy needs.</text>
</svg>''')
p.write_text('\n'.join(t)+'\n');print(p)
# Checks: equal density and energy ratio under periodic free-particle boundary conditions.
for j in range(101):
 for n in (1,2):
  z=2*math.pi*n*j/100
  assert abs(math.cos(z)**2+math.sin(z)**2-1)<1e-12
assert (2/1)**2==4
