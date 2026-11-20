/* AR-ISS 2024 e AIFA Open Data 2024: tabelle regionali, senza poligoni e senza layer.
   Questa edizione non pubblica un rapporto regionale: il portale della Regione Siciliana
   non ha un dataset AMR e il rapporto ReteMIC è escluso perché senza licenza. */
(function () {
  "use strict";
  const region = (window.AMR_ATLAS_CONFIG && window.AMR_ATLAS_CONFIG.regionName) || "Sicilia";
  const arPath = "public/data/ar_iss_2024_sicilia.json";
  const aifaPath = "public/data/aifa_opendata_2024_sicilia_j01.json";
  const esc = (value) => String(value == null ? "" : value).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[char]));
  const num = (value, digits) => Number(value).toLocaleString("it-IT", {
    minimumFractionDigits: digits,
    maximumFractionDigits: digits
  });
  const integer = (value) => Number(value).toLocaleString("it-IT");
  const ci = (value) => String(value == null ? "" : value).replace(/\./g, ",").replace("-", "–");

  const rows = (list) => (list || []).map((row) => `<tr><td>${esc(row.code)}</td><td>${esc(row.pathogen)}</td><td>${esc(row.resistance)}</td><td>${integer(row.isolates)}</td><td>${integer(row.resistant)}</td><td>${num(row.percent, 1)}</td><td>${esc(ci(row.ci95))}</td></tr>`).join("");

  const markup = (ar, aifa) => {
    const coverage = ar.coverage || {};
    const source = ar.source || {};
    const indicator = (aifa && aifa.indicator) || {};
    const aifaSource = (aifa && aifa.source) || {};
    const lead = `Copertura ${num(coverage.value_percent, 1)}% (${esc(coverage.denominator || "")}). Rete regionale con 27 laboratori referenti. Nessun downscaling a provincia o struttura. La tabella non è un layer della mappa.`;
    const aifaLine = `Convenzionata: ${integer(indicator.packs_convenzionata)} confezioni, ${integer(indicator.expenditure_convenzionata_eur)} €. Acquisti diretti: ${integer(indicator.packs_direct_purchase_traceability)} confezioni, ${integer(indicator.expenditure_direct_purchase_traceability_eur)} €. ${esc(indicator.aggregation || "")}. ${esc((aifa && aifa.limitations) || "Confezioni e spesa, non DDD e non resistenza.")}`;
    return `<section class="indicator-panel literature-section" aria-labelledby="ariss-title"><div class="data-digest-heading"><div><p class="section-kicker">SORVEGLIANZA, NON UNA MAPPA DI PREVALENZA</p><h2 id="ariss-title">AR-ISS 2024, indicatori della ${esc(region)}</h2><p class="indicator-lead">${lead}</p></div></div><div class="table-wrap"><table class="literature-table"><thead><tr><th>Indicatore</th><th>Patogeno</th><th>Resistenza</th><th>Isolati</th><th>Resistenti</th><th>%</th><th>IC 95%</th></tr></thead><tbody>${rows(ar.indicators || [])}</tbody></table></div><p class="governance-note">${esc(ar.trend_note || "")} ${esc(coverage.limitations || "")} Licenza ${esc(ar.license || "CC BY 4.0")}. Attribuzione: Istituto Superiore di Sanità (EpiCentro, ${esc(source.report || "RIS-5/2025")}). ${source.url ? `<a href="${esc(source.url)}" target="_blank" rel="noreferrer">Apri il rapporto ↗</a>` : ""}</p><h3>AIFA Open Data 2024, antibatterici J01</h3><p class="governance-note">${aifaLine} Licenza ${esc((aifa && aifa.license) || "CC BY 4.0")}. Attribuzione: Agenzia Italiana del Farmaco. ${aifaSource.url ? `<a href="${esc(aifaSource.url)}" target="_blank" rel="noreferrer">Apri il CSV ↗</a>` : ""}</p></section>`;
  };

  const mount = (html) => {
    if (document.getElementById("ariss-indicators")) return;
    const host = document.querySelector(".data-digest") || document.querySelector(".evidence-shell");
    if (!host) return;
    const holder = document.createElement("div");
    holder.id = "ariss-indicators";
    holder.innerHTML = html;
    host.appendChild(holder);
  };

  Promise.all([
    fetch(arPath, { cache: "no-store" }).then((response) => {
      if (!response.ok) throw new Error("AR-ISS HTTP " + response.status);
      return response.json();
    }),
    fetch(aifaPath, { cache: "no-store" }).then((response) => {
      if (!response.ok) throw new Error("AIFA HTTP " + response.status);
      return response.json();
    })
  ]).then(([ar, aifa]) => mount(markup(ar, aifa))).catch((error) => {
    console.warn("[AMR Atlas] Tabella degli indicatori non disponibile", error);
  });
}());
