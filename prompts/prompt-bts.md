# Prompt de référence — Génération de contenu BTS

Guide de référence pour la création de pages dans la section `maths/bts/`.

---

## Spécificités de la section BTS

### Public cible

Les étudiants de BTS sont des élèves post-bac, issus de Terminale Bac Pro ou Bac Général, qui préparent un diplôme de technicien supérieur. Ils ont un niveau de maturité et d'autonomie plus élevé que les lycéens.

### Différences avec le Bac Pro

| Dimension | Bac Pro | BTS |
|---|---|---|
| **Différenciation** | Socle / Standard / Appro (diff.js) | **Aucune** — un seul niveau |
| **Niveau** | Lycée professionnel | Supérieur (bac+2) |
| **Rigueur** | Accessible, guidé | Technique, formalisé |
| **Formalisme** | Simplifié | Notation mathématique complète |
| **Contextes** | Vie quotidienne + pro | Contextes techniques et scientifiques |

**Ne pas utiliser `diff.js` ni les classes `.diff-socle`, `.diff-standard`, `.diff-appro` sur les pages BTS.**

---

## Structure des chapitres BTS

Chaque dossier `maths/bts/chNN/` contient :
- `lecon.html` — cours complet (obligatoire)
- `exercices.html` — exercices d'entraînement (obligatoire)
- `ds.html` — devoir surveillé (obligatoire)
- `fiche.html` — fiche de révision (recommandé)
- `qcm.html` — QCM (optionnel, sans différenciation — une seule série)
- `interro.html` — interrogation courte (optionnel, sans différenciation)

---

## Rédaction du cours BTS (`lecon.html`)

### Niveau attendu

- Vocabulaire mathématique rigoureux
- Notation formelle (ensembles, limites, dérivées, intégrales avec leur notation standard)
- Démonstrations ou justifications courtes pour les propriétés fondamentales
- Progression logique et structurée (définition → propriétés → méthodes → exemples)

### Structure recommandée

1. **Objectifs** — ce que l'étudiant doit savoir faire à la fin du chapitre
2. **Rappels** (si nécessaire) — notions prérequises du Bac Pro ou du lycée
3. **Définitions et propriétés** — encadrés `.def` et `.prop`, avec démonstration si utile
4. **Méthodes** — encadrés `.meth` avec exemples détaillés pas à pas
5. **Exemples appliqués** — contextes techniques ou scientifiques variés
6. **Résumé / À retenir** — encadré `.retenir` en fin de chapitre

### Ton et style

- Phrases complètes et précises
- Pas de simplification excessive : nommer les objets mathématiques correctement
- Exemple : écrire "la dérivée de f en a" et non "la pente de la courbe en ce point"
- Utiliser MathJax pour toutes les formules

---

## Rédaction des exercices BTS (`exercices.html`)

### Niveau attendu

- Exercices de difficulté progressive (pas de tags de niveau, mais progression naturelle)
- Exercices d'application directe + exercices de synthèse
- Contextes techniques (mécanique, électricité, thermique, économie, statistiques industrielles…)
- Rédaction soignée attendue : justifier les étapes, conclure

### Volume recommandé

- 12 à 20 exercices par chapitre
- Groupés en sections thématiques si le chapitre est large

### Format des exercices

```html
<div class="exo">
  <h3>Exercice X — Titre</h3>
  <p>Énoncé...</p>
  <button class="bc" onclick="toggle(this)">Voir la correction</button>
  <div class="corr">Correction complète et rédigée</div>
</div>
```

Pas de classes `.diff-*` — tous les exercices sont visibles par tous.

---

## Rédaction du DS BTS (`ds.html`)

### Format

- 1h à 1h30
- 3 à 4 exercices indépendants
- Barème total : 20 points
- Contextes techniques variés (pas toujours le même domaine)
- Pas de différenciation, pas de toggle sujet A/sujet B (sauf besoin explicite)

### Structure

```html
<div class="exo">
  <h2>Exercice 1 — Titre <span class="pts">(X points)</span></h2>
  <p>Contexte introductif...</p>
  <!-- Questions numérotées avec barème -->
</div>
```

---

## Contextes professionnels BTS

### Domaines techniques à privilégier

| Domaine | Exemples de situations |
|---|---|
| Électricité / électronique | circuits RC, signaux sinusoïdaux, filtres, impédance |
| Mécanique | vitesse, accélération, forces, couples, déformations |
| Thermique | échangeurs, transferts de chaleur, équations différentielles |
| Économie / gestion | intérêts composés, amortissements, optimisation de coûts |
| Statistiques industrielles | contrôle qualité, loi normale, intervalles de confiance |
| Signaux et images | transformées, fréquences, modélisation |
| Informatique industrielle | suites récurrentes, algorithmes, modèles discrets |

### Règle des sigles

Les filières BTS sont diverses (CRSA, SIO, ERE, SE, MS…). Ne pas mentionner un sigle de filière dans le contenu — utiliser les métiers réels :
- "Un technicien de maintenance..."
- "Un bureau d'études..."
- "Un ingénieur calcule..."
- "Un technicien qualité vérifie..."

