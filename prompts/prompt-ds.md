# Prompt de référence — Génération des Devoirs Surveillés (ds.html)

Guide de référence pour la création des pages `ds.html` dans chaque chapitre du site.

---

## Philosophie et rôle du DS

Le devoir surveillé est l'outil d'**évaluation sommative** du chapitre. Il se distingue des autres pages par son poids dans la notation officielle et sa durée (1 heure).

| Page | Rôle | Durée | Poids |
|---|---|---|---|
| `exercices.html` | S'entraîner | Variable | Aucun |
| `qcm.html` | S'auto-évaluer | 15-20 min | Aucun |
| `interro.html` | Diagnostic rapide | 10-15 min | Léger |
| **`ds.html`** | **Évaluation sommative** | **1 heure** | **Note officielle** |

### Ce que le DS doit évaluer

Le DS évalue **l'ensemble du chapitre** en mobilisant plusieurs capacités. Il ne teste pas seulement la mémorisation : il teste la capacité à **transférer** les notions dans un contexte professionnel.

- **Socle** : vérifier les notions fondamentales avec guidage
- **Standard** : évaluer les capacités attendues du programme sans aide
- **Approfondissement** : pousser vers la mise en équation autonome et le raisonnement type BTS

---

## Différenciation pédagogique

### Les 3 sujets

