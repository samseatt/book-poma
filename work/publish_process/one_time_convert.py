# HISTORICAL ONE-TIME MIGRATION TOOL — DO NOT RUN AFTER CANONICALIZATION.
# The author declared manuscripts/ canonical on 2026-09-29. This file is
# retained only to document the conversion process. It must never overwrite
# canonical Markdown from archived DOCX sources.

from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, re, shutil, subprocess, tempfile, zipfile

PANDOC='/Applications/quarto/bin/tools/x86_64/pandoc'
REPO=Path('/Users/samseatt/projects/book-poma')
SOURCE_ROOT=Path('/Users/samseatt/projects/book_poma')
MANIFEST=REPO/'work/manuscript-manifest.json'
LEGACY_ENDS={
 'v3-theta-interlude':'Now we build the trellis.',
 'v3-33-chapter':'And the world, maddening and beloved, receives another chance.',
 'v3-33-interlude':'The plane was waiting.',
}
SOURCE_OVERRIDE={
 'v3-24-interlude':SOURCE_ROOT/"7 24i - The Developer's Dilemma - Building Without Becoming the New Tyrant.docx"
}
SHARED_EXPECTED={
 'chapter-arrow.png':'f732ac23ecdfce5dc1a9070c7858c751cc57e3b1aed335ab3afeddd0550d6cba',
 'interlude-gear.png':'f1a212743fd903dcad58514301579a5e0ef691f3c69ba3dcc34782c3f4a638d3',
 'separator.png':'8af213714d53e11b65285ca7d626219e6d1ccc80276c96c835dc0f3493dc47b3',
}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s): return re.sub(r'\s+',' ',s).strip()
def word_sequence(s):
 # Portable Markdown may reflow table borders and Pandoc may reconstruct smart
 # punctuation differently around nested emphasis. Preserve and compare every
 # Unicode word/number token in order as the loss-detection invariant.
 return re.findall(r'[^\W_]+',s,flags=re.UNICODE)
def plain(path,fmt):
 return subprocess.check_output([PANDOC,str(path),'--from',fmt,'--to','plain','--wrap=none'],text=True)
def vol_dir(v):
 return {'I':'volume-1','II':'volume-2','III':'volume-3',None:'front-matter'}[v]
def output_rel(x):
 if x['unit_id']=='prologue': return Path('volume-1/prologue.md')
 if x['unit_id']=='epilogue': return Path('back-matter/epilogue.md')
 if x.get('volume') is None: return Path('front-matter')/(x['unit_id']+'.md')
 old=Path(x['planned_markdown_path']).name
 return Path(vol_dir(x['volume']))/old
def archive_rel(x,src):
 if x['unit_id']=='epilogue': base='back-matter'
 elif x.get('volume') is None: base='front-matter'
 else: base=vol_dir(x['volume'])
 return Path(base)/src.name
def uppercase_smallcaps(s):
 return re.sub(r'\[([^\]]+)\]\{\.smallcaps\}',lambda m:m.group(1).upper(),s)
def promote_label_title(s,kind):
 if kind not in {'chapter','interlude'}: return s
 lines=s.splitlines()
 label=re.compile(r'^(CHAPTER|INTERLUDE)\s+.+$',re.I)
 idx=next((i for i,v in enumerate(lines) if label.match(v.strip())),None)
 if idx is None: raise RuntimeError(f'No {kind} label')
 j=idx+1
 while j<len(lines) and not lines[j].strip():j+=1
 if j>=len(lines):raise RuntimeError(f'No {kind} title')
 title=lines[j].strip()
 if not title.startswith('# '):
  if title.startswith(('[','!')):raise RuntimeError(f'Ambiguous {kind} title: {title}')
  lines[j]='# '+title
 return '\n'.join(lines)+('\n' if s.endswith('\n') else '')
def trim_legacy(s,end_text):
 pos=s.find(end_text)
 if pos<0: raise RuntimeError(f'Legacy boundary not found: {end_text}')
 end=pos+len(end_text)
 return s[:end].rstrip()+'\n'
