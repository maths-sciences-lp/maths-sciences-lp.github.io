# Skill : Générer un devoir surveillé (`ds.html`)

## Usage

```
/generate-ds <chemin-chapitre>
```

Exemple : `/generate-ds maths/seconde/ch05`

## Instructions

Tu dois générer une page `ds.html` complète pour le chapitre indiqué.

### Étape 1 — Collecter le contexte

1. **Lire `lecon.html`** du chapitre pour identifier les notions, définitions, propriétés et méthodes
2. **Lire `prompts/prompt-ds.md`** pour les règles de rédaction des DS (structure, barème, compétences, visuels, corrections)
3. **Lire `prompts/regles-communes.md`** pour les règles visuels, données uniquement, références orphelines
4. **Lire le programme officiel** dans `/pdf/` pour le niveau correspondant — extraire les capacités du module
5. **Identifier le prompt de filière** correspondant et le lire :
   - Seconde MAMA : `prompts/prompt-filiere-2mama.md`
   - Première ICCER : `prompts/prompt-filiere-premiere-iccer.md`
   - Première ERA : `prompts/prompt-filiere-premiere-era.md`
   - Terminale ICCER : `prompts/prompt-filiere-ticcer.md`
   - Terminale ERA/MA : `prompts/prompt-filiere-era-ma.md`
   - CAP MIT : `prompts/prompt-filiere-cap-mit.md`
   - CAP Ébéniste : `prompts/prompt-filiere-cap-ebeniste.md`
   - CAP SDG : `prompts/prompt-filiere-cap-sdg.md`
   - BTS : `prompts/prompt-bts.md`
6. **Lire `exercices.html`** du chapitre si existant — pour éviter de dupliquer les mêmes énoncés
7. **Consulter les audits** dans `/audits/` pour vérifier s'il y a des remarques sur ce chapitre

### Étape 2 — Déterminer le thème couleur

| Dossier | `--p` | `--p-bg` | `--p-border` |
|---|---|---|---|
| `maths/seconde` | `#0056b3` | `#ebf5ff` | `#bee3f8` |
| `maths/premiere` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `maths/terminale` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `maths/cap` | `#b45309` | `#fffbeb` | `#fde68a` |
| `maths/bts` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/seconde` | `#6f42c1` | `#f5f0ff` | `#c4b5fd` |
| `physique-chimie/premiere-iccer` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/premiere-era` | `#2da44e` | `#f0fff4` | `#86efac` |
| `physique-chimie/terminale-iccer` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/terminale-era` | `#2da44e` | `#f0fff4` | `#86efac` |
| `physique-chimie/cap` | `#6f42c1` | `#f5f0ff` | `#c4b5fd` |

### Étape 3 — Générer le DS

Créer le fichier `ds.html` dans le dossier du chapitre avec **3 sujets différenciés** (sauf BTS/CAP : un seul sujet).

### Structure HTML obligatoire

Suivre le template complet défini dans `prompts/prompt-ds.md` :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>DS ChXX – Titre – Niveau</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:BG;--p-border:BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../../[sommaire].html" class="nb">← RETOUR SOMMAIRE</a>

<header>
  <h1>Devoir Surveillé – Chapitre X</h1>
  <p class="sous-titre">Titre du chapitre | Niveau Bac Pro</p>
</header>

<!-- Bandeau durée/barème -->
<div class="dh">
  <div class="dh-item">🕑 <strong>Durée :</strong> 1 heure</div>
  <div class="dh-item">🧮 <strong>Calculatrice :</strong> autorisée</div>
  <div class="dh-item">✍ <strong>Barème :</strong> 20 points</div>
  <div class="dh-item">📄 <strong>Documents :</strong> non autorisés</div>
</div>

<!-- Légende compétences -->
<div class="comp-legend">
  <span class="comp comp-app">APP – S'Approprier</span>
  <span class="comp comp-ana">ANA – Analyser</span>
  <span class="comp comp-rea">REA – Réaliser</span>
  <span class="comp comp-val">VAL – Valider</span>
  <span class="comp comp-com">COM – Communiquer</span>
</div>

<!-- Compétences évaluées -->
<div class="objectifs">
  <strong>Compétences évaluées :</strong>
  <ul>
    <li><strong>S'approprier</strong> — [capacité]</li>
    <li><strong>Réaliser</strong> — [capacité]</li>
    <li><strong>Valider</strong> — [capacité]</li>
    <li><strong>Communiquer</strong> — [capacité]</li>
  </ul>
