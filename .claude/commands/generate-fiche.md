# Skill : Générer une fiche résumé (`fiche.html`)

## Usage

```
/generate-fiche <chemin-chapitre>
```

Exemple : `/generate-fiche maths/seconde/ch10`

## Instructions

Tu dois générer une page `fiche.html` de synthèse pour le chapitre indiqué.

### Étape 1 — Collecter le contexte

1. **Lire `lecon.html`** du chapitre en entier — c'est la source principale
2. **Identifier le thème couleur** selon le dossier
3. **Extraire** : définitions, propriétés, formules clés, méthodes, pièges fréquents

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

### Étape 3 — Générer la fiche

Créer `fiche.html` avec une mise en page **compacte en grille**, pensée pour la révision et l'impression.

### Structure HTML obligatoire

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Fiche résumé – ChXX – Titre – Niveau</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<style>
:root{--p:COULEUR;--p-bg:BG;--p-border:BORDER}
.fiche{max-width:780px;margin:0 auto}
.fiche h1{font-size:1.3rem;text-align:center;margin-bottom:4px}
.fiche .sous-titre{text-align:center;margin-bottom:16px}
.fiche-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px}
@media(max-width:600px){.fiche-grid{grid-template-columns:1fr}}
.fiche-card{background:#fff;border:1px solid var(--p-border);border-radius:8px;padding:12px 14px}
.fiche-card h3{font-size:.82rem;color:var(--p);margin:0 0 6px;text-transform:uppercase;letter-spacing:.5px}
.fiche-card p,.fiche-card li{font-size:.84rem;line-height:1.5}
.fiche-card ul{padding-left:16px;margin:0}
.fiche-card li{margin-bottom:3px}
.fiche-card.full{grid-column:1/-1}
.fiche-formula{background:var(--p-bg);border-radius:6px;padding:8px 12px;margin:6px 0;text-align:center;font-size:.92rem}
.piege{border-left:3px solid #e53e3e;background:#fff5f5;border-radius:0 8px 8px 0;padding:8px 12px;margin:6px 0;font-size:.82rem}
.piege strong{color:#e53e3e}
.astuce{border-left:3px solid #16a34a;background:#f0fff4;border-radius:0 8px 8px 0;padding:8px 12px;margin:6px 0;font-size:.82rem}
.astuce strong{color:#16a34a}
@media print{
  body{font-size:11pt}
  .fiche{max-width:100%}
  .nb,.nav-footer{display:none}
  .fiche-card{break-inside:avoid;border:1px solid #ccc}
}
</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<div class="fiche">
<h1>Fiche résumé — Titre du chapitre</h1>
<p class="sous-titre">Chapitre X | Niveau Bac Pro | Matière</p>
<div class="fiche-grid">
  <!-- fiche-card pour chaque notion clé -->
</div>
</div>
</div>
<script src="../../../nav.js"></script>
</body>
</html>
```

### Contenu des cartes

Chaque carte `.fiche-card` couvre une notion clé :

- **Définitions** : formule dans `.fiche-formula`, liste de propriétés
- **Méthodes** : étapes numérotées, astuces de calcul
- **Formules** : encadrées dans `.fiche-formula` avec MathJax
- **Pièges** : dans `.piege` — erreurs fréquentes des élèves
- **Astuces** : dans `.astuce` — raccourcis et moyens mnémotechniques

### Règles

- La fiche tient idéalement sur **1 page A4 imprimée** (2 pages max)
- Pas de diff.js — la fiche est la même pour tous les niveaux
- Texte **concis** : pas de phrases longues, aller à l'essentiel
- Utiliser `.fiche-card.full` pour les cartes larges (tableaux, méthodes longues)
- Ne PAS reprendre le cours entier — seulement l'essentiel pour réviser
