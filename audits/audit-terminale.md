# Audit Terminale Bac Pro — Maths & Physique-Chimie

**Date** : 2026-03-22
**Derniere mise a jour** : 2026-03-22

Audit des 3 sections Terminale :
- Mathematiques Terminale (11 chapitres)
- Physique-Chimie Terminale ICCER / Groupement 1 (8 chapitres)
- Physique-Chimie Terminale ERA / Groupement 3 (8 chapitres)

---

## Resume executif

| Section | Chapitres | Fichiers presents | Couverture | Qualite globale |
|---|---|---|---|---|
| Maths Terminale | 11 | 66/77 (6/7 par ch.) | 85% | Tres bon |
| PC Terminale ICCER | 8 | 48/56 (6/7 par ch.) | 85% | Tres bon |
| PC Terminale ERA | 8 | 48/56 (6/7 par ch.) | 85% | Tres bon |
| **TOTAL** | **27** | **162/189** | **85%** | **Tres bon** |

**Fichier manquant partout** : `simulation.html` (0/27 chapitres — fichier optionnel)

---

## Couverture par fichier

### Mathematiques Terminale (11 chapitres)

| Ch | Titre | lecon | exercices | ds | fiche | qcm | interro | simulation |
|---|---|---|---|---|---|---|---|---|
| 01 | Statistiques a deux variables | OK | OK | OK | OK | OK | OK | — |
| 02 | Probabilites | OK | OK | OK | OK | OK | OK | — |
| 03 | Suites numeriques (suite geometrique) | OK | OK | OK | OK | OK | OK | — |
| 04 | Fonctions polynomes de degre 3 | OK | OK | OK | OK | OK | OK | — |
| 05 | Fonctions exponentielles et logarithme decimal | OK | OK | OK | OK | OK | OK | — |
| 06 | Vecteurs | OK | OK | OK | OK | OK | OK | — |
| 07 | Trigonometrie | OK | OK | OK | OK | OK | OK | — |
| 08 | Calcul integral | OK | OK | OK | OK | OK | OK | — |
| 09 | Fonctions ln et exponentielle | OK | OK | OK | OK | OK | OK | — |
| 10 | Nombres complexes | OK | OK | OK | OK | OK | OK | — |
| 11 | Produit scalaire | OK | OK | OK | OK | OK | OK | — |

**Bilan** : 66/66 fichiers de base presents (100%). 0 simulation.

### Physique-Chimie Terminale ICCER (8 chapitres)

| Ch | Titre | lecon | exercices | ds | fiche | qcm | interro | simulation |
|---|---|---|---|---|---|---|---|---|
| 01 | Puissance consommee | OK | OK | OK | OK | OK | OK | — |
| 02 | Courant alternatif / continu | OK | OK | OK | OK | OK | OK | — |
| 03 | Moteur electrique | OK | OK | OK | OK | OK | OK | — |
| 04 | Rayonnement thermique | OK | OK | OK | OK | OK | OK | — |
| 05 | Pression dans un fluide immobile | OK | OK | OK | OK | OK | OK | — |
| 06 | Transport par un fluide en mouvement | OK | OK | OK | OK | OK | OK | — |
| 07 | Oxydoreduction et corrosion | OK | OK | OK | OK | OK | OK | — |
| 08 | Signal sonore | OK | OK | OK | OK | OK | OK | — |

**Bilan** : 48/48 fichiers de base presents (100%). 0 simulation.

### Physique-Chimie Terminale ERA (8 chapitres)

| Ch | Titre | lecon | exercices | ds | fiche | qcm | interro | simulation |
|---|---|---|---|---|---|---|---|---|
| 01 | Transporter l'energie electrique | OK | OK | OK | OK | OK | OK | — |
| 02 | Stocker l'energie electrochimique | OK | OK | OK | OK | OK | OK | — |
| 03 | Rayonnement thermique & effet de serre | OK | OK | OK | OK | OK | OK | — |
| 04 | Vitesse et acceleration | OK | OK | OK | OK | OK | OK | — |
| 05 | Oxydoreduction & protection metaux | OK | OK | OK | OK | OK | OK | — |
| 06 | Choisir une source lumineuse | OK | OK | OK | OK | OK | OK | — |
| 07 | Transmettre l'information | OK | OK | **INCOMPLET** | OK | OK | OK | — |
| 08 | Attenuer une onde sonore | OK | OK | OK | OK | OK | OK | — |

**Bilan** : 48/48 fichiers de base presents (100%). 0 simulation. 1 DS incomplet (ch07).

---

## Problemes identifies

### 1. MathJax manquant dans maths/terminale/ch09/lecon.html (gravite : CRITIQUE)

Le cours « Fonctions ln et exponentielle » ne charge pas MathJax. Toutes les formules mathematiques sont donc invisibles pour les eleves.

