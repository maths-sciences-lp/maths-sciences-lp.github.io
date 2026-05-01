# Audit Simulations Interactives

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-05-01 (recensement total + référencement 8 simulations bois/agencement ; 2026-04-29 audit qualité approfondi Opus)
**Périmètre** : dossier `simulations/` — **78 fichiers HTML** (vs 70 documenté précédemment)
**Méthode** : Lecture et analyse de l'ensemble des simulations, vérification du référencement depuis les pages de cours, analyse de la couverture par chapitre, audit technique approfondi (autonomie, responsive, accessibilité, qualité JS).

**Note 2026-04-30** : 8 nouvelles simulations ajoutées depuis le précédent comptage, dont 8 simulations bois/agencement créées les 24 avril : `presse-hydraulique.html`, `paroi-multicouche.html`, `escalier-blondel.html`, `eclairage-atelier.html`, `dilatation-parquet.html`, `comparateur-vitrages.html`, `calepinage.html`, `anisotropie-bois.html`, plus `ctn-pt100-comparaison.html` et `ctn-etuve-regulation.html` (7 avril).

**Référencement (Phase 1, 2026-04-30)** : les 8 simulations bois/agencement ont été ajoutées dans `simulations.html` (sections Thermique, Mécanique, Signaux & Optique, Mathématiques) avec badges niveau et chapitre. Les 2 simulations CTN/PT100 étaient déjà référencées. Liens depuis les leçons posés pour 3 sims clés des classes en cours : `paroi-multicouche` et `comparateur-vitrages` → 1ère ERA ch05 ; `presse-hydraulique` → 1ère ERA ch07. **À finaliser** : liaison de `escalier-blondel`, `calepinage`, `dilatation-parquet`, `anisotropie-bois`, `eclairage-atelier` depuis les leçons / activités correspondantes (2nde MAMA principalement).

---

## Inventaire des simulations

### Mathématiques — Seconde (15 simulations)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 1 | `proportionnalite.html` | Proportionnalité, pourcentages, y = kx | Ch01 | Non | Bonne |
| 2 | `statistiques.html` | Diagrammes et indicateurs statistiques | Ch02-03 | Non | Bonne |
| 3 | `probabilites.html` | Probabilités, fluctuation des fréquences | Ch04 | Non | Bonne |
| 4 | `balance.html` | Résolution d'équations du 1er degré (balance) | Ch05 | **Oui** | Très bonne |
| 5 | `entrainement.html` | Quiz équations 1er degré (10 questions) | Ch05 | **Oui** | Très bonne |
| 6 | `equations.html` | Résolveur d'équations (labo virtuel) | Ch05 (implicite) | **Oui** | Moyenne |
| 7 | `graphe-equation.html` | Résolution graphique (intersection droites) | Ch05-06 | **Oui** | Très bonne |
| 8 | `entrainement-ineq.html` | Quiz inéquations (10 questions) | Ch06 | **Oui** | Très bonne |
| 9 | `inegalite.html` | Inéquations sur la droite graduée | Ch06 | **Oui** | Très bonne |
| 10 | `fonction-machine.html` | Machine à fonctions (notion de fonction) | Ch07 | Non | Bonne |
| 11 | `droite-affine.html` | Fonctions linéaire et affine, f(x) = ax + b | Ch08-09 | Non | Bonne |
| 12 | `figures-planes.html` | Périmètres et aires de figures planes | Ch11 | Non | Bonne |
| 13 | `pythagore.html` | Théorème de Pythagore | Ch12 | Non | Bonne |
| 14 | `thales.html` | Théorème de Thalès | Ch13 | Non | Bonne |
| 15 | `solides.html` | Volumes et agrandissement de solides | Ch14 | Non | Bonne |

### Mathématiques — Première (1 simulation)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 16 | `derivee.html` | Fonction dérivée et tangente | Ch06 | Non | Bonne |

### Mathématiques — Terminale (9 simulations)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 17 | `stats-2var.html` | Statistiques à deux variables | Ch01 | Non | Bonne |
| 18 | `suites.html` | Suites arithmétiques et géométriques | Ch03 | Non | Bonne |
| 19 | `polynome3.html` | Fonctions polynômes degré 3 | Ch04 | Non | Bonne |
| 20 | `exp-log.html` | Fonctions exponentielles et logarithme | Ch05 | Non | Bonne |
| 21 | `vecteurs.html` | Vecteurs du plan | Ch06 | Non | Bonne |
| 22 | `trigonometrie.html` | Trigonométrie | Ch07 | Non | Bonne |
| 23 | `integrale.html` | Calcul intégral | Ch08 | Non | Bonne |
| 24 | `complexes.html` | Nombres complexes (plan complexe) | Ch10 | Non | Bonne |
| 25 | `scalaire.html` | Produit scalaire | Ch11 | Non | Bonne |

