# Audit Pedagogique Global

**Date** : 2026-03-16
**Derniere mise a jour** : 2026-03-19 (bilan Seconde)
**Perimetre** : qualite des cours, clarte pedagogique, coherence inter-niveaux, progression 2nde-1ere-Tle, exemples, contextes professionnels
**Methode** : lecture integrale ou partielle de 50+ fichiers lecon.html, analyses statistiques CSS, comparaison inter-sections
**Rapports detailles** : `audit-pedagogique-maths.md`, `audit-pedagogique-pc.md`

---

## Resume executif

Le site presente une **qualite pedagogique globalement bonne** (note moyenne 4/5) avec des points d'excellence (maths Seconde, PC 1ere ICCER, PC Tle ICCER) et des zones a ameliorer (maths Premiere avec 2 chapitres stubs, PC Tle ERA avec peu de guidage methodologique). La progression inter-niveaux est coherente et bien calibree dans toutes les disciplines. Les contextes professionnels respectent parfaitement la regle d'interdiction des sigles de filiere.

### Notes par section

| Section | Note | Cours complets | Points cles |
|---|---|---|---|
| **Maths Seconde** | 4/5 | 14/14 (100%) | Excellentes animations, CSS ancien dans ch02-ch05 |
| **Maths Premiere** | 4/5 | 9/9 (100%) | ch05 et ch09 redigés (2026-03-16), diff. ajoutee |
| **Maths Terminale** | 4/5 | 11/11 (100%) | Programme complementaire complet, double contexte ICCER/ERA |
| **PC Seconde** | 4/5 | 14/14 (100%) | SVG de qualite, redefinitions CSS inline |
| **PC 1ere ICCER** | 4.5/5 | 10/10 (100%) | Situations pro exemplaires, labels inconsistants |
| **PC 1ere ERA** | 4/5 | 10/10 (100%) | Contextes menuiserie parfaits, moins de `.meth` |
| **PC Tle ICCER** | 4.5/5 | 8/8 (100%) | Niveau scientifique eleve, interactivite |
| **PC Tle ERA** | 4/5 | 8/8 (100%) | `.appli`→`.situation` corrige, `.meth` ajoutes (ch01-ch08) |
| **Moyenne** | **4.1/5** | **84/84 (100%)** | |

---

## 1. Qualite des cours

### Points forts globaux

1. **Structure pedagogique coherente** : la majorite des cours suivent le schema situation pro → objectifs → definitions → proprietes → methodes → exemples → a retenir. Les classes CSS `.def`, `.prop`, `.att`, `.meth`, `.retenir`, `.ex`, `.situation` sont utilisees de maniere cohérente.

2. **Richesse des illustrations** : SVG inline pour les schemas (circuits, forces, spectres), Chart.js pour les graphiques interactifs, Canvas pour les animations. Les cours de Seconde (maths et PC) sont particulierement riches.

3. **Exercices de verification integres** : la plupart des cours incluent des mini-exercices corriges avec `<details>` et le bouton `.bc`. Exceptions : PC 1ere ICCER (0 exercices dans les lecons) et maths Terminale (exercices principalement dans exercices.html).

