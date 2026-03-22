# Audit Doublons & Uniformisation des ressources

**Date** : 2026-03-18
**Derniere mise a jour** : 2026-03-18
**Perimetre** : Uniformisation du schema de pages par chapitre (automatismes, QCM, interrogations, fiches)

---

## Resume executif

Le site compte **84 chapitres Bac Pro** (hors BTS). Chaque chapitre doit proposer un ensemble uniforme de ressources. L'audit a revele des incoherences : un doublon d'automatismes (corrige), des pages QCM et interro existantes mais isolees, et une couverture incomplete des types de ressources.

**Decision prise :** chaque chapitre doit a terme proposer **6 types de pages** :

| Page | Role | Existe |
|---|---|---|
| `lecon.html` | Cours (identique pour tous) | 84/84 |
| `exercices.html` | Exercices differencies (socle/standard/appro) | 77/84 |
| `ds.html` | Devoir surveille differencie (1h, 20 pts) | 77/84 |
| `qcm.html` | QCM interactif auto-corrige (15 questions, 15-20 min) | **1/84** |
| `interro.html` | Interrogation ecrite courte & diagnostique (10-15 min, 5-8 questions) | **1/84** |
| `fiche.html` | Fiche de revision / synthese | 57/84 |

---

## Problemes identifies (et corriges)

### 1. [CORRIGE] Doublon automatismes.html vs automatismes/index.html (gravite : HAUTE)

Deux pages servaient de point d'entree aux automatismes avec des approches differentes et des liens incoherents depuis le site.

**Correction :** `automatismes.html` (racine) supprime. Tous les liens unifies vers `automatismes/index.html`. Voir details dans la section "Corrections realisees".

### 2. [CORRIGE] Liens incoherents vers les automatismes (gravite : CRITIQUE)

`maths-term-erama.html` et `maths-term-iccer.html` pointaient vers les deux pages simultanement.

**Correction :** liens fusionnes en un seul vers `automatismes/index.html`.

---

## Problemes identifies (en cours)

### 3. `physique-chimie/seconde/ch07/qcm.html` — page orpheline (gravite : HAUTE)

Page QCM interactive de qualite (15 questions, auto-correction JS, feedback, score) mais **introuvable** par navigation. Le sommaire `pc-2nde-pro.html` ne liste que lecon/exercices/ds pour le ch07.

**Action :** ajouter le lien dans le sommaire + utiliser comme modele pour les 83 autres chapitres.

### 4. `maths/terminale/ch04/interro.html` — page non reliee au schema standard (gravite : MOYENNE)

Interrogation ecrite sur les polynomes de degre 3. Page de qualite, liee depuis les sommaires Terminale. Format a conserver et deployer sur les autres chapitres.

**Clarification :** cette page n'est **pas** consideree comme un doublon de ds.html. L'interro et le DS ont des roles complementaires :
- **Interro** = evaluation diagnostique courte (10-15 min), verification rapide des acquis de base
- **DS** = evaluation sommative complete (1h), differenciation socle/standard/appro

### 5. Couverture incomplete des types de ressources (gravite : HAUTE)

| Ressource | Maths 2nde (14) | Maths 1ere (9) | Maths Term (11) | PC 2nde (14) | PC 1ere-ICCER (10) | PC 1ere-ERA (10) | PC Term-ICCER (8) | PC Term-ERA (8) | Total |
|---|---|---|---|---|---|---|---|---|---|
| `lecon.html` | 14 | 9 | 11 | 14 | 10 | 10 | 8 | 8 | **84/84** |
| `exercices.html` | 14 | 9 | 11 | 14 | 10 | 10 | 5 | 4 | **77/84** |
| `ds.html` | 14 | 9 | 11 | 14 | 10 | 10 | 5 | 4 | **77/84** |
| `fiche.html` | 14 | 2 | 11 | 14 | 0 | 0 | 8 | 8 | **57/84** |
| `qcm.html` | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | **1/84** |
| `interro.html` | 14 | 9 | 11 | 14 | 10 | 10 | 8 | 8 | **84/84** |

**Pages manquantes a creer :**

| Type | Nombre a creer | Priorite |
|---|---|---|
| `qcm.html` | 83 | Haute |
| `interro.html` | 0 | ~~Haute~~ Terminé |
| `fiche.html` | 27 | Moyenne |
| `exercices.html` | 7 | Haute |
| `ds.html` | 7 | Haute |

### 6. CSS des QCM a centraliser (gravite : MOYENNE)

La page `qcm.html` existante contient 25 classes inline (`.qcm-header`, `.q-block`, `.options`, `.q-feedback`, `.score-box`, etc.). Avant de creer 83 autres QCM, ces classes doivent etre centralisees dans `styles.css`.

---

## Schema standard par chapitre

### Structure cible