Chaque DS est proposé en **3 versions complètes** (pas 3 exercices d'un même sujet) :

| Niveau | Profil | Caractéristiques |
|---|---|---|
| **Socle** | Élèves en difficulté | Consignes décomposées, calculs amorcés, tableaux pré-remplis, rappels de méthode intégrés, contextes du quotidien, questions fermées |
| **Standard** | Majorité de la classe | Consignes complètes, contextes professionnels variés, rédaction attendue, toutes les capacités du programme |
| **Approfondissement** | Poursuite BTS/MC | Mise en équation autonome, problèmes multi-étapes, raisonnement justifié, questions type BTS, contextes complexes |

### Volume et barème

- **Barème** : 20 points par sujet (identique pour les 3 niveaux)
- **Volume** : 3 à 4 parties par sujet, 3 à 5 questions par partie
- **Durée** : 1 heure — calibrer en conséquence (ne pas surcharger)
- **Contextes** : varier les situations dans un même sujet (professionnel + quotidien ou scientifique)

---

## Structure HTML

### Template complet

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>DS Ch0X – Titre du chapitre – Niveau</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../../[sommaire].html" class="nb">← RETOUR SOMMAIRE</a>

<header>
  <h1>Devoir Surveillé – Chapitre X</h1>
  <p class="sous-titre">Titre du chapitre &nbsp;|&nbsp; Niveau Bac Pro</p>
</header>

<div class="dh">
  <div class="dh-item">🕑 <strong>Durée :</strong> 1 heure</div>
  <div class="dh-item">🧮 <strong>Calculatrice :</strong> autorisée</div>
  <div class="dh-item">✍ <strong>Barème :</strong> 20 points</div>
  <div class="dh-item">📄 <strong>Documents :</strong> non autorisés</div>
</div>

<div class="comp-legend">
  <span class="comp comp-app">APP – S'Approprier</span>
  <span class="comp comp-ana">ANA – Analyser</span>
  <span class="comp comp-rea">REA – Réaliser</span>
  <span class="comp comp-val">VAL – Valider</span>
  <span class="comp comp-com">COM – Communiquer</span>
</div>

<div class="objectifs">
  <strong>Compétences évaluées :</strong>
  <ul>
    <li><strong>S'approprier</strong> — [capacité 1]</li>
    <li><strong>Analyser</strong> — [capacité 2]</li>
    <li><strong>Réaliser</strong> — [capacité 3]</li>
    <li><strong>Valider</strong> — [capacité 4]</li>
  </ul>
</div>

<!-- ============================================================
     DS NIVEAU SOCLE
     ============================================================ -->
<div class="diff-socle">
<span class="tag-socle">Socle</span>

<div style="background:#f0fdf4;border:1px solid #86efac;border-radius:8px;padding:12px 16px;margin-bottom:20px;font-size:.93em">
  <strong style="color:#14532d">DS Socle – Titre du chapitre</strong><br>
  Lis bien chaque question avant de répondre. Les rappels de méthode sont fournis.
</div>

<!-- PARTIE A -->
<div class="partie">
  <div class="partie-header">
    <span class="partie-title">Partie A – Titre</span>
    <span class="pts">X points</span>
  </div>
  <p class="bareme">X pts par question.</p>

  <p>Énoncé de la situation...</p>

  <div class="q">
    <strong>1.</strong> <span class="comp comp-app">APP</span>
    Question guidée...
    <span class="bareme">(X pts)</span>
  </div>
  <span class="answer-line"></span>
  <span class="answer-line"></span>

  <button class="bc" onclick="toggle(this)">Voir la correction</button>
  <div class="corr">
    <p><strong>1.</strong> Correction...</p>
  </div>
</div>

</div><!-- fin diff-socle -->

<!-- ============================================================
     DS NIVEAU STANDARD
     ============================================================ -->
<div class="diff-standard">
<span class="tag-standard">Standard</span>

<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:8px;padding:12px 16px;margin-bottom:20px;font-size:.93em">
  <strong style="color:#1e40af">DS Standard – Titre du chapitre</strong><br>
  Durée : 1 heure | Calculatrice autorisée | Documents non autorisés
</div>

<!-- PARTIES A, B, C ... -->

</div><!-- fin diff-standard -->

<!-- ============================================================
     DS NIVEAU APPROFONDISSEMENT
     ============================================================ -->
<div class="diff-appro">
<span class="tag-appro">Approfondissement</span>

<div style="background:#f5f0ff;border:1px solid #c4b5fd;border-radius:8px;padding:12px 16px;margin-bottom:20px;font-size:.93em">
  <strong style="color:#4c1d95">DS Approfondissement – Titre du chapitre</strong><br>
  Durée : 1 heure | Calculatrice autorisée | Documents non autorisés
</div>

<!-- PARTIES A, B, C ... -->

</div><!-- fin diff-appro -->

</div><!-- fin .c -->

<script>
function toggle(btn){
  const corr=btn.nextElementSibling;
  if(corr.style.display==='block'){corr.style.display='none';btn.textContent='Voir la correction';}
  else{corr.style.display='block';btn.textContent='Masquer la correction';}
}
</script>
<script src="../../../nav.js"></script>
<script src="../../../diff.js"></script>
</body>
</html>
```

---

## Classes CSS spécifiques aux DS

Ces classes sont définies dans `styles.css` — **ne pas les redéfinir** dans la page :

| Classe | Usage |
|---|---|
| `.dh` | Bandeau durée/calculatrice/barème/documents |
| `.dh-item` | Élément du bandeau (icône + texte) |
| `.comp-legend` | Légende des compétences en haut du DS |
| `.comp` | Badge de compétence (petit, coloré) |
| `.comp-app` | Badge APP – bleu clair |
| `.comp-ana` | Badge ANA – jaune/orange |
| `.comp-rea` | Badge REA – vert clair |
| `.comp-val` | Badge VAL – violet clair |
| `.comp-com` | Badge COM – cyan |
| `.objectifs` | Encadré compétences évaluées |
| `.partie` | Bloc d'exercice (bordure arrondie) |
| `.partie-header` | En-tête de partie (titre + badge points) |
| `.partie-title` | Titre de la partie |
| `.pts` | Badge de points (fond couleur primaire) |
| `.bareme` | Texte petit gris pour indication de points |
| `.q` | Bloc question |
| `.answer-line` | Ligne de réponse (1 ligne ≈ 28px) |
| `.bc` | Bouton "Voir la correction" |
| `.corr` | Correction cachée (display:none) |

---

## Compétences à mobiliser

Chaque question doit être taguée avec la compétence qu'elle évalue. Distribuer les compétences sur l'ensemble du DS.

| Sigle | Compétence | Types de questions |
|---|---|---|
| `APP` | S'Approprier | Identifier, nommer, reconnaître, choisir dans une liste, compléter une phrase |
| `ANA` | Analyser | Évaluer, comparer, expliquer une situation, identifier un risque |
| `REA` | Réaliser | Calculer, compléter un tableau, construire un graphique, appliquer une formule |
| `VAL` | Valider | Vérifier une réponse, comparer au réel, juger si un résultat est cohérent |
| `COM` | Communiquer | Rédiger une réponse argumentée, expliquer à l'écrit, formuler un conseil |

**Équilibre recommandé :** APP + ANA + REA pour 70% des points, VAL + COM pour 30%.

---

## Types de questions disponibles

### Questions fermées (guidées — socle prioritairement)

```html
<!-- Cases à cocher -->
<p style="padding-left:1em">☐ Réponse A &nbsp;&nbsp; ☐ Réponse B &nbsp;&nbsp; ☐ Réponse C</p>

<!-- Compléter une phrase (trous) -->
<p>La grandeur mesurée est ………………… et son unité est …………………</p>
<span class="answer-line"></span>

<!-- Vrai/Faux -->
<p><strong>a)</strong> Le rayonnement nécessite un support matériel. ☐ Vrai &nbsp; ☐ Faux</p>

