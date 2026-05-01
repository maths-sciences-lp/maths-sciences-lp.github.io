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
- [x] ~~**ch04 Probabilites et fluctuation**~~ → **fait 2026-04-30** : 6 SVG ajoutés dans les corrections (tableau 6×6 des sommes de 2 dés Ex 13 ; courbe convergence loi grands nombres Ex 22 ; arbre 2 niveaux fiabilité machine Ex 23 ; droites graduées intervalle fluctuation Ex 25 et Ex 27 ; arbre 2 épreuves panneaux solaires Ex 29). Ratio 19 % → 39 %.
- [x] ~~**ch13 Theoreme de Thales**~~ → **fait 2026-04-30** : 6 SVG ajoutés (ombre piquet/pylône Ex 13 ; comparaison parallèle vs non parallèle Ex 14 ; configuration papillon avec longueurs Ex 15 ; triangle Thalès complet Ex 19 ; triangle équation x résolue Ex 23 ; triangle problème 2 étapes Ex 22). Ratio 18 % → 31 %.
- [x] ~~**ch03 Indicateurs statistiques**~~ → **fait 2026-05-01** : 3 SVG ajoutés (comparaison étendues Ex 5, boîte à moustaches Q1/Me/Q3/IQR Ex 4, distribution + fuseau ±σ Ex 7). Ratio 20 % → 30 %.
- [x] ~~**ch07 Notion de fonction**~~ → **fait 2026-05-01** : 5 SVG ajoutés (graphe C(x)=8x+20 avec antécédents Ex 11, flèches ensembles image/antécédent Ex 6, lecture graphique vert/rouge Ex 7, facture eau Ex 9, E(t)=2t Ex 16). Ratio 12 % → 25 %.
- [x] ~~**ch08 Fonction lineaire**~~ → **fait 2026-05-01** : 1 SVG ajouté (droite f(x)=5x avec lecture antécédents y=30 → x=6 et y=15 → x=3, Ex 13).
- [x] ~~**ch10 Fonction carre**~~ → **fait 2026-05-01** : 5 SVG ajoutés (parabole avec variations Ex 4, résolution graphique x²=k Ex 7, comparaison aires 10/20 cm Ex 9, trajectoire ballon Ex 11, distance freinage v² Ex 14). Ratio 19 % → 30 %.
- [x] ~~**ch14 Solides et volumes**~~ → **fait 2026-05-01** : 1 SVG ajouté (agrandissement pavé en perspective 10×6×4 vs 20×12×8 montrant que V est multiplié par k³=8, Ex 5).

**PC Seconde — cible = ratio ≥ 25 %**

