# Audit Technique

**Date** : 2026-03-16
**Derniere mise a jour** : 2026-03-16
**Perimetre** : HTML, CSS, JavaScript, chemins, accessibilite, simulations, performances
**Nombre total de fichiers HTML audites** : 477 (191 maths, 180 physique-chimie, 63 simulations, 43 autres)

---

## Resume executif

Le site presente une bonne coherence globale dans sa structure HTML et son usage des classes CSS. Les variables de couleur par matiere/niveau sont correctement appliquees sur l'ensemble du site. Cependant, **trois problemes critiques** ont ete identifies, principalement lies aux **chemins absolus** qui empechent le bon fonctionnement sur GitHub Pages. On note aussi des **incoherences dans la differenciation pedagogique** (diff.js present en Seconde alors que CLAUDE.md le reserve a Premiere/Terminale) et des **simulations non autonomes** (26 sur 63 incluent nav.js contrairement a la convention).

**Score de conformite** : 78/100

| Dimension | Etat |
|---|---|
| Structure HTML (meta, template) | Conforme |
| Variables CSS par matiere/niveau | Conforme |
| Redefinitions CSS inline interdites | Conforme |
| Chemins vers styles.css | Conforme (relatifs) |
| Chemins vers nav.js | NON CONFORME (61 absolus) |
| Chemins vers nav.css | NON CONFORME (37 absolus) |
| Chemins vers diff.js | NON CONFORME (6 absolus) |
| Simulations autonomes | NON CONFORME (26/63 avec nav.js) |
| diff.js uniquement exercices/ds | NON CONFORME (present en Seconde) |
| Liens de retour sommaire | PARTIELLEMENT CONFORME |
| Accessibilite images | Non applicable (aucune balise img detectee) |

---

## 1. Structure des pages HTML

### 1.1 Balises meta — CONFORME

- `<meta charset="UTF-8">` : present dans **475/477 fichiers** (2 fichiers speciaux sans)
- `<meta name="viewport">` : present dans **475/477 fichiers**
- `lang="fr"` sur `<html>` : present partout
- `<!DOCTYPE html>` : present partout

### 1.2 Template HTML — CONFORME

Les pages de cours suivent le template defini dans CLAUDE.md :
- Structure `<div class="c">` respectee
- `<header>` avec `<h1>` et `<p class="sous-titre">` presents
- Lien de retour avec `class="nb"` present

### 1.3 Scripts inclus

| Script | Inclusion |
|---|---|
| MathJax v3 | Present dans 403 fichiers (cours + exercices + DS + simulations). Quelques simulations sans MathJax n'utilisent pas de formules — correct. |
| Chart.js | Present dans 124 fichiers (lecons avec graphiques principalement) |
| nav.js | Present dans toutes les pages de cours (mais 61 en chemin absolu) |
| diff.js | Present dans 150 fichiers (exercices + DS) |

**Probleme** : MathJax est inclus dans `automatismes/index.html` qui sert de page d'index — a verifier si necessaire.

---

## 2. Coherence CSS

### 2.1 Variables CSS par matiere/niveau — CONFORME

Toutes les pages utilisent les bonnes valeurs de variables CSS conformement au tableau de CLAUDE.md :

| Section | Valeurs trouvees | Attendu | Statut |
|---|---|---|---|
| `maths/seconde` | `--p:#0056b3;--p-bg:#ebf5ff;--p-border:#bee3f8` | idem | OK |
| `maths/premiere` | `--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd` | idem | OK |
| `maths/terminale` | `--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd` | idem | OK |
| `physique-chimie/seconde` | `--p:#6f42c1;--p-bg:#f5f0ff;--p-border:#c4b5fd` | idem | OK |
| `physique-chimie/premiere-iccer` | `--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd` | idem | OK |
| `physique-chimie/premiere-era` | `--p:#2da44e;--p-bg:#f0fff4;--p-border:#86efac;--s:#0ea5e9` | idem | OK |
| `physique-chimie/terminale-iccer` | `--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd` | idem | OK |
| `physique-chimie/terminale-era` | `--p:#2da44e;--p-bg:#f0fff4;--p-border:#86efac;--s:#0ea5e9` | idem | OK |

### 2.2 Redefinitions inline de classes styles.css — CONFORME

Aucune redefinition inline des classes `.def`, `.prop`, `.att`, `.meth`, `.retenir`, `.exo`, `.corr` detectee dans les pages de cours. Les `<style>` inline contiennent uniquement des classes specifiques a la page (pictogrammes, grilles thematiques, etc.) — conforme a la regle CLAUDE.md.

### 2.3 CSS inline specifique aux pages

20+ fichiers en `physique-chimie/seconde/` et quelques fichiers en `physique-chimie/terminale-iccer/` contiennent du CSS inline specifique (grilles de pictogrammes, styles de cartes EPI, etc.). Ces classes sont uniques a ces pages et ne sont pas des doublons de `styles.css` — **acceptable**.

**Recommandation basse priorite** : si certaines classes comme `.picto-grid`, `.epi-grid` sont reutilisees dans plusieurs pages, envisager de les centraliser dans `styles.css`.

