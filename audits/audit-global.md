# Audit Global du Site Pédagogique

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-04-22
**Note** : compteur simulations corrigé (63 → 70) le 2026-04-06 ; relecture Seconde Pro le 2026-04-22
**Périmètre** : ensemble du site maths-sciences-lp.github.io

---

## Vue d'ensemble

| Indicateur | Valeur |
|---|---|
| Pages HTML (chapitres) | **504** |
| Sections (matière/niveau) | 8 (+1 BTS) |
| Chapitres couverts | **84** |
| Simulations interactives | 70 |
| Complétude structurelle | **100 %** (504/504 fichiers) |
| Stubs détectés | **0** |
| Sigles interdits (contenu) | ~90 occurrences |

### Couverture par section

| Section | Chapitres | Score | Fichiers | Couverture |
|---|---|---|---|---|
| maths/seconde | 14/14 | 13/13 | 84/84 | 100 % |
| maths/premiere | 9/9 | 13/13 | 54/54 | 100 % |
| maths/terminale | 11/11 | 13/13 | 66/66 | 100 % |
| physique-chimie/seconde | 14/14 | 13/13 | 84/84 | 100 % |
| physique-chimie/premiere-iccer | 10/10 | 13/13 | 60/60 | 100 % |
| physique-chimie/premiere-era | 10/10 | 13/13 | 60/60 | 100 % |
| physique-chimie/terminale-iccer | 8/8 | 13/13 | 48/48 | 100 % |
| physique-chimie/terminale-era | 8/8 | 13/13 | 48/48 | 100 % |
| **TOTAL** | **84** | **13/13** | **504/504** | **100 %** |

### Couverture par type de page

| Type de page | Existant | Cible (84 ch.) | Couverture |
|---|---|---|---|
| `lecon.html` | 84 | 84 | 100 % |
| `exercices.html` | 84 | 84 | 100 % |
| `ds.html` | 84 | 84 | 100 % |
| `fiche.html` | 84 | 84 | 100 % |
| `qcm.html` | 84 | 84 | 100 % |
| `interro.html` | 84 | 84 | 100 % |

### Score de complétude

Barème : obligatoires (lecon, exercices, ds) = 3 pts chacun (9 pts max) + recommandé (fiche) = 2 pts + optionnels (qcm, interro) = 1 pt chacun (2 pts max) = **13 pts max par chapitre**.

**Tous les 84 chapitres obtiennent 13/13.**

### Bilan Seconde (2026-03-21)

La **Seconde est la section modèle du site** — vérification exhaustive des exercices réalisée le 2026-03-21.

| Dimension | Maths Seconde | PC Seconde | Total |
|---|---|---|---|
| Chapitres | 14/14 | 14/14 | **28/28** |
| Fichiers HTML | 84 | 84 | **168** |
| Types de pages (6/6) | 100 % | 100 % | **100 %** |
| Corrections exercices | **100 %** | **100 %** | **100 %** |
| Corrections DS | 100 % | 100 % | **100 %** |
| Erreurs scientifiques | 0 | 0 | **0** |
| Blocs différenciés | 168 | 169 | **337** |
| Simulations | 2 | 0 | **2** |

**Note (2026-03-21)** : les taux de corrections d'exercices antérieurs (41 % maths, 80 % PC) étaient sous-estimés car ils ne comptaient pas le format `<details>` + `<summary>`. La vérification exhaustive confirme **100 % de corrections présentes** dans les deux matières.

### Relecture Seconde Pro (2026-04-22)

Passage systématique sur les 28 chapitres Seconde (maths + PC) pour vérifier visuels, différenciation, sigles interdits et complétude.

| Section | Chapitres | 🟢 OK | 🟡 À améliorer | 🔴 Critique | Fichiers | Diff | Sigles |
|---|---|---|---|---|---|---|---|
| maths/seconde | 14 | 7 | 6 | 1 (ch06 → corrigé) | 14/14 ✅ | 14/14 ✅ | 0 ✅ |
| physique-chimie/seconde | 14 | 0 | 14 | 0 | 14/14 ✅ | 14/14 ✅ | 0 ✅ |

**Points forts :**
- Aucun fichier obligatoire manquant, différenciation systématique, aucun sigle interdit.

