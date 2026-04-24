# Plan d'amelioration — Chapitres de Seconde

**Date** : 2026-03-17
**Derniere mise a jour** : 2026-04-22
**Perimetre** : maths/seconde (14 ch.) + physique-chimie/seconde (14 ch.)

---

## Etat des lieux

### Couverture des fichiers (28 chapitres) — verifie 2026-03-31

| Section | lecon | exercices | ds | fiche | qcm | interro | ex-capa | activite | Total |
|---|---|---|---|---|---|---|---|---|---|
| Maths Seconde | 14/14 | 14/14 | 14/14 | 14/14 | 14/14 | 14/14 | 14/14 | 14/14 | 112/112 |
| PC Seconde | 14/14 | 14/14 | 14/14 | 14/14 | 14/14 | 14/14 | 14/14 | 14/14 | 112/112 |
| **Total** | **28/28** | **28/28** | **28/28** | **28/28** | **28/28** | **28/28** | **28/28** | **28/28** | **224/224** |

### Conformite technique — verifie 2026-03-31

| Indicateur | Maths Seconde | PC Seconde |
|---|---|---|
| nav.js present | 100% | 100% |
| print.css present | 100% | 100% |
| styles.css present | 100% | 100% |
| MathJax present (la ou necessaire) | 100% | 100% |
| Theme couleur conforme | `#0056b3` OK | `#6f42c1` OK |
| diff.js absent des lecon.html | OK | OK |
| Differenciation exercices.html | 14/14 | 14/14 |
| Differenciation ds.html | 14/14 | 14/14 |
| Sigles interdits dans contenu | 0 violation | 0 violation |
| Fichiers stubs/vides | aucun | aucun |
| Liens retour sommaire | corrects | corrects |

### Corrections : etat reel (verifie 2026-03-17)

**IMPORTANT** : L'audit precedent surestimait les corrections manquantes (comparaison sous-questions vs blocs `.corr`). La realite :

| Section | Boutons "Voir la correction" | Statut |
|---|---|---|
| PC Seconde exercices (ch01-ch14) | 12-26 par fichier | **Toutes presentes** |
| PC Seconde DS (ch01-ch14) | 7-10 par fichier, corr=parties | **Toutes presentes** |
| Maths Seconde exercices (ch01-ch14) | 12-15 par fichier | **Toutes presentes** |
| Maths Seconde DS (ch01-ch14) | 7-13 par fichier, corr=parties | **Toutes presentes** |

Les corrections sont **toutes redigees**. Le chiffre "517 manquantes" etait une erreur de comptage.

---

## Taches a realiser

### PRIORITE 1 — Problemes techniques (corrections rapides)