**Fichier** : `maths/terminale/ch09/lecon.html`
**Correction** : Ajouter `<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>` dans le `<head>`.

### 2. DS PC ERA ch07 — niveau Approfondissement manquant (gravite : CRITIQUE)

Le DS du chapitre 07 (Transmettre l'information) ne contient que les niveaux Socle et Standard. Aucune section `diff-appro` n'est presente. Les eleves en approfondissement n'ont pas de devoir adapte.

**Fichier** : `physique-chimie/terminale-era/ch07/ds.html`
**Correction** : Ajouter une section Approfondissement avec exercices ouverts, /20 points.

### 3. DS PC ICCER ch03 — contenu reduit (gravite : MOYENNE)

Le DS du chapitre 03 (Moteur electrique) ne contient que 1 exercice par niveau (socle, standard, appro) soit 3 exercices au total, contre 6 a 12 pour les autres chapitres.

**Fichier** : `physique-chimie/terminale-iccer/ch03/ds.html`
**Correction** : Developper le DS avec 3-4 exercices par niveau.

### 4. Sous-titre incoherent dans PC ICCER ch01 (gravite : HAUTE)

Le sous-titre de ch01 indique « TICCER (Grpt 1) / ICCER » au lieu de « ICCER (Grpt 1) ». « TICCER » est une variante non standard.

**Fichier** : `physique-chimie/terminale-iccer/ch01/lecon.html`
**Correction** : Harmoniser avec les autres chapitres : « Terminale Bac Pro ICCER (Grpt 1) ».

### 5. CSS inline volumineux dans certaines lecons (gravite : BASSE)

Quelques lecons contiennent beaucoup de CSS inline (classes specifiques a la page) :
- `maths/terminale/ch04/lecon.html` : 36 lignes de CSS inline
- `maths/terminale/ch05/lecon.html` : 25 lignes de CSS inline
- `physique-chimie/terminale-iccer/ch07/lecon.html` : 29 lignes de CSS inline
- `physique-chimie/terminale-iccer/ch06/lecon.html` : 23 lignes de CSS inline

**Impact** : Pas de redefinition des classes styles.css (verifie). Ce sont des classes specifiques (`.tv-table`, `.classif`, `.calc-box`, etc.). Acceptable mais pourrait etre factorise dans styles.css si ces classes sont reutilisees.

### 6. Commentaires HTML avec sigles interdits dans PC ERA ch01-ch02 (gravite : BASSE)

Les lecons ch01 et ch02 de PC ERA contiennent des commentaires HTML `<!-- APPLICATION ERA-MA -->`. Bien qu'invisibles pour les eleves, cela ne respecte pas la convention du projet.

**Fichiers** :
- `physique-chimie/terminale-era/ch01/lecon.html` (ligne 473)
- `physique-chimie/terminale-era/ch02/lecon.html` (ligne 553)

**Correction** : Remplacer par `<!-- APPLICATION PROFESSIONNELLE -->`.

### 7. Boutons "Voir la correction" (bc) absents en Maths Terminale (gravite : MOYENNE)

Les exercices de Maths Terminale utilisent `<details><summary>` pour les corrections (ce qui fonctionne), mais n'utilisent pas la classe `.bc` (bouton "Voir la correction") presente dans styles.css, contrairement aux sections PC qui l'utilisent systematiquement.

**Fichiers** : tous les `maths/terminale/ch*/exercices.html`
**Impact** : Fonctionnel mais inconsistant avec le reste du site. Les `<details>` fonctionnent bien.
**Correction** : Harmonisation optionnelle — le mecanisme `<details>` est acceptable.

### 8. qcm.js non utilise dans la majorite des QCM (gravite : BASSE)

Sur 27 chapitres, seul `maths/terminale/ch02/qcm.html` inclut `qcm.js`. Tous les autres QCM gerent le scoring en JS inline.

**Impact** : Fonctionnel. La factorisation via `qcm.js` pourrait reduire la duplication de code.

---

## Verification technique

### Ressources essentielles

| Ressource | Maths Term | PC ICCER | PC ERA | Statut |
|---|---|---|---|---|
| MathJax | 10/11 | 8/8 | 8/8 | **ch09 manquant** |
| styles.css | 11/11 | 8/8 | 8/8 | OK |
| print.css | 11/11 | 8/8 | 8/8 | OK |
| nav.js | 11/11 | 8/8 | 8/8 | OK |
| diff.js (exercices/ds/interro/qcm) | 11/11 | 8/8 | 8/8 | OK |
| diff.js absent de lecon.html | 11/11 | 8/8 | 8/8 | OK (conforme) |
| Chemins styles.css corrects | 11/11 | 8/8 | 8/8 | OK |

### Differenciation pedagogique

| Section | exercices.html | ds.html | interro.html | qcm.html |
|---|---|---|---|---|
| Maths Term (11 ch) | 11/11 complet | 11/11 complet | 11/11 complet | 11/11 complet |
| PC ICCER (8 ch) | 8/8 complet | 8/8 complet | 8/8 complet | 8/8 complet |
| PC ERA (8 ch) | 8/8 complet | **7/8** (ch07 manque appro) | 8/8 complet | 8/8 complet |

### Corrections d'exercices

| Section | Corrections (.corr) | Boutons (.bc) | Mecanisme |
|---|---|---|---|
| Maths Term | 171 corrections | 0 (utilise `<details>`) | details/summary |
| PC ICCER | 126 corrections | 126 boutons | bouton onclick toggle |
| PC ERA | 112 corrections | 112 boutons | bouton onclick toggle |

### Classes pedagogiques dans les lecons

| Section | .def | .prop | .meth | .att | .ex | Total |
|---|---|---|---|---|---|---|
| Maths Term (11 ch) | 53 | 56 | 43 | 36 | 97 | **285** |
| PC ICCER (8 ch) | 41 | 48 | 23 | 30 | 36 | **178** |
| PC ERA (8 ch) | ~40 | ~50 | ~25 | ~30 | ~40 | **~185** |

### QCM (nombre de questions radio)

| Section | Questions par chapitre | Total |
|---|---|---|
| Maths Term | ~46 par ch (184 radios / 4 choix) | ~506 questions |
| PC ICCER | ~16 par ch (64 radios / 4 choix) | ~128 questions |
| PC ERA | ~16 par ch (64 radios / 4 choix) | ~128 questions |

### Sigles de filiere interdits dans le contenu

| Section | Occurrences | Detail |
|---|---|---|
| Maths Term | 0 | OK |
| PC ICCER | 0 | OK |
| PC ERA | 2 (commentaires HTML) | ch01 et ch02 : `<!-- APPLICATION ERA-MA -->` |

---

## Taille des lecons (indicateur de richesse du contenu)

| Section | Min | Max | Moyenne |
|---|---|---|---|
| Maths Term | 608 lignes (ch01) | 1288 lignes (ch04) | 852 lignes |
| PC ICCER | 872 lignes (ch04) | 977 lignes (ch07) | 927 lignes |
| PC ERA | 556 lignes (ch05) | 777 lignes (ch04) | 645 lignes |

**Observation** : les lecons PC ERA sont en moyenne plus courtes que les lecons PC ICCER (~30% de moins). Cela peut refleter un contenu un peu moins developpe ou une structure plus concise.

---

## Points forts

1. **Couverture complete** : 162/162 fichiers de base presents (100%)
2. **Differenciation systematique** : Socle/Standard/Approfondissement dans 98% des pages evaluatives
3. **Navigation fonctionnelle** : nav.js + print.css inclus partout
4. **Chemins corrects** : aucun chemin vers styles.css incorrect
5. **Pas de diff.js dans les lecons** : conforme aux regles
6. **Classes pedagogiques variees** : bonne utilisation de .def, .prop, .meth, .att, .ex
7. **Corrections detaillees** : 400+ corrections interactives au total
8. **Pas de sigles interdits** dans le contenu visible (seulement 2 commentaires HTML)
9. **Couleurs thematiques coherentes** : chaque section utilise sa palette

---

## Corrections realisees

_(aucune correction realisee a ce jour — audit initial)_

---

## Ameliorations restantes

### Priorite critique
- [ ] Ajouter MathJax dans `maths/terminale/ch09/lecon.html`
- [ ] Ajouter section Approfondissement dans `physique-chimie/terminale-era/ch07/ds.html`

### Priorite haute
- [ ] Corriger le sous-titre de `physique-chimie/terminale-iccer/ch01/lecon.html` : remplacer « TICCER (Grpt 1) / ICCER » par « ICCER (Grpt 1) »

### Priorite moyenne
- [ ] Developper le DS de `physique-chimie/terminale-iccer/ch03/ds.html` (1 exercice/niveau → 3-4 exercices/niveau)
- [ ] Harmoniser le mecanisme de corrections en Maths Terminale (details/summary vs boutons .bc) — optionnel si coherence souhaitee
- [ ] Verifier que les lecons PC ERA ne sont pas trop courtes par rapport a celles de PC ICCER (comparer le contenu pedagogique)

### Priorite basse
- [ ] Remplacer commentaires `<!-- APPLICATION ERA-MA -->` par `<!-- APPLICATION PROFESSIONNELLE -->` dans PC ERA ch01/ch02
- [ ] Envisager la factorisation du CSS inline volumineux (ch04, ch05 maths ; ch06, ch07 ICCER) dans styles.css
- [ ] Generaliser l'utilisation de `qcm.js` dans tous les QCM (au lieu du JS inline)
- [ ] Creer des simulations interactives pour les chapitres qui s'y pretent (mecanique, ondes, fonctions)
