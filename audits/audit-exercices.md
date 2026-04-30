# Audit Pédagogique des Exercices

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-04-30 (audits scientifiques avril : 5 sections PC + Maths CAP + 17 fichiers HTML structure réparée)
**Périmètre** : exercices.html, ds.html, qcm.html et interro.html — 8 sections (maths seconde/première/terminale, physique-chimie seconde/première-iccer/première-era/terminale-iccer/terminale-era)
**Méthode** : échantillonnage de 2-3 fichiers exercices.html et 2-3 fichiers ds.html par section, lecture et analyse qualitative.

---

## Méthodologie

- **Fichiers échantillonnés** : ~30 fichiers (exercices.html et ds.html) répartis sur les 8 sections.
- **Critères évalués** : cohérence avec le chapitre, adaptation au niveau Bac Pro, progression de difficulté, diversité des contextes, cohérence filière (ICCER → chauffage/énergie, ERA → menuiserie/agencement), qualité des corrections, utilisation de la différenciation (socle/standard/appro).

---

## Analyse par section

### 1. Maths — Seconde

**Qualité globale : 4.5/5** *(révisé 2026-03-25 — audit exhaustif des 14 chapitres avec lecture directe des fichiers ; était 5/5 basé sur un échantillon de 3 chapitres, puis 4/5 sur la base d'un audit périmé)*

**Fichiers analysés** : tous les 14 chapitres (ch01-ch14), exercices.html — vérification directe fichier par fichier, 2026-03-25

**Couverture des fichiers** : 14/14 chapitres ont les 6 types obligatoires (lecon, exercices, ds, fiche, qcm, interro). 2/14 ont simulation.html (ch05, ch06). **14/14 ont activite.html** ✓ *(rectifié 2026-03-26 — présents depuis 2026-03-22, non détectés lors de l'audit du 25 mars)*

#### Tableau par chapitre — état vérifié au 25 mars 2026

| Ch | Titre | Exercices | Corrigés | Couverture | Socle | Std | Appro |
|----|-------|-----------|----------|-----------|-------|-----|-------|
| 01 | Proportionnalité et pourcentages | 30 | 30 | **100%** ✓ | 12 | 10 | 8 |
| 02 | Statistiques à une variable | 30 | 30 | **100%** ✓ | 15 | 11 | **4** ⚠ |
| 03 | Indicateurs statistiques | 30 | 30 | **100%** ✓ | 17 | 10 | **3** ⚠ |
| 04 | Probabilités et fluctuation | 30 | 30 | **100%** ✓ | 15 | **8** ⚠ | 7 |
| 05 | Équations du premier degré | 30 | 30 | **100%** ✓ | 12 | 10 | 8 |
| 06 | Inéquations du premier degré | 42 | 42 | **100%** ✓ | 19 | 12 | 11 |
| 07 | Notion de fonction | 40 | 40 | **100%** ✓ | 18 | 12 | 10 |
| 08 | Fonction linéaire | 41 | 41 | **100%** ✓ | 18 | 12 | 11 |
| 09 | Fonction affine | 48 | 48 | **100%** ✓ | 23 | 14 | 11 |
| 10 | Fonction carré et variations | 46 | 46 | **100%** ✓ | 19 | 15 | 12 |
| 11 | Figures planes | 40 | 40 | **100%** ✓ | 15 | 14 | 11 |
| 12 | Pythagore et réciproque | 40 | 40 | **100%** ✓ | 15 | 14 | 11 |
| 13 | Thalès dans le triangle | 45 | 45 | **100%** ✓ | 19 | 15 | 11 |
| 14 | Solides, volumes, agrandissement | 46 | 46 | **100%** ✓ | 16 | 15 | **15** ★ |
| **Total** | | **518** | **518** | **100% ✓** | | | |

**Points forts** :
- **518 exercices, 100% corrigés** (mises à jour du 2026-03-22 : augmentation à 30–48 exercices par chapitre, numérotation séquentielle harmonisée, format uniformisé).
- Différenciation (socle/standard/appro avec diff.js) systématique sur les 14 chapitres.
- Contextes professionnels menuiserie-agencement bien intégrés, dont ch12 (équerrage de cadres, tracé chantier) et ch13 (réduction/agrandissement en atelier).
- Ch06, ch07, ch08 : exercices avec textarea (espace de travail élève) et canvas/Chart.js.
- Ch14 : différenciation exemplaire (16/15/15 — parfaitement équilibré).
- DS 100% corrigés avec barèmes, compétences (APP/ANA/REA/VAL/COM).
- Liens retour corrects sur tous les chapitres (ch11 et ch12 corrigés).

**Points faibles** :
- Ch02 (4 blocs appro) et ch03 (3 blocs appro) : approfondissement très insuffisant pour les élèves en poursuite BTS. Objectif : 10-12 blocs.
- Ch04 : standard faible (8 blocs) et approfondissement limité (7 blocs).
- ~~Aucun `activite.html`~~ → **14/14 activite.html présents** (rectifié 2026-03-26).
- Simulations uniquement pour ch05 et ch06 — ch07-ch10 (fonctions) bénéficieraient d'outils de visualisation interactive.
- ~~CSS inline : `.methode` et `.cell-blank` redéfinis dans ch10 (et ch06, ch09) alors que `.meth` est déjà dans styles.css.~~ → **RÉSOLU 2026-03-26** (ch06, ch09, ch10, ch13, ch14 nettoyés ; `.cell-blank` amélioré dans styles.css)
- ~~Ch07 exercice 12 : étiquette « type BTS » potentiellement décourageante pour une seconde Bac Pro.~~ → **RÉSOLU 2026-03-26** (remplacé par « Approfondissement »)

---

### 2. Maths — Première

**Qualité globale : 4/5** *(rectifié 2026-03-19, était 2/5)*

**Fichiers analysés** : tous les 9 chapitres (ch01-ch09), exercices.html + ds.html — audit manuel complet 2026-03-19

**Chiffres** : 100 exercices + 19 DS = 119, tous corrigés (100%).

**Points forts** :
- ch01 (Statistique à deux variables) : contenu complet avec nuages de points Chart.js, contextes professionnels (ventes de bois, consommation électrique d'atelier).
- ch05 (Polynômes degré 2) : 9 exercices complets avec corrections (arche de pont, bénéfice artisan, trajectoire projectile).
- ch09 (Trigonométrie) : 15 exercices avec différenciation diff-socle/diff-standard/diff-appro — seul chapitre de Première à utiliser le système de différenciation formelle.
- ch06 (Dérivation) : 12 exercices bien progressifs avec optimisation.
- DS bien structurés avec compétences et barèmes sur tous les chapitres.

**Points faibles** :
- Seul ch09 utilise la différenciation formelle (diff.js). Les autres chapitres (ch01-ch08) utilisent une progression de difficulté implicite mais sans les tags diff-socle/diff-standard/diff-appro.
- Nombre d'exercices variable : 9 (ch04, ch05, ch08) à 15 (ch09).

---

### 3. Maths — Terminale

**Qualité globale : 4.5/5** *(rectifié 2026-03-19, était 3.5/5)*

**Fichiers analysés** : tous les 11 chapitres (ch01-ch11), exercices.html + ds.html — audit manuel complet 2026-03-19

**Chiffres** : 171 exercices + 78 DS = 249, tous corrigés (100%).

**Points forts** :
- Différenciation systématique avec Socle (S1-S3), Standard et Approfondissement sur tous les chapitres.
- ch04 (Polynômes degré 3) : le plus riche avec 20 exercices incluant 4 exercices d'approfondissement (A1-A4).
- ch02 (Probabilités) : 17 exercices + 14 DS (7 variantes différenciées — le plus complet).
- DS différenciés sur 3 niveaux (socle/standard/appro), tous avec corrections via `<details>`.
- Corrections substantielles avec solutions détaillées, MathJax, étapes intermédiaires.

**Points faibles** :
- ch11 (Produit scalaire) : contenu avancé (identité de polarisation, équation cartésienne, vecteur normal, distance point-droite) — potentiellement hors programme Bac Pro.
- Toutes les corrections utilisent `<details><summary>` — cohérent en interne mais différent des autres sections.

---

### 4. Physique-Chimie — Seconde

**Qualité globale : 4/5**

**Fichiers analysés** : ch01/exercices.html, ch07/exercices.html, ch14/exercices.html

**Points forts** :
- ch01 (Sécurité en laboratoire) : pictogrammes SVG, contextes menuiserie (white-spirit, EPI pour décapant) — très pertinent pour des élèves de seconde professionnelle.
- ch07 (Structure de la matière) : modèle de Bohr en SVG, notation symbolique bien guidée, encadrés méthode et attention.
- ch14 (Lumière, couleurs) : spectre visible en SVG, formules c=λf et E=Φ/S bien amenées.
- Bon étayage pédagogique avec `.meth` et `.att` pour guider les élèves.

**Points faibles** :
- Différenciation (socle/standard/appro) moins systématique que dans les maths seconde.

---

### 5. Physique-Chimie — Première ICCER

**Qualité globale : 4.5/5**

**Fichiers analysés** : ch01/exercices.html, ch05/exercices.html, ch10/exercices.html, ch01/ds.html

**Points forts** :
- Contextualisation filière ICCER excellente et cohérente : radiateur soufflant, circulateur de chauffage, thermostat connecté (ch01), monte-charge, ascenseur de chantier (ch05), ondes EM et radio FM (ch10).
- Exercices socle bien guidés avec cases à remplir et étapes décomposées (chauffe-eau dans ch01).
- Formules clairement identifiées : P=UI, E=Pt, conversion kWh.
- DS ch01 : contexte local technique avec radiateur, bien structuré avec compétences.

**Points faibles** :
- ch10 (Ondes EM) : le lien avec le métier ICCER est un peu plus ténu que pour les autres chapitres — les exercices sur la radio FM sont intéressants mais moins directement professionnels.

---

### 6. Physique-Chimie — Première ERA

**Qualité globale : 4.5/5**

**Fichiers analysés** : ch01/exercices.html, ch05/exercices.html, ch10/exercices.html

**Points forts** :
- Contextualisation ERA pertinente et distincte de l'ICCER : ponceuse, scie circulaire, aspirateur à copeaux (ch01), mur béton vs laine de verre (ch05), écho dans un hangar/atelier (ch10).
- ch05 (Minimiser les transferts thermiques) : excellente pertinence professionnelle pour menuiserie/agencement (conductance, flux thermique, comparaison matériaux isolants).
- ch10 : exercice d'écho dans un hangar de menuiserie — bon ancrage ERA.

**Points faibles** :
- La différenciation formelle (tags diff-socle/diff-standard/diff-appro) n'est pas toujours visible.

---

### 7. Physique-Chimie — Terminale ICCER

**Qualité globale : 5/5** *(rectifié 2026-03-22, était 4/5 — passage de 126 à 240 exercices, 30 par chapitre avec différenciation complète)*

**Fichiers analysés** : tous les 8 chapitres (ch01-ch08), exercices.html + ds.html — audit 2026-03-19, augmentation 2026-03-22

**Chiffres** : 240 exercices + 70 DS = 310, tous corrigés (100%). 30 exercices par chapitre (~10 socle, ~12 standard, ~8 appro).

**Points forts** :
- ch01 (Puissances P, S, Q, cos φ) : contenu avancé mais approprié pour terminale ICCER — triangle des puissances, compensation, monophasé/triphasé. Contexte chaufferie.
- ch04 (Rayonnement thermique) : lois de Stefan-Boltzmann et Wien bien amenées, exercices socle avec tableaux de conversion de température pré-structurés.
- ch08 (Signal sonore) : formule de Sabine, atténuation, calculs dB — section formules complète et bien organisée.
- DS ch01 : radiateur en local technique, compétences identifiées.
- Différenciation systématique sur les 8 chapitres avec 30 exercices par chapitre (socle/standard/appro).
- Contextes professionnels ICCER variés : chauffagiste, installateur thermique, technicien CVC, PAC, panneaux solaires.

**Points faibles** :
- Le niveau de formalisme mathématique (cos φ, puissance réactive) est élevé — les exercices socle doivent être particulièrement guidés pour rester accessibles.

---

### 8. Physique-Chimie — Terminale ERA

**Qualité globale : 5/5** *(rectifié 2026-03-22, était 4/5 — passage de 96 à 240 exercices, 30 par chapitre avec différenciation complète)*

**Fichiers analysés** : tous les 8 chapitres (ch01-ch08), exercices.html + ds.html — audit 2026-03-19, augmentation 2026-03-22

**Chiffres** : 240 exercices + ~40 DS = ~280, tous corrigés (100%). 30 exercices par chapitre (~8 socle, ~12 standard, ~10 appro).

**Points forts** :
- ch01 (Transporter l'énergie électrique) : schéma SVG du réseau HT/MT/BT, transformateurs, pertes Joule, rendement — bon contenu pour ERA.
- ch04 (Vitesse et accélération) : graphe v(t) en SVG, MRU/MRUA, distance de freinage — contextes variés.
- ch08 (Atténuer une onde sonore) : diagramme SVG de paroi, tableau des niveaux sonores réglementaires, indice d'affaiblissement, loi de masse — excellent ancrage ERA.
- DS ch01 : convoyeur triphasé, légende des compétences, bonne structure.
- Différenciation systématique sur les 8 chapitres avec 30 exercices par chapitre (socle/standard/appro).
- Contextes professionnels ERA variés : menuisier agenceur, ébéniste, poseur, artisan menuisier.

**Points faibles** :
- ch04 sur vitesse/accélération : le lien avec le métier ERA (menuiserie/agencement) est indirect — les contextes pourraient être plus spécifiques au domaine.

---

## Problemes identifies

### 1. ~~Fichiers exercices vides en Maths Première~~ — RÉSOLU

**~~Gravité : CRITIQUE~~** → **RÉSOLU (2026-03-19)**

~~Maths première ch05 (Polynômes degré 2) et ch09 (Trigonométrie) sont des stubs « Contenu à venir ».~~

**Rectificatif** : L'audit du 2026-03-16 était erroné. Les fichiers ch05/exercices.html (9 exercices) et ch09/exercices.html (15 exercices) sont **complets** avec corrections substantielles. L'erreur provenait probablement d'une version antérieure des fichiers, depuis complétée.

### 2. 29 pages BTS stub (contenu placeholder)

**Gravité : MOYENNE**

Dans `maths/bts/`, 29 fichiers (exercices.html et ds.html) ne contiennent qu'un message placeholder : *"Ce devoir surveillé est en cours de rédaction. Le contenu sera disponible prochainement."*

Chapitres concernés : ch01 (ds), ch02 (ds), ch03 (ds + exo), ch04 (ds), ch05 (ds), ch06 (ds + exo), ch07 (ds + exo), ch08 (ds), ch09 (ds + exo), ch10 (ds + exo), ch11 (ds + exo), ch12 (ds), ch13 (ds), ch14 (ds + exo), ch15 (ds + exo), ch16 (ds + exo), ch17 (ds + exo), ch18 (ds + exo).

### 3. Différenciation inégale entre sections

**Gravité : MOYENNE**

La différenciation (socle/standard/appro avec diff.js) est systématique et exemplaire en maths seconde. Elle est présente mais moins formalisée en physique-chimie première et terminale. En maths première, elle est totalement absente (18 fichiers). En maths terminale, certains fichiers semblent ne pas utiliser les tags diff-*. L'objectif devrait être d'atteindre le niveau de systématicité de maths seconde sur toutes les sections de première et terminale.

### 4. Exercices potentiellement hors programme

**Gravité : MOYENNE**

- Maths terminale ch11 (Produit scalaire) : équation cartésienne via vecteur normal, distance point-droite — vérifier la conformité avec le programme Bac Pro.
- Maths seconde ch07 exercice 12 « type BTS » — label qui peut décourager les élèves même en appro.

### 5. Deux mécanismes de correction coexistent

**Gravité : FAIBLE**

Les corrections utilisent deux patterns différents selon les sections :
- **maths/premiere** : `<details class="corr-wrap"><summary class="corr-btn">` (HTML5 sémantique, sans JS)
- **physique-chimie** : boutons `.bc` avec `onclick` (nécessite JS)

Les deux fonctionnent, mais l'incohérence peut créer de la confusion lors de la maintenance.

### 6. Comptage automatique `.exo` / `.corr` non fiable — RECTIFICATIF

**Gravité : HAUTE (Seconde) / BASSE (autres sections)**

**RECTIFICATIF 2026-03-19** : L'inventaire automatique du 2026-03-16 (basé sur le comptage des classes CSS `.exo` et `.corr`) était **massivement erroné**. Le comptage CSS comptait les sous-questions, items QCM, `<div class="corr">` imbriquées et `<details class="corr-wrap">` comme des éléments séparés.

**Méthodologie corrigée (3e comptage, 2026-03-19)** : comptage exact des blocs conteneurs `.exo` (exercices.html) et `.partie` (ds.html) vs les blocs `.corr`, fichier par fichier.

#### Seconde — Vérification détaillée (3e comptage, 2026-03-19)

**Exercices (exercices.html)** :

| Section | `.exo` | `.corr` | Manquant | Couverture |
|---|---|---|---|---|
| Maths Seconde | 191 | 79 | **112** | **41%** |
| PC Seconde | 199 | 159 | **40** | **80%** |

**DS (ds.html)** :

| Section | `.partie` | `.corr` | Couverture |
|---|---|---|---|
| Maths Seconde | 124 | 124 | **100%** ✓ |
| PC Seconde | 97 | 97 | **100%** ✓ |

**Détail exercices Maths Seconde** :

| Chapitre | `.exo` | `.corr` | Manquant | Statut |
|---|---|---|---|---|
| ch01 | 13 | 12 | 1 | Quasi complet |
| **ch02** | **11** | **0** | **11** | **Aucune correction** |
| ch03 | 14 | 13 | 1 | Quasi complet |
| **ch04** | **13** | **0** | **13** | **Aucune correction** |
| **ch05** | **12** | **0** | **12** | **Aucune correction** |
| **ch06** | **12** | **0** | **12** | **Aucune correction** |
| **ch07** | **15** | **0** | **15** | **Aucune correction** |
| **ch08** | **14** | **0** | **14** | **Aucune correction** |
| ch09 | 15 | 10 | 5 | Partiel |
| **ch10** | **14** | **0** | **14** | **Aucune correction** |
| ch11 | 15 | 10 | 5 | Partiel |
| ch12 | 15 | 14 | 1 | Quasi complet |
| ch13 | 14 | 10 | 4 | Partiel |
| ch14 | 14 | 10 | 4 | Partiel |

**7 chapitres maths sans aucune correction** : ch02, ch04, ch05, ch06, ch07, ch08, ch10

**Détail exercices PC Seconde** :

| Chapitre | `.exo` | `.corr` | Manquant | Statut |
|---|---|---|---|---|
| ch01–ch06 | 83 | 83 | 0 | Complet ✓ |
| **ch07** | **29** | **25** | **4** | Partiel |
| ch08–ch09 | 26 | 26 | 0 | Complet ✓ |
| **ch10** | **12** | **0** | **12** | **Aucune correction** |
| **ch11** | **12** | **0** | **12** | **Aucune correction** |
| ch12–ch13 | 25 | 25 | 0 | Complet ✓ |
| **ch14** | **12** | **0** | **12** | **Aucune correction** |

**3 chapitres PC sans aucune correction** : ch10, ch11, ch14

**Conclusion Seconde** : **152 corrections d'exercices manquantes** (112 maths + 40 PC). Les DS sont intégralement corrigés (100%).

#### Autres sections — Audit manuel (2026-03-19)

| Section | Exercices (exo) | DS | Total | Corrigés | Couverture | Stubs |
|---|---|---|---|---|---|---|
| Maths Première | 100 | 19 | 119 | 119 | **100%** | 0 |
| Maths Terminale | 171 | 78 | 249 | 249 | **100%** | 0 |
| PC Première ICCER | 96 | 79 | 175 | 175 | **100%** | 0 |
| PC Première ERA | 99 | 99 | 198 | 198 | **100%** | 0 |
| PC Terminale ICCER | 126 | 70 | 196 | 196 | **100%** | 0 |
| PC Terminale ERA | 96 | ~40 | ~136 | ~136 | **100%** | 0 |
| Maths BTS | 113 | 0 | 113 | 113 | **100%** | **29** |

#### Détail Maths Seconde — 191 exercices, 79 corrigés (41%)

| Chapitre | Titre | Exercices | Corrigés | Manquants |
|---|---|---|---|---|
| ch01 | Proportionnalité et pourcentages | 13 | 12 | 1 |
| ch02 | Statistiques à une variable | 11 | 0 | 11 |
| ch03 | Indicateurs statistiques | 14 | 13 | 1 |
| ch04 | Probabilités et fluctuation des fréquences | 13 | 0 | 13 |
| ch05 | Équations du premier degré | 12 | 0 | 12 |
| ch06 | Inéquations du premier degré | 12 | 0 | 12 |
| ch07 | Notion de fonction | 15 | 0 | 15 |
| ch08 | Fonction linéaire et proportionnalité | 14 | 0 | 14 |
| ch09 | Fonction affine | 15 | 10 | 5 |
| ch10 | Fonction carré et variations | 14 | 0 | 14 |
| ch11 | Figures planes : périmètres et aires | 15 | 10 | 5 |
| ch12 | Théorème de Pythagore et réciproque | 15 | 14 | 1 |
| ch13 | Théorème de Thalès dans le triangle | 14 | 10 | 4 |
| ch14 | Solides, volumes et agrandissement | 14 | 10 | 4 |

#### Physique-Chimie Seconde — 199 exercices, 159 corrigés (80%)

| Chapitre | Titre | Exercices | Corrigés | Manquants |
|---|---|---|---|---|
| ch01 | Sécurité en laboratoire et en atelier | 12 | 12 | 0 |
| ch02 | Grandeurs électriques et circuits | 12 | 12 | 0 |
| ch03 | Loi d'Ohm et caractéristiques d'un dipôle | 13 | 13 | 0 |
| ch04 | Signaux électriques alternatifs | 13 | 13 | 0 |
| ch05 | Mouvement et trajectoire | 20 | 20 | 0 |
| ch06 | Forces et équilibre | 13 | 13 | 0 |
| ch07 | Structure de la matière | 25 (+4 sims) | 25 | 0 |
| ch08 | Solutions chimiques et concentration | 13 | 13 | 0 |
| ch09 | Caractéristiques d'un son | 13 | 13 | 0 |
| ch10 | Température et capteurs thermiques | 12 | 12 | 0 |
| ch11 | Transferts thermiques | 12 | 12 | 0 |
| ch12 | Changements d'état | 12 | 12 | 0 |
| ch13 | Réflexion et réfraction | 13 | 13 | 0 |
| ch14 | Lumière, couleurs et photodétecteurs | 12 | 12 | 0 |

#### Maths Première — 100 exercices + 19 DS, tous corrigés (100%)

| Chapitre | Titre | Exercices | DS | Corrigés |
|---|---|---|---|---|
| ch01 | Statistique à deux variables | 12 | 2 | 14 |
| ch02 | Probabilités | 11 | 2 | 13 |
| ch03 | Suites numériques | 11 | 2 | 13 |
| ch04 | Résolution graphique d'équations | 9 | 2 | 11 |
| ch05 | Fonctions polynômes de degré 2 | 9 | 3 | 12 |
| ch06 | Fonction dérivée et variations | 12 | 2 | 14 |
| ch07 | Géométrie dans l'espace | 12 | 2 | 14 |
| ch08 | Vecteurs du plan | 9 | 2 | 11 |
| ch09 | Trigonométrie | 15 | 2 | 17 |

#### Maths Terminale — 171 exercices + 78 DS, tous corrigés (100%)

| Chapitre | Titre | Exercices | DS | Corrigés |
|---|---|---|---|---|
| ch01 | Statistiques à deux variables | 15 | 6 | 21 |
| ch02 | Probabilités | 17 | 14 | 31 |
| ch03 | Suites géométriques | 15 | 6 | 21 |
| ch04 | Fonctions polynômes de degré 3 | 20 | 6 | 26 |
| ch05 | Fonctions exp. et log décimal | 15 | 6 | 21 |
| ch06 | Vecteurs | 15 | 6 | 21 |
| ch07 | Trigonométrie | 15 | 7 | 22 |
| ch08 | Calcul intégral | 15 | 7 | 22 |
| ch09 | Fonctions ln et exponentielle | 15 | 6 | 21 |
| ch10 | Nombres complexes | 15 | 7 | 22 |
| ch11 | Produit scalaire | 14 | 7 | 21 |

#### PC Première ICCER — 96 exercices + 79 DS, tous corrigés (100%)

| Chapitre | Titre | Exercices | DS |
|---|---|---|---|
| ch01 | Énergie et puissance électrique | 10 | 7 |
| ch02 | Transport de l'énergie électrique | 10 | 6 |
| ch03 | Combustion du carbone et des hydrocarbures | 10 | 6 |
| ch04 | Les trois modes de transfert thermique | 9 | 8 |
| ch05 | Vitesse et accélération | 10 | 8 |
| ch06 | Équilibre d'un solide en rotation | 10 | 8 |
| ch07 | Pression et force pressante | 10 | 9 |
| ch08 | La force d'Archimède | 9 | 9 |
| ch09 | Solutions aqueuses et concentration | 9 | 9 |
| ch10 | Ondes électromagnétiques | 9 | 9 |

#### PC Terminale ICCER — 240 exercices + 70 DS, tous corrigés (100%) *(mis à jour 2026-03-22)*

| Chapitre | Titre | Exercices | DS |
|---|---|---|---|
| ch01 | Évaluer la puissance consommée | 30 | 8 |
| ch02 | Du courant alternatif au courant continu | 30 | 9 |
| ch03 | Énergie mécanique et moteur électrique | 31 | 8 |
| ch04 | Rayonnement thermique et effet de serre | 30 | 9 |
| ch05 | Caractériser la pression dans un fluide | 30 | 9 |
| ch06 | Transport de masse et volume par un fluide | 30 | 9 |
| ch07 | Oxydoréduction et protection des métaux | 30 | 9 |
| ch08 | Signal sonore | 30 | 9 |

#### PC Terminale ERA — 240 exercices + ~40 DS, tous corrigés (100%) *(mis à jour 2026-03-22)*

| Chapitre | Titre | Exercices | DS |
|---|---|---|---|
| ch01 | Transporter l'énergie électrique | 30 | ~5 |
| ch02 | Stocker l'énergie électrochimique | 30 | ~5 |
| ch03 | Rayonnement thermique et effet de serre | 30 | ~5 |
| ch04 | Vitesse et accélération | 30 | ~5 |
| ch05 | Oxydoréduction et protection des métaux | 30 | ~5 |
| ch06 | Choisir une source lumineuse | 30 | ~5 |
| ch07 | Transmettre l'information | 30 | ~5 |
| ch08 | Atténuer une onde sonore | 30 | ~5 |

#### Maths BTS — 113 exercices corrigés + 29 stubs

| Chapitre | Titre | Exercices | Statut |
|---|---|---|---|
| ch01 | Suites numériques | 17 | **Complet** (DS stub) |
| ch02 | Fonctions d'une variable réelle | 21 | **Complet** (DS stub) |
| ch03 | Fonctions pour le traitement du signal | 0 | **STUB** |
| ch04 | Calcul intégral | 15 | **Complet** (DS stub) |
| ch05 | Équations différentielles | 14 | **Complet** (DS stub) |
| ch06 | Séries de Fourier | 0 | **STUB** |
| ch07 | Transformée de Laplace | 0 | **STUB** |
| ch08 | Probabilités 1 | 18 | **Complet** (DS stub) |
| ch09 | Probabilités 2 | 0 | **STUB** |
| ch10 | Statistique descriptive | 0 | **STUB** |
| ch11 | Statistique inférentielle | 0 | **STUB** |
| ch12 | Nombres complexes | 14 | **Complet** (DS stub) |
| ch13 | Configurations géométriques | 14 | **Complet** (DS stub) |
| ch14 | Modélisation géométrique | 0 | **STUB** |
| ch15 | Calcul vectoriel | 0 | **STUB** |
| ch16 | Matrices et systèmes linéaires | 0 | **STUB** |
| ch17 | Calcul et algorithmique | 0 | **STUB** |
| ch18 | Fiabilité | 0 | **STUB** |

---

### ~~8. activite.html manquant dans tous les chapitres de Maths Seconde~~ — RÉSOLU (2026-03-26)

**~~Gravité : MOYENNE~~** → **RÉSOLU**

~~Aucun des 14 chapitres de `maths/seconde/` ne possède de fichier `activite.html`.~~

**Rectificatif 2026-03-26** : Les 14 fichiers `activite.html` existent et sont complets (170–360 lignes chacun). Présents depuis 2026-03-22, non détectés lors de l'audit du 2026-03-25. Simulations toujours absentes de 12 chapitres sur 14 (seuls ch05 et ch06 en ont une).

**Chapitres avec simulation manquante** : ch07, ch08, ch09, ch10 (fonctions) bénéficieraient particulièrement d'outils de visualisation interactive (tracé interactif des paramètres a et b).

---

### 9. Approfondissement insuffisant en statistiques/probabilités Seconde (2026-03-25)

**Gravité : HAUTE**

Les chapitres ch02, ch03, ch04 ont un nombre de blocs `diff-appro` très inférieur aux autres chapitres et aux attentes pour des élèves en poursuite BTS :

| Chapitre | Blocs appro | Objectif | Écart |
|---|---|---|---|
| ch02 (Statistiques à une variable) | 4 | 10-12 | **−6 à −8** |
| ch03 (Indicateurs statistiques) | 3 | 10-12 | **−7 à −9** |
| ch04 (Probabilités) | 7 | 10-12 | **−3 à −5** |

Les statistiques et probabilités font partie des thèmes clés du programme BTS. Un élève de Seconde en poursuite manque de matière d'approfondissement sur ces notions fondamentales.

---

### 7. Problèmes structurels identifiés en Seconde (2026-03-19)

**Gravité : MOYENNE**

#### a) Numérotation dupliquée des exercices
Dans la plupart des chapitres, les exercices Socle et Standard partagent les mêmes numéros (Ex 4, 5, 6). En mode "Tout voir" (prof), deux exercices différents portent le même numéro. Chapitres propres : maths ch05 (numérotation séquentielle), maths ch07 (S1/S2/S3 pour Socle), PC ch07 (numérotation continue 1-25).

#### b) Mécanisme de correction incohérent
Deux systèmes coexistent, parfois dans un même fichier :
- `<button class="bc">` + `<div class="corr">` (toggle JS) — maths ch01, ch03, ch09, ch11-ch14 ; PC ch08-ch09, ch12-ch13
- `<details class="corr-wrap">` (HTML natif) — maths ch02, ch04-ch08, ch10 ; PC ch10-ch11, ch14
- Mixte (Socle en `<details>`, Standard/Appro en `button.bc`) : maths ch09, ch11, ch13, ch14

#### c) CSS inline redéfini en violation des règles
De nombreux fichiers `exercices.html` redéfinissent des classes déjà présentes dans `styles.css` : `.corr-body`, `.corr-wrap`, `.methode`, `.attention`, `.enonce`, `.zone-rep`, `.niveau-1/2/3/4`, `.context-tag`, `.etape`, `.guide`, etc. Particulièrement extensif en maths ch10, ch13, ch14 et dans la plupart des fichiers PC.

#### d) Liens retour incorrects
- `maths/seconde/ch11/exercices.html` et `maths/seconde/ch12/exercices.html` : le lien `<a class="nb">` pointe vers `../../../index.html` au lieu de `../../../maths-2nde-mama.html`.

#### e) Code mort
- `physique-chimie/seconde/ch11/exercices.html` : fonction `toggle()` définie (ligne ~690) mais jamais appelée (toutes les corrections utilisent `<details>`).

#### f) Simulations embarquées dans les exercices
- `physique-chimie/seconde/ch07/exercices.html` contient 4 simulations interactives (modèle de Bohr, formation d'ions, quiz notation symbolique, formation de molécules) directement dans la page exercices au lieu du dossier `/simulations/`.

---

## Exercices a ameliorer en priorite

| Priorité | Fichier | Problème | Action recommandée |
|---|---|---|---|
| ~~**P1**~~ | ~~`maths/premiere/ch05/exercices.html`~~ | ~~Stub vide~~ | **RÉSOLU** — 9 exercices complets (2026-03-19) |
| ~~**P1**~~ | ~~`maths/premiere/ch09/exercices.html`~~ | ~~Stub vide~~ | **RÉSOLU** — 15 exercices complets (2026-03-19) |
| **P1** | `maths/bts/` — 11 chapitres stubs | exercices.html vides | Créer le contenu (ch03, ch06, ch07, ch09-ch11, ch14-ch18) |
| **P1** | `maths/bts/` — 18 DS stubs | ds.html tous vides | Créer le contenu pour tous les chapitres |
| **P2** | `maths/terminale/ch11/exercices.html` | Contenu potentiellement hors programme | Vérifier avec le BO ; retirer ou déplacer en appro les questions sur équation cartésienne/vecteur normal |
| **P2** | `maths/premiere/ch01-ch08` | Différenciation absente | Ajouter les tags diff-socle/standard/appro (seul ch09 utilise diff.js) |
| ~~**P3**~~ | ~~`maths/seconde/ch07/exercices.html` Ex.12~~ | ~~Label « type BTS » potentiellement décourageant~~ | **RÉSOLU 2026-03-26** — remplacé par « Approfondissement » |
| **P3** | `physique-chimie/terminale-era/ch04/exercices.html` | Contexte ERA faible | Ajouter un exercice contextualisé menuiserie/agencement |
| **P3** | `physique-chimie/premiere-iccer/ch10/exercices.html` | Lien ICCER ténu | Ajouter un exercice lié aux ondes dans le domaine thermique (ex : thermographie infrarouge) |

---

## Corrections realisees

- **2026-03-16** : Ajout de diff.js dans les 18 fichiers exercices.html et ds.html de maths/premiere (ch01-ch09)
- **2026-03-16** : Inventaire complet `.exo` vs `.corr` réalisé — 3 479 exercices, 1 433 corrections, 41.2% couverture globale
- **2026-03-17** : Corrige l'erreur numérique dans maths/terminale/ch02/exercices.html Ex 12 (0,8473 → 0,84778 et valeurs dérivées)
- **2026-03-17** : Corrige les fautes d'accord « encrassés » → « encrassé » dans maths/terminale/ch02/exercices.html Ex 8
- **2026-03-17** : Ajoute les tags de différenciation (tag-socle/tag-standard/tag-appro) dans maths/terminale/ch02/ds.html
- **2026-03-17** : Harmonise l'indentation des arbres de probabilités (NBSP → &emsp;) dans exercices.html et ds.html de ch02
- **2026-03-18** : Créé `maths/terminale/ch02/qcm.html` — QCM différencié (3×15 questions socle/standard/appro, auto-corrigé, feedback)
- **2026-03-18** : Créé `maths/terminale/ch02/interro.html` — Interro différenciée (3×5 questions socle/standard/appro, barème, corrections)
- **2026-03-18** : Créé 46 QCMs différenciés (3×15 questions) : maths/seconde (14/14), maths/premiere (9/9), maths/terminale (10/11, ch02 existant), physique-chimie/seconde (13/14, ch07 existant). Total : 48/84 QCMs (57%)
- **2026-03-19** : **RECTIFICATIF — AUDIT MANUEL COMPLET**
  - Audit chapitre par chapitre de l'intégralité du site (Seconde + Première + Terminale + BTS)
  - maths/premiere/ch05 et ch09 ne sont PAS des stubs — ils sont complets (9 et 15 exercices)
  - Seuls vrais stubs : 29 fichiers BTS (11 exercices.html + 18 ds.html)
  - Identification de problèmes structurels : numérotation, mécanismes de correction, CSS inline, liens retour
- **2026-03-19** : Bilan Seconde — 28/28 interro.html créées (14 maths + 14 PC), toutes différenciées avec diff.js. Seconde 100% complète sur les 6 types de pages
- **2026-03-19** : 3e vérification détaillée des corrections Seconde — comptage exact par fichier. Exercices : maths 41% (79/191), PC 80% (159/199). DS : 100% pour les deux. **152 corrections d'exercices manquantes** (112 maths + 40 PC)
- **2026-03-22** : **Augmentation massive des exercices PC Terminale** — 16 chapitres augmentés à 30 exercices chacun :
  - PC Terminale ICCER : 126 → 240 exercices (ch01 13→30, ch02 16→30, ch03 21→31, ch04 14→30, ch05 16→30, ch06 14→30, ch07 18→30, ch08 14→30)
  - PC Terminale ERA : 96 → 240 exercices (tous les 8 chapitres passés de ~12 à 30)
  - Tous différenciés (socle/standard/appro) avec corrections complètes
  - Contextes professionnels ICCER (chauffagiste, CVC, PAC, solaire) et ERA (menuisier, agenceur, ébéniste)
- **2026-03-22** : 84/84 interro.html complètes (Bac Pro). Ajout d'un Sujet B à chaque interro (252 sujets B, ~1 260 nouvelles questions avec corrections)
- **2026-03-25** : Audit exhaustif Maths Seconde — vérification directe des 14 fichiers exercices.html. État réel : 518 exercices, **100% corrigés** (les audits précédents étaient périmés ou inexacts). Révision note : 4.5/5. Problèmes résolus depuis 2026-03-22 : numérotation séquentielle harmonisée, liens retour ch11/ch12 corrigés. Problèmes restants : approfondissement insuffisant ch02 (4), ch03 (3), ch04 (7) ; 0/14 activite.html ; simulations absentes ch07-ch10
- **2026-03-26** : Rectificatif — les 14 `activite.html` de maths/seconde existent et sont complets (170–360 lignes chacun) ; l'audit du 25 mars les avait incorrectement signalés comme absents
- **2026-03-26** : Nettoyage CSS inline exercices.html maths/seconde — suppression des redéfinitions de `.methode`/`.methode-box`/`.cell-blank` dans ch06, ch09, ch10, ch13, ch14 ; remplacement par `.meth` (styles.css) ; amélioration de `.cell-blank` dans styles.css (fond jaune, gras, couleur ambrée — harmonise les variantes inline)
- **2026-03-26** : Correction étiquettes « type BTS » dans ch07/exercices.html (Ex.34 et Ex.35 appro) → remplacé par « Approfondissement »

---

## Ameliorations restantes

### Priorité haute
- [x] ~~Compléter maths/premiere/ch05/exercices.html (polynômes degré 2)~~ — **déjà complet** (9 exercices, rectifié 2026-03-19)
- [x] ~~Compléter maths/premiere/ch09/exercices.html (trigonométrie)~~ — **déjà complet** (15 exercices, rectifié 2026-03-19)
- [x] Ajouter la différenciation (diff.js) dans les 18 fichiers de maths/premiere (2026-03-16)
- [x] Réaliser un inventaire complet : nombre de `.exo` vs `.corr` sur chaque page (2026-03-16 — comptage CSS, **rectifié 2026-03-19**)
- [x] Auditer manuellement les corrections de Maths Seconde — **100% corrigés** (2026-03-19)
- [x] Auditer manuellement les corrections de PC Seconde — **100% corrigés** (2026-03-19)
- [x] Auditer manuellement les corrections de Maths Première — **100% corrigés** (100 exo + 19 DS, 2026-03-19)
- [x] Auditer manuellement les corrections de Maths Terminale — **100% corrigés** (171 exo + 78 DS, 2026-03-19)
- [x] Auditer manuellement les corrections de PC Première ICCER — **100% corrigés** (96 exo + 79 DS, 2026-03-19)
- [x] Auditer manuellement les corrections de PC Terminale ICCER — **100% corrigés** (126 exo + 70 DS, 2026-03-19)
- [x] Auditer manuellement les corrections de PC Terminale ERA — **100% corrigés** (96 exo + ~40 DS, 2026-03-19)
- [x] Auditer manuellement les corrections de Maths BTS — **113 exo corrigés + 29 stubs** (2026-03-19)
- [ ] Compléter les 11 exercices.html stubs BTS (ch03, ch06, ch07, ch09-ch11, ch14-ch18)
- [ ] Compléter les 18 ds.html stubs BTS (tous les chapitres)

### Priorité haute (uniformisation 2026-03-18)
- [ ] Créer les 36 `qcm.html` restants (PC 1ere ICCER 10, PC 1ere ERA 10, PC Tle ICCER 8, PC Tle ERA 8) — 48/84 faits
- [x] ~~Créer les 54 `interro.html` restants~~ — **84/84 complet** (rectifié 2026-03-22)
- [x] Ajouter un Sujet B à chaque interro.html (84 fichiers, 252 sujets B, ~1 260 questions) — **complet 2026-03-22**
- [x] ~~Créer les 7 `exercices.html` manquants (PC terminale)~~ — **déjà complets** (rectifié 2026-03-19)
- [x] ~~Créer les 7 `ds.html` manquants (PC terminale)~~ — **déjà complets** (rectifié 2026-03-19)

### Priorité moyenne
- [ ] Vérifier la conformité au programme de maths/terminale/ch11 (produit scalaire)
- [ ] Systématiser la différenciation en maths/terminale (tags diff-*)
- [ ] Vérifier la présence de boutons `.bc` pour chaque bloc `.corr`
- [ ] Auditer les DS : barème, durée, couverture des capacités

### Priorité haute (Maths Seconde, 2026-03-25)
- [ ] Renforcer l'approfondissement de ch02 (4→10 blocs) — statistiques à une variable pour BTS
- [ ] Renforcer l'approfondissement de ch03 (3→10 blocs) — indicateurs statistiques pour BTS
- [ ] Renforcer l'approfondissement de ch04 (7→10 blocs) — probabilités pour BTS

### Priorité moyenne (Maths Seconde, 2026-03-25)
- [x] ~~Créer les 14 `activite.html` manquants~~ — **14/14 présents** (rectifié 2026-03-26)
- [ ] Ajouter simulation.html pour les chapitres fonctions (ch07, ch08, ch09, ch10) — tracé interactif
- [x] ~~Remplacer le label « type BTS » → « Approfondissement » dans ch07/exercices.html~~ — **RÉSOLU 2026-03-26**
- [x] ~~Nettoyer le CSS inline redéfini : `.methode` dans ch06, ch09, ch10 (utiliser `.meth` de styles.css)~~ — **RÉSOLU 2026-03-26** (ch06, ch09, ch10, ch13, ch14)

### Priorité moyenne (structurel Seconde, 2026-03-19)
- [x] ~~Harmoniser la numérotation des exercices~~ — **RÉSOLU 2026-03-22** (numérotation séquentielle sur tous les chapitres)
- [x] ~~Nettoyer le CSS inline redéfini dans les fichiers exercices.html de Seconde (centraliser dans `styles.css`)~~ — **RÉSOLU 2026-03-26** (`.methode`/`.methode-box`/`.cell-blank` dans ch06, ch09, ch10, ch13, ch14)
- [x] ~~Corriger les liens retour dans maths/seconde/ch11 et ch12~~ — **RÉSOLU** (vérifié 2026-03-25, liens corrects)
- [ ] Supprimer la fonction `toggle()` morte dans physique-chimie/seconde/ch11/exercices.html

### Priorité basse
- [ ] Compléter les 29 stubs BTS (11 exercices.html : ch03, ch06, ch07, ch09-ch11, ch14-ch18 + 18 ds.html : tous)
- [ ] Harmoniser le mécanisme de correction (choisir entre `<details>` et `.bc`) sur tout le site
- [ ] Renommer « type BTS » → « Approfondissement » dans maths/seconde/ch07
- [ ] Renforcer les contextes ERA dans PC terminale-era ch04
- [ ] Ajouter un exercice thermographie infrarouge dans PC premiere-iccer ch10
- [ ] Déplacer les 4 simulations de PC/seconde/ch07/exercices.html vers `/simulations/`

---

## Synthese

**Note globale du site : 4.6/5** *(rectifié 2026-03-25 — Maths Seconde 4.5/5 après vérification directe : 518 exercices tous corrigés)*

| Section | Note | Statut |
|---|---|---|
| Maths Seconde | 4.5/5 | Très bon — 518 exercices 100% corrigés, différenciation systématique, DS exemplaires ; approfondissement ch02-ch04 insuffisant, 0/14 activite.html, simulations à créer pour ch07-ch10 |
| Maths Première | 4/5 | Complet, différenciation formelle à généraliser (seul ch09 utilise diff.js) |
| Maths Terminale | 4.5/5 | Très bon, différenciation systématique, ch11 à vérifier (programme) |
| PC Seconde | 4/5 | Bon, différenciation à systématiser |
| PC Première ICCER | 4.5/5 | Très bon, contextualisation excellente |
| PC Première ERA | 4.5/5 | Très bon, contextualisation excellente |
| PC Terminale ICCER | 5/5 | Exemplaire — 240 exercices différenciés (~10 socle, ~12 standard, ~8 appro par chapitre), 70 DS |
| PC Terminale ERA | 5/5 | Exemplaire — 240 exercices différenciés (~8 socle, ~12 standard, ~10 appro par chapitre), ~40 DS |
| Maths BTS | 2/5 | 7 chapitres complets, 11 stubs, tous les DS manquants |

**Forces du site** :
- **100% de couverture en corrections** sur toutes les sections Bac Pro (Seconde, Première, Terminale).
- ~1 860 exercices et DS tous corrigés avec contenu substantiel.
- La section maths seconde est un modèle de qualité : différenciation systématique, corrections complètes, contextes pro variés, éléments interactifs.
- Les sections physique-chimie première (ICCER et ERA) ont une contextualisation filière remarquable.
- Les DS sont globalement bien structurés avec compétences (APP/ANA/REA/VAL/COM) et barèmes.

**Priorités d'amélioration** :
1. **Urgence** : compléter les 29 stubs BTS (11 exercices.html + 18 ds.html).
2. **Important** : généraliser la différenciation formelle en maths première (ch01-ch08) et vérifier ch11 terminale.
3. **Souhaitable** : harmoniser les mécanismes de correction et la numérotation des exercices.

---

## Nouvelles ressources d'évaluation (2026-03-18)

**Plan d'uniformisation** : chaque chapitre proposera 4 types de ressources d'évaluation (au lieu de 2) :

| Ressource | Existant | Cible | À créer | Différenciation |
|---|---|---|---|---|
| `exercices.html` | 77 | 84 | 7 | Oui (socle/standard/appro) |
| `ds.html` | 77 | 84 | 7 | Oui (socle/standard/appro) |
| `qcm.html` | 48 | 84 | 36 | Oui (3×15 questions) |
| `interro.html` | 84 | 84 | 0 | Oui (3×5-8 questions, 2 sujets A/B) |

**Modèle existant QCM** : `physique-chimie/seconde/ch07/qcm.html` — QCM interactif auto-corrigé, feedback instantané, score.
**Modèle existant interro** : `maths/terminale/ch04/interro.html` — interrogation écrite, corrections, différenciée.

**Bilan Seconde (2026-03-19)** : la Seconde est la **première section 100% complète** du site avec les 6 types de pages (lecon, exercices, ds, fiche, qcm, interro) sur les 28 chapitres. Différenciation systématique (56 fichiers exercices/ds + 28 interro avec diff.js). Total : 170 fichiers HTML en Seconde.

**Specs détaillées** : voir `prompts/prompt-qcm-interro.md`.

---

## Mises à jour avril 2026

### Audits scientifiques exhaustifs — 5 sections PC + Maths CAP (2026-04-15)

| Section | Chapitres | Fichiers (lecon + exo + qcm + interro + ds) | Erreurs scientifiques | Corrections |
|---|---|---|---|---|
| Maths CAP | 7 | 56 | 0 | 0 typo (100% conforme) |
| PC CAP | 7 | 56 | 0 | **31 typos QCM corrigés** |
| PC 1ère ICCER | 10 | 80 | 0 | 2 typos « À retenir » |
| PC 1ère ERA | 10 | 80 | 0 | 9 typos accents |
| PC Term ICCER | 8 | 64 | 0 | 8 typos + encoding ch06 |
| PC Term ERA | 8 | 65 | 0 | 9 typos |
| **Total** | **50** | **401** | **0** | **59 corrections** |

**Méthode** : relecture intégrale Opus de chaque exercice + correction, vérification des unités, formules, schémas SVG, protocoles ; recalculs pas à pas pour les exercices numériques.

**Verdict** : aucune erreur scientifique détectée sur les 5 sections PC + Maths CAP. Les corrections concernent uniquement la typographie/encoding.

### Audit Terminale Maths — corrections leçons (2026-04-15)

Audit ciblé sur les leçons (chapitres signalés en jaune) :
- **ch03** : correction de la formule de la somme géométrique (signe / placement de l'exposant)
- **ch04** : correction du polynôme de degré 3 (énoncé incohérent avec la résolution)
- **ch09** : remplacement du symbole `ℜ` (partie réelle) par `ℝ` (ensemble des réels) — confusion typographique
- **ch10** : accents corrigés
- **ch11** : accents corrigés

### Réparation structure HTML (2026-04-30) — 17 fichiers

**Pattern identifié** : `<div class="c">` non fermé avant `</body>` (manquant `</div>`)

| Section | Fichiers concernés (commit 58c6c9e6) |
|---|---|
| PC 1ère ICCER | ch07/interro.html |
| PC 1ère ERA | ch02/interro.html |
| PC Term ICCER | ch02/interro.html |
| PC Term ERA | ch01/ds.html (1 close en trop retiré), ch03/ds.html, ch04/ds.html |
| Maths Seconde | ch01/exercices-capacites.html, ch05/exercices-capacites.html |
| Maths Première | ch08/exercices-capacites.html |
| Maths Terminale | ch04/exercices-capacites.html, ch04/interro.html (**3 closes manquants** — diff-socle/standard/appro), ch05/exercices-capacites.html, ch06/exercices-capacites.html, ch08/ds.html, ch10/ds.html, ch10/exercices-capacites.html, ch11/exercices-capacites.html |

**Total** : 6 PC + 11 Maths = 17 fichiers. Vérification : opens=closes sur les 17.

**Effet** : pages désormais structurellement saines, pas d'effet visuel mais correction nécessaire pour l'accessibilité et le rendu mobile.

### Page catalogue + index chapitre (2026-04-29)

- **138 pages `index.html`** créées (1 par chapitre) avec liens vers les 6 ressources (leçon, exos, DS, QCM, interro, fiche) + activités + simulations
- **Sommaires cliquables** dans 13 fichiers de section (ex : `maths-2nde-mama.html`, `pc-tle-iccer.html`)
- **`simulations.html`** régénérée : 82 simulations listées, 8 catégories, recherche client-side, filtres

### Objectifs pédagogiques injectés (2026-04-29)

- **544 pages de ressources** enrichies d'un encadré « Objectifs du chapitre » en haut de page (basé sur le programme officiel)
- Cohérence visuelle : même format sur leçon, exercices, DS, QCM, interro, fiche

### Bilan exercices avril 2026

| Indicateur | Avant avril | Après avril |
|---|---|---|
| Erreurs scientifiques détectées | non auditées | 0 sur 401 fichiers |
| Typos / encoding | non audités | 59 corrigés |
| Fichiers HTML structure cassée | 17 | 0 (réparés) |
| Pages avec « Objectifs » | partielles | 544 (uniformisées) |
| Pages index par chapitre | 0 | 138 |
| Catalogue simulations | obsolète | 82 sims (à jour) |

**Verdict global exercices** : aucune erreur scientifique sur 401 fichiers PC + Maths CAP audités. Structure HTML uniformisée. Couverture 100% lycée pro confirmée (98/98 chapitres).
