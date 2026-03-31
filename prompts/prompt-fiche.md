# Prompt de référence — Génération de fiches de révision (`fiche.html`)

Guide de référence pour la création des pages `fiche.html` dans chaque chapitre du site.

---

## Philosophie générale

### Rôle de la fiche

La fiche de révision est un **mémo synthétique** du chapitre. Elle ne remplace pas le cours — elle le condense pour permettre à l'élève de réviser rapidement avant un contrôle.

| Page | Rôle | Volume |
|---|---|---|
| `lecon.html` | Transmettre le savoir | Long, détaillé, progressif |
| `fiche.html` | **Synthétiser et mémoriser** | Court, dense, visuel |

### Ce qu'est une bonne fiche

- **Tient en 1 à 2 pages** (format A4, imprimable)
- **Visuelle** : formules encadrées, tableaux, icônes
- **Sans redondance** avec le cours : pas de réexplication des notions, seulement les éléments clés
- **Consultable en 5 minutes** : structure claire, titres visibles, hiérarchie lisible
- **Orientée action** : l'élève doit savoir quoi faire, pas juste quoi savoir

### Ce qu'une fiche n'est PAS

- Un cours condensé (pas d'explications longues)
- Un exercice (pas de questions, pas de calculs à faire)
- Un résumé complet (on garde l'essentiel, on coupe le reste)

---

## Structure d'une fiche

### Sections recommandées (dans cet ordre)

1. **En-tête** — titre du chapitre, classe, matière
2. **L'essentiel à retenir** — 3 à 5 points clés formulés en une phrase
3. **Définitions clés** — 3 à 6 définitions courtes (terme + définition en 1 ligne)
4. **Formules et propriétés** — encadrés formule, avec légende des variables
5. **Méthodes** — étapes numérotées pour les techniques principales du chapitre
6. **Erreurs fréquentes** — 2 à 4 pièges courants (encadré `.att`)
7. **Tableau de synthèse** *(si pertinent)* — comparaison, récapitulatif
8. **Exemple rapide** *(optionnel)* — 1 seul exemple court, pas de correction détaillée

---

## Spécifications techniques

### Template `fiche.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Ch0X – Fiche – Titre – Classe</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Fiche – Titre du chapitre</h1>
  <p class="sous-titre">Chapitre X | Niveau | Matière</p>
</header>

<!-- L'ESSENTIEL À RETENIR -->
<div class="retenir">
  <strong>L'essentiel :</strong>
  <ul>
    <li>Point clé 1</li>
    <li>Point clé 2</li>
    <li>Point clé 3</li>
  </ul>
</div>

<!-- DÉFINITIONS -->
<h2>Définitions</h2>
<div class="def">
  <span class="label-def">Définition</span>
  <strong>Terme :</strong> définition courte en une phrase.
</div>

<!-- FORMULES -->
<h2>Formules</h2>
<div class="formule-box">
  \[ formule \]
  <p>Légende : variable = signification (unité)</p>
</div>

<!-- MÉTHODES -->
<h2>Méthodes</h2>
<div class="meth">
  <span class="label-meth">Méthode</span>
  <strong>Titre de la méthode</strong>
  <ol>
    <li>Étape 1</li>
    <li>Étape 2</li>
    <li>Étape 3</li>
  </ol>
</div>

<!-- ERREURS FRÉQUENTES -->
<h2>Erreurs fréquentes</h2>
<div class="att">
  <span class="label-att">Attention</span>
  Description de l'erreur à éviter.
</div>

</div>
<script src="../../../nav.js"></script>
<!-- Pas de diff.js sur les fiches -->
</body>
</html>
```

---

## Règles de rédaction

### Longueur et densité

- **Maximum 2 pages A4** à l'impression (vérifier avec print.css)
- Pas de paragraphes longs : listes à puces, formules, tableaux
- Chaque phrase doit apporter une information nouvelle

### Formules

- Toutes les formules importantes du chapitre doivent apparaître, encadrées dans `.formule-box`
- Légender chaque variable : "avec \( v \) la vitesse en m/s, \( d \) la distance en m..."
- Si plusieurs formules sont liées (ex: loi d'Ohm et ses dérivées), les regrouper dans un tableau

### Méthodes

- Formulées en **étapes numérotées** courtes et actionnables
- Verbes d'action : "Identifier...", "Appliquer...", "Calculer...", "Vérifier..."
- Une méthode = une compétence du chapitre
- Pas plus de 5 étapes par méthode

### Différenciation

**Ne pas appliquer de différenciation sur les fiches.**

La fiche est identique pour tous les élèves (comme le cours) : elle synthétise le savoir commun. Pas de classes `.diff-*`, pas de `diff.js`.

### Pas de correction

La fiche ne contient **pas de corrections cachées** (pas de bouton `.bc` / `.corr`). Si un exemple rapide est inclus, il est directement visible.

---

## Figures et schémas dans les fiches

### Principe

La fiche est un **mémo visuel**. Un schéma synthétique vaut souvent mieux qu'un paragraphe de texte. Les figures de la fiche sont des **résumés visuels** des notions du cours, pas des copies intégrales des figures du cours.

### Quand une figure est OBLIGATOIRE

| Domaine | Figure attendue |
|---|---|
| Géométrie | Figure de référence cotée (triangle rectangle, Thalès, solide) |
| Fonctions | Allure type de la courbe (droite, parabole, exponentielle) avec vocabulaire annoté (sommet, asymptote, extremum) |
| Statistiques | Boîte à moustaches annotée (min, Q1, médiane, Q3, max) |
| Probabilités | Arbre de probabilités type (avec formules P(A∩B)) |
| Électricité | Schéma de circuit de référence avec grandeurs (U, I, R) |
| Mécanique | Bilan des forces type (poids, réaction, frottement) |
| Optique | Schéma de base (réflexion ou réfraction avec angles) |
| Thermique | Courbe de changement d'état type T(t) annotée (paliers, pentes) |

### Style SVG pour les fiches

Mêmes conventions que les exercices, mais les figures doivent être **compactes** (max 250px de large) pour tenir dans le format 1-2 pages A4 :

```html
<figure class="schema" style="text-align:center;margin:8px 0">
  <svg width="220" height="150" viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Contenu compact -->
  </svg>
  <figcaption style="font-size:0.85em;color:#555;margin-top:3px">Légende courte</figcaption>
</figure>
```

Conventions : fill `#ebf5ff`, stroke `#0056b3`, labels `#555`.

---

## Adaptation par matière

### Mathématiques

- Mettre en avant les formules de calcul, les propriétés des fonctions, les tableaux de signes/variations types
- Inclure un tableau de synthèse si le chapitre compare plusieurs objets (ex: suites arithmétiques vs géométriques)
- **Chapitres de géométrie** : figure SVG de référence cotée (OBLIGATOIRE)
- **Chapitres de fonctions** : allure type de la courbe annotée (OBLIGATOIRE)
- **Chapitres de statistiques** : boîte à moustaches annotée ou diagramme type (OBLIGATOIRE)
- **Chapitres de probabilités** : arbre de probabilités type (OBLIGATOIRE)
- **Chapitres de suites** : nuage de points type ou représentation en escalier (RECOMMANDÉ)

### Physique-Chimie

- Mettre en avant les formules physiques avec unités SI
- Tableau des grandeurs : symbole, nom, unité
- Inclure les ordres de grandeur importants
- **Chapitres d'électricité** : schéma de circuit de référence (OBLIGATOIRE)
- **Chapitres de mécanique** : bilan des forces type (OBLIGATOIRE)
- **Chapitres d'optique** : schéma rayon/normale (OBLIGATOIRE)
- **Chapitres de thermique** : courbe T(t) annotée ou schéma de transfert (OBLIGATOIRE)
- **Chapitres d'acoustique** : oscillogramme type ou échelle dB (RECOMMANDÉ)
- **Chapitres de chimie** : schéma de verrerie si protocole (RECOMMANDÉ)

---

## Checklist avant publication

- [ ] Tient en 1 à 2 pages A4 (tester l'impression)
- [ ] Pas de diff.js ni classes diff-*
- [ ] Toutes les formules importantes encadrées dans `.formule-box`
- [ ] Variables légendées avec unités
- [ ] Méthodes en étapes numérotées courtes
- [ ] Au moins un encadré `.att` (erreurs fréquentes)
- [ ] Encadré `.retenir` en haut
- [ ] **Figure SVG de synthèse pour les chapitres visuels** (géométrie, fonctions, statistiques, circuits, forces, optique, thermique)
- [ ] **Conventions SVG respectées** (fill #ebf5ff, stroke #0056b3, compact max 250px)
- [ ] MathJax inclus si formules
- [ ] print.css inclus
- [ ] Couleurs CSS conformes au thème matière/niveau
- [ ] Lien retour vers le sommaire