**Point faible identifié :** ratio visuels/exercices systématiquement insuffisant.

**Chapitres prioritaires :**

| Chapitre | Ratio visuels | Statut |
|---|---|---|
| maths/seconde/ch06 Inéquations | 7/19 → 14/19 | ✅ corrigé 2026-04-22 |
| physique-chimie/seconde/ch11 Transferts thermiques | 6/80 (7 %) | À traiter |
| physique-chimie/seconde/ch01 Sécurité | 7/64 (11 %) | À traiter |
| maths/seconde/ch04 Probabilités | 6/15 (40 %) | À traiter |
| maths/seconde/ch13 Thalès | 8/19 (42 %) | À traiter |
| maths/seconde/ch03, ch07, ch08, ch10 | 50–57 % | À traiter |
| PC/seconde/ch03, ch05, ch08, ch09, ch10, ch12, ch14 | 11–15 % | À traiter |

Détails et plan d'action : voir `audits/plan-amelioration-seconde.md`.

---

## Vérifications techniques (2026-03-21)

Échantillon : 2 chapitres par section (ch01 + dernier ch), 32 fichiers vérifiés.

| Vérification | Résultat |
|---|---|
| nav.js en fin de body | ✅ Partout |
| diff.js sur exercices.html et ds.html | ✅ Partout |
| print.css présent | ✅ Partout |
| Thème couleur `:root{--p:...}` cohérent | ✅ Partout |
| MathJax inclus si formules | ✅ Partout |
| Lien retour sommaire | ✅ Partout |
| Classes styles.css redéfinies inline | ✅ Aucune |

**Aucune anomalie technique détectée.**

---

## Sigles interdits dans le contenu (2026-03-21)

| Sigle | Occurrences | Catégorie principale |
|---|---|---|
| ICCER | ~44 | Commentaires HTML, identifiants Canvas, footers |
| ERA-MA | ~38 | Commentaires HTML, footers, sections pédagogiques |
| MAMA | ~8 | Commentaires HTML, simulations |
| **Total** | **~90** | |

**Fichiers les plus touchés :**
1. `maths/terminale/ch06/lecon.html` (4 occ. ICCER)
2. `physique-chimie/terminale-era/ch02/lecon.html` (ERA-MA dans sections)
3. `physique-chimie/terminale-iccer/ch07/lecon.html` (ICCER dans contenu)

La majorité des occurrences sont dans des **commentaires HTML** et des **footers**, pas dans le texte visible par les élèves. Commande pour corriger : `/check-sigles`

---

## Problemes identifies

1. **Sigles interdits (~90 occurrences)** : commentaires HTML, footers et identifiants Canvas contiennent ICCER/ERA-MA/MAMA dans ~30 fichiers. À nettoyer.

2. ~~**Chapitres manquants en terminale ICCER**~~ : CLAUDE.md indiquait ch01-ch11, mais seuls ch01-ch08 existent. Le programme réel couvre 8 chapitres. **CLAUDE.md à mettre à jour.**

3. ~~**Chemins absolus cassés**~~ — **CORRIGÉ 2026-03-16** : 104 chemins corrigés.

4. ~~**Simulations non liées**~~ — **CORRIGÉ 2026-03-16** : 63 simulations liées à 79 pages de cours.

5. ~~**Différenciation absente en maths/premiere**~~ — **CORRIGÉ 2026-03-16** : diff.js ajouté.

6. ~~**Corrections incomplètes exercices Seconde**~~ — **RÉSOLU 2026-03-21** : vérification exhaustive confirme 100 % de corrections présentes (format `<details>` non comptabilisé initialement).

7. ~~**QCM dans fichiers exercices.html maths/seconde**~~ — **CORRIGÉ 2026-03-21** : 8 QCM remplacés par des exercices de calcul (ch01, ch03, ch09-ch14).

8. ~~**Titres "Terminale" dans maths/seconde**~~ — **CORRIGÉ 2026-03-21** : ch01 et ch03 corrigés.

9. **29 pages BTS stub** : dans `maths/bts/`, 29 fichiers ne contiennent qu'un placeholder.

---

## Corrections realisees

