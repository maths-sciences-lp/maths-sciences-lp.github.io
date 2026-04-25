# CLAUDE.md — Site pédagogique Maths & Sciences LP

Espace pédagogique pour les classes de Bac Professionnel (Seconde, Première, Terminale) et BTS.
Ce fichier est lu automatiquement par Claude Code à chaque session.

**État du site (avril 2026) :** cours, exercices corrigés, devoirs surveillés, QCM, fiches de révision, activités de découverte, simulations interactives et automatismes.

---

## STRUCTURE DU DÉPÔT

```
/
├── styles.css                  ← Feuille de style partagée (NE PAS supprimer)
├── print.css                   ← Feuille de style d'impression (A4, polycopiés)
├── nav.js                      ← Navigation auto-générée (NE PAS modifier sans raison)
├── nav.css                     ← Styles de navigation
├── diff.js                     ← Toggle différenciation pédagogique (socle/standard/appro)
├── qcm.js                     ← Fonctions partagées pour les QCM interactifs
├── comp.js                    ← Filtrage par capacité (exercices-capacites.html)
├── sujet.js                   ← Toggle Sujet A / Sujet B (interrogations)
├── index.html                  ← Page d'accueil
├── maths-*.html / pc-*.html    ← Pages sommaire par matière/niveau
├── maths/
│   ├── seconde/ch01..ch14/
│   ├── premiere/ch01..ch09/
│   ├── terminale/ch01..ch11/
│   ├── lgt-terminale/ch01..ch15/   ← Terminale LGT (voie générale/technologique)
│   ├── cap/ch01..ch07/             ← CAP (groupement 1 : MIT, Ébéniste, SDG)
│   └── bts/ch01..ch25/             ← Cours BTS (maths uniquement)
├── physique-chimie/
│   ├── seconde/ch01..ch14/
│   ├── premiere-iccer/ch01..ch10/  ← groupement 1 (ICCER)
│   ├── premiere-era/ch01..ch10/    ← groupement 3 (ERA-MA)
│   ├── premiere-gpt2/ch01../       ← groupement 2 (en construction)
│   ├── premiere-gpt4/ch01../       ← groupement 4 (en construction)
│   ├── premiere-gpt6/ch01../       ← groupement 6 (en construction)
│   ├── terminale-iccer/ch01..ch08/
│   ├── terminale-era/ch01..ch08/
│   ├── terminale-gpt2/ch01../      ← groupement 2 (en construction)
│   ├── terminale-gpt4/ch01../      ← groupement 4 (en construction)
│   ├── terminale-gpt5/ch01../      ← groupement 5 (en construction)
│   └── cap/ch01..ch07/             ← CAP physique-chimie (programme commun)
├── simulations/                ← Pages interactives (Canvas/SVG/JS) — 70 simulations
├── automatismes/               ← Exercices d'entraînement rapide par thème — 22 pages
├── co-intervention/            ← Séances de co-intervention maths/sciences (38 pages, ICCER/ERA-MA)
├── prompts/                    ← Prompts pédagogiques de référence
├── pdf/                        ← Documents officiels
│   ├── programmes/             ← Programmes scolaires (PDF + extractions .md)
│   ├── referentiels/           ← Référentiels professionnels par filière
│   └── vademecums/             ← Vademecums 2nde (familles de métiers)
├── audits/                     ← Audits qualité (documents vivants)
├── latex/                      ← Sources LaTeX (local, gitignored) — livrets, DS, co-intervention
│   ├── seconde/                ← Livrets, DS, co-intervention Seconde
│   ├── cap/                    ← Cours CAP
│   ├── terminale/              ← Cours Terminale
│   ├── ccf/                    ← Convocations CCF
│   └── livre-caplp/            ← Préparation CAPLP
├── scripts/                    ← Outils de maintenance
│   ├── extract_css.py          ← Nettoyage CSS doublons
│   ├── add_print_css.py        ← Ajout automatique de print.css aux pages
│   ├── generate-pdf.js         ← Génération PDF des cours
│   ├── link_simulations.py     ← Liaison simulations ↔ chapitres
│   ├── check_chapters.py       ← Vérification complétude des chapitres
│   └── telecharger_pdfs.py     ← Téléchargement des PDF programmes
└── .claude/commands/           ← Commandes personnalisées Claude Code (skills)
```

### Structure d'un chapitre (`subject/level/chNN/`)

Chaque dossier de chapitre peut contenir les fichiers suivants :

