#!/usr/bin/env python3
"""Build public/data/literature-catalog.json for the Sicilia edition.

Input: raw/curation/rows.json (curated decisions, 2026-11-20) and
raw/esummary_included.json (PubMed esummary for author initials and journal).
Only rows with decision == "include" enter the catalog.
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCOPE = {"healthcare_amr": "healthcare_amr", "uso_antibiotici_umano": "human_antimicrobial_use",
         "stewardship": "antimicrobial_stewardship", "veterinaria_amr": "veterinary_amr",
         "animali_compagnia": "companion_animal_amr", "ambientale_amr": "environmental_amr", "fauna_selvatica": "wildlife_amr", "alimentare": "foodborne_amr"}
SCALE = {"struttura": "struttura nominata", "comune": "comune", "provincia": "provincia",
         "regione": "regione", "area_nominata": "area nominata"}
rows = json.load(open(ROOT / "raw/curation/rows.json"))
es = json.load(open(ROOT / "raw/esummary_included.json"))["result"]
records = []
for r in rows:
    if r["decision"] != "include":
        continue
    if not r["pmid"]:
        k = r["epmc_id"]; a = r["first_author"]
        records.append({"id": f"epmc_{k}", "year": int(r["year"]), "title": r["title"],
            "authors": f"{a} et al.", "journal": r.get("journal") or "Europe PMC", "scope": SCOPE[r["sector"]],
            "geographic_link": f"{r['place']}. Scala: {SCALE[r['scale']]}. Record Europe PMC senza PMID.",
            "pmid": None, "doi": r["doi"] or None, "source_url": f"https://europepmc.org/article/PMC/{k}"})
        continue
    s = es[r["pmid"]]
    link = f"{r['place']}. Scala: {SCALE[r['scale']]}."
    if r.get("fulltext_check","").startswith("Testo integrale"):
        link += " Luogo verificato sul testo integrale."
    records.append({
        "id": f"pubmed_{r['pmid']}", "year": int(r["year"]), "title": r["title"],
        "authors": f"{s['sortfirstauthor']} et al." if len(s.get("authors", [])) > 1 else s["sortfirstauthor"],
        "journal": s["source"], "scope": SCOPE[r["sector"]], "geographic_link": link,
        "pmid": r["pmid"], "doi": r["doi"] or None,
        "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/"})
records.sort(key=lambda x: (-x["year"], x["id"]))
out = {"schema_version": "1.0", "edition": "sicilia_amr_atlas",
       "selection_note": ("Selezione curata e aggiornata il 2026-11-20: studi regionali o locali con collegamento territoriale esplicito alla Sicilia (struttura, comune o provincia nominati, o regione intera). Gli studi dell'IZS della Sicilia e gli altri studi multiregionali entrano solo se la quota siciliana è separata (titolo/abstract, o testo integrale open access per i casi dubbi). L'afferenza degli autori da sola non basta. Esclusi gli studi di sola resistenza antifungina e antivirale, di efficacia terapeutica, diagnostici e in vitro; gli studi prognostici sono dubbi. Non equivale a una revisione sistematica e gli studi locali non sono trasformati in stime regionali."),
       "records": records}
(ROOT / "public/data/literature-catalog.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(records))
