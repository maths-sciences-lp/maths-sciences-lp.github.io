# Plan d'amelioration — Chapitres de Seconde

**Date** : 2026-03-17
**Derniere mise a jour** : 2026-03-31
**Perimetre** : maths/seconde (14 ch.) + physique-chimie/seconde (14 ch.)

---

## Etat des lieux

### Couverture des fichiers (28 chapitres)

| Section | Lecons | Exercices | DS | Total |
|---|---|---|---|---|
| Maths Seconde | 14/14 | 14/14 | 14/14 | 42/42 |
| PC Seconde | 14/14 | 14/14 | 14/14 | 42/42 |
| **Total** | **28/28** | **28/28** | **28/28** | **84/84** |

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

- [ ] **PC ch04, ch05 lecon** — Labels `.label-def` places hors des blocs `.def` (deplacer a l'interieur)
- [ ] **PC ch01-ch14 lecon** — Uniformiser le format des `<title>` (adopter : `Ch0X — Titre — 2nde Bac Pro`)
- [ ] **PC ch01-ch07 DS** — Entites HTML (`&eacute;`, `&ndash;`, etc.) a convertir en UTF-8 (ch08-ch14 deja propres)
- [ ] **PC ch01-ch07 DS** — CSS inline redondant (classes `.partie`, `.pts`, `.comp-*` etc. a centraliser dans styles.css)
- [ ] **Maths Seconde** — Harmoniser les badges de niveaux (`badge-niv badge-1` → format standard)

### PRIORITE 2 — Ameliorations pedagogiques

- [x] **PC ch01-ch14 lecon** — Ajouter la classe `.situation` aux contextes professionnels existants ✅ 2026-03-31
- [x] **PC Seconde** — Diversifier les contextes pro : ajout sante, sport, energie, telecoms, quotidien ✅ 2026-03-31
- [ ] **Maths ch02 lecon** — Completer ou reorganiser le chapitre Statistiques (indicateurs de position/dispersion renvoyes vers ch03, cours anormalement court a 349 lignes)
- [ ] **Maths Seconde** — Ajouter des sections "Erreurs frequentes" (blocs `.att`) dans les chapitres qui en manquent

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

- **2026-03-31** : Ajout de blocs `.situation` sur 13 lecons PC Seconde (ch01-ch14, ch07 deja traite). Diversification des contextes professionnels : sante (audiologie, serums, oxymetre), sport (tapis de course, cycliste, salle de sport), energie (pompe a chaleur, thermostat, panneaux solaires), telecoms (fibre optique internet), quotidien (boisson, sudation, thermos). Maths ch01 : SVG ajoutés dans exercices et exercices-capacites.

---

## Suivi

| Phase | Statut | Date debut | Date fin |
|---|---|---|---|
| Phase 1 — Corrections techniques | A faire | — | — |
| Phase 2 — Ameliorations pedagogiques | En cours | 2026-03-31 | — |
| Phase 3 — Enrichissements | A faire | — | — |
