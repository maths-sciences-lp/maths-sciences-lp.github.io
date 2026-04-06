"""
add_answer_lines.py — Ajoute des zones de réponse (.answer-line) aux exercices.html
                      et exercices-capacites.html.

Structure produite :
  <div class="zone-rep">
    <label>Mes calculs :</label>
    <span class="answer-line"></span>  (× N selon niveau)
    <div class="corr">...</div>        ← correction déplacée à l'intérieur
  </div>
  <button class="bc" ...>Voir la correction</button>

toggle() mis à jour en conséquence :
  var c = btn.previousElementSibling.querySelector('.corr');

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

# Regex : exo div (pas exo-header, exo-num, etc.)
EXO_OPEN = re.compile(r'<div class="exo( [^"]+)?">')

# Regex : bouton .bc
BC_BTN = re.compile(r'\s*<button class="bc"[^>]*>Voir la correction</button>')

# Nouveau toggle() à injecter en fin de fichier
NEW_TOGGLE = (
    'function toggle(btn){\n'
    '  var c=btn.previousElementSibling.querySelector(\'.corr\');\n'
    '  if(c.style.display===\'block\'){c.style.display=\'none\';'
    'btn.textContent=\'Voir la correction\';}\n'
    '  else{c.style.display=\'block\';'
    'btn.textContent=\'Masquer la correction\';}\n'
    '}'
)

OLD_TOGGLE = re.compile(
    r'function toggle\(btn\)\{[^}]*\}',
    re.DOTALL
)


def div_end(text, start):
    """Retourne la position après </div> fermant le <div> ouvert à start."""
    depth = 0
    pos = start
    while pos < len(text):
        o = text.find('<div', pos)
        c = text.find('</div>', pos)
        if c == -1:
            return -1
        if o != -1 and o < c:
            depth += 1
            pos = o + 4
        else:
            depth -= 1
            end = c + 6
            if depth == 0:
                return end
            pos = end
    return -1


def build_zone_rep(n_lines, corr_content):
    """Construit la zone-rep avec les lignes de réponse et la correction intégrée."""
    lines = ''.join([ANSWER_LINE] * n_lines)
    # Re-indenter corr_content de 2 espaces
    corr_indented = '\n'.join('  ' + l if l.strip() else l
                               for l in corr_content.splitlines())
    return (
        f'  <div class="zone-rep">\n'
        f'    <label>Mes calculs :</label>\n'
        f'{lines}'
        f'{corr_indented}\n'
        f'  </div>\n'
    )


def process_block(block, n_lines):
    """
    Transforme un bloc exercice :
    - Extrait .corr depuis après le bouton
    - Crée/met à jour zone-rep avec answer-lines + corr
    - Supprime corr de sa position originale
    - Déplace le bouton après zone-rep
    Retourne le bloc transformé.
    """
    # 1. Trouver .corr dans le bloc
    corr_start = block.find('<div class="corr">')
    if corr_start == -1:
        return block  # pas de correction, rien à faire

    corr_end = div_end(block, corr_start)
    if corr_end == -1:
        return block

    corr_content = block[corr_start:corr_end]

    # 2. Trouver le bouton .bc (avant .corr)
    btn_m = BC_BTN.search(block, 0, corr_start)
    if not btn_m:
        return block

    btn_str = btn_m.group(0)

    # 3. Construire la zone-rep
    zone_rep = build_zone_rep(n_lines, corr_content)

    # 4. Reconstruire le bloc :
    #    tout avant zone-rep/bouton + zone-rep + bouton + tout après .corr
    if '<div class="zone-rep">' in block[:btn_m.start()]:
        # zone-rep existante : la remplacer
        zr_start = block.find('<div class="zone-rep">')
        zr_end = div_end(block, zr_start)
        before = block[:zr_start]
        after_corr = block[corr_end:]
    else:
        # pas de zone-rep : insérer avant le bouton
        before = block[:btn_m.start()]
        after_corr = block[corr_end:]

    # Supprimer éventuels whitespace/newline entre corr et fin du bloc parent
    after_corr = after_corr.lstrip('\n')

    new_block = before + zone_rep + btn_str + '\n' + after_corr
    return new_block


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Déjà traité ?
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

        n_lines = LINES_BY_LEVEL[level]

        # Délimiter le bloc de cet exercice
        next_m = EXO_OPEN.search(content, m.end())
        end = next_m.start() if next_m else len(content)
        block = content[m.start():end]

        result.append(process_block(block, n_lines))
        pos = end

    result.append(content[pos:])
    new_content = ''.join(result)

    # Mettre à jour toggle()
    new_content = OLD_TOGGLE.sub(NEW_TOGGLE, new_content)

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
