# Programme de mathématiques – Classe terminale professionnelle
> Source : Bulletin officiel de l'Éducation nationale (2020)  
> Document de référence pour l'enseignement et la création de ressources pédagogiques.

---

## Organisation du programme

### Groupements de spécialités
Les spécialités de Bac Pro sont réparties en **trois groupements** :
- **Groupement A** : spécialités avec enseignement de physique-chimie, programme de trigonométrie (ex. : spécialités industrielles type électrotechnique, maintenance…)
- **Groupement B** : spécialités avec enseignement de physique-chimie, programme de vecteurs dans l'espace (ex. : ERA, Menuisier Agenceur, TMA, ICCER…)
- **Groupement C** : spécialités sans enseignement de physique-chimie

> La liste actualisée des spécialités par groupement est publiée par le ministère.

### Domaines et modules

| Domaine | Module | Groupements |
|---|---|---|
| **Statistique et probabilités** | Statistiques à deux variables | A, B, C |
| | Probabilités | A, B, C |
| **Algèbre – Analyse** | Suites numériques | A, B, C |
| | Fonctions polynômes de degré 3 | A, B, C |
| | Fonctions exponentielles et logarithme décimal | A, B, C |
| | Calculs commerciaux et financiers | C seulement (sans phys-chimie) |
| **Géométrie** | Trigonométrie | A seulement |
| | Vecteurs dans l'espace | B seulement |
| **Transversaux** | Algorithmique et programmation | A, B, C |
| | Automatismes | A, B, C |
| | Vocabulaire ensembliste et logique | A, B, C |
| **Complémentaire** | Calcul intégral | Poursuite d'études |
| (orientation) | Fonctions ln et exponentielle (base e) | Poursuite d'études |
| | Nombres complexes | Poursuite d'études |
| | Produit scalaire | Poursuite d'études |

> Les modules transversaux ne font **pas** l'objet de cours spécifiques.

---

## Domaine 1 — Statistique et probabilités

**Objectifs du domaine** : Approfondir les statistiques à deux variables et l'ajustement (affine ou non) ; consolider la probabilité conditionnelle ; introduire les arbres pondérés et la notion d'indépendance.

---

### Module 1.1 — Statistiques à deux variables *(groupements A, B et C)*

**Objectif** : Approfondir la notion d'ajustement à partir de situations professionnelles ou de la vie économique et sociale. Réinvestissement des fonctions logarithme décimal et exponentielles pour des changements de variable.

**Liens 1re Pro** : Découverte des statistiques à deux variables et de l'ajustement affine. En terminale : consolidation + nouveaux types d'ajustement.

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| À l'aide d'outils numériques : choisir un modèle adapté pour réaliser un ajustement d'un nuage de points associé à une série statistique à deux variables. Utiliser un ajustement pour **interpoler** ou **extrapoler** des valeurs inconnues. | Ajustement d'un nuage de points associé à une série statistique à deux variables quantitatives. |

**Commentaires** :
- Les ajustements ne sont **pas** uniquement affines.
- Aucune justification théorique du modèle choisi n'est attendue.
- On indique aux élèves l'ajustement à réaliser (x en y ou y en x).
- Changements de variable possibles (indiqués aux élèves) : *z = log(y)*, *z = 1/x*, *z = qˣ*… permettant de se ramener à un ajustement affine. Le coefficient de détermination peut servir d'indicateur de pertinence.

**Bivalence** : mis en œuvre dans les domaines *Mécanique* et *Électricité* (physique-chimie).

---

### Module 1.2 — Probabilités *(groupements A, B et C)*

**Objectif** : Modéliser des situations aléatoires par des arbres de probabilités pondérés pour déterminer des probabilités. Contextes variés : économie, industrie, médical, développement durable, changement climatique.

