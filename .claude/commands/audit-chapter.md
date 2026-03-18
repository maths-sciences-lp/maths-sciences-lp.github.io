# Skill : Auditer un chapitre

## Usage

```
/audit-chapter <chemin-chapitre>
```

Exemple : `/audit-chapter maths/premiere/ch05`

## Instructions

Tu dois vérifier la complétude et la qualité d'un chapitre donné.

### Étape 1 — Inventaire des fichiers

Lister les fichiers présents dans le dossier du chapitre et vérifier :

| Fichier | Obligatoire | Présent ? |
|---|---|---|
| `lecon.html` | Oui | ? |
| `exercices.html` | Oui | ? |
| `ds.html` | Oui | ? |
| `fiche.html` | Recommandé | ? |
| `qcm.html` | Recommandé | ? |
| `interro.html` | Recommandé | ? |

### Étape 2 — Vérifications techniques (pour chaque fichier présent)

1. **CSS** : le `<style>:root{...}` utilise les bonnes couleurs pour la matière/niveau
2. **Scripts** : `nav.js` est inclus en fin de `<body>`
3. **Scripts** : `diff.js` est inclus SI la page contient des blocs `.diff-*` (et uniquement dans ce cas)
4. **Styles** : aucune classe de `styles.css` n'est redéfinie inline (`.def`, `.prop`, `.att`, `.meth`, `.retenir`, `.ex`, `.exo`, `.corr`, `.bc`, etc.)
5. **Chemins** : `../../../styles.css`, `../../../nav.js`, `../../../diff.js` sont corrects
6. **MathJax** : inclus si la page contient des formules `\(...\)` ou `\[...\]`
7. **print.css** : `<link rel="stylesheet" href="../../../print.css" media="print">` est présent
8. **Lien retour** : le lien `← Retour au sommaire` pointe vers le bon sommaire

### Étape 3 — Vérifications pédagogiques

1. **Sigles interdits** : scanner le contenu (pas les titres/badges) pour les mots ICCER, ERA-MA, ERA, MAMA utilisés comme noms de métiers
2. **Différenciation** : si `exercices.html` et `ds.html` existent, vérifier qu'ils contiennent des blocs `diff-socle`, `diff-standard`, `diff-appro`
3. **Corrections** : les exercices ont-ils des corrections (`.corr`) ?
4. **Contenu non vide** : les fichiers ne sont-ils pas des squelettes vides ("en cours de rédaction") ?

### Étape 4 — Rapport

Afficher un rapport structuré :

```
## Audit : maths/premiere/ch05

### Fichiers
- lecon.html .......... OK
- exercices.html ...... OK (stub — contenu vide)
- ds.html ............. OK
- fiche.html .......... MANQUANT
- qcm.html ........... MANQUANT
- interro.html ........ MANQUANT

### Technique
- Thème couleur : OK (#0969da)
- nav.js : OK (6/6 fichiers)
- diff.js : OK (présent sur exercices + ds)
- print.css : MANQUANT sur lecon.html
- Classes redéfinies : aucune

### Pédagogie
- Sigles interdits : 2 occurrences ("technicien ERA-MA" dans exercices.html L.45, L.112)
- Différenciation : OK (3 niveaux dans exercices et ds)
- Corrections : 8/10 exercices corrigés

### Actions recommandées
1. Ajouter print.css à lecon.html
2. Remplacer "technicien ERA-MA" par "menuisier agenceur" (2 occurrences)
3. Générer fiche.html (/generate-fiche)
4. Générer qcm.html (/generate-qcm)
5. Générer interro.html (/generate-interro)
6. Compléter exercices.html (contenu vide)
```

### Règles

- Ne PAS modifier les fichiers — seulement analyser et rapporter
- Signaler les problèmes par ordre de gravité (critique > haute > moyenne > basse)
- Suggérer les skills à utiliser pour corriger les manques
