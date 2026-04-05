# Prompt — QCM et Interrogations

> ⚠ **Interdits absolus** (→ détails dans [`regles-communes.md`](regles-communes.md)) :
> 1. Les visuels montrent uniquement les données brutes — jamais la réponse ni le point à déterminer
> 2. Toute référence "le graphique ci-dessous" exige une figure présente dans la page
> 3. Canvas animé interdit (`requestAnimationFrame`, `setInterval`)
> 4. Dès 3 valeurs numériques → `<table class="full">` avant la question

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

### L'interrogation : outil de diagnostic rapide

L'interrogation est un outil **papier** distribué en classe. Courte (10-15 min), ciblée sur les notions essentielles, avec corrections disponibles en ligne.

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

**Socle :** reconnaissance immédiate, vocabulaire simple, calculs élémentaires, contextes du quotidien
**Standard :** application de formules dans un contexte, lecture de graphiques, vocabulaire technique, contextes professionnels
**Approfondissement :** raisonnement par déduction/élimination, croisement de notions, vocabulaire BTS, contextes complexes

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

**Important :** les fonctions `corriger()` et `reinitialiser()` sont définies dans `qcm.js` (lib partagée). Ne pas les réécrire dans la page. Seul `var explications = {...}` reste dans le `<script>` de la page.

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
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}
/* styles spécifiques QCM (q-block, options, score-box, etc.) */
</style>
</head>
<body>
<div class="c">
<a href="../../../[sommaire].html" class="nb">← Retour au sommaire</a>
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
<form id="qcm-socle">

<div class="q-block" data-correct="a">
  <h3>Question 1</h3>
  <p class="theme">Thème — notion testée</p>
  <p>Énoncé de la question ?</p>
  <div class="options">
    <label><input type="radio" name="s1" value="a"> Réponse A</label>
    <label><input type="radio" name="s1" value="b"> Réponse B</label>
    <label><input type="radio" name="s1" value="c"> Réponse C</label>
    <label><input type="radio" name="s1" value="d"> Réponse D</label>
  </div>
  <div class="q-feedback"></div>
</div>
<!-- Q2 à Q15 ... -->

<button type="button" class="btn-valider" onclick="corriger('qcm-socle','score-socle')">Valider le QCM</button>
<button type="button" class="btn-reset" onclick="reinitialiser('qcm-socle','score-socle')">Recommencer</button>
<div class="score-box" id="score-socle"></div>
</form>
</div>

<!-- === STANDARD === -->
<div class="diff-standard">
<span class="tag-standard">Standard</span>
<form id="qcm-standard">
<!-- 15 questions standard ... -->
<button type="button" class="btn-valider" onclick="corriger('qcm-standard','score-standard')">Valider le QCM</button>
<button type="button" class="btn-reset" onclick="reinitialiser('qcm-standard','score-standard')">Recommencer</button>
<div class="score-box" id="score-standard"></div>
</form>
</div>

<!-- === APPROFONDISSEMENT === -->
<div class="diff-appro">
<span class="tag-appro">Approfondissement</span>
<form id="qcm-appro">
<!-- 15 questions approfondissement ... -->
<button type="button" class="btn-valider" onclick="corriger('qcm-appro','score-appro')">Valider le QCM</button>
<button type="button" class="btn-reset" onclick="reinitialiser('qcm-appro','score-appro')">Recommencer</button>
<div class="score-box" id="score-appro"></div>
</form>
</div>

