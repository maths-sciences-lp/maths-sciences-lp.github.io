# Journal de bord du projet

**Site :** https://maths-sciences-lp.github.io/
**Dernière mise à jour :** 2026-03-31

---

## État actuel du site

| Indicateur | Valeur |
|---|---|
| Pages HTML totales | ~950 |
| Chapitres Bac Pro | 84 (8 fichiers/ch) |
| Chapitres CAP | 14 (4 fichiers/ch : leçon, exercices, QCM, fiche) |
| Chapitres BTS | 25 (leçons + exercices partiels) |
| Chapitres nouveaux groupements (gpt 2/4/5/6) | 14 (leçons seules) |
| Simulations interactives | 69 |
| Automatismes | 22 pages (24 exo/page) |
| CCF LaTeX | 5 sujets + 5 corrections + 2 fiches |
| Programmes en markdown | 9/9 complets |
| Prompts de filière | 10 |

### Couverture par section

| Section | Chapitres | Fichiers/ch | Complétion |
|---|---|---|---|
| Maths 2nde | 14 | 8/8 | 100% |
| Maths 1ère | 9 | 8/8 (sauf activité) | 88% |
| Maths Term | 11 | 8/8 | 100% |
| Maths BTS | 25 | 1-3/8 | ~30% |
| Maths CAP | 7 | 4/8 | 50% |
| PC 2nde | 14 | 8/8 | 100% |
| PC 1ère ICCER | 10 | 8/8 | 100% |
| PC 1ère ERA | 10 | 8/8 | 100% |
| PC Term ICCER | 8 | 8/8 | 100% |
| PC Term ERA | 8 | 8/8 | 100% |
| PC CAP | 7 | 4/8 | 50% |
| PC gpt 2/4/5/6 | 14 | 1/8 (leçon) | 12% |

---

## Travail réalisé

### Session 27-28 mars 2026
- Audit conformité programmes (Seconde, Première, Terminale)
- Création 9 exercices-capacités maths Première (~115 exercices)
- Fix 29 fichiers C6 hors conteneur, 41 toggle manquants, 26 data-cap→data-filtre
- Corrections erreurs scientifiques (vitesse son, indice eau, neon→sodium)
- Correction groupement B (ICCER/ERA/TMA)
- Création CCF maths (probas + polynômes) ERA-TMA + ICCER + corrections
- Création CCF PC ICCER (fluides + courant alternatif) + correction
- Création CCF PC ERA (électricité + acoustique) + correction + fiche
- 2 simulations interactives (debit-fluide.html, attenuation-sonore.html)
- CCF ERA-MA avec TP numérique acoustique

### Session 28-31 mars 2026
- Audit simulations : fix sci(0), variable morte, print.css, index
- Corrections LaTeX manquantes (ICCER maths + PC)
- Harmonisation + enrichissement 21 automatismes (15→24 exo chacun, +189 exercices)
- 19 figures SVG dans exercices PC Term ICCER (ch02, ch03, ch04, ch07)
- 68 activités de découverte créées (PC Seconde, maths 1ère, PC 1ère ICCER/ERA, PC Term ICCER/ERA)
- Fix liens cassés (6 retour sommaire, ~38 inter-chapitres Seconde)
- Création section CAP complète : 14 leçons + 14 exercices + 14 QCM + 14 fiches
- Pages sommaire CAP (maths-cap.html, pc-cap.html)
- 14 chapitres nouveaux groupements PC (gpt 2: champ magnétique, induction, triphasé; gpt 4: lentilles, image couleur, diffraction, transmission; gpt 5: pH, chimie organique, plastiques, savons, analyses; gpt 6: masse volumique, classification périodique)
- Extraction 9 programmes scolaires en markdown (Bac Pro maths 3 niveaux, PC 2nde + 1ère + Term 6 gpt, CAP maths + sciences, BTS maths)
- 7 prompts de filière (MEE, EEB/TGT, CAP MIT, CAP Ébéniste, CAP SDG + existants ICCER, ERA)
- Réorganisation page d'accueil (CAP, BTS, 6 groupements visibles)
- Mise à jour page groupements.html (liens vers chapitres existants)
- Fix corrections activités (83 fichiers onclick→toggle)
- Fix corrections CAP (7 fichiers toggle manquant)
- Bouton Imprimer sur 84 activités
- Ajout liens Activité dans 7 pages sommaire
- Fix capacité C5 manquante (ch12 Pythagore + ch13 Thalès) + 6 exercices + SVG
- SVG ajoutés dans exercices-capacités (ch01, ch03, ch05, ch06 — 8 figures)

