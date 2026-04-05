# Prompt de référence — Exercices par capacités (`exercices-capacites.html`)

Guide de référence pour la création des pages `exercices-capacites.html` dans chaque chapitre du site.

---

## Philosophie générale

### Objectif pédagogique

La page "Exercices par capacités" organise les exercices selon les **capacités et connaissances du programme officiel (BO)**, et non selon le niveau de difficulté (différenciation) ou l'ordre chronologique du cours.

Elle permet :
- un entraînement **ciblé** sur une compétence précise
- d'**isoler les difficultés** et de faciliter la remédiation
- de **structurer les apprentissages** par savoir-faire mesurable
- un futur filtrage interactif par capacité (avec `comp.js`)

### Relation avec les autres pages du chapitre

| Page | Organisation | Usage |
|---|---|---|
| `exercices.html` | Par difficulté (socle/standard/appro) | Entraînement différencié |
| `exercices-capacites.html` | **Par capacité du programme** | Entraînement ciblé, remédiation |
| `ds.html` | Par exercice complet | Évaluation sommative |

**Ne pas modifier la page `exercices.html` existante.** Créer une nouvelle page dédiée.

---

## Définition des capacités

### Ce qu'est une capacité

Une capacité est ce que l'élève doit **savoir faire concrètement**, exprimée par un verbe d'action.

**Exemples de capacités valides :**
- reconnaître une fonction affine
- calculer une image ou un antécédent
- déterminer les variations d'une fonction
- calculer la dérivée d'une fonction polynôme
- résoudre une équation du second degré
- lire et interpréter un graphique
- calculer un terme d'une suite arithmétique ou géométrique
- appliquer la loi d'Ohm
- convertir des unités

### Ce qu'une capacité n'est PAS

Ne pas utiliser les **compétences transversales** génériques :
- ~~Chercher~~
- ~~Modéliser~~
- ~~Représenter~~
- ~~Raisonner~~
- ~~Calculer~~
- ~~Communiquer~~

Ces compétences sont trop larges. Utiliser uniquement des capacités disciplinaires précises issues du programme.

### Source des capacités

