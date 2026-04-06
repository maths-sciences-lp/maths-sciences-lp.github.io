# Skill : Auditer un chapitre

## Usage

```
/audit-chapter <chemin-chapitre>
```

Exemple : `/audit-chapter maths/premiere/ch05`

## Ce que fait ce skill

Vérifie la **complétude** d'un chapitre : fichiers présents, sigles interdits, contenu non vide.
Pour les vérifications techniques et qualité du contenu, utiliser `/check-quality`.

---

## Instructions

### Étape 1 — Inventaire des fichiers

Lister les fichiers présents dans le dossier du chapitre et vérifier :

| Fichier | Statut attendu |
|---|---|
| `lecon.html` | **Obligatoire** |
| `exercices.html` | **Obligatoire** |
| `ds.html` | **Obligatoire** |
| `fiche.html` | Recommandé |
| `qcm.html` | Recommandé |
| `interro.html` | Recommandé |
| `activite.html` | Recommandé |
| `exercices-capacites.html` | Recommandé |
| `simulation.html` | Optionnel (info) |

### Étape 2 — Contenu non vide

Pour chaque fichier présent, vérifier qu'il n'est pas un squelette :
- pas de mention "en cours de rédaction" ou "à compléter"
- contenu réel (au moins une section avec du texte)

### Étape 3 — Sigles interdits

Scanner le **contenu pédagogique** (hors titres `<h1>`, sous-titres `.sous-titre`, liens de navigation, badges) de tous les fichiers présents.

Signaler toute occurrence des sigles utilisés comme noms de métiers :
- ICCER, ERA-MA, ERA, MAMA utilisés dans des phrases du type "un technicien ICCER…", "vous êtes ERA-MA…"

Rappel des formulations correctes : installateur thermique, menuisier agenceur, menuisier, métreur, etc.

### Étape 4 — Rapport

```
## Audit : maths/premiere/ch05

### Fichiers
- lecon.html .................. ✅ présent
- exercices.html .............. ✅ présent
- ds.html ..................... ✅ présent
- fiche.html .................. ⚠ MANQUANT
- qcm.html .................... ⚠ MANQUANT
- interro.html ................ ⚠ MANQUANT
- activite.html ............... ✅ présent
- exercices-capacites.html .... ⚠ MANQUANT
- simulation.html ............. — (optionnel, absent)

### Contenu
- lecon.html : ✅ contenu réel
- exercices.html : ⚠ squelette ("en cours de rédaction")

### Sigles
- ✅ Aucun sigle interdit détecté
- OU : ✗ "technicien ERA-MA" dans exercices.html L.45, L.112

### Actions recommandées
1. Générer fiche.html → /generate-fiche maths/premiere/ch05
2. Générer qcm.html → /generate-qcm maths/premiere/ch05
3. Générer interro.html → /generate-interro maths/premiere/ch05
4. Compléter exercices.html (contenu vide)
5. Remplacer "technicien ERA-MA" par "menuisier agenceur" (2 occurrences)

→ Pour les vérifications techniques et qualité : /check-quality maths/premiere/ch05
```

---

## Étape 5 — Mettre à jour le journal des audits

Après avoir affiché le rapport, mettre à jour `audits/audit-log.md` :

1. Chercher si le chapitre a déjà une ligne dans le tableau
2. Si oui : mettre à jour la colonne `/audit-chapter` avec la date du jour (format `YYYY-MM-DD`) et le résultat (🔴 / 🟡 / 🟢)
3. Si non : ajouter une nouvelle ligne
4. Mettre à jour la date `Dernière mise à jour` en haut du fichier

---

## Règles

- Ne PAS modifier les fichiers audités — seulement analyser et rapporter
- Signaler les problèmes par ordre de gravité : critique > haute > moyenne > basse
- Toujours terminer en suggérant `/check-quality` pour la suite
- Toujours mettre à jour `audits/audit-log.md` en fin d'exécution
