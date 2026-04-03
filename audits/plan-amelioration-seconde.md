# Plan d'amelioration — Chapitres de Seconde

**Date** : 2026-03-17
**Derniere mise a jour** : 2026-03-31
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

- **2026-04-03** : Conversion UTF-8 complete PC Seconde — 80 fichiers modifies, 26 678 entites HTML converties (lecon, exercices, ds, fiche, qcm, interro, activite, ch01-ch14). Titres `<title>` uniformises (UTF-8 propre, format `Ch0X – Titre – 2nde Bac Pro`). Labels ch04/ch05 et badges niveaux maths verifies conformes.
- **2026-03-31** : Audit complet des 28 chapitres Seconde Pro (14 maths + 14 PC). Structure 8 fichiers complete sur 100% des chapitres. Aucun probleme technique detecte (nav.js, print.css, styles.css, MathJax, themes couleur, diff.js, sigles interdits, liens sommaire).

---

## Suivi

| Phase | Statut | Date debut | Date fin |
|---|---|---|---|
| Phase 1 — Corrections techniques | Quasi complete (1 item CSS inline restant) | 2026-04-03 | 2026-04-03 |
| Phase 2 — Ameliorations pedagogiques | Complete | 2026-04-03 | 2026-04-03 |
| Phase 3 — Enrichissements | A faire | — | — |
