# Audit Technique

**Date** : 2026-03-16
**Derniere mise a jour** : 2026-04-30 (audit complet + 17 fix HTML + 10 sims mobile + relecture prompts)
**Perimetre** : HTML, CSS, JavaScript, chemins, accessibilite, simulations, performances
**Nombre total de fichiers HTML audites** : 477 (191 maths, 180 physique-chimie, 63 simulations, 43 autres)

---

## Resume executif

Le site presente une bonne coherence globale dans sa structure HTML et son usage des classes CSS. Les variables de couleur par matiere/niveau sont correctement appliquees sur l'ensemble du site. Les **trois problemes critiques de chemins absolus** (nav.js, nav.css, diff.js) ont ete **corriges le 2026-03-16** (104 fichiers). Il reste des problemes de **liens casses** (5 sommaires + 1 lien interne), des **simulations non autonomes** (26/63 incluent nav.js) et la **differenciation absente en maths/premiere** (18 fichiers).

**Score de conformite** : 90/100

| Dimension | Etat |
|---|---|
| Structure HTML (meta, template) | Conforme |
| Variables CSS par matiere/niveau | Conforme |
| Redefinitions CSS inline interdites | Conforme |
| Chemins vers styles.css | Conforme (relatifs) |
| Chemins vers nav.js | Conforme (corrige 2026-03-16) |
| Chemins vers nav.css | Conforme (corrige 2026-03-16) |
| Chemins vers diff.js | Conforme (corrige 2026-03-16) |
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
| diff.js | Present dans 178 fichiers (exercices + DS + interros) |

**Note** : `automatismes.html` (racine) a ete supprime le 2026-03-18 (doublon de `automatismes/index.html`). Tous les liens ont ete unifies vers `automatismes/index.html`.

**A faire** : centraliser les 25 classes CSS inline de `physique-chimie/seconde/ch07/qcm.html` (`.qcm-header`, `.q-block`, `.options`, `.q-feedback`, `.score-box`, etc.) dans `styles.css` avant la creation en masse des `qcm.html` (83 chapitres).

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

**Verification detaillee maths/seconde/ch02-ch05 (2026-03-19)** : Les 25 fichiers HTML de ces 4 chapitres ont ete audites en profondeur. **Aucune classe non-standard residuelle** (`def-box`, `exemple`, `methode`, `attention`, `container`) n'a ete trouvee — la correction du 2026-03-16 est confirmee. Tous les `<style>` inline contiennent uniquement des classes specifiques aux pages (interactivite, competences, fiches). **Seule anomalie** : `maths/seconde/ch03/exercices.html` utilise `.niveau-header.niv1/niv2/niv3/niv4` au lieu de `.niveau-header.niveau-1/niveau-2/niveau-3/niveau-4` (forme raccourcie non-standard).

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
| ~~1~~ | ~~Chemins absolus `/nav.js`~~ | ~~CRITIQUE~~ | ~~61~~ | **CORRIGE 2026-03-16** |
| ~~2~~ | ~~Chemins absolus `/nav.css`~~ | ~~CRITIQUE~~ | ~~37~~ | **CORRIGE 2026-03-16** |
| ~~3~~ | ~~Chemins absolus `/diff.js`~~ | ~~HAUTE~~ | ~~6~~ | **CORRIGE 2026-03-16** |
| ~~4~~ | ~~Liens vers `sommaire.html` inexistant~~ | ~~HAUTE~~ | ~~5~~ | **CORRIGE 2026-03-16** |
| ~~5~~ | ~~Lien `ch01_exos.html` inexistant~~ | ~~HAUTE~~ | ~~1~~ | **CORRIGE 2026-03-16** |
| 6 | ~~diff.js en Seconde (hors perimetre)~~ | ~~MOYENNE~~ | ~~56~~ | **RESOLU** — CLAUDE.md mis a jour, Seconde incluse |
| ~~7~~ | ~~diff.js absent en Premiere maths~~ | ~~MOYENNE~~ | ~~18~~ | **CORRIGE 2026-03-16** |
| ~~11~~ | ~~diff.js absent sur 83 interro.html (tous niveaux)~~ | ~~HAUTE~~ | ~~83~~ | **CORRIGE 2026-03-25** |
| 8 | Simulations non autonomes (nav.js) | MOYENNE | 26 | Non-conformite CLAUDE.md |
| 9 | Tableaux sans `scope`/`caption` | BASSE | Generalise | Accessibilite reduite |
| 10 | Boutons interactifs sans ARIA | BASSE | Generalise | Accessibilite reduite |

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
- **2026-03-19** : Bilan technique Seconde — 170 fichiers HTML, 84/84 fichiers exercices/ds/interro avec diff.js, 0 chemin absolu, 0 lien cassé. Conformité technique Seconde : 95/100
- **2026-03-19** : Verification detaillee CSS maths/seconde/ch02-ch05 (25 fichiers) — aucune classe non-standard residuelle. Correction 2026-03-16 confirmee. Anomalie mineure : `niv1` au lieu de `niveau-1` dans ch03/exercices.html
- **2026-03-25** : Corrige diff.js manquant sur 83 interro.html (tous niveaux et matieres : maths/seconde, maths/premiere, maths/terminale, physique-chimie/seconde, physique-chimie/premiere-iccer, physique-chimie/premiere-era, physique-chimie/terminale-iccer, physique-chimie/terminale-era). La differenciation pedagogique etait silencieusement cassee sur toutes les interrogations du site.
- **2026-03-25** : Corrige print.css manquant sur physique-chimie/seconde/ch10/fiche.html
- **2026-03-25** : Corrige lien retour interro.html ch10 (pc-2nde-mama → pc-2nde-pro)
- **2026-04-17** : Audit page d'accueil (`index.html`) — compteur simulations 69 → 72 (hero + carte), ajout du timestamp `.maj` dans le header (regle #10), date « Chapitres en cours » calculee automatiquement (mois/annee courants), desambiguisation des ancres de nav (#card-maths / #card-pc au lieu de deux #disciplines identiques)
- **2026-04-17** : Correction typo CLAUDE.md : `logicie.html` (fichier inexistant) → `logique.html` (fragment réellement présent dans les sommaires maths)

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
- [x] Ajouter diff.js dans les 83 interro.html qui en etaient depourvus sur tout le site (2026-03-25)
- [x] Corriger les liens casses dans maths/seconde/ch05/ (lecon.html, simulation.html, exercices.html) (2026-03-17)
- [x] Ajouter toggle() dans maths/seconde/ch05/lecon.html (2026-03-17)
- [x] Supprimer le bloc HTML hors-conteneur dans maths/seconde/ch05/lecon.html (2026-03-17)
- [ ] Retirer nav.js des 26 simulations pour les rendre autonomes conformement a CLAUDE.md

