#!/usr/bin/env python3
"""Génère les pages d'accueil de chapitre (index.html).

Pour un chapitre donné, lit le lecon.html pour extraire titre, sous-titre,
objectifs, couleur thème, puis génère un index.html portail listant les
ressources réellement présentes dans le dossier.

Usage:
    python3 scripts/generate_chapter_index.py physique-chimie/premiere-gpt2/ch01
    python3 scripts/generate_chapter_index.py physique-chimie/premiere-gpt2
    python3 scripts/generate_chapter_index.py --force <path>
    python3 scripts/generate_chapter_index.py --dry-run <path>

Règles : voir prompts/prompt-index-chapitre.md
"""

import os
import re
import sys

# Mapping section → URL du sommaire matière
SOMMAIRES = {
    "maths/seconde": "maths-2nde-mama.html",
    "maths/premiere": "maths-1ere-pro.html",
    "maths/terminale": "maths-term-iccer.html",
    "maths/lgt-terminale": "maths-lgt-terminale.html",
    "maths/cap": "maths-cap.html",
    "maths/bts": "maths-bts.html",
    "physique-chimie/seconde": "pc-2nde-pro.html",
    "physique-chimie/premiere-iccer": "pc-1ere-iccer.html",
    "physique-chimie/premiere-era": "pc-1ere-erama.html",
    "physique-chimie/premiere-gpt2": "pc-1ere-gpt2.html",
    "physique-chimie/premiere-gpt4": "pc-1ere-gpt4.html",
    "physique-chimie/premiere-gpt6": "pc-1ere-gpt6.html",
    "physique-chimie/terminale-iccer": "pc-term-iccer.html",
    "physique-chimie/terminale-era": "pc-term-erama.html",
    "physique-chimie/terminale-gpt2": "pc-term-gpt2.html",
    "physique-chimie/terminale-gpt4": "pc-term-gpt4.html",
    "physique-chimie/terminale-gpt5": "pc-term-gpt5.html",
    "physique-chimie/cap": "pc-cap.html",
}

# Libellés des sommaires (utilisés dans le lien retour)
SOMMAIRE_LABEL = {
    "maths/seconde": "Sommaire 2de MAMA",
    "maths/premiere": "Sommaire 1re Pro",
    "maths/terminale": "Sommaire Terminale",
    "maths/lgt-terminale": "Sommaire LGT Term",
    "maths/cap": "Sommaire CAP",
    "maths/bts": "Sommaire BTS",
    "physique-chimie/seconde": "Sommaire PC 2nde",
    "physique-chimie/premiere-iccer": "Sommaire 1re ICCER",
    "physique-chimie/premiere-era": "Sommaire 1re ERA-MA",
    "physique-chimie/premiere-gpt2": "Sommaire 1re Grpt 2",
    "physique-chimie/premiere-gpt4": "Sommaire 1re Grpt 4",
    "physique-chimie/premiere-gpt6": "Sommaire 1re Grpt 6",
    "physique-chimie/terminale-iccer": "Sommaire Term ICCER",
    "physique-chimie/terminale-era": "Sommaire Term ERA-MA",
    "physique-chimie/terminale-gpt2": "Sommaire Term Grpt 2",
    "physique-chimie/terminale-gpt4": "Sommaire Term Grpt 4",
    "physique-chimie/terminale-gpt5": "Sommaire Term Grpt 5",
    "physique-chimie/cap": "Sommaire PC CAP",
}

# Définition des cartes par section
RESSOURCES = [
    # (filename, section_titre, icon, title, desc, tag, featured)
    ("activite.html", "Découvrir et apprendre", "🧭", "Activité de découverte",
     "Situation-problème guidée pour aborder la notion par un cas concret.",
     "~30 min", False),
    ("lecon.html", "Découvrir et apprendre", "📘", "Cours",
     "Définitions, propriétés, méthodes et exemples résolus.",
     "Référence", True),
    ("fiche.html", "Découvrir et apprendre", "📑", "Fiche de révision",
     "Mémo synthétique : formules clés, méthodes, à imprimer.",
     "~5 min", False),
    ("simulation.html", "Découvrir et apprendre", "🔬", "Simulation interactive",
     "Manipulation d'un modèle interactif lié au chapitre.",
     "Interactif", False),
    ("exercices.html", "S'entraîner", "✏️", "Exercices",
     "Exercices différenciés (socle, standard, approfondissement) avec corrections.",
     "3 niveaux", False),
    ("exercices-capacites.html", "S'entraîner", "🎯", "Exercices par capacités",
     "Exercices organisés selon les capacités du programme officiel.",
     "Programme", False),
    ("qcm.html", "S'évaluer", "✅", "QCM interactif",
     "Auto-évaluation interactive avec correction automatique et score.",
     "~10 min", False),
    ("interro.html", "S'évaluer", "📝", "Interrogation",
     "Évaluation courte chronométrée, barème /20.",
     "~15 min", False),
    ("ds.html", "S'évaluer", "🎓", "Devoir surveillé",
     "Évaluation complète avec barème détaillé et correction.",
     "1 h", False),
]


