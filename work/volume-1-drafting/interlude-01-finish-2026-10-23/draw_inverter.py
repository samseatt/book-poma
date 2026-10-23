#!/usr/bin/env python3
"""Original POMA illustration: CMOS inverter as ideal switches in two settled states.
Usage: python3 draw_inverter.py OUTPUT_DIRECTORY
Pillow is needed only for the high-resolution grayscale PNG; SVG uses the same geometry.
"""
from pathlib import Path
import sys, html
from PIL import Image, ImageDraw, ImageFont
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
W,H,S=600,355,5
im=Image.new('L',(W*S,H*S),255); d=ImageDraw.Draw(im)
fontroot=Path('/System/Library/Fonts/Supplemental')
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="600" height="355" viewBox="0 0 600 355" role="img" aria-labelledby="title desc">','<title id="title">A CMOS NOT gate in its two settled states</title>','<desc id="desc">Left: input zero turns the upper pMOS switch on and lower nMOS switch off; the output connects to the positive supply and becomes one. Right: input one reverses the switches; the output connects to ground and becomes zero. Each input controls both switches. This is a simplified switch model, not a physical layout.</desc>','<rect width="600" height="355" fill="white"/>']
def line(x1,y1,x2,y2,width=1.4,gray=0):
 d.line((x1*S,y1*S,x2*S,y2*S),fill=gray,width=round(width*S))
 svg.append(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="rgb({gray},{gray},{gray})" stroke-width="{width}" stroke-linecap="round"/>')
def circle(x,y,rad=3,filled=False):
 d.ellipse(((x-rad)*S,(y-rad)*S,(x+rad)*S,(y+rad)*S),fill=0 if filled else 255,outline=0,width=round(1.2*S))
 svg.append(f'<circle cx="{x}" cy="{y}" r="{rad}" fill="{"black" if filled else "white"}" stroke="black" stroke-width="1.2"/>')
def txt(x,y,t,size=17,bold=False,anchor='middle'):
 ft=ImageFont.truetype(str(fontroot/('Arial Bold.ttf' if bold else 'Arial.ttf')),size*S)
 d.text((x*S,y*S),t,font=ft,fill=0,anchor={'middle':'mm','start':'lm','end':'rm'}[anchor])
 svg.append(f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" text-anchor="{anchor}" dominant-baseline="central">{html.escape(t)}</text>')
def switch(x,top,bottom,on):
 line(x,bottom,x if on else x+22,top if on else top+6,width=2.7 if on else 1.4)
 circle(x,top);circle(x,bottom)
for k,low in enumerate([True,False]):
 offset=300*k; x=offset+100
 txt(offset+150,22,'INPUT 0 (LOW)' if low else 'INPUT 1 (HIGH)',19,True)
 txt(x,60,'+ supply',16)
 line(x-24,80,x+24,80,width=2)
 line(x,80,x,120,width=2.7 if low else 1.4)
 switch(x,120,155,low)
 line(x,155,x,195,width=2.7 if low else 1.4)
 txt(x+47,126,'pMOS',17,True,'start');txt(x+47,148,'ON' if low else 'OFF',16,False,'start')
 circle(x,195,3.5,True)
 line(x,195,x+95,195,width=2.7)
 txt(x+103,186,'OUT',15,False,'start');txt(x+103,208,'1' if low else '0',24,True,'start')
 line(x,195,x,235,width=1.4 if low else 2.7)
 switch(x,235,270,not low)
 txt(x+47,241,'nMOS',17,True,'start');txt(x+47,263,'OFF' if low else 'ON',16,False,'start')
 line(x,270,x,305,width=1.4 if low else 2.7)
 for yy,ww in [(305,22),(312,14),(319,6)]:line(x-ww/2,yy,x+ww/2,yy,width=1.6)
 txt(x,340,'ground (0 V)',16)
line(300,52,300,342,width=.7,gray=165)
svg.append('</svg>')
(out/'cmos-not-gate.svg').write_text('\n'.join(svg)+'\n')
im.save(out/'cmos-not-gate.png',dpi=(600,600),optimize=True)
im.resize((900,533),Image.Resampling.LANCZOS).save(out/'preview.png')
print('Created 3000 × 1775 grayscale PNG and editable SVG.')
