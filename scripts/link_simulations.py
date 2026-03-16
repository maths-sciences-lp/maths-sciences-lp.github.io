#!/usr/bin/env python3
"""Insert simulation links into lecon.html pages."""
import re, os

BASE = "/home/user/maths-sciences-lp.github.io"

# Mapping: chapter_path -> [(simulation_filename, short_title)]
MAPPING = {
    # ═══ MATHS SECONDE ═══
    "maths/seconde/ch01": [("proportionnalite.html", "Proportionnalité et pourcentages")],
    "maths/seconde/ch02": [("statistiques.html", "Statistiques — Diagrammes et indicateurs")],
    "maths/seconde/ch03": [("statistiques.html", "Statistiques — Diagrammes et indicateurs")],
    "maths/seconde/ch04": [("probabilites.html", "Probabilités et fluctuation des fréquences")],
    "maths/seconde/ch05": [("entrainement.html", "Entraînement — Équations du premier degré"), ("equations.html", "Résolveur d'équations")],
    "maths/seconde/ch06": [("entrainement-ineq.html", "Entraînement — Inéquations"), ("inegalite.html", "Inéquations sur la droite graduée")],
    "maths/seconde/ch07": [("fonction-machine.html", "La machine à fonctions")],
    "maths/seconde/ch08": [("droite-affine.html", "Fonctions linéaire et affine")],
    "maths/seconde/ch09": [("droite-affine.html", "Fonctions linéaire et affine")],
    "maths/seconde/ch10": [("traceur.html", "Fonction du second degré — Traceur")],
    "maths/seconde/ch11": [("figures-planes.html", "Figures planes — Périmètres et aires")],
    "maths/seconde/ch12": [("pythagore.html", "Théorème de Pythagore")],
    "maths/seconde/ch13": [("thales.html", "Théorème de Thalès")],
    "maths/seconde/ch14": [("solides.html", "Solides usuels — Volumes et agrandissement")],

    # ═══ MATHS PREMIÈRE ═══
    "maths/premiere/ch01": [("stats-2var.html", "Statistiques à deux variables")],
    "maths/premiere/ch03": [("suites.html", "Suites numériques")],
    "maths/premiere/ch04": [("graphe-equation.html", "Résolution graphique d'équations")],
    "maths/premiere/ch05": [("traceur.html", "Fonction du second degré — Traceur")],
    "maths/premiere/ch06": [("derivee.html", "Fonction dérivée et tangente")],
    "maths/premiere/ch09": [("trigonometrie.html", "Trigonométrie")],

    # ═══ MATHS TERMINALE ═══
    "maths/terminale/ch01": [("stats-2var.html", "Statistiques à deux variables")],
    "maths/terminale/ch03": [("suites.html", "Suites numériques")],
    "maths/terminale/ch04": [("polynome3.html", "Fonctions polynômes de degré 3")],
    "maths/terminale/ch05": [("exp-log.html", "Fonctions exponentielles et logarithme")],
    "maths/terminale/ch06": [("vecteurs.html", "Vecteurs")],
    "maths/terminale/ch07": [("trigonometrie.html", "Trigonométrie")],
    "maths/terminale/ch08": [("integrale.html", "Calcul intégral")],
    "maths/terminale/ch09": [("exp-log.html", "Fonctions exponentielles et logarithme")],
    "maths/terminale/ch10": [("complexes.html", "Nombres complexes")],
    "maths/terminale/ch11": [("scalaire.html", "Produit scalaire")],

    # ═══ PC SECONDE ═══
    "physique-chimie/seconde/ch02": [("circuit-electrique.html", "Grandeurs électriques et circuits")],
    "physique-chimie/seconde/ch03": [("ohm.html", "Loi d'Ohm — Laboratoire virtuel")],
    "physique-chimie/seconde/ch04": [("signal-alternatif.html", "Signal alternatif — Oscilloscope virtuel")],
    "physique-chimie/seconde/ch05": [("mouvement.html", "Mouvement et trajectoire")],
    "physique-chimie/seconde/ch06": [("forces.html", "Forces et équilibre")],
    "physique-chimie/seconde/ch07": [("atome.html", "Constructeur d'atomes et ions"), ("atome-couches.html", "Configuration électronique"), ("modeles-atome.html", "Histoire du modèle de l'atome")],
    "physique-chimie/seconde/ch08": [("concentration.html", "Solutions chimiques et concentration")],
    "physique-chimie/seconde/ch09": [("son-2nde.html", "Caractéristiques d'un son")],
    "physique-chimie/seconde/ch10": [("chaleur.html", "Température et énergie thermique")],
    "physique-chimie/seconde/ch11": [("transferts-thermiques.html", "Transferts thermiques et équilibre")],
    "physique-chimie/seconde/ch12": [("changement-etat.html", "Courbe de chauffage — Changements d'état")],
    "physique-chimie/seconde/ch13": [("refraction.html", "Réflexion et réfraction de la lumière")],
    "physique-chimie/seconde/ch14": [("sources-lumineuses.html", "Sources lumineuses"), ("melangeur.html", "Mélangeur RVB")],

    # ═══ PC PREMIÈRE ICCER ═══
    "physique-chimie/premiere-iccer/ch01": [("puissance.html", "Puissance électrique")],
    "physique-chimie/premiere-iccer/ch02": [("transformateur.html", "Transformateur et transport d'énergie"), ("effet-joule.html", "Effet Joule")],
    "physique-chimie/premiere-iccer/ch03": [("combustion.html", "Combustion du carbone et des hydrocarbures")],
    "physique-chimie/premiere-iccer/ch04": [("conductance-thermique.html", "Conductance thermique et isolation")],
    "physique-chimie/premiere-iccer/ch05": [("vitesse-acceleration.html", "Vitesse et accélération")],
    "physique-chimie/premiere-iccer/ch06": [("moments.html", "Moments et équilibre en rotation")],
    "physique-chimie/premiere-iccer/ch07": [("pression.html", "Pression dans un fluide")],
    "physique-chimie/premiere-iccer/ch08": [("archimede.html", "Force d'Archimède")],
    "physique-chimie/premiere-iccer/ch09": [("concentration.html", "Solutions chimiques et concentration")],
    "physique-chimie/premiere-iccer/ch10": [("ondes-em.html", "Spectre électromagnétique")],

    # ═══ PC PREMIÈRE ERA ═══
    "physique-chimie/premiere-era/ch01": [("puissance.html", "Puissance électrique")],
    "physique-chimie/premiere-era/ch02": [("puissance.html", "Puissance électrique")],
    "physique-chimie/premiere-era/ch03": [("combustion.html", "Combustion du carbone et des hydrocarbures")],
    "physique-chimie/premiere-era/ch04": [("conductance-thermique.html", "Conductance thermique et isolation")],
    "physique-chimie/premiere-era/ch05": [("conductance-thermique.html", "Conductance thermique et isolation")],
    "physique-chimie/premiere-era/ch06": [("moments.html", "Moments et équilibre en rotation")],
    "physique-chimie/premiere-era/ch07": [("pression.html", "Pression dans un fluide")],
    "physique-chimie/premiere-era/ch08": [("concentration.html", "Solutions chimiques et concentration")],
    "physique-chimie/premiere-era/ch09": [("ondes-em.html", "Spectre électromagnétique")],
    "physique-chimie/premiere-era/ch10": [("son.html", "Signal sonore")],

    # ═══ PC TERMINALE ICCER ═══
    "physique-chimie/terminale-iccer/ch01": [("puissance.html", "Puissance électrique")],
    "physique-chimie/terminale-iccer/ch02": [("redressement.html", "Redressement du courant"), ("dephasage.html", "Déphasage et triangle des puissances")],
    "physique-chimie/terminale-iccer/ch03": [("moteur.html", "Moteur électrique")],
    "physique-chimie/terminale-iccer/ch04": [("rayonnement.html", "Rayonnement thermique")],
    "physique-chimie/terminale-iccer/ch05": [("pression.html", "Pression dans un fluide")],
    "physique-chimie/terminale-iccer/ch06": [("debit.html", "Débit d'un fluide")],
    "physique-chimie/terminale-iccer/ch07": [("oxydoreduction.html", "Oxydoréduction"), ("pile-electrochimique.html", "Pile électrochimique")],
    "physique-chimie/terminale-iccer/ch08": [("son.html", "Signal sonore")],

    # ═══ PC TERMINALE ERA ═══
    "physique-chimie/terminale-era/ch01": [("transformateur.html", "Transformateur et transport d'énergie")],
    "physique-chimie/terminale-era/ch02": [("pile-electrochimique.html", "Pile électrochimique")],
    "physique-chimie/terminale-era/ch03": [("rayonnement.html", "Rayonnement thermique"), ("serre.html", "Effet de serre")],
    "physique-chimie/terminale-era/ch04": [("vitesse-acceleration.html", "Vitesse et accélération")],
    "physique-chimie/terminale-era/ch05": [("oxydoreduction.html", "Oxydoréduction")],
    "physique-chimie/terminale-era/ch06": [("sources-lumineuses.html", "Sources lumineuses")],
    "physique-chimie/terminale-era/ch07": [("transmission-info.html", "Transmettre l'information")],
    "physique-chimie/terminale-era/ch08": [("son.html", "Signal sonore")],
}