**Liens 1re Pro** : Événements, tableaux croisés, fréquence et probabilité conditionnelle découverts en première. En terminale : construction d'arbres pondérés, probabilité conditionnelle réinvestie, expériences à plusieurs épreuves, indépendance formalisée.

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Représenter par un **arbre de probabilités pondéré** une situation aléatoire donnée. | Arbres de probabilités pondérés : nœud, branche, chemin. |
| Exploiter la lecture d'un arbre pour déterminer les probabilités des événements associés aux différents chemins. Dans des cas simples, calculer une probabilité à l'aide de la **formule des probabilités totales**. | Probabilité conditionnée par un événement de probabilité non nulle. Règles de calcul des probabilités. Formule des probabilités totales. |
| Montrer que deux événements sont **indépendants**. | Indépendance de deux événements : P(A∩B) = P(A) × P(B). |

**Commentaires** :
- Les premiers arbres pondérés sont introduits à partir des tableaux croisés d'effectifs vus en première.
- La formule des probabilités totales est systématiquement mise en relation avec un arbre pondéré, appliquée sans formalisme, présentée sur un exemple.

---

## Domaine 2 — Algèbre – Analyse

**Objectifs** : Modéliser des situations ; résoudre des problèmes en choisissant une méthode adaptée ; découvrir de nouveaux types de suites et de nouvelles fonctions. Situations liées aux métiers préparés et aux enjeux du développement durable.

---

### Module 2.1 — Suites numériques *(groupements A, B et C)*

**Objectif** : Résoudre des problèmes concernant des phénomènes discrets modélisés par une **suite géométrique**.

**Liens 1re Pro** : Suites arithmétiques étudiées en première. En terminale : réinvestissement des suites arithmétiques + étude des suites géométriques de raison strictement positive.

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Calculer un terme de rang donné d'une suite géométrique (par récurrence ou par l'expression du terme général). Réaliser et exploiter une représentation graphique du nuage (n ; uₙ). Déterminer le sens de variation à l'aide de la raison *q* (avec *q* > 0) et du premier terme. | Suites géométriques de raison strictement positive : relation *uₙ₊₁ = uₙ × q*, expression du terme de rang *n*, sens de variation. |
| Calculer la **somme des *n* premiers termes** d'une suite géométrique (avec ou sans outils numériques). | Somme des *n* premiers termes d'une suite géométrique. |

**Exemples d'algorithmes** :
- Calculer un terme de rang donné.
- Calculer la somme d'un nombre fini de termes.
- Générer et représenter une liste de termes (nuage de points).
- Déterminer le rang à partir duquel les termes sont supérieurs ou inférieurs à une valeur donnée.

**Commentaires** :
- La connaissance de la formule de la somme n'est **pas exigée**.
- La notation ∑ peut être introduite en vue de poursuite d'études.
- Lien établi entre suites géométriques et fonctions exponentielles.
- Exemples de modélisation d'une évolution à taux fixe.

---

### Module 2.2 — Fonctions polynômes de degré 3 *(groupements A, B et C)*

**Objectif** : Étudier la **fonction cube** et les fonctions polynômes de degré 3.

**Liens 1re Pro** : Variations des fonctions polynômes de degré 2 via le signe de la dérivée étudiées en première. En terminale : même démarche appliquée aux polynômes de degré 3.

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Étudier la fonction cube : dérivée, variations, représentation graphique. | Fonction cube. Dérivée de la fonction cube. |
| Utiliser les formules et règles de dérivation pour déterminer la dérivée d'une fonction polynôme de degré ≤ 3. Dresser le tableau de variations à partir du signe de la dérivée. Exploiter le tableau de variations pour : déterminer le nombre de solutions de *ƒ(x) = c* ; déterminer les éventuels extremums locaux. | Fonction polynôme de degré 3. |

**Exemples d'algorithmes** :
- Déterminer par balayage un encadrement ou une valeur approchée d'une solution de *ƒ(x) = g(x)* sur un intervalle donné.

