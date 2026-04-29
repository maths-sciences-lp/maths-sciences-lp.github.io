#!/usr/bin/env python3
"""
Génère simulations.html (page catalogue) à partir de simulations_data.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from simulations_data import SIMULATIONS

# Catégorisation manuelle des simulations
CATEGORIES = {
    "Mathématiques": [
        "proportionnalite.html", "statistiques.html", "probabilites.html",
        "balance.html", "equations.html", "graphe-equation.html",
        "entrainement-ineq.html", "inegalite.html", "fonction-machine.html",
        "droite-affine.html", "traceur.html", "figures-planes.html",
        "pythagore.html", "thales.html", "solides.html", "stats-2var.html",
        "suites.html", "derivee.html", "trigonometrie.html", "polynome3.html",
        "exp-log.html", "vecteurs.html", "integrale.html", "complexes.html",
        "scalaire.html", "calculs-numeriques.html", "combinatoire.html",
        "probabilites-conditionnelles.html", "matrices.html",
    ],
    "Électricité": [
        "circuit-electrique.html", "ohm.html", "signal-alternatif.html",
        "puissance.html", "transformateur.html", "effet-joule.html",
        "redressement.html", "dephasage.html", "moteur.html",
        "transmission-info.html",
    ],
    "Mécanique": [
        "mouvement.html", "forces.html", "vitesse-acceleration.html",
        "moments.html",
    ],
    "Fluides": [
        "pression.html", "archimede.html", "presse-hydraulique.html",
        "debit.html", "debit-fluide.html", "boyle-mariotte.html", "gaz.html",
    ],
    "Thermique": [
        "chaleur.html", "transferts-thermiques.html", "changement-etat.html",
        "conductance-thermique.html", "paroi-multicouche.html",
        "comparateur-vitrages.html", "rayonnement.html", "serre.html",
        "dilatation-parquet.html", "ctn-etuve-regulation.html",
        "ctn-pt100-comparaison.html",
    ],
    "Chimie": [
        "atome.html", "atome-couches.html", "modeles-atome.html",
        "liaisons-chimiques.html", "concentration.html", "oxydoreduction.html",
        "pile-electrochimique.html", "combustion.html",
    ],
    "Optique & Ondes": [
        "refraction.html", "sources-lumineuses.html", "melangeur.html",
        "eclairage-atelier.html", "son.html", "son-2nde.html",
        "attenuation-sonore.html", "ondes-em.html",
    ],
    "Sécurité & pratique": [
        "securite-laboratoire.html", "anisotropie-bois.html",
        "calepinage.html", "ccf-bac-rangement.html", "escalier-blondel.html",
    ],
}

CATEGORY_COLORS = {
    "Mathématiques": ("#1976d2", "#0a4f9c"),
    "Électricité": ("#eab308", "#a16207"),
    "Mécanique": ("#0284c7", "#0369a1"),
    "Fluides": ("#0891b2", "#155e75"),
    "Thermique": ("#e67e22", "#92400e"),
    "Chimie": ("#6f42c1", "#553c9a"),
    "Optique & Ondes": ("#c026d3", "#86198f"),
    "Sécurité & pratique": ("#dc2626", "#991b1b"),
}


def html_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def render_card(filename: str) -> str:
    meta = SIMULATIONS.get(filename)
    if not meta:
        return f'<!-- Sim manquante : {filename} -->'
    sims_dir = Path(__file__).resolve().parent.parent / "simulations"
    file_path = sims_dir / filename
    if not file_path.exists():
        return f'<!-- Fichier manquant : {filename} -->'
    tags = "".join(f'<span class="tag">{html_escape(t)}</span>' for t in meta.get("tags", []))
    return f"""    <a href="simulations/{filename}" class="sim-card" data-search="{html_escape(meta['title'].lower() + ' ' + meta['description'].lower() + ' ' + ' '.join(meta.get('tags', [])).lower())}">
      <div class="sim-icon">{meta['icon']}</div>
      <div class="sim-body">
        <h3>{html_escape(meta['title'])}</h3>
        <p>{html_escape(meta['description'])}</p>
        <div class="sim-tags">{tags}</div>
      </div>
    </a>"""


def render_category(name: str, sims: list[str]) -> str:
    color, color_dark = CATEGORY_COLORS.get(name, ("#1976d2", "#0a4f9c"))
    cards = "\n".join(render_card(s) for s in sims if (Path(__file__).resolve().parent.parent / "simulations" / s).exists())
    if not cards.strip():
        return ""
    sims_count = sum(1 for s in sims if (Path(__file__).resolve().parent.parent / "simulations" / s).exists())
    return f"""<section class="cat" data-cat="{html_escape(name)}" style="--cat-color:{color};--cat-color-dark:{color_dark}">
  <h2 class="cat-title">{html_escape(name)} <span class="cat-count">{sims_count}</span></h2>
  <div class="sim-grid">
{cards}
  </div>