- [x] ~~**PC ch04, ch05 lecon** — Labels `.label-def` places hors des blocs `.def`~~ → deja corrects (labels bien a l'interieur)
- [x] ~~**PC ch01-ch14 lecon** — Uniformiser le format des `<title>`~~ → **2026-04-03** 13 titres convertis en UTF-8
- [x] ~~**PC ch01-ch07 DS** — Entites HTML a convertir en UTF-8~~ → **2026-04-03** 80 fichiers PC Seconde convertis (26 678 entites), tous types (lecon, exercices, ds, fiche, qcm, interro, activite)
- [x] ~~**PC DS ch01-ch14** — CSS inline redondant~~ → **2026-04-03** : `.answer-box`, `.aide-box`, `.formule-donnee`, `.ds-title`, `.ds-title--card` centralisés dans `styles.css` ; `@media print` redondants supprimés de 14 DS ; ch10/ch11 migrés vers `.ds-title--card`
- [x] ~~**Maths Seconde** — Harmoniser les badges de niveaux~~ → `badge-niv/1/2/3` deja dans styles.css, conformes

### PRIORITE 2 — Ameliorations pedagogiques

- [x] ~~**PC ch01-ch14 lecon** — Ajouter la classe `.situation` aux contextes professionnels existants (0 occurrences actuellement)~~ → **2026-04-03** 1 bloc `.situation` ajouté dans chacune des 14 leçons PC Seconde
- [x] ~~**Maths ch02 lecon** — Completer ou reorganiser le chapitre Statistiques~~ → **2026-04-03** Chapitre restructuré (372→561 lignes) : section fréquences cumulées, tableau double entrée, histogramme ajoutés ; médiane/quartiles/boîte renvoyés proprement vers ch03
- [x] ~~**PC Seconde** — Diversifier les contextes pro : ajouter sport, sante, environnement (actuellement quasi exclusivement menuiserie)~~ → **2026-04-03** 3 exercices variés ajoutés dans ch03, ch06, ch08, ch10, ch11, ch12 (sport, santé, énergie, environnement)
- [x] ~~**Maths Seconde** — Ajouter des sections "Erreurs frequentes" (blocs `.att`) dans les chapitres qui en manquent~~ → **2026-04-03** Sections `.erreur-item` ajoutées dans ch02, ch03, ch09, ch10, ch11, ch12, ch13, ch14 (4-5 erreurs/chapitre)

### PRIORITE 3 — Enrichissements

- [ ] **PC 1ere ICCER** — Ajouter des mini-exercices dans les lecons (actuellement 0 `.exo` dans les lecons)
- [ ] **PC Seconde** — Enrichir les situations professionnelles avec davantage de personnages/scenarios

### PRIORITE 4 — Ratio visuels / exercices (releve 2026-04-22)

La relecture detaillee Seconde Pro du 2026-04-22 a mis en evidence un deficit systematique de visuels dans les pages d'exercices. Objectif : atteindre au moins 0,5 visuel par exercice en maths et 25 % en PC.

**Maths Seconde — cible = ratio ≥ 0,65**

- [x] ~~**ch06 Inequations du 1er degre** (ratio 7/19 = 0,37 → critique)~~ → **2026-04-22** 7 SVG droites graduees recapitulatives ajoutees (Ex 3, 4, 6, 7, 20, 21, 27). Ratio 14/19 = 0,74.
- [ ] **ch04 Probabilites et fluctuation** (6/15 = 0,40) : ajouter arbres de probabilites, diagrammes de fluctuation, histogrammes. Priorite haute.
- [ ] **ch13 Theoreme de Thales** (8/19 = 0,42) : ajouter figures geometriques (configurations droites paralleles, triangles emboites, inversion). Priorite haute.
- [ ] **ch03 Indicateurs statistiques** (6/12 = 0,50) : graphiques de distribution, boites a moustaches.
- [ ] **ch07 Notion de fonction** (10/18 = 0,55) : schemas de correspondance, tableaux de valeurs illustres.
- [ ] **ch08 Fonction lineaire** (9/18 = 0,50) : courbes representatives, triangles de pente.
- [ ] **ch10 Fonction carre** (11/19 = 0,57) : paraboles, tableaux de signe visuels.
- [ ] **ch14 Solides et volumes** (9/16 = 0,56) : vues eclatees de solides, patrons annotes.

**PC Seconde — cible = ratio ≥ 25 %**

- [ ] **ch11 Transferts thermiques** (6/80 = 7 % — pire ratio) : schemas conduction / convection / rayonnement, courbes T(t), diagrammes d'echanges thermiques. Priorite **critique**.
- [ ] **ch01 Securite en laboratoire** (7/64 = 11 %) : pictogrammes GHS SVG, schemas EPI annotes, pictogrammes interdiction/obligation. Priorite haute.
- [ ] **ch03 Loi d'Ohm** (8/72 = 11 %) : caracteristiques (U,I), schemas de circuits annotes.
- [ ] **ch05 Mouvement et trajectoire** (8/64 = 12 %) : chronophotographies stylisees, vecteurs vitesse.
- [ ] **ch08 Solutions chimiques** (8/72 = 11 %) : schemas dissolution/dilution, echelles de concentration.
- [ ] **ch09 Caracteristiques d'un son** (8/62 = 13 %) : oscillogrammes, spectres, courbes sinusoidales.
- [ ] **ch10 Temperature et capteurs** (8/72 = 11 %) : courbes etalonnage, schemas thermistance/PT100.
- [ ] **ch12 Changements d'etat** (9/76 = 12 %) : diagrammes etat, courbes T(Q), paliers de changement d'etat.
- [ ] **ch14 Lumiere et couleurs** (8/66 = 12 %) : synthese additive/soustractive, spectres, decomposition prisme.

---

## Organisation du travail

### Phase 1 : Corrections techniques (rapides, groupees)
1. Labels ch04/ch05 → deplacer a l'interieur des `.def`
2. Titres `<title>` uniformises sur les 14 lecons PC
3. Entites HTML → UTF-8 dans DS ch01-ch07
4. Badges de niveaux maths harmonises
5. Un seul commit

### Phase 2 : Ameliorations pedagogiques
1. Ajout `.situation` dans les 14 lecons PC Seconde
2. Completude de maths/seconde/ch02 (statistiques)
3. Diversification des contextes pro

### Phase 3 : Enrichissements
1. Mini-exercices lecons PC
2. Scenarios professionnels enrichis

---

## Corrections realisees

- **2026-04-22** : Relecture detaillee des 28 chapitres Seconde Pro (maths + PC). Tableau de bord publie dans `audit-global.md`. Chapitres prioritaires identifies (visuels insuffisants). **Enrichissement de `maths/seconde/ch06/exercices.html`** : 7 SVG droites graduees recapitulatives ajoutees aux corrections des exercices 3, 4, 6, 7, 20, 21, 27 (ratio visuels/exercices de 0,37 a 0,74). Timestamp mis a jour.
- **2026-04-03** : Conversion UTF-8 complete PC Seconde — 80 fichiers modifies, 26 678 entites HTML converties (lecon, exercices, ds, fiche, qcm, interro, activite, ch01-ch14). Titres `<title>` uniformises (UTF-8 propre, format `Ch0X – Titre – 2nde Bac Pro`). Labels ch04/ch05 et badges niveaux maths verifies conformes.
- **2026-03-31** : Audit complet des 28 chapitres Seconde Pro (14 maths + 14 PC). Structure 8 fichiers complete sur 100% des chapitres. Aucun probleme technique detecte (nav.js, print.css, styles.css, MathJax, themes couleur, diff.js, sigles interdits, liens sommaire).

---

## Suivi

| Phase | Statut | Date debut | Date fin |
|---|---|---|---|
| Phase 1 — Corrections techniques | Quasi complete (1 item CSS inline restant) | 2026-04-03 | 2026-04-03 |
| Phase 2 — Ameliorations pedagogiques | Complete | 2026-04-03 | 2026-04-03 |
| Phase 3 — Enrichissements | A faire | — | — |
| Phase 4 — Visuels dans exercices | En cours (1/15 chapitres traites : maths ch06) | 2026-04-22 | — |