### Physique-Chimie — Seconde (17 simulations liées à 13 chapitres)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 26 | `circuit-electrique.html` | Grandeurs électriques, P = U × I | Ch02 | **Oui** | Bonne |
| 27 | `ohm.html` | Loi d'Ohm, labo multi-séries, U = f(I) | Ch03 | **Oui** | Très bonne |
| 28 | `signal-alternatif.html` | Oscilloscope virtuel, u(t) = Umax sin(2πft) | Ch04 | **Oui** | Très bonne |
| 29 | `mouvement.html` | Mouvement et trajectoire, v = d/t | Ch05 | **Oui** | Bonne |
| 30 | `forces.html` | Forces et équilibre, P = mg | Ch06 | **Oui** | Bonne |
| 31 | `atome.html` | Constructeur d'atomes et ions | Ch07 | **Oui** | Très bonne |
| 32 | `atome-couches.html` | Configuration électronique (Bohr) | Ch07 | **Oui** | Bonne |
| 33 | `modeles-atome.html` | Histoire du modèle de l'atome | Ch07 | **Oui** | Bonne |
| 34 | `liaisons-chimiques.html` | Liaisons covalente vs ionique, molécules | Ch07 | **Oui** | Très bonne |
| 35 | `concentration.html` | Solutions chimiques, Cm = m/V | Ch08 | **Oui** | Bonne |
| 36 | `son-2nde.html` | Caractéristiques d'un son, v = d/t | Ch09 | **Oui** | Bonne |
| 37 | `chaleur.html` | Chaleur massique, Q = mcΔT | Ch10 | **Oui** | Bonne |
| 38 | `transferts-thermiques.html` | 3 modes de transfert thermique | Ch11 | **Oui** | Bonne |
| 39 | `changement-etat.html` | Courbe de chauffage, changements d'état | Ch12 | **Oui** | Bonne |
| 40 | `refraction.html` | Réflexion et réfraction, loi de Snell-Descartes | Ch13 | **Oui** | Très bonne |
| 41 | `sources-lumineuses.html` | Choisir une source lumineuse | Ch14 | **Oui** | Bonne |
| 42 | `melangeur.html` | Mélangeur RVB (synthèse additive) | Ch14 | **Oui** | Bonne |

**Note** : Ch01 (Sécurité au laboratoire) est le seul chapitre sans simulation — un chapitre essentiellement réglementaire pour lequel une simulation interactive n'est pas prioritaire.

**Couverture détaillée par chapitre PC Seconde :**

| Chapitre | Titre | Simulations liées | Nb |
|---|---|---|---|
| Ch01 | Sécurité en laboratoire et en atelier | aucune | 0 |
| Ch02 | Grandeurs électriques et circuits | `circuit-electrique.html` | 1 |
| Ch03 | Loi d'Ohm et caractéristiques d'un dipôle | `ohm.html` | 1 |
| Ch04 | Signaux électriques alternatifs | `signal-alternatif.html` | 1 |
| Ch05 | Mouvement et trajectoire | `mouvement.html` | 1 |
| Ch06 | Forces et équilibre | `forces.html` | 1 |
| Ch07 | Structure de la matière | `atome.html`, `atome-couches.html`, `modeles-atome.html`, `liaisons-chimiques.html` | 4 |
| Ch08 | Solutions chimiques et concentration | `concentration.html` | 1 |
| Ch09 | Caractéristiques d'un son | `son-2nde.html` | 1 |
| Ch10 | Température et capteurs thermiques | `chaleur.html` | 1 |
| Ch11 | Transferts thermiques et équilibre thermique | `transferts-thermiques.html` | 1 |
| Ch12 | Changements d'état et énergie thermique | `changement-etat.html` | 1 |
| Ch13 | Réflexion, réfraction et signaux lumineux | `refraction.html` | 1 |
| Ch14 | Lumière, couleurs et photodétecteurs | `sources-lumineuses.html`, `melangeur.html` | 2 |

### Physique-Chimie — Première ICCER (5 simulations)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 35 | `combustion.html` | Combustion du carbone et hydrocarbures | Ch03 | Non | Bonne |
| 36 | `moments.html` | Moments et équilibre en rotation | Ch06 | Non | Bonne |
| 37 | `archimede.html` | Force d'Archimède | Ch08 | Non | Bonne |
| 38 | `ondes-em.html` | Spectre électromagnétique | Ch09-10 | Non | Bonne |

### Physique-Chimie — Première ERA (1 simulation)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 39 | `conductance-thermique.html` | Conductance thermique et isolation | Ch05 ERA | Non | Bonne |

### Physique-Chimie — Terminale ICCER (8 simulations)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 40 | `puissance.html` | Puissance active, réactive, apparente | Ch01 | Non | Bonne |
| 41 | `redressement.html` | Redressement du courant AC/DC | Ch02 | Non | Bonne |
| 42 | `moteur.html` | Moteur électrique, champ tournant | Ch03 | Non | Bonne |
| 43 | `rayonnement.html` | Loi de Wien, corps noir | Ch04 | Non | Bonne |
| 44 | `pression.html` | Pression dans un fluide, P = P0 + ρgh | Ch05 | Non | Bonne |
| 45 | `debit.html` | Débit d'un fluide, Qv = Sv | Ch06 | Non | Bonne |
| 46 | `oxydoreduction.html` | Réactions redox, corrosion | Ch07 | Non | Bonne |
| 47 | `son.html` | Signal sonore, fréquence, amplitude | Ch08 | Non | Bonne |

### Physique-Chimie — Terminale ERA (5 simulations)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 48 | `transformateur.html` | Transformateur et transport d'énergie | Ch01 ERA | Non | Bonne |
| 49 | `pile-electrochimique.html` | Pile électrochimique | Ch02 ERA | Non | Bonne |
| 50 | `vitesse-acceleration.html` | Vitesse et accélération | Ch04 ERA | Non | Bonne |
| 51 | `sources-lumineuses.html` | Choisir une source lumineuse | Ch06 ERA + **PC 2nde Ch14** | **Oui** | Bonne |
| 52 | `transmission-info.html` | Transmettre l'information (Shannon) | Ch07 ERA | Non | Bonne |