<!-- Relier (tableau 3 colonnes) -->
<table style="margin:8px 0;font-size:.9em">
  <tr><td style="padding-right:20px"><strong>Terme A</strong></td><td>• •</td><td style="padding-left:20px">Définition 1</td></tr>
  <tr><td style="padding-right:20px"><strong>Terme B</strong></td><td>• •</td><td style="padding-left:20px">Définition 2</td></tr>
</table>
```

### Questions ouvertes (calcul, rédaction — standard et appro)

```html
<!-- Calcul guidé par étapes (socle/standard) -->
<p><strong>Étape 1 :</strong> Identifier les données : \(m =\) ……… kg, \(g =\) ……… m/s²</p>
<p><strong>Étape 2 :</strong> Appliquer la formule : \(P = m \times g =\) ………</p>
<span class="answer-line"></span>
<span class="answer-line"></span>

<!-- Calcul libre (standard/appro) -->
<div class="q">
  <strong>2.</strong> <span class="comp comp-rea">REA</span>
  Calculer la valeur de ... <span class="bareme">(2 pts)</span>
</div>
<span class="answer-line"></span>
<span class="answer-line"></span>
<span class="answer-line"></span>

<!-- Rédaction argumentée (appro) -->
<div class="q">
  <strong>4.</strong> <span class="comp comp-com">COM</span>
  Rédiger un conseil argumenté : ... <span class="bareme">(2 pts)</span>
</div>
<span class="answer-line"></span>
<span class="answer-line"></span>
<span class="answer-line"></span>
<span class="answer-line"></span>
```

### Tableau à compléter

```html
<table class="full" style="margin:8px 0 14px;font-size:.92em">
  <thead>
    <tr><th>Grandeur</th><th>Symbole</th><th>Unité</th></tr>
  </thead>
  <tbody>
    <tr><td>Tension</td><td>\(U\)</td><td>…</td></tr>
    <tr><td>Intensité</td><td>…</td><td>ampère (A)</td></tr>
    <tr><td>Résistance</td><td>\(R\)</td><td>…</td></tr>
  </tbody>
</table>
```

---

## Figures et visuels dans les DS

### Règle fondamentale — données uniquement

**Un visuel dans un DS montre uniquement les données brutes fournies à l'élève.**

Il ne doit **jamais** :
- Montrer l'équation à construire
- Afficher la valeur inconnue ou la solution
- Tracer une droite que l'élève doit tracer lui-même
- Indiquer un point d'intersection que l'élève doit déterminer

Il doit **toujours** servir de support de compréhension, pas de support de correction.

> **Règle mnémotechnique :** *"Ce que l'élève a le droit de voir sur sa copie, et rien de plus."*

### Quand ajouter un tableau de données

**Règle systématique :** dès qu'un exercice présente des valeurs numériques (prix, mesures, quantités, résultats), les regrouper dans un tableau avant les questions — même si le texte les cite déjà.

```html
<!-- Avant les questions, dans la situation -->
<table class="full" style="margin:8px 0 14px;font-size:.92em;max-width:360px">
  <thead><tr><th>Donnée</th><th>Valeur</th></tr></thead>
  <tbody>
    <tr><td>Puissance du radiateur</td><td>2 000 W</td></tr>
    <tr><td>Durée de fonctionnement</td><td>8 h</td></tr>
    <tr><td>Prix du kWh</td><td>0,18 €</td></tr>
  </tbody>