**Commentaires** :
- Constater (via la fonction cube) que *ƒ'(a) = 0* ne suffit **pas** pour conclure à un extremum local en *a*.
- Si la dérivée n'est pas facilement factorisable, l'outil numérique peut en déterminer les racines.

---

### Module 2.3 — Fonctions exponentielles et logarithme décimal *(groupements A, B et C)*

**Objectif** : Résoudre des problèmes concernant des phénomènes modélisables par la fonction logarithme décimal ou par une fonction exponentielle. Lien avec les suites géométriques.

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Représenter graphiquement les fonctions exponentielles de base *q* (*x ↦ qˣ*, avec *q* > 0, *q* ≠ 1) sur un intervalle donné. Utiliser leurs **propriétés opératoires** pour transformer des écritures. | Fonctions exponentielles de base *q* (*x ↦ qˣ*). Variations. Propriétés opératoires. |
| Représenter graphiquement la fonction **logarithme décimal** sur un intervalle donné. | Fonction logarithme décimal *x ↦ log(x)*. Variations. Propriétés opératoires. |
| Résoudre (par le calcul, graphiquement ou avec outils numériques) des équations du type *qˣ = a* et *log(x) = a*, ou des inéquations du type *qˣ ≥ a* et *log(x) ≥ a*. | Résolution de ces équations et inéquations. |

**Exemples d'algorithmes** :
- Déterminer par balayage un encadrement ou une valeur approchée d'une solution de *ƒ(x) = g(x)*.

**Commentaires** :
- Les fonctions exponentielles sont présentées comme prolongement des suites géométriques de premier terme 1 ; leurs variations sont admises.
- La fonction logarithme décimal est introduite à partir de *ƒ(x) = 10ˣ* : log(b) est l'unique solution de *10ˣ = b*.
- L'identité *log(10ˣ) = x* se déduit de la définition.
- Utilisation possible du **papier semi-logarithmique**.

**Bivalence** : mis en œuvre dans les domaines *Chimie* et *Signaux* (physique-chimie).

---

### Module 2.4 — Calculs commerciaux et financiers
> ⚠️ **Uniquement pour les spécialités sans enseignement de physique-chimie (groupement C)**

**Objectif** : Réinvestir suites arithmétiques/géométriques, fonctions exponentielles et logarithme décimal dans des situations professionnelles (intérêts composés, emprunts).

**Liens 1re Pro** : Intérêts simples, taux proportionnels, coûts étudiés en première. En terminale : intérêts composés.

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Calculer le capital obtenu après *n* périodes d'un placement à intérêts composés. Déterminer la durée *n* de placement pour obtenir un capital donné. | Intérêts composés. Formule *cₙ = c₀(1 + t)ⁿ*. |
| Compléter un tableau d'amortissement. | Emprunt : remboursement par annuités constantes ou par amortissement constant. Coût d'un emprunt. |
| Calculer un taux mensuel équivalent à un taux annuel donné. Calculer un taux moyen. | Taux mensuel, taux annuel, taux moyen. |

**Commentaires** :
- La 1re ligne des tableaux d'amortissement est fournie entièrement, la 2e partiellement.
- Ce module se fait, dans la mesure du possible, en collaboration avec l'enseignement professionnel.

---

## Domaine 3 — Géométrie

> Ce domaine se compose de deux modules **mutuellement exclusifs** selon le groupement.

---

### Module 3.1 — Trigonométrie *(groupement A uniquement)*

**Objectif** : Résoudre certaines équations trigonométriques et faire découvrir un outil permettant d'**additionner ou soustraire des tensions ou intensités sinusoïdales** de même fréquence (vecteurs de Fresnel). S'appuie sur des exemples concrets du domaine professionnel ou de la physique.