---

## 3. Liens et chemins

### 3.1 Chemins absolus vers nav.js — CRITIQUE (61 fichiers)

**Gravite : CRITIQUE**

61 fichiers utilisent `<script src="/nav.js"></script>` au lieu du chemin relatif. Sur GitHub Pages, ces chemins ne resolvent pas correctement si le site est heberge dans un sous-repertoire.

**Sections touchees** :
- `maths/terminale/ch01-ch11/` : lecon.html, exercices.html, ds.html (33 fichiers)
- `physique-chimie/terminale-era/ch01-ch08/` : lecon.html, exercices.html, ds.html (24 fichiers)
- `physique-chimie/terminale-iccer/ch01-ch08/` : lecon.html (4 fichiers)

### 3.2 Chemins absolus vers nav.css — CRITIQUE (37 fichiers)

**Gravite : CRITIQUE**

37 fichiers utilisent `<link rel="stylesheet" href="/nav.css">` au lieu de `href="../../../nav.css"`.

**Sections touchees** :
- `maths/terminale/` : 29 fichiers
- `maths/bts/` : 8 fichiers

### 3.3 Chemins absolus vers diff.js — HAUTE (6 fichiers)

**Gravite : HAUTE**

6 fichiers utilisent `<script src="/diff.js"></script>` au lieu du chemin relatif :
- `maths/terminale/ch04/ds.html`
- `maths/terminale/ch04/exercices.html`
- `maths/terminale/ch06/ds.html`
- `maths/terminale/ch06/exercices.html`
- `maths/terminale/ch11/ds.html`
- `maths/terminale/ch11/exercices.html`

### 3.4 Liens vers sommaire.html inexistant — HAUTE (5 fichiers)

**Gravite : HAUTE**

5 fichiers en `maths/terminale/` pointent vers `../../sommaire.html` qui n'existe pas :
- `maths/terminale/ch07/ds.html`
- `maths/terminale/ch08/ds.html`
- `maths/terminale/ch10/ds.html`
- `maths/terminale/ch11/ds.html`
- `maths/terminale/ch11/exercices.html`

Le lien correct devrait etre `../../../maths-term-iccer.html` ou `../../../maths-term-erama.html` selon le groupement.

### 3.5 Lien interne casse — HAUTE (1 fichier)

**Gravite : HAUTE**

`maths/seconde/ch01/lecon.html` ligne 859 : `<a href="ch01_exos.html">` pointe vers un fichier inexistant. Le fichier correct est `exercices.html`.

### 3.6 Chemins vers styles.css — CONFORME

Aucun chemin absolu vers `styles.css` detecte. Tous les fichiers utilisent le chemin relatif correct (`../../../styles.css` pour les pages de cours, `../styles.css` pour les automatismes, etc.).

---

## 4. Simulations

### 4.1 Autonomie des simulations — NON CONFORME (26/63)

**Gravite : MOYENNE**

Selon CLAUDE.md, les simulations doivent etre **autonomes** (styles inline, pas de styles.css ni nav.js). Or :

- **26 simulations sur 63 incluent `nav.js`** (soit 41%)
- **Aucune simulation n'inclut `styles.css`** — conforme sur ce point
- **37 simulations sont pleinement autonomes** — conforme

**Simulations avec nav.js** (non autonomes) :
atome-couches.html, atome.html, balance.html, chaleur.html, changement-etat.html, debit.html, dephasage.html, effet-joule.html, entrainement-ineq.html, entrainement.html, equations.html, gaz.html, graphe-equation.html, inegalite.html, melangeur.html, modeles-atome.html, moteur.html, ohm.html, oxydoreduction.html, pression.html, puissance.html, rayonnement.html, redressement.html, serre.html, son.html, traceur.html

**Simulations autonomes** (37 fichiers) :
archimede.html, circuit-electrique.html, combustion.html, complexes.html, concentration.html, conductance-thermique.html, derivee.html, droite-affine.html, exp-log.html, figures-planes.html, fonction-machine.html, forces.html, integrale.html, moments.html, mouvement.html, ondes-em.html, pile-electrochimique.html, polynome3.html, probabilites.html, proportionnalite.html, pythagore.html, refraction.html, scalaire.html, signal-alternatif.html, solides.html, son-2nde.html, sources-lumineuses.html, statistiques.html, stats-2var.html, suites.html, thales.html, transferts-thermiques.html, transformateur.html, transmission-info.html, trigonometrie.html, vecteurs.html, vitesse-acceleration.html

### 4.2 MathJax dans les simulations

32 simulations sur 63 incluent MathJax, les 31 restantes ne l'incluent pas. Cela semble coherent avec le contenu (simulations mathematiques vs simulations purement interactives).

---

## 5. Scripts et performances

### 5.1 diff.js — NON CONFORME (present en Seconde)

**Gravite : MOYENNE**

Selon CLAUDE.md, la differenciation pedagogique s'applique **uniquement en Premiere et Terminale**. Or :

