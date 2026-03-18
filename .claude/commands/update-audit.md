# Skill : Mettre à jour un fichier d'audit

## Usage

```
/update-audit <fichier-audit> <action> <description>
```

Exemples :
- `/update-audit audit-technique.md fix "Ajout print.css sur 15 fichiers lecon.html"`
- `/update-audit audit-pedagogique.md problem "3 chapitres PC ERA utilisent le sigle ERA-MA dans le contenu"`
- `/update-audit audit-exercices.md partial "Corrections ajoutées pour maths/seconde/ch01-ch07, reste ch08-ch14"`

## Instructions

Tu dois mettre à jour un fichier d'audit après une modification du site, conformément aux règles du CLAUDE.md.

### Actions possibles

#### `fix` — Correction réalisée

1. Ouvrir `audits/<fichier-audit>`
2. Trouver l'élément correspondant dans `## Problemes identifies` ou `## Ameliorations restantes`
3. Ajouter dans `## Corrections realisees` :
   ```
   - **AAAA-MM-JJ** : Description de la correction
   ```
4. Si l'élément était dans `## Ameliorations restantes`, cocher la case `[x]`
5. Si le problème est entièrement résolu, le retirer de `## Problemes identifies`
6. Mettre à jour `**Dernière mise à jour** : AAAA-MM-JJ`

#### `problem` — Nouveau problème découvert

1. Ouvrir `audits/<fichier-audit>`
2. Ajouter dans `## Problemes identifies` avec la gravité appropriée (CRITIQUE/HAUTE/MOYENNE/BASSE)
3. Ajouter une tâche dans `## Ameliorations restantes` à la bonne priorité
4. Mettre à jour la date

#### `partial` — Correction partielle

1. Ajouter la correction partielle dans `## Corrections realisees`
2. Laisser l'élément dans `## Ameliorations restantes` avec une note sur ce qui reste
3. Mettre à jour la date

### Règles

- Toujours utiliser la date du jour (format AAAA-MM-JJ)
- Ne jamais supprimer d'historique dans `## Corrections realisees`
- Mettre à jour les compteurs si applicable (ex: "61 fichiers" → "46 fichiers")
- Si un fichier d'audit n'a pas la structure standard, la créer avant de modifier
- Les fichiers d'audit valides sont :
  - `audit-global.md`
  - `audit-technique.md`
  - `audit-programmes.md`
  - `audit-pedagogique.md`
  - `audit-pedagogique-maths.md`
  - `audit-pedagogique-pc.md`
  - `audit-exercices.md`
  - `audit-simulations.md`
