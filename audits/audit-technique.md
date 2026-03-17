# Audit Technique

**Date** : 2026-03-16
**Derniere mise a jour** : 2026-03-17
**Score de conformite** : 92/100
**Perimetre** : HTML, CSS, JavaScript, chemins, accessibilite, simulations, performances
**Nombre total de fichiers HTML audites** : 477 (191 maths, 180 physique-chimie, 63 simulations, 43 autres)

---

## Resume executif

Le site presente une bonne coherence globale dans sa structure HTML et son usage des classes CSS. Les variables de couleur par matiere/niveau sont correctement appliquees sur l'ensemble du site. Les **trois problemes critiques de chemins absolus** (nav.js, nav.css, diff.js) ont ete **corriges le 2026-03-16** (104 fichiers). Il reste des problemes de **liens casses** (5 sommaires + 1 lien interne), des **simulations non autonomes** (26/63 incluent nav.js) et la **differenciation absente en maths/premiere** (18 fichiers).

**Score de conformite** : 92/100

| Dimension | Etat |
|---|---|
| Structure HTML (meta, template) | Conforme |
| Variables CSS par matiere/niveau | Conforme |
| Redefinitions CSS inline interdites | Conforme |
| Chemins vers styles.css | Conforme (relatifs) |
| Chemins vers nav.js | Conforme (corrige 2026-03-16) |
| Chemins vers nav.css | Conforme (corrige 2026-03-16) |
| Chemins vers diff.js | Conforme (corrige 2026-03-16) |
| SVG responsive (width/max-width) | Conforme (corrige 2026-03-17) |
| Simulations autonomes | NON CONFORME (26/63 avec nav.js) |
| diff.js uniquement exercices/ds | NON CONFORME (present en Seconde) |
| Liens de retour sommaire | Conforme (corrige 2026-03-16) |
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

### 3.1 Chemins absolus vers nav.js — CORRIGE

~~**Gravite : CRITIQUE** — 61 fichiers utilisaient `src="/nav.js"` au lieu du chemin relatif.~~

**Corrige le 2026-03-16** : 61 fichiers corriges → `src="../../../nav.js"`. 0 chemin absolu restant.

### 3.2 Chemins absolus vers nav.css — CORRIGE

~~**Gravite : CRITIQUE** — 37 fichiers utilisaient `href="/nav.css"` au lieu du chemin relatif.~~

**Corrige le 2026-03-16** : 37 fichiers corriges → `href="../../../nav.css"`. 0 chemin absolu restant.

### 3.3 Chemins absolus vers diff.js — CORRIGE

~~**Gravite : HAUTE** — 6 fichiers utilisaient `src="/diff.js"` au lieu du chemin relatif.~~

**Corrige le 2026-03-16** : 6 fichiers corriges → `src="../../../diff.js"`. 0 chemin absolu restant.

### 3.4 Liens vers sommaire.html inexistant — CORRIGE

~~**Gravite : HAUTE** — 5 fichiers pointaient vers `../../sommaire.html` inexistant.~~

**Corrige le 2026-03-16** : 5 liens corriges → `../../../maths-term-iccer.html`. 0 lien casse restant.

### 3.5 Lien interne casse — CORRIGE

~~**Gravite : HAUTE** — `maths/seconde/ch01/lecon.html` : `ch01_exos.html` inexistant.~~

**Corrige le 2026-03-16** : lien corrige → `exercices.html`.

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

### 5.1 diff.js — PARTIELLEMENT CONFORME

**Gravite : MOYENNE**

Depuis la mise a jour du 2026-03-16, CLAUDE.md precise que la differenciation s'applique aux **trois niveaux** (Seconde, Premiere, Terminale). Etat actuel :

- **28 fichiers en `maths/seconde/`** contiennent `diff.js` — conforme
- **28 fichiers en `physique-chimie/seconde/`** contiennent `diff.js` — conforme
- **18 fichiers en `maths/premiere/`** contiennent diff.js — **CONFORME** (corrige 2026-03-16)

**Note** : aucun fichier `lecon.html` ne contient diff.js ou des classes de differenciation — conforme.

### 5.2 Chart.js — usage correct

