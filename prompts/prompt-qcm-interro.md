# Prompt — QCM et Interrogations

Guide de reference pour la creation des pages `qcm.html` et `interro.html` dans chaque chapitre du site.

---

## Philosophie generale

### Pourquoi QCM et interro en plus des exercices et DS ?

Le site propose **6 types de pages par chapitre**, chacun avec un role pedagogique distinct :

| Page | Role | Duree | Quand l'utiliser |
|---|---|---|---|
| `lecon.html` | Transmettre le savoir | — | En classe, decouverte |
| `exercices.html` | S'entrainer | Variable | En classe ou a la maison |
| `qcm.html` | **S'auto-evaluer** | 15-20 min | Avant un controle, en autonomie |
| `interro.html` | **Diagnostiquer** | 10-15 min | En debut de seance, verification rapide |
| `ds.html` | Evaluer (sommatif) | 1h | Controle officiel |
| `fiche.html` | Reviser / synthetiser | — | Avant un controle, revision |

### Le QCM : outil d'auto-evaluation

Le QCM est un outil **numerique et interactif** que l'eleve utilise en autonomie. Il ne remplace pas les exercices — il les complete en offrant un retour immediat.

**Principes fondamentaux :**
- L'eleve sait **immediatement** s'il a compris ou non (feedback instantane)
- Le score lui donne une **mesure objective** de sa maitrise du chapitre
- Le format QCM permet de **couvrir largement** le chapitre en peu de temps (15 questions)
- L'explication apres chaque reponse est **pedagogique**, pas juste "bonne/mauvaise reponse"
- Le QCM est **rejouable** : l'eleve peut recommencer pour s'ameliorer

**Ce que le QCM n'est PAS :**
- Un exercice redige (pas de redaction, pas de demarche)
- Un DS (pas de bareme officiel, pas de note dans le bulletin)
- Un cours deguise (les explications restent breves, pas de theorie nouvelle)

### L'interrogation : outil de diagnostic rapide

L'interrogation est un outil **papier** que l'enseignant utilise en classe pour prendre la temperature. Elle permet de reperer rapidement les eleves en difficulte et d'ajuster le cours.

**Principes fondamentaux :**
- **Courte** (10-15 min) : ne mange pas la seance, s'insere en debut ou fin de cours
- **Ciblee** : 5-8 questions sur les notions essentielles du chapitre
- **Imprimable** : concue pour etre distribuee sur papier en classe
- Les corrections sont disponibles en ligne (bouton "Voir la correction")
- L'interro donne une **photo instantanee** des acquis, pas une evaluation definitive

**Ce que l'interro n'est PAS :**
- Un DS (trop courte, pas le meme poids dans l'evaluation)
- Un QCM (format redige, pas de choix multiples)
- Un exercice d'entrainement (c'est une evaluation, meme si courte)

### Difference cle entre interro et DS

| Dimension | `interro.html` | `ds.html` |
|---|---|---|
| **Duree** | 10-15 min | 1h |
| **Volume** | 5-8 questions | 4+ exercices complets |
| **Objectif** | Diagnostic rapide | Evaluation sommative |
| **Poids** | Leger (verification) | Lourd (note officielle) |
| **Frequence** | Reguliere (chaque semaine possible) | Ponctuelle (fin de chapitre) |
| **Contenu** | Notions essentielles seulement | Tout le chapitre en profondeur |
| **Differenciation** | Socle/standard/appro (3 sujets courts) | Socle/standard/appro (3 sujets complets) |

---

## Differenciation pedagogique

### QCM : 3 series de 15 questions

Le QCM utilise `diff.js` pour proposer 3 series adaptees :

**Socle (15 questions) :**
- Questions directes, vocabulaire simple
- Reconnaissance immediate (identifier, nommer, choisir)
- Calculs elementaires (operations de base, substitution directe)
- Contextes du quotidien
- Formulations courtes et univoques
- Exemple maths : "Quelle est la derivee de f(x) = 3x ?" → A. 3 / B. 3x / C. 0 / D. x
- Exemple PC : "L'unite de la force est :" → A. le Joule / B. le Newton / C. le Watt / D. le Pascal