def remove_strikeout(s):
 matches=re.findall(r'~~.*?~~',s,flags=re.S)
 s=re.sub(r'~~.*?~~','',s,flags=re.S)
 s=re.sub(r'\n{3,}','\n\n',s)
 return s,len(matches)
def image_matches(s):
 return list(re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)(?:\{[^\n]*\})?',s))
def ext_for(p): return p.suffix.lower() or '.bin'

def main(outroot):
 source_manifest=json.load(open(MANIFEST))
 if source_manifest.get('conversion_transition',{}).get('status')=='complete-canonical':
  raise RuntimeError('Conversion is finalized: manuscripts/ is canonical. This historical one-time tool must not be rerun.')
 units=[dict(x) for x in source_manifest['documents']]
 units.append({
  'unit_id':'glossary','volume':None,'kind':'glossary','original_chapter_id':None,
  'status':'source-docx','active_source':{'format':'docx','path':str(SOURCE_ROOT/'9 Glossary of Key Concepts in Our Work.docx')},
  'provenance_source':str(SOURCE_ROOT/'9 Glossary of Key Concepts in Our Work.docx'),
  'source_sha256_at_inventory':sha(SOURCE_ROOT/'9 Glossary of Key Concepts in Our Work.docx'),
  'planned_markdown_path':'back-matter/glossary.md','design_packet':None
 })
 manuscripts=outroot/'manuscripts'; archive=outroot/'archive/docx-originals'; reports=manuscripts/'_conversion-reports'; shared=manuscripts/'assets/shared'
 for p in (manuscripts,archive,reports,shared):p.mkdir(parents=True,exist_ok=True)
 aggregated=[]; shared_sources={}; now=datetime.now(timezone.utc).isoformat()
 with tempfile.TemporaryDirectory(prefix='poma-convert-work-') as td:
  td=Path(td)
  for number,x in enumerate(units,1):
   uid=x['unit_id'];src=SOURCE_OVERRIDE.get(uid,Path(x['active_source']['path']))
   if not src.exists():raise RuntimeError(f'Missing source {uid}: {src}')
   dest_rel=Path('back-matter/glossary.md') if uid=='glossary' else output_rel(x)
   dest=manuscripts/dest_rel;dest.parent.mkdir(parents=True,exist_ok=True)
   ar=archive/archive_rel(x,src) if uid!='glossary' else archive/'back-matter'/src.name
   ar.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,ar)
   if sha(ar)!=sha(src):raise RuntimeError(f'Archive hash mismatch {uid}')
   wd=td/uid;wd.mkdir();raw=wd/'raw.md'
   cp=subprocess.run([PANDOC,str(src),'-f','docx','-t','markdown','--wrap=none','--extract-media=assets','-o',str(raw)],cwd=wd,text=True,capture_output=True)
   if cp.returncode:raise RuntimeError(f'Pandoc failed {uid}: {cp.stderr}')
   raw_s=raw.read_text(); s=raw_s
   refs=image_matches(s); extracted=[wd/m.group(2).split()[0] for m in refs]
   if any(not p.is_file() for p in extracted):raise RuntimeError(f'Unresolved extracted image {uid}')
   replacements=[]; local_assets=[]
   for i,(m,p) in enumerate(zip(refs,extracted),1):
    target=None; ref=None; ownership='unit-specific'
    if x['kind']=='chapter' and i==1:
     name='chapter-arrow.png';target=shared/name;ref='../assets/shared/'+name;ownership='shared'
    elif x['kind']=='interlude' and i==1:
     name='interlude-gear.png';target=shared/name;ref='../assets/shared/'+name;ownership='shared'
    elif (x['kind']=='cold-open' and i==2) or (x['kind']=='interlude' and i==2):
     name='separator.png';target=shared/name;ref='../assets/shared/'+name;ownership='shared'
    else:
     stem=dest.stem
     asset_dir=dest.parent/'assets'/stem
     asset_dir.mkdir(parents=True,exist_ok=True)
     label='opening' if x['kind']=='cold-open' and i==1 else f'image-{i:02d}'
     target=asset_dir/(label+ext_for(p));ref=f'assets/{stem}/{target.name}'
    h=sha(p)
    if ownership=='shared':
     if h!=SHARED_EXPECTED[name]:raise RuntimeError(f'{uid}: unexpected shared {name} hash {h}')
     if target.exists() and sha(target)!=h:raise RuntimeError(f'{uid}: shared target conflict {name}')
     if not target.exists():shutil.copy2(p,target);shared_sources[name]={'sha256':h,'first_source':str(src)}
    else: shutil.copy2(p,target);local_assets.append(target)
    replacements.append((m.span(),f'![{m.group(1)}]({ref})',target,ownership))
   for (a,b),new,_,_ in reversed(replacements):s=s[:a]+new+s[b:]
   s=uppercase_smallcaps(s)
   s=promote_label_title(s,x['kind'])
   strike_removed=0
   if uid=='v2-coda':s,strike_removed=remove_strikeout(s)
   legacy_trimmed=False
   if uid in LEGACY_ENDS:s=trim_legacy(s,LEGACY_ENDS[uid]);legacy_trimmed=True
   dest.write_text(s)
   # Text verification: raw Pandoc round-trip, then normalized output against intended transformed candidate.
   source_plain=norm(plain(src,'docx')); raw_plain=norm(plain(raw,'markdown'))
   source_roundtrip_exact=source_plain==raw_plain
   source_word_sequence_exact=word_sequence(source_plain)==word_sequence(raw_plain)
   output_plain=norm(plain(dest,'markdown'))
   if uid=='v2-coda':
    expected_tmp=wd/'expected.md'; expected_s,_=remove_strikeout(raw_s);expected_tmp.write_text(expected_s)
    intended_plain=norm(plain(expected_tmp,'markdown'))
   elif uid in LEGACY_ENDS:
    expected_tmp=wd/'expected.md';expected_tmp.write_text(trim_legacy(raw_s,LEGACY_ENDS[uid]))
    intended_plain=norm(plain(expected_tmp,'markdown'))
   else:intended_plain=source_plain
   transformed_exact=output_plain==intended_plain
   transformed_word_sequence_exact=word_sequence(output_plain)==word_sequence(intended_plain)
   out_refs=image_matches(s);resolved=[(dest.parent/m.group(2).split()[0]).resolve() for m in out_refs]
   if not source_word_sequence_exact or not transformed_word_sequence_exact or not all(p.is_file() for p in resolved):
    raise RuntimeError(f'Verification failed {uid}: source_words={source_word_sequence_exact} transformed_words={transformed_word_sequence_exact} refs={all(p.is_file() for p in resolved)}')
   with zipfile.ZipFile(src) as z:
    media=sorted(n for n in z.namelist() if n.startswith('word/media/') and not n.endswith('/'))
    names=z.namelist(); has_notes={'footnotes_xml':'word/footnotes.xml' in names,'endnotes_xml':'word/endnotes.xml' in names}
   report={
    'schema_version':1,'authority_status':'conversion-candidate-not-canonical','converted_at':now,'unit_id':uid,'kind':x['kind'],'volume':x.get('volume'),
    'source':{'format':'docx','path':str(src),'archive_path':str(ar.relative_to(outroot)),'sha256':sha(src),'bytes':src.stat().st_size},
    'output':{'format':'portable-authoring-markdown','path':str((Path('manuscripts')/dest_rel)),'sha256':sha(dest),'bytes':dest.stat().st_size},
    'pandoc_version':subprocess.check_output([PANDOC,'--version'],text=True).splitlines()[0],
    'verification':{'source_to_raw_markdown_plain_exact':source_roundtrip_exact,'source_to_raw_markdown_word_sequence_exact':source_word_sequence_exact,'candidate_plain_matches_intended_transformation':transformed_exact,'candidate_word_sequence_matches_intended_transformation':transformed_word_sequence_exact,'all_image_references_resolve':all(p.is_file() for p in resolved),'source_embedded_media_count':len(media),'markdown_image_reference_count':len(out_refs),'unused_embedded_media_count':max(0,len(media)-len(out_refs)),'source_plain_characters':len(source_plain),'candidate_plain_characters':len(output_plain),'word_package_notes_parts':has_notes},
    'assets':[{'path':str(p.relative_to(outroot)),'sha256':sha(p),'ownership':own} for _,_,p,own in replacements],
    'normalization':{'portable_markdown':True,'title_promoted_to_h1':x['kind'] in {'chapter','interlude'},'presentation_attributes_removed':True,'strikeout_passages_removed':strike_removed,'legacy_tail_excluded':legacy_trimmed,'legacy_end_text':LEGACY_ENDS.get(uid)},
    'note':'Conversion candidate only. Canonical authority requires review and explicit author confirmation.'
   }
   (reports/(uid+'.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
   aggregated.append(report)
   print(f'[{number:03d}/{len(units)}] {uid} -> {dest_rel}')
 conversion_manifest={
  'schema_version':1,'created_at':now,'authority_status':'full-conversion-candidates-not-canonical','source_root_read_only':str(SOURCE_ROOT),'destination_repository':str(REPO),
  'selection':{'manifest_units':120,'additional_units':['glossary'],'excluded_noncopy_docx':[{'path':str(SOURCE_ROOT/'notes_misc-2025-12-01.docx'),'reason':'Working notes explicitly excluded by author'},{'path':str(SOURCE_ROOT/'5 11c - SM.docx'),'reason':'Planning/outline material, not the full Chapter 11 source'},{'path':str(SOURCE_ROOT/'__book summary.docx'),'reason':'Project summary/reference material, not a manuscript unit'}]},
  'shared_assets':{k:{'sha256':v,'policy':'Deduplicate only on exact SHA-256 match'} for k,v in SHARED_EXPECTED.items()},
  'special_transformations':{'v2-coda':'35 Pandoc strikeout spans removed as deleted draft text','v3-theta-interlude':f'Current body ends at: {LEGACY_ENDS["v3-theta-interlude"]}','v3-33-chapter':f'Current body ends at: {LEGACY_ENDS["v3-33-chapter"]}','v3-33-interlude':f'Current body ends at: {LEGACY_ENDS["v3-33-interlude"]}; later art material remains in archived DOCX and editorial records','epilogue':'One embedded Word image is unused in document flow; only two referenced images were migrated'},
  'counts':{'units':len(aggregated),'by_kind':{}},'units':aggregated}
 from collections import Counter
 conversion_manifest['counts']['by_kind']=dict(Counter(r['kind'] for r in aggregated))
 (outroot/'archive/conversion-manifest.json').parent.mkdir(parents=True,exist_ok=True)
 (outroot/'archive/conversion-manifest.json').write_text(json.dumps(conversion_manifest,ensure_ascii=False,indent=2)+'\n')
 (outroot/'archive/README.md').write_text('# Manuscript conversion archive\n\nThis directory preserves the selected Word sources and the one-time Word-to-Markdown conversion manifest. The Word files are frozen provenance after the author confirms the source-of-truth transition. They must never be reconverted over edited canonical Markdown.\n')
 # Comprehensive link check.
 missing=[]
 for md in manuscripts.rglob('*.md'):
  for m in image_matches(md.read_text()):
   p=(md.parent/m.group(2).split()[0]).resolve()
   if not p.is_file():missing.append((str(md),m.group(2)))
 if missing:raise RuntimeError(f'Broken image references: {missing}')
 print(json.dumps({'units':len(aggregated),'reports':len(list(reports.glob('*.json'))),'markdown':len(list(manuscripts.rglob('*.md'))),'assets':len([p for p in manuscripts.rglob('*') if p.is_file() and p.suffix.lower()!='.md' and '_conversion-reports' not in p.parts]),'broken_refs':len(missing)},indent=2))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('outroot',type=Path);a=ap.parse_args();main(a.outroot)
