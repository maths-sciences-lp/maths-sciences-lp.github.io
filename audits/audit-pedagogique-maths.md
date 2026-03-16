# Audit Pedagogique — Mathematiques (Seconde, Premiere, Terminale)

**Date** : 2026-03-16
**Derniere mise a jour** : 2026-03-16
**Perimetre** : Qualite pedagogique des cours (lecon.html) de mathematiques
**Methode** : Lecture integrale de 5 chapitres par niveau + lecture structurelle de tous les autres

---

## Inventaire des chapitres

| Niveau | Chapitres | Cours complets | Cours stubs |
|---|---|---|---|
| **Seconde** (ch01-ch14) | 14 | 14 (100 %) | 0 |
| **Premiere** (ch01-ch09) | 9 | 7 (78 %) | 2 (ch05, ch09) |
| **Terminale** (ch01-ch11) | 11 | 11 (100 %) | 0 |
| **Total** | 34 | 32 (94 %) | 2 (6 %) |

### Chapitres stubs (contenu absent)

- `maths/premiere/ch05/lecon.html` — Fonctions polynomes de degre 2 : **squelette uniquement** ("Contenu a venir")
- `maths/premiere/ch09/lecon.html` — Trigonometrie : **squelette uniquement** ("Contenu a venir")

---

## Section 1 — Seconde (maths/seconde)

### Note globale : 4/5

### Chapitres lus integralement

| Chapitre | Sujet | Lignes | Qualite |
|---|---|---|---|
| ch01 | Proportionnalite et pourcentages | 865 | Excellent |
| ch02 | Statistiques a une variable | 349 | Bon, mais incomplet |
| ch05 | Equations du premier degre | 507 | Excellent |
| ch07 | Notion de fonction | 682 | Excellent |
| ch09 | Fonction affine | ~450 | Tres bon |
| ch12 | Theoreme de Pythagore | 427 | Excellent |

### Points forts

1. **Progression pedagogique exemplaire** : les chapitres suivent un schema clair : situation professionnelle d'introduction, definitions, methodes, exemples, exercices corriges, synthese "A retenir". C'est le cas de ch01, ch05, ch07, ch12.

2. **Richesse des illustrations interactives** : ch01 (animation y=kx, graphique Chart.js proportionnalite, graphique TVA), ch07 (animation lecture graphique, comparaison artisans, calculateur d'image), ch12 (animation theoreme de Pythagore, preuve par l'eau). Ces outils sont pedagogiquement tres pertinents.

3. **Contextes professionnels adaptes** : les metiers reels sont utilises (menuisier, metreur, poseur de parquet, ebeniste, artisan charpentier). Aucun sigle de filiere (MAMA, ERA, ICCER) n'est utilise dans le contenu pedagogique — seuls les titres et sous-titres les mentionnent. Conforme aux regles.

4. **Utilisation correcte des classes CSS pedago dans la majorite des chapitres** : `.def`, `.prop`, `.att`, `.meth`, `.retenir`, `.ex`, `.exo`, `.situation`, `.formule-box` sont utilisees dans ch01, ch05, ch07, ch09, ch10-ch14.

5. **Mini-exercices integres aux cours** : la plupart des chapitres incluent 3-5 mini-exercices corriges de niveaux progressifs dans le cours meme. Les corrections sont cachees derriere des balises `<details>`.