| Fichier | Rôle | Présence |
|---|---|---|
| `lecon.html` | Cours (identique pour tous les élèves) | **Obligatoire** — tous les chapitres |
| `exercices.html` | Exercices d'entraînement (différenciés socle/standard/appro) | **Obligatoire** — tous les chapitres |
| `ds.html` | Devoir surveillé (différencié socle/standard/appro) | **Obligatoire** — tous les chapitres |
| `fiche.html` | Fiche de révision / mémo du chapitre | Standard — majorité des chapitres |
| `qcm.html` | QCM interactif avec correction automatique et score (différencié) | Optionnel — à créer pour chaque chapitre |
| `interro.html` | Interrogation écrite courte, 10-15 min, barème /20 (différenciée) | Optionnel — à créer pour chaque chapitre |
| `exercices-capacites.html` | Exercices organisés par capacités du programme (filtrage comp.js) | Standard — 14/14 en Seconde maths |
| `activite.html` | Activité de découverte (situation-problème guidée vers la notion) | Optionnel — recommandé |
| `simulation.html` | Simulation interactive liée au chapitre | Optionnel — si pertinent |

**Objectif :** chaque chapitre devrait à terme contenir les 8 fichiers ci-dessus.

### Pages sommaire (racine)

Les pages de type `maths-2nde-mama.html`, `pc-1ere-iccer.html`, etc. servent de sommaire par matière/niveau. Elles listent les chapitres avec liens vers leçons, exercices, DS, etc.

Les pages sommaire existantes :
- `maths-2nde-mama.html` — Maths Seconde Pro (MAMA)
- `maths-1ere-pro.html` — Maths Première Pro
- `maths-term-iccer.html` — Maths Terminale ICCER
- `maths-term-erama.html` — Maths Terminale ERA-MA
- `maths-lgt-terminale.html` — Maths Terminale LGT
- `maths-cap.html` — Maths CAP
- `maths-bts.html` — Maths BTS
- `pc-2nde-pro.html` — PC Seconde Pro
- `pc-1ere-iccer.html` — PC Première ICCER
- `pc-1ere-erama.html` — PC Première ERA-MA
- `pc-1ere-gpt2.html` / `pc-1ere-gpt4.html` / `pc-1ere-gpt6.html` — PC Première Gpts 2/4/6
- `pc-term-iccer.html` — PC Terminale ICCER
- `pc-term-erama.html` — PC Terminale ERA-MA
- `pc-term-gpt2.html` / `pc-term-gpt4.html` / `pc-term-gpt5.html` — PC Terminale Gpts 2/4/5
- `pc-cap.html` — PC CAP

**Conventions communes aux pages sommaire** (à respecter / déployer) :