- [x] ~~**ch11 Transferts thermiques**~~ → **fait 2026-05-01** : 6 SVG ajoutés (3 schémas modes conduction/convection/rayonnement Ex 1 ; diagramme log des conductivités Ex 5 ; comparaison flux R panneaux bois/verre Ex 17 ; schéma atelier avant/après isolation Ex 19 ; comparaison cadre fenêtre bois/alu Ex 22 ; coupe double vitrage + R en série Ex 25). Ratio 10 % → 25 %.
- [x] ~~**ch01 Securite en laboratoire**~~ → **fait 2026-05-01** : 5 SVG ajoutés (6 EPI illustrés Ex 2 ; échelle des niveaux sonores avec seuils Ex 8 ; 3 bacs de tri Ex 9 ; schéma installation électrique disjoncteurs Ex 14 ; tableau des 5 classes de laser Ex 17). Ratio 16 % → 31 %.
- [x] ~~**ch03 Loi d'Ohm**~~ → **fait 2026-05-01** : 5 SVG ajoutés (3 pistolets en parallèle Ex 6, 2 lampes parallèle Ex 11, choix fusible Ex 13, circuit mixte Ex 20, caractéristique non linéaire lampe Ex 19). Ratio 17 % → 31 %.
- [x] ~~**ch05 Mouvement et trajectoire**~~ → **fait 2026-05-01** : 3 SVG ajoutés (chronophotographie uniforme avec vecteurs vitesse Ex 4, piste 400 m vue de dessus Ex 11, comparaison 3 types de mouvement Ex 14). Ratio 19 % → 28 %.
- [x] ~~**ch08 Solutions chimiques**~~ → **fait 2026-05-01** : 1 SVG ajouté (échelle pH 0-14 avec gradient acide/neutre/basique et placement des produits d'atelier : décapant 2, vinaigre 3, eau 7, dégraissant 11, zones de danger pH&lt;4 et pH&gt;10, Ex 5).
- [x] ~~**ch09 Caracteristiques d'un son**~~ → **fait 2026-05-01** : 1 SVG ajouté (oscillogramme d'un diapason avec 5 oscillations sur 11,4 ms, mesure d'une période T=2,28 ms entre 2 maxima, Ex 22).
- [x] ~~**ch10 Temperature et capteurs**~~ → **fait 2026-05-01** : 4 SVG ajoutés (double échelle °C/K Ex 1, 5 températures placées Ex 8, plages capteurs Ex 11, courbe R(T) CTN Ex 14). Ratio 11 % → 30 %.
- [x] ~~**ch12 Changements d'etat**~~ → **fait 2026-05-01** : 3 SVG ajoutés (courbe T(t) 3 phases annotées Ex 3, fusion glace E=mL_f Ex 4, vaporisation eau E=mL_v Ex 5). Ratio 12 % → 23 %.
- [x] ~~**ch14 Lumiere et couleurs**~~ → **fait 2026-05-01** : 1 SVG ajouté (spectre visible 380-780 nm avec gradient de couleur, 6 couleurs placées violet/bleu/vert/jaune/orange/rouge, zones UV/IR invisibles, Ex 7).

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

- **2026-05-01** : **Phase 4 (visuels) — clôture vague 4 (6 derniers chapitres)**. (11) `maths/seconde/ch03/exercices.html` (Indicateurs stats) — 3 SVG : comparaison étendue 2 séries A/B (groupé vs dispersé) Ex 5 ; boîte à moustaches Q1=19/Me=26,5/Q3=36,5 + IQR=17,5 Ex 4 ; distribution autour moyenne 137 kWh avec fuseau ±σ=12,3 Ex 7. Ratio 20 % → 30 %. (12) `maths/seconde/ch08/exercices.html` (Fonction linéaire) — 1 SVG : droite f(x)=5x avec lecture antécédents y=30 → x=6 et y=15 → x=3, Ex 13. (13) `maths/seconde/ch14/exercices.html` (Solides) — 1 SVG : agrandissement pavé en perspective k=2 avec V=240→1920 cm³, Ex 5. (14) `physique-chimie/seconde/ch08/exercices.html` (Solutions) — 1 SVG : échelle pH 0-14 colorée avec produits d'atelier placés et zones danger Ex 5. (15) `physique-chimie/seconde/ch09/exercices.html` (Son) — 1 SVG : oscillogramme diapason 5 oscillations sur 11,4 ms avec mesure période T=2,28 ms Ex 22. (16) `physique-chimie/seconde/ch14/exercices.html` (Lumière) — 1 SVG : spectre visible 380-780 nm avec 6 couleurs placées et zones UV/IR Ex 7. **Phase 4 du plan d'amélioration Seconde maintenant complète : 15/15 chapitres traités.**
- **2026-05-01** : **Phase 4 (visuels) — 3 nouveaux chapitres traites (vague 3)**. (8) `physique-chimie/seconde/ch10/exercices.html` (Temperature et capteurs) — 4 SVG ajoutes : double echelle thermometrique Celsius/Kelvin avec 6 reperes (zero absolu, fusion eau, ambiante, etuve, ebullition) (Ex 1) ; placement de 5 temperatures sur l'echelle (azote -196, hiver -5, eau 15, corps 37, etuve 80) (Ex 8) ; plages de fonctionnement des 6 capteurs sur axe -200 a 1200 °C (Ex 11) ; courbe R(T) d'une CTN de sonde d'etuve avec seuil 8 kΩ (Ex 14). Ratio 11 % → 30 %. (9) `physique-chimie/seconde/ch12/exercices.html` (Changements d'etat) — 3 SVG ajoutes : courbe T(t) annotee avec 3 phases couleurs (montee/palier/vapeur) (Ex 3) ; schema fusion glace E=m×L_f avec etats avant/apres et calcul (Ex 4) ; schema vaporisation eau dans planche E=m×L_v (Ex 5). Ratio 12 % → 23 %. (10) `maths/seconde/ch10/exercices.html` (Fonction carre) — 5 SVG ajoutes : parabole avec tableau de variations annote (Ex 4) ; resolution graphique x²=k avec 4 droites horizontales (4 cas : 2 sols, 2 sols, 1 sol, 0 sol) (Ex 7) ; comparaison aires de cadres 10 cm vs 20 cm illustrant (2x)²=4x² (Ex 9) ; trajectoire ballon h(t)=-t²+4 avec sommet en haut (Ex 11) ; courbe d(v)=0,006v² distance freinage avec effet quadratique (Ex 14). Ratio 19 % → 30 %.
- **2026-05-01** : **Relecture critique des 33 SVG ajoutes en Phase 2 vagues 1 et 2**. 7 corrections appliquees (ch07 Ex 7/9/11, ch13 Ex 14 cas 2/Ex 15, ch04 Ex 22, ch01 Ex 8). 26 SVG verifies sans correction necessaire. Methode : recalcul des positions pixel a partir de l'echelle et confrontation aux valeurs cx/cy/x/width.
- **2026-05-01** : **Phase 4 (visuels) — 3 nouveaux chapitres traites (vague 2)**. (5) `physique-chimie/seconde/ch03/exercices.html` (Loi d'Ohm) — 5 SVG ajoutes : 3 pistolets a colle en parallele avec disjoncteur (Ex 6) ; 2 lampes 60 ohm en parallele avec lois de Kirchhoff (Ex 11) ; choix du fusible selon I (Ex 13) ; schema circuit mixte serie+parallele R1 + (R2 ∥ R3) (Ex 20) ; caracteristique U(I) non lineaire d'une lampe vs droite ohmique (Ex 19). Ratio 17 % → 31 %. (6) `maths/seconde/ch07/exercices.html` (Notion de fonction) — 5 SVG ajoutes : graphe C(x)=8x+20 avec deux droites horizontales et lecture des antecedents x=5 et x=10 (Ex 11) ; schema correspondance image/antecedent par fleches entre 2 ensembles (Ex 6) ; graphe avec lecture image (vert montant) et antecedent (rouge horizontal) (Ex 7) ; graphe facture d'eau f(x)=4x+10 avec ordonnee origine = abonnement fixe (Ex 9) ; graphe E(t)=2t avec lecture antecedent E=7 → t≈3,5 h (Ex 16). Ratio 12 % → 25 %. (7) `physique-chimie/seconde/ch05/exercices.html` (Mouvement) — 3 SVG ajoutes : chronophotographie 5 positions equidistantes avec vecteurs vitesse identiques (Ex 4) ; piste d'athletisme 400 m vue de dessus avec lignes droites (rectiligne bleu) et virages circulaires (rouge) (Ex 11) ; comparaison 3 chronophotographies uniforme/accelere/decelere (Ex 14). Ratio 19 % → 28 %.
- **2026-05-01** : **Phase 4 (visuels) — 2 nouveaux chapitres PC traites**. (3) `physique-chimie/seconde/ch11/exercices.html` (Transferts thermiques) — 6 SVG ajoutes : 3 schemas illustres conduction/convection/rayonnement avec barre chauffee, radiateur+cellules d'air, soleil+rayons (Ex 1) ; diagramme barres logarithmique des conductivites de 6 materiaux (Ex 5) ; comparaison flux 2 panneaux bois vs verre avec R (Ex 17) ; schema atelier avant/apres isolation avec fleches de flux thermique (Ex 19) ; comparaison cadre fenetre bois vs aluminium (Ex 22) ; coupe transversale double vitrage + schema equivalent R en serie (Ex 25). Ratio 10 % → 25 %. (4) `physique-chimie/seconde/ch01/exercices.html` (Securite) — 5 SVG ajoutes : 6 pictogrammes EPI illustres (lunettes, masque, gants, casque, chaussures, tablier) avec libelles et codes couleurs ISO (Ex 2) ; echelle des niveaux sonores 0-130 dB avec seuils 85 dB et 120 dB et placement des machines d'atelier (Ex 8) ; 3 bacs de tri DDS rouge / recyclage jaune / ordures gris (Ex 9) ; schema installation electrique compteur+DJ general+DDR+DJ prise+meuleuse (Ex 14) ; tableau des 5 classes de laser de classe 1 a classe 4 avec progression du danger (Ex 17). Ratio 16 % → 31 %.
- **2026-04-30** : **Phase 4 (visuels) — 2 nouveaux chapitres traites**. (1) `maths/seconde/ch04/exercices.html` (Probabilites) — 6 SVG ajoutes dans les corrections : tableau 6×6 des sommes de 2 des (Ex 13), courbe de convergence loi des grands nombres (Ex 22), arbre 2 niveaux fiabilite machine (Ex 23), droites graduees intervalle de fluctuation panneaux et piece truquee (Ex 25 et 27), arbre 2 epreuves panneaux solaires (Ex 29). Ratio 19 % → 39 %. (2) `maths/seconde/ch13/exercices.html` (Thales) — 6 SVG ajoutes : ombre piquet/pylone avec rayons solaires (Ex 13), comparaison cas parallele/non parallele (Ex 14), configuration papillon (Ex 15), triangle Thales direct (Ex 19), triangle equation x resolue (Ex 23), triangle probleme 2 etapes (Ex 22). Ratio 18 % → 31 %. Timestamps mis a jour.
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
| Phase 4 — Visuels dans exercices | **Complète** (15/15 chapitres : maths ch03, ch04, ch06, ch07, ch08, ch10, ch13, ch14 + PC ch01, ch03, ch05, ch08, ch09, ch10, ch11, ch12, ch14) | 2026-04-22 | 2026-05-01 |
