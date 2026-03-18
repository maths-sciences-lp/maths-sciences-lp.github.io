# Skill : Créer la structure d'un nouveau chapitre

## Usage

```
/new-chapter <matiere/niveau> <chNN> <titre>
```

Exemple : `/new-chapter physique-chimie/terminale-iccer ch09 "Les ondes sonores"`

## Instructions

Tu dois créer le dossier complet d'un nouveau chapitre avec les 6 fichiers de base.

### Étape 1 — Valider les paramètres

1. Vérifier que `<matiere/niveau>` est un dossier valide parmi :
   - `maths/seconde`, `maths/premiere`, `maths/terminale`
   - `physique-chimie/seconde`, `physique-chimie/premiere-iccer`, `physique-chimie/premiere-era`
   - `physique-chimie/terminale-iccer`, `physique-chimie/terminale-era`
2. Vérifier que le dossier `chNN` n'existe pas déjà
3. Déterminer le thème couleur depuis la table :

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

### Étape 2 — Créer le dossier et les 6 fichiers

Créer `<matiere/niveau>/chNN/` contenant :

#### 1. `lecon.html` — Page de cours (squelette)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – TITRE – NIVEAU</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<style>:root{--p:COULEUR;--p-bg:BG;--p-border:BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Chapitre XX – TITRE</h1>
  <p class="sous-titre">NIVEAU | MATIÈRE | Module</p>
</header>
<div class="objectifs"><strong>Objectifs :</strong>
<ul><li><!-- À compléter --></li></ul>
</div>
<!-- CONTENU DU COURS À RÉDIGER -->
<p style="text-align:center;color:#718096;margin-top:40px"><em>Contenu en cours de rédaction.</em></p>
</div>
<script src="../../../nav.js"></script>
</body>
</html>
```

#### 2. `exercices.html` — Exercices (squelette avec différenciation)

Même structure de base, avec `diff.js` inclus et les 3 blocs `diff-socle`, `diff-standard`, `diff-appro` vides mais prêts.

#### 3. `ds.html` — Devoir surveillé (squelette avec différenciation)

Même structure, avec 3 sujets différenciés et barème sur 20.

#### 4. `fiche.html` — Fiche résumé (squelette)

Structure `.fiche` / `.fiche-grid` / `.fiche-card` vide.

#### 5. `qcm.html` — QCM (squelette)

Structure avec 3 formulaires `diff-socle/standard/appro` vides.

#### 6. `interro.html` — Interrogation (squelette)

Structure avec 3 sujets différenciés vides.

### Étape 3 — Vérifier

- Les 6 fichiers existent dans le bon dossier
- Tous les chemins relatifs (`../../../styles.css`, `../../../nav.js`, etc.) sont corrects
- Le thème couleur est cohérent avec la matière/niveau
- Les titres et sous-titres sont remplis
- Signaler à l'utilisateur que les fichiers sont des squelettes à compléter

### Règles

- Ne PAS générer de contenu pédagogique dans ce skill — seulement la structure
- Pour remplir le contenu, utiliser les skills dédiés (`/generate-qcm`, `/generate-interro`, `/generate-fiche`) ou travailler manuellement
- Les squelettes doivent être des HTML valides qui s'affichent correctement même vides
