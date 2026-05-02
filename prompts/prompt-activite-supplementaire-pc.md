# Prompt de référence — Activités supplémentaires en physique-chimie

Guide de référence pour la création d'**activités supplémentaires** dans un chapitre de physique-chimie qui possède déjà une `activite.html` principale.

> **Lire d'abord :** `prompts/prompt-activite.md` (cadre général des activités). Ce prompt-ci ne **remplace pas** le prompt principal — il **le complète** pour le cas particulier des activités additionnelles.

---

## 1. Différence avec l'activité principale

| Page | Rôle | Position dans la séquence |
|---|---|---|
| `activite.html` | **Découverte** : amène la notion par investigation. L'élève ne connaît pas encore le cours. | Avant ou pendant `lecon.html` |
| `activite-2-…html`, `activite-3-…html`, … | **Réinvestissement / approfondissement** : la notion est connue, on la met en œuvre dans un nouveau contexte. | Après `lecon.html` |

L'activité supplémentaire **n'est pas redondante** avec la principale : elle apporte un **angle nouveau** (autre métier, autre type de données, autre démarche, autre niveau).

### Pourquoi en créer ?

- **Choix pour le professeur** selon son public et son temps : 6 activités de 30 min permettent de varier d'une année à l'autre, ou d'adapter à 3 classes différentes.
- **Différenciation horizontale** : un élève rapide peut faire l'activité 2 pendant que les autres terminent l'activité 1.
- **Devoir maison / co-intervention** : certains formats (mesure chez soi, diagnostic, projet) demandent du temps hors classe.
- **Compétences variées** : couvrir l'ensemble du référentiel (APP/ANA/REA/VAL/COM) en multipliant les contextes.

---

## 2. Six formats d'activité supplémentaire

Choisir **un seul** format par activité — ne pas mélanger.

| # | Format | Compétences dominantes | Durée | Quand l'utiliser |
|---|---|---|---|---|
| **A** | **Situation professionnelle ciblée** | APP / REA | 25–30 min | Réinvestir dans un autre métier que celui de l'activité principale |
| **B** | **Étude de cas / fiche technique** | ANA / REA | 30–40 min | Lire une notice/datasheet et en extraire des grandeurs |
| **C** | **TP numérique (simulation, tableur)** | REA / VAL | 40–50 min | Faire varier un paramètre et observer |
| **D** | **Devoir maison expérimental** | REA | 20–30 min (chez soi) | Mesure simple à faire à la maison |
| **E** | **Diagnostic / dépannage** | ANA / VAL | 30–40 min | Identifier une panne ou un dysfonctionnement à partir d'indices |
| **F** | **Projet ouvert / mini-investigation** | ANA / VAL / COM | 40–60 min | Résolution autonome d'une question ouverte (type CCF) |

### Exemples par chapitre (ch06 ICCER — Transport par un fluide)

| Format | Activité concrète |
|---|---|
| A | Remplissage d'un ballon ECS chez un client (calculs Q<sub>v</sub>, t = V/Q<sub>v</sub>) |
| B | Choisir une pompe : lecture d'une fiche technique constructeur, point de fonctionnement |
| C | TP simulateur de débit en ligne, faire varier le diamètre et observer |
| D | Mesurer le débit des robinets de chez soi avec chrono + récipient gradué |
| E | Diagnostic d'une fuite : à partir du compteur d'eau, retrouver le débit de fuite |
| F | Effet Venturi : comprendre pourquoi une buse de pulvérisation aspire le produit |

---

## 3. Convention de nommage

### Fichiers

- L'activité principale conserve le nom **`activite.html`** (ne jamais la renommer).
- Les activités supplémentaires sont nommées **`activite-N-slug.html`** où :
  - `N` est le numéro d'ordre (2, 3, 4, …)
  - `slug` est un mot-clé descriptif en kebab-case (ex : `remplissage-ballon-ecs`, `effet-venturi`)

**Exemples :**
```
physique-chimie/terminale-iccer/ch06/
├── activite.html                              ← découverte (existante)
├── activite-2-remplissage-ballon-ecs.html     ← format A
├── activite-3-mesure-debit-domestique.html    ← format D
├── activite-4-effet-venturi.html              ← format F
└── activite-5-choisir-pompe.html              ← format B
```

### Titre HTML

```html
<title>ChNN – Activité N – Titre court – Niveau (Filière)</title>
```

