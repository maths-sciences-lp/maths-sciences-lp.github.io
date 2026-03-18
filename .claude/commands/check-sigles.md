# Skill : Vérifier les sigles de filière interdits

## Usage

```
/check-sigles [chemin-optionnel]
```

Exemples :
- `/check-sigles` — scanne tout le repo
- `/check-sigles maths/seconde` — scanne seulement maths/seconde
- `/check-sigles physique-chimie/premiere-era/ch03/lecon.html` — scanne un fichier

## Instructions

Tu dois scanner les fichiers HTML pour détecter l'utilisation interdite des sigles de filière dans le contenu pédagogique.

### Règle rappel (CLAUDE.md)

Les sigles **ICCER**, **ERA**, **ERA-MA**, **MA**, **MAMA** ne doivent JAMAIS apparaître dans le contenu pédagogique comme noms de métiers. Ils sont autorisés uniquement dans :
- `<title>`, `<h1>`
- `<p class="sous-titre">`
- Liens de navigation (`← RETOUR SOMMAIRE`)
- Badges visuels (`<span class="ticcer-badge">`, `<span class="erama-badge">`)

### Étape 1 — Scanner

Utiliser Grep pour chercher les patterns suivants dans les fichiers HTML :
- `ICCER` (hors titres et badges)
- `ERA-MA` (hors titres et badges)
- `ERA` isolé dans un contexte métier (hors titres et badges)
- `MAMA` (hors titres et badges)
- Patterns courants : `technicien ICCER`, `technicien ERA`, `contexte ERA-MA`, `application ICCER`, `exemple ERA`, `lien ERA-MA`

### Étape 2 — Filtrer les faux positifs

Ignorer les occurrences dans :
- Les balises `<title>...</title>`
- Les balises `<h1>...</h1>`
- Les balises `<p class="sous-titre">...</p>`
- Les balises `<a href=...>← RETOUR...</a>` ou `<a ... class="nb">...</a>`
- Les balises `<span class="ticcer-badge">` ou `<span class="erama-badge">`
- Les noms de fichiers/dossiers dans les attributs `href` ou `src`
- Les commentaires HTML

### Étape 3 — Rapport

Pour chaque occurrence trouvée, afficher :

```
## Sigles interdits dans le contenu pédagogique

### Fichier : physique-chimie/premiere-era/ch03/exercices.html
- L.45 : "Un technicien ERA-MA installe..." → "Un menuisier agenceur installe..."
- L.112 : "Contexte ERA-MA : chantier..." → "Contexte professionnel : chantier..."

### Fichier : physique-chimie/terminale-iccer/ch02/ds.html
- L.78 : "Un technicien ICCER effectue..." → "Un installateur thermique effectue..."

### Résumé
- X fichiers analysés
- Y fichiers avec violations
- Z occurrences totales
```

### Corrections suggérées

| Sigle trouvé | Remplacement |
|---|---|
| technicien ICCER | installateur thermique / technicien chauffagiste / technicien CVC |
| technicien ERA-MA | menuisier agenceur / technicien d'agencement |
| technicien MAMA | menuisier / métreur |
| contexte ICCER | contexte professionnel / contexte chauffage |
| contexte ERA-MA | contexte professionnel / contexte menuiserie |
| application ERA-MA | application en agencement |
| exemple ERA | exemple professionnel |

### Règles

- Ne PAS corriger automatiquement — lister et proposer les corrections
- Demander à l'utilisateur s'il veut appliquer les corrections avant de modifier
- Varier les métiers proposés (ne pas toujours utiliser le même remplacement)
