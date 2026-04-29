#!/usr/bin/env python3
"""
Génère les pages simulation.html par chapitre à partir des données curées
dans simulations_data.py.

Pour chaque chapitre listé dans CHAPTER_SIMS :
- Extrait les métadonnées du chapitre (titre, sous-titre, n°) depuis lecon.html
- Liste les simulations associées avec leurs descriptions et notes pédagogiques
- Génère simulation.html avec le design validé (hero, intro, cartes riches, footer)
"""

from __future__ import annotations

import html as _html
import re
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from simulations_data import SIMULATIONS, CHAPTER_SIMS

# ---------------------------------------------------------------------------
# Configuration des thèmes par section (alignée avec generate_chapter_indexes)
# ---------------------------------------------------------------------------

THEMES = {
    "maths/seconde": ("#0056b3", "#ebf5ff", "#bee3f8", "#003d80"),
    "maths/premiere": ("#0969da", "#dbeafe", "#93c5fd", "#0a4f9c"),
    "maths/terminale": ("#0969da", "#dbeafe", "#93c5fd", "#0a4f9c"),
    "maths/lgt-terminale": ("#4f46e5", "#eef2ff", "#a5b4fc", "#3730a3"),
    "maths/cap": ("#b45309", "#fffbeb", "#fde68a", "#92400e"),
    "maths/bts": ("#0969da", "#dbeafe", "#93c5fd", "#0a4f9c"),
    "physique-chimie/seconde": ("#6f42c1", "#f5f0ff", "#c4b5fd", "#553c9a"),
    "physique-chimie/premiere-iccer": ("#0969da", "#dbeafe", "#93c5fd", "#0a4f9c"),
    "physique-chimie/premiere-era": ("#2da44e", "#f0fff4", "#86efac", "#1e7034"),
    "physique-chimie/terminale-iccer": ("#0969da", "#dbeafe", "#93c5fd", "#0a4f9c"),
    "physique-chimie/terminale-era": ("#2da44e", "#f0fff4", "#86efac", "#1e7034"),
    "physique-chimie/cap": ("#6f42c1", "#f5f0ff", "#c4b5fd", "#553c9a"),
}

# ---------------------------------------------------------------------------
# Extraction des métadonnées du chapitre depuis lecon.html
# ---------------------------------------------------------------------------

H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
SOUS_TITRE_RE = re.compile(r'<p\s+class="sous-titre"[^>]*>(.*?)</p>', re.DOTALL)
CHAPITRE_NUM_RE = re.compile(r"(?:chapitre|ch)\s*0*(\d+)", re.IGNORECASE)


def strip_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = _html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract_chapter_meta(lecon_text: str, chapter_dir: str) -> dict:
    title = ""
    chapter_num = 0
    sous_titre = ""

    m = H1_RE.search(lecon_text)
    if m:
        raw = strip_html(m.group(1))
        m_num = CHAPITRE_NUM_RE.search(raw)
        if m_num:
            chapter_num = int(m_num.group(1))
        title = re.sub(
            r"^(?:chapitre|ch)\s*0*\d+\s*[–\-—:]\s*",
            "",
            raw,
            flags=re.IGNORECASE,
        ).strip()

    if chapter_num == 0:
        m_dir = re.search(r"ch(\d+)", chapter_dir)
        if m_dir:
            chapter_num = int(m_dir.group(1))

    m2 = SOUS_TITRE_RE.search(lecon_text)
    if m2:
        sous_titre = strip_html(m2.group(1))

    return {"num": chapter_num, "title": title, "sous_titre": sous_titre}


def html_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def get_section_path(chapter_path: str) -> str:
    """Retourne le préfixe section ('maths/seconde', etc.) depuis un path chapitre."""
    parts = chapter_path.split("/")
    if parts[0] == "physique-chimie":
        return f"{parts[0]}/{parts[1]}"
    return f"{parts[0]}/{parts[1]}"


# ---------------------------------------------------------------------------
# Rendu HTML
# ---------------------------------------------------------------------------


