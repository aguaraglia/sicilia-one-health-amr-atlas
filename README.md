# Atlante One Health AMR · Sicilia

Edizione regionale `sicilia_amr_atlas`, pubblicata da Codex Vitae ETS sulla stessa
base delle altre edizioni regionali. Il portale nazionale è [atlanteamr.it](https://atlanteamr.it).

## Stato

La letteratura pubblicata con collegamento territoriale esplicito alla Sicilia
è concentrata su Palermo e Catania. Ne restano 93 inclusi (20 novembre 2026):
21 di struttura, 30 di comune, 11 di provincia e 31 a scala regionale. Sono
92 record PubMed e 1 record Europe PMC senza PMID (PMC10595122, CC BY-NC).

Sette strutture sono punti, geocodificate su OSM Nominatim il 20 novembre 2026
(© OpenStreetMap contributors, ODbL):

- AOU Policlinico «Paolo Giaccone», Palermo: 8 studi (38,1044530 N, 13,3610802 E; amenity=hospital);
- IRCCS ISMETT, Palermo: 5 studi (38,1017403 N, 13,3580549 E; building=hospital);
- AOU Policlinico «G. Martino», Messina: 3 studi (38,1647706 N, 15,5356849 E);
- Ospedale Sant'Elia, Caltanissetta: 2 studi (37,4904746 N, 14,0309610 E);
- ARNAS Civico, Palermo: 1 studio (38,1033334 N, 13,3547225 E);
- Fondazione Istituto G. Giglio, Cefalù: 1 studio (38,0279694 N, 14,0123641 E);
- Centro Cuore Morgagni, Pedara (CT): 1 studio (37,6172218 N, 15,0520608 E).

Il Policlinico «G. Rodolico – San Marco» e l'ARNAS Garibaldi di Catania hanno
più presidi e gli studi non indicano quale. La Casa di cura Di Stefano di
Catania non ha un risultato Nominatim. Restano sul comune di Catania. Aziende
agricole, macelli, depuratori, coste e centri di recupero non sono punti.

Palermo ha 37 studi. Catania ne ha 10. Messina ne ha 6. Caltanissetta e Ragusa
ne hanno 2 ciascuna. Agrigento, Enna, Siracusa e Trapani non hanno studi con
luogo provinciale esclusivo. Cinque studi coprono più province. Trentuno studi
a scala regionale usano il contorno della regione, isole minori comprese.
Ustica (fauna selvatica) e Casteldaccia (ambiente) sono comuni con uno studio.

Per settore: 48 AMR clinica, 7 consumo, 2 stewardship, 8 veterinaria, 1 animali
d'affezione, 11 alimentare, 7 ambientale, 9 fauna selvatica.

L'edizione pubblica AR-ISS 2024 (copertura 77,0%, 27 laboratori referenti,
CC BY 4.0; attribuzione Istituto Superiore di Sanità; referenti F. G. Leanza e
S. Stefani) e AIFA Open Data 2024, antibatterici J01 (CC BY 4.0; codreg 190;
convenzionata 6.045.091 confezioni e 51,07 milioni di euro, acquisti diretti
1.644.348 confezioni e 25,20 milioni di euro; attribuzione Agenzia Italiana
del Farmaco). Nessun rapporto ISTISAN/ISS regionale sulla Sicilia è stato
trovato. Il rapporto ReteMIC di Qualità Sicilia SSR è escluso perché senza
licenza.

Sei layer (AMR umana, veterinaria, alimentare, ambientale, fauna selvatica,
contorno regionale):

- AMR umana: 12 elementi, 47 studi (7 punti: Policlinico «P. Giaccone», ARNAS Civico e ISMETT a Palermo, Policlinico «G. Martino» a Messina, Sant'Elia a Caltanissetta, Fondazione Giglio a Cefalù, Centro Cuore Morgagni a Pedara; comuni di Palermo e Catania; province di Messina, Palermo e Ragusa);
- AMR veterinaria: 4 elementi, 9 studi (regione; province di Palermo e Ragusa; comune di Palermo);
- AMR alimentare: 3 elementi, 11 studi (regione; comune di Palermo; province di Agrigento, Palermo e Trapani);
- AMR ambientale: 3 elementi, 7 studi (regione; Casteldaccia; Catania, Siracusa e Giarre);
- AMR nella fauna selvatica: 6 elementi, 9 studi (regione; Ustica; province di Messina e di Palermo; Caltanissetta-Ragusa-Siracusa; Catania-Ragusa-Siracusa);
- studi a scala regionale: 1 elemento, 10 studi umani sul contorno.

I layer vuoti e le aree senza segnaposto sono nessuna evidenza pubblicata,
non resistenza zero. In questa edizione nessun layer di studi è vuoto. Ogni
popup cita lo studio e il DOI (o il record PubMed o Europe PMC se il DOI non
è assegnato) e ricorda che il segnaposto è il luogo dello studio, non una
prevalenza.

Confini ISTAT 2026 (391 comuni, 9 unità sovracomunali, regione 19), letti in
UTF-8. Il contorno comprende le isole minori (Ustica, Eolie, Egadi, Pantelleria,
Pelagie). Il portale regionale, Qualità Sicilia SSR, dati.regione.sicilia.it,
ARPA Sicilia, i siti dei Policlinici, il sito dell'IZS della Sicilia e il PDF
OsMed sono esclusi o non disponibili: vedi `metadata/EXCLUDED_SOURCES.md`.

Il conteggio in homepage e in pubblicazioni legge
`public/data/literature-catalog.json` (93).

## Pagine

Sorgente su `main`. Il sito statico è pubblicato dal branch `gh-pages`
(GitHub Pages, cartella `/`). Nessun file `CNAME`: il dominio
`sicilia.atlanteamr.it` si configura a parte. Analitica: GoatCounter
`https://atlanteamr.goatcounter.com/count`, come le altre edizioni.

## Build locale

```bash
python3 -m http.server 8000
```

Aprire `http://localhost:8000/`.

Per rigenerare i dati pubblici servono gli input in `raw/` e, per i confini,
l'archivio ISTAT indicato in `metadata/SNAPSHOTS.tsv`. I DBF ISTAT si leggono
in UTF-8:

```bash
pip install -r requirements-geodata.txt
python3 scripts/build_istat_geography.py --source-root <Limiti01012026_g> --output-root public/geography
python3 scripts/build_literature_catalog.py
python3 scripts/build_study_evidence_layers.py
```

## Directory

- `public/`: dati e asset approvati per il sito;
- `metadata/`: fonti, snapshot, ambito pubblico e fonti escluse;
- `raw/`: curatela, esummary e risposte Nominatim;
- `scripts/`: ricostruzione del catalogo e dei layer;
- `private/`: nessun dato riservato in questa edizione.
