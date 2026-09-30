#!/usr/bin/env python3
"""Generate the complete Quarto representation from canonical POMA Markdown."""
from pathlib import Path
from datetime import datetime,timezone
from typing import Callable
import hashlib,json,re,shutil
P=Path(__file__).resolve().parent.parent; R=P.parent; M=R/'manuscripts'; C=P/'content'; MF=R/'work/manuscript-manifest.json'
MARK='<!-- Generated from canonical manuscripts; do not edit here. -->'
VD={'I':'volume-1','II':'volume-2','III':'volume-3'}; VN={'I':1,'II':2,'III':3}; VG={'I':'Φ','II':'Δ','III':'Θ'}; G={'phi','delta','theta'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gen(*b,yaml=None):
 x=[]
 if yaml:x.append(f'---\n{yaml.strip()}\n---')
 x.extend([MARK,*[z.strip() for z in b if z.strip()]])
 return '\n\n'.join(x)+'\n'
def nb(lines):return [i for i,x in enumerate(lines) if x.strip()]
def roman(n):
 vals=((1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I'));out=[]
 for v,g in vals:
  while n>=v:out.append(g);n-=v
 return ''.join(out)
def chapter_id(u):
 """Return the current publication number, preserving symbolic chapter IDs."""
 return str(u.get('current_chapter_number') or u.get('original_chapter_id') or '')
def front(t,u):return gen('# Title Page {.unnumbered .visually-hidden}',t)
def index(t,u):return gen('# Contents {.unnumbered}',re.sub(r'(?m)^# ','## ',t))
def intro(t,u):
 l=t.splitlines();n=nb(l)
 if len(n)<3 or not l[n[0]].lstrip().startswith('!') or l[n[1]].strip().upper()!='INTRODUCTION':raise ValueError('Introduction opening not recognized')
 a,b,c=n[:3];op='\n\n'.join(['::: {.chapter-opening}',l[a].strip(),'[Introduction]{.smallcaps}',':::'])
 return gen(op,f'# {l[c].strip()} {{.unnumbered}}','\n'.join(l[c+1:]))
def prologue(t,u):
 l=t.splitlines()
 for i,x in enumerate(l):
  if x.lstrip().startswith('!'):l[i]=f'::: {{.chapter-opening}}\n\n{x.strip()}\n\n:::'
 return gen('# Prologue {.unnumbered}','\n'.join(l))
def part(t,u):return gen(f'# Part {VN[u["volume"]]} {{.unnumbered}}',t)
def discipline(x):
 s=x.strip()
 if s.startswith(('>','#','-','!')):return False
 q=s.strip('*').strip()
 return bool(q) and ((s.startswith('*') and s.endswith('*')) or (len(q)<80 and q==q.upper()))
def labelled(t,u):
 l=t.splitlines();n=nb(l)
 if len(n)<4:raise ValueError(f'{u["unit_id"]} opening incomplete')
 a,b,c,d=n[:4];label=l[b].strip();title=l[c].strip()
 if not l[a].lstrip().startswith('!') or not title.startswith('# '):raise ValueError(f'{u["unit_id"]} opening not recognized')
 title=title[2:].strip();sub=l[d].strip();start=d+1;second=[sub]
 if len(n)>4 and discipline(l[n[4]]):
  e=n[4];second.append(f'*[{l[e].strip().strip("*").strip().title()}]{{.smallcaps}}*');start=e+1
 op='\n\n'.join(['::: {.chapter-opening}',l[a].strip(),f'[{label.capitalize()}]{{.smallcaps}}',':::'])
 sec='\n\n'.join(['::: {.chapter-opening}',*second,':::']);cid=chapter_id(u)
 if u['kind']=='chapter' and cid.isdigit():heading=f'# {int(cid)} {title} {{.unnumbered}}';y=None
 else:heading=f'# {title} {{.unnumbered}}';y=None
 return gen(op,heading,sec,'\n'.join(l[start:]),yaml=y)
def opened(t,u):
 cid=chapter_id(u);symbol=VG[u['volume']] if cid in G else roman(int(cid))
 return gen(f'# Open {symbol} {{.unnumbered}}','::: {.book-open}',t,':::')
def named(t,u):
 l=t.splitlines();n=nb(l)
 if len(n)<3 or not l[n[0]].lstrip().startswith('!'):raise ValueError(f'{u["unit_id"]} opening not recognized')
 a,b,c=n[:3];op='\n\n'.join(['::: {.chapter-opening}',l[a].strip(),f'[{l[b].strip().title()}]{{.smallcaps}}',':::'])
 return gen(op,f'# {l[c].strip()} {{.unnumbered}}','\n'.join(l[c+1:]))
def glossary(t,u):
 l=t.splitlines();n=nb(l);start=n[0]+1 if n and 'Glossary' in l[n[0]] else 0
 return gen('# Glossary of Key Concepts in Our Work {.unnumbered}','\n'.join(l[start:]))
A={'front-matter':front,'index':index,'introduction':intro,'prologue':prologue,'part-opening':part,'cold-open':opened,'chapter':labelled,'interlude':labelled,'coda':named,'overture':named,'epilogue':named,'glossary':glossary}
def out(u):
 k=u['kind']
 if k=='front-matter':return Path('front-matter/front-matter.qmd')
 if k=='index':return Path('front-matter/content-summary.qmd')
 if k=='introduction':return Path('front-matter/introduction.qmd')
 if k=='epilogue':return Path('back-matter/epilogue.qmd')
 if k=='glossary':return Path('back-matter/glossary.qmd')
 v=VD[u['volume']];num=VN[u['volume']]
 if k=='prologue':name='prologue.qmd'
 elif k=='part-opening':name=f'part-{num}.qmd'
 elif k=='overture':name=f'overture-{num}.qmd'
 elif k=='coda':name=f'coda-{num}.qmd'
 else:
  cid=chapter_id(u);s='00' if cid in G else f'{int(cid):02d}';prefix={'cold-open':'open','chapter':'chapter','interlude':'interlude'}[k];name=f'{prefix}-{s}.qmd'
 return Path(v)/name
def main():
 m=json.loads(MF.read_text());units=[*map(dict,m['documents']),*map(dict,m.get('supplemental_canonical_units',[]))]
 if len(units)!=121:raise SystemExit(f'Expected 121 units, found {len(units)}')
 if C.exists():shutil.rmtree(C)
 C.mkdir();records=[]
 for u in units:
  src=Path(u['active_source']['path']);dst=C/out(u);dst.parent.mkdir(parents=True,exist_ok=True);dst.write_text(A[u['kind']](src.read_text(),u))
  records.append({'unit_id':u['unit_id'],'kind':u['kind'],'original_chapter_id':u.get('original_chapter_id'),'current_chapter_number':u.get('current_chapter_number'),'source':str(src.relative_to(R)),'source_sha256':sha(src),'output':str(dst.relative_to(P)),'output_sha256':sha(dst)})
 for rel in ['front-matter/assets','volume-1/assets','volume-2/assets','volume-3/assets','back-matter/assets','assets/shared']:
  src=M/rel
  if src.is_dir():shutil.copytree(src,C/rel,dirs_exist_ok=True)
 missing=[]
 for q in C.rglob('*.qmd'):
  for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',q.read_text()):
   if not (q.parent/ref.split()[0]).resolve().is_file():missing.append(f'{q.relative_to(P)} -> {ref}')
 if missing:raise SystemExit('Broken images:\n'+'\n'.join(missing))
 data={'schema_version':3,'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'Complete POMA canonical manuscript','unit_count':len(records),'volume_iii_original_identity_order':m['volume_iii_orders_by_original_chapter_id']['final_order'],'volume_iii_current_reading_order':m['volume_iii_renumbering']['current_reading_order'],'records':records,'broken_image_references':0}
 (P/'content-manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print(f'Generated all {len(records)} canonical manuscript units for Quarto.')
if __name__=='__main__':main()