**Standard (15 questions) :**
- Questions classiques du programme
- Application de formules dans un contexte
- Interpretation de resultats, lecture de graphiques
- Contextes professionnels varies
- Formulations precises, vocabulaire technique attendu
- Exemple maths : "f(x) = x^3 - 3x. f'(x) = 0 pour :" → A. x=1 / B. x=-1 et x=1 / C. x=0 / D. x=sqrt(3)
- Exemple PC : "Un radiateur de 2000 W fonctionne 3h. L'energie consommee est :" → A. 6 kWh / B. 6000 J / C. 667 Wh / D. 6 kJ

**Approfondissement (15 questions) :**
- Questions a raisonnement (deduction, elimination, croisement de notions)
- Problemes ouverts adaptes au format QCM (quel raisonnement est correct ?)
- Vocabulaire BTS, formulations exigeantes
- Contextes professionnels complexes ou scientifiques
- Exemple maths : "f(x) = ax^3 + bx avec f(1)=2 et f'(1)=5. Alors a = :" → A. 1 / B. 2 / C. 3 / D. -1
- Exemple PC : "Un systeme isole echange de la chaleur. La variation d'enthalpie est negative. On peut en deduire que :" → ...

### Interro : 3 sujets de 5-8 questions

L'interro utilise `diff.js` pour proposer 3 sujets differencies :

**Socle :**
- Exercices tres guides, etape par etape
- Calculs amorces ("Completer : f(2) = 3 x (...)^2 - 1 = ...")
- Tableaux pre-remplis a completer
- Questions de reconnaissance ("Entourer les polynomes de degre 3")
- Rappels de methode integres

**Standard :**
- Consignes completes sans guidage excessif
- Calculs a faire integralement
- Contextes professionnels varies
- Redaction attendue (justifier, expliquer)
- Questions d'application directe du cours

**Approfondissement :**
- Problemes plus ouverts (moins de guidage)
- Mise en equation autonome
- Questions de demonstration ou justification
- Contextes complexes ou pluridisciplinaires
- Questions type BTS

---

## Specifications techniques

### Template `qcm.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – QCM – Titre – Classe</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>QCM – Titre du chapitre</h1>
  <p class="sous-titre">Chapitre X | Niveau | Matière</p>
</header>

<div class="qcm-header">
  <div class="dh-item">⏱ <strong>Durée :</strong> 15–20 min</div>
  <div class="dh-item">📄 <strong>15 questions</strong></div>
</div>

<!-- === SOCLE === -->
<div class="diff-socle">
<span class="tag-socle">Socle</span>

<div class="q-block" data-correct="A">
  <h3>Question 1</h3>
  <div class="options">
    <label><input type="radio" name="s1" value="A"> Réponse A</label>
    <label><input type="radio" name="s1" value="B"> Réponse B</label>
    <label><input type="radio" name="s1" value="C"> Réponse C</label>
    <label><input type="radio" name="s1" value="D"> Réponse D</label>
  </div>
  <div class="q-feedback ok">Explication si correct</div>
  <div class="q-feedback ko">Explication si incorrect</div>
</div>
<!-- Q2 à Q15 ... -->

<button class="btn-valider" onclick="evaluerQCM('socle')">Valider mes réponses</button>
<button class="btn-reset" onclick="resetQCM('socle')">Recommencer</button>
<div class="score-box" id="score-socle"></div>
</div>

<!-- === STANDARD === -->
<div class="diff-standard">
<span class="tag-standard">Standard</span>
<!-- 15 questions standard ... -->
</div>

<!-- === APPROFONDISSEMENT === -->
<div class="diff-appro">
<span class="tag-appro">Approfondissement</span>
<!-- 15 questions approfondissement ... -->
</div>

</div>
<script src="../../../nav.js"></script>
<script src="../../../diff.js"></script>
<script>
/* Script auto-correction QCM */
function evaluerQCM(niveau) { /* ... */ }
function resetQCM(niveau) { /* ... */ }
</script>
</body>
</html>
```

### Template `interro.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – Interrogation – Titre – Classe</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Chapitre X – Interrogation écrite</h1>
  <p class="sous-titre">Titre du chapitre — Niveau</p>
</header>

<div class="dh">
  <p><strong>Durée :</strong> 10-15 min | <strong>Barème :</strong> X points</p>
</div>

<!-- === SOCLE === -->
<div class="diff-socle">
<span class="tag-socle">Socle</span>

<div class="exo">
<h2>Question 1 <span class="pts">(X points)</span></h2>
<div class="meth"><strong>Rappel :</strong> aide methodologique</div>
<p>Consigne guidée, étape par étape...</p>
<button class="bc" onclick="this.nextElementSibling.style.display='block'">Voir la correction</button>
<div class="corr">Correction détaillée</div>
</div>
<!-- Q2 à Q5-8 ... -->
</div>