def get_sim_path(chapter_path):
    """Return relative path to simulations/ from chapter depth."""
    depth = chapter_path.count("/")
    # maths/seconde/ch01 = depth 2, physique-chimie/seconde/ch01 = depth 2
    return "../" * (depth + 1) + "simulations/"

def build_link_block(sims, sim_base_path):
    """Build the HTML block with simulation links."""
    lines = []
    lines.append("")
    lines.append("<!-- Simulations interactives -->")
    lines.append('<div class="retenir" style="border-color:var(--p);background:var(--p-bg)">')
    lines.append('  <h3>Simulation interactive</h3>' if len(sims) == 1 else '  <h3>Simulations interactives</h3>')
    lines.append('  <ul style="list-style:none;padding:0;margin:0">')
    for filename, title in sims:
        url = sim_base_path + filename
        lines.append(f'    <li style="margin:.4em 0"><a href="{url}" target="_blank" style="color:var(--p);font-weight:600;text-decoration:underline">{title}</a></li>')
    lines.append('  </ul>')
    lines.append('</div>')
    lines.append("")
    return "\n".join(lines)

def already_has_sim_link(content):
    """Check if the file already contains a simulation link."""
    return "<!-- Simulations interactives -->" in content or "simulations/" in content

def insert_before_closing(content, block):
    """Insert the block before the closing </div> + <script src nav.js."""
    # Find the last </div> before nav.js
    pattern = r'(\n</div>\s*\n<script src="[^"]*nav\.js")'
    match = re.search(pattern, content)
    if match:
        return content[:match.start()] + block + content[match.start():]
    # Fallback: before </body>
    pattern2 = r'(</body>)'
    match2 = re.search(pattern2, content)
    if match2:
        return content[:match2.start()] + block + "\n" + content[match2.start():]
    return None

def main():
    modified = 0
    skipped = 0
    errors = 0

    for chapter, sims in sorted(MAPPING.items()):
        lecon_path = os.path.join(BASE, chapter, "lecon.html")
        if not os.path.exists(lecon_path):
            print(f"  SKIP (no file): {lecon_path}")
            skipped += 1
            continue

        with open(lecon_path, "r", encoding="utf-8") as f:
            content = f.read()

        if already_has_sim_link(content):
            print(f"  SKIP (already linked): {chapter}")
            skipped += 1
            continue

        sim_base = get_sim_path(chapter)
        block = build_link_block(sims, sim_base)
        new_content = insert_before_closing(content, block)

        if new_content is None:
            print(f"  ERROR (no insertion point): {chapter}")
            errors += 1
            continue

        with open(lecon_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        sim_names = ", ".join(s[0] for s in sims)
        print(f"  OK: {chapter} -> {sim_names}")
        modified += 1

    print(f"\nDone: {modified} modified, {skipped} skipped, {errors} errors")

if __name__ == "__main__":
    main()
