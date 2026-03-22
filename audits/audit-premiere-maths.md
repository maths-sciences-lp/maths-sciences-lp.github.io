# Audit complet — Mathématiques Première Bac Pro

**Date** : 2026-03-22
**Dernière mise à jour** : 2026-03-22 (v2 — après corrections priorités hautes)
**Périmètre** : Tous les fichiers de `maths/premiere/` (ch01 à ch09)
**Méthode** : Lecture intégrale de tous les fichiers, audit structurel, pédagogique et technique

---

## Vue d'ensemble

| Indicateur | Valeur |
|---|---|
| Chapitres | 9 (ch01 à ch09) |
| Fichiers attendus (6 par chapitre) | 54 |
| Fichiers présents | **54 / 54 (100 %)** |
| Fichiers stubs / vides | **0** |
| Note globale | **4 / 5** |

### Couverture par type de fichier

| Type | Présent | Contenu réel | Différenciation |
|---|---|---|---|
| `lecon.html` | 9/9 ✅ | 9/9 ✅ | N/A (pas de diff sur les cours) |
| `exercices.html` | 9/9 ✅ | 9/9 ✅ | ✅ 9/9 (socle/standard/appro) |
| `ds.html` | 9/9 ✅ | 9/9 ✅ | ✅ 9/9 (socle/standard/appro) |
| `fiche.html` | 9/9 ✅ | 9/9 ✅ | N/A |
| `qcm.html` | 9/9 ✅ | 9/9 ✅ | ✅ 9/9 (3 niveaux, 45 questions) |
| `interro.html` | 9/9 ✅ | 9/9 ✅ | ✅ 9/9 (3 niveaux, /20) |

---

## Chapitres — Détail

| Ch | Titre | Module | lecon | exo | ds | fiche | qcm | interro |
|---|---|---|---|---|---|---|---|---|
| 01 | Statistique à deux variables | Stat & Probas | ✅ 22 Ko | ✅ 24 Ko | ✅ 9,6 Ko | ✅ 7,8 Ko | ✅ 43 Ko | ✅ 19 Ko |
| 02 | Probabilités | Stat & Probas | ✅ 21 Ko | ✅ 25 Ko | ✅ 15 Ko | ✅ 7,1 Ko | ✅ 38 Ko | ✅ 18 Ko |
| 03 | Suites numériques | Algèbre-Analyse | ✅ 24 Ko | ✅ 19 Ko | ✅ 9,8 Ko | ✅ 7,6 Ko | ✅ 39 Ko | ✅ 17 Ko |
| 04 | Résolution graphique d'équations | Algèbre-Analyse | ✅ 35 Ko | ✅ 27 Ko | ✅ 11 Ko | ✅ 8,1 Ko | ✅ 43 Ko | ✅ 18 Ko |
| 05 | Fonctions polynômes de degré 2 | Algèbre-Analyse | ✅ 48 Ko | ✅ 16 Ko | ✅ 11 Ko | ✅ 6,3 Ko | ✅ 38 Ko | ✅ 18 Ko |
| 06 | Fonction dérivée et variations | Algèbre-Analyse | ✅ 26 Ko | ✅ 17 Ko | ✅ 9,9 Ko | ✅ 8,1 Ko | ✅ 38 Ko | ✅ 15 Ko |
| 07 | Géométrie dans l'espace | Géométrie | ✅ 29 Ko | ✅ 15 Ko | ✅ 11 Ko | ✅ 8,0 Ko | ✅ 39 Ko | ✅ 14 Ko |
| 08 | Vecteurs du plan | Géométrie | ✅ 19 Ko | ✅ 15 Ko | ✅ 9,2 Ko | ✅ 7,3 Ko | ✅ 41 Ko | ✅ 15 Ko |
| 09 | Trigonométrie | Géométrie | ✅ 40 Ko | ✅ 39 Ko | ✅ 15 Ko | ✅ 9,1 Ko | ✅ 43 Ko | ✅ 16 Ko |

---

## Points forts

### 1. Structure complète et homogène
Tous les 9 chapitres contiennent les 6 fichiers requis avec du contenu substantiel. Aucun stub, aucun placeholder. C'est la section la plus complète en termes de couverture de fichiers.

### 2. Cours de très bonne qualité
- Progression pédagogique claire : situation professionnelle → définitions → propriétés → méthodes → exemples → exercices → synthèse
- Utilisation correcte et cohérente des classes CSS : `.def`, `.prop`, `.att`, `.meth`, `.retenir`, `.ex`, `.exo`, `.situation`, `.formule-box`
- CSS inline minimal (1 ligne `:root` dans la majorité des fichiers)
- ch03 (Suites), ch05 (Polynômes degré 2) et ch09 (Trigonométrie) sont particulièrement riches

