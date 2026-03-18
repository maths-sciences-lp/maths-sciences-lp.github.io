# Skill : Générer un QCM (`qcm.html`)

## Usage

```
/generate-qcm <chemin-chapitre>
```

Exemple : `/generate-qcm maths/seconde/ch03`

## Instructions

Tu dois générer une page `qcm.html` complète pour le chapitre indiqué.

### Étape 1 — Collecter le contexte

1. **Lire `lecon.html`** du chapitre pour identifier les notions, définitions, propriétés et méthodes
2. **Lire `prompts/prompt-qcm-interro.md`** pour les règles de rédaction des QCM
3. **Identifier le thème couleur** selon le dossier (voir table ci-dessous)
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

### Étape 3 — Générer le QCM

Créer le fichier `qcm.html` dans le dossier du chapitre avec :

- **3 séries de 15 questions** différenciées : socle, standard, approfondissement
- Chaque série dans un `<div class="diff-socle">`, `<div class="diff-standard">`, `<div class="diff-appro">`
- Chaque série a un `<form>` dédié, un bouton "Valider le QCM" et un score
- Les questions sont des `<div class="q-block" data-correct="X">` avec 4 options radio
- Chaque question a un `<div class="q-feedback">` pour l'explication
- Le JavaScript en fin de page gère la correction automatique et le score

### Structure HTML obligatoire

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – Titre – QCM – Niveau Bac Pro</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:BG;--p-border:BORDER}
/* styles QCM inline — voir le modèle existant */
</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>QCM – Titre du chapitre</h1>
  <p class="sous-titre">Chapitre X | Niveau Bac Pro | Matière</p>
</header>
<!-- En-tête QCM : durée, nb questions, calculatrice -->
<!-- div.diff-socle > form#qcm-socle > 15 q-blocks -->
<!-- div.diff-standard > form#qcm-standard > 15 q-blocks -->
<!-- div.diff-appro > form#qcm-appro > 15 q-blocks -->
</div>
<script src="../../../nav.js"></script>
<script src="../../../diff.js"></script>
<script>/* JS de correction automatique */</script>
</body>
</html>
```

### Règles de contenu

- **Socle** : questions directes, vocabulaire simple, calculs élémentaires, reconnaissance
- **Standard** : application du cours, contextes professionnels, calculs intermédiaires
- **Approfondissement** : analyse, synthèse, problèmes multi-étapes, vocabulaire BTS
- Chaque question a exactement **4 propositions** (a, b, c, d), **une seule correcte**
- L'explication (feedback) est **pédagogique**, pas juste "bonne/mauvaise réponse"
- Couvrir **largement** les notions du chapitre (pas tout sur le même thème)
- Ne JAMAIS utiliser les sigles ICCER/ERA-MA/MAMA dans le contenu des questions

### Étape 4 — Vérifier

- Le fichier est bien formé (HTML valide)
- Les 3 séries contiennent 15 questions chacune
- Les `data-correct` sont cohérents avec les bonnes réponses
- Le JavaScript de correction fonctionne pour les 3 formulaires
- Le lien retour sommaire est correct
- `nav.js` et `diff.js` sont inclus
