# Nominatim, 2026-11-20 (Sicilia)

UA "CodexVitae-AMR-atlas/1.0 (info@codexvitae.it)", countrycodes=it, jsonv2, limit=3, pausa 1,1 s. Risposte grezze: results_2026-11-20.json (16 query).

Strutture nominate negli studi inclusi da geocodificare: AOU Policlinico «Paolo Giaccone» (Palermo), ARNAS Civico (Palermo), IRCCS ISMETT (Palermo), AOU Policlinico «G. Martino» (Messina), Ospedale Sant'Elia (Caltanissetta), Fondazione Istituto G. Giglio (Cefalù), Centro Cuore Morgagni (Pedara, CT), AOU Policlinico «G. Rodolico – San Marco» (Catania), ARNAS Garibaldi (Catania), Casa di cura Di Stefano (Catania).

Punti usati (solo oggetti ospedalieri OSM):
- giaccone_pa: "Azienda Ospedaliera Universitaria Policlinico «Paolo Giaccone»", amenity=hospital, Via Gaetano Lodato, Palermo: lat 38.1044530, lon 13.3610802.
- civico_pa: "Ospedale Civico e Benefratelli «G. Di Cristina» e «M. Ascoli»", amenity=hospital, Via Carmelo Lazzaro, Palermo: lat 38.1033334, lon 13.3547225 (Nominatim restituisce due oggetti con lo stesso nome a circa 400 m; scelto quello su Via Carmelo Lazzaro, lato dell'ingresso principale di Piazza Nicola Leotta; scartato quello su Via Andrea Chiaramonte, 38.1033119, 13.3582682).
- ismett_pa: "ISMETT", building=hospital (edificio ospedaliero, non amenity), Viale Fra Giuliano Majali, Palermo: lat 38.1017403, lon 13.3580549 (scartata la fermata del tram omonima).
- martino_me: "Policlinico Universitario Gaetano Martino", amenity=hospital, Via Rinaldo Bonanno, Messina: lat 38.1647706, lon 15.5356849.
- santelia_cl: "Ospedale Sant'Elia", amenity=hospital, Caltanissetta: lat 37.4904746, lon 14.0309610.
- giglio_cefalu: "Fondazione Istituto Giuseppe Giglio", amenity=hospital, Viale G. Giardina, Cefalù: lat 38.0279694, lon 14.0123641.
- morgagni_ct: "Centro Cuore Morgagni", amenity=hospital, Via La Rosa, Pedara (CT): lat 37.6172218, lon 15.0520608 (lo studio scrive «Catania»: la struttura è nel comune di Pedara, città metropolitana di Catania).

Non usati come punti (studi sul poligono comunale di Catania):
- AOU Policlinico «G. Rodolico – San Marco»: azienda su più presidi (Ospedale Gaspare Rodolico, Via Santa Sofia, 37.5299837, 15.0702874; Ospedale San Marco, Librino, 37.4800172, 15.0381272; in passato Vittorio Emanuele, Ferrarotto, Santo Bambino). Gli studi non indicano il presidio: nessun punto.
- ARNAS Garibaldi: due presidi (Garibaldi Centro e Garibaldi Nesima), lo studio non indica quale: nessun punto.
- Casa di cura Di Stefano (Catania): nessun risultato.