### 3. Contextes professionnels conformes
- Métiers réels utilisés : menuisier agenceur, artisan charpentier, installateur thermique, technicien chauffagiste, ébéniste
- **0 sigle de filière** (ICCER, ERA, MAMA) dans le contenu pédagogique — conforme aux règles
- Variété des contextes : professionnel, quotidien, scientifique

### 4. QCM et interrogations exemplaires
- 45 questions par QCM, réparties en 3 niveaux (15 socle + 15 standard + 15 approfondissement)
- Toutes les interrogations ont un barème /20, 3 niveaux différenciés, et des corrections complètes
- JavaScript embarqué pour les QCM avec scoring automatique et feedback coloré

### 5. Fiches de révision uniformes
- 9/9 fiches suivent le même modèle de grille de cartes (`.fiche-grid`, `.fiche-card`)
- Contenu concis avec formules clés, astuces (`.astuce`) et pièges (`.piege`)
- Support impression inclus

### 6. Thème couleur cohérent
Tous les fichiers utilisent le thème Première Pro : `--p:#0969da; --p-bg:#dbeafe; --p-border:#93c5fd`

---

## Problemes identifies

### ~~1. Différenciation absente dans exercices.html~~ — CORRIGÉ 2026-03-22

~~8 chapitres sur 9 n'implémentaient pas la différenciation.~~ → **Corrigé** : les 9 chapitres ont maintenant les balises `diff-socle`, `diff-standard`, `diff-appro` avec des exercices guidés (socle), des exercices standard intermédiaires (créés pour ch02-ch08), et des exercices avancés (appro).

### ~~2. Différenciation absente dans ds.html~~ — CORRIGÉ 2026-03-22

~~Aucun des 9 DS n'implémentait la différenciation.~~ → **Corrigé** : les 9 DS ont maintenant 3 versions (socle guidée /20, standard /20, approfondissement BTS /20) avec corrections complètes.

### 3. Simulations manquantes — 3 chapitres non couverts (gravité : MOYENNE)

| Chapitre | Simulation liée | Commentaire |
|---|---|---|
| ch01 | ✅ simulations/stats-2var.html | OK |
| ch02 | ✅ simulations/probabilites.html | Lien ajouté 2026-03-22 |
| ch03 | ✅ simulations/suites.html | OK |
| ch04 | ✅ simulations/graphe-equation.html | OK |
| ch05 | ✅ simulations/derivee.html | OK (partagée avec ch06) |
| ch06 | ✅ simulations/derivee.html | OK |
| ch07 | ✅ simulations/solides.html | Lien ajouté 2026-03-22 |
| ch08 | ✅ simulations/vecteurs.html | Lien ajouté 2026-03-22 |
| ch09 | ✅ simulations/trigonometrie.html | OK |

**~~Chapitres sans simulation~~** — CORRIGÉ 2026-03-22 : les simulations existaient déjà, les liens ont été ajoutés aux leçons.

### 4. Page sommaire : simulation manquante dans l'index (gravité : BASSE)

La page `maths-1ere-pro.html` (sommaire) est complète avec les 9 chapitres et les 6 liens par chapitre (cours, exercices, DS, fiche, QCM, interro). Aucun lien cassé détecté (54/54 fichiers existent).

Cependant, l'index des simulations (`simulations.html`) ne référence qu'**1 simulation** explicitement liée à Maths Première (ch06 — Dérivée), alors que 6 chapitres ont des simulations liées.

### 5. Mini-exercices absents dans certains cours (gravité : MOYENNE)

Certains cours n'intègrent pas de mini-exercices corrigés dans le corps de la leçon :

| Chapitre | Mini-exercices dans lecon.html |
|---|---|
| ch01 | ❌ Aucun |
| ch02 | ✅ 5 mini-exercices |
| ch03 | ✅ 6 mini-exercices |
| ch04 | ❌ Aucun |
| ch05 | ❌ Aucun |
| ch06 | ✅ 5 mini-exercices |
| ch07 | ⚠ 2 mini-exercices (sans bouton de correction) |
| ch08 | ✅ 5 mini-exercices |
| ch09 | ❌ Aucun |

**Chapitres sans mini-exercices** : ch01, ch04, ch05, ch09

### 6. Exercices : système de niveaux hétérogène (gravité : MOYENNE)

Les exercices.html de ch01 à ch08 utilisent un système de **niveau-header** (niv1/niv2/niv3/niv4) au lieu des balises `diff-socle/diff-standard/diff-appro` requises par le CLAUDE.md. Seul ch09 utilise le système conforme. Les deux systèmes coexistent, ce qui crée une incohérence.

