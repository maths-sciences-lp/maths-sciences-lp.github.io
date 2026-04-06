# Skill : Vérification qualité d'un chapitre

## Usage

```
/check-quality <chemin-chapitre>
```

Exemple : `/check-quality physique-chimie/seconde/ch10`

Sans argument, demander le chemin du chapitre à analyser.

## Ce que fait ce skill

Revue complète d'un chapitre par lecture directe des fichiers HTML. Vérifie les règles techniques et pédagogiques définies dans les prompts.

---

## Instructions

### Étape 0 — Identifier le chapitre

Si un argument est fourni (`$ARGUMENTS`), utiliser ce chemin.
Sinon, demander le chemin du chapitre à analyser.

### Étape 1 — Inventaire

Lister les fichiers HTML présents dans le dossier du chapitre.

### Étape 2 — Lecture et vérification de chaque fichier

Lire chaque fichier HTML présent et vérifier les points suivants.

#### Règles communes à tous les fichiers

- `nav.js` inclus en fin de `<body>`
- `print.css` inclus dans le `<head>`
- Variables CSS `:root` présentes (`--p`, `--p-bg`, `--p-border`) avec les bonnes couleurs pour la section
- Lien retour sommaire présent (pointe vers la bonne page sommaire)
- Aucune classe de `styles.css` redéfinie inline (`.def`, `.prop`, `.meth`, `.exo`, `.corr`, `.bc`, etc.)
- Chemins vers les ressources corrects (`../../../styles.css`, `../../../nav.js`, etc.)
- MathJax inclus si la page contient des formules `\(...\)` ou `\[...\]`

#### exercices.html, ds.html, interro.html, exercices-capacites.html

**Densité de visuels :**

Compter sur la page :
- `nb_visuels` = nombre de `<svg`, `<canvas`, instances Chart.js (`new Chart`), `<img` (hors balises décoratives sans `alt` significatif)
- `nb_exercices` = nombre de blocs `.exo` ou titres d'exercice (`<h3>`, `<h4>` contenant "Exercice" ou numéro)

Appliquer les règles suivantes :

| Situation | Signal |
|---|---|
| `nb_visuels == 0` | 🔴 CRITIQUE — page sans aucun visuel |
| `nb_visuels / nb_exercices < 0,25` et physique-chimie | 🟡 AVERTISSEMENT — moins de 1 visuel pour 4 exercices |
| `nb_visuels / nb_exercices < 0,20` et maths (fonctions/géométrie/stats) | 🟡 AVERTISSEMENT |
| `nb_visuels / nb_exercices < 0,20` et maths algèbre/calcul pur | ✅ Acceptable |

Précisions :
- Ne pas signaler l'absence de visuel sur un exercice individuel — la règle s'applique à la **page entière**
- Un exercice purement numérique ou algébrique sans contexte géométrique n'a pas besoin de figure
- Signaler uniquement si le ratio global de la page est insuffisant

**Données uniquement :**
- Parcourir tous les `<table>` hors `.corr`
- Signaler toute ligne qui contient l'équation à construire, la valeur inconnue ou la solution
- Exemples interdits : `<td>x = 10</td>`, `<td>18,50x + 22 = 207</td>`

**Tableaux de données :**
- Repérer les exercices qui citent 3 valeurs numériques ou plus dans le texte sans `<table class="full">`
- Signaler ces exercices

**Références orphelines :**
- Chercher "ci-dessous", "ci-contre", "d'après le graphique", "d'après la courbe", "à partir de la courbe"
- Vérifier qu'un SVG, Canvas, Chart.js ou tableau est présent dans les environs (avant ou après)
- Signaler si aucune figure n'est trouvée

**Différenciation (exercices.html et ds.html uniquement) :**
- `diff-socle`, `diff-standard`, `diff-appro` présents
- `diff.js` inclus

**Animations :**
- Signaler tout `requestAnimationFrame` ou `setInterval` (réservé aux leçons et simulations)

#### lecon.html

**Mini-exo :**
- Compter les `.mini-exo` — signaler si moins de 3
- Vérifier qu'ils sont répartis dans le cours (pas regroupés à la fin)
- Vérifier que chaque `.mini-exo` a sa correction `.bc` + `.corr`

**Différenciation interdite :**
- `diff.js` absent
- Aucun bloc `diff-socle`, `diff-standard`, `diff-appro`

**Références orphelines :** même règle que ci-dessus.

#### qcm.html

- `qcm.js` inclus (ou fonction `corriger()` inline si ancien format)
- Objet `explications` défini (`var explications` ou `let explications`)
- `diff.js` inclus
- Bloc `diff-socle` présent
- Options A/B/C/D plausibles (distracteurs réalistes)

#### interro.html

- `diff.js` inclus
- Bloc `diff-socle` présent
- Corrections dans `.corr` et masquées par défaut
- Lignes `.answer-line` suffisantes pour chaque question

#### activite.html

- Bloc `.situation` ou problématique présente en introduction
- Corrections dans `.corr` et masquées par défaut
- Bouton Imprimer présent (`window.print()`)
- Pas de `diff.js` (les activités ne sont pas différenciées)

### Étape 3 — Rapport

Afficher un rapport structuré :

```
## Qualité : <chemin-chapitre>

### lecon.html
- ✓ nav.js, print.css, :root présents
- ✓ 4 mini-exo répartis dans le cours, chacun avec .corr
- ✗ diff.js présent — interdit sur lecon.html

### exercices.html
- ✓ diff-socle/standard/appro présents
- ✓ Visuels : 3 SVG pour 10 exercices (ratio 0,30 — OK)
- ✗ Ex.3 : tableau avec "x = 12" hors .corr (ligne ~145)
- ✗ Ex.7 : "le graphique ci-dessous" sans SVG adjacent

### ds.html
- ✓ Différenciation complète
- ⚠ Exercice 2 : 4 valeurs numériques dans le texte sans <table class="full">

### Actions recommandées
1. [haute] Supprimer diff.js de lecon.html
2. [critique] Retirer "x = 12" du tableau dans exercices.html Ex.3
3. [moyenne] Ajouter SVG ou table pour le graphique Ex.7
4. [basse] Tabuler les données de ds.html Ex.2
```

### Règles du rapport

- Ne PAS modifier les fichiers — seulement analyser et rapporter
- Classer par gravité : critique > haute > moyenne > basse
- Indiquer le fichier et le numéro de ligne ou d'exercice
- Proposer la correction exacte

---

## Étape 4 — Mettre à jour le journal des audits

Après avoir affiché le rapport, mettre à jour `audits/audit-log.md` :

1. Chercher si le chapitre a déjà une ligne dans le tableau
2. Si oui : mettre à jour la colonne `/check-quality` avec la date du jour (format `YYYY-MM-DD`) et le résultat (🔴 / 🟡 / 🟢)
3. Si non : ajouter une nouvelle ligne
4. Mettre à jour la date `Dernière mise à jour` en haut du fichier

ARGUMENTS: $ARGUMENTS
