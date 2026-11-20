#!/usr/bin/env python3
"""Edizione Sicilia, 2026-11-20: testi integrali open access
letti dall'archivio PMC tramite NCBI E-utilities (efetch db=pmc, API pubblica), 20 PMCID per richiesta.
Salva ft/<pmid>.xml e ft/ncbi_src.json; poi fulltext_fetch_2026-11-20.py estrae i frammenti con georx.GEO."""
import json,requests,re,time,os
R=json.load(open('raw/pubmed_records.json'))
ids=[p for p in open('ft_ids.txt').read().split() if not os.path.exists(f'ft/{p}.xml')]
pm={R[p]['pmc'].replace('PMC',''):p for p in ids if R[p].get('pmc')}
src={};keys=list(pm)
for i in range(0,len(keys),20):
    b=keys[i:i+20]
    x=requests.post('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',data={'db':'pmc','id':','.join(b),'retmode':'xml'},timeout=120)
    for a in re.findall(r'<article[\s>][\s\S]*?</article>',x.text):
        m=re.search(r'<article-id pub-id-type="(?:pmc|pmcid|pmcaid)">(?:PMC)?(\d+)</article-id>',a)
        if m and m.group(1) in pm:
            open(f'ft/{pm[m.group(1)]}.xml','w').write(a); src[pm[m.group(1)]]='NCBI PMC efetch'+('' if '<body' in a else ' (senza body)')
    time.sleep(0.5)
json.dump(src,open('ft/ncbi_src.json','w'))