```
subject/level/chNN/
├── lecon.html       Cours commun (pas de differenciation)
├── exercices.html   Exercices differencies (diff.js, socle/standard/appro)
├── ds.html          Devoir surveille differencie (1h, 20 pts, socle/standard/appro)
├── qcm.html         QCM interactif auto-corrige (15 questions, 15-20 min)
├── interro.html     Interrogation diagnostique (10-15 min, 5-8 questions rapides)
└── fiche.html       Fiche de revision / synthese
```

### Specifications `qcm.html`

| Dimension | Specification |
|---|---|
| **Format** | QCM interactif avec auto-correction JS |
| **Nombre de questions** | 15 par niveau (3 x 15 = 45 questions par chapitre) |
| **Duree** | 15-20 min par niveau |
| **Contenu** | Mix connaissances (definitions, vocabulaire, reconnaissance) + calculs rapides |
| **Feedback** | Immediat (correct/incorrect + explication) |
| **Score** | Calcule et affiche automatiquement |
| **Differenciation** | **Oui** — 3 series avec `diff.js` (socle/standard/appro) |
| **Impression** | Supportee (print.css) |
| **Modele existant** | `physique-chimie/seconde/ch07/qcm.html` (a adapter pour differenciation) |

**Differenciation QCM :**
- **Socle** : questions directes, vocabulaire simple, reconnaissance immediate, calculs elementaires
- **Standard** : questions classiques du programme, application de formules, interpretation de resultats
- **Approfondissement** : questions a raisonnement, croisement de notions, problemes ouverts, vocabulaire BTS

**Adaptation par matiere :**
- **Maths** : plus de calcul mental, reconnaissance de formules, lecture graphique, vrai/faux sur proprietes
- **Physique-Chimie** : plus de questions sur les unites, schemas, protocoles, vocabulaire scientifique, conversions

### Specifications `interro.html`

| Dimension | Specification |
|---|---|
| **Format** | Interrogation ecrite courte, imprimable |
| **Nombre de questions** | 5-8 par niveau (3 sujets differencies) |
| **Duree** | 10-15 min |
| **Objectif** | Diagnostic rapide des acquis |
| **Differenciation** | **Oui** — 3 sujets avec `diff.js` (socle/standard/appro) |
| **Corrections** | Oui (bouton "Voir la correction") |
| **Bareme** | 10-20 pts selon le chapitre |
| **Modele existant** | `maths/terminale/ch04/interro.html` |

**Differenciation interro :**
- **Socle** : exercices tres guides, calculs amorces, tableaux pre-remplis, questions de reconnaissance
- **Standard** : exercices du programme, consignes completes, redaction attendue
- **Approfondissement** : problemes plus ouverts, mise en equation autonome, questions type BTS

**Difference cle avec `ds.html` :**
- L'interro est **courte** (10-15 min, 5-8 questions) : verification rapide des acquis
- Le DS est **long** (1h, 4+ exercices) : evaluation sommative complete
- Les deux sont differencies socle/standard/appro avec diff.js

---

## Corrections realisees

- **2026-03-18** : Doublon automatismes corrige — `automatismes.html` (racine) supprime
- **2026-03-18** : Liens unifies dans 5 fichiers vers `automatismes/index.html`
- **2026-03-18** : Liens fusionnes (2→1) dans `maths-term-erama.html` et `maths-term-iccer.html`
- **2026-03-18** : Verification contenu — pages thematiques plus completes, aucune migration necessaire

---

## Ameliorations restantes

### Priorite critique
- [x] Unifier les liens automatismes (corrige 2026-03-18)
- [x] Supprimer le doublon `automatismes.html` (corrige 2026-03-18)

### Priorite haute — Uniformisation des ressources
- [ ] Centraliser les classes CSS QCM dans `styles.css` (prerequis avant creation en masse)
- [ ] Ajouter le lien `qcm.html` du ch07 PC dans le sommaire `pc-2nde-pro.html`
- [ ] Creer `qcm.html` pour les 83 chapitres manquants
- [x] ~~Creer `interro.html` pour les 83 chapitres manquants~~ — **84/84 complet** (2026-03-22, + Sujet B sur chaque fichier)
- [ ] Creer les 7 `exercices.html` manquants (PC terminale-iccer ch04-08, terminale-era ch05-08)
- [ ] Creer les 7 `ds.html` manquants (memes chapitres)
- [ ] Mettre a jour les sommaires pour lister qcm.html et interro.html pour chaque chapitre

### Priorite moyenne
- [ ] Creer les 27 `fiche.html` manquantes (maths/premiere 7, PC/premiere-iccer 10, PC/premiere-era 10)
- [ ] Ajouter l'optimisation impression aux pages thematiques automatismes

### Priorite basse
- [ ] Harmoniser le rendu MathJax (tex-mml-chtml vs tex-svg) sur toutes les pages
