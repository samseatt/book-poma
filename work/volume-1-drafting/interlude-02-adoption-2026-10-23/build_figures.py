"""Original POMA grayscale SVG diagrams, made without external artwork.
Run: python3 build_figures.py --output OUTPUT_DIRECTORY
PNG previews can be made with the bundled sharp module (not manuscript assets).
"""
from pathlib import Path
import argparse,html
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).parent/'figures');args=p.parse_args();out=args.output;out.mkdir(parents=True,exist_ok=True)
class Rectangle:
 def __init__(self,xy,w,h,fc='white',ec='black',lw=1):self.xy,self.w,self.h,self.fc,self.ec,self.lw=xy,w,h,fc,ec,lw
class Canvas:
 def __init__(self,size):
  self.w=1000;self.h=1000*size[1]/size[0];self.items=[];self.sf=1000/(size[0]*72)
 def xy(self,x,y):return x*10,(100-y)*self.h/100
 def add_patch(self,r):
  x,y=self.xy(r.xy[0],r.xy[1]+r.h)
  self.items.append(f'<rect x="{x}" y="{y}" width="{r.w*10}" height="{r.h*self.h/100}" fill="{r.fc}" stroke="{r.ec}" stroke-width="{r.lw*self.sf}"/>')
 def plot(self,xs,ys,color='black',lw=1):
  pts=' '.join(f'{self.xy(x,y)[0]},{self.xy(x,y)[1]}' for x,y in zip(xs,ys));self.items.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{lw*self.sf}"/>')
def frame(size):
 a=Canvas(size);return a,a
def txt(ax,x,y,s,size=10,weight='normal',ha='center',va='center'):
 x,y=ax.xy(x,y);lines=s.split('\n');dy=size*ax.sf*1.25;y-=dy*(len(lines)-1)/2
 anchor={'center':'middle','left':'start','right':'end'}[ha]
 for i,l in enumerate(lines):ax.items.append(f'<text x="{x}" y="{y+i*dy}" font-size="{size*ax.sf}" font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="central">{html.escape(l)}</text>')
def box(ax,x,y,w,h,s,fill='white',size=10):
 ax.add_patch(Rectangle((x,y),w,h,fc=fill));txt(ax,x+w/2,y+h/2,s,size)
def arr(ax,a,b):
 x1,y1=ax.xy(*a);x2,y2=ax.xy(*b);ax.items.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black" stroke-width="2" marker-end="url(#arrow)"/>')
def save(fig,name):
 hdr=f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{fig.h:.3f}" viewBox="0 0 1000 {fig.h:.3f}" font-family="Arial, Helvetica, sans-serif"><title>{name.replace("-"," ")}</title><desc>Original POMA teaching illustration. See manuscript caption and source notes for scope.</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="black"/></marker></defs><rect width="100%" height="100%" fill="white"/>'
 (out/(name+'.svg')).write_text(hdr+'\n'.join(fig.items)+'</svg>\n')
fig,ax=frame((6.6,5.8))
# Compartment panels; paths are schematic, not molecular sizes.
ax.add_patch(Rectangle((2,40),44,55,fc='#f3f3f3',ec='black',lw=.8));ax.add_patch(Rectangle((54,40),44,55,fc='white',ec='black',lw=.8))
txt(ax,24,91,'NUCLEUS',10,'bold');txt(ax,76,91,'CYTOPLASM',10,'bold')
box(ax,10,77,28,9,'DNA gene')
arr(ax,(24,77),(24,65));txt(ax,26,71,'transcription',9,ha='left')
box(ax,10,56,28,9,'pre-mRNA')
arr(ax,(24,56),(24,48));txt(ax,26,52,'RNA processing',9,ha='left')
box(ax,8,41.5,32,7,'mature mRNA',size=10)
txt(ax,5,34,'Processing: remove introns, join exons; add a cap and usually a poly-A tail.',9,ha='left')
arr(ax,(40,45),(63,45));txt(ax,50,48.5,'export',8)
box(ax,64,41.5,26,7,'ribosome',fill='#ededed')
arr(ax,(76,50),(76,65));txt(ax,77.5,57,'translation',9,ha='left')
box(ax,62,66,30,9,'amino-acid chain',size=9.5)
txt(ax,76,82,'charged tRNAs deliver\namino acids',9)
ax.plot([93,93],[80,52],color='black',lw=1)
arr(ax,(93,52),(88,48.5))
# Coding example with explicit chemical direction and stop.
ax.plot([2,98],[30,30],color='black',lw=.7)
txt(ax,50,26,'A SMALL CODING EXAMPLE',10,'bold')
xs=[16,39,62,85];codons=['AUG','CCU','GAA','UAA'];products=['Met','Pro','Glu','STOP']
txt(ax,4,18,"5′",10);txt(ax,96,18,"3′",10)
for x,co,pr in zip(xs,codons,products):
 box(ax,x-8,14,16,8,co,fill='#eeeeee',size=12)
 arr(ax,(x,14),(x,9));txt(ax,x,6.8,pr,11,'bold' if pr=='STOP' else 'normal')
ax.plot([22,33],[6.8,6.8],color='black',lw=1);ax.plot([45,56],[6.8,6.8],color='black',lw=1)
txt(ax,50,1.4,'Standard code; teaching fragment, not a functional protein.',8.5)
save(fig,'gene-expression')
fig,ax=frame((6.6,4.8))
txt(ax,50,95,'ONE LAB RECORD, TWO REPRESENTATIONS',11,'bold')
txt(ax,50,87,'RELATIONAL TABLES',10,'bold')
def table(x,y,w,title,heads,vals):
 txt(ax,x+w/2,y+18,title,10,'bold')
 ax.add_patch(Rectangle((x,y),w,14,fc='white',ec='black',lw=1));ax.add_patch(Rectangle((x,y+7),w,7,fc='#ededed',ec='black',lw=.7))
 n=len(heads)
 for i,(h,v) in enumerate(zip(heads,vals)):
  if i: ax.plot([x+i*w/n,x+i*w/n],[y,y+14],color='black',lw=.6)
  txt(ax,x+(i+.5)*w/n,y+10.5,h,8.5);txt(ax,x+(i+.5)*w/n,y+3.5,v,10)
table(2,61,22,'Donor',['donor_id'],['D4'])
table(31,61,46,'Sample',['sample_id','donor_id','run_id'],['S17','D4','R2'])
table(84,61,14,'Run',['run_id'],['R2'])
# FK relation connectors routed below without touching table text.
ax.plot([54,54,13,13],[61,55,55,61],color='black',lw=1)
ax.plot([69.3,69.3,91,91],[61,51,51,61],color='black',lw=1)
txt(ax,50,45,'Keys retain identity and link the records.',9)
ax.plot([2,98],[39,39],color='black',lw=.7)
txt(ax,50,34,'PROPERTY GRAPH',10,'bold')
box(ax,2,16,22,12,'Donor\nD4',fill='#ededed');box(ax,39,16,22,12,'Sample\nS17',fill='#ededed');box(ax,76,16,22,12,'Run\nR2',fill='#ededed')
arr(ax,(24,22),(39,22));txt(ax,31.5,29,'donated',8.5)
arr(ax,(61,22),(76,22));txt(ax,68.5,29,'sequenced in',8.5)
txt(ax,50,8,'Same facts; joins or traversals can recover the path.',9)
txt(ax,50,2.5,'Simplified example: one run recorded per sample.',8.5)
save(fig,'data-models')
print('Rendered two original diagrams:',out)