### Titre `<h1>`

```html
<h1>Activité N – Titre descriptif <span style="font-size:.55em;color:#7c3aed;font-weight:600">DEVOIR MAISON</span></h1>
```

Le badge en gris (ou violet pour DM, vert pour TP numérique) permet d'identifier visuellement le format.

---

## 4. Structure HTML d'une activité supplémentaire

Identique à l'activité principale, avec **3 différences**.

### Différence 1 — En-tête

Sous-titre allégé : pas besoin de redonner les objectifs du chapitre, juste ceux de **cette activité**.

```html
<header>
  <h1>Activité N – Titre</h1>
  <p class="sous-titre">Chapitre NN – Titre du chapitre | Niveau | Matière | ⏱ Durée</p>
</header>

<div class="objectifs">
  <strong>Objectifs :</strong>
  <ul>
    <li>Objectif spécifique 1 (différent de ceux de l'activité principale)</li>
    <li>Objectif spécifique 2</li>
  </ul>
</div>
```

### Différence 2 — Pas de notion à découvrir

L'encadré `.retenir` final ne **redéfinit pas** la notion (déjà dans `lecon.html`). Il rappelle :
- les **formules clés** utilisées dans l'activité
- les **ordres de grandeur** rencontrés
- une **règle pratique** issue de l'activité

```html
<div class="retenir">
  <strong>À retenir</strong>
  <ul>
    <li><strong>Relation utilisée :</strong> formule</li>
    <li><strong>Ordre de grandeur :</strong> valeur typique du contexte</li>
    <li><strong>Règle pratique :</strong> astuce de terrain</li>
  </ul>
</div>
```

### Différence 3 — Lien vers l'activité principale (recommandé)

Si l'activité réutilise une notion vue dans la principale, ajouter un rappel discret :

```html
<p style="margin:8px 0;padding:8px 12px;background:#fef3c7;border-left:3px solid #b45309;font-size:.9em">
  💡 Notion vue dans <a href="activite.html">l'activité de découverte</a> et formalisée dans la <a href="lecon.html">leçon</a>.
</p>
```

---

## 5. Mise à jour de `index.html` du chapitre

Quand on ajoute des activités supplémentaires, mettre à jour la page sommaire du chapitre pour les lister.

### Section « Découvrir et apprendre »

Ajouter une carte par activité supplémentaire, avec le format suivant :

```html
<a href="activite-2-remplissage-ballon-ecs.html" class="ress-card">
  <div class="ress-icon">🧭</div>
  <h3>Activité 2 — Remplissage d'un ballon ECS</h3>
  <p>Calculer un temps de remplissage à partir d'un débit donné.</p>
  <span class="ress-tag">~25 min · APP/REA</span>
</a>
```

### Compteur de ressources

Mettre à jour le compteur dans le hero : `<div class="meta"><span>X ressources</span></div>`

---

## 6. Règles spécifiques par format

### Format D — Devoir maison

- Préciser explicitement **DEVOIR MAISON** dans le titre et la consigne d'introduction
- Lister le **matériel** que l'élève doit avoir chez lui (pas de matériel rare)
- Donner une **grille de retour attendu** : feuille papier, photo, fichier numérique
- Inclure une **partie « pistes de réponse »** plutôt qu'une correction stricte (les mesures varient)

### Format C — TP numérique

- Préciser le **logiciel ou le simulateur** utilisé (URL stable, simulation locale du site, tableur)
- Privilégier les simulations **déjà présentes dans `simulations/`** du site
- Si tableur : fournir un **modèle Excel/Calc téléchargeable** ou décrire précisément les colonnes attendues
- Penser à la **reproductibilité** : un élève absent doit pouvoir refaire le TP chez lui

### Format E — Diagnostic

- Partir d'un **scénario réaliste** (compteur, alarme, plainte client)
- Donner **plusieurs indices** dont certains sont des distracteurs
- La conclusion doit être **argumentée** (compétence VAL prédominante)

### Format F — Projet ouvert

- Une **seule question principale** large, posée en début d'activité
- L'élève **construit son raisonnement** : il choisit ses données, ses hypothèses, ses calculs
- Prévoir **3 à 5 questions guides** (étapes facultatives) pour les élèves qui ont besoin d'un cadre
- Évaluation par compétences (grille jointe optionnelle)

---

## 7. Données et contextes

Reprendre intégralement les règles de `prompts/prompt-activite.md` :

