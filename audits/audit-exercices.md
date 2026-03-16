# Audit Pédagogique des Exercices

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-03-16 (session 5)
**Périmètre** : exercices.html et ds.html — 8 sections (maths seconde/première/terminale, physique-chimie seconde/première-iccer/première-era/terminale-iccer/terminale-era)
**Méthode** : échantillonnage de 2-3 fichiers exercices.html et 2-3 fichiers ds.html par section, lecture et analyse qualitative.

---

## Méthodologie

- **Fichiers échantillonnés** : ~30 fichiers (exercices.html et ds.html) répartis sur les 8 sections.
- **Critères évalués** : cohérence avec le chapitre, adaptation au niveau Bac Pro, progression de difficulté, diversité des contextes, cohérence filière (ICCER → chauffage/énergie, ERA → menuiserie/agencement), qualité des corrections, utilisation de la différenciation (socle/standard/appro).

---

## Analyse par section

### 1. Maths — Seconde

**Qualité globale : 5/5**

**Fichiers analysés** : ch01/exercices.html, ch07/exercices.html, ch14/exercices.html, ch01/ds.html, ch07/ds.html, ch14/ds.html

**Points forts** :
- Différenciation pédagogique complète et systématique (socle/standard/appro) sur tous les fichiers.
- Corrections présentes pour tous les exercices (`.corr` + bouton `.bc`).
- Progression de difficulté claire : Niveau 1 (bases) → Niveau 2 (guidé) → Niveau 3 (autonomie) → Niveau 4 (contexte pro).
- Contextes professionnels variés et pertinents : menuiserie (colle à bois, pose parquet, étagères), maintenance automobile, tuyauterie, béton.
- Éléments interactifs de qualité : graphiques Chart.js (ch01), graphes SVG (ch07), canvas interactif pour tracer des fonctions (ch07), QCM (ch14).
- DS très bien structurés avec barèmes, compétences (APP/ANA/REA/VAL/COM), et versions socle pré-remplies.

**Points faibles** :
- L'exercice 12 du ch07 est étiqueté « type BTS » — potentiellement trop ambitieux pour une seconde Bac Pro, même en approfondissement.

---

### 2. Maths — Première

**Qualité globale : 2/5**

**Fichiers analysés** : ch01/exercices.html, ch05/exercices.html, ch09/exercices.html, ch01/ds.html, ch05/ds.html

