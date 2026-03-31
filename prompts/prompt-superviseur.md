# PROMPT SUPERVISEUR — GÉNÉRATION DU SITE PÉDAGOGIQUE

Tu travailles sur un site pédagogique de mathématiques et de physique-chimie destiné aux élèves de lycée professionnel.

Le site contient :
- des cours
- des exercices
- des devoirs surveillés

Ton rôle est d'aider à générer ou compléter ces contenus de manière cohérente avec les programmes officiels.

---

## LECTURE DES RESSOURCES DU DÉPÔT

Avant de générer du contenu, lire les ressources suivantes :

### 1. Les programmes officiels situés dans :
`/pdf`

Ces fichiers contiennent les programmes de mathématiques et de physique-chimie du Bac Professionnel.

### 2. Les prompts pédagogiques situés dans :
`/prompts`

Ils contiennent :
- `prompt-cours.md` — structure d'une page de cours (avec consignes figures SVG)
- `prompt-exercices.md` — structure d'une page d'exercices (avec figures obligatoires)
- `prompt-exercices-capacites.md` — exercices par capacités du programme (conventions SVG détaillées)
- `prompt-qcm-interro.md` — QCM et interrogations (avec figures dans les questions)
- `prompt-activite.md` — activités de découverte (avec figures dans le document d'accroche)
- `prompt-fiche.md` — fiches de révision (avec figures de synthèse)
- `prompt-bts.md` — contenu BTS (avec figures techniques)
- `prompt-simulation.md` — simulations interactives (Canvas/SVG animé)
- Prompts de filière : contextes professionnels par formation

Ces prompts définissent :
- la structure pédagogique de chaque type de page
- les **figures et schémas SVG obligatoires** par domaine
- les conventions visuelles du site
- les contextes professionnels des filières

Toujours utiliser ces prompts comme référence.

---

## OBJECTIF DU TRAVAIL

Le but est de compléter progressivement le site pédagogique.

Pour chaque chapitre, générer si nécessaire :
- la page de cours
- la page d'exercices
- la page de devoir surveillé

Les pages doivent être cohérentes avec la structure HTML déjà utilisée sur le site.
Ne jamais casser la structure existante.

---

## STRUCTURE DES PAGES

Chaque chapitre possède un dossier `subject/level/chNN/` avec les fichiers suivants :

```
lecon.html              ← cours (obligatoire)
exercices.html          ← exercices différenciés (obligatoire)
ds.html                 ← devoir surveillé (obligatoire)
fiche.html              ← fiche de révision (standard)
qcm.html               ← QCM interactif (optionnel)
interro.html            ← interrogation courte (optionnel)
exercices-capacites.html ← exercices par capacités (standard)
activite.html           ← activité de découverte (optionnel)
```

Respecter cette organisation. Voir CLAUDE.md pour les détails.

---

## GÉNÉRATION DES COURS

Pour créer un cours :

1. Lire le prompt : `/prompts/prompt-cours.md`
2. Appliquer cette structure pour produire une page HTML pédagogique.

Le cours doit contenir :
- explications progressives
- exemples détaillés
- **figures SVG obligatoires** pour les notions visuelles (voir ci-dessous)
- graphiques (Chart.js ou SVG) pour les données quantitatives
- animations pédagogiques si pertinentes
- encadrés "À retenir"

Le niveau doit être adapté au lycée professionnel.

---

## GÉNÉRATION DES EXERCICES

Pour créer des exercices :

1. Lire le prompt : `/prompts/prompt-exercices.md`
2. Générer une série d'exercices progressifs.

Les exercices doivent :
- être accessibles
- comporter plusieurs niveaux de difficulté (socle / standard / appro)
- proposer des contextes variés
- **contenir des figures SVG pour tous les exercices de lecture graphique, géométrie, circuits, statistiques** (voir prompt-exercices.md)

Les contextes peuvent être :
- professionnels
- scientifiques
- quotidiens
- sportifs
- climatiques
- énergétiques

Ne pas utiliser uniquement des contextes professionnels.

---

## UTILISATION DES CONTEXTES PROFESSIONNELS

Si le chapitre concerne une filière particulière, lire le prompt correspondant :

| Filière | Prompt |
|---|---|
| Terminale ICCER | `prompt-filiere-ticcer` |
| Terminale ERA / MA | `prompt-filiere-era-ma` |
| Seconde MAMA | `prompt-filiere-2mama` |

Ces prompts décrivent :
- les métiers
- les contextes professionnels
- les règles de rédaction

Toujours utiliser les noms de métiers plutôt que les sigles des filières.

---

## FIGURES ET SCHÉMAS — RÈGLE TRANSVERSALE

**Règle absolue :** toute page qui porte sur une notion visuelle DOIT contenir des figures SVG inline. Un cours de géométrie sans figure, un exercice de lecture graphique sans courbe, un QCM sur un oscillogramme sans oscillogramme sont des pages **incomplètes**.

### Situations où une figure est OBLIGATOIRE

**Mathématiques :**
- Fonctions : courbe représentative, tableau de variations illustré, lecture graphique
- Géométrie : figure cotée (triangles, parallélogrammes, solides), vecteurs
- Statistiques : diagramme en bâtons, circulaire, boîte à moustaches, histogramme
- Probabilités : arbre de probabilités, tableau à double entrée
- Suites : nuage de points \((n ; u_n)\)

**Physique-Chimie :**
- Électricité : schéma de circuit, caractéristique I(U)
- Mécanique : bilan des forces, diagramme v(t)
- Optique : schéma rayon/normale, réflexion/réfraction
- Thermique : courbe T(t), schéma de transfert thermique
- Acoustique : oscillogramme, échelle dB
- Chimie : schéma de verrerie, spectres

### Ne JAMAIS décrire textuellement un graphique que l'élève doit lire

Si l'énoncé dit "le graphique ci-dessous", "l'oscillogramme ci-dessous", "le schéma ci-dessous", alors la figure SVG **DOIT** être présente dans le HTML.

### Conventions SVG

Toutes les figures SVG du site suivent les mêmes conventions (détaillées dans `prompt-exercices-capacites.md`) :
- Remplissage : `fill="#ebf5ff"`, contour : `stroke="#0056b3"`
- Labels : `fill="#555"`, axes : `stroke="#333"`
- Inconnues : `stroke="#c53030"` en pointillés
- Deuxième courbe : `stroke="#c53030"` (rouge)

### Application par type de page

| Page | Figures |
|---|---|
| `lecon.html` | Figures d'illustration des notions (obligatoires si visuel) |
| `exercices.html` | Figures d'énoncé pour lecture graphique, géométrie, circuits (obligatoires) |
| `exercices-capacites.html` | Idem exercices, une figure par capacité visuelle (obligatoires) |
| `ds.html` | Figures d'énoncé si exercice visuel (obligatoires) |
| `qcm.html` | Figures dans les questions visuelles (obligatoires) |
| `interro.html` | Figures pour schémas à légender, graphiques à lire (obligatoires) |
| `activite.html` | Figures dans le document d'accroche si visuel (obligatoires) |
| `fiche.html` | Figures de synthèse compactes (obligatoires pour chapitres visuels) |

Consulter le prompt spécifique de chaque type de page pour les détails.

---

## CONFORMITÉ AU PROGRAMME

Lors de la création des contenus, vérifier les notions dans les PDF du programme.

Ne pas introduire de notions hors programme.

Respecter :
- les capacités attendues
- les connaissances associées
- les limites indiquées dans le programme officiel

---

## STYLE DU SITE

Toujours respecter :
- la structure HTML existante
- les classes CSS existantes
- le style visuel du site
- l'organisation actuelle des pages

Ne pas modifier le CSS global.
Ne pas casser la navigation du site.

---

## OBJECTIF FINAL

Aider à compléter progressivement le site pédagogique en produisant :
- des cours clairs et pédagogiques
- des exercices progressifs
- des devoirs surveillés cohérents

tout en respectant :
- les programmes officiels
- la structure existante du site
- les prompts pédagogiques stockés dans le dépôt
