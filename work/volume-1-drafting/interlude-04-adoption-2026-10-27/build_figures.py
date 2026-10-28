"""Original grayscale process figures. Standard-library SVG; no source artwork."""
from pathlib import Path
from html import escape
P=Path(__file__).parent
OUT=P/'figures';OUT.mkdir(exist_ok=True)
class Figure:
 def __init__(self,h,title,desc):
  self.p=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{h}" viewBox="0 0 1040 {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 1 L 9 5 L 0 9 Z" fill="#333"/></marker></defs>
<style>text{{font-family:Arial,Helvetica,sans-serif;font-size:25px;fill:#171717}}.title{{font-size:31px;font-weight:bold}}.head{{font-size:26px;font-weight:bold}}.small{{font-size:23px}}.mono{{font-family:monospace;font-size:24px}}</style><rect width="1040" height="{h}" fill="white"/>''']
 def text(self,x,y,t,cls='',anchor='start'):
  self.p.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(t)}</text>')
 def box(self,x,y,w,h,fill='#f4f4f4',dash=False):
  self.p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="#666" stroke-width="1.7"'+(' stroke-dasharray="7 5"' if dash else '')+'/>')
 def line(self,d,arrow=True,dash=False):
  self.p.append(f'<path d="{d}" fill="none" stroke="#333" stroke-width="2.4"'+(' marker-end="url(#a)"' if arrow else '')+(' stroke-dasharray="7 5"' if dash else '')+'/>')
 def save(self,name):
  (OUT/name).write_text('\n'.join(self.p+['</svg>']))

f=Figure(820,'A token can protect work without guaranteeing progress','Two threads share a semaphore initialized to one. A takes the token and B waits. A signals and finishes. B proceeds, but an extra wait blocks forever because nobody can signal. The example illustrates a failure of progress, not the exact historical assignment.')
f.text(30,45,'A token protects access; ordering must preserve progress.','title')
f.text(30,87,'Semaphore starts with one available token. Time proceeds downward.','small')
f.text(280,140,'THREAD A','head','middle');f.text(755,140,'THREAD B','head','middle')
f.line('M 280 165 L 280 555',False);f.line('M 755 165 L 755 715',False)
def row(x,y,a,b='',fill='#fff',dash=False):
 f.box(x,y,390,82,fill,dash);f.text(x+195,y+33,a,'head','middle')
 if b:f.text(x+195,y+66,b,'small','middle')
row(85,175,'wait() succeeds','A takes the token.')
row(560,285,'wait() blocks','No token is available.','#eee',True)
row(85,385,'signal(), then finish','A releases the token.')
f.line('M 475 426 L 520 426 L 520 500 L 560 500')
f.text(515,395,'wake','small','middle')
row(560,460,'B resumes','B now has the token.')
row(560,610,'Extra wait(): blocked','Nobody remains to signal.','#e0e0e0',True)
f.text(85,565,'A has finished.','small');f.text(85,600,'The scheduler cannot supply','small');f.text(85,633,'the missing signal.','small')
f.line('M 755 692 L 755 728',False,True)
f.text(520,783,'Safety against interference is different from liveness: eventual progress.','small','middle')
f.save('semaphore-progress.svg')

f=Figure(960,'Training updates parameters; serving manages executions','Training loops from batches through forward calculation, loss, gradients and optimizer updates to weights. Validation selects a checkpoint. A separate serving path loads a deployed model and processes requests with fixed parameters and changing activations and cache. Conventional software handles data, checkpoints, scheduling and permissions.')
f.text(30,46,'A   Training: change the parameters','title')
f.box(30,72,980,429,'#fafafa')
for x,t in [(55,'Batch of data'),(365,'Forward pass'),(675,'Loss')]:
 f.box(x,120,275,90,'#fff');f.text(x+137.5,158,t,'head','middle')
f.text(192,190,'inputs + targets','small','middle');f.text(502,190,'activations','small','middle');f.text(812,190,'task error','small','middle')
f.line('M 330 165 L 365 165');f.line('M 640 165 L 675 165')
f.box(365,284,275,92,'#e4e4e4');f.text(502,320,'Weights','head','middle');f.text(502,353,'learned parameters','small','middle')
f.line('M 502 284 L 502 210')
f.box(675,284,275,92,'#fff');f.text(812,320,'Backward pass','head','middle');f.text(812,353,'gradients via chain rule','small','middle')
f.line('M 812 210 L 812 284')
f.line('M 812 376 L 812 434 L 502 434 L 502 376')
f.text(657,471,'Optimizer uses gradients to update weights.','small','middle')
f.text(57,315,'Repeat over batches.','small');f.text(57,353,'Save resumable state.','small')
f.line('M 166 284 L 166 210',True,True)
f.text(30,551,'Validation helps select a checkpoint; deployment is a separate step.','small')
f.line('M 980 501 L 980 585',True,True)
f.text(30,627,'B   Serving: execute with deployed parameters','title')
f.box(30,649,980,226,'#fafafa')
for x,t in [(55,'Request'),(365,'Deployed model'),(675,'Output')]:
 f.box(x,689,275,84,'#fff');f.text(x+137.5,724,t,'head','middle')
f.text(192,754,'prepare / tokenize','small','middle');f.text(502,754,'forward computation','small','middle');f.text(812,754,'tokens or prediction','small','middle')
f.line('M 330 733 L 365 733');f.line('M 640 733 L 675 733')
f.text(520,814,'Weights stay fixed in ordinary inference.','small','middle')
f.text(520,847,'Activations and request state (including an LLM’s KV cache) change.','small','middle')
f.text(520,918,'Conventional software manages data, checkpoints, scheduling and permissions.','small','middle')
f.save('training-serving.svg')
print(OUT)