### Session 31 mars 2026
- 15 SVG ajoutés dans exercices-capacités ch04/07/08/09/10 (arbres probas, courbes fonctions, paraboles)
- Audit exercices classiques maths Seconde : 517 exercices analysés
- Fix ch02 exercices.html : rééquilibrage appro (4→7) + 3 SVG
- Fix ch03 exercices.html : rééquilibrage appro (3→8) + 3 SVG, socle allégé (17→12)
- Fix ch09 exercices.html : +12 SVG intégrés (0→12, graphiques fonctions affines)
- **features.js** : barre de recherche (Ctrl+K), mode sombre (🌙), progression élève (✅ checkbox localStorage)
- JOURNAL.md créé (journal de bord du projet)
- 3 programmes extraits en markdown : PC 1ère 6 gpt, PC Term 6 gpt, BTS maths
- Ajout séries CAP dans nav.js (fil d'Ariane fonctionnel sur pages CAP)

---

## Prochaines priorités

### Priorité 1 — Classes de cette année (2nde MAMA, Term ICCER, Term ERA-MA)
- [x] ~~Améliorer ch02, ch03 exercices.html (appro faible)~~ ✅ fait
- [x] ~~Ajouter SVG ch09 exercices.html~~ ✅ fait (12 SVG)
- [ ] Figures SVG PC Term ERA (ch02-08, comme fait pour ICCER)

### Priorité 2 — CAP
- [ ] exercices-capacités (14 fichiers)
- [ ] DS (14 fichiers)
- [ ] Interro (14 fichiers)
- [ ] Activités (14 fichiers)

### Priorité 3 — 6 groupements PC
- [ ] Exercices pour 14 nouveaux chapitres (gpt 2/4/5/6)
- [ ] Pages sommaire par groupement (12 pages)

### Priorité 4 — BTS
- [ ] Compléter ch19-25 (exercices, DS)
- [ ] Remplir les DS vides (ch01-18)

### Priorité 5 — Améliorations continues
- [ ] Enrichir exercices Première (maths ~13/ch, PC ~9/ch)
- [ ] Automatismes PC (pas encore créés)
- [ ] Co-intervention pour toutes les filières

---

## Décisions et conventions

- **Groupements maths :** tous les Bac Pro du lycée sont en groupement B
- **Contextes pro :** mixer les filières (~25% chacune + quotidien + brut), ne pas cloisonner
- **Pas d'impression pour les simulations**
- **Bouton Imprimer sur les activités**
- **Amélioration :** ajouter, modifier OU remplacer — pas juste empiler du nouveau
- **Sigles interdits dans le contenu pédagogique** (ICCER, ERA, etc. → noms de métiers réels)
- **Un chapitre = un module** (pas de duplication entre groupements)
- **Programme en markdown** = référence obligatoire avant de créer du contenu

---

## Filières du lycée

| Formation | Sigle | Maths | PC | Sur le site |
|---|---|---|---|---|
| Bac Pro ICCER | ICCER | B | 1 | ✅ |
| Bac Pro MEE | MEE | B | 1 | ✅ (même prog) |
| Bac Pro ERA | ERA | B | 3 | ✅ |
| Bac Pro TMA | TMA | B | 3 | ✅ |
| Bac Pro EEB | EEB | B | 3 | ✅ (même prog) |
| Bac Pro Géomètre | ex-TGT | B | 6 | Leçons seules |
| CAP MIT | MIT | gpt 1 | commun | ✅ (4 fichiers/ch) |
| CAP Ébéniste | — | gpt 1 | commun | ✅ |
| CAP SDG | SDG | gpt 1 | commun | ✅ |
| BMA Ébéniste | — | — | — | ❌ |
| BMA Graphisme | — | — | — | ❌ |
| BTS MGTMN | — | — | — | Partiel |

**Classes 2025-2026 :** 2nde MAMA, Terminale ICCER, Terminale ERA-MA
