#!/usr/bin/env python3
"""
Génère un index.html pour chaque chapitre du site.
- Extrait dynamiquement titre, sous-titre, objectifs depuis lecon.html
- Détecte automatiquement les ressources présentes
- Gère les thèmes couleurs par section (variables --p, --p-bg, --p-border)
- Construit la navigation chapitre précédent / chapitre suivant
"""

from __future__ import annotations

import glob
import os
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration des sections : (chemin, sommaire par défaut, thème, libellé)
# ---------------------------------------------------------------------------

SECTIONS = [
    {
        "path": "maths/seconde",
        "default_sommaire": "maths-2nde-mama.html",
        "label_sommaire": "Sommaire 2nde MAMA",
        "theme": ("#0056b3", "#ebf5ff", "#bee3f8"),
        "depth": 3,  # ../../../ pour remonter à la racine
    },
    {
        "path": "maths/premiere",
        "default_sommaire": "maths-1ere-pro.html",
        "label_sommaire": "Sommaire 1ère Pro",
        "theme": ("#0969da", "#dbeafe", "#93c5fd"),
        "depth": 3,
    },
    {
        "path": "maths/terminale",
        "default_sommaire": "maths-term-iccer.html",
        "label_sommaire": "Sommaire Terminale",
        "theme": ("#0969da", "#dbeafe", "#93c5fd"),
        "depth": 3,
    },
    {
        "path": "maths/lgt-terminale",
        "default_sommaire": "maths-lgt-terminale.html",
        "label_sommaire": "Sommaire LGT Terminale",
        "theme": ("#4f46e5", "#eef2ff", "#a5b4fc"),
        "depth": 3,
    },
    {
        "path": "maths/cap",
        "default_sommaire": "maths-cap.html",
        "label_sommaire": "Sommaire CAP",
        "theme": ("#b45309", "#fffbeb", "#fde68a"),
        "depth": 3,
    },
    {
        "path": "maths/bts",
        "default_sommaire": "maths-bts.html",
        "label_sommaire": "Sommaire BTS",
        "theme": ("#0969da", "#dbeafe", "#93c5fd"),
        "depth": 3,
    },
    {
        "path": "physique-chimie/seconde",
        "default_sommaire": "pc-2nde-pro.html",
        "label_sommaire": "Sommaire PC 2nde",
        "theme": ("#6f42c1", "#f5f0ff", "#c4b5fd"),
        "depth": 3,
    },
    {
        "path": "physique-chimie/premiere-iccer",
        "default_sommaire": "pc-1ere-iccer.html",
        "label_sommaire": "Sommaire PC 1ère ICCER",
        "theme": ("#0969da", "#dbeafe", "#93c5fd"),
        "depth": 3,
    },
    {
        "path": "physique-chimie/premiere-era",
        "default_sommaire": "pc-1ere-erama.html",
        "label_sommaire": "Sommaire PC 1ère ERA",
        "theme": ("#2da44e", "#f0fff4", "#86efac"),
        "depth": 3,
    },
    {
        "path": "physique-chimie/terminale-iccer",
        "default_sommaire": "pc-term-iccer.html",
        "label_sommaire": "Sommaire PC Term ICCER",
        "theme": ("#0969da", "#dbeafe", "#93c5fd"),
        "depth": 3,
    },
    {
        "path": "physique-chimie/terminale-era",
        "default_sommaire": "pc-term-erama.html",
        "label_sommaire": "Sommaire PC Term ERA",
        "theme": ("#2da44e", "#f0fff4", "#86efac"),
        "depth": 3,
    },
    {
        "path": "physique-chimie/cap",
        "default_sommaire": "pc-cap.html",
        "label_sommaire": "Sommaire PC CAP",
        "theme": ("#6f42c1", "#f5f0ff", "#c4b5fd"),
        "depth": 3,
    },
]

# ---------------------------------------------------------------------------
# Métadonnées par type de ressource (titre, icône, description, tag)
# ---------------------------------------------------------------------------

