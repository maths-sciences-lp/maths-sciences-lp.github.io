"""
add_answer_lines.py — Ajoute des zones de réponse (.answer-line) aux exercices.html
                      et exercices-capacites.html.

Structure produite :
  <div class="zone-rep">
    <label>Mes calculs :</label>
    <span class="answer-line"></span>  (× N selon niveau)
  </div>
  <button class="bc" ...>Voir la correction</button>
  <div class="corr">...</div>

toggle() inchangé : btn.nextElementSibling

Usage :
  python3 scripts/add_answer_lines.py maths/seconde/ch05
  python3 scripts/add_answer_lines.py maths/seconde
  python3 scripts/add_answer_lines.py --all

Règles :
  - diff-socle    → 3 lignes
  - diff-standard → 5 lignes
  - diff-appro    → 6 lignes
  - sans diff     → 4 lignes
"""

import re
import sys
import glob
import os

LINES_BY_LEVEL = {
    'diff-socle': 3,
    'diff-standard': 5,
    'diff-appro': 6,
    'none': 4,
}

ANSWER_LINE = '    <span class="answer-line"></span>\n'

# Regex : exo div uniquement (pas exo-header, exo-num, etc.)
EXO_OPEN = re.compile(r'<div class="exo( [^"]+)?">')

# Zone-rep existante (label vide, pas encore de answer-lines)
ZONE_REP_PATTERN = re.compile(
    r'<div class="zone-rep">\s*(<label>[^<]*</label>)?\s*</div>',
    re.DOTALL
)

# Bouton .bc
BC_BTN = re.compile(r'(\s*<button class="bc"[^>]*>Voir la correction</button>)')


def build_zone_rep(n_lines):
    lines = ''.join([ANSWER_LINE] * n_lines)
    return (
        f'  <div class="zone-rep">\n'
        f'    <label>Mes calculs :</label>\n'
        f'{lines}'
        f'  </div>\n'
    )


def process_block(block, n_lines):
    zone_rep = build_zone_rep(n_lines)

    if '<div class="zone-rep">' in block:
        # Remplacer zone-rep existante par version avec answer-lines
        return ZONE_REP_PATTERN.sub(zone_rep.rstrip('\n'), block, count=1)
    else:
        # Insérer zone-rep avant le premier bouton .bc
        return BC_BTN.sub(f'\n{zone_rep}\\1', block, count=1)


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<span class="answer-line"></span>' in content:
        print(f'[skip] {path}')
        return

    result = []
    pos = 0

    for m in EXO_OPEN.finditer(content):
        result.append(content[pos:m.start()])

        classes = m.group(1) or ''
        if 'diff-socle' in classes:
            level = 'diff-socle'
        elif 'diff-standard' in classes:
            level = 'diff-standard'
        elif 'diff-appro' in classes:
            level = 'diff-appro'
        else:
            level = 'none'

        next_m = EXO_OPEN.search(content, m.end())
        end = next_m.start() if next_m else len(content)
        block = content[m.start():end]

        result.append(process_block(block, LINES_BY_LEVEL[level]))
        pos = end

    result.append(content[pos:])
    new_content = ''.join(result)

    if new_content == content:
        print(f'[WARN] aucun changement dans {path}')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'[OK]   {path}')


def collect_files(arg):
    if arg == '--all':
        patterns = [
            'maths/**/exercices.html',
            'maths/**/exercices-capacites.html',
            'physique-chimie/**/exercices.html',
            'physique-chimie/**/exercices-capacites.html',
        ]
    elif os.path.isdir(arg):
        patterns = [
            f'{arg}/exercices.html',
            f'{arg}/exercices-capacites.html',
            f'{arg}/*/exercices.html',
            f'{arg}/*/exercices-capacites.html',
        ]
    else:
        return [arg] if os.path.isfile(arg) else []

    files = []
    for p in patterns:
        files.extend(glob.glob(p, recursive=True))
    return sorted(set(files))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 scripts/add_answer_lines.py <chemin|--all>')
        sys.exit(1)

    files = collect_files(sys.argv[1])
    if not files:
        print('Aucun fichier trouvé.')
        sys.exit(1)

    ok = 0
    for path in files:
        before = open(path, encoding='utf-8').read()
        process_file(path)
        after = open(path, encoding='utf-8').read()
        if before != after:
            ok += 1

    print(f'\n{ok} fichier(s) modifié(s).')