### Priorite HAUTE (uniformisation 2026-03-18)
- [ ] Centraliser les classes CSS QCM (`.qcm-header`, `.q-block`, `.options`, `.q-feedback`, `.score-box`, etc.) dans `styles.css`
- [ ] Valider le template QCM/interro (chemins, nav.js, diff.js, print.css) avant deploiement en masse
- [ ] Mettre a jour les sommaires pour lister `qcm.html` et `interro.html`

### Priorite BASSE
- [ ] Ajouter `scope="col"` aux `<th>` des tableaux pour l'accessibilite
- [ ] Ajouter `role="button"` et `tabindex="0"` aux elements interactifs non-boutons
- [ ] Creer un script de validation des chemins (lint HTML) pour detecter les chemins absolus
- [ ] Centraliser les classes CSS repetees dans plusieurs simulations si applicable
- [ ] Verifier la coherence des balises `<title>` sur l'ensemble du site

---

## Session du 2026-04-30 — Audit complet & corrections

### Axe 1 : Liens cassés
**0 référence cassée** vers `simulations/X.html` détectée parmi les 1190+ pages (audit automatisé).

### Axe 2 : Structure HTML — 17 pages corrigées

Pattern récurrent : la balise `<div class="c">` (conteneur principal) n'était pas fermée avant `</body>`, causant un déséquilibre `<div>` / `</div>` de 1.

**Fichiers corrigés** :
- 4 fichiers PC (interros et DS Bac Pro 1ère et Terminale ICCER/ERA)
- 13 fichiers Maths (DS, exercices-capacites, interros sur Seconde, Première, Terminale)
- Cas spéciaux : `terminale-era/ch01/ds.html` (extra `</div>` retiré), `terminale/ch04/interro.html` (3 closes ajoutés pour les 3 sections diff-socle/standard/appro mal fermées)

Vérification : 17/17 fichiers maintenant balanced.

### Axe 3 : Animations simulations (déjà documenté ailleurs)
Voir `audit-simulations.md` — bug memory leak corrigé dans `modeles-atome.html` (pattern génération propre).

### Axe 4 : Audit mobile

**Ajouts dans `styles.css`** :
- Nouveau breakpoint @media (max-width: 800px) pour tablette : tables et canvas/SVG responsive
- Améliorations du breakpoint mobile (max-width: 600px) :
  - Titres h1/h2/h3 lisibles
  - Padding des cartes pédagogiques resserré
  - Inputs avec font-size 16 px (anti-zoom auto iOS)
  - Boutons taille tactile minimum (36 px)
  - MathJax : `overflow-x: auto` pour éviter débordement
- Nouveau breakpoint @media (max-width: 380px) pour très petits écrans

**10 simulations corrigées** : ajout de `canvas{max-width:100%;height:auto}` dans le `<style>` inline de :
- moteur, gaz, transmission-info, pile-electrochimique, debit, effet-joule,
  transformateur, pression, chaleur, vitesse-acceleration

Avant le fix, ces simulations avaient des canvas de 820 px qui débordaient sur écrans < 600 px.

### Axe 5 : Relecture des prompts
30 prompts dans `/prompts/` audités. Conclusion : 0 référence cassée vers fichier ou PDF (les classes inline mentionnées sont normales pour les pages spécifiques). Prompts cohérents avec l'état actuel du site.

### Bilan global session
- **17 pages HTML structurellement corrigées**
- **10 simulations PC mobile-responsive**
- **3 nouveaux breakpoints** dans styles.css (tablette, mobile, very small)
- **0 lien cassé** restant
- **30 prompts** validés cohérents