**Note** : `sources-lumineuses.html` et `melangeur.html` sont partagées entre Terminale ERA et PC Seconde Ch14.

### Physique-Chimie — Première ICCER/ERA supplémentaires (3 simulations — 2026-04-05)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 53 | `chaleur.html` | Chaleur massique, Q = mcΔT | 1ère Ch04 (transferts thermiques) | **Oui** | Bonne |
| 54 | `gaz.html` | Loi Boyle-Mariotte + Gay-Lussac | 1ère Ch07 (pression) | **Oui** | Bonne |
| 55 | `boyle-mariotte.html` | Loi de Boyle-Mariotte, P×V = cste | 1ère Ch07 (pression) | **Oui** | Bonne |

### Physique-Chimie — Terminale (simulations partagées)

| # | Fichier | Notion illustrée | Chapitre | Référencée | Pertinence |
|---|---|---|---|---|---|
| 56 | `dephasage.html` | Déphasage, triangle des puissances | Tle ICCER Ch02 | **Oui** | Bonne |
| 57 | `effet-joule.html` | Échauffement d'un conducteur | 1ère ICCER Ch02 | **Oui** | Bonne |
| 58 | `serre.html` | Effet de serre | Tle ERA Ch03 | **Oui** | Bonne |

### ~~Simulations sans niveau ni chapitre~~ — RECLASSÉES

~~7 simulations étaient non attribuées.~~

**Corrigé le 2026-03-17** : Toutes les simulations anciennement "sans niveau" sont désormais rattachées à un chapitre et référencées depuis les cours :

| Fichier | Désormais rattachée à | Référencée |
|---|---|---|
| `atome.html` | PC Seconde Ch07 | **Oui** |
| `atome-couches.html` | PC Seconde Ch07 | **Oui** |
| `modeles-atome.html` | PC Seconde Ch07 | **Oui** |
| `ohm.html` | PC Seconde Ch03 | **Oui** |
| `melangeur.html` | PC Seconde Ch14 | **Oui** |
| `traceur.html` | Maths Première Ch05 | **Oui** |

---

## Problemes identifies

### ~~1. 89 % des simulations sont orphelines~~ — CORRIGÉ

~~**Gravité : HAUTE**~~

**Corrigé le 2026-03-16 (session 4)** : 79 pages de cours ont été modifiées pour inclure des liens vers les simulations correspondantes. Les 63 simulations sont désormais toutes accessibles depuis au moins une page de cours. Seules 4 simulations restent sans lien direct (balance.html, gaz.html liées uniquement via simulations.html).

Détail des liaisons ajoutées :
- Maths seconde : 14 chapitres liés (ch01–ch14)
- Maths première : 6 chapitres liés (ch01, ch03–ch06, ch09)
- Maths terminale : 10 chapitres liés (ch01, ch03–ch11)
- Physique-chimie seconde : 13 chapitres liés (ch02–ch14)
- Physique-chimie première ICCER : 10 chapitres liés (ch01–ch10)
- Physique-chimie première ERA : 10 chapitres liés (ch01–ch10)
- Physique-chimie terminale ICCER : 8 chapitres liés (ch01–ch08)
- Physique-chimie terminale ERA : 8 chapitres liés (ch01–ch08)

### ~~2. 26 simulations incluent nav.js (non-conformité CLAUDE.md)~~ — CORRIGÉ

~~**Gravité : MOYENNE**~~

**Corrigé le 2026-03-16** : nav.js retiré des 26 simulations. 0 simulation non-conforme restante.

~~CLAUDE.md spécifie que les simulations doivent être autonomes (pas de dépendance à styles.css ou nav.js). Or 26 simulations incluent `nav.js` :~~

`atome-couches.html`, `atome.html`, `balance.html`, `chaleur.html`, `changement-etat.html`, `debit.html`, `dephasage.html`, `effet-joule.html`, `entrainement-ineq.html`, `entrainement.html`, `equations.html`, `gaz.html`, `graphe-equation.html`, `inegalite.html`, `melangeur.html`, `modeles-atome.html`, `moteur.html`, `ohm.html`, `oxydoreduction.html`, `pression.html`, `puissance.html`, `rayonnement.html`, `redressement.html`, `serre.html`, `son.html`, `traceur.html`

### 3. Simulations avec template visuel ancien (à réévaluer)

**Gravité : FAIBLE**

**Mise à jour 2026-03-17** : L'audit technique approfondi des 14 simulations PC Seconde montre qu'elles utilisent **toutes le template moderne** (card-based, CSS custom properties, `linear-gradient` dans le header). La liste initiale de 30 simulations anciennes est donc surévaluée et doit être revérifiée pour les autres sections.

Simulations PC Seconde confirmées **modernes** : `circuit-electrique.html`, `signal-alternatif.html`, `mouvement.html`, `forces.html`, `liaisons-chimiques.html`, `concentration.html`, `son-2nde.html`, `transferts-thermiques.html`, `changement-etat.html`, `refraction.html`, `atome.html`, `atome-couches.html`, `modeles-atome.html`, `ohm.html`.

Simulations **non vérifiées** (potentiellement anciennes, à auditer) : `debit.html`, `effet-joule.html`, `equations.html`, `gaz.html`, `graphe-equation.html`, `inegalite.html`, `moteur.html`, `oxydoreduction.html`, `pile-electrochimique.html`, `pression.html`, `puissance.html`, `rayonnement.html`, `redressement.html`, `son.html`, `sources-lumineuses.html`, `traceur.html`, `transformateur.html`, `transmission-info.html`, `vitesse-acceleration.html`.