RESOURCES = {
    "activite.html": {
        "title": "Activité de découverte",
        "icon": "🧭",
        "description": "Situation-problème guidée pour aborder la notion par un cas concret.",
        "tag": "~30 min",
        "section": "decouvrir",
    },
    "lecon.html": {
        "title": "Cours",
        "icon": "📘",
        "description": "Définitions, propriétés, méthodes et exemples résolus.",
        "tag": "Référence",
        "section": "decouvrir",
        "featured": True,
    },
    "fiche.html": {
        "title": "Fiche de révision",
        "icon": "📑",
        "description": "Mémo synthétique : formules clés, méthodes, à imprimer.",
        "tag": "~5 min",
        "section": "decouvrir",
    },
    "exercices.html": {
        "title": "Exercices",
        "icon": "✏️",
        "description": "Exercices d'entraînement avec corrections détaillées.",
        "tag": "Pratique",
        "section": "entrainer",
    },
    "exercices-capacites.html": {
        "title": "Exercices par capacités",
        "icon": "🎯",
        "description": "Exercices organisés selon les capacités du programme officiel.",
        "tag": "Programme",
        "section": "entrainer",
    },
    "qcm.html": {
        "title": "QCM interactif",
        "icon": "✅",
        "description": "Auto-évaluation interactive avec correction automatique et score.",
        "tag": "~10 min",
        "section": "evaluer",
    },
    "interro.html": {
        "title": "Interrogation",
        "icon": "📝",
        "description": "Évaluation courte chronométrée, barème /20.",
        "tag": "~15 min",
        "section": "evaluer",
    },
    "ds.html": {
        "title": "Devoir surveillé",
        "icon": "🎓",
        "description": "Évaluation complète avec barème détaillé et correction.",
        "tag": "1 h",
        "section": "evaluer",
    },
    "simulation.html": {
        "title": "Simulation interactive",
        "icon": "🔬",
        "description": "Manipulation d'un modèle interactif lié au chapitre.",
        "tag": "Interactif",
        "section": "decouvrir",
    },
}

# Adaptations dynamiques : exercices.html pour Bac Pro = différencié, BTS = simple
ENTRAINER_DIFF = {
    "title": "Exercices",
    "icon": "✏️",
    "description": "Exercices différenciés (socle, standard, approfondissement) avec corrections.",
    "tag": "3 niveaux",
    "section": "entrainer",
}


# ---------------------------------------------------------------------------
# Extraction des métadonnées depuis lecon.html
# ---------------------------------------------------------------------------

H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
SOUS_TITRE_RE = re.compile(r'<p\s+class="sous-titre"[^>]*>(.*?)</p>', re.DOTALL)
OBJECTIFS_RE = re.compile(
    r'<div\s+class="objectifs"[^>]*>(.*?)</div>', re.DOTALL
)
LI_RE = re.compile(r"<li[^>]*>(.*?)</li>", re.DOTALL)
RETOUR_RE = re.compile(
    r'<a\s+href="(\.\./){0,5}([^"]*?\.html)"\s+class="nb"[^>]*>\s*←\s*RETOUR\s*SOMMAIRE',
    re.IGNORECASE,
)
RETOUR_RE2 = re.compile(
    r'<a\s+href="(\.\./){0,5}([^"]*?\.html)"\s+class="nb"[^>]*>\s*←\s*Retour\s+au\s+sommaire',
    re.IGNORECASE,
)

CHAPITRE_NUM_RE = re.compile(
    r"(?:chapitre|ch)\s*0*(\d+)",
    re.IGNORECASE,
)


import html as _html


def strip_html(s: str) -> str:
    """Retire les tags HTML d'une chaîne et décode les entités."""
    s = re.sub(r"<[^>]+>", "", s)
    s = _html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract_title(s: str) -> str:
    """Extrait le titre principal (sans le numéro de chapitre)."""
    m = H1_RE.search(s)
    if not m:
        return ""
    raw = strip_html(m.group(1))
    # Retire "Chapitre X –" / "Ch01 -" / etc.
    cleaned = re.sub(
        r"^(?:chapitre|ch)\s*0*\d+\s*[–\-—:]\s*",
        "",
        raw,
        flags=re.IGNORECASE,
    )
    return cleaned.strip()


def extract_chapter_num(s: str, fallback: str) -> int:
    """Extrait le numéro de chapitre depuis h1 ou utilise le nom de dossier."""
    m = H1_RE.search(s)
    if m:
        m2 = CHAPITRE_NUM_RE.search(strip_html(m.group(1)))
        if m2:
            return int(m2.group(1))
    # Fallback sur le nom du dossier (chXX → XX)
    m3 = re.search(r"ch(\d+)", fallback)
    if m3:
        return int(m3.group(1))
    return 0


