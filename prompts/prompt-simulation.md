# Prompt de référence — Génération de simulations interactives

Je veux que tu crées une simulation interactive, pédagogique et visuellement soignée, destinée à des élèves de lycée professionnel.

Objectif : produire une page HTML autonome (single-file) prête à être intégrée dans le dossier `simulations/` du site pédagogique.

---

## TYPES DE SIMULATIONS

Chaque simulation appartient à l'un des quatre types suivants. Le type détermine la complexité et les fonctionnalités attendues.

### Type 1 — Illustration

Objectif : illustrer un phénomène simple de manière visuelle.

Caractéristiques :
- 1 à 2 paramètres modifiables (sliders ou boutons)
- Interface minimaliste, compréhension immédiate
- Animation ou dessin Canvas/SVG qui réagit en temps réel
- Pas de tableau de données ni de mesures

Exemples : modèle de l'atome, propagation d'une onde, effet Joule qualitatif.

### Type 2 — TP numérique

Objectif : permettre une investigation scientifique guidée.

Caractéristiques :
- 2 à 4 paramètres modifiables
- Possibilité de faire des **mesures** (affichage de valeurs calculées)
- **Tableau de données** remplissable (bouton "Ajouter la mesure")
- Possibilité d'exporter ou copier les données
- Zone de résultats avec calculs intermédiaires visibles

Exemples : loi d'Ohm (mesurer U et I pour différentes R), pression hydrostatique (mesurer P à différentes profondeurs).

### Type 3 — Exploration libre

Objectif : laisser l'élève explorer librement un modèle physique ou mathématique.

Caractéristiques :
- 3 à 6 paramètres modifiables
- Système ouvert sans parcours imposé
- Retour visuel immédiat (animation, couleurs, déformations)
- Pas forcément de tableau de mesures, mais des indicateurs visuels clairs

Exemples : mélange de couleurs, simulation de gaz (pression-volume-température), balance des forces.

### Type 4 — Modèle mathématique

Objectif : relier la simulation aux équations et aux graphiques.

Caractéristiques :
- Affichage des **équations** (via MathJax) avec les valeurs numériques mises à jour
- **Graphique dynamique** (Chart.js) qui se met à jour en temps réel
- Variation des paramètres mathématiques avec sliders
- Lien explicite entre le phénomène visuel et la courbe/l'équation

Exemples : Q = m·c·ΔT avec graphique, traceur de droites y = ax + b, redressement du signal.

---

## STRUCTURE HTML

### Template minimal

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Titre — Simulation</title>
<!-- MathJax si équations -->
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!-- Chart.js si graphique -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  /* Styles inline — les simulations sont autonomes */
</style>
</head>
<body>
<div class="container">
  <header>
    <a href="../simulations.html" class="btn-back">← Retour</a>
    <h1>Titre de la simulation</h1>
    <p>Niveau — Chapitre · Formule clé</p>
  </header>

  <!-- Zone d'explication (optionnelle) -->
  <div class="explication">
    Rappel de la loi ou du phénomène...
  </div>

  <!-- Contrôles -->
  <div class="card">
    <!-- Sliders, selects, boutons -->
  </div>

  <!-- Visualisation -->
  <div class="card">
    <canvas id="canvas"></canvas>
  </div>

  <!-- Résultats / Graphique (selon le type) -->
  <div class="card">
    <!-- Valeurs calculées, graphique Chart.js, tableau de mesures -->
  </div>
</div>
<script>
  // Logique de la simulation