def render_simulation_card(sim_filename: str, chapter_pedagogy: str) -> str:
    """Génère une carte de simulation."""
    meta = SIMULATIONS.get(sim_filename)
    if not meta:
        return f"<!-- Simulation inconnue: {sim_filename} -->"

    tags_html = "".join(
        f'        <span class="sim-tag">{html_escape(t)}</span>\n'
        for t in meta.get("tags", [])
    )

    pedagogy_html = ""
    if chapter_pedagogy:
        pedagogy_html = (
            f'      <span class="pedago">{html_escape(chapter_pedagogy)}</span>\n'
        )

    return f"""  <div class="sim-item">
    <div class="sim-icon">{meta['icon']}</div>
    <div class="sim-body">
      <h3>{html_escape(meta['title'])}</h3>
      <p>{html_escape(meta['description'])}</p>
{pedagogy_html}      <div class="sim-tags">
{tags_html}      </div>
    </div>
    <a href="../../../simulations/{sim_filename}" class="sim-launch" target="_blank" rel="noopener">Ouvrir →</a>
  </div>
"""


def render_simulation_page(
    *,
    chapter_num: int,
    chapter_title: str,
    sous_titre: str,
    sims: list[str],
    pedagogy: dict,
    theme: tuple,
) -> str:
    p, p_bg, p_border, p_dark = theme
    n = len(sims)

    cards_html = "\n".join(
        render_simulation_card(sim, pedagogy.get(sim, "")) for sim in sims
    )

    title_html = html_escape(chapter_title) if chapter_title else f"Chapitre {chapter_num}"
    sous_titre_safe = html_escape(sous_titre)
    page_title = f"Ch{chapter_num:02d} — Simulations interactives — {title_html}"

    plural_disponibles = "s" if n > 1 else ""

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{page_title}</title>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>
:root{{--p:{p};--p-bg:{p_bg};--p-border:{p_border}}}

