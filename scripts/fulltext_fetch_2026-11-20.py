import json,requests,time,re,sys
R=json.load(open('raw/pubmed_records.json'))
ids=open("ft_ids.txt").read().split()
try: st=json.load(open('ft/status.json'))
except: st={}
from georx import GEO
import os
NS=json.load(open('ft/ncbi_src.json')) if os.path.exists('ft/ncbi_src.json') else {}
for p in ids:
    if p in st and st[p]['n']>0: continue
    r=R[p]; pmc=r.get('pmc',''); txt=None
    import os
    if pmc and os.path.exists(f'ft/{p}.xml'):
        t=open(f'ft/{p}.xml').read(); how=NS.get(p,f'EPMC {pmc}')+f' {pmc}'
        t=re.sub(r'<aff[\s\S]*?</aff>',' ',t); t=re.sub(r'<ref-list[\s\S]*?</ref-list>',' ',t); txt=re.sub(r'<[^>]+>',' ',t)
    elif pmc:
        try:
            x=requests.get(f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML',timeout=30)
            if x.status_code==200 and len(x.text)>2000:
                open(f'ft/{p}.xml','w').write(x.text); how=f'EPMC {pmc}'
                t=x.text
                # drop affiliations and references
                t=re.sub(r'<aff[\s\S]*?</aff>',' ',t); t=re.sub(r'<ref-list[\s\S]*?</ref-list>',' ',t)
                txt=re.sub(r'<[^>]+>',' ',t)
            else: how=f'EPMC {pmc} HTTP {x.status_code}'
        except Exception as e: how=f'EPMC err {e}'
    else: how='no PMCID'
    sn=[]
    if txt:
        for m in GEO.finditer(txt): sn.append(' '.join(txt[max(0,m.start()-150):m.end()+110].split()))
    st[p]=dict(how=how,n=len(sn),snips=sn[:14]); print(p,how,len(sn),flush=True); time.sleep(0.3)
    json.dump(st,open('ft/status.json','w'),ensure_ascii=False,indent=1)
json.dump(st,open('ft/status.json','w'),ensure_ascii=False,indent=1)