6. **Qualite des erreurs frequentes** : les blocs `.att` sont bien utilises pour anticiper les confusions (ex: ch01 — pourcentages ne s'additionnent pas; ch07 — confusion image/antecedent, f(a+b) != f(a)+f(b)).

### Points faibles

1. **Incoherence CSS entre chapitres anciens et recents** (PRIORITE HAUTE)

   - `ch02` (Statistiques) utilise des classes non-standard : `def-box` (10 occurrences), `exemple` (4 occurrences), `methode`, `attention`, `erreur-item` au lieu des classes standards `def`, `ex`, `meth`, `att`. Ces classes sont redefinies dans le `<style>` inline, ce qui duplique les styles de `styles.css`.
   - `ch03` (Indicateurs statistiques) utilise egalement `exemple` (10 occurrences) au lieu de `ex`, et utilise `<div class="container">` au lieu de `<div class="c">`.
   - Les chapitres ch04 et ch05 ont des classes inline custom (`situation-pro`, `erreur-item`, `hors-prog`, `correct`) au lieu des classes standards.

   **Fichiers concernes** : `seconde/ch02/lecon.html`, `seconde/ch03/lecon.html`, `seconde/ch04/lecon.html`, `seconde/ch05/lecon.html`, `seconde/ch06/lecon.html`

2. **Ch02 (Statistiques) est incomplet** (PRIORITE MOYENNE)

   Le cours se coupe apres les representations graphiques avec un renvoi vers le chapitre 3 : "Suite dans le Chapitre 3". Les indicateurs de position (moyenne, mediane, mode) et de dispersion (etendue, ecart-type, IQR, boite a moustaches) ne sont pas traites dans ch02 mais dans ch03. En soi ce decoupage est possible, mais ch02 est anormalement court (349 lignes) et les graphiques/animations en fin de page (calculatrice de statistiques) sont deconnectes du contenu pedagogique qui precede.

3. **Volume de CSS inline excessif dans certains chapitres**

   - ch01 : le tag `<style>` est minimaliste (1 ligne :root), ce qui est ideal.
   - ch02 : 22 lignes de CSS inline avec classes non-standard.
   - ch04 : 30 lignes, ch05 : 28 lignes, ch06 : 35 lignes, ch07 : 34 lignes.
   - Les chapitres ch08 a ch14 (plus recents?) sont beaucoup plus propres avec 3-14 lignes de CSS inline.

4. **Labels de badges heterogenes** (PRIORITE BASSE)

   - ch07 utilise `<span class="badge-niv badge-1">Niveau 1 — Bases</span>` (style non-standard)
   - ch01 utilise `<span class="badge badge-green">Niveau 1</span>` (style standard)
   - ch05 n'utilise pas de badges de niveau sur les exercices
   - La nomenclature des niveaux n'est pas coherente d'un chapitre a l'autre.

### Exemples concrets de problemes

**Probleme 1 — ch02 utilise `def-box` au lieu de `def`** :
```html
<!-- ch02/lecon.html ligne 96 -->
<div class="def-box">
  <strong>Population :</strong> l'ensemble de tous les elements etudies.
</div>
```
Devrait etre :
```html
<div class="def">
  <strong>Population :</strong> l'ensemble de tous les elements etudies.
</div>
```

**Probleme 2 — ch03 utilise `<div class="container">` au lieu de `<div class="c">`** :
```html
<!-- ch03/lecon.html ligne 33 -->
<div class="container">
```
Non conforme au template standard.

**Probleme 3 — ch02 inline CSS redefinit ce qui existe dans styles.css** :
```css
/* ch02/lecon.html lignes 18-22 */
.def-box{background:#ebf5ff;border-left:4px solid var(--p);...}
.exemple{background:#fffbeb;border-left:4px solid var(--o);...}
.attention{background:#fff5f5;border-left:4px solid var(--d);...}
.methode{background:#f0fff4;border:1px solid #a7f3d0;...}
```
Ce sont des duplications des classes `.def`, `.ex`, `.att`, `.meth` de styles.css.

---

## Section 2 — Premiere (maths/premiere)

### Note globale : 3.5/5

### Chapitres lus integralement

| Chapitre | Sujet | Lignes | Qualite |
|---|---|---|---|
| ch01 | Statistique a deux variables | 444 | Tres bon |
| ch02 | Probabilites | ~350 | Bon |
| ch03 | Suites numeriques | 417 | Excellent |
| ch04 | Resolution graphique | ~250 | Bon |
| ch06 | Fonction derivee | ~450 | Tres bon |
| ch07 | Geometrie dans l'espace | ~400 | Bon |
| ch08 | Vecteurs du plan | ~350 | Bon |

### Points forts

1. **Cours de tres bonne qualite quand ils existent** : ch01 (statistique a deux variables) est un modele de clarte avec nuage de points, point moyen, droite de regression, R2, interpolation/extrapolation, et section sur correlation/causalite. Ch03 (suites) est pedagogiquement excellent avec une progression claire arithmetique → geometrique → comparaison → synthese.

2. **Utilisation coherente des classes CSS standard** : Tous les chapitres de Premiere utilisent correctement `.def`, `.prop`, `.att`, `.meth`, `.retenir`, `.ex`, `.exo`, `.situation`, `.formule-box`. Le CSS inline est minimal (1 ligne :root dans la plupart des chapitres). C'est un progres significatif par rapport a certains chapitres de Seconde.

3. **Contextes professionnels bien choisis** : ch01 utilise un "technicien chauffagiste" et un "menuisier agenceur", ch03 utilise un "menuisier agenceur", un "artisan charpentier", un "installateur thermique", un "technicien chauffagiste". ch06 utilise un "artisan menuisier", un atelier de charpente. Conforme aux regles.

4. **Exercices corriges integres** : ch03 contient 6 mini-exercices corriges avec le bouton standard `.bc` / `.corr`. Ch02 contient des exercices avec arbres de probabilites.

5. **Lien avec la Seconde explicite** : ch01 commence par un "Rappels de Seconde" qui reprend effectif, frequence, moyenne, etendue. Ch03 repose naturellement sur les fonctions affines de Seconde.

### Points faibles

1. **Deux chapitres sont des stubs vides** (PRIORITE CRITIQUE)

   - **ch05 — Fonctions polynomes de degre 2** : seulement le squelette HTML (29 lignes), message "Contenu a venir". C'est un chapitre fondamental du programme de Premiere.
   - **ch09 — Trigonometrie** : meme situation, 29 lignes, "Contenu a venir". Egalement au programme.

   Ces deux manques creent un trou significatif dans la couverture du programme.

2. **Absence de graphiques/animations interactives dans plusieurs chapitres** (PRIORITE MOYENNE)

   Contrairement aux chapitres de Seconde (qui sont tres riches en Chart.js, SVG, Canvas), plusieurs chapitres de Premiere n'ont aucune visualisation interactive :
   - ch02 (Probabilites) : pas de graphique
   - ch03 (Suites) : pas de graphique (la representation graphique est decrite mais non illustree)
   - ch04 (Resolution graphique) : pas de graphique interactif (paradoxal pour un chapitre sur la lecture graphique!)
   - ch07 (Geometrie dans l'espace) : pas de visualisation 3D

   Seul ch01 contient des graphiques Chart.js (nuages de points).

3. **Ch06 (Derivation) ne contient pas de graphique de la tangente** (PRIORITE MOYENNE)

   Un cours sur la derivation sans visualisation graphique de la tangente glissante est une occasion manquee. L'interpretation geometrique de f'(a) comme pente de la tangente merite une animation interactive.

4. **Pas de section "Erreurs frequentes" dans la plupart des chapitres** (PRIORITE BASSE)

   Contrairement a la Seconde ou les blocs `.att` sont systematiques, en Premiere seuls ch01 et ch06 ont des blocs d'attention aux erreurs frequentes. ch03 a un bloc "Ne pas confondre" (arithmetique vs geometrique) mais pas de section dediee.

### Exemples concrets de problemes

**Probleme 1 — ch05 est vide** :
```html
<!-- maths/premiere/ch05/lecon.html -->
<div class="objectifs">
  <h3>Objectifs du chapitre</h3>
  <p>Contenu a venir.</p>
</div>
<!-- Fin du fichier -->
```

**Probleme 2 — ch03 n'a pas de graphique pour illustrer la representation des suites** :
La section V "Representation graphique des suites" (ligne 273-309) explique comment representer graphiquement une suite mais ne fournit aucun graphique. Un Chart.js montrant les points (n, u_n) pour la suite arithmetique vs la suite geometrique serait tres utile.

---

## Section 3 — Terminale (maths/terminale)

### Note globale : 4/5

### Chapitres lus integralement ou partiellement

| Chapitre | Sujet | Lignes | Qualite |
|---|---|---|---|
| ch01 | Statistiques a deux variables | ~600 | Excellent |
| ch03 | Suites (geometrique) | ~700 | Excellent |
| ch05 | Fonctions exponentielles et log | ~900 | Excellent |
| ch08 | Calcul integral | ~750 | Tres bon |
| ch10 | Nombres complexes | ~600 | Tres bon |
| ch11 | Produit scalaire | ~550 | Tres bon |

### Points forts

1. **Cours tres complets et structures** : tous les 11 chapitres sont des cours complets (aucun stub). Le volume moyen est de 700-900 lignes, ce qui temoigne d'un contenu substantiel.

2. **Utilisation exemplaire des classes CSS standards** : `.def`, `.prop`, `.att`, `.meth`, `.retenir`, `.ex`, `.exo`, `.situation`, `.formule-box` sont utilises de maniere coherente. Le CSS inline est minimal (principalement :root + quelques classes specifiques a la page).

3. **Double contexte professionnel ICCER/ERA** : les chapitres de Terminale utilisent systematiquement les badges `ticcer-badge` et `erama-badge` pour proposer des contextes adaptes aux deux groupements. Exemple dans ch03 : depreciation de pompe a chaleur (ICCER) et chiffre d'affaires d'atelier de menuiserie (ERA).

4. **Animations et interactivite de qualite** : ch05 (exponentielle/log) et ch08 (calcul integral) contiennent des visualisations Canvas interactives. Ch10 (nombres complexes) propose une representation dans le plan complexe. Ch11 (produit scalaire) a une visualisation temps reel des vecteurs.

5. **Sections "Pour aller plus loin"** : certains chapitres incluent des sections hors-programme clairement identifiees (classe `.hors-prog` ou `.hprog`), ce qui est une bonne pratique pour les eleves en poursuite BTS.

6. **Liens explicites avec la Premiere** : ch03 (suites geometriques) fait reference aux suites arithmetiques de Premiere. ch05 (exponentielle) fait le lien avec les suites geometriques.

### Points faibles

1. **Chemin absolu `/nav.css` dans 8 chapitres de Terminale** (PRIORITE HAUTE — technique)

   Les fichiers suivants utilisent `href="/nav.css"` au lieu du chemin relatif :
   - `terminale/ch01/lecon.html`
   - `terminale/ch03/lecon.html`
   - `terminale/ch04/lecon.html`
   - `terminale/ch06/lecon.html`
   - `terminale/ch07/lecon.html`
   - `terminale/ch08/lecon.html`
   - `terminale/ch09/lecon.html`
   - `terminale/ch10/lecon.html`
   - `terminale/ch11/lecon.html`

   Ce chemin absolu fonctionne en local mais peut casser en deploiement GitHub Pages.

2. ~~**Encodage HTML entities dans certains chapitres** (PRIORITE BASSE)~~ — **CORRIGE 2026-03-16**

   ~~Les chapitres ch04, ch05, ch08 utilisent des entites HTML~~ — Corrige dans les **44 fichiers** de maths/terminale (6 041 entites converties en UTF-8).

3. **Absence d'exercices dans certains cours** (PRIORITE MOYENNE)

   Contrairement a la Seconde ou la plupart des cours incluent des mini-exercices, certains cours de Terminale n'en contiennent pas directement (les exercices sont dans les fichiers `exercices.html` separes). C'est un choix pedagogique valide mais moins autonome que le modele de Seconde.

4. **Certains chapitres pourraient etre hors programme Bac Pro** (A VERIFIER)

   - ch10 (Nombres complexes) mentionne les impedances en courant alternatif (ICCER). Les nombres complexes sont au programme du groupement 1 mais pas forcement du groupement 3.
   - ch11 (Produit scalaire) est au programme du groupement 1.
   - ch09 (Fonctions ln et exponentielle) fait potentiellement double emploi avec ch05 (Fonctions exponentielles et logarithme decimal).

   **Recommandation** : verifier la coherence avec les programmes officiels dans `/pdf/`.

---

## Progression inter-niveaux

### Statistiques : Seconde → Premiere → Terminale

| Niveau | Contenu | Qualite |
|---|---|---|
| Seconde ch02-ch03 | Statistique a 1 variable : vocabulaire, effectifs, frequences, diagrammes, moyenne, mediane, quartiles, boite a moustaches | Bon (mais ch02 incomplet, renvoie vers ch03) |
| Premiere ch01 | Statistique a 2 variables : nuage de points, point moyen, droite de regression, R2, interpolation/extrapolation, correlation vs causalite | Tres bon, rappels de Seconde explicites |
| Terminale ch01 | Statistique a 2 variables (approfondissement) : ajustements non lineaires, changement de variable | Excellent, progression naturelle |

**Verdict** : Progression coherente et bien articulee. Le passage de 1 variable (Seconde) a 2 variables (Premiere) puis approfondissement (Terminale) est logique. Les rappels sont presents.

### Fonctions : Seconde → Premiere → Terminale

| Niveau | Contenu | Qualite |
|---|---|---|
| Seconde ch07 | Notion de fonction, image, antecedent, tableau de valeurs, representation graphique | Excellent, tres progressif |
| Seconde ch08 | Fonction lineaire et proportionnalite | Bon |
| Seconde ch09 | Fonction affine (y=ax+b) | Tres bon |
| Seconde ch10 | Fonction carree | Bon |
| Premiere ch04 | Resolution graphique d'equations et d'inequations | Bon |
| Premiere ch05 | Fonctions polynomes de degre 2 | **ABSENT** (stub) |
| Premiere ch06 | Fonction derivee et etude des variations | Tres bon |
| Terminale ch04 | Fonctions polynomes de degre 3 | Complet |
| Terminale ch05 | Exponentielles et logarithme | Excellent |
| Terminale ch08 | Calcul integral | Tres bon |
| Terminale ch09 | Fonctions ln et exponentielle | Complet |

**Verdict** : Progression globalement bonne MAIS le chapitre manquant sur les polynomes de degre 2 (Premiere ch05) cree un trou entre la fonction carree (Seconde ch10) et les polynomes de degre 3 (Terminale ch04). Les eleves n'auront pas vu la forme canonique, le discriminant, ni la resolution de ax2+bx+c=0 en Premiere.

### Suites : Premiere → Terminale

| Niveau | Contenu | Qualite |
|---|---|---|
| Premiere ch03 | Suites arithmetiques et geometriques : definitions, terme general, somme (arithmetique), representation graphique | Excellent |
| Terminale ch03 | Suites geometriques (approfondissement) : somme, sens de variation, lien avec exponentielle | Excellent |

**Verdict** : Tres bonne progression. Le cours de Premiere introduit les deux types de suites, celui de Terminale approfondit la suite geometrique. Les exercices et contextes sont varies (salaire, epargne, depreciation, amortissement).

### Geometrie : Seconde → Premiere → Terminale

| Niveau | Contenu | Qualite |
|---|---|---|
| Seconde ch11 | Figures planes : perimetres et aires | Bon |
| Seconde ch12 | Theoreme de Pythagore | Excellent |
| Seconde ch13 | Theoreme de Thales | Bon |
| Seconde ch14 | Solides, volumes, agrandissement | Bon |
| Premiere ch07 | Geometrie dans l'espace (solides, sections) | Bon |
| Premiere ch08 | Vecteurs du plan | Bon |
| Premiere ch09 | Trigonometrie | **ABSENT** (stub) |
| Terminale ch06 | Vecteurs (approfondissement) | Complet |
| Terminale ch07 | Trigonometrie (approfondissement) | Complet |
| Terminale ch11 | Produit scalaire | Complet |

**Verdict** : Le trou en trigonometrie (Premiere ch09 stub) est problematique car le cours de Terminale ch07 suppose des prerequis de Premiere sur les rapports trigonometriques. La progression en vecteurs (Premiere ch08 → Terminale ch06 → ch11 produit scalaire) est bien construite.

---

## Synthese des recommandations

### Priorite critique

1. **Rediger maths/premiere/ch05/lecon.html** (Fonctions polynomes de degre 2) : discriminant, forme canonique, resolution ax2+bx+c=0, representation graphique parabole. Ce chapitre est fondamental et manquant.

2. **Rediger maths/premiere/ch09/lecon.html** (Trigonometrie) : cosinus, sinus, tangente dans le triangle rectangle, applications professionnelles. Prerequis pour la Terminale.

### Priorite haute

3. **Harmoniser les classes CSS de seconde/ch02 et ch03** : remplacer `def-box` par `def`, `exemple` par `ex`, `methode` par `meth`, `attention` par `att`. Supprimer les definitions inline correspondantes. Remplacer `<div class="container">` par `<div class="c">` dans ch03.

4. **Corriger les chemins absolus `/nav.css`** dans les 9 fichiers de terminale (remplacer par `../../../nav.css`).

### Priorite moyenne

5. **Ajouter des visualisations interactives en Premiere** : graphiques Chart.js pour ch03 (suites), ch04 (resolution graphique), ch06 (tangente glissante). Les chapitres de Seconde montrent que c'est pedagogiquement tres efficace.

6. **Completer le cours de seconde/ch02** : la section sur les indicateurs statistiques (moyenne, mediane, quartiles) est renvoyee vers ch03. Il serait utile de fusionner les deux chapitres ou au minimum d'ajouter un resume des indicateurs dans ch02.

7. **Verifier la conformite au programme** des chapitres terminale ch09 (double emploi avec ch05?) et ch10 (nombres complexes — groupement 1 uniquement?).

### Priorite basse

8. **Harmoniser les badges de niveaux dans les mini-exercices** de Seconde (certains utilisent `badge-niv badge-1`, d'autres `badge badge-green`).

9. ~~**Convertir les entites HTML** en caracteres UTF-8 dans les titres de terminale ch04, ch05, ch08.~~ — **CORRIGE 2026-03-16** (44 fichiers, 6 041 entites)

10. **Ajouter des sections "Erreurs frequentes"** dans les cours de Premiere (seuls ch01 et ch06 en ont).

---

## Corrections realisees

- **2026-03-16** : Harmonise CSS maths/seconde/ch02 (def-box→def, exemple→ex, suppression inline)
- **2026-03-16** : Harmonise CSS maths/seconde/ch03 (container→c, exemple→ex, nav-btn→nb, sub→sous-titre)
- **2026-03-16** : Harmonise CSS maths/seconde/ch04 exercices (methode style inline→meth)
- **2026-03-16** : Harmonise CSS maths/seconde/ch05 exercices (methode style inline→meth)
- **2026-03-16** : Converti 6 041 entites HTML en UTF-8 dans les 44 fichiers de maths/terminale

---

## Ameliorations restantes

- [x] Rediger premiere/ch05 (polynomes degre 2) (2026-03-16, 1037 lignes, conforme BO)
- [x] Rediger premiere/ch09 (trigonometrie) (2026-03-16, 761 lignes, conforme BO)
- [x] Harmoniser CSS de seconde/ch02 (def-box → def, exemple → ex, etc.) (2026-03-16)
- [x] Harmoniser CSS de seconde/ch03 (container → c, exemple → ex) (2026-03-16)
- [x] Harmoniser CSS inline de seconde/ch04, ch05 (methode→meth) (2026-03-16)
- [x] Corriger chemins `/nav.css` dans 9 fichiers terminale (deja corrige lors de la session 1)
- [ ] Ajouter graphiques Chart.js dans premiere/ch03 (suites)
- [ ] Ajouter animation tangente dans premiere/ch06
- [ ] Ajouter graphique interactif dans premiere/ch04
- [ ] Completer ou reorganiser seconde/ch02 (indicateurs stats)
- [ ] Verifier conformite programme terminale ch09, ch10
- [ ] Harmoniser badges de niveaux dans mini-exercices seconde
- [x] Convertir entites HTML en UTF-8 dans maths/terminale (44 fichiers, 6 041 entites) (2026-03-16)
- [ ] Ajouter blocs "Erreurs frequentes" dans premiere ch02, ch03, ch04, ch07, ch08