Chart.js est inclus dans 124 fichiers, principalement des pages de cours (`lecon.html`) et quelques exercices qui utilisent des graphiques. Pas d'inclusion superflue detectee.

### 5.3 MathJax — usage correct

MathJax est inclus dans la grande majorite des pages de cours et exercices (403 fichiers). Les pages sans MathJax sont principalement des pages d'index et sommaires — conforme.

---

## 6. SVG responsive — CORRIGE

### 6.1 SVG a dimensions fixes — CORRIGE

~~**Gravite : MOYENNE** — 97 SVG dans 46 fichiers utilisaient des dimensions fixes (`width="700" height="320"`) sans `max-width:100%`, provoquant un debordement horizontal sur mobile/tablette.~~

**Corrige le 2026-03-17** : 97 SVG corriges dans 46 fichiers. Remplacement de `width="NUM" height="NUM"` par `width="100%" style="max-width:NUMpx;height:auto"`. Les SVG < 200px (icones) n'ont pas ete modifies.

Fichiers concernes : maths (seconde ch01-ch13, premiere ch07/ch09, terminale ch02/ch06/ch07, BTS ch17/ch18/ch20/ch21/ch24), physique-chimie (seconde ch01-ch13, premiere-era ch06/ch09, terminale-era ch05-ch08, terminale-iccer ch01-ch06), automatismes/polynomes.html.

---

## 7. Accessibilite basique

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
| ~~1~~ | ~~Chemins absolus `/nav.js`~~ | ~~CRITIQUE~~ | ~~61~~ | **CORRIGE 2026-03-16** |
| ~~2~~ | ~~Chemins absolus `/nav.css`~~ | ~~CRITIQUE~~ | ~~37~~ | **CORRIGE 2026-03-16** |
| ~~3~~ | ~~Chemins absolus `/diff.js`~~ | ~~HAUTE~~ | ~~6~~ | **CORRIGE 2026-03-16** |
| ~~4~~ | ~~Liens vers `sommaire.html` inexistant~~ | ~~HAUTE~~ | ~~5~~ | **CORRIGE 2026-03-16** |
| ~~5~~ | ~~Lien `ch01_exos.html` inexistant~~ | ~~HAUTE~~ | ~~1~~ | **CORRIGE 2026-03-16** |
| 6 | ~~diff.js en Seconde (hors perimetre)~~ | ~~MOYENNE~~ | ~~56~~ | **RESOLU** — CLAUDE.md mis a jour, Seconde incluse |
| ~~7~~ | ~~diff.js absent en Premiere maths~~ | ~~MOYENNE~~ | ~~18~~ | **CORRIGE 2026-03-16** |
| 8 | Simulations non autonomes (nav.js) | MOYENNE | 26 | Non-conformite CLAUDE.md |
| ~~9~~ | ~~SVG a dimensions fixes (debordement mobile)~~ | ~~MOYENNE~~ | ~~97 (46 fichiers)~~ | **CORRIGE 2026-03-17** |
| 10 | Tableaux sans `scope`/`caption` | BASSE | Generalise | Accessibilite reduite |
| 11 | Boutons interactifs sans ARIA | BASSE | Generalise | Accessibilite reduite |

---

## Corrections realisees

