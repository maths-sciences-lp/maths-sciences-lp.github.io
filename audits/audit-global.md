# Audit Global du Site Pédagogique

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-03-18 (QCMs)
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

Chaque chapitre doit proposer **6 types de pages** : lecon, exercices, ds, qcm, interro, fiche (voir `audits/audit-uniformisation.md` pour les specs).

### Couverture par type de page

| Type de page | Existant | Cible (84 ch.) | Couverture |
|---|---|---|---|
| `lecon.html` | 84 | 84 | 100 % |
| `exercices.html` | 77 | 84 | 92 % |
| `ds.html` | 77 | 84 | 92 % |
| `fiche.html` | 57 | 84 | 68 % |
| `qcm.html` | 48 | 84 | 57 % |
| `interro.html` | 2 | 84 | 2 % |

**Référence specs :** `prompts/prompt-qcm-interro.md` — philosophie, différenciation et templates.

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
- **2026-03-18** : Supprimé le doublon `automatismes.html` (racine), unifié les liens vers `automatismes/index.html`. Plan d'uniformisation : 6 types de pages par chapitre (ajout qcm.html et interro.html différenciés). Créé `prompts/prompt-qcm-interro.md`.
- **2026-03-18** : Créé 46 QCMs différenciés (3×15 questions socle/standard/appro) : maths/seconde (14), maths/premiere (9), maths/terminale (9 + ch02 existant), physique-chimie/seconde (13 + ch07 existant). Total QCMs : 48/84 (57%).

---

## Ameliorations restantes

### Priorité haute
- [x] Corriger les 61 chemins absolus `/nav.js` → `../../../nav.js` (2026-03-16)
- [x] Corriger les 37 chemins absolus `/nav.css` → `../../../nav.css` (2026-03-16)
- [ ] Clarifier le nombre de chapitres attendus en physique-chimie/terminale-iccer (mettre à jour CLAUDE.md : ch01-ch08)

### Priorité haute (uniformisation 2026-03-18)
- [ ] Créer les 36 `qcm.html` restants (PC 1ere ICCER 10, PC 1ere ERA 10, PC Tle ICCER 8, PC Tle ERA 8) — 48/84 faits
- [ ] Créer les 83 `interro.html` manquants (interrogations diagnostiques différenciées, 3×5-8 questions)
- [ ] Créer les 7 `exercices.html` et 7 `ds.html` manquants (PC terminale)
- [ ] Centraliser les classes CSS QCM dans `styles.css` avant création en masse
- [ ] Mettre à jour les sommaires pour lister qcm.html et interro.html

### Priorité moyenne
- [x] Ajouter diff.js et la différenciation dans maths/premiere (2026-03-16)
- [x] Lier les 63 simulations aux pages de cours correspondantes (2026-03-16, 79 pages modifiées)
- [ ] Compléter les corrections manquantes dans les pages d'exercices
- [ ] Créer les 27 `fiche.html` manquants

### Priorité basse
- [ ] Compléter les 29 pages BTS stub (exercices et DS)
- [ ] Harmoniser les conventions de nommage entre sections
- [ ] Mettre en place un script de vérification automatique (CI)
