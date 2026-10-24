from pathlib import Path
from html import escape
out=Path(__file__).parent
svg=['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1160" width="1200" height="1160" role="img" aria-labelledby="title desc">
<title id="title">From a signal to a changed connection</title>
<desc id="desc">An original grayscale process schematic: integration and spikes in a cortical neuron; glutamate release, AMPA current and NMDA magnesium blockade at a chemical synapse; and a recurrent excitatory circuit with inhibitory feedback. Not to scale.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9 Z" fill="#222"/></marker><marker id="bar" viewBox="0 0 10 16" refX="6" refY="8" markerWidth="10" markerHeight="16" orient="auto"><path d="M 6 1 L 6 15" stroke="#222" stroke-width="2"/></marker></defs>
<style>text{font-family:Arial,Helvetica,sans-serif;fill:#111;font-size:25px} .title{font-weight:700;font-size:30px}.small{font-size:23px}.tiny{font-size:21px}.line{stroke:#222;stroke-width:3;fill:none;stroke-linecap:round;stroke-linejoin:round}.fine{stroke:#555;stroke-width:2;fill:none}.panel{fill:#fafafa;stroke:#777;stroke-width:1.4}</style>
<rect width="1200" height="1160" fill="white"/>
''']
def add(t): svg.append(t)
def txt(x,y,s,cls='',anchor=None):
    att=f' class="{cls}"' if cls else ''
    if anchor:att+=f' text-anchor="{anchor}"'
    add(f'<text x="{x}" y="{y}"{att}>{escape(s)}</text>')
def path(d,arrow=False,bar=False,cls='line'):
    end=' marker-end="url(#arrow)"' if arrow else (' marker-end="url(#bar)"' if bar else '')
    add(f'<path class="{cls}" d="{d}"{end}/>')
def circle(x,y,r,fill='white',stroke='#222'):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
for y,h in [(15,285),(320,490),(830,315)]:
    add(f'<rect class="panel" x="15" y="{y}" width="1170" height="{h}" rx="10"/>')
txt(40,58,'A   Integrate → fire → transmit','title')
# branching neuron
path('M 330 170 L 250 122 L 210 90 M 250 122 L 178 132 M 330 170 L 242 185 L 185 173 M 242 185 L 200 229 M 330 170 L 285 225 L 260 250')
circle(330,170,39,'#e0e0e0'); circle(330,170,12,'white')
path('M 370 170 L 905 170',True)
for x in [490,590,690,790]:
    add(f'<rect x="{x}" y="155" width="75" height="30" rx="14" fill="#d8d8d8" stroke="#555" stroke-width="2"/>')
path('M 906 170 L 965 116 M 906 170 L 982 174 M 906 170 L 965 230')
for x,y in [(965,116),(982,174),(965,230)]:circle(x,y,9,'#666')
txt(40,115,'Excitation (+)')
path('M 165 112 L 216 132',True)
txt(40,210,'Inhibition (−)')
path('M 175 205 L 232 184',False,True)
txt(290,105,'Cell body')
txt(520,123,'Axon: spike propagation')
txt(1000,168,'Chemical')
txt(1000,198,'synapses')
path('M 423 149 L 423 106',False,False,'fine')
txt(402,92,'Threshold','small')
txt(318,273,'Inputs vary; spikes signal through timing, rate and population activity.','small')
# B panel
txt(40,363,'B   A glutamatergic synapse: transmission and coincidence','title')
# membrane outline presyn terminal
add('<path d="M 75 410 L 75 508 Q 75 541 110 541 L 490 541 Q 525 541 525 508 L 525 410" fill="#eee" stroke="#333" stroke-width="3"/>')
txt(100,432,'Sending axon terminal','small')
# vesicles and transmitter
for x,y in [(180,472),(270,481),(360,474)]:
    circle(x,y,19)
    for dx,dy in [(-5,-4),(6,-2),(0,7)]:circle(x+dx,y+dy,2,'#222')
path('M 445 445 L 445 500',True)
txt(415,421,'Ca²⁺','small')
txt(548,481,'Spike → Ca²⁺ entry','small')
txt(548,515,'→ vesicle release','small')
for x,y in [(190,562),(249,569),(303,556),(351,580),(404,565),(219,587)]:circle(x,y,4,'#222')
txt(80,577,'Glutamate','tiny')
# postsyn membrane two lines interrupted around channels
path('M 75 616 L 200 616 M 240 616 L 365 616 M 405 616 L 525 616')
path('M 75 640 L 200 640 M 240 640 L 365 640 M 405 640 L 525 640')
for x in [200,365]:
    add(f'<path d="M {x} 603 L {x} 651 M {x+40} 603 L {x+40} 651" class="line"/>')
txt(175,684,'AMPA','small')
txt(347,684,'NMDA','small')
path('M 220 596 L 220 655',True)
circle(385,627,13,'#bbb')
txt(430,601,'Mg²⁺ block','small')
path('M 443 607 L 402 623',False,False,'fine')
txt(90,728,'Receiving dendrite','small')
txt(90,766,'AMPA current can help depolarize it.','small')
# right conditions
add('<rect x="628" y="556" width="518" height="224" rx="8" fill="white" stroke="#777" stroke-width="1.5"/>')
txt(650,592,'NMDA current needs both:','small')
txt(650,630,'• Glutamate + co-agonist binding','small')
txt(650,665,'• Depolarization easing Mg²⁺ block','small')
txt(650,707,'Ca²⁺ entry → biochemical signaling','small')
txt(650,746,'→ synaptic strength can change','small')
# C recurrent circuit
txt(40,872,'C   Activity returns through the circuit','title')
for x,y,label,fill in [(160,962,'E₁','white'),(465,962,'E₂','white'),(315,1090,'I','#d0d0d0')]:
    circle(x,y,31,fill);txt(x,y+9,label,'',anchor='middle')
path('M 190 949 C 265 909 355 909 435 949',True)
path('M 435 978 C 355 1018 265 1018 190 978',True)
path('M 444 989 L 340 1070',True)
path('M 288 1075 L 180 990',False,True)
path('M 62 962 L 125 962',True)
path('M 499 962 L 566 962',True)
txt(626,928,'E: excitatory cell     I: inhibitory cell','small')
path('M 630 971 L 692 971',True); txt(714,979,'Excitatory influence','small')
path('M 630 1017 L 692 1017',False,True);txt(714,1025,'Inhibitory influence','small')
txt(626,1073,'Recurrence provides feedback; inhibition','small')
txt(626,1110,'helps constrain and shape the activity.','small')
add('</svg>')
(out/'neuron-synapse-circuit.svg').write_text('\n'.join(svg))
print(out/'neuron-synapse-circuit.svg')
