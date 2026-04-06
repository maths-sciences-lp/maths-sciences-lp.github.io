"""
fix_qcm_pc.py — Supprime les fonctions corriger()/reinitialiser() inline
dans les qcm.html de physique-chimie/ et ajoute qcm.js.

Traite les deux cas :
  - avec diff.js  → ajoute qcm.js après diff.js
  - sans diff.js  → ajoute qcm.js après nav.js
"""

import re
import glob
import os

# Pattern : supprime tout depuis "function corriger(" jusqu'à la fermeture </script>
# qui suit reinitialiser(). Fonctionne même si forEach a un 2e argument (block, i).
FUNC_PATTERN = re.compile(
    r'\nfunction corriger\(.*?\n</script>',
    re.DOTALL
)

files = glob.glob('physique-chimie/**/qcm.html', recursive=True)
files.sort()

fixed = 0
skipped = 0

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Déjà corrigé ?
    if 'qcm.js' in content:
        print(f'[skip] {path}')
        skipped += 1
        continue

    # Supprimer les fonctions inline
    new_content, count = FUNC_PATTERN.subn('\n</script>', content)

    if count == 0:
        print(f'[WARN] pattern non trouvé dans {path}')
        continue

    # Ajouter qcm.js avant </body>
    if '<script src="../../../diff.js"></script>' in new_content:
        new_content = new_content.replace(
            '<script src="../../../diff.js"></script>\n</body>',
            '<script src="../../../diff.js"></script>\n<script src="../../../qcm.js"></script>\n</body>'
        )
    else:
        # CAP : pas de diff.js → après nav.js
        new_content = new_content.replace(
            '<script src="../../../nav.js"></script>\n</body>',
            '<script src="../../../nav.js"></script>\n<script src="../../../qcm.js"></script>\n</body>'
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'[OK]   {path}')
    fixed += 1

print(f'\n{fixed} fichiers corrigés, {skipped} déjà OK.')
