#!/usr/bin/env python3
"""
Harmonise les exercices.html de maths/terminale :
- Supprime les section-titre / section-ligne
- Ajoute les classes diff-socle/standard/appro selon le niveau (n1/n2/n3-n4)
- Convertit exo-titre + num → exo-header
- Convertit <details> → button.bc + div.corr
- Assure la présence de diff.js et de toggle()
"""
import re, os, sys

LEVEL_MAP = {'n1': ('socle', 'Socle'),
             'n2': ('standard', 'Standard'),
             'n3': ('appro', 'Approfondissement'),
             'n4': ('appro', 'Approfondissement')}

TOGGLE_FN = '''\n<script>function toggle(b){const c=b.nextElementSibling;c.style.display=c.style.display==='block'?'none':'block';b.textContent=c.style.display==='block'?'Masquer la correction':'Voir la correction';}</script>'''

def strip_tags(html):
    """Remove HTML tags."""
    return re.sub(r'<[^>]+>', '', html).strip()

def convert(content, filename=''):
    lines = content.split('\n')
    out = []
    current_level = ('socle', 'Socle')
    i = 0
    exo_counter = 0

    while i < len(lines):
        line = lines[i]

        # ── Detect section-titre block and extract niveau ─────────────────────
        if re.search(r'<div class="section-titre">', line):
            # Scan ahead for niveau span
            j = i
            while j < min(i + 8, len(lines)):
                m = re.search(r'<span class="niveau (n\d)">', lines[j])
                if m:
                    current_level = LEVEL_MAP.get(m.group(1), ('appro', 'Approfondissement'))
                    break
                j += 1
            # Skip until closing </div> of section-titre (depth tracking)
            depth = 0
            while i < len(lines):
                depth += lines[i].count('<div') - lines[i].count('</div>')
                i += 1
                if depth <= 0:
                    break
            continue

        # ── Detect stand-alone <div class="section-ligne"> ────────────────────
        if re.search(r'<div class="section-ligne">', line):
            i += 1
            continue

        # ── Convert <div class="exo"> → <div class="exo diff-{level}"> ───────
        if re.match(r'\s*<div class="exo">', line):
            exo_counter += 1
            level_cls, level_label = current_level
            out.append(line.replace('<div class="exo">', f'<div class="exo diff-{level_cls}">'))
            i += 1
            # Next line should be the exo-titre
            if i < len(lines) and re.search(r'<div class="exo-titre">', lines[i]):
                titre_line = lines[i]
                # Extract number from <span class="num">N</span>
                num_m = re.search(r'<span class="num">(\d+)</span>', titre_line)
                num = num_m.group(1) if num_m else str(exo_counter)
                # Extract title text (strip num span + badge spans)
                title_html = titre_line
                title_html = re.sub(r'<div class="exo-titre">', '', title_html)
                title_html = re.sub(r'</div>', '', title_html)
                title_html = re.sub(r'<span class="num">\d+</span>', '', title_html)
                title_html = re.sub(r'<span class="[^"]*-badge">[^<]*</span>', '', title_html)
                title_text = title_html.strip()
                if not title_text:
                    title_text = f'Exercice {num}'
                indent = re.match(r'^(\s*)', lines[i - 1]).group(1)  # match exo div indent
                out.append(f'{indent}  <div class="exo-header">')
                out.append(f'{indent}    <span class="exo-num">Exercice {num}</span>')
                out.append(f'{indent}    <span class="exo-title">{title_text}</span>')
                out.append(f'{indent}    <span class="tag-{level_cls}">{level_label}</span>')
                out.append(f'{indent}  </div>')
                i += 1
            continue

        # ── Convert <details> → button.bc + div.corr ─────────────────────────
        if re.match(r'\s*<details>', line):
            indent = re.match(r'^(\s*)', line).group(1)
            # Consume <summary>...</summary>
            i += 1
            while i < len(lines) and not re.search(r'</summary>', lines[i]):
                i += 1
            i += 1  # skip the </summary> line
            # Now we should be at <div class="corr"> or its content
            # Find and remove wrapping <div class="corr"> if present
            corr_content = []
            depth = 0
            in_corr = False
            corr_div_open = False
            while i < len(lines):
                l = lines[i]
                if re.match(r'\s*<div class="corr">', l) and not in_corr:
                    corr_div_open = True
                    in_corr = True
                    depth = 1
                    i += 1
                    continue
                if re.match(r'\s*</details>', l):
                    i += 1
                    break
                if in_corr:
                    depth += l.count('<div') - l.count('</div>')
                    if depth <= 0:
                        i += 1
                        break
                    corr_content.append(l)
                else:
                    corr_content.append(l)
                i += 1
            out.append(f'{indent}<button class="bc" onclick="toggle(this)">Voir la correction</button>')
            out.append(f'{indent}<div class="corr">')
            out.extend(corr_content)
            out.append(f'{indent}</div>')
            continue

        out.append(line)
        i += 1

    result = '\n'.join(out)

    # ── Ensure diff.js is loaded ───────────────────────────────────────────────
    if 'diff.js' not in result:
        result = result.replace('</body>', '<script src="../../../diff.js"></script>\n</body>')

    # ── Ensure toggle() function is present ────────────────────────────────────
    if 'function toggle' not in result:
        result = result.replace('</body>', TOGGLE_FN + '\n</body>')

    # ── Clean up leftover empty lines (more than 2 consecutive) ───────────────
    result = re.sub(r'\n{3,}', '\n\n', result)

    return result


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    terminale_dir = os.path.join(base, 'maths', 'terminale')
    chapters = sorted([d for d in os.listdir(terminale_dir) if d.startswith('ch')])
    for ch in chapters:
        filepath = os.path.join(terminale_dir, ch, 'exercices.html')
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = convert(content, filepath)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        # Count results
        exo = new_content.count('diff-socle') + new_content.count('diff-standard') + new_content.count('diff-appro')
        print(f'{ch}: {exo} exo taggés')

if __name__ == '__main__':
    main()
