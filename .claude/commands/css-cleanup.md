# Skill : Nettoyer les styles CSS inline

## Usage

```
/css-cleanup [chemin-optionnel]
```

Exemples :
- `/css-cleanup` — nettoie tout le repo
- `/css-cleanup maths/seconde` — nettoie seulement maths/seconde
- `/css-cleanup physique-chimie/premiere-era/ch03/lecon.html` — nettoie un fichier

## Instructions

Tu dois détecter et supprimer les styles CSS inline qui redéfinissent des classes déjà présentes dans `styles.css`.

### Étape 1 — Identifier les classes protégées

Les classes suivantes sont définies dans `styles.css` et ne doivent JAMAIS être redéfinies dans un `<style>` inline :

```
.def, .prop, .att, .meth, .retenir, .ex, .exo, .corr, .bc,
.label-def, .label-prop, .label-att, .label-meth,
.situation, .objectifs, .formule-box, .formula-box,
.niveau-header, .niv1, .niv2, .niv3, .niv4,
.chart-wrap, .svg-wrap, .anim-wrap,
.grid2, .deux-col,
.badge-green, .badge-blue, .badge-yellow, .badge-red,
.diff-socle, .diff-standard, .diff-appro,
.tag-socle, .tag-standard, .tag-appro,
.c, .nb, .sous-titre, .dh
```

### Étape 2 — Scanner les fichiers HTML

Pour chaque fichier HTML dans le périmètre :
1. Extraire le contenu des balises `<style>...</style>`
2. Parser les sélecteurs CSS définis
3. Comparer avec la liste des classes protégées
4. Signaler les redéfinitions

### Étape 3 — Vérifier les thèmes couleur

Vérifier que chaque fichier utilise les bonnes variables CSS `:root` pour sa matière/niveau :

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

### Étape 4 — Rapport et nettoyage

Afficher le rapport :

```
## CSS Cleanup

### Classes redéfinies (à supprimer)
- maths/seconde/ch03/lecon.html : .def, .exo (2 classes)
- physique-chimie/seconde/ch07/exercices.html : .corr (1 classe)

### Thèmes couleur incorrects
- maths/premiere/ch02/lecon.html : --p=#0056b3 (devrait être #0969da)

### Résumé
- X fichiers analysés
- Y fichiers avec classes redéfinies (Z classes au total)
- W fichiers avec thème couleur incorrect
```

Puis demander à l'utilisateur s'il veut appliquer les corrections.

### Correction automatique

Si l'utilisateur confirme :
1. Supprimer les sélecteurs redéfinis du `<style>` inline
2. Si le `<style>` ne contient plus que `:root{...}`, c'est normal — garder uniquement les variables
3. Corriger les variables `:root` si le thème est incorrect
4. Ne PAS supprimer les styles vraiment spécifiques à la page (ex: styles QCM, styles fiche)

### Règles

- Le script `scripts/extract_css.py` fait un travail similaire — le mentionner comme alternative
- Ne jamais toucher aux styles spécifiques des simulations (elles sont autonomes)
- Les styles de QCM (`.q-block`, `.options`, `.score-box`, etc.) sont spécifiques aux pages QCM et doivent rester inline
- Les styles de fiche (`.fiche`, `.fiche-grid`, `.fiche-card`, etc.) sont spécifiques aux fiches et doivent rester inline