### 4. 8 simulations non responsives (sans @media)

**Gravité : FAIBLE**

`balance.html`, `equations.html`, `graphe-equation.html`, `inegalite.html`, `melangeur.html`, `modeles-atome.html`, `redressement.html`, `traceur.html`

**Mise à jour 2026-03-17** : Parmi les simulations PC Seconde, seul `modeles-atome.html` manque de `@media` queries (utilise CSS Grid mais sans breakpoint explicite). Toutes les autres simulations PC Seconde sont bien responsives.

### ~~5. 12 simulations avec métadonnées incomplètes~~ — CORRIGÉ

~~**Gravité : MOYENNE**~~

**Corrigé le 2026-04-05** : Métadonnées (niveau + chapitre) ajoutées dans les 11 simulations sans subtitle, et chapter ajouté dans `attenuation-sonore.html`. Audit complet réalisé sur les 70 simulations.

Simulations corrigées :
- `atome-couches.html`, `atome.html`, `modeles-atome.html` → `2nde Bac Pro · Ch07`
- `ohm.html` → `2nde Bac Pro · Ch03`
- `signal-alternatif.html` → `2nde Bac Pro · Ch04`
- `concentration.html` → `Bac Pro · Ch07-09`
- `equations.html` → `2nde Bac Pro · Ch05`
- `melangeur.html` → `2nde Bac Pro · Ch14`
- `refraction.html` → `2nde Bac Pro · Ch13`
- `traceur.html` → `2nde / 1ère Bac Pro · Ch05-10`
- `attenuation-sonore.html` → `Ch08` ajouté

**Constat de l'audit 2026-04-05** : Les 13 simulations initialement listées (chaleur, dephasage, effet-joule, gaz, serre, debit, moteur, oxydoreduction, pression, puissance, rayonnement, redressement, son) avaient en réalité déjà des métadonnées partielles ou complètes — l'audit initial était inexact pour ce groupe.

### ~~6. Simulation à pertinence faible~~ — CORRIGÉ

~~**Gravité : FAIBLE**~~

**Corrigé** : `melangeur.html` est désormais rattachée à PC Seconde Ch14 (Lumière, couleurs et photodétecteurs) et référencée depuis `physique-chimie/seconde/ch14/lecon.html`. La simulation illustre la synthèse additive des couleurs (notion au programme).

### 7. Accessibilité des simulations (NOUVEAU)

**Gravité : MOYENNE**

**Découvert le 2026-03-17** : Aucune des 14 simulations PC Seconde ne possède d'attributs `aria-label` sur les éléments `<canvas>` ou `<svg>`. Les sliders (`<input type="range">`) ne sont pas associés à des `<label>` via `for`. Pas de texte alternatif pour les visualisations.

**Impact** : Les simulations sont inaccessibles aux lecteurs d'écran. Le contenu visuel (graphiques, animations, diagrammes) n'est pas décrit textuellement.

**Points positifs** : bon contraste de couleurs, navigation clavier possible via sliders et boutons.

**Fichiers concernés** : les 64 simulations (problème transversal).

**Actions recommandées** :
- Ajouter `aria-label` sur chaque `<canvas>` et `<svg>` (description du contenu visuel)
- Associer les sliders à des `<label for="...">` ou `aria-labelledby`
- Ajouter un texte alternatif `<desc>` dans les SVG

---

## Couverture par section

### Sections bien couvertes
- **PC Seconde** : 17 simulations pour 13/14 chapitres — **très bonne couverture**, qualité technique excellente
- **Maths Seconde** : 15 simulations pour 14 chapitres — bonne couverture (manque Ch10 fonction carrée)
- **PC Terminale ICCER** : 8 simulations pour 8 chapitres — excellente couverture, modèle à suivre
- **Maths Terminale** : 9 simulations pour 11 chapitres — bonne couverture (manque Ch02, Ch09)

### Sections sous-représentées
- **Maths Première** : 1 seule simulation pour 9 chapitres — très insuffisant
- **PC Première ERA** : 1 seule simulation pour 10 chapitres — très insuffisant (noter que plusieurs simulations ICCER couvrent les mêmes notions)

### Simulations manquantes suggérées