</div><!-- fin .c -->
<script>
/* Explications par question — clés = attribut name des radios */
var explications = {
  "s1": "Explication socle Q1...",
  /* ... toutes les clés s1–s15, t1–t15, a1–a15 */
};
</script>
<script src="../../../qcm.js"></script>
<script src="../../../nav.js"></script>
<script src="../../../diff.js"></script>
</body>
</html>
```

### Template `interro.html`

**Structure :** chaque niveau (socle/standard/appro) contient **2 sujets** (A et B) gérés par `sujet.js`. Chaque sujet est un `sujet-wrap` autonome, imprimable, barème /20.

**Règles CSS :** ne pas redéfinir `.corr` dans le `<style>` de la page — elle est déjà dans `styles.css`. Pour le comportement `display:none` par défaut, scoper la règle : `.sujet-body .corr { display:none }`.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – Interrogation écrite – Titre – Classe</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>
:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}

/* Bandeaux de niveau */
.level-banner{display:flex;align-items:flex-start;gap:14px;padding:14px 20px;border-radius:10px;margin:32px 0 16px;border-width:2px;border-style:solid}
.level-banner .lb-icon{font-size:1.5rem;flex-shrink:0}
.level-banner .lb-body h2{margin:0 0 3px;font-size:1.05rem;font-weight:700}
.level-banner .lb-body p{margin:0;font-size:.82rem;opacity:.9}
.lb-socle{background:#f0fdf4;border-color:#10b981;color:#064e3b}
.lb-standard{background:#eff6ff;border-color:#3b82f6;color:#1e3a8a}
.lb-appro{background:#f5f0ff;border-color:var(--p);color:#4c1d95}

/* Bloc sujet A / B */
.sujet-wrap{border:1px solid var(--p-border);border-radius:10px;margin-bottom:20px;overflow:hidden}
.sujet-header{display:flex;align-items:center;justify-content:space-between;background:var(--p);color:#fff;padding:10px 16px}
.sujet-header .sh-title{font-weight:700;font-size:.97rem}
.sujet-header .sh-meta{font-size:.82rem;opacity:.9}
.sujet-body{padding:14px 18px}

/* Questions */
.exo{margin-bottom:16px;padding-bottom:12px;border-bottom:1px dashed var(--p-border)}
.exo:last-child{border-bottom:none;margin-bottom:0;padding-bottom:0}
.exo h2{display:flex;align-items:center;gap:8px;font-size:.92rem;color:var(--p);margin:0 0 6px;font-weight:700}
.pts{display:inline-block;background:var(--p);color:#fff;border-radius:10px;padding:1px 9px;font-size:.75rem;font-weight:600}

/* Corrections — scoper pour éviter conflit avec styles.css global */
.sujet-body .corr{background:#f0fff4;border-left:3px solid #10b981;border-radius:0 8px 8px 0;padding:10px 14px;margin-top:8px;display:none}
.sujet-body .corr p,.sujet-body .corr li{font-size:.87rem;margin:3px 0}

/* Impression — corrections CACHÉES (sujet élève, pas corrigé) */
@media print{
  .nb,.bc{display:none}
  .sujet-wrap{break-inside:avoid}
  .level-banner{break-before:page}
}
</style>
</head>
<body>
<div class="c">
<a href="../../../[sommaire].html" class="nb">← Retour au sommaire</a>

<header>
  <h1>Chapitre X – Interrogation écrite</h1>
  <p class="sous-titre">Titre du chapitre — Matière — Niveau</p>
</header>

<div class="interro-meta">
  <div class="interro-meta-item"><strong>Durée :</strong> 10–15 minutes</div>
  <div class="interro-meta-item"><strong>Barème :</strong> /20 points par sujet</div>
  <div class="interro-meta-item"><strong>Niveaux :</strong> Socle · Standard · Approfondissement</div>
</div>

<!-- ========================= SOCLE ========================= -->
<div class="diff-socle">

<div class="level-banner lb-socle">
  <div class="lb-icon">🟢</div>
  <div class="lb-body">
    <h2>Niveau Socle</h2>
    <p>Questions guidées — rappels fournis — réponses courtes</p>
  </div>
</div>

<!-- SOCLE SUJET A -->
<div class="sujet-a">
<div class="sujet-wrap">
<div class="sujet-header">
  <span class="sh-title">Sujet A</span>
  <span class="sh-meta">Barème : /20 pts — Durée 10–15 min</span>
</div>
<div class="sujet-body">

<div class="exo">
  <h2>Question 1 <span class="pts">4 pts</span></h2>
  <div class="meth"><strong>Rappel :</strong> aide méthodologique (socle uniquement)</div>
  <p>Consigne guidée, étape par étape...</p>
  <button class="bc" onclick="this.nextElementSibling.style.display='block'">Voir la correction</button>
  <div class="corr">Correction détaillée.</div>
</div>
<!-- Q2 à Q5 ... total = 20 pts -->

</div></div>
</div><!-- fin sujet-a -->

<!-- SOCLE SUJET B -->
<div class="sujet-b">
<div class="sujet-wrap">
<div class="sujet-header">
  <span class="sh-title">Sujet B</span>
  <span class="sh-meta">Barème : /20 pts — Durée 10–15 min</span>
</div>
<div class="sujet-body">
<!-- questions sujet B ... -->
</div></div>
</div><!-- fin sujet-b -->

</div><!-- fin diff-socle -->

<!-- ========================= STANDARD ========================= -->
<div class="diff-standard">
<div class="level-banner lb-standard">
  <div class="lb-icon">🔵</div>
  <div class="lb-body"><h2>Niveau Standard</h2><p>...</p></div>
</div>
<!-- sujet-a + sujet-b ... -->
</div><!-- fin diff-standard -->

<!-- ========================= APPROFONDISSEMENT ========================= -->
<div class="diff-appro">
<div class="level-banner lb-appro">
  <div class="lb-icon">🟣</div>
  <div class="lb-body"><h2>Niveau Approfondissement</h2><p>...</p></div>
</div>
<!-- sujet-a + sujet-b ... -->
</div><!-- fin diff-appro -->

</div><!-- fin .c -->
<script src="../../../nav.js"></script>
<script src="../../../diff.js"></script>
<script src="../../../sujet.js"></script>
</body>
</html>
```

