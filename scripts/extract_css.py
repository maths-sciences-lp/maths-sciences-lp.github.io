#!/usr/bin/env python3
"""
extract_css.py — Retire le CSS générique des fichiers de cours HTML
et le remplace par un lien vers styles.css + un micro <style> de thème.

Usage : python3 scripts/extract_css.py [--dry-run]
"""

import re
import sys
from pathlib import Path

# ── Couleurs primaires par dossier parent (subject/level) ──────────────────
THEME_MAP = {
    "maths/seconde": (
        "--p:#0056b3;--p-bg:#ebf5ff;--p-border:#bee3f8",
        "Maths 2nde"),
    "maths/terminale": (
        "--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd",
        "Maths Terminale"),
    "physique-chimie/seconde": (
        "--p:#6f42c1;--p-bg:#f5f0ff;--p-border:#c4b5fd",
        "PC 2nde"),
    "physique-chimie/terminale-iccer": (
        "--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd",
        "PC Term ICCER"),
    "physique-chimie/terminale-era": (
        "--p:#2da44e;--p-bg:#f0fff4;--p-border:#86efac;--s:#0ea5e9;--s-bg:#e0f2fe;--s-border:#7dd3fc",
        "PC Term ERA"),
}

DRY_RUN = "--dry-run" in sys.argv
ROOT = Path(__file__).parent.parent


# ── Liste de sélecteurs dont les règles sont déjà dans styles.css ─────────
# Chaque entrée est un sélecteur CSS (peut contenir des espaces).
# On matche: sélecteur + éventuels espaces + { + contenu + }
KNOWN_SELECTORS = [
    ":root",
    r"\*,\s*\*::before,\s*\*::after",
    "body",
    r"\.c",
    r"\.container",
    "header",
    "h1", "h2", "h3", "h4",
    r"\.sous-titre", r"\.maj",
    r"\.nb", r"\.nb:hover",
    r"\.nav-footer",
    r"\.nav-footer\s+a", r"\.nav-footer\s+a:hover",
    r"\.nav-bottom",
    r"\.nav-bottom\s+a", r"\.nav-bottom\s+a:hover",
    r"\.nav-btn", r"\.nav-btn:hover",
    r"\.nav-links", r"\.nav-link",
    r"\.nav-back", r"\.nav-fwd", r"\.nav-fwd:hover",
    r"\.def", r"\.def\s+strong",
    r"\.prop", r"\.prop\s+strong",
    r"\.att", r"\.att\s+strong",
    r"\.meth", r"\.meth\s+strong",
    r"\.retenir", r"\.retenir\s+h3", r"\.retenir\s+strong",
    r"\.situation", r"\.situation\s+h3",
    r"\.objectifs", r"\.objectifs\s+ul",
    r"\.appli", r"\.biv",
    r"\.ex", r"\.ex-titre",
    r"\.exo",
    r"\.exo-num", r"\.exo-titre",
    r"\.exo-header", r"\.exo-num-badge", r"\.exo-title",
    r"\.mama-tag",
    r"\.etape", r"\.etape-txt",
    r"\.nc", r"\.num", r"\.guide-num",
    r"\.guide", r"\.guide-step",
    r"\.corr",
    r"\.corr\s+p,\s*\.corr\s+li",
    r"\.corr\s+ul,\s*\.corr\s+ol",
    r"\.corr\s+p", r"\.corr\s+li",
    r"\.corr\s+ul", r"\.corr\s+ol",
    r"\.corr\s+strong",
    r"\.correction",
    r"details\.corr-wrap",
    r"summary\.corr-btn",
    r"summary\.corr-btn::-webkit-details-marker",
    r"\.corr-body", r"\.corr-rep",
    r"details",
    r"details\s+summary",
    r"details\s+summary:hover",
    r"details\s+p",
    r"details\s+summary::-webkit-details-marker",
    r"\.bc", r"\.bc:hover",
    r"\.btn-corr", r"\.btn-corr:hover",
    r"\.bcq", r"\.bcq:hover",
    r"\.qcm-grid",
    r"\.qcm-item",
    r"\.qcm-item\s+strong",
    r"\.qcm-item\s+ul",
    r"\.qcm-item\s+ul\s+li",
    r"\.qcm-item\s+ul\s+li::before",
    r"\.qcm-item\s+ul\s+li\.ok::before",
    r"\.qcm-item\s+ul\s+li\.ok",
    r"\.qcm-item\s+label",
    r"\.qcm-corr",
    r"\.niveau-header",
    r"\.niv1", r"\.niv2", r"\.niv3", r"\.niv4",
    r"\.niv1\s+h2,\s*\.niv2\s+h2,\s*\.niv3\s+h2,\s*\.niv4\s+h2",
    r"\.niv1\s+h2", r"\.niv2\s+h2", r"\.niv3\s+h2", r"\.niv4\s+h2",
    r"\.badge-niv",
    r"\.badge-1", r"\.badge-2", r"\.badge-3", r"\.badge-4",
    r"\.niveau",
    r"\.n1", r"\.n2", r"\.n3", r"\.n4",
    r"\.diff", r"\.diff-1", r"\.diff-2", r"\.diff-3",
    r"table",
    r"table\.full",
    r"th,\s*td",
    r"th", r"td",
    r"td\.tv-x", r"td\.ok", r"td\.hi", r"td\.vide", r"td\.hl",
    r"td:first-child",
    r"tr:nth-child\(even\)\s+td",
    r"\.cell-blank",
    r"\.chart-wrapper", r"\.chart-wrap",
    r"\.chart-wrapper\s+h3", r"\.chart-wrap\s+h3",
    r"\.chart-label",
    r"canvas\.anim",
    r"\.ctrl-vis",
    r"\.ctrl-vis\s+input\[type=range\]",
    r"\.ctrl-vis\s+label",
    r"\.anim-result",
    r"\.anim-wrap",
    r"\.anim-wrap\s+button",
    r"\.anim-wrap\s+button:hover",
    r"\.svg-wrap", r"\.svg-leg",
    r"\.formula-box", r"\.formule-box", r"\.formule",
    r"\.formula-box\s+\.fb-label",
    r"\.formula-box\s+\.fb-formula",
    r"\.formula-box\.green",
    r"\.formula-box\.green\s+\.fb-formula",
    r"\.formula-box\.orange",
    r"\.formula-box\.orange\s+\.fb-formula",
    r"\.formula-box\.red",
    r"\.formula-box\.red\s+\.fb-formula",
    r"\.formule-box\s+small", r"\.formule\s+small",
    r"\.badge",
    r"\.badge-green", r"\.badge-blue", r"\.badge-yellow", r"\.badge-red",
    r"\.label",
    r"\.label-def", r"\.label-prop", r"\.label-att",
    r"\.label-meth", r"\.label-ex", r"\.label-ret", r"\.label-biv",
    r"\.ticcer-badge", r"\.erama-badge", r"\.badge-appro",
    r"\.card-grid",
    r"\.grid2", r"\.two-col", r"\.deux-col",
    r"\.info-grid",
    r"\.info-card",
    r"\.info-card\s+\.val",
    r"\.info-card\s+\.lbl",
    r"\.zone-rep", r"\.reponse-box", r"\.reponse",
    r"\.q", r"\.q-sub",
    r"\.consigne",
    r"\.slider-row",
    r"\.slider-row\s+label",
    r"\.slider-row\s+input\[type=range\]",
    r"\.value-badge",
    r"\.sep", r"\.section-sep",
    r"\.intro-box", r"\.result-box", r"\.ds-head",
    r"\.section-titre", r"\.section-ligne", r"\.section-label",
    r"ul\.styled\s+li",
]