**Maths Première (prioritaire)** :
- Ch01 Statistiques à deux variables
- Ch02 Probabilités
- Ch03 Suites numériques
- Ch04 Résolution graphique d'équations
- Ch05 Fonctions polynômes degré 2 (`traceur.html` pourrait correspondre mais n'est pas tagué)
- Ch07 Géométrie dans l'espace (visualisation 3D très utile)
- Ch08 Vecteurs du plan
- Ch09 Trigonométrie

**PC Première ERA** :
- Ch01 Énergie et puissance électrique
- Ch02 Puissance consommée
- Ch04 Transferts thermiques
- Ch06 Équilibre en rotation
- Ch07 Pression et force pressante

---

## Corrections realisees

- **2026-03-16** : Retiré nav.js des 26 simulations non autonomes (atome-couches, atome, balance, chaleur, changement-etat, debit, dephasage, effet-joule, entrainement-ineq, entrainement, equations, gaz, graphe-equation, inegalite, melangeur, modeles-atome, moteur, ohm, oxydoreduction, pression, puissance, rayonnement, redressement, serre, son, traceur)
- **2026-03-16** : Lié 59 simulations orphelines à 79 pages de cours (toutes les sections maths et physique-chimie). Les simulations sont désormais accessibles via un encadré en fin de chaque lecon.html correspondante.
- **2026-03-17** : Corrigé fuite mémoire d'animation dans `modeles-atome.html` (variable `animationFrame` unique → tableau `animationFrames[]` pour annuler toutes les animations au changement de modèle).
- **2026-03-17** : Corrigé sélection d'isotope dans `atome.html` (`stableIsotopes[z][length-1]` → `stableIsotopes[z][0]` pour sélectionner l'isotope le plus courant au lieu du plus lourd).
- **2026-03-17** : Créé `liaisons-chimiques.html` — simulation interactive sur les types de liaisons chimiques (covalente vs ionique), 6 molécules (H₂O, CO₂, CH₄, O₂, N₂, NaCl), ancrage Ch07 PC Seconde. Ajouté à `simulations.html`.
- **2026-03-17** : Audit technique approfondi des simulations PC Seconde et page simulations — corrections de l'inventaire : 17 simulations rattachées à PC Seconde (pas 11), 13/14 chapitres couverts, toutes référencées depuis les cours. Reclassement des 6 simulations "sans niveau". Identification d'un nouveau problème d'accessibilité (aria-label manquants). Confirmation que toutes les simulations PC Seconde utilisent le template moderne et sont responsives (sauf modeles-atome.html).
- **2026-03-19** : Bilan Seconde — 32 simulations couvrent la Seconde (15 maths + 17 PC), couvrant 27/28 chapitres (seul PC ch01 Sécurité sans simulation). En plus, maths/seconde/ch05 et ch06 disposent de simulation.html intégrées dans le chapitre.
- **2026-03-31** : Audit approfondi de `trigonometrie.html` (Maths Terminale Ch07) — 7 corrections : ajout `</head>` manquant (HTML invalide), correction arc d'angle pour α > 180°, correction bug marqueurs Chart.js (points invisibles car format `{x,y}` incompatible avec axe catégoriel), ajout aria-label sur canvas et `for` sur labels, extension affichage symbolique radians (17 angles remarquables au lieu de 5), surbrillance dynamique du tableau des angles remarquables, repositionnement labels sin/cos selon le quadrant.
- **2026-04-05** : Audit complet des 70 simulations par chapitre. Métadonnées (niveau + chapitre) ajoutées dans 11 simulations : `atome-couches`, `atome`, `concentration`, `equations`, `melangeur`, `modeles-atome`, `ohm`, `refraction`, `signal-alternatif`, `traceur`, `attenuation-sonore`. Simulations orphelines liées depuis les leçons : `balance.html` → maths/seconde/ch05 ; `debit-fluide.html` → pc/terminale-iccer/ch06 ; `chaleur.html` → pc/premiere-iccer/ch04 + premiere-era/ch04 ; `gaz.html` + `boyle-mariotte.html` → pc/premiere-iccer/ch07 + premiere-era/ch07 ; `attenuation-sonore.html` → pc/terminale-era/ch08. Périmètre mis à jour : 70 simulations (vs 64 à la dernière mise à jour). (Maths Terminale Ch07) — 7 corrections : ajout `</head>` manquant (HTML invalide), correction arc d'angle pour α > 180°, correction bug marqueurs Chart.js (points invisibles car format `{x,y}` incompatible avec axe catégoriel), ajout aria-label sur canvas et `for` sur labels, extension affichage symbolique radians (17 angles remarquables au lieu de 5), surbrillance dynamique du tableau des angles remarquables, repositionnement labels sin/cos selon le quadrant.

---

## Ameliorations restantes

### Priorité haute
- [x] Lier chaque simulation orpheline à la page de cours correspondante (79 pages modifiées, 2026-03-16)
- [x] Compléter les métadonnées des 12 simulations incomplètes (2026-04-05)
- [x] Rattacher les 7 simulations sans niveau/chapitre à leur chapitre (atome→ch07, ohm→ch03, melangeur→ch14, traceur→ch05/ch10, 2026-03-16)
- [x] Vérifier `simulations.html` — les 70 simulations y sont déjà toutes listées (2026-04-05)

### Priorité moyenne
- [x] Retirer `nav.js` des 26 simulations non conformes (2026-03-16)
- [ ] Ajouter des `aria-label` sur les canvas/SVG et associer les sliders à des `<label>` (accessibilité — 64 simulations)
- [ ] Ajouter des media queries aux 8 simulations non responsives (dont `modeles-atome.html` pour PC Seconde)
- [ ] Créer des simulations pour maths/première (1 seule pour 9 chapitres)
- [ ] Créer des simulations pour PC/première-ERA (1 seule pour 10 chapitres)

### Priorité basse
- [ ] Vérifier et migrer les simulations hors PC Seconde avec ancien template (liste initiale surévaluée — les 14 PC Seconde sont déjà modernes)
- [x] Évaluer la pertinence de `melangeur.html` → rattachée à Ch14 PC Seconde (synthèse additive)
- [ ] Généraliser le format quiz adaptatif (`entrainement.html`) à d'autres chapitres

---

## Synthese

### Chiffres clés