---

## Figures et schémas dans les QCM et interrogations

### Distinction fondamentale : QCM (écran) vs interro (papier)

| | QCM (`qcm.html`) | Interro (`interro.html`) |
|---|---|---|
| **Support** | Écran — numérique | Papier — imprimé |
| **Visuels autorisés** | SVG statique uniquement | SVG statique uniquement |
| **Interactivité** | Boutons de réponse (géré par `qcm.js`) | Aucune |
| **Chart.js statique** | ✓ Acceptable (rendu une fois) | ✓ Acceptable |
| **Canvas animé** | ❌ Non — réservé aux leçons/simulations | ❌ Non |
| **Données en tableau** | `<table class="full">` | `<table class="full">` |

**Remarque :** même le QCM n'utilise pas Chart.js pour les figures de questions — les courbes/graphiques sont des SVG statiques. Chart.js et Canvas restent réservés aux **leçons** et **simulations**.

### Règle fondamentale — données uniquement

→ Règle complète avec exemples dans [`regles-communes.md`](regles-communes.md)

Points spécifiques au QCM/interro :
- **QCM** : le visuel fait partie de l'énoncé, pas des options A/B/C/D ; ne jamais tracer le point d'intersection
- **Interro** : pour un graphique à lire, fournir la courbe sans marquer le point de lecture ; pour un schéma à compléter, laisser les éléments manquants en pointillés

> *"L'élève doit lire ou compléter le visuel — pas le recopier."*

### Règle absolue

**Si une question porte sur un élément visuel, la figure SVG DOIT être présente dans la question.** Ne jamais écrire "le graphique ci-dessous montre..." sans fournir le graphique.

### Quand une figure est OBLIGATOIRE

Dès que la question porte sur : lecture graphique, courbe, oscillogramme, schéma électrique, bilan de forces, figure géométrique, spectre, tableau de mesures. Si la question cite un objet visuel, la figure SVG doit être dans la page.

### Style SVG à respecter

Les SVG dans les interros utilisent la classe `.svg-it` qui charge les styles partagés définis dans le `<style>` de la page. Ne pas mettre de styles inline sur les éléments SVG si la classe CSS couvre le cas.

**Classes SVG disponibles dans interro.html :**

| Classe | Usage |
|---|---|
| `.svg-it` | Sur le `<svg>` — active tous les styles enfants |
| `.curve-ctn` | Courbe R(T) d'une CTN (stroke violet, no fill) |
| `.curve-t` | Courbe T(t) d'un thermocouple (même style) |
| `.pt-ctn` / `.pt-t` | Points sur la courbe (fill violet) |
| `.seuil-line` | Ligne de seuil (tirets rouges) |
| `.readoff-h` / `.readoff-v` | Lignes de lecture graphique (tirets bleus) |

```html
<!-- SVG inline dans une question d'interro -->
<svg class="svg-it" viewBox="0 0 300 160" style="width:100%;max-width:300px;display:block;margin:.5em auto 0" aria-label="Description">
  <!-- axes, ticks, labels ... -->
  <polyline class="curve-ctn" points="50,24 104,91 157,114 211,123 265,126"/>
  <circle class="pt-ctn" cx="50" cy="24" r="3.5"/>
  <line class="seuil-line" x1="50" y1="91" x2="265" y2="91"/>
  <line class="readoff-h" x1="50" y1="114" x2="157" y2="114"/>
  <line class="readoff-v" x1="157" y1="114" x2="157" y2="135"/>
</svg>
```