- **Métiers réels** dans le contenu (jamais ICCER, ERA, MA, MAMA — voir `CLAUDE.md`)
- **Données numériques réalistes** : ordres de grandeur cohérents avec le métier
- **Programme officiel** : ne pas dépasser le niveau du chapitre
- **Toutes les données nécessaires** dans l'énoncé (l'élève ne cherche pas dehors)

### Métiers à privilégier en physique-chimie selon la filière

| Filière | Activité 2-3 | Activité 4-5 (variation) | Activité 6+ (extension) |
|---|---|---|---|
| ICCER | plombier chauffagiste, technicien CVC | installateur PAC, technicien climatisation | thermicien, bureau d'études |
| ERA-MA | menuisier agenceur, ébéniste | poseur de cuisine, technicien d'agencement | architecte d'intérieur |
| Gpt 1 (industriel) | technicien de maintenance | régleur, opérateur CN | ingénieur procédés |
| CAP | aide-installateur, apprenti | ouvrier qualifié | — |
| Seconde | métiers de la famille | quotidien (sport, maison) | sciences (laboratoire, espace) |

Varier les métiers d'une activité à l'autre dans le même chapitre.

---

## 8. Cohérence avec l'activité principale

Avant de rédiger une activité supplémentaire :

1. **Lire `activite.html`** : noter le contexte, les données, les compétences travaillées
2. **Lire `lecon.html`** : identifier la notion centrale et les formules à mobiliser
3. **Lire `exercices.html`** : ne pas refaire un exercice déjà présent
4. **Choisir un format différent** : si activité principale = situation pro classique, l'activité 2 peut être un TP numérique ou un DM

### Test de différenciation

Une activité supplémentaire est **valide** si l'on peut répondre OUI à au moins **2 questions** sur 3 :

| Question | OUI / NON |
|---|---|
| L'activité utilise un **contexte différent** (autre métier, autre situation) ? | … |
| L'activité travaille une **compétence dominante différente** ? | … |
| L'activité utilise un **format différent** (cf. tableau §2) ? | … |

Sinon, c'est probablement un doublon — fusionner ou retravailler.

---

## 9. Visuels

### Règle absolue — héritée du prompt principal

Toute question qui demande de lire/analyser un visuel doit fournir le **SVG inline** correspondant.

### Visuels typiques par format

| Format | Visuel à privilégier |
|---|---|
| A — Situation pro | Schéma de l'installation, plan coté de la pièce |
| B — Fiche technique | Reproduction simplifiée de la fiche (tableau + courbe SVG) |
| C — TP numérique | Capture-style du simulateur, tableau résultats |
| D — DM | Schéma du protocole (matériel + grandeurs mesurées) |
| E — Diagnostic | Schéma de l'installation avec indicateur de panne |
| F — Projet | Schéma général + données dispersées |

### Conventions SVG (rappel)

- `viewBox` cadré sur le contenu, **pas** d'attributs `width/height` fixes
- Couleurs thématisées par filière (variables `--p`, `--p-bg`)
- Légendes en `<text>` SVG avec police 11–12 px
- Attribut `role="img"` + `aria-label` descriptif pour l'accessibilité

---

## 10. Différenciation

L'activité supplémentaire peut intégrer la différenciation **`diff.js`** (voir `CLAUDE.md`) :

- **Socle** : aides explicites, calculs amorcés, tableaux pré-remplis
- **Standard** : énoncé classique, sans aide
- **Approfondissement** : questions bonus en fin d'activité (ouverture vers BTS)

Mais ce n'est **pas obligatoire** : la plupart des activités supplémentaires peuvent rester en base commune (un seul niveau).

Si différenciation activée, ajouter `<script src="../../../diff.js"></script>` en fin de body.

---

## 11. Checklist avant publication

### Cohérence pédagogique
- [ ] L'activité **n'est pas un doublon** de `activite.html` ou de `exercices.html`
- [ ] Le **format** (§2) est identifiable (un seul des 6)
- [ ] Le **contexte** est différent de celui de l'activité principale
- [ ] La **notion** travaillée est **dans le programme** du chapitre
- [ ] Les **compétences** sont équilibrées (au moins 2 différentes)