---

## Figures et schémas — BTS

### Principe

Le niveau BTS exige des représentations graphiques rigoureuses : courbes précises, schémas techniques, diagrammes annotés. Les figures sont un outil de communication professionnelle, pas seulement pédagogique.

### Quand une figure est OBLIGATOIRE

**Cours (`lecon.html`) :**
- Fonctions : courbe représentative annotée (tangente, asymptotes, points d'inflexion)
- Suites : représentation graphique (nuage, escalier, toile d'araignée)
- Statistiques : diagramme en boîte, histogramme, nuage de points avec droite de régression
- Probabilités : loi normale (courbe de Gauss avec zones de probabilité), arbre
- Nombres complexes : plan complexe, module, argument
- Équations différentielles : famille de courbes intégrales
- Géométrie dans l'espace : solides, plans, droites (si au programme)

**Exercices (`exercices.html`) :**
- Tout exercice de lecture graphique → fournir la courbe SVG
- Tout exercice de statistiques → fournir le diagramme SVG
- Tout exercice demandant "représenter graphiquement" → fournir le repère SVG (axes, grille, graduations)
- Contextes techniques : schéma de la situation (circuit RC, échangeur, pièce mécanique)

**DS (`ds.html`) :**
- Si l'exercice porte sur des données graphiques → fournir le graphique SVG
- Si l'exercice porte sur un contexte technique → fournir le schéma de la situation

**Fiche (`fiche.html`) :**
- Allure type des courbes étudiées (exponentielle, logarithme, sinusoïde)
- Courbe de Gauss annotée pour les chapitres de probabilités
- Figure de référence pour les chapitres de géométrie

### Style SVG à respecter

```html
<figure class="schema" style="text-align:center;margin:12px 0">
  <svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
    <!-- Contenu -->
  </svg>
  <figcaption style="font-size:0.88em;color:#555;margin-top:4px">Légende</figcaption>
</figure>
```

**Conventions graphiques :**
- Remplissage : `fill="#ebf5ff"` (bleu très clair)
- Contour principal : `stroke="#0056b3"`, `stroke-width="2"`
- Labels : `font-size="12"`, `fill="#555"`
- Grilles : `stroke="#e2e8f0"`, `stroke-width="0.5"`
- Axes : `stroke="#333"`, `stroke-width="1.5"`, flèches aux extrémités
- Deuxième courbe/droite : `stroke="#c53030"` (rouge)
- Zones hachurées (probabilités, intégrales) : `fill="#0056b3"`, `opacity="0.15"`
- Tangentes : `stroke="#2da44e"` (vert), `stroke-dasharray="6,3"`

### Spécificités BTS

- Les figures BTS doivent être **plus précises** que celles du Bac Pro : graduations complètes, unités sur les axes, légendes détaillées
- Les graphiques de fonctions doivent montrer les **éléments caractéristiques** : points d'inflexion, asymptotes, tangentes
- Les diagrammes statistiques doivent respecter les **conventions professionnelles** (titres, échelles, sources)

---

## Spécifications techniques

### Template `lecon.html` BTS

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Ch0X – Titre – BTS</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd}</style>
</head>
<body>
<div class="c">
<a href="../../maths-bts.html" class="nb">← Retour au sommaire BTS</a>
<header>
  <h1>Chapitre X – Titre</h1>
  <p class="sous-titre">BTS | Mathématiques</p>
</header>
<!-- contenu -->
</div>
<script src="../../../nav.js"></script>
<!-- Pas de diff.js pour le BTS -->
</body>
</html>
```

**Couleur thème BTS :** `--p:#0969da` / `--p-bg:#dbeafe` / `--p-border:#93c5fd`

### QCM BTS

Si un QCM est créé pour une page BTS :
- **Une seule série de questions** (pas de diff-socle/standard/appro)
- 15 questions minimum
- Inclure `qcm.js` mais pas `diff.js`
- Questions de niveau standard/avancé

---

## Checklist avant publication

### Leçon BTS
- [ ] Pas de diff.js ni classes diff-*
- [ ] MathJax inclus
- [ ] Notation mathématique rigoureuse
- [ ] Exemples appliqués à des contextes techniques
- [ ] Encadrés `.def`, `.prop`, `.meth`, `.retenir` utilisés
- [ ] **Figures SVG pour les chapitres visuels** (fonctions, suites, statistiques, probabilités, complexes)
- [ ] **Conventions SVG respectées** (fill #ebf5ff, stroke #0056b3, graduations complètes)
- [ ] Lien retour vers `maths-bts.html`
- [ ] print.css inclus

### Exercices / DS BTS
- [ ] Pas de différenciation
- [ ] Corrections complètes (bouton toggle)
- [ ] Barème explicite pour le DS
- [ ] Contextes techniques variés
- [ ] **Figures SVG pour les exercices de lecture graphique, statistiques et contextes techniques**
- [ ] Rédaction soignée attendue dans les corrections
