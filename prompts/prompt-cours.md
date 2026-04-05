# Prompt de référence — Génération de pages de cours

Je veux que tu rédiges une page de cours complète, très pédagogique et bien structurée, destinée à des élèves de lycée professionnel.

Objectif : produire une page HTML prête à être intégrée dans un site pédagogique.

Le cours doit être clair, progressif et accessible, avec beaucoup d'explications et des éléments visuels.

---

## STRUCTURE DU COURS

### 1. Titre du chapitre

### 2. Introduction
- expliquer la notion simplement
- donner un exemple concret lié à la vie réelle ou au domaine professionnel

### 3. Notions essentielles
- explication détaillée des concepts
- vocabulaire scientifique expliqué simplement
- encadrés pour les définitions importantes

### 4. Exemples expliqués
- plusieurs exemples détaillés
- raisonnement étape par étape
- explications pédagogiques

### 5. Figures et schémas — OBLIGATOIRES selon le domaine

**Règle absolue :** un cours qui porte sur une notion visuelle DOIT contenir des figures SVG inline. Un cours de géométrie sans figure, un cours de fonctions sans courbe, ou un cours d'électricité sans schéma de circuit est **incomplet**.

#### Lien avec les capacités du programme

Avant de générer le cours, lire le fichier programme (`.md` dans `/pdf/`) pour identifier les capacités du chapitre. **Toute capacité contenant un verbe visuel impose une figure dans la leçon :**

| Verbe dans la capacité | Figure obligatoire |
|---|---|
| "lire (un graphique / oscillogramme / schéma)" | SVG ou Chart.js du graphique en question |
| "représenter (une force / un vecteur / un schéma)" | SVG de la situation |
| "tracer (une droite / courbe / diagramme)" | SVG avec repère vierge annoté + exemple tracé |
| "exploiter (une courbe / un enregistrement)" | SVG ou Chart.js de la courbe exploitée |
| "construire (un graphique / diagramme / schéma)" | SVG de l'exemple construit |
| "réaliser un schéma / montage" | SVG du schéma normalisé |
| "identifier (à partir d'un enregistrement / schéma)" | SVG de l'enregistrement ou du schéma |

Utiliser `python3 scripts/check_visuals.py` pour vérifier la couverture graphique après génération.

#### Interactivité dans les leçons

