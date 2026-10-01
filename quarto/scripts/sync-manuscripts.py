#!/usr/bin/env python3
"""Generate the complete Quarto representation from canonical POMA Markdown."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,shutil,tempfile
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
class AnnotationError(ValueError):pass
TOKENS=(('escaped-open',r'\[\['),('escaped-close',r'\]\]'),('open','[['),('close',']]'))
def location(text,pos):
 line=text.count('\n',0,pos)+1;last=text.rfind('\n',0,pos)
 return line,pos-last
def annotation_error(source,text,pos,message):
 line,col=location(text,pos);raise AnnotationError(f'{source}:{line}:{col}: {message}')
def annotation_spans(text,source):
 """Return complete annotation spans, rejecting malformed or nested delimiters."""
 spans=[];i=0
 while i<len(text):
  token=next(((name,value) for name,value in TOKENS if text.startswith(value,i)),None)
  if token is None:i+=1;continue
  name,value=token
  if name.endswith('close'):annotation_error(source,text,i,'unmatched annotation closer')
  expected='escaped-close' if name=='escaped-open' else 'close';start=i;i+=len(value)
  while i<len(text):
   inner=next(((n,v) for n,v in TOKENS if text.startswith(v,i)),None)
   if inner is None:i+=1;continue
   inner_name,inner_value=inner
   if inner_name.endswith('open'):annotation_error(source,text,i,'nested annotation opener')
   if inner_name!=expected:annotation_error(source,text,i,'mismatched annotation closer')
   i+=len(inner_value);spans.append((start,i));break
  else:annotation_error(source,text,start,'unclosed annotation opener')
 return spans
def join_inline(left,right):
 """Join text at an inline omission boundary without broad whitespace changes."""
 lm=re.search(r'[ \t]*$',left);rm=re.match(r'[ \t]*',right)
 ls=lm.start();re_=rm.end();before=left[:ls];after=right[re_:]
 left_space=lm.group();right_space=rm.group();previous=before[-1:] or '';following=after[:1] or ''
 if following=='\n':
  if len(right_space)>=2:separator=right_space
  elif len(left_space)>=2:separator='  '
  else:separator=''
 elif not following:separator=''
 elif not before or previous=='\n':
  separator=left_space if left_space else (right_space if len(right_space)>=4 else '')
 elif following in ',.;:!?)]}…':separator=''
 elif previous and previous in '([{—–/':separator=''
 elif left_space or right_space:separator=' '
 elif previous and following and previous.isalnum() and following.isalnum():separator=' '
 else:separator=''
 return before+separator+after
def join_standalone(left,right):
 """Remove an annotation-only line while retaining one paragraph boundary."""
 trailing=re.search(r'(?:[ \t]*\n)+$',left);leading=re.match(r'(?:[ \t]*\n)+',right)
 if trailing and leading:return left[:trailing.start()]+'\n\n'+right[leading.end():]
 if trailing and not right:return left[:trailing.start()]+'\n'
 if leading and not left:return right[leading.end():]
 return left+right
def omit_annotations(text,source):
 spans=annotation_spans(text,source)
 for start,end in reversed(spans):
  line_start=text.rfind('\n',0,start)+1;line_end=text.find('\n',end)
  if line_end<0:line_end=len(text)
  prefix=text[line_start:start];suffix=text[end:line_end]
  structural_only=bool(re.fullmatch(r'[ \t]*(?:[-+*]|\d+[.)]|>|#{1,6})[ \t]*',prefix))
  if (not prefix.strip() or structural_only) and not suffix.strip():
   remove_end=line_end+1 if line_end<len(text) else line_end
   text=join_standalone(text[:line_start],text[remove_end:])
  else:text=join_inline(text[:start],text[end:])
 if annotation_spans(text,source):raise AssertionError('annotation removal left a complete block')
 return text,len(spans)
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
def sync(manifest_path=MF,content_dir=C,manifest_output=P/'content-manifest.json',expected_count=121,asset_root=M):
 m=json.loads(Path(manifest_path).read_text());units=[*map(dict,m['documents']),*map(dict,m.get('supplemental_canonical_units',[]))]
 if expected_count is not None and len(units)!=expected_count:raise SystemExit(f'Expected {expected_count} units, found {len(units)}')
 # Preflight every source before creating, deleting, or writing generated output.
 prepared=[];omissions=[]
 for u in units:
  src=Path(u['active_source']['path']);cleaned,count=omit_annotations(src.read_text(),src)
  prepared.append((u,src,cleaned,count))
  if count:omissions.append({'source':str(src.relative_to(R)) if src.is_relative_to(R) else str(src),'count':count})
 temp_root=Path(tempfile.mkdtemp(prefix='.sync-manuscripts-',dir=P));staged=temp_root/'content';staged.mkdir();records=[]
 try:
  for u,src,cleaned,count in prepared:
   dst=staged/out(u);dst.parent.mkdir(parents=True,exist_ok=True);dst.write_text(A[u['kind']](cleaned,u))
   records.append({'unit_id':u['unit_id'],'kind':u['kind'],'original_chapter_id':u.get('original_chapter_id'),'current_chapter_number':u.get('current_chapter_number'),'source':str(src.relative_to(R)) if src.is_relative_to(R) else str(src),'source_sha256':sha(src),'annotation_omission_count':count,'output':str((content_dir/out(u)).relative_to(P)) if content_dir.is_relative_to(P) else str(content_dir/out(u)),'output_sha256':sha(dst)})
  for rel in ['front-matter/assets','volume-1/assets','volume-2/assets','volume-3/assets','back-matter/assets','assets/shared']:
   src=asset_root/rel
   if src.is_dir():shutil.copytree(src,staged/rel,dirs_exist_ok=True)
  missing=[]
  for q in staged.rglob('*.qmd'):
   generated=q.read_text()
   remaining=annotation_spans(generated,q)
   if remaining:raise SystemExit(f'Annotation delimiter remained in generated output: {q.relative_to(staged)}')
   for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',generated):
    if not (q.parent/ref.split()[0]).resolve().is_file():missing.append(f'{q.relative_to(staged)} -> {ref}')
  if missing:raise SystemExit('Broken images:\n'+'\n'.join(missing))
  data={'schema_version':4,'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'Complete POMA canonical manuscript','unit_count':len(records),'annotation_omission_count':sum(x['count'] for x in omissions),'annotation_omissions':omissions,'volume_iii_original_identity_order':m.get('volume_iii_orders_by_original_chapter_id',{}).get('final_order',[]),'volume_iii_current_reading_order':m.get('volume_iii_renumbering',{}).get('current_reading_order',[]),'records':records,'broken_image_references':0}
  staged_manifest=temp_root/'content-manifest.json';staged_manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
  backup=temp_root/'previous-content'
  try:
   if content_dir.exists():content_dir.rename(backup)
   staged.rename(content_dir)
  except Exception:
   if backup.exists() and not content_dir.exists():backup.rename(content_dir)
   raise
  if backup.exists():shutil.rmtree(backup)
  os.replace(staged_manifest,manifest_output)
 finally:shutil.rmtree(temp_root,ignore_errors=True)
 print(f'Generated all {len(records)} canonical manuscript units for Quarto; omitted {sum(x["count"] for x in omissions)} annotation blocks from derived content.')
 return data
def main():
 sync()
if __name__=='__main__':main()
