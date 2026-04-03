# Journal de bord du projet

**Site :** https://maths-sciences-lp.github.io/
**Dernière mise à jour :** 2026-04-03

---

## État actuel du site

| Indicateur | Valeur |
|---|---|
| Pages HTML totales | ~992 |
| Chapitres Bac Pro | 84 (8 fichiers/ch) |
| Chapitres CAP | 14 (4 fichiers/ch : leçon, exercices, QCM, fiche) |
| Chapitres BTS | 25 (leçons + exercices partiels) |
| Chapitres nouveaux groupements (gpt 2/4/5/6) | 14 (leçons seules) |
| Simulations interactives | 70 + 12 inline LGT |
| Automatismes | 22 pages (24 exo/page) |
| CCF LaTeX | 5 sujets + 5 corrections + 2 fiches |
| Programmes en markdown | 11/11 complets |
| Prompts de filière | 14 |

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
| Maths LGT Term spé | 15 | 2/8 (leçon + exo-cap) | 25% |

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

### Session 3 avril 2026 (fin de journée)
- **Classe CSS `.mini-exo`** ajoutée dans `styles.css` — fond `var(--p-bg)`, bordure gauche `var(--p)`, label "Application" en petites capitales
- **`prompt-cours.md`** : section "Mini exercices" remplacée par la règle complète (format, position, fréquence, interdictions, checklist)
- **`CLAUDE.md`** : règle n°9 + entrée dans le tableau des classes CSS
- **Redistribution `.mini-exo` dans 28 leçons Seconde** (14 maths + 14 PC) :
  - Exercices groupés en fin de leçon → redistribués après les définitions/méthodes correspondantes
  - Format `.exo` + `exo-num` + `toggle()` → `.mini-exo` + `.bc` + `this.nextElementSibling`
  - `<details class="corr-wrap">` → `.bc` + `.corr` (maths seconde)
  - Résultat : 2 à 7 mini-exo distribués par leçon, 0 section groupée résiduelle

### Session 3 avril 2026 (fin)
- **Diversification contextes PC Seconde** : +3 exercices sport/santé/énergie/environnement dans ch03, ch06, ch08, ch10, ch11, ch12 — ratio menuiserie réduit dans les 6 chapitres à 73–83%
- **`.situation` dans les 14 leçons PC Seconde** : 1 bloc par leçon ajouté (ch01–ch14), scénarios pro réels (menuisier, technicien, installateur)
- **Maths ch02 statistiques** : chapitre restructuré (372→561 lignes) — fréquences cumulées, tableau double entrée, histogramme ajoutés ; médiane/quartiles proprement renvoyés vers ch03
- **Erreurs fréquentes maths Seconde** : sections `.erreur-item` ajoutées dans ch02, ch03, ch09, ch10, ch11, ch12, ch13, ch14 (4–5 erreurs par chapitre)
- **Phase 2 plan-amelioration-seconde.md** : toutes les améliorations pédagogiques 2nde complètes

### Session 3 avril 2026 (suite)
- **Corrections techniques groupées 2nde MAMA** :
  - 13 titres `<title>` PC Seconde convertis en UTF-8
  - 80 fichiers PC Seconde (tous types, ch01–ch14) : 26 678 entités HTML → UTF-8
  - Labels ch04/ch05, lien ch12, badges niveaux maths → vérifiés conformes (rien à faire)
- **Audit + mise à jour problématiques** : bloc `Problématique` ajouté dans les 28 activités (14 maths + 14 PC Seconde) — critère rendu obligatoire par la mise à jour du prompt-activite.md
- **prompt-activite.md** : nouvelle section "Cohérence activité ↔ problématique (OBLIGATOIRE)" avec règles, interdictions, test de validation à 3 questions

### Session 2-3 avril 2026
- **Nouvelle section Maths Terminale générale spécialité (LGT)** : 15 chapitres complets (`maths/lgt-terminale/ch01..ch15`) — lecon.html + exercices-capacites.html pour chaque chapitre, 30 fichiers HTML créés
- Page sommaire `maths-lgt-terminale.html` + section "Lycée Général" sur `index.html`
- 16 figures SVG dans les cours LGT (géométrie, analyse, probabilités)
- 12 simulations interactives Canvas/JS intégrées dans les leçons (12/15 chapitres couverts) — +10 SVG supplémentaires ajoutés lors du renforcement de contenu (PRs #248, #250)
- Fix : liens Terminale PC manquants sur la page d'accueil
- Ajout bouton "Me contacter" (Google Form) dans la section À propos de `index.html`

### Session 1-2 avril 2026
- Sections "Erreurs fréquentes" (blocs `.erreur-item`) ajoutées dans 8 leçons maths Seconde : ch02 (statistiques), ch03 (médiane/IQR), ch09 (fonction affine), ch10 (fonction carré), ch11 (figures planes), ch12 (Pythagore), ch13 (Thalès), ch14 (solides)
- Phase 1 complète — conversion UTF-8 : ~17 000 entités HTML supprimées dans 42 fichiers PC Seconde (leçons, DS, exercices). Titres `<title>` uniformisés sur 13 leçons PC
- CLAUDE.md : règle n°9 ajoutée — UTF-8 obligatoire, entités HTML interdites sauf `&lt;` `&gt;` `&amp;` `&nbsp;`
- plan-amelioration-seconde.md : Phase 1 et Phase 2 clôturées (2026-04-02)
- Mise à jour mémoire filières (source ONISEP) : CAPs indépendants des Bac Pro 2nde, 3 Secondes pro, BTS en apprentissage, UPE2A, voie générale STI2D
- Source ajoutée dans `prompt-filiere-cap-sdg.md` (Arrêté du 16 octobre 2007)
- Copie `referentiel-cap-enseigne-signaletique-2007.pdf` dans `pdf/`
- Analyse des 3 PDFs BMA (BO n°28 du 15-7-2021 : maths, PC, épreuve)
- Copie des 3 PDFs BMA dans `pdf/` : `programme-bma-maths-2021.pdf`, `programme-bma-physique-chimie-2021.pdf`, `epreuve-bma-maths-pc-2021.pdf`
- Création 2 prompts de filière BMA : `prompt-filiere-bma-ebeniste.md`, `prompt-filiere-bma-arts-graphiques.md`
- CLAUDE.md : tableau des prompts complété (CAP MIT, CAP Ébéniste, CAP SDG, BMA Ébéniste, BMA Arts Graphiques, EEB/TGT, MEE)
- Création 2 extractions programme BMA en markdown : `programme_bma_maths.md` (9 modules, automatismes 1ère + 2ème année), `programme_bma_physique_chimie.md` (15 modules + transversaux)

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

### Priorité 5 — Section CAPLP (nouveau)
- [ ] Créer `prompts/prompt-caplp.md` (format des leçons CAPLP)
- [ ] Créer section `caplp/maths/` + `caplp/pc/`
- [ ] A.1 maths commun (~14 chapitres) — Sonnet suffisant
- [ ] A.2 maths majeure (~8 chapitres) — Opus préférable
- [ ] B.1 + B.2 PC (~30 chapitres) — après

### Priorité 6 — Améliorations continues
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