</table>
```

**Ne jamais ajouter** de ligne "Résultat", "Énergie = ?", "Coût à calculer" — ce sont les questions.

### Quand ajouter un schéma SVG

**Obligatoire** si l'énoncé cite un objet physique à analyser ou à mesurer :
- Situation géométrique (pièce, objet coté, figure)
- Schéma de circuit électrique
- Objet coupé, plié, assemblé (menuiserie)
- Schéma de montage (laboratoire)
- Bilan de forces
- Graphique à lire (oscillo, T(t), courbe)

**Optionnel mais recommandé** pour contextualiser une situation professionnelle (ex : dessin d'une étagère avec les dimensions données).

### Style SVG

```html
<figure class="schema" style="text-align:center;margin:10px 0 14px">
  <svg width="280" height="180" viewBox="0 0 280 180" xmlns="http://www.w3.org/2000/svg">
    <!-- fill données : #ebf5ff (maths) ou #f5f0ff (PC) selon matière -->
    <!-- stroke : var(--p) ou la couleur primaire -->
    <!-- inconnues : fill="#c53030" italic bold -->
    <!-- labels : fill="#555" -->
  </svg>
  <figcaption style="font-size:.88em;color:#555;margin-top:4px">Légende du schéma</figcaption>
</figure>
```

**Conventions de couleur :**

| Matière | Fond formes | Trait | Inconnue |
|---|---|---|---|
| Maths Seconde | `#ebf5ff` | `#0056b3` | `#c53030` italique |
| PC Seconde | `#f5f0ff` | `#6f42c1` | `#c53030` italique |
| Maths Première/Terminale | `#dbeafe` | `#0969da` | `#c53030` italique |
| PC Première | `#dbeafe` ou `#f0fff4` | selon filière | `#c53030` italique |

### Visuels dans les DS — statiques uniquement