**Points forts** :
- ch01 (Statistique à deux variables) : contenu complet avec nuages de points Chart.js, contextes professionnels (ventes de bois, consommation électrique d'atelier).
- ch01/ds.html et ch05/ds.html : DS bien structurés avec compétences et barèmes.

**Points faibles** :
- **ch05/exercices.html et ch09/exercices.html sont des STUBS VIDES** (« Contenu à venir ») — c'est le problème majeur de cette section.
- L'absence de contenu sur les polynômes de degré 2 (ch05) et la trigonométrie (ch09) laisse deux chapitres fondamentaux sans exercices.
- Pour ch01, la différenciation est moins visible/systématique que dans la seconde.

---

### 3. Maths — Terminale

**Qualité globale : 3.5/5**

**Fichiers analysés** : ch01/exercices.html, ch06/exercices.html, ch11/exercices.html, ch01/ds.html, ch06/ds.html

**Points forts** :
- ch01 (Statistiques à deux variables) : contenu complet, contextes ICCER (consommation chauffage) et ERA (surface/coût menuisier, débit/perte charge installateur).
- ch06 (Vecteurs) : progression claire des coordonnées aux vecteurs égaux.
- DS bien structurés avec versions différenciées et contextes professionnels (chauffagiste pour socle, vecteurs guidés).

**Points faibles** :
- ch11 (Produit scalaire) : contenu avancé (identité de polarisation, équation cartésienne, vecteur normal, distance point-droite) — potentiellement trop difficile pour un Bac Pro, même en approfondissement.
- ch06 : pas de tags de différenciation visibles (diff-socle/diff-standard/diff-appro absents dans la structure), bien que le contenu soit progressif.
- Différenciation moins systématique qu'en seconde.

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

**Qualité globale : 4/5**

**Fichiers analysés** : ch01/exercices.html, ch04/exercices.html, ch08/exercices.html, ch01/ds.html

**Points forts** :
- ch01 (Puissances P, S, Q, cos φ) : contenu avancé mais approprié pour terminale ICCER — triangle des puissances, compensation, monophasé/triphasé. Contexte chaufferie.
- ch04 (Rayonnement thermique) : lois de Stefan-Boltzmann et Wien bien amenées, exercices socle avec tableaux de conversion de température pré-structurés.
- ch08 (Signal sonore) : formule de Sabine, atténuation, calculs dB — section formules complète et bien organisée.
- DS ch01 : radiateur en local technique, compétences identifiées.

**Points faibles** :
- Le niveau de formalisme mathématique (cos φ, puissance réactive) est élevé — les exercices socle doivent être particulièrement guidés pour rester accessibles.
- ch08 : la formule de Sabine et les calculs d'atténuation acoustique sont exigeants ; vérifier que le programme officiel les inclut bien à ce niveau.

---

### 8. Physique-Chimie — Terminale ERA

**Qualité globale : 4/5**

**Fichiers analysés** : ch01/exercices.html, ch04/exercices.html, ch08/exercices.html, ch01/ds.html

**Points forts** :
- ch01 (Transporter l'énergie électrique) : schéma SVG du réseau HT/MT/BT, transformateurs, pertes Joule, rendement — bon contenu pour ERA.
- ch04 (Vitesse et accélération) : graphe v(t) en SVG, MRU/MRUA, distance de freinage — contextes variés.
- ch08 (Atténuer une onde sonore) : diagramme SVG de paroi, tableau des niveaux sonores réglementaires, indice d'affaiblissement, loi de masse — excellent ancrage ERA (atelier, machines industrielles).
- DS ch01 : convoyeur triphasé, légende des compétences, bonne structure.

**Points faibles** :
- ch04 sur vitesse/accélération : le lien avec le métier ERA (menuiserie/agencement) est indirect — les contextes pourraient être plus spécifiques au domaine.

---

## Problemes identifies

### 1. Fichiers exercices vides (stubs)

**Gravité : CRITIQUE**

Maths première ch05 (Polynômes degré 2) et ch09 (Trigonométrie) sont des stubs « Contenu à venir ». Ce sont des chapitres fondamentaux du programme.

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

### 6. Corrections massivement incomplètes

**Gravité : CRITIQUE**

L'inventaire complet (2026-03-16) révèle un taux de couverture global de **41.2%** (1 433 `.corr` pour 3 479 `.exo`), soit **2 046 corrections manquantes**.

| Section | `.exo` | `.corr` | Écart | Couverture |
|---|---|---|---|---|
| Maths Seconde | 573 | 422 | 151 | 73.6% |
| Maths Première | 219 | 85 | 134 | 38.8% |
| Maths Terminale | 338 | 169 | 169 | 50.0% |
| Maths BTS | 330 | 115 | 215 | 34.8% |
| PC Seconde | 738 | 221 | 517 | 29.9% |
| PC Première ICCER | 294 | 96 | 198 | 32.7% |
| **PC Première ERA** | **99** | **99** | **0** | **100%** |
| PC Terminale ICCER | 504 | 126 | 378 | 25.0% |
| PC Terminale ERA | 384 | 96 | 288 | 25.0% |
| **TOTAL** | **3 479** | **1 433** | **2 046** | **41.2%** |

**Pires fichiers individuels (écart > 50) :**
- `physique-chimie/terminale-iccer/ch03/exercices.html` : 84 exo / 21 corr (écart 63)
- `physique-chimie/seconde/ch07/exercices.html` : 76 exo / 15 corr (écart 61)
- `physique-chimie/seconde/ch05/exercices.html` : 80 exo / 20 corr (écart 60)
- `physique-chimie/terminale-iccer/ch07/exercices.html` : 72 exo / 18 corr (écart 54)
- `maths/bts/ch01/exercices.html` : 68 exo / 17 corr (écart 51)

**Section exemplaire** : PC Première ERA (100% de couverture sur 10 chapitres).

**Anomalies** : maths/seconde/ch07 et ch08 ont plus de `.corr` que de `.exo` (structure HTML à vérifier).

---

## Exercices a ameliorer en priorite

| Priorité | Fichier | Problème | Action recommandée |
|---|---|---|---|
| **P1** | `maths/premiere/ch05/exercices.html` | Stub vide | Créer le contenu complet (polynômes degré 2) avec différenciation |
| **P1** | `maths/premiere/ch09/exercices.html` | Stub vide | Créer le contenu complet (trigonométrie) avec différenciation |
| **P2** | `maths/terminale/ch11/exercices.html` | Contenu potentiellement hors programme | Vérifier avec le BO ; retirer ou déplacer en appro les questions sur équation cartésienne/vecteur normal |
| **P2** | `maths/terminale/ch06/exercices.html` | Différenciation absente | Ajouter les tags diff-socle/standard/appro et diff.js |
| **P3** | `maths/seconde/ch07/exercices.html` Ex.12 | Label « type BTS » potentiellement décourageant | Remplacer par « Approfondissement » ou « Pour aller plus loin » |
| **P3** | `physique-chimie/terminale-era/ch04/exercices.html` | Contexte ERA faible | Ajouter un exercice contextualisé menuiserie/agencement |
| **P3** | `physique-chimie/premiere-iccer/ch10/exercices.html` | Lien ICCER ténu | Ajouter un exercice lié aux ondes dans le domaine thermique (ex : thermographie infrarouge) |

---

## Corrections realisees

- **2026-03-16** : Ajout de diff.js dans les 18 fichiers exercices.html et ds.html de maths/premiere (ch01-ch09)
- **2026-03-16** : Inventaire complet `.exo` vs `.corr` réalisé — 3 479 exercices, 1 433 corrections, 41.2% couverture globale

---

## Ameliorations restantes

### Priorité haute
- [ ] Compléter maths/premiere/ch05/exercices.html (polynômes degré 2)
- [ ] Compléter maths/premiere/ch09/exercices.html (trigonométrie)
- [x] Ajouter la différenciation (diff.js) dans les 18 fichiers de maths/premiere (2026-03-16)
- [x] Réaliser un inventaire complet : nombre de `.exo` vs `.corr` sur chaque page (2026-03-16 — 41.2% couverture)

### Priorité moyenne
- [ ] Vérifier la conformité au programme de maths/terminale/ch11 (produit scalaire)
- [ ] Systématiser la différenciation en maths/terminale (tags diff-*)
- [ ] Vérifier la présence de boutons `.bc` pour chaque bloc `.corr`
- [ ] Auditer les DS : barème, durée, couverture des capacités

### Priorité basse
- [ ] Compléter les 29 pages BTS stub avec du contenu réel
- [ ] Harmoniser le mécanisme de correction (choisir entre `<details>` et `.bc`)
- [ ] Renommer « type BTS » → « Approfondissement » dans maths/seconde/ch07
- [ ] Renforcer les contextes ERA dans PC terminale-era ch04
- [ ] Ajouter un exercice thermographie infrarouge dans PC premiere-iccer ch10
- [ ] Créer un script de comptage automatique `.exo` vs `.corr` pour le suivi

---

## Synthese

**Note globale du site : 3.8/5**

| Section | Note | Statut |
|---|---|---|
| Maths Seconde | 5/5 | Exemplaire — modèle à suivre |
| Maths Première | 2/5 | Lacunaire — 2 chapitres vides, pas de différenciation |
| Maths Terminale | 3.5/5 | Bon mais différenciation et programme à vérifier |
| PC Seconde | 4/5 | Bon, différenciation à systématiser |
| PC Première ICCER | 4.5/5 | Très bon, contextualisation excellente |
| PC Première ERA | 4.5/5 | Très bon, contextualisation excellente |
| PC Terminale ICCER | 4/5 | Bon, niveau exigeant mais adapté |
| PC Terminale ERA | 4/5 | Bon, quelques contextes à renforcer |

**Forces du site** :
- La section maths seconde est un modèle de qualité : différenciation systématique, corrections complètes, contextes pro variés, éléments interactifs (SVG, Canvas, Chart.js).
- Les sections physique-chimie première (ICCER et ERA) ont une contextualisation filière remarquable.
- Les DS sont globalement bien structurés avec compétences (APP/ANA/REA/VAL/COM) et barèmes.

**Priorités d'amélioration** :
1. **Urgence** : compléter les exercices de maths première (ch05 et ch09).
2. **Important** : généraliser la différenciation formelle à toutes les sections de première et terminale, en prenant maths seconde comme modèle.
3. **Souhaitable** : vérifier la conformité au programme de maths terminale ch11 et ajuster si nécessaire.
