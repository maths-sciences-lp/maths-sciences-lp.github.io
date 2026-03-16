# Audit Global du Site Pédagogique

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-03-16 (session 4)
**Périmètre** : ensemble du site maths-sciences-lp.github.io

---

## Vue d'ensemble

| Indicateur | Valeur |
|---|---|
| Pages HTML totales | 477 |
| Sections (matière/niveau) | 8 (+1 BTS) |
| Chapitres couverts | 89 |
| Simulations interactives | 63 |
| Pages de cours (lecon.html) | 89 |
| Pages d'exercices (exercices.html) | 89 |
| Pages de DS (ds.html) | 89 |
| Programmes officiels (PDF) | 10+ |

### Couverture par section

| Section | Chapitres attendus | Chapitres existants | Couverture |
|---|---|---|---|
| maths/seconde | 14 | 14 | 100 % |
| maths/premiere | 9 | 9 | 100 % |
| maths/terminale | 11 | 11 | 100 % |
| physique-chimie/seconde | 14 | 14 | 100 % |
| physique-chimie/premiere-iccer | 10 | 10 | 100 % |
| physique-chimie/premiere-era | 10 | 10 | 100 % |
| physique-chimie/terminale-iccer | 11 (CLAUDE.md) | 8 | 73 % |
| physique-chimie/terminale-era | 8 | 8 | 100 % |

Chaque chapitre existant possède les 3 types de pages (lecon, exercices, ds).

---

## Problemes identifies

1. **Chapitres manquants en terminale ICCER** : CLAUDE.md indique ch01-ch11, mais seuls ch01-ch08 existent. Soit le programme a été réduit (mettre à jour CLAUDE.md), soit 3 chapitres restent à créer.

2. ~~**Chemins absolus cassés**~~ — **CORRIGÉ 2026-03-16** : 104 chemins corrigés (nav.js, nav.css, diff.js).

3. ~~**Simulations non liées**~~ — **CORRIGÉ 2026-03-16** : 63 simulations liées à 79 pages de cours.

4. ~~**Différenciation absente en maths/premiere**~~ — **CORRIGÉ 2026-03-16** : diff.js et classes diff-* ajoutées aux 18 fichiers.

5. **Corrections incomplètes** : certaines pages d'exercices ont un déséquilibre entre le nombre d'exercices (.exo) et de corrections (.corr), ce qui suggère des corrections manquantes.

6. **29 pages BTS stub** : dans `maths/bts/`, 29 fichiers (exercices.html et ds.html) ne contiennent qu'un placeholder "Ce devoir surveillé est en cours de rédaction". Les chapitres ch03-ch18 sont partiellement ou totalement incomplets.

---

## Corrections realisees

- **2026-03-16 (sessions 1-3)** : Corrigé 104 chemins absolus (nav.js, nav.css, diff.js), ajouté diff.js à maths/premiere (18 fichiers), harmonisé CSS maths seconde + PC seconde, standardisé labels PC premiere, remplacé .appli→.situation PC terminale ERA, retiré nav.js de 26 simulations, rédigé maths premiere ch05 et ch09.
- **2026-03-16 (session 4)** : Lié 63 simulations à 79 pages de cours (0 orpheline restante). Ajouté blocs .meth à PC terminale ERA ch01-ch06. Ajouté visualisations interactives à maths premiere ch03 et ch04.

---

## Ameliorations restantes

### Priorité haute
- [x] Corriger les 61 chemins absolus `/nav.js` → `../../../nav.js` (2026-03-16)
- [x] Corriger les 37 chemins absolus `/nav.css` → `../../../nav.css` (2026-03-16)
- [ ] Clarifier le nombre de chapitres attendus en physique-chimie/terminale-iccer (mettre à jour CLAUDE.md : ch01-ch08)

### Priorité moyenne
- [x] Ajouter diff.js et la différenciation dans maths/premiere (2026-03-16)
- [x] Lier les 63 simulations aux pages de cours correspondantes (2026-03-16, 79 pages modifiées)
- [ ] Compléter les corrections manquantes dans les pages d'exercices

### Priorité basse
- [ ] Compléter les 29 pages BTS stub (exercices et DS)
- [ ] Harmoniser les conventions de nommage entre sections
- [ ] Mettre en place un script de vérification automatique (CI)