def extract_sous_titre(s: str) -> str:
    m = SOUS_TITRE_RE.search(s)
    if not m:
        return ""
    return strip_html(m.group(1))


def extract_objectifs(s: str) -> list[str]:
    m = OBJECTIFS_RE.search(s)
    if not m:
        return []
    inner = m.group(1)
    items = LI_RE.findall(inner)
    return [strip_html(li) for li in items]


def extract_sommaire(s: str, default: str) -> str:
    """Extrait le href de la balise '← RETOUR SOMMAIRE' si présent."""
    for pat in (RETOUR_RE, RETOUR_RE2):
        m = pat.search(s)
        if m:
            return m.group(2)
    return default


# ---------------------------------------------------------------------------
# Construction du HTML
# ---------------------------------------------------------------------------


def html_escape(text: str) -> str:
    """Échappe les caractères critiques tout en préservant les accents."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_card(file_name: str, meta: dict) -> str:
    """Rend une carte ressource."""
    classes = "ress-card"
    if meta.get("featured"):
        classes += " featured"
    return f"""    <a href="{file_name}" class="{classes}">
      <span class="icon">{meta['icon']}</span>
      <p class="title">{meta['title']}</p>
      <p class="desc">{meta['description']}</p>
      <span class="tag">{meta['tag']}</span>
    </a>
"""


def render_section(name: str, title: str, cards: list[str]) -> str:
    if not cards:
        return ""
    grid = "".join(cards)
    return f"""<div class="ress-section">
  <h2>{title}</h2>
  <div class="ress-grid">
{grid}  </div>
</div>

"""


def render_objectifs(objectifs: list[str]) -> str:
    if not objectifs:
        return ""
    items = "\n".join(f"    <li>{html_escape(o)}</li>" for o in objectifs)
    return f"""<div class="ch-objectifs">
  <strong>Objectifs du chapitre</strong>
  <ul>
{items}
  </ul>
</div>