</div>

<!-- DS SOCLE -->
<div class="diff-socle">
<span class="tag-socle">Socle</span>
<!-- 3-4 parties, barème 20 pts, rappels .meth, calculs amorcés -->
</div>

<!-- DS STANDARD -->
<div class="diff-standard">
<span class="tag-standard">Standard</span>
<!-- 3-4 parties, barème 20 pts, contextes pro variés -->
</div>

<!-- DS APPROFONDISSEMENT -->
<div class="diff-appro">
<span class="tag-appro">Approfondissement</span>
<!-- 3-4 parties, barème 20 pts, problèmes ouverts -->
</div>

</div>

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

### Différenciation pédagogique — les 3 sujets

Chaque DS est proposé en **3 versions complètes** (pas 3 exercices d'un même sujet) :

| Niveau | Classe CSS | Tag | Contenu |
|---|---|---|---|
| **Socle** | `.diff-socle` | `.tag-socle` | Rappels `.meth`, calculs amorcés (`U = R × I = … × … =`), tableaux pré-remplis, questions fermées, étapes numérotées, contextes du quotidien |
| **Standard** | `.diff-standard` | `.tag-standard` | Consignes complètes, calculs intégraux, contextes professionnels variés, rédaction attendue pour COM |
| **Approfondissement** | `.diff-appro` | `.tag-appro` | Aucune formule fournie, mise en équation autonome, problèmes multi-étapes, questions ouvertes, vocabulaire BTS |

### Règles de contenu

- **Barème** : 20 points par sujet (identique pour les 3 niveaux)
- **Volume** : 3 à 4 parties par sujet, 3 à 5 questions par partie
- **Durée** : 1 heure — calibrer en conséquence
- **Compétences** : chaque question taguée `.comp .comp-XXX` (APP, ANA, REA, VAL, COM)
- **Équilibre** : APP + ANA + REA pour 70% des points, VAL + COM pour 30%
- **Corrections** : une par partie (bouton `.bc` + `.corr`), détaillées avec formule + AN + résultat + unité
- **Lignes de réponse** : `.answer-line` adaptées à la complexité (1 à 5 lignes)
- **Contextes variés** : professionnel + quotidien + scientifique
- Ne JAMAIS utiliser les sigles ICCER/ERA-MA/MAMA dans le contenu pédagogique
- **Valeurs physiques réalistes** et unités SI cohérentes

### Figures SVG

- **Obligatoire** si l'énoncé cite un objet physique, un schéma ou un graphique
- **Repère vierge** (axes + grille, sans droite) pour exercice de tracé graphique
- Conventions couleur : fond `var(--p-bg)`, trait `var(--p)`, inconnues `#c53030` italique
- `<figure class="schema">` + `<figcaption>` autour de chaque SVG
- Les visuels montrent uniquement les données brutes — jamais l'équation, la solution ou le point d'intersection

### Tableaux de données

- Dès 3 valeurs numériques → `<table class="full">` avant les questions
- Le tableau montre UNIQUEMENT les données — jamais l'équation, la solution, ou l'inconnue

### Spécificité BTS

Pour les chapitres dans `maths/bts/` :
- **Pas de différenciation** (pas de diff.js, pas de classes diff-*)
- Un seul sujet, notation rigoureuse
- Lire `prompts/prompt-bts.md` pour les règles spécifiques

### Étape 4 — Vérifier

- Le fichier est bien formé (HTML valide)
- Les 3 niveaux de différenciation sont présents (sauf BTS)
- Barème total = 20 pts pour chaque niveau
- Chaque question taguée avec une compétence
- Corrections complètes (une par partie) avec étapes + unités
- Les calculs des corrections sont exacts (refaire chaque calcul)
- Figures SVG présentes pour les exercices de lecture graphique ou les schémas
- Tableaux de données `<table class="full">` pour les situations avec valeurs numériques
- Aucune référence orpheline ("ci-dessous" sans figure adjacente)
- Le lien retour sommaire est correct
- `nav.js` et `diff.js` sont inclus (sauf BTS : pas de diff.js)
- `print.css` est inclus
- MathJax est inclus si formules
- Les couleurs CSS correspondent au thème matière/niveau
- Aucun sigle de filière dans le contenu pédagogique
- Les valeurs numériques sont réalistes et les unités correctes

ARGUMENTS: $ARGUMENTS