1. **Lire les fichiers PDF du programme (BO)** dans `/pdf/`
2. **Extraire les capacités et connaissances** liées au chapitre
3. **Reformuler légèrement** si nécessaire (niveau lycée professionnel, verbe d'action clair)
4. **Ne pas inventer** de capacités hors programme

---

## Structure de la page

### Template `exercices-capacites.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Ch0X – Exercices par capacités – Titre – Classe</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Chapitre X – Exercices par capacités</h1>
  <p class="sous-titre">Titre du chapitre | Niveau | Matière</p>
</header>

<!-- Liste des capacités du programme -->
<div class="objectifs">
  <strong>Capacités et connaissances du programme :</strong>
  <ul>
    <li>Capacité 1</li>
    <li>Capacité 2</li>
    <li>Capacité 3</li>
  </ul>
</div>

<!-- Boutons de filtre (si comp.js est utilisé) -->
<div class="cap-filtres">
  <button class="btn-cap" data-cap="all">Toutes</button>
  <button class="btn-cap" data-cap="C1">C1</button>
  <button class="btn-cap" data-cap="C2">C2</button>
  <button class="btn-cap" data-cap="C3">C3</button>
</div>

<!-- Section par capacité -->
<div class="cap-section" data-cap="C1">
<h2>C1 — Nom de la capacité</h2>

<div class="exo">
  <h3>Exercice 1</h3>
  <p>Énoncé ciblant uniquement cette capacité...</p>
  <button class="bc" onclick="toggle(this)">Voir la correction</button>
  <div class="corr">Correction détaillée</div>
</div>

<!-- Exercices 2 à 5 pour C1 -->
</div>

<div class="cap-section" data-cap="C2">
<h2>C2 — Nom de la capacité</h2>
<!-- Exercices pour C2 -->
</div>

</div>
<script src="../../../nav.js"></script>
<script src="../../../comp.js"></script>
<!-- Pas de diff.js — pas de différenciation sur cette page -->
</body>
</html>
```

---

## Règles de rédaction

### Nombre d'exercices par capacité

- **3 à 6 exercices par capacité**
- Difficulté progressive dans chaque série (du plus simple au plus complexe)
- Le premier exercice doit être accessible à tous les élèves

### Ciblage strict

- Chaque exercice cible **une seule capacité principale**
- Pas de mélange de plusieurs capacités dans un même exercice
- Si un exercice mobilise naturellement deux capacités, le classer dans la capacité principale et l'indiquer

### Corrections

- Toutes les corrections sont présentes (bouton `.bc` + `.corr`)
- Corrections **complètes et rédigées** : montrer toutes les étapes
- Pas de correction partielle ou abrégée

### Figures et illustrations SVG

Les exercices de géométrie, de fonctions et de statistiques doivent inclure des **figures SVG inline** pour aider l'élève à visualiser la situation.

#### Règle fondamentale — données uniquement

**Un visuel dans un exercice-capacité montre uniquement les données brutes fournies à l'élève.**

Il ne doit **jamais** contenir :
- L'équation à construire
- La valeur inconnue ou la solution
- Un point d'intersection tracé que l'élève doit déterminer
- Une droite que l'élève doit tracer lui-même

> *"Ce que l'élève a le droit de voir sur son énoncé, et rien de plus."*

#### Règle des tableaux de données (proactive)

Dès qu'un exercice présente des valeurs numériques (prix, mesures, quantités, résultats de mesures), les regrouper dans un tableau **avant les questions** — même si le texte les cite déjà.

```html
<table class="full" style="margin:8px 0 14px;font-size:.92em;max-width:360px">
  <thead><tr><th>Donnée</th><th>Valeur</th></tr></thead>
  <tbody>
    <tr><td>Résistance R</td><td>47 Ω</td></tr>
    <tr><td>Tension U</td><td>12 V</td></tr>
  </tbody>
</table>
```

Ne jamais ajouter de ligne "Résultat :", "I = ?" ou "Équation :".

#### Pas d'interactivité — SVG statique uniquement

Les pages `exercices-capacites.html` sont **imprimées et distribuées**. Ne jamais ajouter :
- Canvas avec animation
- Chart.js dynamique
- Boutons interactifs (calculette, vérification automatique)

Tout visuel est un **SVG statique** ou un **tableau HTML**. L'interactivité est réservée aux leçons et simulations.

#### Vérification automatique

Utiliser `python3 scripts/check_visuals.py` pour détecter les références orphelines ("le graphique ci-dessous" sans SVG présent) avant publication.

**IMPORTANT — Figures liées aux capacités du programme**

Certaines capacités du programme **exigent** une figure pour être travaillées. Sans figure, l'exercice ne couvre PAS la capacité. Ne JAMAIS décrire textuellement un graphique que l'élève doit lire. Si l'énoncé dit "le graphique ci-dessous", le graphique DOIT être présent en SVG.

**Capacités qui NÉCESSITENT une figure (la figure EST l'exercice) :**

*Mathématiques :*
- "Lire graphiquement les extremums / variations" → fournir la courbe SVG
- "Construire / lire un diagramme statistique" → fournir le diagramme SVG
- "Construire / lire un diagramme en boîte" → fournir le box plot SVG
- "Représenter le nuage (n ; un)" → fournir le nuage de points
- "Lire un tableau de variations" → la courbe aide à comprendre
- "Résoudre graphiquement f(x) = g(x)" → fournir les deux courbes
- "Tracer la droite représentative" → fournir le repère avec les points

*Physique-Chimie :*
- "Lire un oscillogramme" → fournir le SVG de l'oscillogramme
- "Représenter une force par un vecteur" → fournir le schéma avec repère
- "Exploiter une caractéristique I(U)" → fournir la courbe SVG
- "Lire un diagramme de changement d'état" → fournir le diagramme T(t)
- "Exploiter une courbe d'étalonnage" → fournir la courbe SVG
- "Exploiter une échelle de niveaux sonores" → fournir l'échelle en dB
- "Vérifier les lois de la réflexion/réfraction" → fournir le schéma rayon/normale
- "Identifier un mouvement à partir d'un enregistrement" → fournir le diagramme v(t)
- "Lire un schéma électrique" → fournir le schéma du circuit
- "Exploiter le spectre d'émission d'une lampe" → fournir le spectre SVG
- "Exploiter des images de caméra thermique" → fournir un schéma thermique

**Quand ajouter une figure (aide visuelle, pas obligatoire mais recommandé) :**
- Exercices de géométrie (triangles, figures planes, solides) : **systématiquement**
- Exercices de fonctions (courbes, droites, paraboles) : dans le rappel de cours et les exercices de lecture graphique
- Exercices de statistiques : diagrammes en bâtons, barres, circulaires
- Exercices de proportionnalité/Thalès : figure avec segments cotés
- Tout exercice décrivant une situation spatiale (échelle, toiture, rampe, pièce mécanique…)
- Exercices de probabilités : arbres, tableaux à double entrée
- Exercices de chimie : schéma de verrerie (fiole jaugée, dilution)

**Style SVG à respecter :**
```html
<figure class="schema" style="text-align:center;margin:12px 0">
  <svg width="250" height="170" viewBox="0 0 250 170" xmlns="http://www.w3.org/2000/svg">
    <!-- Contenu -->
  </svg>
  <figcaption style="font-size:0.88em;color:#555;margin-top:4px">Légende</figcaption>
</figure>
```

**Conventions graphiques :**
- Remplissage des formes : `fill="#ebf5ff"` (bleu très clair)
- Contour principal : `stroke="#0056b3"` (bleu primaire), `stroke-width="2"`
- Longueurs inconnues : `stroke-dasharray="6,3"` + couleur `#c53030` (rouge)
- Labels sommets : `font-size="13"`, `fill="#0056b3"`, `font-weight="bold"`
- Labels dimensions : `font-size="11-12"`, `fill="#555"`
- Angle droit : petit carré via `<polyline>` dans le coin
- Grilles (graphiques) : `stroke="#e2e8f0"`, `stroke-width="0.5"`
- Axes : `stroke="#333"`, `stroke-width="1.5"`, flèches aux extrémités
- Deuxième courbe/droite : `stroke="#c53030"` (rouge)
- Solides 3D : arêtes cachées en `stroke-dasharray="4,2"`

### Différenciation

**Ne pas appliquer de différenciation sur cette page.**

La page est conçue pour un usage ciblé (remédiation, révision par compétence). Tous les exercices sont visibles par tous. Pas de classes `.diff-*`, pas de `diff.js`.

---

## Intégration de comp.js

`comp.js` est le script de filtrage par capacité (ajouté en PR #131). Il permet d'afficher uniquement les exercices d'une capacité donnée via des boutons.

### Utilisation

- Ajouter `<script src="../../../comp.js"></script>` en fin de `<body>`
- Numéroter les capacités : C1, C2, C3… (ou utiliser des identifiants courts)
- Chaque section doit avoir `class="cap-section" data-cap="CX"`
- Chaque bouton de filtre doit avoir `class="btn-cap" data-cap="CX"`
- Le bouton "Toutes" utilise `data-cap="all"`

---

## Procédure avant génération

Avant de générer la page, toujours :

1. **Reformuler la demande** : quel chapitre, quelle classe, quelle matière ?
2. **Lire le fichier programme officiel (.md)** correspondant au niveau :
   - Maths 2nde : `programme-maths-2nde-bac-pro.md`
   - Maths 1ère : `programme_maths_premiere_bacpro.md`
   - Maths Terminale : `programme-maths-terminale-bac-pro.md`
   - PC 2nde : `programme-physique-chimie-2nde-bac-pro.md`
   - PC 1ère : `programme_pc_premiere_bacpro.md`
   - PC Terminale : `programme-physique-chimie-terminale-bac-pro.md`
3. **Extraire les capacités et connaissances** du tableau officiel pour le module concerné
4. **Lire `lecon.html`** du chapitre pour identifier les notions enseignées
5. **Vérifier que chaque capacité du programme** a au moins 2 exercices
6. **Proposer la structure** : capacités C1, C2, C3… avec leur intitulé
7. **Indiquer les fichiers à créer** : `exercices-capacites.html` uniquement

### Contenus hors programme

Si un exercice dépasse le programme officiel (notion de classe supérieure ou complément), **ne pas le supprimer** mais :
- Ajouter **(HP)** dans le titre de la capacité
- Ajouter une note dans le rappel de cours : *"Cette notion dépasse le programme de [niveau]. Elle est proposée en complément pour la poursuite d'études."*

### Vérification scientifique

Vérifier systématiquement dans chaque correction :
- **Refaire chaque calcul** (ne pas faire confiance aux résultats "évidents")
- **Cohérence des unités** (SI, conversions correctes)
- **Valeurs physiques réalistes** (vitesse du son dans un solide ≠ 340 m/s, indice de l'eau = 1,33, etc.)
- **Formules conformes au niveau** (pas de formules hors programme sans le signaler)

---

## Checklist avant publication

- [ ] Capacités extraites du programme officiel (pas inventées)
- [ ] 3 à 6 exercices par capacité
- [ ] Difficulté progressive dans chaque série
- [ ] Un exercice = une capacité principale
- [ ] Corrections complètes pour tous les exercices
- [ ] comp.js inclus et fonctionnel
- [ ] Pas de diff.js ni classes diff-*
- [ ] MathJax inclus si formules
- [ ] print.css inclus
- [ ] Couleurs CSS conformes au thème matière/niveau
- [ ] Lien retour vers le sommaire
- [ ] Page `exercices.html` originale non modifiée
- [ ] Figures SVG inline pour les exercices géométriques, graphiques et statistiques
- [ ] Style SVG conforme aux conventions (fill #ebf5ff, stroke #0056b3, labels #555)
- [ ] Tableaux de données `<table class="full">` pour tout exercice avec valeurs numériques
- [ ] Les visuels montrent UNIQUEMENT les données — jamais l'équation, la solution, l'inconnue
- [ ] Aucun Canvas, Chart.js ou interactivité (page imprimable — SVG statique uniquement)
- [ ] Aucune référence orpheline (`check_visuals.py` validé)