"""


def render_meta_badges(num_resources: int, sous_titre: str) -> str:
    """Construit la barre méta du hero (compteur + niveau)."""
    parts = [f"{num_resources} ressource{'s' if num_resources > 1 else ''}"]
    if sous_titre:
        # On peut découper le sous-titre par séparateurs courants
        for sep in ("|", "•", "·"):
            if sep in sous_titre:
                tokens = [t.strip() for t in sous_titre.split(sep) if t.strip()]
                # Évite de dupliquer le niveau déjà en hero
                tokens = [t for t in tokens if t not in (sous_titre,)]
                parts.extend(tokens[1:])  # On saute le 1er token (souvent le niveau redondant)
                break
    return "".join(f"<span>{html_escape(p)}</span>" for p in parts)


def render_index(
    *,
    chapter_num: int,
    chapter_title: str,
    sous_titre: str,
    objectifs: list[str],
    resources: list[str],  # noms de fichiers présents
    sommaire_href: str,
    sommaire_label: str,
    theme: tuple[str, str, str],
    prev_link: tuple[str, str] | None,
    next_link: tuple[str, str] | None,
    chapter_dir_name: str,
    section_path: str,
) -> str:
    """Construit le HTML complet de l'index d'un chapitre."""
    p, p_bg, p_border = theme

    # Adaptations contextuelles : si Bac Pro Seconde/1ère/Terminale et exercices.html présent,
    # utiliser la version "3 niveaux"
    is_bac_pro = any(
        section_path.startswith(s)
        for s in (
            "maths/seconde",
            "maths/premiere",
            "maths/terminale",
            "physique-chimie/seconde",
            "physique-chimie/premiere",
            "physique-chimie/terminale",
        )
    )

    # Préparation des cartes par section
    sections_cards: dict[str, list[str]] = {
        "decouvrir": [],
        "entrainer": [],
        "evaluer": [],
    }
    # Ordre canonique
    order = [
        "activite.html",
        "lecon.html",
        "fiche.html",
        "exercices.html",
        "exercices-capacites.html",
        "simulation.html",
        "qcm.html",
        "interro.html",
        "ds.html",
    ]

    for fname in order:
        if fname not in resources:
            continue
        if fname == "exercices.html" and is_bac_pro:
            meta = ENTRAINER_DIFF
        else:
            meta = RESOURCES[fname]
        sections_cards[meta["section"]].append(render_card(fname, meta))

    sections_html = (
        render_section("decouvrir", "Découvrir et apprendre", sections_cards["decouvrir"])
        + render_section("entrainer", "S'entraîner", sections_cards["entrainer"])
        + render_section("evaluer", "S'évaluer", sections_cards["evaluer"])
    )

    objectifs_html = render_objectifs(objectifs)

    # Hero meta
    nb = sum(len(v) for v in sections_cards.values())
    meta_html = f"<span>{nb} ressource{'s' if nb > 1 else ''}</span>"

    # Footer navigation
    nav_left = (
        f'<a href="../../../{sommaire_href}" class="nb">← {html_escape(sommaire_label)}</a>'
    )
    if prev_link:
        nav_left = (
            f'<a href="{prev_link[0]}" class="nb">← Chapitre précédent : {html_escape(prev_link[1])}</a>'
        )
    nav_right = (
        f'<a href="../../../{sommaire_href}" class="nb">↑ Retour au sommaire</a>'
    )
    if next_link:
        nav_right = (
            f'<a href="{next_link[0]}" class="nb">Chapitre suivant : {html_escape(next_link[1])} →</a>'
        )

    title_html = html_escape(chapter_title) if chapter_title else f"Chapitre {chapter_num}"
    sous_titre_safe = html_escape(sous_titre)
    page_title = f"Ch{chapter_num:02d} – {title_html} – Sommaire du chapitre"

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

.ch-hero{{
  background:linear-gradient(135deg,var(--p) 0%,#0a4f9c 100%);
  color:#fff;border-radius:14px;padding:32px 28px;margin:18px 0 28px;
  box-shadow:0 6px 20px rgba(0,0,0,.12)
}}
.ch-hero .ch-num{{
  display:inline-block;background:rgba(255,255,255,.2);
  border:1px solid rgba(255,255,255,.4);border-radius:8px;
  padding:4px 14px;font-size:.85em;font-weight:700;letter-spacing:.5px
}}
.ch-hero h1{{margin:14px 0 8px;color:#fff;font-size:1.8em;line-height:1.2}}
.ch-hero .sub{{opacity:.92;font-size:.95em;margin:0}}
.ch-hero .meta{{margin-top:14px;display:flex;gap:18px;flex-wrap:wrap;font-size:.85em;opacity:.92}}
.ch-hero .meta span::before{{content:"• ";opacity:.6}}
.ch-hero .meta span:first-child::before{{content:""}}

.ch-objectifs{{
  background:var(--p-bg);border-left:4px solid var(--p);
  padding:16px 22px;border-radius:0 10px 10px 0;margin:0 0 30px
}}
.ch-objectifs strong{{color:var(--p);display:block;margin-bottom:6px}}
.ch-objectifs ul{{margin:6px 0 0;padding-left:22px}}
.ch-objectifs li{{margin:3px 0}}

.ress-section{{margin:30px 0 18px}}
.ress-section h2{{margin:0 0 14px;color:var(--p);font-size:1.15em;font-weight:700;border:none;padding:0}}

.ress-grid{{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(230px,1fr));
  gap:14px
}}

.ress-card{{
  display:block;text-decoration:none;color:inherit;
  background:#fff;border:1px solid #e2e8f0;border-radius:10px;
  padding:16px 18px;transition:all .15s ease;
  position:relative;overflow:hidden
}}
.ress-card:hover{{
  border-color:var(--p);transform:translateY(-2px);
  box-shadow:0 6px 16px rgba(0,0,0,.10)
}}
.ress-card .icon{{font-size:1.6em;line-height:1;margin-bottom:10px;display:block}}
.ress-card .title{{font-weight:700;color:var(--p);font-size:1.02em;margin:0 0 4px}}
.ress-card .desc{{font-size:.83em;color:#4a5568;line-height:1.4;margin:0}}
.ress-card .tag{{
  display:inline-block;background:var(--p-bg);color:var(--p);
  border:1px solid var(--p-border);border-radius:4px;
  padding:1px 7px;font-size:.7em;font-weight:600;
  margin-top:8px;text-transform:uppercase;letter-spacing:.3px
}}
.ress-card.featured{{border-width:2px;border-color:var(--p)}}
.ress-card.featured::before{{
  content:"";position:absolute;top:0;left:0;right:0;height:3px;
  background:var(--p)
}}

.ch-footer-nav{{
  display:flex;justify-content:space-between;align-items:center;
  margin-top:36px;padding-top:18px;border-top:1px solid #e2e8f0;
  font-size:.88em;flex-wrap:wrap;gap:12px
}}
.ch-footer-nav a{{color:var(--p);text-decoration:none;font-weight:600}}
.ch-footer-nav a:hover{{text-decoration:underline}}

@media(max-width:600px){{
  .ch-hero{{padding:22px 18px}}
  .ch-hero h1{{font-size:1.4em}}
  .ress-grid{{grid-template-columns:1fr 1fr;gap:10px}}
  .ress-card{{padding:12px 14px}}
}}
</style>
</head>
<body>
<div class="c">
<a href="../../../{sommaire_href}" class="nb">← {html_escape(sommaire_label)}</a>

<div class="ch-hero">
  <span class="ch-num">CHAPITRE {chapter_num}</span>
  <h1>{title_html}</h1>
  <p class="sub">{sous_titre_safe}</p>
  <div class="meta">{meta_html}</div>
</div>

{objectifs_html}{sections_html}<div class="ch-footer-nav">
  {nav_left}
  {nav_right}
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
    os.chdir(repo_root)

    total_generated = 0
    total_skipped = 0

    for sec in SECTIONS:
        chapter_paths = sorted(glob.glob(f"{sec['path']}/ch*"))
        # Pré-extraction des titres pour la nav prev/next
        chapter_meta: list[dict] = []
        for ch_path in chapter_paths:
            lecon_path = Path(ch_path) / "lecon.html"
            if not lecon_path.exists():
                chapter_meta.append({
                    "path": ch_path,
                    "num": int(re.search(r"ch(\d+)", ch_path).group(1)),
                    "title": "",
                    "lecon_text": "",
                })
                continue
            text = lecon_path.read_text(encoding="utf-8")
            chapter_meta.append({
                "path": ch_path,
                "num": extract_chapter_num(text, ch_path),
                "title": extract_title(text),
                "lecon_text": text,
            })

        for i, ch in enumerate(chapter_meta):
            ch_path = ch["path"]
            num = ch["num"]
            title = ch["title"]
            lecon_text = ch["lecon_text"]

            if not lecon_text:
                # Pas de lecon.html → on skip ce chapitre
                total_skipped += 1
                print(f"  SKIP {ch_path} (pas de lecon.html)")
                continue

            sous_titre = extract_sous_titre(lecon_text)
            objectifs = extract_objectifs(lecon_text)
            sommaire = extract_sommaire(lecon_text, sec["default_sommaire"])

            # Détection des ressources présentes
            files_in_dir = set(p.name for p in Path(ch_path).iterdir() if p.is_file())
            resources = [name for name in RESOURCES if name in files_in_dir]

            # Navigation chapitre prev/next
            prev_link = None
            next_link = None
            if i > 0:
                prev_ch = chapter_meta[i - 1]
                prev_dir = Path(prev_ch["path"]).name
                prev_link = (f"../{prev_dir}/index.html", prev_ch["title"] or f"Chapitre {prev_ch['num']}")
            if i < len(chapter_meta) - 1:
                next_ch = chapter_meta[i + 1]
                next_dir = Path(next_ch["path"]).name
                next_link = (f"../{next_dir}/index.html", next_ch["title"] or f"Chapitre {next_ch['num']}")

            html = render_index(
                chapter_num=num,
                chapter_title=title,
                sous_titre=sous_titre,
                objectifs=objectifs,
                resources=resources,
                sommaire_href=sommaire,
                sommaire_label=sec["label_sommaire"],
                theme=sec["theme"],
                prev_link=prev_link,
                next_link=next_link,
                chapter_dir_name=Path(ch_path).name,
                section_path=sec["path"],
            )

            output = Path(ch_path) / "index.html"
            output.write_text(html, encoding="utf-8")
            total_generated += 1

        print(f"  {sec['path']}: {len(chapter_meta)} chapitres")

    print(f"\n✓ Total : {total_generated} index générés, {total_skipped} skippés")


if __name__ == "__main__":
    main()