Les leçons sont **consultées sur écran**. L'interactivité est **autorisée et encouragée** :
- **Chart.js** : graphiques de données quantitatives (fonctions, statistiques, courbes d'étalonnage)
- **Canvas + JavaScript** : animations pédagogiques (convergence, oscillation, tracé dynamique)
- **SVG animé** : transitions simples (flèches, zones)

L'interactivité sert à **illustrer** une notion, jamais à évaluer l'élève.

#### Quand une figure est OBLIGATOIRE dans le cours

**Mathématiques :**
- Fonctions : courbe représentative, tableau de variations illustré, lecture graphique (extremums, antécédents, signe)
- Géométrie : figure cotée (triangles, parallélogrammes, solides), repérage dans le plan, vecteurs
- Statistiques : diagramme en bâtons, diagramme circulaire, boîte à moustaches, histogramme
- Probabilités : arbre de probabilités, tableau à double entrée
- Suites : nuage de points \((n ; u_n)\), représentation en escalier/toile d'araignée

**Physique-Chimie :**
- Électricité : schéma de circuit (symboles normalisés), caractéristique I(U)
- Mécanique : bilan des forces (vecteurs), diagramme v(t), trajectoire
- Optique : schéma rayon/normale/miroir, réflexion/réfraction
- Thermique : diagramme de changement d'état T(t), schéma de transfert thermique
- Acoustique : oscillogramme, échelle de niveaux sonores (dB)
- Chimie : schéma de verrerie (dilution, dosage), spectres d'émission

#### Style SVG à respecter

```html
<figure class="schema" style="text-align:center;margin:12px 0">
  <svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
    <!-- Contenu -->
  </svg>
  <figcaption style="font-size:0.88em;color:#555;margin-top:4px">Légende</figcaption>
</figure>
```

**Conventions graphiques :**
- Remplissage : `fill="#ebf5ff"` (bleu très clair)
- Contour principal : `stroke="#0056b3"`, `stroke-width="2"`
- Labels : `font-size="12"`, `fill="#555"`
- Grilles : `stroke="#e2e8f0"`, `stroke-width="0.5"`
- Axes : `stroke="#333"`, `stroke-width="1.5"`, flèches aux extrémités
- Deuxième courbe/droite : `stroke="#c53030"` (rouge)
- Solides 3D : arêtes cachées en `stroke-dasharray="4,2"`

#### Quand une figure est RECOMMANDÉE (pas obligatoire)

- Illustration d'une situation professionnelle (croquis coté d'une pièce, plan d'une pièce)
- Schéma récapitulatif d'une méthode (organigramme de résolution)
- Toute situation où le texte seul est ambigu ou difficile à comprendre

### 6. Graphiques dynamiques

Pour les données quantitatives qui évoluent (courbes de fonctions, régressions, séries statistiques) :
- Privilégier **Chart.js** pour les graphiques interactifs
- Utiliser **SVG** pour les graphiques statiques (lecture graphique, schémas cotés)
- Réserver **Canvas** pour les animations

### 7. Animations pédagogiques

Si c'est pertinent, créer une petite animation ou simulation pour illustrer la notion (JavaScript, Canvas, SVG animé). L'animation doit illustrer un phénomène scientifique du programme.

### 8. Encadrés importants
Ajouter des encadrés pédagogiques :
- À retenir
- Attention aux erreurs fréquentes

### 9. Applications concrètes
Relier la notion à :
- la vie quotidienne
- les métiers professionnels

### 10. Exercices d'application intégrés (OBLIGATOIRE)

Les exercices d'application doivent être **distribués dans le déroulé de la leçon**, pas regroupés en fin de chapitre.

**Position :** après une définition importante, une propriété, une méthode ou un exemple.

**Format HTML :**
```html
<div class="mini-exo">
  <strong>Application</strong>
  <p>Consigne...</p>
  <button class="bc" onclick="this.nextElementSibling.style.display='block'">Voir la correction</button>
  <div class="corr">Correction détaillée avec démarche et résultat mis en évidence...</div>
</div>
```

**Types attendus :** application directe d'une définition, utilisation d'une formule, calcul simple, lecture de graphique ou de tableau, vérification d'un résultat.

**Règles :**
- 1 exercice minimum par notion importante
- 3 à 6 par chapitre en moyenne
- Réalisable en 1 à 3 minutes
- Une seule compétence ciblée
- Consigne claire et courte
- Correction avec démarche + résultat mis en évidence

**Interdictions :**
- Exercices longs ou nécessitant plusieurs notions non encore vues
- Regroupement en bloc unique en fin de leçon
- Exercices sans lien avec le contenu immédiat

---

## CONTRAINTES PÉDAGOGIQUES

- niveau lycée professionnel
- phrases simples
- vocabulaire accessible
- progression logique
- explications détaillées

---

## CONTRAINTES TECHNIQUES

- produire une page HTML propre
- utiliser des sections bien structurées
- utiliser des classes CSS simples
- intégrer les graphiques et animations directement dans la page

---

---

## CHECKLIST AVANT PUBLICATION

### Exercices d'application (OBLIGATOIRE)
- [ ] **3 à 6 `.mini-exo` répartis dans la leçon** (pas seulement en fin)
- [ ] Chaque `.mini-exo` placé après une définition, propriété, méthode ou exemple
- [ ] Chaque `.mini-exo` a un bouton "Voir la correction" avec démarche expliquée
- [ ] Consignes courtes, réalisables en 1–3 min, une seule compétence ciblée

### Figures et schémas
- [ ] Programme lu — capacités visuelles identifiées avant génération
- [ ] Toute capacité avec verbe visuel ("lire", "représenter", "tracer", "exploiter") a sa figure dans le cours
- [ ] Figures SVG présentes pour toutes les notions visuelles (géométrie, fonctions, circuits, forces…)
- [ ] Conventions SVG respectées (fill #ebf5ff, stroke #0056b3, labels #555)
- [ ] Graphiques Chart.js pour les données quantitatives interactives (leçon = écran)
- [ ] Canvas pour les animations pédagogiques pertinentes
- [ ] Aucune figure décrite uniquement par du texte quand un schéma est nécessaire
- [ ] Légendes (`<figcaption>`) sur chaque figure
- [ ] `check_visuals.py` lancé pour vérifier les références orphelines

### Technique
- [ ] MathJax inclus si formules
- [ ] print.css inclus
- [ ] nav.js inclus
- [ ] Couleurs CSS conformes au thème matière/niveau

---

## OBJECTIF FINAL

Produire une page de cours riche, visuelle, claire et très pédagogique, utilisable directement sur un site éducatif.