**Liens 1re Pro** : Cercle trigonométrique et fonctions sinus/cosinus découverts en première. En terminale : lien vecteurs de Fresnel / fonctions trigonométriques + résolution d'équations trigonométriques.

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Établir des liens entre le **vecteur de Fresnel** d'une tension ou intensité sinusoïdale *a sin(ωt + φ)* et la courbe représentative de la fonction *t ↦ a sin(ωt + φ)*. | Représentation de Fresnel d'une grandeur sinusoïdale. |
| Résoudre les équations de la forme : *cos x = a*, *sin x = b* sur ]-π ; π] et *sin(ωt + φ) = c* sur un intervalle approprié au contexte. | Équations de la forme *cos x = a*, *sin x = b* et *sin(ωt + φ) = c* sur un intervalle donné. |

**Commentaires** : traité en s'appuyant sur des exemples concrets du domaine professionnel.

**Bivalence** : mis en œuvre dans le domaine *Électricité* (physique-chimie).

---

### Module 3.2 — Vecteurs dans l'espace *(groupement B uniquement)*

**Objectif** : Aborder le repérage et les notions vectorielles dans l'espace (extension sans formalisme des notions vues en première dans le plan).

**Liens 1re Pro** : Vecteurs dans le plan (égaux, opposés, colinéaires, norme) découverts en première. En terminale : extension à l'espace.

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Déterminer graphiquement les coordonnées d'un vecteur dans l'espace muni d'un repère orthonormé. Représenter un vecteur dont les coordonnées sont données. | Dans l'espace muni d'un repère orthonormé : coordonnées cartésiennes d'un point ; coordonnées d'un vecteur. |
| Calculer la **norme** d'un vecteur dans l'espace. | Norme d'un vecteur dans l'espace muni d'un repère orthonormé. |
| Calculer les coordonnées du **vecteur somme** de deux vecteurs. | Coordonnées du vecteur somme de deux vecteurs. |
| Reconnaître des vecteurs **égaux ou colinéaires** à l'aide de leurs coordonnées. | Coordonnées du produit d'un vecteur par un réel. |

**Commentaires** :
- Lien entre produit d'un vecteur par un réel et colinéarité établi.
- La norme est définie comme la longueur d'un représentant.

**Bivalence** : mis en œuvre dans les domaines *Mécanique* et *Électricité* (physique-chimie).

---

## Module transversal — Algorithmique et programmation *(groupements A, B et C)*

**Objectif** : Consolider et approfondir l'algorithmique et la programmation des classes antérieures. Langage : **Python** (en continuité avec la seconde et la première).

**Liens 1re Pro** : Variables, instructions conditionnelles, boucles, fonctions et listes découverts. En terminale : approfondissement de toutes ces notions.

### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Analyser un problème. Décomposer en sous-problèmes. Repérer les enchaînements logiques et les traduire en instructions conditionnelles et en boucles. | Séquences d'instructions, instructions conditionnelles, boucles bornées (`for`) et non bornées (`while`). |
| Choisir ou reconnaître le type d'une variable. Réaliser un calcul à l'aide d'une ou plusieurs variables. | Types de variables : entiers, flottants, chaînes de caractères, booléens. Affectation d'une variable. |
| Modifier ou compléter un algorithme ou un programme. Concevoir un algorithme ou un programme simple. | *(mis en pratique sur les domaines du programme)* |
| Comprendre et utiliser des fonctions. Compléter la définition d'une fonction. Structurer un programme avec des fonctions. | Arguments d'une fonction. Valeur(s) renvoyée(s) par une fonction. |
| Générer une liste. Manipuler des éléments d'une liste (ajouter, supprimer, extraire). Parcourir une liste. Itérer des instructions sur les éléments d'une liste. | Liste (en extension et en compréhension). |

**Commentaires** :
- Pas de cours spécifique : notions travaillées en situation.
- La maîtrise des propriétés des types de variables n'est pas attendue.
- En terminale, l'entête de la fonction n'est plus systématiquement donnée aux élèves dans les cas simples.
- Affectation : symbole ← en langage naturel, signe = en Python.
- Accent sur la **programmation modulaire**.
- Listes en compréhension mises en lien avec la notion d'ensemble.
- Se limiter aux listes sans présenter d'autres types de collections.