</section>
"""


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    sections_html = "\n".join(render_category(name, sims) for name, sims in CATEGORIES.items())

    total = sum(1 for sims in CATEGORIES.values() for s in sims
                if (repo_root / "simulations" / s).exists())

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Catalogue des simulations interactives</title>
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="print.css" media="print">
<style>
:root{{--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd}}

.sim-hero{{
  background:linear-gradient(135deg,#0969da,#0a4f9c);
  color:#fff;border-radius:14px;padding:30px 28px;margin:18px 0 24px;
  text-align:center;box-shadow:0 6px 20px rgba(0,0,0,.12)
}}
.sim-hero h1{{margin:0 0 8px;color:#fff;font-size:1.8em}}
.sim-hero p{{opacity:.92;font-size:1em;margin:0 0 14px}}
.sim-hero .stats{{display:flex;justify-content:center;gap:22px;font-size:.92em;opacity:.92;flex-wrap:wrap}}
.sim-hero .stats span::before{{content:"• ";opacity:.6}}
.sim-hero .stats span:first-child::before{{content:""}}

.search-bar{{
  display:flex;gap:10px;margin:0 0 22px;flex-wrap:wrap;align-items:center
}}
.search-bar input{{
  flex:1;min-width:200px;padding:10px 16px;border:2px solid #e2e8f0;
  border-radius:8px;font-size:1em;font-family:inherit;outline:none;transition:border-color .15s
}}
.search-bar input:focus{{border-color:#0969da}}
.filter-tags{{display:flex;gap:6px;flex-wrap:wrap}}
.filter-tag{{
  background:#fff;border:1.5px solid #cbd5e1;color:#334155;
  padding:6px 14px;border-radius:18px;cursor:pointer;font-size:.85em;
  font-weight:600;transition:all .15s
}}
.filter-tag:hover{{border-color:#0969da}}
.filter-tag.active{{background:#0969da;color:#fff;border-color:#0969da}}
.filter-tag.cat-Mathématiques.active{{background:#1976d2;border-color:#1976d2}}
.filter-tag.cat-Électricité.active{{background:#eab308;border-color:#eab308;color:#1e293b}}
.filter-tag.cat-Mécanique.active{{background:#0284c7;border-color:#0284c7}}
.filter-tag.cat-Fluides.active{{background:#0891b2;border-color:#0891b2}}
.filter-tag.cat-Thermique.active{{background:#e67e22;border-color:#e67e22}}
.filter-tag.cat-Chimie.active{{background:#6f42c1;border-color:#6f42c1}}
.filter-tag.cat-Optique{{}}

.cat{{margin:24px 0}}
.cat-title{{
  margin:0 0 14px;color:var(--cat-color);font-size:1.15em;font-weight:700;
  display:flex;align-items:center;gap:10px;border:none;padding:0
}}
.cat-title::before{{
  content:"";width:5px;height:1.2em;background:var(--cat-color);border-radius:3px
}}
.cat-count{{
  background:var(--cat-color);color:#fff;border-radius:12px;padding:2px 10px;
  font-size:.7em;font-weight:600
}}

.sim-grid{{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(280px,1fr));
  gap:14px
}}

.sim-card{{
  display:flex;text-decoration:none;color:inherit;
  background:#fff;border:1px solid #e2e8f0;border-radius:10px;
  padding:14px 16px;gap:12px;align-items:flex-start;
  transition:all .15s ease
}}
.sim-card:hover{{
  border-color:var(--cat-color);transform:translateY(-2px);
  box-shadow:0 4px 12px rgba(0,0,0,.08)
}}
.sim-icon{{
  flex-shrink:0;width:44px;height:44px;border-radius:8px;
  background:rgba(0,0,0,.04);
  display:flex;align-items:center;justify-content:center;font-size:1.3em
}}
.sim-body{{flex:1;min-width:0}}
.sim-body h3{{
  margin:0 0 4px;color:var(--cat-color);font-size:.98em;font-weight:700;
  border:none;padding:0
}}
.sim-body p{{
  margin:0 0 6px;font-size:.82em;color:#475569;line-height:1.45;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden
}}
.sim-tags{{display:flex;gap:4px;flex-wrap:wrap}}
.sim-tags .tag{{
  background:rgba(0,0,0,.04);color:#475569;padding:1px 7px;
  border-radius:4px;font-size:.7em;font-weight:600
}}

.no-results{{
  text-align:center;padding:40px 20px;color:#64748b;font-size:.95em;
  background:#f8fafc;border:1px dashed #cbd5e1;border-radius:10px
}}

@media(max-width:600px){{
  .sim-hero h1{{font-size:1.35em}}
  .sim-grid{{grid-template-columns:1fr}}
}}
</style>
</head>
<body>
<div class="c">
<a href="index.html" class="nb">← Accueil</a>

<div class="sim-hero">
  <h1>🔬 Catalogue des simulations interactives</h1>
  <p>Manipule, explore et apprends avec {total} simulations en ligne</p>
  <div class="stats">
    <span>{total} simulations</span>
    <span>{len(CATEGORIES)} domaines</span>
    <span>Bac Pro · CAP · BTS</span>
  </div>
</div>

<div class="search-bar">
  <input type="search" id="search" placeholder="🔍 Rechercher (titre, mot-clé, sujet…)" aria-label="Rechercher une simulation">
  <div class="filter-tags" id="filter-tags">
    <button class="filter-tag active" data-filter="all" onclick="setFilter('all')">Toutes</button>
    {''.join(f'<button class="filter-tag cat-{html_escape(c).replace(" ", "_")}" data-filter="{html_escape(c)}" onclick="setFilter({chr(39)}{html_escape(c)}{chr(39)})">{html_escape(c)}</button>' for c in CATEGORIES.keys())}
  </div>
</div>

<div id="no-results" class="no-results" style="display:none">
  Aucune simulation ne correspond à ta recherche.
</div>

{sections_html}

</div>
<script src="nav.js"></script>
<script>
let activeFilter = 'all';
let activeQuery = '';

function setFilter(name) {{
  activeFilter = name;
  document.querySelectorAll('.filter-tag').forEach(t => {{
    t.classList.toggle('active', t.dataset.filter === name);
  }});
  applyFilters();
}}

function applyFilters() {{
  const query = activeQuery.trim().toLowerCase();
  let total = 0, visible = 0;
  document.querySelectorAll('.cat').forEach(cat => {{
    const matchCat = activeFilter === 'all' || cat.dataset.cat === activeFilter;
    let any = false;
    cat.querySelectorAll('.sim-card').forEach(card => {{
      total++;
      const matchQ = !query || card.dataset.search.includes(query);
      const show = matchCat && matchQ;
      card.style.display = show ? '' : 'none';
      if (show) {{ any = true; visible++; }}
    }});
    cat.style.display = any ? '' : 'none';
  }});
  document.getElementById('no-results').style.display = visible === 0 ? '' : 'none';
}}

document.getElementById('search').addEventListener('input', e => {{
  activeQuery = e.target.value;
  applyFilters();
}});
</script>
</body>
</html>
"""

    out = repo_root / "simulations.html"
    out.write_text(html, encoding="utf-8")
    print(f"✓ simulations.html généré ({total} simulations)")


if __name__ == "__main__":
    main()
