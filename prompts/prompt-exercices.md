# Prompt de référence — Génération de pages d'exercices

> ⚠ **Interdits absolus** (→ détails et exemples dans [`regles-communes.md`](regles-communes.md)) :
> 1. Les visuels montrent uniquement les données brutes — jamais l'équation, la solution, le point d'intersection
> 2. Toute référence "le graphique ci-dessous" exige une figure présente dans la page
> 3. Canvas animé interdit (`requestAnimationFrame`, `setInterval`)
> 4. Dès 3 valeurs numériques → `<table class="full">` avant les questions

Je veux que tu rédiges une page d'exercices complète, très pédagogique et bien structurée, destinée à des élèves de lycée professionnel.

Objectif : produire une page HTML prête à être intégrée dans un site pédagogique.

La page d'exercices doit être claire, progressive et accessible, avec des exercices variés, des explications simples et une correction pédagogique.

---

## STRUCTURE DE LA PAGE

### 1. Titre du chapitre

### 2. Introduction
- rappeler brièvement la notion travaillée
- expliquer l'objectif des exercices
- indiquer que les exercices sont progressifs

### 3. Exercices de base
- exercices simples pour vérifier la compréhension du cours
- questions directes
- application immédiate des définitions et méthodes

### 4. Exercices guidés
- exercices avec raisonnement étape par étape
- progression claire
- aide pédagogique implicite dans l'énoncé si nécessaire

### 5. Exercices d'application
- exercices plus complets
- mobilisation de plusieurs notions du chapitre
- calculs et raisonnements adaptés au niveau lycée professionnel

### 6. Exercices contextualisés
- proposer des exercices liés à la vie réelle ou au domaine professionnel
- utiliser des exemples concrets liés aux métiers professionnels

### 7. Illustrations visuelles
- proposer des schémas explicatifs si c'est utile
- proposer des images pédagogiques si nécessaire
- décrire précisément les images à générer

Pour chaque image, ajouter :

> **Prompt image :** description détaillée de l'image à générer

### 8. Graphiques
- produire des graphiques clairs si le chapitre s'y prête
- si possible générer le code pour :
  - Chart.js
  - SVG
  - ou Canvas

### 9. Encadrés importants
Ajouter des encadrés pédagogiques :
- Méthode
- Attention aux erreurs fréquentes
- À retenir

### 10. Correction
- proposer une correction détaillée
- expliquer les étapes du raisonnement
- corriger de manière pédagogique et progressive
- utiliser des phrases simples

---

## DIFFÉRENCIATION PÉDAGOGIQUE

La différenciation s'applique à **tous les niveaux** (Seconde, Première, Terminale).

### Les 3 niveaux de différenciation

| Niveau | Profil cible | Contenu |
|---|---|---|
| **Socle** | Élèves en difficulté | Exercices très guidés, étape par étape, calculs amorcés, tableaux pré-remplis, contextes du quotidien |
| **Standard** | Majorité de la classe | Exercices du programme, contextes professionnels variés, rédaction attendue |
| **Approfondissement** | Poursuite BTS/MC | Problèmes ouverts, mise en équation autonome, questions type BTS |

### Formes possibles de différenciation

1. **Niveau de difficulté progressif** : exercices de base → intermédiaires → avancés
2. **Variété des contextes** : professionnels, scientifiques, vie quotidienne
3. **Aides pédagogiques** : indices, rappels de méthode, étapes guidées
4. **Parcours possibles** : exercices accessibles à tous + exercices d'approfondissement

### Mise en œuvre technique

Utiliser les classes CSS `diff-socle`, `diff-standard`, `diff-appro` pour tagger les blocs par niveau (voir CLAUDE.md pour les détails techniques).

Le contenu doit rester **lisible, clair et structuré** — la différenciation ne doit pas rendre les pages confuses ou trop chargées.

---

## CONTRAINTES PÉDAGOGIQUES

- niveau lycée professionnel
- phrases simples
- vocabulaire accessible
- progression logique
- exercices progressifs
- correction détaillée et pédagogique

---

## VÉRIFICATION PROGRAMME OFFICIEL

Avant de générer, lire OBLIGATOIREMENT le fichier programme (.md) correspondant :
- `pdf/programme-maths-2nde-bac-pro.md`, `pdf/programme-maths-terminale-bac-pro.md`
- `pdf/programme-physique-chimie-2nde-bac-pro.md`, `pdf/programme-physique-chimie-terminale-bac-pro.md`
- `pdf/programme_maths_premiere_bacpro.md`, `pdf/programme_pc_premiere_bacpro.md`