---

## Module transversal — Automatismes *(groupements A, B et C)*

> Entraînement régulier tout au long de l'année (rituels, questions flash, activités mentales). Les automatismes de seconde et de première continuent à être **entretenus**.

### Liste non exhaustive d'automatismes à travailler en terminale

- Calcul de la probabilité d'un événement ; de l'événement contraire Ā connaissant P(A).
- Calcul de la probabilité de la réunion d'événements incompatibles.
- Calcul de la probabilité de la réunion de deux événements.
- Calcul de la probabilité de l'intersection de deux événements.
- Exploitation de représentations de données : tableaux croisés d'effectifs, diagrammes.
- Calcul de probabilités conditionnelles.
- Calcul du terme de rang donné d'une suite arithmétique (premier terme et raison donnés).
- Visualisation (à partir de la représentation graphique d'un polynôme de degré 2) du nombre de solutions de *ƒ(x) = 0*.
- Écriture de la forme factorisée d'un polynôme de degré 2 dont les racines et le coefficient dominant sont connus.
- Utilisation des formules et règles de dérivation pour déterminer la dérivée d'une fonction polynôme de degré ≤ 2.
- Construction d'un vecteur du plan *(groupements A et B uniquement)* obtenu comme somme de deux vecteurs ou produit d'un vecteur par un réel non nul.

---

## Module transversal — Vocabulaire ensembliste et logique *(groupements A, B et C)*

*(Identique à celui de la seconde et de la première — travaillé transversalement dans tous les chapitres.)*

### Notions ensemblistes
- Élément, sous-ensemble, appartenance, inclusion, réunion, intersection, complémentaire.
- Symboles : ∈, ⊂, ∩, ∪.
- Intervalles : [a ; b], ]a ; b[, [a ; b[, ]a ; b] avec a et b réels.
- Notation du complémentaire : Ā (notation probabiliste).
- Notion de couple.

### Raisonnement logique (sur des exemples)
- Connecteurs logiques « et », « ou ».
- Quantificateurs « quel que soit » et « il existe » (∀ et ∃ sont **hors programme**).
- Implications et équivalences logiques.
- Réciproque d'une implication.
- Contre-exemple pour infirmer une proposition universelle.
- Raisonnements par disjonction des cas et par l'absurde.
- Distinctions : égalité / identité / équation pour « = » ; variable / indéterminée / inconnue / paramètre pour les lettres.

---

## Programme complémentaire — Préparation à une poursuite d'études

> Ces modules sont traités dans le cadre de l'**accompagnement au choix d'orientation** (heures dédiées). Les modules à traiter dépendent du projet de l'élève.

---

### Complément 1 — Calcul intégral

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Déterminer les primitives des fonctions usuelles par lecture inverse d'un tableau des dérivées. Déterminer (avec ou sans outils numériques) les primitives d'une somme de fonctions, du produit d'une fonction par un réel. | Primitives d'une fonction sur un intervalle. Si *F* est une primitive de *ƒ*, alors *F + k* (k constante) est aussi une primitive de *ƒ*. Primitives d'une somme de fonctions et du produit d'une fonction par un réel. |
| Calculer l'intégrale d'une fonction *ƒ* admettant une primitive *F* sur [a ; b] (avec ou sans outils numériques). Interpréter l'intégrale d'une fonction positive sur [a ; b] comme une **aire**. | Définition : ∫ₐᵇ ƒ(x)dx = F(b) − F(a). |

**Commentaires** :
- Aucune virtuosité calculatoire n'est imposée.
- Le calcul d'aire est plus spécifiquement destiné aux élèves visant une poursuite dans le secteur industriel.
- Approximation par la méthode des rectangles possible avec les outils numériques.

---

### Complément 2 — Fonctions logarithme népérien et exponentielle (base e)

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Étudier les variations et représenter graphiquement la **fonction ln** sur un intervalle donné. Utiliser ses propriétés opératoires pour transformer des écritures. | Fonction logarithme népérien *x ↦ ln(x)*. Définition du nombre *e*. Propriétés opératoires de ln. |
| Passer de *ln(x) = a* à *x = eᵃ* et inversement. Utiliser les propriétés opératoires de la **fonction exponentielle** (base e). Étudier ses variations et la représenter sur ℝ. | Fonction exponentielle de base e. Propriétés opératoires. |

**Commentaires** :
- ln est définie sur ℝ⁺*, s'annule en 1, sa dérivée est la fonction inverse.
- Lien possible entre ln et log.
- Propriétés opératoires de ln admises.
- *e* est l'unique solution de *ln(x) = 1*.
- La fonction *x ↦ eˣ* est un cas particulier des fonctions *x ↦ qˣ*.

---

### Complément 3 — Nombres complexes

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Calculer et interpréter géométriquement (dans le plan muni d'un repère orthonormé direct) : partie réelle, partie imaginaire, conjugué, module, argument d'un nombre complexe non nul. Passer de la forme algébrique à la forme trigonométrique et réciproquement. | **Forme algébrique** : partie réelle, partie imaginaire, conjugué, module ; égalité ; représentation dans le plan (affixe d'un point, d'un vecteur) ; somme, produit, quotient ; conjugué d'une somme/produit/quotient ; module d'un produit et d'un quotient. **Argument et forme trigonométrique** d'un nombre complexe non nul. |

**Commentaires** : L'image de la somme et du produit de deux nombres complexes peuvent être illustrées à l'aide d'un logiciel de géométrie dynamique.

---

### Complément 4 — Produit scalaire de deux vecteurs du plan

#### Capacités et connaissances

| Capacités | Connaissances |
|---|---|
| Utiliser les **trois expressions du produit scalaire** pour déterminer des longueurs et des angles. | Définition du produit scalaire de deux vecteurs dans un repère orthonormé. Propriétés : commutativité, linéarité. |
| Reconnaître des **vecteurs orthogonaux** à l'aide de leurs coordonnées. | Deux vecteurs $\vec{u}$ et $\vec{v}$ sont orthogonaux si et seulement si $\vec{u} \cdot \vec{v} = 0$. |

**Commentaires** : Le produit scalaire est défini par l'une des trois expressions suivantes, les deux autres étant admises :
1. $\vec{u} \cdot \vec{v} = \frac{1}{2}(\|\vec{u} + \vec{v}\|^2 - \|\vec{u}\|^2 - \|\vec{v}\|^2)$
2. $\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos\theta$ avec $\theta = (\vec{u}, \vec{v})$ (notion d'angle orienté abordée intuitivement)
3. Si $\vec{u}(x, y)$ et $\vec{v}(x', y')$ : $\vec{u} \cdot \vec{v} = xx' + yy'$

---

## Récapitulatif — Correspondances bivalence maths / physique-chimie

| Module mathématiques | Domaines physique-chimie associés |
|---|---|
| Statistiques à deux variables | Mécanique, Électricité |
| Fonctions exponentielles et logarithme décimal | Chimie, Signaux |
| Vecteurs dans l'espace (grp B) | Mécanique, Électricité |
| Trigonométrie / Fresnel (grp A) | Électricité |

---

## Note sur les filières bâtiment (ERA, Menuisier Agenceur, TMA, ICCER)

Ces spécialités appartiennent au **groupement B**. Le programme de terminale inclut donc :
- tous les modules communs (A, B, C) ;
- le module **Vecteurs dans l'espace** (et non Trigonométrie / Fresnel) ;
- **pas** de module Calculs commerciaux et financiers (présence de physique-chimie).

---

*Document établi d'après le programme officiel (BO 2020) — Terminale Bac Pro.*