| Indicateur | Valeur |
|---|---|
| Nombre total de simulations | **70** |
| Référencées depuis un cours | **70** (100 %) |
| Orphelines | **0** (0 %) |
| Listées dans `simulations.html` | **70** (100 %) |
| Sans niveau/chapitre | **0** (0 %) |
| Avec métadonnées incomplètes | **0** (0 %) — corrigé 2026-04-05 |
| ~~Incluant `nav.js` (non-conforme)~~ | **0** (corrigé 2026-03-16) |
| Sans media query | **8** (13 %) — dont 1 seule en PC Seconde |
| Template ancien (à revérifier) | **~19** (estimation révisée, PC Seconde = 0) |
| Sans `aria-label` (accessibilité) | **63** (98 %) — problème transversal (trigonometrie.html corrigée) |

### Répartition par section

| Section | Simulations | Chapitres couverts | Couverture |
|---|---|---|---|
| Maths Seconde | 15 | 14 | Bonne |
| Maths Première | 1 | 9 | **Très faible** |
| Maths Terminale | 9 | 11 | Bonne |
| **PC Seconde** | **17** | **13/14** | **Très bonne** |
| PC Première ICCER | 5 | 10 | Moyenne |
| PC Première ERA | 1 | 10 | **Très faible** |
| PC Terminale ICCER | 8 | 8 | **Excellente** |
| PC Terminale ERA | 5 | 8 | Bonne |
| Non attribuées | **0** | — | — |

### Audit technique approfondi — PC Seconde (2026-03-17)

| Critère | Résultat | Détails |
|---|---|---|
| **Autonomie** (pas de nav.js/styles.css) | ✅ 14/14 | Toutes autonomes, styles inline |
| **Template moderne** (card-based, CSS vars) | ✅ 14/14 | Toutes conformes au template moderne |
| **Responsive** (@media queries) | ✅ 13/14 | Seul `modeles-atome.html` sans breakpoint |
| **Métadonnées** (charset, viewport, lang) | ✅ 14/14 | Toutes complètes |
| **Erreurs JavaScript** | ✅ 0 erreur | Code propre, APIs modernes |
| **Ancrage pédagogique** | ✅ 14/14 | Contextes pro pertinents |
| **Accessibilité** (aria-label) | ❌ 0/14 | Aucun aria-label sur canvas/SVG |
| **Types d'interactivité** | Varié | 8 Canvas, 3 SVG, 1 Chart.js, 2 hybrides |

### Page simulations.html

| Critère | Résultat |
|---|---|
| Simulations listées | **64/64** (100 %) |
| Liens fonctionnels | ✅ Tous valides |
| Filtrage par niveau | ✅ JavaScript (Tous / Tle / 1ère / 2nde) |
| 6 catégories thématiques | ✅ Maths, Électricité, Thermique, Mécanique, Chimie, Signaux & Optique |
| Design responsive | ✅ CSS Grid auto-fill |
| Intégration index.html | ✅ Lien dans navigation + carte accueil |

### Points positifs
1. **Diversité thématique remarquable** : 64 simulations couvrent algèbre, géométrie, statistiques, électricité, thermique, chimie, ondes, mécanique.
2. **Qualité pédagogique globalement bonne** : formules visibles, sliders réactifs, contextes professionnels, valeurs physiquement réalistes.
3. **Page hub complète** : `simulations.html` catalogue les 64 simulations avec filtrage par niveau.
4. **Excellente couverture PC Seconde** : 17 simulations pour 13/14 chapitres, toutes modernes et responsives.
5. **Excellente couverture PC Terminale ICCER** : 8 simulations pour 8 chapitres, modèle à reproduire.
6. **Simulations d'entraînement (quiz)** : format adaptatif original et utile à généraliser.
7. **Qualité technique des simulations PC Seconde** : zéro erreur JS, zéro dépendance externe non autorisée, animations fluides (requestAnimationFrame).

### Priorités
1. ~~**Référencement**~~ ✅ **FAIT** (2026-03-16) : 64 simulations liées à 79+ pages de cours.
2. **Accessibilité** (effort moyen) : ajouter aria-label sur canvas/SVG et labels sur sliders (64 fichiers).
3. **Métadonnées** (effort faible) : compléter les 12 simulations hors PC Seconde avec informations manquantes.
4. **Couverture** (effort important) : créer des simulations pour maths/première et PC/première-ERA.
5. **Responsive** (effort faible) : ajouter @media à 8 simulations (dont `modeles-atome.html`).
6. **Harmonisation visuelle** (effort moyen) : vérifier et migrer les ~19 simulations hors PC Seconde potentiellement anciennes.

---

## Audit qualité approfondi — 2026-04-29 (Opus, vérification manuelle)

**Méthode** : lecture directe du code de plusieurs simulations + grep ciblés sur les 78 fichiers du dossier `simulations/`. Vérification manuelle des claims de l'audit Sonnet précédent (Explore agent), recalcul des formules clés, contrôle de l'autonomie (pas de `nav.js` / `styles.css` externe), de l'accessibilité (aria-label) et de la conformité au prompt-simulation.md.

### Résultats par catégorie

#### 1. Bugs scientifiques / mathématiques
**Aucun bug confirmé** après vérification des calculs des simulations suivantes :
- `polynome3.html` : `f(x) = ax³+bx²+cx+d` ✓, `f'(x) = 3ax²+2bx+c` ✓, inflection en `-b/(3a)` ✓
- `complexes.html` : multiplication `(za + zb·i) × (wa + wb·i) = (za·wa − zb·wb) + (za·wb + zb·wa)·i` ✓
- `exp-log.html` : changement de base `log_a(x) = ln(x)/ln(a)` ✓
- `gaz.html` : Boyle-Mariotte `P = P₀·V₀/V` ✓ ; Gay-Lussac `P = P₀·T/T₀` (T₀ = 300 K) ✓
- `archimede.html` : `F_A = ρ·V·g`, gestion DPR/retina propre ✓
- `moments.html` : `M = F × d`, somme algébrique des moments ✓