### 7. Blocs `.att` peu présents dans les cours (gravité : BASSE)

Contrairement aux cours de Seconde qui utilisent systématiquement les blocs d'attention aux erreurs fréquentes, seuls quelques chapitres de Première en ont :
- ch01 : 3 blocs `.att`
- ch02 : 1 bloc `.att` (événements non incompatibles)
- ch03 : 1 bloc `.att` (ne pas confondre arithmétique/géométrique)
- ch05 : 3 blocs `.att`
- ch08 : 1 bloc `.att` (ordre des lettres dans un vecteur)

---

## Corrections realisees

- **2026-03-22** : Chapitres ch05 (Fonctions polynômes degré 2) et ch09 (Trigonométrie) — cours complets (anciennement stubs vides, signalés dans l'audit du 2026-03-16)
- **2026-03-22** : Création des 8 fiches manquantes (ch02 à ch09) — complétude 9/9
- **2026-03-22** : Création des 9 QCM avec différenciation 3 niveaux (45 questions chacun)
- **2026-03-22** : Création des 9 interrogations avec différenciation et barème /20
- **2026-03-22** : Ajout différenciation exercices.html (ch01-ch08) — balises diff-socle/standard/appro + exercices standard intermédiaires
- **2026-03-22** : Ajout différenciation ds.html (ch01-ch09) — versions socle guidée, standard, approfondissement BTS (/20 chacune)
- **2026-03-22** : Liaison des simulations existantes aux leçons ch02 (probabilites.html), ch07 (solides.html), ch08 (vecteurs.html)

---

## Ameliorations restantes

### Priorité haute
- [x] ~~Convertir les exercices.html de ch01-ch08 vers diff-socle/standard/appro~~ — **FAIT 2026-03-22**
- [x] ~~Ajouter la différenciation aux 9 fichiers ds.html~~ — **FAIT 2026-03-22**

### Priorité moyenne
- [x] ~~Lier simulation probabilités (ch02)~~ — **FAIT 2026-03-22** (simulation existante, lien ajouté)
- [x] ~~Lier simulation solides (ch07)~~ — **FAIT 2026-03-22** (simulation existante, lien ajouté)
- [x] ~~Lier simulation vecteurs (ch08)~~ — **FAIT 2026-03-22** (simulation existante, lien ajouté)
- [ ] Mettre à jour l'index des simulations pour référencer toutes les simulations liées à Première

### Priorité basse
- [ ] Ajouter des mini-exercices corrigés dans les leçons de ch01, ch04, ch05, ch09
- [ ] Ajouter les boutons de correction manquants dans ch07/lecon.html (2 exercices sans toggle)
- [ ] Ajouter des blocs `.att` (erreurs fréquentes) dans les cours de ch04, ch06, ch07
- [ ] Vérifier que les QCM ont des explications pédagogiquement progressives (socle < standard < appro)
- [ ] Harmoniser la numérotation des sections dans les cours (certains utilisent "I, II, III", d'autres "1, 2, 3")

---

## Conformite technique

| Vérification | Résultat |
|---|---|
| MathJax inclus | ✅ 54/54 fichiers |
| styles.css inclus | ✅ 54/54 fichiers |
| print.css inclus | ✅ 54/54 fichiers |
| nav.js inclus | ✅ 54/54 fichiers |
| diff.js (exercices + ds) | ✅ 18/18 fichiers chargent le script |
| Thème couleur correct | ✅ 54/54 fichiers |
| Wrapper `.c` correct | ✅ 54/54 fichiers |
| Pas de classes CSS redéfinies | ✅ Aucune redéfinition détectée |
| Liens cassés (sommaire) | ✅ 0 lien cassé |
| Sigles de filière dans le contenu | ✅ 0 occurrence interdite |

---

## Synthèse et recommandations

La section **Maths Première** est structurellement **complète à 100 %** avec 54 fichiers présents et fonctionnels. La qualité pédagogique est bonne à excellente pour les cours, QCM et interrogations.

**Le chantier principal restant est la différenciation** dans les exercices (8/9 chapitres) et les DS (9/9 chapitres). C'est un travail important mais systématique : réorganiser les exercices existants en 3 niveaux et ajouter les balises CSS appropriées.

**Priorité recommandée** :
1. Différencier les exercices et DS (impact pédagogique majeur)
2. Créer les 3 simulations manquantes (ch02, ch07, ch08)
3. Enrichir les cours avec des blocs `.att` et harmoniser la numérotation