.sim-hero{{
  background:linear-gradient(135deg,var(--p) 0%,{p_dark} 100%);
  color:#fff;border-radius:14px;padding:28px 26px;margin:18px 0 26px;
  box-shadow:0 6px 20px rgba(0,0,0,.12)
}}
.sim-hero .ch-num{{
  display:inline-block;background:rgba(255,255,255,.2);
  border:1px solid rgba(255,255,255,.4);border-radius:8px;
  padding:4px 14px;font-size:.85em;font-weight:700;letter-spacing:.5px
}}
.sim-hero h1{{margin:12px 0 6px;color:#fff;font-size:1.6em;line-height:1.2}}
.sim-hero .sub{{opacity:.92;font-size:.9em;margin:0}}
.sim-hero .meta{{margin-top:12px;font-size:.85em;opacity:.92}}

.intro-pedago{{
  background:var(--p-bg);border-left:4px solid var(--p);
  padding:14px 20px;border-radius:0 10px 10px 0;margin:0 0 26px;font-size:.95em
}}
.intro-pedago strong{{color:var(--p)}}

.sim-list{{display:flex;flex-direction:column;gap:18px;margin:24px 0}}

.sim-item{{
  background:#fff;border:1px solid #e2e8f0;border-radius:12px;
  padding:20px 22px;display:grid;
  grid-template-columns:60px 1fr auto;gap:18px;align-items:center;
  transition:all .15s ease
}}
.sim-item:hover{{border-color:var(--p);box-shadow:0 4px 14px rgba(0,0,0,.08)}}

.sim-icon{{
  width:60px;height:60px;border-radius:12px;
  background:var(--p-bg);
  display:flex;align-items:center;justify-content:center;
  font-size:1.8em
}}
.sim-body h3{{
  margin:0 0 6px;color:var(--p);font-size:1.08em;font-weight:700;
  border:none;padding:0
}}
.sim-body p{{margin:0 0 6px;font-size:.92em;color:#4a5568;line-height:1.5}}
.sim-body .pedago{{
  display:block;font-size:.83em;color:#6b7280;
  margin-top:4px;font-style:italic
}}

.sim-launch{{
  display:inline-flex;align-items:center;gap:6px;
  background:var(--p);color:#fff;text-decoration:none;
  padding:9px 16px;border-radius:8px;font-weight:600;font-size:.92em;
  transition:transform .12s
}}
.sim-launch:hover{{transform:translateY(-1px);background:{p_dark}}}

.sim-tags{{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}}
.sim-tag{{
  display:inline-block;background:var(--p-bg);color:var(--p);
  border:1px solid var(--p-border);border-radius:4px;
  padding:1px 8px;font-size:.72em;font-weight:600;letter-spacing:.3px
}}

.ch-footer-nav{{
  display:flex;justify-content:space-between;align-items:center;
  margin-top:36px;padding-top:18px;border-top:1px solid #e2e8f0;
  font-size:.88em;flex-wrap:wrap;gap:12px
}}
.ch-footer-nav a{{color:var(--p);text-decoration:none;font-weight:600}}
.ch-footer-nav a:hover{{text-decoration:underline}}

@media(max-width:600px){{
  .sim-item{{grid-template-columns:48px 1fr;gap:12px;padding:14px 16px}}
  .sim-icon{{width:48px;height:48px;font-size:1.4em}}
  .sim-launch{{grid-column:1/-1;justify-content:center;margin-top:6px}}
}}
</style>
</head>
<body>
<div class="c">
<a href="index.html" class="nb">← Retour au chapitre</a>

<div class="sim-hero">
  <span class="ch-num">CHAPITRE {chapter_num} · SIMULATIONS</span>
  <h1>{title_html} — Simulations interactives</h1>
  <p class="sub">{sous_titre_safe}</p>
  <div class="meta">{n} simulation{plural_disponibles} disponible{plural_disponibles}</div>
</div>

<div class="intro-pedago">
  <strong>Comment utiliser cette page&nbsp;?</strong> Chaque simulation ci-dessous illustre une notion du chapitre. Tu peux les utiliser <em>avant</em> le cours pour découvrir, <em>pendant</em> pour vérifier ce que tu lis, ou <em>après</em> pour t'entraîner avec différents cas. Les manipulations sont sans risque&nbsp;: explore, observe, raisonne.
</div>

<div class="sim-list">

{cards_html}
</div>

<div class="ch-footer-nav">
  <a href="index.html" class="nb">← Sommaire du chapitre</a>
  <a href="../../../simulations.html" class="nb">Toutes les simulations du site →</a>
</div>

</div>
<script src="../../../nav.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Boucle principale
# ---------------------------------------------------------------------------


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    generated = 0
    skipped = 0
    missing_lecon = 0

    for chapter_path, data in CHAPTER_SIMS.items():
        sims = data.get("sims", [])
        pedagogy = data.get("pedagogy", {})
        if not sims:
            skipped += 1
            continue

        chapter_dir = repo_root / chapter_path
        lecon = chapter_dir / "lecon.html"
        if not lecon.exists():
            print(f"  ⚠  {chapter_path}: lecon.html absent")
            missing_lecon += 1
            continue

        section = get_section_path(chapter_path)
        theme = THEMES.get(section)
        if not theme:
            print(f"  ⚠  {chapter_path}: thème inconnu pour section {section}")
            skipped += 1
            continue

        lecon_text = lecon.read_text(encoding="utf-8")
        meta = extract_chapter_meta(lecon_text, chapter_path)

        # Vérification : toutes les sims listées sont-elles dans SIMULATIONS ?
        unknown = [s for s in sims if s not in SIMULATIONS]
        if unknown:
            print(f"  ⚠  {chapter_path}: simulations inconnues {unknown}")

        html_content = render_simulation_page(
            chapter_num=meta["num"],
            chapter_title=meta["title"],
            sous_titre=meta["sous_titre"],
            sims=sims,
            pedagogy=pedagogy,
            theme=theme,
        )

        out = chapter_dir / "simulation.html"
        out.write_text(html_content, encoding="utf-8")
        generated += 1

    print(f"\n✓ {generated} pages générées · {skipped} skippées · {missing_lecon} sans lecon.html")


if __name__ == "__main__":
    main()
