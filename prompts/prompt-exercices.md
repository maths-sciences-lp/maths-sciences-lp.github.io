# Prompt de référence — Génération de pages d'exercices

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
- `programme-maths-2nde-bac-pro.md`, `programme-maths-terminale-bac-pro.md`
- `programme-physique-chimie-2nde-bac-pro.md`, `programme-physique-chimie-terminale-bac-pro.md`
- `programme_maths_premiere_bacpro.md`, `programme_pc_premiere_bacpro.md`

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

### Règle fondamentale — données uniquement

**Un visuel dans un exercice montre uniquement les données brutes fournies à l'élève.**

Il ne doit **jamais** contenir :
- L'équation à construire (ex : une ligne "Équation : 18,50x + 22 = 207")
- La valeur inconnue ou la solution (ex : "x = 10 panneaux")
- Un point d'intersection tracé que l'élève doit déterminer
- Une droite que l'élève doit tracer lui-même

Il doit servir de **support de compréhension**, jamais de **support de correction**.

> **Règle mnémotechnique :** *"Ce que l'élève a le droit de voir sur son énoncé, et rien de plus."*

### Règle des tableaux de données (proactive)

**Dès qu'un exercice présente des valeurs numériques (prix, mesures, quantités, paramètres), les regrouper dans un tableau avant les questions** — même si le texte les cite déjà. Ne pas attendre que l'énoncé dise "le tableau ci-dessous".

```html
<!-- À placer dans la situation, avant les questions -->
<table class="full" style="margin:8px 0 14px;font-size:.92em;max-width:360px">
  <thead><tr><th>Donnée</th><th>Valeur</th></tr></thead>
  <tbody>
    <tr><td>Prix unitaire</td><td>18,50 €</td></tr>
    <tr><td>Frais de livraison</td><td>22 €</td></tr>
    <tr><td>Total facturé</td><td>207 €</td></tr>
  </tbody>
</table>
```

**Ne jamais ajouter** de ligne "Équation :", "Inconnue :", "Résultat :" — ces lignes sont les questions.

### Règle des repères vierges

Pour tout exercice de tracé ou de résolution graphique : fournir un repère avec axes et grille **sans aucune droite tracée** ni point d'intersection marqué.

```html
<figure class="schema" style="text-align:center;margin:10px 0 14px">
  <svg width="280" height="200" viewBox="0 0 280 200" xmlns="http://www.w3.org/2000/svg">
    <!-- Grille + axes uniquement — AUCUNE droite, AUCUN point solution -->
    <g stroke="#e5e7eb" stroke-width="0.5"><!-- lignes de grille --></g>
    <line x1="40" y1="10" x2="40" y2="170" stroke="#374151" stroke-width="1.5"/>
    <line x1="30" y1="160" x2="270" y2="160" stroke="#374151" stroke-width="1.5"/>
  </svg>
  <figcaption style="font-size:.88em;color:#555;margin-top:4px">Repère vierge — utiliser pour répondre</figcaption>
</figure>
```

### Visuels dans les exercices — statiques uniquement

Toutes les pages du site sont dual-use (écran + impression). Dans les exercices :
- **SVG statique** ✓ — format prioritaire pour les exercices
- **Chart.js** ✓ — acceptable si le graphique est rendu une seule fois (pas d'interaction)
- **Canvas animé** ✗ — réservé aux leçons (petite quantité) et simulations
- **Interactivité de réponse** ✗ — réservée au QCM via `qcm.js`

Concrètement : pas de `requestAnimationFrame`, `setInterval`, ni boutons qui modifient la figure. L'élève observe, lit, calcule — il n'interagit pas avec le visuel.

### Règle absolue — jamais de référence sans figure

Si l'énoncé dit "le graphique ci-dessous", "l'oscillogramme suivant", "le schéma ci-contre" ou "à partir de la courbe" — la figure **DOIT** être présente dans la page. Ne jamais décrire textuellement un graphique que l'élève doit lire.

`check_visuals.py` détecte automatiquement ces références orphelines.

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