**Conventions de couleur selon la matière :**

| Matière | Couleur principale | Usage |
|---|---|---|
| Maths Seconde | `#0056b3` | fill axes, stroke courbe |
| PC Seconde | `#6f42c1` | fill axes, stroke courbe |
| Maths Première/Terminale | `#0969da` | fill axes, stroke courbe |

Pour les interros PC, utiliser `var(--p)` et `#7c3aed` (violet foncé) pour les courbes — pas `#0056b3` (qui est pour les maths).

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
- Petits problemes professionnels (1-2 etapes, contexte professionnel — ne jamais utiliser les sigles ICCER, ERA, MAMA dans le contenu)
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
- [ ] 4 choix par question (valeurs `a/b/c/d` en minuscules), 1 seul correct
- [ ] `data-correct="a"` sur chaque `.q-block`
- [ ] `<div class="q-feedback"></div>` présent sur chaque `.q-block` (vide — rempli par `qcm.js`)
- [ ] `var explications = {...}` défini dans un `<script>` avant `qcm.js`
- [ ] `<script src="../../../qcm.js"></script>` inclus (avant nav.js)
- [ ] Boutons `corriger('qcm-socle','score-socle')` et `reinitialiser(...)` — **pas** `evaluerQCM()` ni `resetQCM()`
- [ ] Chaque niveau dans un `<form id="qcm-socle/standard/appro">`
- [ ] Score affiché dans `<div class="score-box" id="score-socle/standard/appro">`
- [ ] **Figures SVG présentes pour toute question portant sur un élément visuel**
- [ ] **Conventions SVG conformes à la matière** (PC Seconde : `#6f42c1`, Maths : `#0056b3`)
- [ ] **Tableaux de données** pour toute question avec valeurs numériques (avant les options)
- [ ] **Les visuels montrent uniquement les données** — jamais la réponse ni le point de lecture
- [ ] **Aucun Canvas animé** — Chart.js statique acceptable, animations Canvas interdites
- [ ] Aucune référence orpheline ("le graphique ci-dessous" sans figure)
- [ ] diff.js inclus et fonctionnel
- [ ] MathJax si formules
- [ ] print.css inclus
- [ ] Lien retour → `../../../[sommaire].html` (pas `../../sommaire.html`)
- [ ] Couleurs CSS conformes au thème matière/niveau
- [ ] Questions ancrées au programme officiel

### Interro
- [ ] 5 questions par niveau (barème /20 pts par sujet)
- [ ] 2 sujets (A et B) par niveau — `sujet.js` inclus en fin de `<body>`
- [ ] Structure `diff-socle / diff-standard / diff-appro` avec `level-banner` pour chaque niveau
- [ ] Chaque sujet dans `sujet-a` / `sujet-b` → `sujet-wrap` → `sujet-header` + `sujet-body`
- [ ] Barème explicite par question (`<span class="pts">X pts</span>`) — total = 20 pts par sujet
- [ ] Corrections complètes (bouton `.bc` + `<div class="corr">`)
- [ ] `.corr` **non redéfinie** globalement — utiliser `.sujet-body .corr { display:none }` pour scoper
- [ ] **Figures SVG présentes pour toute question nécessitant un support visuel** — utiliser la classe `.svg-it`
- [ ] **Conventions SVG conformes à la matière** (PC Seconde : `#6f42c1` / `#7c3aed`, Maths : `#0056b3`)
- [ ] **Tableaux de données** pour toute question avec valeurs numériques (avant les sous-questions)
- [ ] **Les visuels montrent uniquement les données** — jamais la réponse, le point de lecture, ou la valeur à trouver
- [ ] **Aucun Chart.js / Canvas** — interro = papier imprimé, SVG statique uniquement
- [ ] Aucune référence orpheline ("le graphique ci-dessous" sans figure)
- [ ] Rappels méthodologiques (`.meth`) pour le niveau socle uniquement
- [ ] diff.js inclus
- [ ] sujet.js inclus
- [ ] MathJax si formules
- [ ] print.css inclus
- [ ] `@media print` : corrections **NON affichées** (pas de `.corr{display:block!important}`) — l'élève imprime son sujet sans corrections
- [ ] Lien retour → `../../../[sommaire].html` (pas `../../sommaire.html`)
- [ ] Couleurs CSS conformes au thème matière/niveau
- [ ] Questions ancrées au programme officiel