### Contenu
- [ ] Durée estimée indiquée dans le sous-titre
- [ ] Objectifs spécifiques formulés (différents de ceux de la leçon)
- [ ] Toutes les données utiles présentes dans l'énoncé
- [ ] **Aucun sigle de filière** (ICCER, ERA-MA, MAMA, …) dans le corps de l'activité
- [ ] Métier réel et nommé dans la situation
- [ ] Correction complète pour chaque question (bouton « Voir la correction »)
- [ ] Encadré « À retenir » avec formules / ordres de grandeur / règles pratiques (pas de redéfinition de notion)

### Technique
- [ ] Nom de fichier `activite-N-slug.html` (kebab-case, slug court)
- [ ] `<title>` au format `ChNN – Activité N – Titre – Niveau`
- [ ] Couleurs CSS thématisées (variables `--p`, `--p-bg`, `--p-border`)
- [ ] MathJax inclus si formules
- [ ] `print.css` inclus
- [ ] `nav.js` inclus
- [ ] **SVG inline** pour tout visuel demandé à l'élève
- [ ] **`index.html` du chapitre mis à jour** avec une carte vers cette activité
- [ ] Compteur de ressources de `index.html` mis à jour

---

## 12. Modèle minimal (squelette)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChNN – Activité N – Titre – Niveau (Filière)</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:#0969da;--p-bg:#dbeafe;--p-border:#93c5fd}</style>
</head>
<body>
<div class="c">
<a href="../../../pc-LIEN-SOMMAIRE.html" class="nb">← RETOUR SOMMAIRE</a>

<header>
  <h1>Activité N – Titre <span style="font-size:.55em;color:#6b7280;font-weight:600">FORMAT (DM, TP, …)</span></h1>
  <p class="sous-titre">Chapitre NN – Titre du chapitre | Niveau | Matière | ⏱ Durée</p>
</header>

<button onclick="window.print()" style="margin:10px 0;padding:8px 18px;border:1px solid #ccc;border-radius:6px;background:#f8fafc;cursor:pointer;font-size:.9em;font-weight:600">🖨️ Imprimer cette activité</button>

<div class="objectifs">
  <strong>Objectifs :</strong>
  <ul>
    <li>Objectif spécifique 1</li>
    <li>Objectif spécifique 2</li>
  </ul>
</div>

<!-- (optionnel) Lien vers l'activité de découverte -->
<p style="margin:8px 0;padding:8px 12px;background:#fef3c7;border-left:3px solid #b45309;font-size:.9em">
  💡 Notion vue dans <a href="activite.html">l'activité de découverte</a> et formalisée dans la <a href="lecon.html">leçon</a>.
</p>

<!-- SITUATION / DOCUMENT D'ACCROCHE -->
<div class="situation">
  <h2>Situation</h2>
  <p><em>Contexte avec un métier réel nommé.</em></p>
  <!-- Tableau, données, schéma SVG -->
</div>

<!-- PROBLÉMATIQUE -->
<div class="objectifs" style="border-left:4px solid var(--p);background:var(--p-bg);padding:14px 18px;border-radius:0 8px 8px 0;margin:16px 0">
  <strong>Problématique :</strong> Question centrale concrète.
</div>

<!-- QUESTIONS -->
<div class="exo">
  <h2>Question 1 <span class="badge-green">APP</span></h2>
  <p>Consigne…</p>
  <button class="bc" onclick="toggle(this)">Voir la correction</button>
  <div class="corr">…</div>
</div>

<!-- … -->

<!-- A RETENIR (formules / ordres de grandeur / règles pratiques) -->
<div class="retenir">
  <strong>À retenir</strong>
  <ul>
    <li><strong>Formule clé :</strong> …</li>
    <li><strong>Ordre de grandeur :</strong> …</li>
    <li><strong>Règle pratique :</strong> …</li>
  </ul>
</div>

</div>
<script src="../../../nav.js"></script>
</body>
</html>
```

---

## 13. Pour les maths ?

Les principes (formats A–F, nommage, mise à jour de `index.html`, checklist) s'appliquent **également aux activités supplémentaires de mathématiques**. Adaptations :

- Privilégier les formats **A** (situation pro), **C** (TP tableur/GeoGebra) et **F** (projet ouvert type CCF)
- Le format **D** (devoir maison) est plus rare en maths et concerne souvent un projet long (statistique sur données réelles, étude d'une suite via tableur)
- Les visuels sont obligatoires pour : courbes, figures géométriques, diagrammes, arbres de probabilités

Voir `prompts/prompt-activite.md` pour les détails par compétence.