# Construire les patterns regex à partir des sélecteurs
# Chaque règle CSS commence soit en début de texte, soit juste après un '}'
def build_patterns(selectors):
    patterns = []
    for sel in selectors:
        # Ancre : précédé de début de chaîne, }, ou saut de ligne
        p = r'(?:(?:^|(?<=\}))[ \t]*)' + sel + r'[ \t]*\{[^{}]*\}'
        patterns.append(re.compile(p, re.MULTILINE))
    return patterns

COMPILED_PATTERNS = build_patterns(KNOWN_SELECTORS)

# Pattern pour @media avec une règle imbriquée (1 niveau)
MEDIA_CLEANUP = re.compile(r'@media\s*\([^)]+\)\s*\{[^{}]*\{[^{}]*\}[^{}]*\}')


def remove_known_rules(css_text):
    """Retire toutes les règles CSS déjà présentes dans styles.css."""
    result = css_text
    for pat in COMPILED_PATTERNS:
        result = pat.sub('', result)
    # Retirer les @media vides ou ne contenant que des règles connues
    result = MEDIA_CLEANUP.sub('', result)
    # Nettoyer les espaces multiples/lignes vides
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = result.strip()
    return result


def get_theme_key(filepath):
    rel = filepath.relative_to(ROOT)
    parts = rel.parts
    if len(parts) >= 3:
        return f"{parts[0]}/{parts[1]}"
    return None


def get_relative_css_path(filepath):
    depth = len(filepath.relative_to(ROOT).parts) - 1
    return "../" * depth + "styles.css"


def process_file(filepath):
    content = filepath.read_text(encoding='utf-8')

    if 'styles.css' in content:
        return False  # Déjà traité

    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
    if not style_match:
        return False

    original_css = style_match.group(1)
    remaining_css = remove_known_rules(original_css)

    theme_key = get_theme_key(filepath)
    theme_vars, theme_name = THEME_MAP.get(theme_key, ("", ""))
    css_path = get_relative_css_path(filepath)

    link_tag = f'<link rel="stylesheet" href="{css_path}">'

    if remaining_css:
        new_style = f'<style>:root{{{theme_vars}}}\n{remaining_css}</style>'
    elif theme_vars:
        new_style = f'<style>:root{{{theme_vars}}}</style>'
    else:
        new_style = ''

    replacement = link_tag + ('\n' + new_style if new_style else '')

    new_content = re.sub(
        r'<style>.*?</style>',
        replacement,
        content,
        count=1,
        flags=re.DOTALL | re.IGNORECASE
    )

    if new_content == content:
        return False

    size_saved = len(content) - len(new_content)
    print(f"  ✓  {filepath.relative_to(ROOT)}  [{theme_name}]  -{size_saved} octets")

    if not DRY_RUN:
        filepath.write_text(new_content, encoding='utf-8')
    return True


def main():
    print(f"{'[DRY-RUN] ' if DRY_RUN else ''}Extraction CSS en cours...\n")
    html_files = sorted(ROOT.glob("*/*/ch*/*.html"))
    processed = sum(process_file(f) for f in html_files)
    print(f"\n✅ {processed} fichiers traités sur {len(html_files)} fichiers de cours.")
    if DRY_RUN:
        print("(Mode dry-run : aucun fichier modifié)")


if __name__ == "__main__":
    main()