</script>
</body>
</html>
```

### Points importants

- **Page autonome** : styles inline (pas de lien vers `styles.css`), tout dans un seul fichier HTML
- **Chemin de retour** : `<a href="../simulations.html">← Retour</a>` (les simulations sont dans `simulations/`)
- **Pas de `nav.js`** dans les simulations (navigation autonome)
- **Responsive** : grille CSS avec media query pour mobile (`@media(max-width:600px)`)

---

## CRITÈRES DE QUALITÉ

### 1. Lisibilité visuelle
- Police : `'Segoe UI', system-ui, sans-serif`
- Fond de page : couleur neutre (`#f4f4f9` ou `#f8fafc`)
- Cartes blanches avec `border-radius: 10px` et ombre légère
- Header coloré avec le thème de la simulation
- Couleurs d'accent cohérentes (une couleur primaire par simulation)
- Taille de texte lisible, espacement aéré

### 2. Interaction immédiate
- Chaque slider/select déclenche une mise à jour instantanée (`oninput="update()"`)
- Pas de bouton "Calculer" inutile — la mise à jour est en temps réel
- Valeur numérique affichée à côté de chaque slider (`<span id="vParam">valeur</span>`)
- Appel initial à `update()` ou `init()` au chargement de la page

### 3. Paramètres pertinents
- Sliders avec `min`, `max` et `step` réalistes et physiquement cohérents
- Unités toujours affichées (kg, m, Pa, °C, V, A...)
- Valeurs par défaut qui donnent un résultat parlant
- Possibilité de sélectionner des matériaux/fluides prédéfinis si pertinent

### 4. Retour visuel clair
- Animation Canvas ou SVG réactive
- Couleurs qui changent pour refléter les grandeurs (ex : rouge = chaud, bleu = froid)
- Légendes et annotations directement sur le Canvas
- Taille du Canvas adaptée (400-600px de large typiquement)

### 5. Mesures et données (Type 2 — TP numérique)
- Zone de résultats avec valeurs calculées mises en forme
- Tableau de données avec bouton "Ajouter la mesure"
- Bouton "Effacer les données" pour recommencer
- Format des nombres : `toFixed(1)` ou `toFixed(2)` selon la précision utile

### 6. Équations et graphiques (Type 4 — Modèle mathématique)
- Équation affichée avec MathJax, valeurs numériques injectées dynamiquement
- Graphique Chart.js avec axes titrés et unités
- Mise à jour du graphique en temps réel (pas de recréation, utiliser `chart.update()`)
- Point courant visible sur la courbe

### 7. Performance
- Pas de `requestAnimationFrame` inutile — redessiner uniquement quand un paramètre change
- Si animation continue nécessaire, utiliser `requestAnimationFrame` avec possibilité de pause
- Canvas effacé avant chaque redessin (`ctx.clearRect(...)`)

---

## CONVENTIONS DE STYLE

### Palette de couleurs par domaine

| Domaine | Couleur header | accent-color |
|---|---|---|
| Électricité | `#e91e63` (rose) ou `#2563eb` (bleu) | idem |
| Thermique | `#e67e22` (orange) | `#e67e22` |
| Mécanique | `#0284c7` (bleu) | `#0284c7` |
| Chimie | `#16a34a` (vert) ou `#6f42c1` (violet) | idem |
| Ondes / Signaux | `#8b5cf6` (violet) | `#8b5cf6` |
| Mathématiques | `#2563eb` (bleu) | `#2563eb` |

### Classes CSS récurrentes

```css
.container { max-width: 860px; margin: 0 auto; }
.card { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); margin-bottom: 20px; }
.btn-back { position: absolute; left: 15px; top: 15px; background: rgba(255,255,255,0.2); color: white; text-decoration: none; padding: 5px 12px; border-radius: 5px; font-size: 0.85em; }
.row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.explication { background: #fff8f0; border-left: 4px solid var(--accent); padding: 12px 16px; border-radius: 0 8px 8px 0; }
.formule { font-family: monospace; background: #eee; border-radius: 6px; padding: 10px; }
.result { background: ...; border-radius: 8px; padding: 15px; }
```

Ces classes ne sont pas dans `styles.css` — elles sont redéfinies dans chaque simulation (pages autonomes).

---