<!-- === STANDARD === -->
<div class="diff-standard">
<span class="tag-standard">Standard</span>
<!-- 5-8 questions standard ... -->
</div>

<!-- === APPROFONDISSEMENT === -->
<div class="diff-appro">
<span class="tag-appro">Approfondissement</span>
<!-- 5-8 questions approfondissement ... -->
</div>

</div>
<script src="../../../nav.js"></script>
<script src="../../../diff.js"></script>
</body>
</html>
```

---

## Figures et schémas dans les QCM et interrogations

### Règle absolue

**Si une question porte sur un élément visuel (graphique, schéma, oscillogramme, figure géométrique), la figure SVG DOIT être présente dans la question.** Ne jamais écrire "le graphique ci-dessous montre..." sans fournir le graphique.

### Quand une figure est OBLIGATOIRE

**QCM maths — questions nécessitant une figure :**
- Lecture graphique : "Quel est le maximum de f sur [a;b] ?" → fournir la courbe SVG
- Identification de courbes : "Quelle courbe représente f(x) = x² ?" → fournir les 4 courbes en options
- Statistiques : "Quelle est la médiane ?" → fournir le diagramme en boîte ou l'histogramme SVG
- Géométrie : "Quelle est la mesure de l'angle ?" → fournir la figure cotée SVG
- Suites : "Cette suite est-elle croissante ?" → fournir le nuage de points SVG
- Probabilités : "Calculer P(A∩B)" → fournir l'arbre ou le tableau à double entrée

**QCM physique-chimie — questions nécessitant une figure :**
- Oscillogrammes : "La fréquence du signal est :" → fournir l'oscillogramme SVG
- Circuits : "Quel est le schéma correct ?" → fournir les schémas de circuits SVG
- Forces : "Quel vecteur représente le poids ?" → fournir le bilan des forces SVG
- Optique : "L'angle de réfraction est :" → fournir le schéma rayon/normale SVG
- Changements d'état : "La température de fusion est :" → fournir la courbe T(t) SVG
- Spectres : "Cette lampe émet dans le :" → fournir le spectre SVG
- Niveaux sonores : "Ce niveau est dangereux car :" → fournir l'échelle en dB SVG

**Interro maths — questions nécessitant une figure :**
- "À partir du graphique, déterminer..." → fournir le graphique SVG
- "Compléter le tableau de variations à l'aide de la courbe" → fournir la courbe SVG
- "Lire les coordonnées des points sur la figure" → fournir la figure SVG
- Tout exercice de géométrie (triangles, Thalès, Pythagore) → fournir la figure cotée SVG

**Interro physique-chimie — questions nécessitant une figure :**
- "Légender le schéma" → fournir le schéma SVG à compléter
- "Lire la valeur sur l'oscillogramme" → fournir l'oscillogramme SVG
- "Compléter le schéma du circuit" → fournir le circuit SVG partiellement rempli
- "Tracer le vecteur force" → fournir le schéma de la situation SVG

### Style SVG à respecter

```html
<figure class="schema" style="text-align:center;margin:12px 0">
  <svg width="250" height="170" viewBox="0 0 250 170" xmlns="http://www.w3.org/2000/svg">
    <!-- Contenu -->
  </svg>
  <figcaption style="font-size:0.88em;color:#555;margin-top:4px">Légende</figcaption>
</figure>
```

**Conventions :** fill `#ebf5ff`, stroke `#0056b3`, labels `#555`, axes `#333`, deuxième courbe `#c53030`.

### Bonnes pratiques

- Dans un QCM, la figure est placée **dans le bloc de la question**, avant les choix
- Dans une interro, la figure est placée **dans l'énoncé**, avant les sous-questions
- Pour les QCM avec identification visuelle : proposer 4 figures SVG (une par option A/B/C/D) plutôt que 4 descriptions textuelles
- Pour le socle : figures plus grandes et plus lisibles, avec labels explicites
- Pour l'approfondissement : figures pouvant contenir plus d'informations à extraire

---

## Adaptation par matiere

### Mathematiques