- **2026-04-22** : Relecture détaillée des sections Seconde Pro (maths + PC, 28 chapitres). Tableau de bord publié, chapitres prioritaires identifiés. Enrichissement de `maths/seconde/ch06/exercices.html` (Inéquations) : 7 nouveaux SVG droites graduées récapitulatives ajoutés aux corrections des exercices 3, 4, 6, 7, 20, 21, 27. Ratio visuels/exercices de ch06 : 0,37 → 0,74.
- **2026-03-21** : Audit global automatisé — inventaire 504 fichiers, vérifications techniques, recherche sigles interdits. Mise à jour complète du tableau de bord.
- **2026-04-06** : Création `prompts/prompt-ds.md` (prompt complet pour les devoirs surveillés). Mise à jour de 4 prompts existants (`prompt-exercices.md`, `prompt-cours.md`, `prompt-qcm-interro.md`, `prompt-exercices-capacites.md`) : ajout règle "données uniquement", tableaux de données proactifs, références orphelines, règle animations Canvas. Skill `/check-quality` réécrit en revue IA pure (suppression des scripts `check_visuals.py`, `check_chapter_quality.py`, `count_svg.py`). Fix lien retour sommaire `physique-chimie/seconde/ch11/interro.html`.
- **2026-03-21** : Vérification exhaustive des 28 chapitres exercices Seconde (maths + PC) — 0 erreur, 100 % corrections présentes.
- **2026-03-21** : Remplacement de 8 QCM par des exercices dans maths/seconde (ch01, ch03, ch09-ch14).
- **2026-03-21** : Correction titres "Terminale" → "Seconde" dans ch01 et ch03 exercices.
- **2026-03-19** : Bilan complet Seconde. Interros : 84/84. QCMs : 84/84. Mise à jour compteurs.
- **2026-03-18** : Créé 46 QCMs différenciés + `prompts/prompt-qcm-interro.md`.
- **2026-03-16 (sessions 1-4)** : Corrigé 104 chemins, ajouté diff.js maths/premiere, harmonisé CSS, lié 63 simulations, ajouté blocs .meth PC terminale ERA.

---

## Ameliorations restantes

### Priorité haute
- [ ] Enrichir `physique-chimie/seconde/ch11` (Transferts thermiques) — ratio visuels/exercices 7 % (cible ≥ 25 %) : ajouter schémas conduction/convection/rayonnement, courbes T°(t), diagrammes échanges thermiques.
- [ ] Enrichir `physique-chimie/seconde/ch01` (Sécurité) — ratio 11 % : ajouter pictogrammes GHS et schémas EPI annotés.
- [ ] Enrichir `maths/seconde/ch04` (Probabilités) — ratio 40 % : ajouter arbres de probabilités, diagrammes de fluctuation, histogrammes.
- [ ] Enrichir `maths/seconde/ch13` (Thalès) — ratio 42 % : ajouter figures géométriques (configurations de Thalès, triangles).

### Priorité moyenne
- [ ] Enrichir `maths/seconde/ch03, ch07, ch08, ch10` (ratio 50–57 %) : graphiques de distribution, courbes de fonctions, paraboles.
- [ ] Enrichir `physique-chimie/seconde/ch03, ch05, ch08, ch09, ch10, ch12, ch14` (ratio 11–15 %) : circuits électriques annotés, diagrammes thermiques, schémas ondulatoires.
- [ ] Corriger les ~90 sigles interdits dans les commentaires HTML et footers → `/check-sigles`
- [ ] Clarifier le nombre de chapitres en physique-chimie/terminale-iccer (mettre à jour CLAUDE.md : ch01-ch08)

### Priorité basse
- [ ] Nettoyer les styles CSS inline → `/css-cleanup`
- [ ] Standardiser le format `<title>` sur l'ensemble du site
- [ ] Ajouter le balisage `.situation` aux contextes professionnels en PC/seconde
- [ ] Corriger `.niv1/.niv2` → `.niveau-1/.niveau-2` dans maths/seconde/ch03/exercices.html
- [ ] Corriger le placement des labels `.label-def` dans PC/seconde/ch04 et ch05
- [ ] Compléter les 29 pages BTS stub (exercices et DS)
- [ ] Mettre en place un script de vérification automatique (CI)