## RÈGLE FONDAMENTALE — ANCRAGE PÉDAGOGIQUE

**Toute simulation doit être en lien direct avec un chapitre, une classe et le programme officiel.**

### Avant de créer ou modifier une simulation

1. **Analyser la page du chapitre concerné** (`lecon.html`) pour identifier les notions, formules et objectifs pédagogiques
2. **Vérifier le programme officiel** dans `/pdf/` pour confirmer que la notion est au programme de la classe concernée
3. **Concevoir la simulation** pour qu'elle illustre, exploite ou prolonge une notion réellement étudiée

### Ce qu'une simulation doit servir à faire

- Illustrer une notion du cours (visualiser un phénomène)
- Accompagner un exercice ou un TP numérique (manipuler des grandeurs)
- Faire manipuler un modèle mathématique ou physique du programme (relier formule et phénomène)
- Compléter un TP numérique (remplacer ou prolonger une manipulation réelle)

### Interdit

- Créer une simulation déconnectée du contenu pédagogique existant
- Introduire des notions hors-programme dans une simulation
- Créer une simulation "pour le plaisir" sans ancrage dans un chapitre précis

---

## RÈGLES PÉDAGOGIQUES

1. **Lien avec le programme** : chaque simulation doit correspondre à un chapitre du programme Bac Pro. Indiquer le chapitre et le niveau dans le header.

2. **Vocabulaire accessible** : utiliser un langage simple, adapté aux élèves de lycée professionnel. Expliquer les termes techniques.

3. **Formules visibles** : toujours afficher la formule utilisée, soit en MathJax soit dans un encadré `.formule`.

4. **Valeurs réalistes** : les paramètres par défaut et les plages de valeurs doivent correspondre à des situations physiquement réalistes.

5. **Contextes professionnels** : quand c'est pertinent, intégrer un contexte professionnel (chauffage, menuiserie, électricité du bâtiment...). Utiliser les vrais noms de métiers (voir CLAUDE.md).

6. **Pas de surcharge** : une simulation = un concept. Ne pas essayer de tout mettre dans une seule page. Mieux vaut deux simulations simples qu'une seule trop complexe.

---

## EXEMPLES EXISTANTS (à consulter comme référence)

| Fichier | Type | Description |
|---|---|---|
| `simulations/ohm.html` | Type 2 (TP) | Loi d'Ohm — multi-séries, graphique, mesures |
| `simulations/pression.html` | Type 4 (Modèle) | Pression hydrostatique — Canvas + formule |
| `simulations/chaleur.html` | Type 4 (Modèle) | Q = m·c·ΔT — thermomètre, graphique, matériaux |
| `simulations/atome.html` | Type 1 (Illustration) | Modèle atomique — Canvas animé |
| `simulations/gaz.html` | Type 3 (Exploration) | Gaz parfait — P, V, T libres |
| `simulations/balance.html` | Type 3 (Exploration) | Équilibre des forces |
| `simulations/traceur.html` | Type 4 (Modèle) | Traceur de droites — graphique dynamique |

---

## CHECKLIST AVANT LIVRAISON

- [ ] La simulation correspond à un chapitre et une classe identifiés
- [ ] Les notions utilisées sont au programme officiel (vérifié dans `/pdf/`)
- [ ] La page s'ouvre sans erreur dans un navigateur
- [ ] Les sliders et contrôles réagissent immédiatement
- [ ] Les valeurs numériques sont affichées avec les bonnes unités
- [ ] Le Canvas/SVG est lisible et bien dimensionné
- [ ] Le responsive fonctionne (mobile)
- [ ] Le lien retour pointe vers `../simulations.html`
- [ ] La formule clé est visible
- [ ] Les valeurs par défaut donnent un résultat parlant
- [ ] Le code JavaScript est propre (pas de variables globales inutiles, pas de console.log)
- [ ] MathJax / Chart.js inclus uniquement si utilisés
