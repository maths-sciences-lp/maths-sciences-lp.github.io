# Skill : Générer une interrogation (`interro.html`)

## Usage

```
/generate-interro <chemin-chapitre>
```

Exemple : `/generate-interro maths/terminale/ch05`

## Instructions

Tu dois générer une page `interro.html` complète pour le chapitre indiqué.

### Étape 1 — Collecter le contexte

1. **Lire `lecon.html`** du chapitre pour identifier les notions essentielles
2. **Lire `prompts/prompt-qcm-interro.md`** pour les règles de rédaction des interrogations
3. **Identifier le thème couleur** selon le dossier (même table que generate-qcm)
4. **Identifier la matière et le niveau** depuis le chemin

### Étape 2 — Déterminer le thème couleur

| Dossier | `--p` | `--p-bg` | `--p-border` |
|---|---|---|---|
| `maths/seconde` | `#0056b3` | `#ebf5ff` | `#bee3f8` |
| `maths/premiere` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `maths/terminale` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/seconde` | `#6f42c1` | `#f5f0ff` | `#c4b5fd` |
| `physique-chimie/premiere-iccer` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/premiere-era` | `#2da44e` | `#f0fff4` | `#86efac` |
| `physique-chimie/terminale-iccer` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/terminale-era` | `#2da44e` | `#f0fff4` | `#86efac` |

### Étape 3 — Générer l'interrogation

Créer le fichier `interro.html` dans le dossier du chapitre avec :

- **3 sujets différenciés** : socle (très guidé), standard (programme), approfondissement (ouvert)
- Chaque sujet dans un `<div class="diff-socle">`, `<div class="diff-standard">`, `<div class="diff-appro">`
- **5 à 8 questions par sujet**, format rédigé (PAS de QCM)
- Barème sur 20 points pour chaque sujet
- Corrections cachées avec bouton `.bc` / `.corr`

### Structure HTML obligatoire

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – Titre – Interrogation – Niveau Bac Pro</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:BG;--p-border:BORDER}
.pts{font-size:.82em;color:#718096;font-weight:normal}
</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Chapitre X – Interrogation écrite</h1>
  <p class="sous-titre">Titre — Niveau Bac Pro</p>
</header>
<div class="dh"><p><strong>Durée :</strong> 10-15 min | <strong>Calculatrice autorisée</strong></p></div>
<!-- div.diff-socle > questions avec .exo, .bc, .corr -->
<!-- div.diff-standard > questions -->
<!-- div.diff-appro > questions -->
</div>
<script src="../../../nav.js"></script>
<script src="../../../diff.js"></script>
</body>
</html>
```

### Règles de contenu

- **Socle** : questions décomposées, calculs amorcés (`\(\dfrac{...}{...} = ...\)`), rappels de méthode dans des `.meth`, tableaux pré-remplis
- **Standard** : questions complètes, contextes professionnels, rédaction attendue
- **Approfondissement** : problèmes ouverts, mise en équation autonome, questions type BTS
- Chaque question indique son barème : `<span class="pts">(X points)</span>`
- Les corrections utilisent `<button class="bc">Voir la correction</button><div class="corr">...</div>`
- Conçue pour être **imprimable** (format papier)
- Ne JAMAIS utiliser les sigles ICCER/ERA-MA/MAMA dans le contenu des questions

### Étape 4 — Vérifier

- Total des points = 20 pour chaque sujet
- Les corrections sont complètes et pédagogiques
- Le HTML est bien formé
- `nav.js` et `diff.js` sont inclus
