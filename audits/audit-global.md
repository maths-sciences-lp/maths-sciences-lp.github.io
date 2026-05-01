# Audit Global du Site Pédagogique

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-05-01 (Phase 4 visuels Seconde TERMINÉE 15/15 + Phase 1 quick wins — 30/04 audit complet + couverture simulations 100% + index par chapitre)
**Note** : compteur simulations corrigé (63 → 70 → 78 → 82) ; cible chapitre Bac Pro = 8 types (lecon, exercices, ds, fiche, qcm, interro, exercices-capacites, activite)
**Périmètre** : ensemble du site maths-sciences-lp.github.io

---

## Vue d'ensemble (avril 2026)

| Indicateur | Valeur |
|---|---|
| Pages HTML totales | **~1 190** |
| Sections (matière/niveau) | **12** (Maths Seconde, 1ère, Terminale, LGT Term, CAP, BTS · PC Seconde, 1ère ICCER, 1ère ERA, Term ICCER, Term ERA, CAP) |
| Chapitres couverts | **138** |
| **Pages d'accueil par chapitre** (`index.html`) | **138** ✅ (créées avril 2026) |
| **Pages simulation par chapitre** (`simulation.html`) | **120** |
| Simulations interactives autonomes | **82** (catalogue régénéré) |
| Couverture simulations Lycée Pro | **98/98 (100 %)** ✅ |
| Activités (`activite.html`) | **130+** (Bac Pro + CAP + PC) |
| Sommaires cliquables (titres → index) | **13/13** ✅ |
| Objectifs injectés sur pages-ressources | **544 pages** |
| Aria-label sur canvas/SVG | **114 ajoutés** (a11y WCAG 2.1) |
| Sigles interdits (contenu) | **0** (corrigés en mars/avril ; +1 résiduel `maths/terminale/ch10/qcm.html` reformulé 2026-04-30) |
| Pages HTML structurellement saines | **100%** (17 fixes balance divs) |
| Mobile responsive | **3 breakpoints** (380/600/800 px) |
| **Phase 4 visuels Seconde Pro (relevé 22/04)** | **15/15 chapitres traités** (clôture 01/05) — 68 SVG ajoutés sur les exercices.html |
| Stubs BTS | **29** (placeholders « en cours de rédaction ») |

### Couverture par section (avril 2026)

| Section | Chapitres | Index | Simulation | Couverture |
|---|---|---|---|---|
| maths/seconde | 14/14 | 14/14 ✅ | 14/14 ✅ | 100 % |
| maths/premiere | 9/9 | 9/9 ✅ | 9/9 ✅ | 100 % |
| maths/terminale | 11/11 | 11/11 ✅ | 11/11 ✅ | 100 % |
| maths/lgt-terminale | 15/15 | 15/15 ✅ | 11/15 | 73 % |
| maths/cap | 7/7 | 7/7 ✅ | 7/7 ✅ | 100 % |
| maths/bts | 25/25 | 25/25 ✅ | 11/25 | 44 % (BTS hors lycée pro) |
| physique-chimie/seconde | 14/14 | 14/14 ✅ | 14/14 ✅ | 100 % |
| physique-chimie/premiere-iccer | 10/10 | 10/10 ✅ | 10/10 ✅ | 100 % |
| physique-chimie/premiere-era | 10/10 | 10/10 ✅ | 10/10 ✅ | 100 % |
| physique-chimie/terminale-iccer | 8/8 | 8/8 ✅ | 8/8 ✅ | 100 % |
| physique-chimie/terminale-era | 8/8 | 8/8 ✅ | 8/8 ✅ | 100 % |
| physique-chimie/cap | 7/7 | 7/7 ✅ | 7/7 ✅ | 100 % |
| **TOTAL** | **138** | **138/138** ✅ | **120/138** | **87 %** (100% lycée pro) |

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