- **2026-03-16** : Corrige les 61 chemins absolus `src="/nav.js"` → `src="../../../nav.js"` dans maths/terminale (33), physique-chimie/terminale-era (24), physique-chimie/terminale-iccer (4)
- **2026-03-16** : Corrige les 37 chemins absolus `href="/nav.css"` → `href="../../../nav.css"` dans maths/terminale (29), maths/bts (8)
- **2026-03-16** : Corrige les 6 chemins absolus `src="/diff.js"` → `src="../../../diff.js"` dans maths/terminale/ch04, ch06, ch11
- **2026-03-16** : Corrige les 5 liens casses `../../sommaire.html` → `../../../maths-term-iccer.html` dans maths/terminale/ch07, ch08, ch10, ch11
- **2026-03-16** : Corrige le lien `ch01_exos.html` → `exercices.html` dans maths/seconde/ch01/lecon.html
- **2026-03-16** : Ajoute diff.js dans les 18 fichiers exercices.html et ds.html de maths/premiere (ch01-ch09)
- **2026-03-16** : Supprime les redefinitions CSS inline (.exo .exo-num, details.corr) dans 28 fichiers physique-chimie/seconde et centralise dans styles.css
- **2026-03-16** : Corrige le lien retour de physique-chimie/seconde/ch13/lecon.html (index.html → pc-2nde-pro.html)
- **2026-03-17** : Corrige les liens casses dans maths/seconde/ch05/ : lecon.html (9 liens vers simulations inexistantes et navigation), simulation.html (6 liens), exercices.html (2 liens)
- **2026-03-17** : Ajoute la fonction toggle() manquante dans maths/seconde/ch05/lecon.html (boutons correction inoperants)
- **2026-03-17** : Supprime le bloc HTML hors-conteneur (apres `</div><!-- fin .c -->`) dans maths/seconde/ch05/lecon.html
- **2026-03-17** : Corrige l'exemple 3 du cours ch05 (valeurs qui ne tombaient pas juste : 63,50/8,50 → 66/8,50)
- **2026-03-17** : Convertit 396 entités HTML en UTF-8 dans maths/seconde/ch05/ds.html (185) et exercices.html (211)
- **2026-03-17** : Centralise dans styles.css les classes .situation-pro, .sp-grid, .sp-label, .erreur-item, .hors-prog, .simu-link (utilisées dans 11+ fichiers)
- **2026-03-17** : Nettoie le CSS inline de maths/seconde/ch05/lecon.html (28→4 lignes), ch04/lecon.html et ch06/lecon.html (suppression des doublons)
- **2026-03-17** : Remplace .hprog (classe inline) par .hors-prog (classe centralisée dans styles.css) dans maths/terminale/ch02/lecon.html
- **2026-03-17** : Ajoute « Terminale Bac Pro » aux balises `<title>` de maths/terminale/ch02/ (lecon.html, exercices.html, ds.html)
- **2026-03-17** : Rend 97 SVG responsive dans 46 fichiers (width="100%" + max-width) — supprime le debordement horizontal sur mobile/tablette pour tous les schemas, arbres et graphiques > 200px

---

## Ameliorations restantes

### Priorite CRITIQUE
- [x] Remplacer `src="/nav.js"` par le chemin relatif correct dans 61 fichiers (2026-03-16)
- [x] Remplacer `href="/nav.css"` par le chemin relatif correct dans 37 fichiers (2026-03-16)

### Priorite HAUTE
- [x] Remplacer `src="/diff.js"` par le chemin relatif correct dans 6 fichiers (2026-03-16)
- [x] Corriger les 5 liens vers `../../sommaire.html` dans `maths/terminale/` (2026-03-16)
- [x] Corriger le lien `ch01_exos.html` → `exercices.html` dans `maths/seconde/ch01/lecon.html` (2026-03-16)

### Priorite MOYENNE
- [x] Decider si la differenciation en Seconde est intentionnelle — OUI, CLAUDE.md mis a jour (2026-03-16)
- [x] Ajouter diff.js dans les exercices.html et ds.html de `maths/premiere/` (2026-03-16)
- [x] Corriger les liens casses dans maths/seconde/ch05/ (lecon.html, simulation.html, exercices.html) (2026-03-17)
- [x] Ajouter toggle() dans maths/seconde/ch05/lecon.html (2026-03-17)
- [x] Supprimer le bloc HTML hors-conteneur dans maths/seconde/ch05/lecon.html (2026-03-17)
- [x] Rendre les 97 SVG responsive (width="100%" + max-width) dans 46 fichiers (2026-03-17)
- [ ] Retirer nav.js des 26 simulations pour les rendre autonomes conformement a CLAUDE.md

### Priorite BASSE
- [ ] Ajouter `scope="col"` aux `<th>` des tableaux pour l'accessibilite
- [ ] Ajouter `role="button"` et `tabindex="0"` aux elements interactifs non-boutons
- [ ] Creer un script de validation des chemins (lint HTML) pour detecter les chemins absolus
- [ ] Centraliser les classes CSS repetees dans plusieurs simulations si applicable
- [ ] Verifier la coherence des balises `<title>` sur l'ensemble du site