def extract_section(chapter_path: str) -> str:
    """Retourne par exemple 'physique-chimie/premiere-gpt2'."""
    parts = chapter_path.split(os.sep)
    if len(parts) >= 3:
        return f"{parts[0]}/{parts[1]}"
    return ""


def extract_from_lecon(lecon_path: str) -> dict:
    """Extrait titre, sous-titre, objectifs et variables CSS depuis lecon.html."""
    with open(lecon_path, encoding="utf-8") as f:
        html = f.read()

    # Couleur thème
    css_match = re.search(r":root\{(--p:[^}]+)\}", html)
    css_vars = css_match.group(1) if css_match else "--p:#0056b3;--p-bg:#ebf5ff;--p-border:#bee3f8"

    # Titre h1 (première occurrence)
    h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.DOTALL)
    h1 = h1_match.group(1).strip() if h1_match else "Chapitre"
    # Retire balises internes éventuelles (ex: <span>)
    h1 = re.sub(r"<[^>]+>", "", h1).strip()
    # Retire le préfixe "Chapitre N – " ou "ChN – " pour avoir juste le titre
    title = re.sub(r"^(Chapitre|Ch)\s*\d+\s*[–\-—]\s*", "", h1).strip()

    # Sous-titre
    sub_match = re.search(r'<p class="sous-titre">([^<]+)</p>', html)
    sous_titre = sub_match.group(1).strip() if sub_match else ""

    # Objectifs : le premier <ul> dans <div class="objectifs">
    obj_match = re.search(
        r'<div class="objectifs">.*?<ul[^>]*>(.*?)</ul>',
        html, flags=re.DOTALL,
    )
    objectifs = []
    if obj_match:
        ul = obj_match.group(1)
        for li in re.findall(r"<li[^>]*>(.*?)</li>", ul, flags=re.DOTALL):
            objectifs.append(li.strip())

    return {
        "css_vars": css_vars,
        "title": title,
        "sous_titre": sous_titre,
        "objectifs": objectifs,
    }


def get_chapter_number(chapter_dir: str) -> int:
    """Extrait le numéro de chN."""
    base = os.path.basename(chapter_dir)
    m = re.match(r"ch0*(\d+)", base)
    return int(m.group(1)) if m else 0


def find_neighbours(chapter_dir: str):
    """Retourne (prev_dir, next_dir) où chacun est None ou le path d'un dossier voisin."""
    parent = os.path.dirname(chapter_dir)
    siblings = sorted(
        [d for d in os.listdir(parent) if d.startswith("ch") and os.path.isdir(os.path.join(parent, d))]
    )
    base = os.path.basename(chapter_dir)
    if base not in siblings:
        return None, None
    idx = siblings.index(base)
    prev = os.path.join(parent, siblings[idx - 1]) if idx > 0 else None
    nxt = os.path.join(parent, siblings[idx + 1]) if idx < len(siblings) - 1 else None
    return prev, nxt


def get_neighbour_title(neighbour_dir: str) -> str:
    if neighbour_dir is None:
        return ""
    lecon = os.path.join(neighbour_dir, "lecon.html")
    if not os.path.isfile(lecon):
        return ""
    info = extract_from_lecon(lecon)
    return info["title"]


def render_card(filename, icon, title, desc, tag, featured: bool) -> str:
    extra_class = " featured" if featured else ""
    return f'''    <a href="{filename}" class="ress-card{extra_class}">
      <span class="icon">{icon}</span>
      <p class="title">{title}</p>
      <p class="desc">{desc}</p>
      <span class="tag">{tag}</span>
    </a>'''


STYLE_BLOCK = """\
:root{{{css_vars}}}

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
}}\
"""