- **Fil d'Ariane** : `<nav>` en haut de page avec deux niveaux (`Accueil › <Matière — Niveau Filière>`). La couleur du libellé courant doit utiliser la variable `var(--primary)` du thème de la page (jamais une couleur en dur incohérente avec le thème).
- **Timestamp** `<p class="maj">` dans le `<header>` (règle #10) — au même titre que les pages chapitres.
- **`<meta name="description">`** dans le `<head>` (1 phrase courte décrivant la matière + le niveau + la filière).
- **Tous les liens vers les fichiers chapitres** (`activite.html`, `lecon.html`, `exercices.html`, `exercices-capacites.html`, `ds.html`, `fiche.html`, `qcm.html`, `interro.html`) avec un ordre uniforme.
- **Liens « Simulation »** (classe `link-sim`) vers les simulations rattachées au chapitre, quand il y en a.

Autres pages utilitaires à la racine :
- `simulations.html` — Index des simulations interactives
- `groupements.html` — Groupements de filières Bac Pro
- `ccf-convocations.html` — Convocations CCF
- `cv-eleve.html` — Générateur de CV élève
- `lettre-motivation-parcoursup.html` — Aide à la rédaction Parcoursup
- `python.html` — Fragment Python (inclus dans les sommaires maths)
- `logique.html` — Fragment Logique (inclus dans les sommaires maths)

### Section BTS (`maths/bts/`)

25 chapitres de mathématiques pour BTS. Même structure que les chapitres Bac Pro mais sans différenciation pédagogique (pas de diff.js).

### Automatismes (`automatismes/`)

22 pages d'exercices d'entraînement rapide (calcul mental, automatismes) organisées par niveau et thème. Pages autonomes avec leur propre `index.html`.

---

## CLASSES CSS — RÈGLES IMPORTANTES

**`styles.css` est la feuille de style centrale.** Toutes les classes communes y sont définies.

Chaque page de cours utilise :
```html
<link rel="stylesheet" href="../../../styles.css">
<style>:root{--p:#0056b3;--p-bg:#ebf5ff;--p-border:#bee3f8}</style>
```

### Thèmes couleur par matière/niveau

| Dossier | `--p` | `--p-bg` | `--p-border` |
|---|---|---|---|
| `maths/seconde` | `#0056b3` | `#ebf5ff` | `#bee3f8` |
| `maths/premiere` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `maths/terminale` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `maths/lgt-terminale` | `#4f46e5` | `#eef2ff` | `#a5b4fc` |
| `maths/cap` | `#b45309` | `#fffbeb` | `#fde68a` |
| `physique-chimie/seconde` | `#6f42c1` | `#f5f0ff` | `#c4b5fd` |
| `physique-chimie/premiere-iccer` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/premiere-era` | `#2da44e` | `#f0fff4` | `#86efac` + `--s:#0ea5e9` |
| `physique-chimie/premiere-gpt2/4/6` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/terminale-iccer` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/terminale-era` | `#2da44e` | `#f0fff4` | `#86efac` + `--s:#0ea5e9` |
| `physique-chimie/terminale-gpt2/4` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/terminale-gpt5` | `#059669` | `#ecfdf5` | `#86efac` |
| `physique-chimie/cap` | `#6f42c1` | `#f5f0ff` | `#c4b5fd` |

### Classes pédagogiques disponibles dans styles.css

| Classe | Usage |
|---|---|
| `.def` | Définition (fond bleu/couleur primaire) |
| `.prop` | Propriété (fond vert) |
| `.att` | Attention/erreur fréquente (fond rouge) |
| `.meth` | Méthode (fond orange) |
| `.retenir` | Encadré "À retenir" (bordure verte) |
| `.ex` | Exemple expliqué |
| `.exo` | Exercice |
| `.corr` | Correction cachée (display:none) |
| `.bc` | Bouton "Voir la correction" |
| `.label-def/prop/att/meth` | Badge de type de bloc |
| `.situation` | Situation professionnelle (fond violet pointillé) |
| `.objectifs` | Objectifs du chapitre |
| `.formule-box` / `.formula-box` | Encadré formule |
| `.mini-exo` | Exercice d'application intégré dans la leçon (bordure gauche couleur primaire) |
| `.niveau-header .niv1/2/3/4` | En-tête de niveau de difficulté |
| `.chart-wrap` | Conteneur graphique Chart.js |
| `.svg-wrap` | Conteneur SVG centré |
| `.anim-wrap` | Conteneur animation/Canvas |
| `.grid2` / `.deux-col` | Grille 2 colonnes |
| `.badge-green/blue/yellow/red` | Badges colorés |
| `.erreur-item` | Bloc "Erreur fréquente" (icône ❌ + texte + conseil) dans les sections `.att` |

**Ne jamais redéfinir ces classes dans un `<style>` inline** — elles sont déjà dans styles.css.
Seules les classes vraiment spécifiques à une page peuvent rester inline.

---

## CRÉATION D'UNE NOUVELLE PAGE

### Template HTML minimal

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Ch0X – Titre – Classe</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Chapitre X – Titre</h1>
  <p class="sous-titre">Niveau | Matière | Module</p>
</header>
<!-- contenu -->
</div>
<script src="../../../nav.js"></script>
</body>
</html>
```

### Chemin vers styles.css selon la profondeur
- Pages dans `subject/level/chNN/` → `../../../styles.css`
- Pages dans `simulations/` → `../styles.css`
- Pages à la racine → `styles.css`

---

## DIFFÉRENCIATION PÉDAGOGIQUE (Seconde, Première & Terminale)

### Philosophie

La différenciation s'applique aux **trois niveaux du lycée professionnel** : Seconde, Première et Terminale.

Elle apparaît principalement dans les **exercices (exercices.html)**, les **DS (ds.html)** et les **activités**.
Les cours (lecon.html) restent **identiques pour tous** : le programme est le même, c'est le socle commun de savoir. Le cours doit rester clair et accessible à tous les élèves. La différenciation ne porte pas sur le savoir transmis mais sur le **niveau de pratique** :
- On ne simplifie pas le cours pour les élèves en difficulté — on leur donne un cours identique avec des exercices plus guidés.
- On n'ajoute pas de théorie supplémentaire pour les élèves en poursuite — on leur donne des exercices plus ouverts et formalisés.
- Ne jamais créer de « cours au rabais » : un élève socle doit avoir accès au même savoir pour pouvoir progresser.

### Formes de différenciation

La différenciation peut prendre plusieurs formes :

1. **Niveau de difficulté progressif** : exercices de base → intermédiaires → avancés
2. **Variété des contextes** : professionnels, scientifiques, vie quotidienne
3. **Aides pédagogiques** : indices, rappels de méthode, étapes guidées
4. **Parcours possibles** : exercices accessibles à tous + exercices d'approfondissement pour les élèves plus à l'aise

### Les 3 niveaux

| Niveau | Profil cible | Contenu (exercices & DS) |
|---|---|---|
| **Socle** | Élèves en difficulté | Exercices très guidés, étape par étape, calculs amorcés, tableaux pré-remplis |
| **Standard** | Majorité de la classe | Exercices du programme, contextes pro variés, rédaction attendue |
| **Approfondissement** | Poursuite BTS/MC | Problèmes ouverts, mise en équation autonome, questions type BTS |

### Mise en place sur une page

1. Ajouter `<script src="../../../diff.js"></script>` avant `</body>` (après nav.js)
2. Tagger les blocs avec les classes CSS :

```html
<!-- Visible par tous (pas de classe diff) = tronc commun -->
<div class="exo">Exercice commun</div>

<!-- Seulement niveau Socle -->
<div class="exo diff-socle">
  <span class="tag-socle">Socle</span>
  Exercice très guidé, étape par étape...
</div>

<!-- Seulement niveau Standard -->
<div class="exo diff-standard">
  <span class="tag-standard">Standard</span>
  Exercice classique du programme...
</div>

<!-- Seulement niveau Approfondissement -->
<div class="exo diff-appro">
  <span class="tag-appro">Approfondissement</span>
  Exercice ouvert type BTS...
</div>
```

**Ne PAS utiliser diff.js ni les classes diff-* sur les pages lecon.html.**

### Classes CSS disponibles

| Classe | Usage |
|---|---|
| `.diff-socle` | Bloc visible uniquement en mode Socle |
| `.diff-standard` | Bloc visible uniquement en mode Standard |
| `.diff-appro` | Bloc visible uniquement en mode Approfondissement |
| `.tag-socle` | Badge vert "Socle" |
| `.tag-standard` | Badge bleu "Standard" |
| `.tag-appro` | Badge violet "Approfondissement" |

### Comportement
- Le toggle apparaît automatiquement si la page contient des blocs `.diff-socle`, `.diff-standard` ou `.diff-appro`
- Le choix est mémorisé en `localStorage` (persistant entre les pages)
- Le bouton "Tout voir" affiche tous les blocs (mode prof)
- Sans `diff.js`, tous les blocs restent visibles (dégradation gracieuse)

### Principes de rédaction par niveau
- **Socle** : consignes décomposées, calculs intermédiaires donnés, tableaux pré-remplis, contextes du quotidien
- **Standard** : consignes complètes, contextes professionnels variés, rédaction attendue
- **Approfondissement** : mise en équation autonome, problèmes à étapes, questions ouvertes, vocabulaire BTS

---

## PROMPTS PÉDAGOGIQUES DE RÉFÉRENCE

Avant de générer du contenu, consulter les fichiers dans `/prompts/` :

| Fichier | Usage |
|---|---|
| `prompts/regles-communes.md` | Règles partagées — données uniquement, tableaux, références orphelines, animations Canvas, conventions SVG |
| `prompts/prompt-cours.md` | Structure d'une page de cours |
| `prompts/prompt-exercices.md` | Structure d'une page d'exercices |
| `prompts/prompt-exercices-capacites.md` | Structure d'une page d'exercices par capacités du programme (`exercices-capacites.html`) |
| `prompts/prompt-ds.md` | Structure d'un devoir surveillé (`ds.html`) — différenciation, compétences, visuels, corrections |
| `prompts/prompt-qcm-interro.md` | Structure d'un QCM ou d'une interrogation |
| `prompts/prompt-activite.md` | Structure d'une activité de découverte (`activite.html`) |
| `prompts/prompt-fiche.md` | Structure d'une fiche de révision (`fiche.html`) |
| `prompts/prompt-simulation.md` | Structure d'une simulation interactive (4 types) |
| `prompts/prompt-superviseur.md` | Prompt de supervision globale du projet |
| `prompts/prompt-filiere-2mama.md` | Contextes pro Seconde MAMA (menuiserie/agencement) |
| `prompts/prompt-filiere-2tne.md` | Contextes pro Seconde TNE (transitions numérique et énergétique) |
| `prompts/prompt-filiere-premiere-era.md` | Contextes pro Première ERA-MA (bois/agencement) |
| `prompts/prompt-filiere-premiere-iccer.md` | Contextes pro Première ICCER (chauffage/énergie) |
| `prompts/prompt-filiere-era-ma.md` | Contextes pro Terminale ERA/MA (agencement/bois) |
| `prompts/prompt-filiere-ticcer.md` | Contextes pro Terminale ICCER (chauffage/énergie) |
| `prompts/prompt-filiere-mee.md` | Contextes pro MEE (maintenance énergétique) |
| `prompts/prompt-filiere-eeb-tgt.md` | Contextes pro EEB / TGT (bâtiment, géomètre) |
| `prompts/prompt-filiere-cap-mit.md` | Contextes pro CAP MIT (installations thermiques) |
| `prompts/prompt-filiere-cap-ebeniste.md` | Contextes pro CAP Ébéniste (bois, mobilier) |
| `prompts/prompt-filiere-cap-sdg.md` | Contextes pro CAP SDG (signalétique, décors graphiques) |
| `prompts/prompt-filiere-bma-ebeniste.md` | Contextes pro BMA Ébéniste (ébénisterie d'art) |
| `prompts/prompt-filiere-bma-arts-graphiques.md` | Contextes pro BMA Arts Graphiques option A (signalétique) |
| `prompts/prompt-bts.md` | Structure et règles pour les pages BTS maths |
| `prompts/prompt-caplp-cours.md` | Prompt de préparation CAPLP maths-sciences |
| `prompts/prompt-cours-universel.md` | Prompt LaTeX universel pour générer un livret de cours (Overleaf) |
| `prompts/prompt-exercices-universel.md` | Prompt LaTeX universel pour générer un livret d'exercices avec corrections (Overleaf) |
| `prompts/instructions-co-intervention-ICCER.md` | Instructions co-intervention maths/sciences ICCER |
| `prompts/instructions-co-intervention-ERA.md` | Instructions co-intervention maths/sciences ERA |
| `prompts/instructions-co-intervention-MA.md` | Instructions co-intervention maths/sciences MA |

### Règles contextes professionnels

**RÈGLE ABSOLUE : Ne JAMAIS utiliser les sigles de filière (ICCER, ERA, MA, ERA-MA, MAMA) comme noms de métiers dans le contenu.**

Ces sigles sont des noms de formations scolaires, pas des métiers réels. Ils ne doivent apparaître que dans :
- les titres de pages (`<title>`, `<h1>`)
- les sous-titres identifiant la classe (`<p class="sous-titre">`)
- les liens de navigation (`← RETOUR SOMMAIRE`)
- les badges visuels (`<span class="ticcer-badge">`, `<span class="erama-badge">`)

**Interdit dans le contenu pédagogique :**
- ~~"Un technicien ICCER installe..."~~ → **"Un installateur thermique installe..."**
- ~~"Un technicien ERA-MA effectue..."~~ → **"Un menuisier agenceur effectue..."**
- ~~"Vous êtes technicien ERA-MA dans..."~~ → **"Vous êtes technicien d'agencement dans..."**
- ~~"Un technicien MAMA prépare un devis..."~~ → **"Un métreur prépare un devis..."**
- ~~"Contexte ERA-MA"~~ → **"Contexte professionnel"** ou **"Contexte menuiserie"**
- ~~"Application ERA-MA"~~ → **"Application en agencement"**
- ~~"Utilisations en ERA-MA"~~ → **"Utilisations en agencement"**
- ~~"Exemple ERA-MA"~~ → **"Exemple professionnel"**
- ~~"Lien ERA-MA"~~ → **"Application professionnelle"** ou **"Lien métier"**

**Métiers réels à utiliser :**

| Filière | Métiers à utiliser |
|---|---|
| ICCER | plombier chauffagiste, installateur thermique, technicien chauffagiste, technicien climatisation, technicien CVC, technicien de maintenance énergétique, installateur de pompes à chaleur, technicien en énergies renouvelables |
| ERA / MA | menuisier, menuisier agenceur, ébéniste, fabricant de meubles, installateur d'agencement, poseur de cuisines, artisan menuisier, aménageur d'intérieur, technicien d'agencement |
| MAMA (Seconde) | menuisier, métreur, artisan menuisier, fabricant de mobilier |

**Autres règles :**
- Varier les contextes : professionnel + sport + science + quotidien + énergie + santé + climat
- On peut aussi utiliser des métiers plus qualifiés : ingénieur thermicien, architecte d'intérieur, chef de chantier, conducteur de travaux, etc.

---

## PROGRAMMES OFFICIELS ET RÉFÉRENTIELS

Le dossier `/pdf/` est organisé en 3 sous-dossiers. Voir `pdf/README.md` pour l'inventaire complet.

### Programmes scolaires (`pdf/programmes/`)

- Maths Bac Pro : Seconde (2019), Première (2020), Terminale (2020)
- PC Bac Pro : Seconde (2019), Première (2020), Terminale (2020)
- CAP : maths (2019) + sciences (2019)
- BMA : maths (2021) + PC (2021)
- BTS : maths
- Extractions `.md` exploitables : maths + PC Bac Pro (3 niveaux), CAP, BMA, BTS, PC 6 groupements

### Référentiels de filières (`pdf/referentiels/`)

| Pôle | Filière | Fichier |
|---|---|---|
| **Énergie** | Bac Pro ICCER | `referentiel-bcp-iccer.pdf` |
| | Bac Pro MEE | `referentiel-bcp-mee.pdf` |
| | CAP MIT | `referentiel-cap-mit.pdf` |
| **Bois** | Bac Pro TMA | `referentiel-bcp-tma.pdf` |
| | Bac Pro ERA | `referentiel-bcp-era-reglement-examen.pdf` (réf. complet sur [Legifrance](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000023894109/)) |
| | CAP Ébéniste | `referentiel-cap-ebeniste.pdf` |
| | BMA Ébéniste | `referentiel-bma-ebeniste-annexe-*.pdf` (6 annexes) |
| **Arts graphiques** | CAP SDG | `referentiel-cap-sdg.pdf` |
| | BMA Arts Graphiques | `referentiel-bma-arts-graphiques.pdf` |
| **Bâtiment** | Bac Pro EEB | `referentiel-bcp-eeb.pdf` (complet) + `eeb-activites.pdf` / `eeb-certification.pdf` |
| | Bac Pro Géomètre (TGT) | `referentiel-bcp-geometre.pdf` |

### Vademecums Seconde (`pdf/vademecums/`)

| Famille | Fichier | Débouchés |
|---|---|---|
| 2nde MAMA | `vademecum-...-agencement-...-70002.pdf` | → ERA, TMA |
| 2nde TNE | `vademecum-...-transitions-...-70029.pdf` | → ICCER, MEE |
| 2nde Bâtiment | `vademecum-...-batiment-68028.pdf` | → EEB, TGT |

Vérifier les notions avant de créer du contenu : respecter les capacités attendues et ne pas introduire de hors-programme.

---

## SIMULATIONS INTERACTIVES

Les simulations sont dans le dossier `simulations/`. Elles sont autonomes (styles inline, pas de `styles.css` ni `nav.js`).

Consulter `prompts/prompt-simulation.md` pour les 4 types de simulations, le template HTML et les conventions.

### Règle fondamentale : ancrage pédagogique

**Toute simulation doit être en lien direct avec un chapitre, une classe et le programme officiel.**

Avant de créer ou modifier une simulation :
1. **Analyser la page du chapitre concerné** (lecon.html) pour identifier les notions
2. **Vérifier le programme officiel** dans `/pdf/` pour confirmer que la notion est au programme
3. **Concevoir la simulation** pour qu'elle illustre, exploite ou prolonge une notion réellement étudiée

Une simulation doit toujours servir à :
- illustrer une notion du cours
- accompagner un exercice ou un TP numérique
- faire manipuler un modèle mathématique ou physique du programme

**Interdit :** créer une simulation déconnectée du contenu pédagogique existant ou hors-programme.

---

## RÈGLES DE DÉVELOPPEMENT

1. **Ne jamais modifier `nav.js`** sans raison explicite — il gère toute la navigation
2. **Ne jamais redéfinir les classes de `styles.css`** dans les pages
3. **Respecter la structure des dossiers** : `subject/level/chNN/pagetype.html`
4. **Ajouter `<script src="../../../nav.js"></script>`** en fin de `<body>` sur toutes les pages de cours
5. **Ajouter `<link rel="stylesheet" href="../../../print.css">`** pour le support impression
6. **QCM** : inclure `<script src="../../../qcm.js"></script>` dans les pages `qcm.html` — définir un objet global `explications` avec les clés correspondant aux `name` des radios
7. **Chart.js** : `<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>` si graphiques
8. **MathJax** : inclure le script si la page contient des formules mathématiques
9. **Exercices d'application dans les leçons** : utiliser la classe `.mini-exo` pour les exercices courts intégrés dans le déroulé du cours — 3 à 6 par chapitre, répartis après les définitions/propriétés/méthodes, avec correction `.bc` obligatoire. Ne pas regrouper en fin de leçon.
10. **Timestamp « Dernière mise à jour »** : à chaque modification d'une page, ajouter/mettre à jour une ligne `<p class="maj">Dernière mise à jour : J mois AAAA, HH:MM</p>` à l'intérieur du `<header>`, juste après le dernier `<p class="sous-titre">`. Format français, date et heure locale au moment de l'édition. La classe `.maj` est déjà définie dans `styles.css` (petit, gris, italique, centré). Sert au suivi du travail.

### Scripts de maintenance

| Script | Usage |
|---|---|
| `python3 scripts/extract_css.py` | Nettoyer les doublons CSS inline → styles.css |
| `python3 scripts/add_print_css.py` | Ajouter print.css aux pages qui ne l'ont pas |
| `python3 scripts/link_simulations.py` | Vérifier/ajouter les liens simulations ↔ chapitres |
| `python3 scripts/check_chapters.py` | Vérifier la complétude des chapitres (fichiers manquants) |
| `python3 scripts/check_chapters.py --missing` | Afficher seulement les chapitres incomplets |
| `python3 scripts/check_chapters.py --section maths/bts` | Vérifier une section précise |
| `node scripts/generate-pdf.js` | Générer les PDF des cours |

### Commandes Claude Code personnalisées

Les fichiers dans `.claude/commands/` définissent des skills invocables via `/nom-commande` :

#### Génération de contenu

| Commande | Usage |
|---|---|
| `/new-chapter` | Créer la structure d'un nouveau chapitre |
| `/generate-lecon` | Générer un cours (`lecon.html`) |
| `/generate-exercices` | Générer des exercices (`exercices.html`) |
| `/generate-exercices-capacites` | Générer des exercices par capacités (`exercices-capacites.html`) |
| `/generate-ds` | Générer un devoir surveillé (`ds.html`) |
| `/generate-qcm` | Générer un QCM (`qcm.html`) |
| `/generate-interro` | Générer une interrogation (`interro.html`) |
| `/generate-fiche` | Générer une fiche résumé (`fiche.html`) |
| `/generate-activite` | Générer une activité de découverte (`activite.html`) |
| `/generate-simulation` | Générer une simulation interactive (`simulation.html`) |

#### Audit et qualité

Les skills d'audit s'utilisent en chaîne, du plus large au plus précis :

```
/section-audit <section>          →  tableau de bord macro (tous les chapitres)
      ↓ identifie les chapitres prioritaires
/audit-chapter <chapitre>         →  complétude + sigles (1 chapitre)
      ↓ fichiers OK → on entre dans le détail
/check-quality <chapitre>         →  qualité technique et contenu (1 chapitre)
      ↓ lecon.html signalée
/scientific-audit <lecon.html>    →  rigueur scientifique (1 page)
```

| Commande | Portée | Ce qu'il vérifie | Modèle conseillé |
|---|---|---|---|
| `/section-audit` | Section entière | Complétude, visuels, différenciation, sigles — vue macro | Opus |
| `/audit-chapter` | 1 chapitre | Fichiers manquants, contenu vide, sigles interdits | Sonnet |
| `/check-quality` | 1 chapitre | Technique (nav.js, CSS…), données, refs orphelines, mini-exo, visuels, QCM | Sonnet |
| `/scientific-audit` | 1 page | Valeurs numériques, calculs, formules, modèles, réglementation | Sonnet |
| `/check-sigles` | 1 chapitre | Sigles de filière utilisés comme noms de métiers | Sonnet |

#### Maintenance

| Commande | Usage |
|---|---|
| `/update-audit` | Mettre à jour un fichier d'audit |
| `/css-cleanup` | Nettoyer les styles CSS inline |

---

## Audits du site — Feuille de route du développement

Les audits dans `/audits/` sont le **tableau de bord central du projet**. Ils ne sont pas de simples documents d'analyse : ils constituent la **feuille de route** pour le développement et l'amélioration du site.

### Principe fondamental

**Les audits pilotent le travail.** Avant de générer du nouveau contenu ou de modifier le site :

1. **Consulter les audits** dans `/audits/` pour identifier les priorités
2. **Identifier** dans les audits :
   - les chapitres manquants ou incomplets
   - les pages à compléter (cours, exercices, DS)
   - les exercices à améliorer ou à créer
   - les simulations à créer ou à corriger
   - les incohérences pédagogiques (progression, différenciation, contextes pro)
   - les problèmes techniques (CSS, chemins, accessibilité)
3. **Travailler en priorité** sur les éléments identifiés comme critiques ou hauts dans les audits
4. **Ne pas refaire une analyse déjà présente** dans un audit existant — s'appuyer sur le travail déjà fait

### Fichiers d'audit

| Fichier | Dimension auditée |
|---|---|
| `audits/audit-global.md` | Vue d'ensemble, indicateurs, couverture par section |
| `audits/audit-technique.md` | HTML, CSS, JS, chemins, accessibilité |
| `audits/audit-programmes.md` | Conformité programmes officiels, chapitres, PDF |
| `audits/audit-pedagogique.md` | Différenciation, contextes pro, classes pédagogiques (synthèse) |
| `audits/audit-pedagogique-maths.md` | Détail pédagogique — cours de mathématiques |
| `audits/audit-pedagogique-pc.md` | Détail pédagogique — cours de physique-chimie |
| `audits/audit-exercices.md` | Corrections, DS, complétude, qualité |
| `audits/audit-interros.md` | Interrogations écrites courtes (`interro.html`) |
| `audits/audit-simulations.md` | Simulations interactives, ancrage pédagogique |
| `audits/audit-uniformisation.md` | Uniformisation des formats et conventions |
| `audits/audit-seconde.md` | Audit transverse niveau Seconde Bac Pro |
| `audits/audit-premiere-maths.md` | Audit Première Bac Pro — mathématiques |
| `audits/audit-terminale.md` | Audit transverse niveau Terminale Bac Pro |
| `audits/audit-log.md` | Journal des audits (historique des passes) |
| `audits/plan-amelioration-seconde.md` | Plan d'amélioration spécifique Seconde |

### Règle de mise à jour obligatoire

**Après chaque modification du site liée à un audit :**

1. **Ouvrir l'audit concerné** (ex: `audits/audit-technique.md`)
2. **Déplacer l'élément corrigé** de `## Problemes identifies` vers `## Corrections realisees` avec la date
3. **Cocher la case** correspondante dans `## Ameliorations restantes`
4. **Mettre à jour la date** (`Dernière mise à jour`) en haut du fichier
5. **Mettre à jour les compteurs** si applicable (ex: "61 fichiers" → "0 fichiers")

**Si une amélioration est partiellement réalisée :**

- Laisser l'élément dans `## Ameliorations restantes` avec une note sur ce qui a été fait et ce qui reste
- Ajouter la correction partielle dans `## Corrections realisees`

**Quand un nouveau problème est découvert :**

1. L'ajouter dans `## Problemes identifies` de l'audit approprié
2. Ajouter une tâche dans `## Ameliorations restantes`
3. Mettre à jour la date

### Structure standard d'un audit

Chaque fichier d'audit doit contenir ces sections dans cet ordre :

```markdown
# Titre de l'audit
**Date** : AAAA-MM-JJ
**Dernière mise à jour** : AAAA-MM-JJ

## Problemes identifies
### 1. Titre du problème (gravité : CRITIQUE/HAUTE/MOYENNE/BASSE)
Description, fichiers concernés, nombre d'occurrences.

## Corrections realisees
- **AAAA-MM-JJ** : Description de la correction

## Ameliorations restantes
### Priorité critique
- [ ] Tâche à faire
### Priorité haute
- [ ] Tâche à faire
### Priorité moyenne
- [ ] Tâche à faire
### Priorité basse
- [ ] Tâche à faire
```

### Objectifs

- **Éviter les analyses redondantes** : ne pas refaire ce qui est déjà documenté
- **Suivre l'avancement** : chaque correction est tracée avec sa date
- **Prioriser le travail** : les niveaux critique > haute > moyenne > basse guident l'ordre de traitement
- **Maintenir la cohérence** : les audits reflètent toujours l'état réel du site