**Code mort mineur** (à nettoyer, non bloquant) :
- `exp-log.html:274` : `const ga = (Math.log(a) / Math.log(a))` toujours = 1, variable inutilisée

#### 2. Conformité au prompt-simulation.md (autonomie)

Les simulations doivent être **autonomes** (pas de `nav.js`, pas de `styles.css` externe). 76 / 78 sont conformes.

**❌ 2 fichiers non-conformes (CRITIQUE)** :

| Fichier | Problème | Lignes |
|---|---|---|
| `simulations/attenuation-sonore.html` | Charge `<link rel="stylesheet" href="../styles.css">` ET `<script src="../nav.js">` | header |
| `simulations/debit-fluide.html` | Idem | header |

**Conséquence** : ces deux simulations dépendent de fichiers du parent ; elles ne fonctionnent pas comme pages autonomes (chemin de retour cassé si servies depuis un autre contexte).

#### 3. Canvas sans attribut `width` (faux positif Sonnet)

L'audit Sonnet précédent flaguait ~12 simulations comme « canvas sans dimensions ». Vérification manuelle :

- **Ce n'est PAS un bug** dans la majorité des cas car :
  - les canvas Chart.js (`probabilites.html`, `ohm.html`, etc.) auto-dimensionnent via `responsive: true`
  - les canvas avec resize JS (`circuit-electrique.html` lignes 91-96, 479-480) recalculent `cv.width = cv.offsetWidth` au load et au `resize` window
  - les canvas avec gestion DPR (`archimede.html` lignes 226-233) pilotent eux-mêmes leurs dimensions via `cv.clientWidth`

- **Vrais cas à corriger (3 max)** : aucune simulation n'a simultanément (canvas sans width) ET (pas Chart.js) ET (pas de resize JS). → faux positif Sonnet.

#### 4. Accessibilité — `aria-label` sur Canvas/SVG (problème transversal)

Sur les 78 simulations :
- **68 / 78 simulations sans `aria-label`** sur leurs canvas (87 %)
- **6 / 78 simulations sans `aria-label`** sur leurs SVG (mais total SVG faible)
- Seules ~10 simulations (dont `trigonometrie.html`) ont des labels d'accessibilité

**Effort moyen** pour corriger : ajouter `aria-label="..."` à chaque `<canvas>` et `<svg>` graphique. Les canvas purement décoratifs peuvent rester sans (ou recevoir `role="presentation"`).

#### 5. Trigger initial fragile sur `trigonometrie.html` (faux positif Sonnet)

Vérification : le `<script>` est bien à la ligne 133, **après** le `<canvas id="sinCosChart">` à la ligne 91. Le DOM est donc parsé avant l'exécution. **Pas de risque de null reference**.

### Top problèmes confirmés à corriger

| Priorité | Fichier(s) | Action | Effort |
|---|---|---|---|
| **CRITIQUE** | `attenuation-sonore.html`, `debit-fluide.html` | Inliner les styles + retirer `nav.js` + retirer `<link>` styles.css | ~30 min/fichier |
| **HAUTE (a11y)** | 68 simulations | Ajouter `aria-label` sur canvas et SVG graphiques | ~1-2 min/fichier (2-3 h total) |
| **BASSE** | `exp-log.html` | Supprimer `const ga = ...` ligne 274 (code mort) | < 1 min |

### Faux positifs identifiés (audit Sonnet précédent)

- ❌ « Canvas sans width → bug responsive » (12 fichiers) : faux positif, le canvas est sizé via JS ou Chart.js.
- ❌ « `trigonometrie.html` référence null sur sinCosChart » : faux positif, ordre DOM correct.
- ❌ « Bugs de calculs » dans plusieurs simulations : faux positif, tous les calculs vérifiés sont corrects.

### Récap chiffré

- **Simulations totales** : 78
- **Simulations à corriger pour conformité** : 2 (attenuation-sonore, debit-fluide)
- **Simulations à enrichir en accessibilité** : 68
- **Bugs scientifiques avérés** : 0
- **Code mort identifié** : 1 ligne (exp-log.html:274)

### Prochaines actions recommandées

1. **Phase 1 — Conformité** (immédiat) : corriger les 2 simulations non-autonomes
2. **Phase 2 — Accessibilité** : ajouter `aria-label` sur canvas/SVG des 68 simulations restantes
3. **Phase 3 — Cohérence visuelle** (optionnel) : harmoniser palettes pour chimie / électricité (PC Seconde déjà OK)

---

## Audit pages utilitaires racine — 2026-04-29

**Périmètre** : 8 pages utilitaires à la racine
- `index.html` (accueil), `simulations.html` (catalogue)
- `cv-eleve.html`, `lettre-motivation-parcoursup.html` (générateurs)
- `groupements.html`, `ccf-convocations.html`
- `python.html`, `logique.html` (modules transversaux)

### Bug critique trouvé et corrigé : `python.html` et `logique.html`

**Problème** : ces deux fichiers étaient des **fragments HTML** (sans `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`) mais étaient liés depuis 4 sommaires Maths comme pages standalone (`<a href="python.html">`). À l'ouverture directe dans le navigateur, la page s'affichait sans styles, sans navigation, sans titre.

