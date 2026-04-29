#!/usr/bin/env python3
"""
Met à jour les pages sommaire pour rendre le titre de chaque chapitre cliquable.
Le titre pointera vers le chXX/index.html du chapitre correspondant.

Détection : on cherche les blocs `<div class="chapter-row">` puis on identifie
le chemin du chapitre via le 1er <a href="..."> dans `links-group`.
"""

from __future__ import annotations

import re
from pathlib import Path

SOMMAIRES = [
    "maths-2nde-mama.html",
    "maths-1ere-pro.html",
    "maths-term-iccer.html",
    "maths-term-erama.html",
    "maths-lgt-terminale.html",
    "maths-cap.html",
    "maths-bts.html",
    "pc-2nde-pro.html",
    "pc-1ere-iccer.html",
    "pc-1ere-erama.html",
    "pc-term-iccer.html",
    "pc-term-erama.html",
    "pc-cap.html",
]

# Cherche un bloc chapter-row entier
CHAPTER_ROW_RE = re.compile(
    r'(<div\s+class="chapter-row">.*?</div>\s*</div>)',
    re.DOTALL,
)

# Dans un bloc, trouve le 1er href du links-group
HREF_RE = re.compile(r'href="([^"]+/ch\d+/[^"]+\.html)"')

# Trouve <span class="ch-title">…</span> (sans déjà être un lien)
SPAN_TITLE_RE = re.compile(
    r'(<span\s+class="ch-title">)(.*?)(</span>)',
    re.DOTALL,
)


def chapter_dir_from_href(href: str) -> str:
    """Extrait le chemin de dossier 'maths/seconde/ch01' depuis 'maths/seconde/ch01/lecon.html'."""
    parts = href.rsplit("/", 1)
    return parts[0] if len(parts) == 2 else ""


def transform_block(block: str) -> str:
    """Remplace <span class="ch-title">X</span> par un lien vers index.html."""
    m = HREF_RE.search(block)
    if not m:
        return block
    chapter_dir = chapter_dir_from_href(m.group(1))
    if not chapter_dir:
        return block

    index_url = f"{chapter_dir}/index.html"

    def replace_title(match: re.Match[str]) -> str:
        # Si le titre est déjà un lien (déjà transformé), on ne touche pas
        title_text = match.group(2)
        if "<a " in title_text:
            return match.group(0)
        return (
            f'<a href="{index_url}" class="ch-title-link">'
            f'{match.group(0)}'
            f'</a>'
        )

    return SPAN_TITLE_RE.sub(replace_title, block)


# Bloc CSS à injecter dans chaque sommaire (idempotent)
CSS_SNIPPET = """
        .ch-title-link {
            text-decoration: none;
            color: inherit;
            transition: color 0.15s;
        }
        .ch-title-link:hover .ch-title { color: var(--primary); text-decoration: underline; }"""

CSS_MARKER = ".ch-title-link"


def inject_css(content: str) -> str:
    if CSS_MARKER in content:
        return content
    # On insère avant la première règle @media (max-width:768)
    media_idx = content.find("@media (max-width: 768")
    if media_idx == -1:
        # Fallback : avant </style>
        return content.replace("</style>", CSS_SNIPPET + "\n        </style>", 1)
    insert_pos = content.rfind("\n", 0, media_idx)
    return content[:insert_pos] + "\n" + CSS_SNIPPET + content[insert_pos:]


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    text = CHAPTER_ROW_RE.sub(lambda m: transform_block(m.group(1)), text)
    text = inject_css(text)

    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    changed = 0
    for name in SOMMAIRES:
        p = repo_root / name
        if not p.exists():
            print(f"  SKIP {name} (introuvable)")
            continue
        if process_file(p):
            print(f"  ✓ {name}")
            changed += 1
        else:
            print(f"  − {name} (déjà à jour)")
    print(f"\n{changed} fichier(s) modifié(s)")


if __name__ == "__main__":
    main()