4. **Erreurs frequentes bien anticipees** : les blocs `.att` identifient les confusions courantes (ex : pourcentages qui ne s'additionnent pas, f(a+b) != f(a)+f(b), confusion masse/poids).

### Chapitres a ameliorer en priorite

| Chapitre | Probleme | Priorite |
|---|---|---|
| `maths/premiere/ch05` | **Stub vide** — Polynomes degre 2 (discriminant, forme canonique) | CRITIQUE |
| `maths/premiere/ch09` | **Stub vide** — Trigonometrie (cos, sin, tan) | CRITIQUE |
| `maths/seconde/ch02` | Incomplet (renvoie vers ch03), classes CSS non-standard | HAUTE |
| `maths/seconde/ch03` | Container non-standard, classes CSS non-standard | HAUTE |
| ~~Tous les chapitres `PC Tle ERA`~~ | ~~Seulement 4 blocs `.meth` sur 8 chapitres~~ — **CORRIGE** (2+ par chapitre) | ~~MOYENNE~~ |

---

## 1b. Nouvelles ressources : QCM et interrogations (2026-03-18)

**Decision prise** : chaque chapitre proposera 6 types de pages (au lieu de 3). Deux nouveaux types differencies :

| Ressource | Role | Differenciation | Specs |
|---|---|---|---|
| `qcm.html` | Auto-evaluation interactive | Oui — 3 series de 15 questions (socle/standard/appro) via diff.js | `prompts/prompt-qcm-interro.md` |
| `interro.html` | Diagnostic rapide (10-15 min) | Oui — 3 sujets de 5-8 questions (socle/standard/appro) via diff.js | `prompts/prompt-qcm-interro.md` |

**Strategie de differenciation QCM :**
- **Socle** : questions directes, vocabulaire simple, reconnaissance, calculs elementaires
- **Standard** : questions programme, application de formules, contextes pro
- **Appro** : raisonnement, croisement de notions, vocabulaire BTS

**Strategie de differenciation interro :**
- **Socle** : exercices guides, calculs amorces, tableaux pre-remplis, rappels methode
- **Standard** : consignes completes, redaction attendue, contextes pro
- **Appro** : problemes ouverts, mise en equation autonome, questions type BTS

**Adaptation par matiere :**
- Maths : calcul mental, lecture graphique, reconnaissance de formules
- PC : unites, schemas, protocoles, vocabulaire scientifique, conversions

**Couverture actuelle** : 48 QCMs sur 84 chapitres (57%) + 30 interros sur 84 chapitres (36%). Sections QCM complètes : maths/seconde (14/14), maths/premiere (9/9), maths/terminale (11/11), PC seconde (14/14). Restant QCM : PC 1ere ICCER (0/10), PC 1ere ERA (0/10), PC Tle ICCER (0/8), PC Tle ERA (0/8). Sections interro complètes : maths/seconde (14/14), PC seconde (14/14). Restant interro : maths/premiere 0/9, maths/terminale 2/11, PC 1ere ICCER 0/10, PC 1ere ERA 0/10, PC Tle ICCER 0/8, PC Tle ERA 0/8.

---

## 2. Clarte pedagogique

### Notions bien expliquees

- **Statistiques** (toute la filiere) : progression exemplaire de la stat 1 variable (2nde) a la regression non lineaire (Tle)
- **Suites** (maths 1ere → Tle) : introduction claire, exemples concrets, progression naturelle
- **Derivation** (maths 1ere ch06) : bien structure malgre l'absence de graphique de tangente
- **Combustion** (PC 1ere) : ancrage parfait pour les deux filieres
- **Oxydoreduction** (PC Tle) : schema SVG du transfert d'electrons, methode pas-a-pas

### Notions a ameliorer

| Notion | Chapitre | Probleme |
|---|---|---|
| Polynomes degre 2 | maths/premiere/ch05 | **Absent** — chapitre stub |
| Trigonometrie | maths/premiere/ch09 | **Absent** — chapitre stub |
| ~~Resolution graphique~~ | ~~maths/premiere/ch04~~ | ~~Pas de graphique interactif~~ — **CORRIGE** (2026-03-16) |
| Geometrie dans l'espace | maths/premiere/ch07 | Pas de visualisation 3D |
| ~~Derivee (tangente)~~ | ~~maths/premiere/ch06~~ | ~~Pas d'animation tangente glissante~~ — **CORRIGE** (2026-03-16) |
| ~~Suites (representation)~~ | ~~maths/premiere/ch03~~ | ~~Pas de graphique Chart.js~~ — **CORRIGE** (2026-03-16) |

---

## 3. Coherence entre les niveaux

### Mathematiques

| Theme | 2nde | 1ere | Tle | Verdict |
|---|---|---|---|---|
| Statistiques | ch02-03 (1 var) | ch01 (2 var, regression) | ch01 (ajust. non lineaire) | Excellent |
| Fonctions | ch07-10 (notion, lineaire, affine, carree) | ch04-06 (graphique, **deg 2 ABSENT**, derivee) | ch04-05, ch08-09 (deg 3, expo/log, integrale) | **Trou en 1ere** (ch05 stub) |
| Geometrie | ch11-14 (Pythagore, Thales, solides) | ch07-09 (espace, vecteurs, **trigo ABSENT**) | ch06-07, ch11 (vecteurs, trigo, scalaire) | **Trou en 1ere** (ch09 stub) |
| Suites | — | ch03 (arithmetiques, geometriques) | ch03 (geometriques approfondies) | Excellent |
| Probabilites | ch04 | ch02 (conditionnelles) | ch02 (arbres, independance) | Bon |

### Physique-Chimie

| Theme | 2nde | 1ere | Tle | Verdict |
|---|---|---|---|---|
| Electricite | ch02-04 (U, I, Ohm, alternatif) | ch01-02 (P, E, transport HT) | ICCER: cos phi, moteur / ERA: transport, stockage | Excellent |
| Thermique | ch10-12 (T, transferts, changements d'etat) | ch04 (3 modes) + ERA ch05 (minimiser) | ch04/03 (rayonnement, Wien, GES) | Excellent |
| Mecanique | ch05-06 (mouvement, forces) | ch05-08 (v, a, moments, pression, Archimede) | ICCER: fluides (Pascal, debit) | Bon |
| Chimie | ch07-08 (atome, solutions) | ch03 (combustion) + ch08/09 (titrage) | ch07/05 (oxydoreduction) | Bon |
| Signaux | ch09, ch13-14 (son, lumiere) | ch09/10 (ondes EM, son) | ICCER: son / ERA: lumiere, info, attenuation | Bon |

**Bilan** : la progression est logique et bien calibree en physique-chimie. En mathematiques, les 2 chapitres stubs de Premiere creent des trous dans la progression fonctions et geometrie.

---

## 4. Qualite des exemples

### Points forts
- **Variete** : les exemples couvrent des contextes professionnels, quotidiens et scientifiques
- **Pertinence** : les exemples numeriques sont realistes et verifies
- **Progressivite** : dans un meme chapitre, les exemples vont du simple au complexe

### Points faibles
- **Premiere maths** : moins d'exemples interactifs que la Seconde (pas de Chart.js dans 7 chapitres sur 9)
- **Terminale ERA** : exemples corrects mais moins detailles que ICCER
- **Seconde PC** : les contextes sont essentiellement menuiserie — pourrait beneficier de plus de diversite (sport, sante, environnement)

---

## 5. Contextes professionnels

### Respect de la regle "pas de sigles dans le contenu"

**CONFORME** — Aucune occurrence de :
- "technicien ICCER", "technicien ERA", "technicien ERA-MA", "technicien MAMA"
- "Contexte ERA-MA", "Application ICCER", "Exemple ERA-MA"

Les sigles sont correctement limites aux `<title>`, `<h1>`, `<p class="sous-titre">`, liens de retour et badges.

### Metiers reels utilises

| Filiere | Metiers trouves | Conforme |
|---|---|---|
| ICCER | technicien chauffagiste, technicienne chauffagiste, installateur thermique, plombier chauffagiste, technicienne de maintenance energetique | OUI |
| ERA | menuisier agenceur, ebeniste, menuisier metallier, charpentier-menuisier, fabricant de meubles, installateur d'agencement | OUI |
| Seconde | menuisier, metreur, artisan menuisier | OUI |

### Coherence ICCER / ERA

Les modules communs (combustion, transferts thermiques, moments, pression, solutions, oxydoreduction) sont traites avec un **contenu scientifique identique** mais des **exemples adaptes a chaque filiere** :
- ICCER : chaudiere, climatiseur, ballon ECS, circuit hydraulique, anode sacrificielle
- ERA : defonceuse, scie, presse hydraulique, double vitrage, isolation phonique, garde-corps

**Bilan** : differenciation des contextes pro reussie.

---

## 6. Coherence CSS des classes pedagogiques

### Utilisation des classes standards

| Section | .def | .prop | .att | .meth | .retenir | .ex | .exo | .situation |
|---|---|---|---|---|---|---|---|---|
| Maths 2nde | Oui (sauf ch02-05) | Oui | Oui | Oui | Oui | Oui | Oui | Oui |
| Maths 1ere | Oui | Oui | Partiel | Oui | Oui | Oui | Oui | Oui |
| Maths Tle | Oui | Oui | Oui | Oui | Oui | Oui | Oui | Oui |
| PC 2nde | Oui | Oui | Oui | Oui | Oui | Oui | Oui (inline) | Non (0) |
| PC 1ere ICCER | Oui | Oui | Oui | Oui | Oui | Oui | Non (0) | Partiel (situation-pro) |
| PC 1ere ERA | Oui | Oui | Oui | Partiel (10) | Oui | Oui | Oui (20) | Oui (14) |
| PC Tle ICCER | Oui | Oui | Oui | Oui (23) | Oui | Oui | Oui (36) | Oui |
| PC Tle ERA | Oui | Oui | Oui | **Faible (4)** | Oui | Oui | Oui | **Non (.appli)** |

### Problemes CSS identifies

1. **maths/seconde ch02-ch05** : classes non-standard (`def-box`, `exemple`, `methode`, `attention`, `container`)
2. **PC seconde (14 fichiers)** : redefinition inline de `.exo .exo-num` et `details.corr`
3. **PC 1ere ICCER (10 fichiers)** : `label-def` au lieu de `label label-def`
4. **PC 1ere ERA (5 fichiers)** : format de labels mixte
5. **PC Tle ERA (8 fichiers)** : `class="appli"` au lieu de `class="situation"`
6. **PC 1ere ICCER (7 fichiers)** : `class="situation-pro"` au lieu de `class="situation"`

---

## Problemes identifies (synthese hierarchisee)

### Priorite CRITIQUE

1. **Chapitres stubs en maths/premiere** : ch05 (Polynomes degre 2) et ch09 (Trigonometrie) sont vides. Ce sont des chapitres fondamentaux qui creent des trous dans la progression vers la Terminale.

### Priorite HAUTE

2. **Differenciation absente en maths/premiere** : 18 fichiers (exercices.html + ds.html) sans diff.js ni classes de differenciation.

3. **Classes CSS non-standard en maths/seconde ch02-ch05** : `def-box` au lieu de `def`, `exemple` au lieu de `ex`, `container` au lieu de `c`.

4. **Redefinitions CSS inline en PC seconde** : 14 fichiers redefinissent des classes de `styles.css`.

5. **Labels inconsistants en PC 1ere ICCER** : `label-def` (classe unique) au lieu de `label label-def` (10 fichiers).

6. **Classe `.appli` en PC Tle ERA** : 8 fichiers utilisent `.appli` au lieu de `.situation` (28 occurrences).

### Priorite MOYENNE

7. ~~**PC Tle ERA : faible guidage methodologique**~~ : **CORRIGE** — `.meth` ajoutes dans les 8 chapitres (2+ par chapitre).

8. **Maths 1ere : pas de visualisations interactives** : contrairement a la Seconde, les chapitres 1ere n'ont quasiment pas de Chart.js, SVG ou Canvas.

9. ~~**Maths 1ere ch06**~~ : **CORRIGE** — animation tangente glissante ajoutee (Canvas interactif).

10. **PC 1ere ICCER** : `class="situation-pro"` au lieu de `class="situation"` dans 7 fichiers.

11. **PC seconde ch12** : lien retour incorrect vers `index.html` au lieu de `pc-2nde-pro.html`.

12. **PC seconde ch04-ch05** : labels places hors des blocs `.def`.

### Priorite BASSE

13. **Titres `<title>` inconsistants** dans toutes les sections (format variable).

14. **Maths seconde** : badges de niveaux heterogenes (`badge-niv badge-1` vs `badge badge-green`).

15. ~~**Maths terminale** : entites HTML (`&ndash;`, `&eacute;`) au lieu de caracteres UTF-8 dans certains titres.~~ — **CORRIGE 2026-03-16** (44 fichiers, 6 041 entites)

16. **PC seconde** : pas de classe `.situation` (0 occurrences) — contextes pro non balises.

17. **PC 1ere ICCER** : pas de mini-exercices dans les lecons (0 `.exo`).

---

## Corrections realisees

- **2026-03-16** : Remplace `class="appli"` par `class="situation"` dans les 8 fichiers `physique-chimie/terminale-era` (28 occurrences)
- **2026-03-16** : Remplace `class="situation-pro"` par `class="situation"` dans les 7 fichiers `physique-chimie/premiere-iccer`
- **2026-03-16** : Uniformise `label-def/prop/att/meth` en `label label-def/prop/att/meth` dans 17 fichiers `physique-chimie/premiere-iccer` (119 occurrences)
- **2026-03-16** : Corrige le lien retour de `physique-chimie/seconde/ch12/lecon.html` et `fiche.html` (index.html → pc-2nde-pro.html)
- **2026-03-16** : Converti 6 041 entites HTML en UTF-8 dans les 44 fichiers de maths/terminale
- **2026-03-16** : Harmonise CSS maths/seconde/ch02-ch05 (def-box→def, exemple→ex, container→c, methode→meth)
- **2026-03-16** : Supprime redefinitions CSS inline dans 28 fichiers physique-chimie/seconde (centralise dans styles.css)
- **2026-03-16** : Ajoute diff.js dans 18 fichiers maths/premiere (exercices.html + ds.html)
- **2026-03-16** : Corrige le lien retour de physique-chimie/seconde/ch13/lecon.html (index.html → pc-2nde-pro.html)
- **2026-03-16** : Ajoute blocs `.meth` dans PC terminale-era ch07 et ch08 (2 par chapitre, total 8 chapitres couverts)
- **2026-03-16** : Ajoute animation tangente glissante interactive dans maths/premiere/ch06 (Canvas)
- **2026-03-16** : Uniformise labels dans PC premiere-era ch06-ch10 (`label-def` → `label label-def`)
- **2026-03-16** : Corrige CLAUDE.md : terminale-iccer ch01..ch08 (et non ch11)
- **2026-03-19** : Bilan Seconde — la Seconde est confirmee comme section modele du site : 28/28 chapitres avec 6 types de pages (170 fichiers), differenciation systematique (337 blocs diff-* equilibres), 32 simulations interactives, 100% conformite programme. Reste a ameliorer : corrections PC Seconde (29.9%), ajout `.situation` en PC Seconde, CSS residuel ch02-ch05

---

## Ameliorations restantes

### Priorite critique
- [x] Rediger `maths/premiere/ch05/lecon.html` (Polynomes degre 2) (2026-03-16)
- [x] Rediger `maths/premiere/ch09/lecon.html` (Trigonometrie) (2026-03-16)

### Priorite haute
- [x] Ajouter diff.js et differenciation dans `maths/premiere` (18 fichiers exercices + ds) (2026-03-16)
- [x] Harmoniser CSS de `maths/seconde/ch02-ch05` (def-box → def, exemple → ex, etc.) (2026-03-16)
- [x] Supprimer redefinitions CSS inline dans les 14 fichiers `physique-chimie/seconde` (2026-03-16)
- [x] Uniformiser labels en `label label-def` dans les 17 fichiers `premiere-iccer` (2026-03-16)
- [x] Remplacer `class="appli"` par `class="situation"` dans les 8 fichiers `terminale-era` (2026-03-16)

### Priorite moyenne
- [x] Ajouter des blocs `.meth` dans les chapitres `terminale-era` (objectif : 2+ par chapitre) (2026-03-16)
- [x] Ajouter visualisations interactives en `maths/premiere` (Chart.js pour ch03 suites, ch04 graphique, ch06 tangente) (2026-03-16)
- [x] Remplacer `class="situation-pro"` par `class="situation"` dans les 7 fichiers `premiere-iccer` (2026-03-16)
- [x] Corriger lien retour de `physique-chimie/seconde/ch12/lecon.html` (2026-03-16)
- [x] Corriger placement des labels dans `seconde/ch04` et `seconde/ch05` (2026-03-16)
- [x] Uniformiser les labels dans les 5 fichiers `premiere-era` concernes (2026-03-16)

### Priorite haute (uniformisation 2026-03-18)
- [ ] Creer les 36 `qcm.html` restants (PC 1ere ICCER 10, PC 1ere ERA 10, PC Tle ICCER 8, PC Tle ERA 8) — 48/84 faits
- [ ] Creer les 54 `interro.html` restants (30/84 faits : Seconde 28 + Terminale 2)
- [ ] Centraliser les classes CSS QCM dans `styles.css` (prerequis)

### Priorite basse
- [ ] Uniformiser le format des `<title>` dans toutes les sections
- [ ] Harmoniser badges de niveaux dans mini-exercices `maths/seconde`
- [x] Convertir entites HTML en UTF-8 dans maths/terminale (44 fichiers, 6 041 entites) (2026-03-16)
- [ ] Ajouter `.situation` aux contextes pro existants en `physique-chimie/seconde`
- [ ] Ajouter mini-exercices dans les lecons de `premiere-iccer`
- [ ] Enrichir situations pro de `terminale-era` (personnages, scenarios)
- [ ] Diversifier les contextes en Seconde (sport, sante, environnement)
- [ ] Ajouter sections "Erreurs frequentes" dans cours `maths/premiere`