- **28 fichiers en `maths/seconde/`** contiennent `diff.js` et des classes `diff-socle/standard/appro` (tous les exercices.html et ds.html)
- **28 fichiers en `physique-chimie/seconde/`** contiennent `diff.js` et des classes `diff-socle/standard/appro`
- **0 fichier en `maths/premiere/`** contient diff.js (alors qu'il devrait en avoir)

Cela represente une incoherence par rapport a la philosophie de differenciation decrite dans CLAUDE.md.

**Note** : aucun fichier `lecon.html` ne contient diff.js ou des classes de differenciation — conforme.

### 5.2 Chart.js — usage correct

Chart.js est inclus dans 124 fichiers, principalement des pages de cours (`lecon.html`) et quelques exercices qui utilisent des graphiques. Pas d'inclusion superflue detectee.

### 5.3 MathJax — usage correct

MathJax est inclus dans la grande majorite des pages de cours et exercices (403 fichiers). Les pages sans MathJax sont principalement des pages d'index et sommaires — conforme.

---

## 6. Accessibilite basique

### 6.1 Images — Non applicable

Aucune balise `<img>` detectee dans les pages de cours. Le site utilise principalement des emojis Unicode, des canvas, et des SVG inline pour les illustrations. Pas de probleme d'attribut `alt` manquant.

### 6.2 Tableaux

Les tableaux de donnees dans les pages de cours utilisent les balises `<table>`, `<thead>`, `<th>`, `<tbody>` standard. Pas de `<caption>` ni d'attributs `scope` detectes — amelioration possible pour l'accessibilite.

### 6.3 Contraste des couleurs

Les variables CSS definies offrent un bon contraste :
- Texte principal : `#2d3748` sur fond blanc — ratio > 10:1
- Titres en couleur primaire (`#0056b3`, `#0969da`, `#6f42c1`, `#2da44e`) sur fond blanc — tous > 4.5:1
- Badges et tags : texte blanc sur fond colore — a verifier au cas par cas

### 6.4 Navigation au clavier

Le site repose sur des liens `<a>` et boutons `<button>` standards, naturellement accessibles au clavier. Les scripts `diff.js` et correction toggle (`bc`) utilisent des gestionnaires `onclick` — recommandation d'ajouter `role="button"` et `tabindex="0"` si ce n'est pas deja fait.

---

## Tableau synthetique des problemes

| # | Probleme | Gravite | Fichiers | Impact |
|---|---|---|---|---|
| 1 | Chemins absolus `/nav.js` | CRITIQUE | 61 | Navigation cassee sur GitHub Pages |
| 2 | Chemins absolus `/nav.css` | CRITIQUE | 37 | Styles de navigation absents |
| 3 | Chemins absolus `/diff.js` | HAUTE | 6 | Differenciation cassee |
| 4 | Liens vers `sommaire.html` inexistant | HAUTE | 5 | Lien de retour casse |
| 5 | Lien `ch01_exos.html` inexistant | HAUTE | 1 | Lien interne casse |
| 6 | diff.js en Seconde (hors perimetre) | MOYENNE | 56 | Incoherence pedagogique |
| 7 | diff.js absent en Premiere maths | MOYENNE | ~18 | Differenciation manquante |
| 8 | Simulations non autonomes (nav.js) | MOYENNE | 26 | Non-conformite CLAUDE.md |
| 9 | Tableaux sans `scope`/`caption` | BASSE | Generalise | Accessibilite reduite |
| 10 | Boutons interactifs sans ARIA | BASSE | Generalise | Accessibilite reduite |

---

## Corrections realisees

- Aucune a ce stade.

---

## Ameliorations restantes

### Priorite CRITIQUE
- [ ] Remplacer `src="/nav.js"` par le chemin relatif correct dans 61 fichiers
- [ ] Remplacer `href="/nav.css"` par le chemin relatif correct dans 37 fichiers

### Priorite HAUTE
- [ ] Remplacer `src="/diff.js"` par le chemin relatif correct dans 6 fichiers
- [ ] Corriger les 5 liens vers `../../sommaire.html` dans `maths/terminale/` (pointer vers le bon sommaire)
- [ ] Corriger le lien `ch01_exos.html` → `exercices.html` dans `maths/seconde/ch01/lecon.html` (ligne 859)

### Priorite MOYENNE
- [ ] Decider si la differenciation en Seconde est intentionnelle ou doit etre retiree (56 fichiers)
- [ ] Ajouter diff.js dans les exercices.html et ds.html de `maths/premiere/` si la differenciation est souhaitee
- [ ] Retirer nav.js des 26 simulations pour les rendre autonomes conformement a CLAUDE.md

### Priorite BASSE
- [ ] Ajouter `scope="col"` aux `<th>` des tableaux pour l'accessibilite
- [ ] Ajouter `role="button"` et `tabindex="0"` aux elements interactifs non-boutons
- [ ] Creer un script de validation des chemins (lint HTML) pour detecter les chemins absolus
- [ ] Centraliser les classes CSS repetees dans plusieurs simulations si applicable
- [ ] Verifier la coherence des balises `<title>` sur l'ensemble du site