**QCM maths — types de questions privilegies :**
- Calcul mental (derivees, images, operations sur fractions)
- Reconnaissance de formules (identifier la bonne expression)
- Lecture graphique (extremum, signe, variations)
- Vrai/Faux sur proprietes (avec justification dans le feedback)
- Identification de parametres (coefficients, degre, nature d'une suite)

**Interro maths — types de questions privilegies :**
- Calculs directs (deriver, calculer une image, resoudre)
- Tableaux a completer (signes, variations)
- Exercices de reconnaissance (classer, identifier)
- Petits problemes contextuels (1-2 etapes max)

### Physique-Chimie

**QCM PC — types de questions privilegies :**
- Unites et conversions (identifier l'unite correcte, convertir)
- Vocabulaire scientifique (definitions, termes techniques)
- Schemas et protocoles (identifier le montage correct)
- Formules (choisir la bonne formule pour un probleme)
- Securite et environnement (pictogrammes, regles)
- Ordres de grandeur (estimer, comparer)

**Interro PC — types de questions privilegies :**
- Applications numeriques (formules, conversions)
- Schemas a completer ou legender
- Questions de cours (definir, expliquer, citer)
- Petits problemes professionnels (1-2 etapes, contexte ICCER ou ERA)
- Analyse de documents simples (graphiques, tableaux de mesures)

---

## Regles de redaction

### Regles communes QCM et interro

1. **Ancrage pedagogique** : chaque question doit correspondre a une notion du `lecon.html` du meme chapitre
2. **Pas de hors-programme** : verifier les capacites attendues dans `/pdf/`
3. **Contextes professionnels** : respecter les regles de CLAUDE.md (pas de sigles de filiere dans le contenu)
4. **Variete des contextes** : professionnel + quotidien + scientifique + sport + sante
5. **Corrections pedagogiques** : expliquer le raisonnement, pas juste donner la reponse

### Regles specifiques QCM

1. **4 choix par question** (A, B, C, D) — jamais 2 ou 3
2. **Un seul choix correct** par question (pas de "plusieurs reponses possibles")
3. **Distracteurs plausibles** : les mauvaises reponses doivent correspondre a des erreurs frequentes, pas a des absurdites
4. **Feedback differencie** : un message si correct, un message different si incorrect (expliquant l'erreur)
5. **Pas de "toutes les reponses" ni "aucune reponse"** : chaque option doit etre une reponse concrete
6. **Formulations positives** : eviter les doubles negations ("Laquelle n'est PAS incorrecte ?")
7. **Questions independantes** : la reponse a Q5 ne doit pas dependre de Q4

### Regles specifiques interro

1. **Format imprimable** : tester l'impression avant validation (print.css)
2. **Bareme explicite** : chaque question affiche ses points
3. **Progression logique** : les questions vont du plus simple au plus complexe
4. **Espace de redaction** : laisser de la place pour ecrire (pas de page surchargee)
5. **Rappels methodologiques** (socle uniquement) : integres dans les blocs `.meth`
6. **Pas de QCM dans l'interro** : format redige uniquement (le QCM a sa propre page)

---

## Checklist avant publication

### QCM
- [ ] 15 questions par niveau (socle, standard, appro)
- [ ] 4 choix par question, 1 seul correct
- [ ] Feedback correct ET incorrect pour chaque question
- [ ] Score calcule et affiche
- [ ] Bouton "Recommencer" fonctionnel
- [ ] **Figures SVG présentes pour toute question portant sur un élément visuel** (graphique, oscillogramme, circuit, figure géométrique)
- [ ] **Conventions SVG respectées** (fill #ebf5ff, stroke #0056b3, labels #555)
- [ ] diff.js inclus et fonctionnel
- [ ] MathJax si formules
- [ ] print.css inclus
- [ ] Couleurs CSS conformes au theme matiere/niveau
- [ ] Questions ancrees au programme officiel

### Interro
- [ ] 5-8 questions par niveau (socle, standard, appro)
- [ ] Bareme explicite (points par question)
- [ ] Corrections completes (bouton "Voir la correction")
- [ ] **Figures SVG présentes pour toute question nécessitant un support visuel** (schéma à légender, graphique à lire, figure géométrique)
- [ ] **Conventions SVG respectées** (fill #ebf5ff, stroke #0056b3, labels #555)
- [ ] diff.js inclus et fonctionnel
- [ ] Rappels methodologiques pour le niveau socle
- [ ] MathJax si formules
- [ ] print.css inclus
- [ ] Impression testee (mise en page correcte)
- [ ] Couleurs CSS conformes au theme matiere/niveau
- [ ] Questions ancrees au programme officiel
