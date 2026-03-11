# PROMPT SUPERVISEUR — GÉNÉRATION DU SITE PÉDAGOGIQUE

Tu travailles sur un site pédagogique de mathématiques et de physique-chimie destiné aux élèves de lycée professionnel.

Le site contient :
- des cours
- des exercices
- des devoirs surveillés

Ton rôle est d'aider à générer ou compléter ces contenus de manière cohérente avec les programmes officiels.

---

## LECTURE DES RESSOURCES DU DÉPÔT

Avant de générer du contenu, lire les ressources suivantes :

### 1. Les programmes officiels situés dans :
`/pdf`

Ces fichiers contiennent les programmes de mathématiques et de physique-chimie du Bac Professionnel.

### 2. Les prompts pédagogiques situés dans :
`/prompts`

Ils contiennent :
- prompt-cours
- prompt-exercices
- prompt-filiere-ticcer
- prompt-filiere-era-ma
- prompt-filiere-2mama

Ces prompts définissent :
- la structure pédagogique des cours
- la structure des exercices
- les contextes professionnels des filières

Toujours utiliser ces prompts comme référence.

---

## OBJECTIF DU TRAVAIL

Le but est de compléter progressivement le site pédagogique.

Pour chaque chapitre, générer si nécessaire :
- la page de cours
- la page d'exercices
- la page de devoir surveillé

Les pages doivent être cohérentes avec la structure HTML déjà utilisée sur le site.
Ne jamais casser la structure existante.

---

## STRUCTURE DES PAGES

Chaque chapitre possède trois pages :

```
chapitre_lecon.html
chapitre_exos.html
chapitre_ds.html
```

Exemple :

```
ch01_lecon.html
ch01_exos.html
ch01_ds.html
```

Respecter cette organisation.

---

## GÉNÉRATION DES COURS

Pour créer un cours :

1. Lire le prompt : `/prompts/prompt-cours.md`
2. Appliquer cette structure pour produire une page HTML pédagogique.

Le cours doit contenir :
- explications progressives
- exemples détaillés
- illustrations
- graphiques si nécessaires
- animations pédagogiques si pertinentes
- encadrés "À retenir"

Le niveau doit être adapté au lycée professionnel.

---

## GÉNÉRATION DES EXERCICES

Pour créer des exercices :

1. Lire le prompt : `/prompts/prompt-exercices.md`
2. Générer une série d'exercices progressifs.

Les exercices doivent :
- être accessibles
- comporter plusieurs niveaux de difficulté
- proposer des contextes variés

Les contextes peuvent être :
- professionnels
- scientifiques
- quotidiens
- sportifs
- climatiques
- énergétiques

Ne pas utiliser uniquement des contextes professionnels.

---

## UTILISATION DES CONTEXTES PROFESSIONNELS

Si le chapitre concerne une filière particulière, lire le prompt correspondant :

| Filière | Prompt |
|---|---|
| Terminale ICCER | `prompt-filiere-ticcer` |
| Terminale ERA / MA | `prompt-filiere-era-ma` |
| Seconde MAMA | `prompt-filiere-2mama` |

Ces prompts décrivent :
- les métiers
- les contextes professionnels
- les règles de rédaction

Toujours utiliser les noms de métiers plutôt que les sigles des filières.

---

## CONFORMITÉ AU PROGRAMME

Lors de la création des contenus, vérifier les notions dans les PDF du programme.

Ne pas introduire de notions hors programme.

Respecter :
- les capacités attendues
- les connaissances associées
- les limites indiquées dans le programme officiel

---

## STYLE DU SITE

Toujours respecter :
- la structure HTML existante
- les classes CSS existantes
- le style visuel du site
- l'organisation actuelle des pages

Ne pas modifier le CSS global.
Ne pas casser la navigation du site.

---

## OBJECTIF FINAL

Aider à compléter progressivement le site pédagogique en produisant :
- des cours clairs et pédagogiques
- des exercices progressifs
- des devoirs surveillés cohérents

tout en respectant :
- les programmes officiels
- la structure existante du site
- les prompts pédagogiques stockés dans le dépôt
