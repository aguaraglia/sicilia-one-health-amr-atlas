# Geografia pubblica - edizione Sicilia

La cartografia pubblica dell'edizione Sicilia comprende:

- `atlas_region.geojson`: confine regionale ISTAT 2026 (codice 19);
- `atlas_provinces.geojson`: 9 unità sovracomunali ISTAT 2026 (liberi consorzi comunali e città metropolitane): Trapani (081), Palermo (082, città metropolitana), Messina (083, città metropolitana), Agrigento (084), Caltanissetta (085), Enna (086), Catania (087, città metropolitana), Ragusa (088), Siracusa (089);
- `atlas_municipalities.geojson`: 391 comuni ISTAT al 1/1/2026.

Fonte: ISTAT, «Confini delle unità amministrative a fini statistici al 1° gennaio 2026», versione generalizzata (Limiti01012026_g.zip, SHA-256 in `metadata/SNAPSHOTS.tsv`), CC BY 4.0. Gli attributi dei DBF sono letti in UTF-8 e le coordinate sono convertite da EPSG:32632 a WGS84 da `scripts/build_istat_geography.py`.

Gli studi della letteratura curata stanno in layer distinti sotto `public/data/`. Sette strutture sono punti, geocodificate su OSM Nominatim (ODbL) il 2026-11-20 con oggetti ospedalieri: AOU Policlinico «Paolo Giaccone» (38.1044530 N, 13.3610802 E), ARNAS Civico (38.1033334 N, 13.3547225 E) e IRCCS ISMETT (38.1017403 N, 13.3580549 E; oggetto `building=hospital`) a Palermo; AOU Policlinico «G. Martino» a Messina (38.1647706 N, 15.5356849 E); Ospedale Sant'Elia a Caltanissetta (37.4904746 N, 14.0309610 E); Fondazione Istituto G. Giglio a Cefalù (38.0279694 N, 14.0123641 E); Centro Cuore Morgagni a Pedara, CT (37.6172218 N, 15.0520608 E). Il Policlinico «G. Rodolico – San Marco» e l'ARNAS Garibaldi di Catania hanno più presidi e gli studi non dicono quale: stanno sul poligono comunale di Catania, come la Casa di cura Di Stefano (nessun risultato Nominatim). Dettagli in `raw/nominatim/NOTE.md`. Aziende agricole, macelli, depuratori, coste e centri di recupero non sono punti.