- **2026-04-30** : Audit total du site — recensement complet (1 103 fichiers HTML, 84 chapitres Bac Pro × 8 types = 672 fichiers, 14 chapitres CAP, 25 chapitres BTS, 15 chapitres LGT, 14 chapitres groupements PC, 78 simulations, 21 automatismes, 38 co-interventions). Constats : 0 chemin absolu résiduel, 0 chapitre Bac Pro stub, 1 sigle ICCER en contenu (maths/terminale/ch10/qcm.html), entités HTML résiduelles dans ~125 fichiers (CAP, BTS, PC première/terminale), timestamp `.maj` déployé sur 82/1 103 fichiers seulement (≈7 %), 1 leçon sans mini-exo (`physique-chimie/premiere-era/ch10/lecon.html`).
- **2026-04-30** : **Phase 1 — Quick wins** : (A) sigle « Contexte ICCER » dans `maths/terminale/ch10/qcm.html` ligne 529 reformulé en « Application en installation thermique » → 0 sigle interdit en contenu sur l'ensemble du site. (B) 3 mini-exo `.mini-exo` ajoutés dans `physique-chimie/premiere-era/ch10/lecon.html` (vitesse du son dans le bois, longueur d'onde aspirateur, addition de niveaux sonores) → toutes les leçons Bac Pro ont désormais des mini-exo. (C) 8 simulations bois/agencement référencées dans `simulations.html` (presse-hydraulique, paroi-multicouche, escalier-blondel, eclairage-atelier, dilatation-parquet, comparateur-vitrages, calepinage, anisotropie-bois) + 3 liens ajoutés depuis les leçons (1ère ERA ch05 et ch07).
- **2026-04-30** : **Phase 2 — Enrichissement visuels Seconde Pro** : (E) `maths/seconde/ch04/exercices.html` (Probabilités) — 6 SVG ajoutés dans les corrections : tableau 6×6 des sommes de deux dés (Ex 13), courbe de convergence f → p de la loi des grands nombres (Ex 22), arbre de probabilités à 2 niveaux fiabilité d'une machine (Ex 23), droites graduées d'intervalle de fluctuation pour panneaux conformes (Ex 25), pour pièce truquée (Ex 27), arbre 2 épreuves contrôle panneaux solaires (Ex 29). Ratio visuels/exos : 19 % → **39 %**. (F) `maths/seconde/ch13/exercices.html` (Thalès) — 6 SVG ajoutés : ombre piquet/pylône avec rayons solaires (Ex 13), comparaison cas parallèle/non parallèle réciproque (Ex 14), configuration papillon avec longueurs (Ex 15), triangle Thalès complet AD/AB/AE/AC/DE/BC (Ex 19), triangle après résolution équation x (Ex 23), triangle problème 2 étapes (Ex 22). Ratio : 18 % → **31 %**. Timestamp `.maj` mis à jour.
- **2026-05-01** : **Phase 2 (suite) — Enrichissement visuels PC Seconde Pro** : (H) `physique-chimie/seconde/ch11/exercices.html` (Transferts thermiques) — 6 SVG ajoutés dans les corrections : 3 schémas illustrés conduction/convection/rayonnement (Ex 1), diagramme barres logarithmique des conductivités thermiques (Ex 5), comparaison flux 2 panneaux bois vs verre (Ex 17), schéma atelier avant/après isolation avec flèches de flux (Ex 19), comparaison cadre fenêtre bois vs aluminium (Ex 22), coupe double vitrage + schéma équivalent R en série (Ex 25). Ratio visuels/exos : 10 % → **25 %** (cible atteinte). (I) `physique-chimie/seconde/ch01/exercices.html` (Sécurité) — 5 SVG ajoutés : 6 pictogrammes EPI avec libellés (Ex 2), échelle des niveaux sonores avec seuils 85 dB et 120 dB (Ex 8), 3 bacs de tri DDS/recyclage/ordures (Ex 9), schéma installation électrique compteur+DJ+DDR (Ex 14), tableau des 5 classes de laser (Ex 17). Ratio : 16 % → **31 %**. Timestamp `.maj` mis à jour.
- **2026-05-01** : **Phase 2 (suite, vague 2)** : (K) `physique-chimie/seconde/ch03/exercices.html` (Loi d'Ohm) — 5 SVG ajoutés : 3 pistolets à colle en parallèle (Ex 6), 2 lampes 60 Ω en parallèle avec lois de Kirchhoff (Ex 11), choix du fusible (Ex 13), schéma circuit mixte série+parallèle (Ex 20), caractéristique U(I) non linéaire d'une lampe à incandescence vs droite ohmique (Ex 19). Ratio 17 % → **31 %**. (L) `maths/seconde/ch07/exercices.html` (Notion de fonction) — 5 SVG ajoutés : graphe C(x) = 8x+20 avec lecture antécédents (Ex 11), schéma flèches image vs antécédent ensemble départ → arrivée (Ex 6), graphe avec lecture image (vert montant) et antécédent (rouge horizontal) (Ex 7), facture d'eau f(x)=4x+10 avec abonnement (Ex 9), graphe E(t)=2t avec antécédent t≈3,5 h (Ex 16). Ratio 12 % → **25 %**. (M) `physique-chimie/seconde/ch05/exercices.html` (Mouvement) — 3 SVG ajoutés : chronophotographie 5 positions équidistantes avec vecteurs vitesse identiques (Ex 4), piste d'athlétisme 400 m vue de dessus avec lignes droites + virages circulaires (Ex 11), comparaison 3 chronophotographies uniforme/accéléré/décéléré (Ex 14). Ratio 19 % → **28 %**. Timestamps `.maj` mis à jour.
- **2026-05-01** : **Relecture critique des 33 SVG ajoutés en Phase 2** — 7 corrections appliquées : ch07 Ex 7 (alignement points/graduations), ch07 Ex 11 (graduations Y linéaires), ch07 Ex 9 (droite étendue), ch13 Ex 14 cas 2 (E placé sur AC), ch13 Ex 15 (papillon à l'échelle 1u=8px), ch04 Ex 22 (graduations linéaires + 4 points), ch01 Ex 8 (graduations 30/60 + zones colorées). 26 SVG vérifiés sans correction nécessaire.
- **2026-05-01** : **Phase 2 (vague 3)** : (P) `physique-chimie/seconde/ch10/exercices.html` (Température) — 4 SVG ajoutés : double échelle Celsius/Kelvin avec 6 repères (Ex 1), placement de 5 températures sur échelle (azote, hiver, eau, corps, étuve) (Ex 8), plages de fonctionnement des 6 capteurs CTN/CTP/LM35/Pt100/thermocouple/IR (Ex 11), courbe R(T) d'une CTN avec seuil 8 kΩ (Ex 14). Ratio 11 % → **30 %**. (Q) `physique-chimie/seconde/ch12/exercices.html` (Changements d'état) — 3 SVG ajoutés : courbe T(t) annotée avec 3 phases (Ex 3), schéma fusion glace E=m×L_f (Ex 4), schéma vaporisation eau dans bois E=m×L_v (Ex 5). Ratio 12 % → **23 %**. (R) `maths/seconde/ch10/exercices.html` (Fonction carré) — 5 SVG ajoutés : parabole avec variations (Ex 4), résolution graphique x²=k avec 4 droites horizontales (Ex 7), aire de cadres 10 cm vs 20 cm × 4 (Ex 9), trajectoire ballon h(t)=−t²+4 (Ex 11), distance de freinage v² avec effet quadratique (Ex 14). Ratio 19 % → **30 %**.
- **2026-05-01** : **Phase 2 vague 4 — clôture Phase 4 du plan d'amélioration Seconde** : (T) `maths/seconde/ch03/exercices.html` (Indicateurs stats) — 3 SVG : comparaison étendue 2 séries A/B (Ex 5), boîte à moustaches Q1/Me/Q3 + IQR (Ex 4), distribution autour moyenne avec fuseau ±σ (Ex 7). Ratio 20 % → 30 %. (U) `maths/seconde/ch08/exercices.html` (Fonction linéaire) — 1 SVG : droite f(x)=5x avec lecture antécédents (Ex 13). (V) `maths/seconde/ch14/exercices.html` (Solides) — 1 SVG : agrandissement pavé 10×6×4 → 20×12×8 montrant V × 2³ = 8 (Ex 5). (W) `physique-chimie/seconde/ch08/exercices.html` (Solutions) — 1 SVG : échelle pH avec placement des produits d'atelier et zones de danger (Ex 5). (X) `physique-chimie/seconde/ch09/exercices.html` (Son) — 1 SVG : oscillogramme diapason 5 oscillations sur 11,4 ms (Ex 22). (Y) `physique-chimie/seconde/ch14/exercices.html` (Lumière) — 1 SVG : spectre visible 380-780 nm avec 6 couleurs placées (Ex 7). **Phase 4 : 15/15 chapitres complétés, 60+8 = 68 SVG ajoutés au total**.
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

### Priorité haute (chantiers structurels — relevé 2026-04-30)
- [ ] **BTS** — compléter les 7 chapitres sans exercices ni DS (ch19–ch25) + créer les fiche/qcm/interro/exercices-capacites pour les 25 chapitres
- [ ] **LGT Terminale** — créer exercices/ds/fiche/qcm/interro pour les 15 chapitres (actuellement lecon + exercices-capacites uniquement)
- [ ] **Groupements PC** — créer ds.html pour les 14 chapitres gpt 2/4/5/6 + qcm/interro/exercices-capacites
- [x] ~~Corriger l'unique sigle interdit dans contenu : `maths/terminale/ch10/qcm.html:529` (« Contexte ICCER »)~~ → **fait 2026-04-30** (« Application en installation thermique »)
- [ ] Convertir les entités HTML résiduelles → UTF-8 dans les ~125 fichiers identifiés (CAP 56, BTS 19, PC première-iccer 19, terminale-iccer/era 34, premiere-era 10, premiere maths 11)

### Priorité haute (audit Seconde Pro 2026-04-22)
- [x] ~~Enrichir `physique-chimie/seconde/ch11` (Transferts thermiques)~~ → **fait 2026-05-01** : 6 SVG (3 modes illustrés, conductivités log, R bois vs verre, atelier isolation, fenêtre bois vs alu, coupe double vitrage). Ratio 10 % → 25 %.
- [x] ~~Enrichir `physique-chimie/seconde/ch01` (Sécurité)~~ → **fait 2026-05-01** : 5 SVG (6 EPI illustrés, échelle dB, bacs tri, installation électrique disjoncteurs, classes laser). Ratio 16 % → 31 %.
- [x] ~~Enrichir `maths/seconde/ch04` (Probabilités)~~ → **fait 2026-04-30** : 6 SVG ajoutés (tableau dés, convergence f→p, 2 arbres, 2 droites graduées intervalles), ratio 19 % → 39 %
- [x] ~~Enrichir `maths/seconde/ch13` (Thalès)~~ → **fait 2026-04-30** : 6 SVG ajoutés (ombre soleil, 2 cas réciproque, papillon, 3 triangles Thalès), ratio 18 % → 31 %

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
- [ ] Déployer le timestamp `.maj` (règle CLAUDE.md n°10) sur les sections où il manque (PC première/terminale, CAP) — actuellement 82/1 103 fichiers (≈7 %)
- [x] ~~Ajouter mini-exo manquant dans `physique-chimie/premiere-era/ch10/lecon.html`~~ → **fait 2026-04-30** (3 mini-exo : poutre chêne, aspirateur, addition niveaux)