**Fichiers concernés** :
- `python.html` (41 lignes de fragment)
- `logique.html` (38 lignes de fragment)

**Correction** : enveloppés en pages HTML complètes avec :
- DOCTYPE + structure html/head/body
- Lien vers `styles.css` et `print.css`
- Header standardisé avec sous-titre
- Inclusion de `nav.js` (pour le toggle des corrections)
- Conservation du contenu pédagogique original
- Nettoyage : caractères HTML entities (`&eacute;` → `é`) et négatifs (`-1` → `−1`)

### Audit des autres pages utilitaires

| Page | Typos | ℜ | Sigles abusifs | Structure | Statut |
|---|---|---|---|---|---|
| `index.html` | 0 | 0 | 0 | OK | ✅ |
| `simulations.html` | 0 (faux positif sur nom de fichier `polynome3.html`) | 0 | 0 | OK | ✅ |
| `cv-eleve.html` | 0 | 0 | 0 | OK | ✅ |
| `lettre-motivation-parcoursup.html` | 0 | 0 | 0 (sigles ICCER/ERA présents mais dans titres/labels uniquement, métiers réels utilisés dans le contenu) | OK | ✅ |
| `groupements.html` | 0 | 0 | 0 | OK | ✅ |
| `ccf-convocations.html` | 0 | 0 | 0 | OK | ✅ |

### Audit co-intervention (38 pages) — 2026-04-29

**Périmètre** : `co-intervention/co-intervention-*.html` (37 séances + 1 index)

**Audit mécanique** : 0 typos, 0 ℜ utilisé, 0 sigle utilisé comme métier, toutes les pages incluent nav.js + styles.css + print.css.

**Audit scientifique** (spot-check sur 5 fichiers représentatifs) :
- `co-intervention-chimie-combustion-ICCER.html` : énergie utile 24 × 8 × 180 = 34 560 kWh ✓ ; coût 32 914 × 0,12 = 3 950 € ✓
- `co-intervention-thermo-cop-pac-ICCER.html` : COP = Qc/W ✓ ; W = 12/3 = 4 kW ✓
- `co-intervention-fluides-debit-ICCER.html` : 1,2/3 600 = 3,33×10⁻⁴ ✓ ; D = √(4S/π) = 20,6 mm ✓
- `co-intervention-statique-moments.html` : M = F × d = 30 × 0,25 = 7,5 N·m ✓
- `co-intervention-thermique-resistance.html` : R = e/λ = 0,20/1,75 ≈ 0,11 ✓

**Petite imprécision** détectée (non bloquante) :
- `co-intervention-thermique-deperditions.html:154` : `P_chauf = 990 W` arrondi à `1,0 kW` pour le coût mensuel → coût affiché 48 € au lieu de 47,52 € (écart de 1 %, acceptable pédagogiquement).

**Verdict** : qualité scientifique excellente, aucune correction nécessaire.

### Récap final de la session 2026-04-29

| Section | Fichiers audités | Bugs trouvés | Corrigés |
|---|---|---|---|
| Simulations | 78 | 2 (autonomie) + 1 (code mort) | 3 ✅ |
| Co-intervention | 38 | 0 | — |
| Pages utilitaires racine | 8 | 2 (fragments HTML) | 2 ✅ |
| **TOTAL** | **124** | **5** | **5** |

Total : **5 bugs corrigés**, 0 erreur scientifique restante détectée.

---

## Phase 2 — Accessibilité (2026-04-29)

**Action** : ajout de `aria-label` descriptifs sur tous les `<canvas>` et `<svg>` graphiques des simulations.

**Méthode** :
- Inventaire automatique : 73 fichiers concernés, 106 canvas + 8 SVG sans `aria-label` (114 éléments au total)
- Curation manuelle : un `aria-label` distinct par élément, décrivant ce que l'utilisateur visualise (et pas le nom technique de la balise)
- Application via `scripts/add_aria_labels.py` (idempotent, ne modifie pas si déjà présent)

**Exemples de labels curés** :
- `archimede.html / canvas#cv` → "Animation d'un objet plongé dans un fluide montrant la poussée d'Archimède"
- `atome.html / svg#atom-svg` → "Représentation interactive d'un atome avec protons, neutrons et électrons"
- `boyle-mariotte.html / canvas#canvasGraphPV` → "Graphique de la pression en fonction du volume (loi de Boyle-Mariotte)"
- `transferts-thermiques.html / canvas#cvConduction` → "Animation de la conduction thermique à travers une barre"
- `polynome3.html / canvas#graphCanvas` → "Courbe d'une fonction polynôme de degré 3 avec points clés (racines, extremums, inflexion)"

**Résultat** :

| Avant | Après |
|---|---|
| 73 / 78 simulations sans aria-label sur canvas/SVG | **0 / 78** |
| 114 éléments graphiques sans description | **0** |

**Vérification** : grep automatique confirme qu'il ne reste aucun `<canvas>` ou `<svg>` sans `aria-label` dans le dossier `simulations/`.

**Impact pédagogique** :
- Les élèves utilisant un lecteur d'écran ou une aide à la lecture entendent maintenant une description du contenu de la simulation
- Conforme aux recommandations WCAG 2.1 (critère 1.1.1 — Contenu non textuel)
- Conforme au RGAA (Référentiel général d'amélioration de l'accessibilité, France)