Toutes les pages du site fonctionnent en ligne et à l'impression. Dans les DS :
- **SVG statique** ✓ — format privilégié
- **Chart.js** ✓ — acceptable si rendu une seule fois (pas d'animation)
- **Canvas animé** ✗ — réservé aux leçons et simulations

L'élève observe et lit les figures — il ne les manipule pas.

### Repère vierge (graphique à compléter)

Pour les exercices de lecture ou de tracé graphique, fournir un repère avec axes et grille **sans aucune droite tracée** :

```html
<figure class="schema" style="text-align:center;margin:10px 0 14px">
  <svg width="280" height="200" viewBox="0 0 280 200" xmlns="http://www.w3.org/2000/svg">
    <!-- Grille -->
    <g stroke="#e5e7eb" stroke-width="0.5">
      <!-- lignes horizontales et verticales -->
    </g>
    <!-- Axes uniquement — PAS de droite tracée -->
    <line x1="40" y1="10" x2="40" y2="170" stroke="#374151" stroke-width="1.5"/>
    <line x1="30" y1="160" x2="270" y2="160" stroke="#374151" stroke-width="1.5"/>
    <!-- Labels des axes -->
    <text x="275" y="164" fill="#555" font-size="11">x</text>
    <text x="44" y="8" fill="#555" font-size="11">y</text>
  </svg>
  <figcaption style="font-size:.88em;color:#555;margin-top:4px">Repère vierge — utiliser pour répondre</figcaption>
</figure>
```

### Schéma de situation (SVG contextuel)

Pour les situations texte qui décrivent un objet physique :

```html
<!-- Exemple : barre de bois de 180 cm découpée en 3 morceaux de longueur x, x, et 60 cm -->
<figure class="schema" style="text-align:center;margin:10px 0 14px">
  <svg width="300" height="60" viewBox="0 0 300 60">
    <!-- Rectangle principal (données brutes) -->
    <rect x="20" y="20" width="260" height="20" fill="#ebf5ff" stroke="#0056b3" stroke-width="1.5" rx="3"/>
    <!-- Longueur totale donnée -->
    <text x="150" y="15" text-anchor="middle" fill="#555" font-size="11">180 cm (donnée)</text>
    <!-- Trait de coupe -->
    <line x1="106" y1="15" x2="106" y2="45" stroke="#374151" stroke-width="1" stroke-dasharray="3,2"/>
    <!-- Inconnues : pas de valeur affichée -->
  </svg>
  <figcaption style="font-size:.88em;color:#555;margin-top:4px">Barre de bois — longueur totale : 180 cm</figcaption>
</figure>
```

---

## Corrections

### Règles de rédaction des corrections

1. **Détaillées et pédagogiques** — montrer chaque étape du calcul
2. **Avec les formules** — écrire la formule, puis l'application numérique, puis le résultat
3. **Unités systématiques** — chaque résultat numérique porte son unité
4. **Justifications** — pour VAL et COM, expliquer le raisonnement en phrases

```html
<button class="bc" onclick="toggle(this)">Voir la correction</button>
<div class="corr">
  <p><strong>1.</strong> Les grandeurs sont <strong>proportionnelles</strong> (production régulière).</p>
  <p><strong>2.</strong> \( k = \dfrac{120}{8} = \mathbf{15} \) pièces/heure</p>
  <p><strong>3.</strong> Pour 11 heures : \( 15 \times 11 = \mathbf{165} \) pièces</p>
  <p><strong>4. VAL :</strong> 165 pièces est cohérent — c'est plus que 120 (8h) et moins que 180 (12h). ✓</p>
</div>
```

### Une correction par partie

Placer un bouton `.bc` + `.corr` **à la fin de chaque partie**, pas après chaque question. Cela préserve la cohérence de l'évaluation et évite de trop fragmenter.

---

## Adaptation par matière

### Mathématiques

**Structure type :**
- Partie A : notion centrale du chapitre (proportionnalité, équation, fonction, etc.)
- Partie B : application dans un contexte professionnel
- Partie C (appro) : problème ouvert ou mise en équation autonome

**Types de questions privilégiés :**
- Calculer une valeur, compléter un tableau de valeurs
- Résoudre une équation, lire un graphique
- Compléter un tableau de variations ou de signes
- Construire un graphique (repère vierge fourni)
- Mettre en équation une situation (appro)

**Contextes professionnels :** menuiserie, agencement, chantier, devis, fabrication en série.

### Physique-Chimie

**Structure type :**
- Partie A : notions de cours (définitions, unités, pictogrammes, protocoles)
- Partie B : application numérique (formule + calcul)
- Partie C : analyse d'une situation (contexte professionnel, sécurité, environnement)

**Types de questions privilégiés :**
- Schémas à légender ou à compléter (circuit, montage, bilan de forces)
- Calculs avec formule fournie (socle) ou à retrouver (standard/appro)
- Tableaux de mesures à compléter
- Analyse d'un oscillogramme ou d'une courbe
- Rédaction d'une consigne de sécurité

**Contextes professionnels :** atelier de menuiserie, installation électrique, chauffage, laboratoire. Ne jamais utiliser les sigles ICCER, ERA, MAMA, ERA-MA dans le contenu.

---

## Structure des parties selon le niveau

### Socle — principes de rédaction

- **Rappels intégrés** : encadré `.meth` ou phrase "Rappel : formule =" avant les questions
- **Calculs amorcés** : `\(U = R \times I = \ldots \times \ldots =\)` ………
- **Tableaux pré-remplis partiellement** : certaines cellules complétées
- **Questions fermées** : cases à cocher, compléter une phrase à trous, relier
- **Étapes numérotées** : "Étape 1 : Étape 2 : Étape 3 :"
- **Contextes simples** : quotidien, situations concrètes et familières

### Standard — principes de rédaction

- **Consignes complètes** : pas de guidage pas-à-pas
- **Formule à rappeler** : "Rappel : P = U × I" seulement si c'est une formule secondaire
- **Calculs intégraux** : l'élève écrit toutes les étapes
- **Contextes professionnels** : menuisier, installateur, technicien...
- **Rédaction attendue** : justifier, expliquer, argumenter pour COM

### Approfondissement — principes de rédaction

- **Mise en équation autonome** : aucune formule fournie
- **Problèmes à plusieurs étapes** : l'élève doit planifier sa démarche
- **Questions ouvertes** : "Choisir et justifier", "Rédiger un conseil", "Comparer"
- **Vocabulaire technique** : termes du programme BTS si pertinents
- **Contextes complexes** : deux grandeurs qui varient, optimisation, comparaison de solutions

---

## Mise en page et impression

### Espacement des réponses

Adapter le nombre de lignes `.answer-line` à la complexité attendue :
- 1 ligne → réponse courte (1 mot, 1 valeur)
- 2 lignes → phrase courte ou 1 calcul
- 3-4 lignes → rédaction ou calcul développé
- 5+ lignes → paragraphe argumenté (COM, appro)

```html
<!-- Réponse courte -->
<span class="answer-line"></span>

<!-- Calcul développé -->
<span class="answer-line"></span>
<span class="answer-line"></span>
<span class="answer-line"></span>
```

### Sauts de page à l'impression

Si un DS dépasse une page A4, utiliser pour éviter les coupures malheureuses :

```html
<div class="partie" style="break-inside:avoid">
  ...
</div>
```

### Boutons masqués à l'impression

`print.css` masque automatiquement `.bc` et `.nb`. Ne pas surcharger avec du CSS inline.

---

## Vérification scientifique

Avant de valider un DS :

- **Refaire chaque calcul** des corrections — notamment les unités
- **Vérifier le barème** : total = 20 points exactement par sujet
- **Vérifier la cohérence des données** : les valeurs numériques doivent être réalistes
- **Vérifier le programme** : chaque capacité attendue du chapitre est couverte dans au moins un des 3 sujets
- **Formules** : conformes au niveau (signaler avec **(HP)** si hors programme)
- **Contextes PC** : valeurs physiques réalistes (ex : g = 9,81 m/s², son dans l'air = 340 m/s)

---

## Règles de contexte professionnel

Identiques à toutes les autres pages du site :

**Interdit dans le contenu pédagogique :**
- ~~"Un technicien ICCER..."~~ → "Un installateur thermique..."
- ~~"Un technicien ERA-MA..."~~ → "Un menuisier agenceur..."
- ~~"Contexte ERA-MA"~~ → "Contexte professionnel"

**Varier les contextes :** professionnel + vie quotidienne + sport + science + énergie.

---

## Checklist avant publication

### Structure
- [ ] 3 niveaux complets : `diff-socle`, `diff-standard`, `diff-appro`
- [ ] Bandeau `dh` (durée, calculatrice, barème, documents)
- [ ] `comp-legend` présent
- [ ] Encadré `objectifs` avec compétences évaluées
- [ ] Bandeau intro de niveau (vert socle / bleu standard / violet appro)
- [ ] 3 à 4 parties par sujet
- [ ] Barème total = 20 pts pour chaque niveau

### Technique
- [ ] `styles.css` et `print.css` inclus
- [ ] CSS variables `:root{--p:...;--p-bg:...;--p-border:...}` correctes selon la matière/niveau
- [ ] `MathJax` inclus (si formules `\(...\)` ou `\[...\]`)
- [ ] `nav.js` inclus en fin de `<body>`
- [ ] `diff.js` inclus en fin de `<body>`
- [ ] Fonction `toggle(btn)` définie dans un `<script>` inline
- [ ] Lien retour → `../../../[sommaire].html`
- [ ] Classes `.bc`, `.corr`, `.q`, `.partie`, etc. non redéfinies en inline

### Pédagogie
- [ ] Chaque question taguée avec la compétence `.comp .comp-XXX`
- [ ] Compétences distribuées (APP + ANA + REA + VAL + COM)
- [ ] Corrections complètes (une par partie)
- [ ] Corrections pédagogiques (étapes + justifications + unités)
- [ ] Rappels de méthode (`.meth`) au niveau Socle uniquement
- [ ] Contextes professionnels variés (sans sigles de filière)
- [ ] Niveau de complexité croissant socle → appro
- [ ] Programme officiel couvert

### Visuels
- [ ] Tableau de données `<table class="full">` pour toute situation avec valeurs numériques
- [ ] Tableau montre UNIQUEMENT les données — jamais l'équation, la solution, ou l'inconnue
- [ ] SVG présent si l'énoncé décrit un objet géométrique, un schéma ou un graphique
- [ ] Repère vierge (axes + grille, sans droite) pour exercice de tracé graphique
- [ ] `<figure class="schema">` + `<figcaption>` autour de chaque SVG
- [ ] Conventions couleur respectées selon la matière

---

## Points de contrôle finaux

Avant de soumettre le DS généré, vérifier :

1. **Un seul contexte par partie** — ne pas mélanger deux situations dans la même partie
2. **Les 3 sujets couvrent le même programme** — un élève socle et un élève appro ont accès au même savoir
3. **Le sujet appro ne fait pas l'impasse sur les notions de base** — il les aborde différemment (plus de mise en équation)
4. **Chaque ligne `.answer-line`** correspond à un espace de rédaction réaliste
5. **Les données numériques sont cohérentes entre elles** — ex : si la production est de 15 pièces/h et qu'on demande la production sur 8h, le résultat de la correction doit être 120, pas 118
