# Fonti escluse o non disponibili (edizione Sicilia, 2026-11-20)

Regola di riuso (decisione di Alex, 2026-11-20): sono accettabili le licenze aperte CC BY e CC0, e anche CC BY-NC e CC BY-NC-SA, perché CodexVitae ETS non ha scopi commerciali. Servono sempre l'attribuzione e, per NC-SA, la stessa licenza sui file derivati. Non usiamo fonti senza licenza dichiarata o con il riuso vietato. Le pagine che rispondono 403 o 500, o che mostrano una challenge anti-bot, non vengono aggirate; la verifica TLS non viene mai disattivata. Il rapporto OsMed (con i rapporti regionali OsMed e il rapporto AIFA sugli antibiotici basato su OsMed) è escluso per decisione di progetto.

## Regione Siciliana (regione.sicilia.it)
- Note legali (https://www.regione.sicilia.it/note-legali): riproduzione e distribuzione «autorizzate esclusivamente [...] per finalità non commerciali, garantendo l'integrità degli elementi riprodotti e mediante indicazione della fonte». Compatibile con la regola NC, ma sul portale non è stato trovato nessun rapporto o dataset AMR. NESSUN DATO.

## Qualità Sicilia SSR (DASOE, Assessorato della Salute)
- Le pagine «Antibioticoresistenza e Stewardship» e «Consumo e antibiotico resistenze» (https://www.qualitasiciliassr.it/) pubblicano il Rapporto ReteMIC n. 1 (dati di sorveglianza regionale delle resistenze 2019, novembre 2020), documenti sulla stewardship, la «Dashboard AMR – Rete MIC» e la sorveglianza CRE.
- Il sito non ha note legali (la pagina risponde 404) e il PDF del rapporto ReteMIC non riporta condizioni di riuso. Le note legali di regione.sicilia.it valgono per quel portale, non per questo dominio. Licenza non chiara: ESCLUSO. Il rapporto non è stato ridistribuito (solo URL e SHA-256 in `metadata/SNAPSHOTS.tsv`). Se serve, va chiesta un'autorizzazione esplicita al DASOE.
- Il dato regionale di resistenza resta quello AR-ISS 2024 (la Sicilia partecipa con la propria rete regionale).

## Rapporti ISS/ISTISAN regionali
- NON TROVATO. https://www.epicentro.iss.it/farmaci/pdf/sicilia/ restituisce la pagina 404 di EpiCentro.

## Open data regionali (dati.regione.sicilia.it)
- Errore TLS (EOF durante l'handshake) dal box; il fetch esterno riceve HTTP 504. Non aggirato. NON DISPONIBILE.

## ARPA Sicilia
- https://www.arpa.sicilia.it/ e https://arpa.sicilia.it/: errore TLS (certificato non verificabile; EOF) dal box; il fetch esterno riceve HTTP 500. Non aggirato. NON DISPONIBILE.

## Aziende sanitarie e ospedaliere
- AOU Policlinico «P. Giaccone» (policlinicogiaccone.it): certificato TLS non valido per il nome host. AOU Policlinico «G. Rodolico – San Marco» (policlinicorodolico.it): errore TLS (EOF). Non aggirati. NON DISPONIBILI.

## IZS della Sicilia «A. Mirri» (Palermo)
- https://www.izssicilia.it/ e il sito di amministrazione trasparente sono raggiungibili, ma non dichiarano una licenza per i contenuti (note legali 404) e non pubblicano dati AMR. NESSUN DATO.
- Gli articoli con autori IZS entrano dalla letteratura solo con luogo siciliano esplicito: tra gli inclusi 33396502 (E. coli da animali domestici, sede di Ragusa), 34356729 (Salmonella da animali e alimenti), 37922428, 40001431 (mastiti, area di Ragusa), 40137779 (Listeria), 42791794 (suini e cinghiali).

## OsMed
- Escluso per decisione di progetto.

## Letteratura: testi integrali
- Testi integrali open access letti dall'archivio PMC tramite NCBI E-utilities (efetch db=pmc, API pubblica): 57 richiesti, 57 scaricati, 54 con corpo del testo (21900525, 31524037 e 34659460 senza corpo).
- Nessuna pagina 403 o challenge anti-bot è stata aggirata.