def render_index(chapter_dir: str) -> str:
    section = extract_section(chapter_dir)
    sommaire_url = f"../../../{SOMMAIRES.get(section, 'index.html')}"
    sommaire_label = SOMMAIRE_LABEL.get(section, "Sommaire")

    lecon_path = os.path.join(chapter_dir, "lecon.html")
    info = extract_from_lecon(lecon_path)

    chapter_num = get_chapter_number(chapter_dir)

    # Détecter ressources présentes
    cards_by_section = {"Découvrir et apprendre": [], "S'entraîner": [], "S'évaluer": []}
    n_resources = 0
    for filename, sec, icon, title, desc, tag, featured in RESSOURCES:
        if os.path.isfile(os.path.join(chapter_dir, filename)):
            cards_by_section[sec].append(render_card(filename, icon, title, desc, tag, featured))
            n_resources += 1

    # Voisins
    prev_dir, next_dir = find_neighbours(chapter_dir)
    prev_title = get_neighbour_title(prev_dir) if prev_dir else ""
    next_title = get_neighbour_title(next_dir) if next_dir else ""

    nav_parts = []
    if prev_dir:
        prev_basename = os.path.basename(prev_dir)
        nav_parts.append(
            f'  <a href="../{prev_basename}/index.html" class="nb">'
            f'← Chapitre précédent : {prev_title}</a>'
        )
    if next_dir:
        nxt_basename = os.path.basename(next_dir)
        nav_parts.append(
            f'  <a href="../{nxt_basename}/index.html" class="nb">'
            f'Chapitre suivant : {next_title} →</a>'
        )
    footer_nav = "\n".join(nav_parts) if nav_parts else ""

    # Construction des sections
    sections_html = []
    for sec_label in ["Découvrir et apprendre", "S'entraîner", "S'évaluer"]:
        cards = cards_by_section[sec_label]
        if not cards:
            continue
        sections_html.append(f'''<div class="ress-section">
  <h2>{sec_label}</h2>
  <div class="ress-grid">
{chr(10).join(cards)}
  </div>
</div>''')
    sections_block = "\n\n".join(sections_html)

    objectifs_html = "\n".join(f"    <li>{o}</li>" for o in info["objectifs"])

    style = STYLE_BLOCK.format(css_vars=info["css_vars"])

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Ch{chapter_num:02d} – {info["title"]} – Sommaire du chapitre</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>
{style}
</style>
</head>
<body>
<div class="c">
<a href="{sommaire_url}" class="nb">← {sommaire_label}</a>

<div class="ch-hero">
  <span class="ch-num">CHAPITRE {chapter_num}</span>
  <h1>{info["title"]}</h1>
  <p class="sub">{info["sous_titre"]}</p>
  <div class="meta"><span>{n_resources} ressources</span></div>
</div>

<div class="ch-objectifs">
  <strong>Objectifs du chapitre</strong>
  <ul>
{objectifs_html}
  </ul>
</div>

{sections_block}

<div class="ch-footer-nav">
{footer_nav}
</div>

</div>
<script src="../../../nav.js"></script>
</body>
</html>
'''


def is_chapter_dir(path: str) -> bool:
    return (
        os.path.isdir(path)
        and re.match(r"ch\d+$", os.path.basename(path))
        and os.path.isfile(os.path.join(path, "lecon.html"))
    )


def main():
    args = sys.argv[1:]
    force = False
    dry_run = False
    while args and args[0].startswith("--"):
        if args[0] == "--force":
            force = True
        elif args[0] == "--dry-run":
            dry_run = True
        else:
            print(f"Option inconnue : {args[0]}")
            sys.exit(1)
        args = args[1:]

    if not args:
        print(__doc__)
        sys.exit(1)

    target = args[0]

    chapter_dirs = []
    if is_chapter_dir(target):
        chapter_dirs = [target]
    elif os.path.isdir(target):
        for entry in sorted(os.listdir(target)):
            full = os.path.join(target, entry)
            if is_chapter_dir(full):
                chapter_dirs.append(full)
    else:
        print(f"Cible introuvable ou pas un chapitre : {target}")
        sys.exit(1)

    if not chapter_dirs:
        print(f"Aucun chapitre trouvé dans {target}")
        sys.exit(1)

    written = 0
    skipped = 0
    for ch in chapter_dirs:
        idx = os.path.join(ch, "index.html")
        exists = os.path.isfile(idx)
        if exists and not force:
            print(f"  [skip]    {idx} existe (utiliser --force pour écraser)")
            skipped += 1
            continue
        try:
            html = render_index(ch)
        except Exception as e:
            print(f"  [erreur]  {ch} : {e}")
            continue
        if dry_run:
            print(f"  [dry-run] {idx} ({len(html)} caractères)")
        else:
            with open(idx, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  [ok]      {idx}")
            written += 1

    print()
    print("=== Résumé ===")
    print(f"Chapitres traités : {len(chapter_dirs)}")
    print(f"index.html créés  : {written}")
    print(f"Ignorés (existant) : {skipped}")


if __name__ == "__main__":
    main()