**Chaque capacité du programme** doit être couverte par au moins un exercice dans la page. Si une capacité est absente, ajouter un exercice.

**Contenus hors programme** : ne pas supprimer, mais signaler avec une mention **(HP)** dans le titre de l'exercice ou de la section.

### Cohérence avec exercices-capacités

Les pages `exercices.html` et `exercices-capacites.html` couvrent le **même programme** avec des approches différentes :
- `exercices.html` : par difficulté (socle / standard / appro) via `diff.js`
- `exercices-capacites.html` : par capacité du programme via `comp.js`

Vérifier qu'il n'y a pas de capacité couverte dans l'une mais absente de l'autre.

---

## FIGURES ET ILLUSTRATIONS SVG

### Figures liées aux capacités (OBLIGATOIRES)

Certaines capacités du programme **exigent** une figure pour être travaillées. Sans figure, l'exercice ne couvre PAS la capacité.

**Règle absolue :** si l'énoncé dit "le graphique ci-dessous", "l'oscillogramme ci-dessous", "le schéma ci-dessous", alors la figure SVG **DOIT** être présente. Ne JAMAIS décrire textuellement un graphique que l'élève doit lire.

**Capacités nécessitant une figure (maths) :**
- Lecture graphique de fonctions (extremums, antécédents, variations)
- Diagrammes statistiques (bâtons, circulaires, boîte à moustaches)
- Figures géométriques (triangles, Thalès, Pythagore, solides)
- Vecteurs (représentation, parallélogramme)
- Arbres de probabilités

**Capacités nécessitant une figure (physique-chimie) :**
- Oscillogrammes (lecture de T, Umax, f)
- Schémas de circuits électriques
- Bilans de forces (vecteurs)
- Diagrammes espace-temps et vitesse-temps
- Courbes d'étalonnage de capteurs
- Diagrammes de changement d'état T(t)
- Schémas d'optique (rayon, normale, miroir, dioptre)
- Échelles de niveaux sonores (dB)
- Schémas de verrerie (fiole jaugée, dilution)
- Spectres d'émission

### Style SVG

```html
<figure class="schema" style="text-align:center;margin:12px 0">
  <svg width="250" height="170" viewBox="0 0 250 170" xmlns="http://www.w3.org/2000/svg">
    <!-- Contenu -->
  </svg>
  <figcaption style="font-size:0.88em;color:#555;margin-top:4px">Légende</figcaption>
</figure>
```

Conventions : fill `#ebf5ff`, stroke `#0056b3`, labels `#555`, inconnues `#c53030` en pointillés. Voir `prompt-exercices-capacites.md` pour les conventions détaillées.

---

## RÈGLES DES VISUELS DANS LES EXERCICES

→ Règles complètes avec exemples : [`regles-communes.md`](regles-communes.md)

En résumé :
- **Données uniquement** : pas d'équation, de solution ni de point d'intersection dans les visuels
- **Tableaux de données** : `<table class="full">` dès 3 valeurs numériques, avant les questions
- **Repères vierges** : axes + grille uniquement, aucune droite tracée
- **SVG statique prioritaire** ; Chart.js acceptable ; Canvas animé interdit
- **Jamais "le graphique ci-dessous" sans figure** dans la page

---

## VÉRIFICATION SCIENTIFIQUE

Vérifier systématiquement :
- **Refaire chaque calcul** des corrections
- **Unités SI** cohérentes
- **Valeurs physiques réalistes** (ex : vitesse du son dans un solide ≠ 340 m/s ; indice eau = 1,33 ; g = 9,81 m/s²)
- **Formules conformes au niveau** (signaler si hors programme)
- **Identifications correctes** (ex : raie 589 nm = sodium, pas néon)

---

## CONTRAINTES TECHNIQUES

- produire une page HTML propre
- utiliser des sections bien structurées
- utiliser les classes CSS de `styles.css` (voir CLAUDE.md)
- intégrer les figures SVG directement dans la page (pas d'images externes)
- inclure `styles.css`, `print.css`, `nav.js`, `diff.js`, MathJax

---

## OBJECTIF FINAL

Produire une page d'exercices riche, claire et très pédagogique, utilisable directement sur un site éducatif. Chaque capacité du programme doit être couverte. Chaque exercice de lecture graphique doit avoir sa figure.
