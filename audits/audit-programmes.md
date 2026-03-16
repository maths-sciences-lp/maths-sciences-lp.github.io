# Audit de couverture des programmes officiels

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-03-16
**Périmètre** : conformité du contenu avec les programmes Bac Pro (BO 2019 Seconde, BO 2020 Première/Terminale)
**Méthode** : lecture des 6 PDF officiels dans `/pdf/`, inventaire des `lecon.html` par section, comparaison module par module.

---

## Programmes de référence disponibles

| Fichier PDF | Contenu |
|---|---|
| `programme_bacpro_seconde_maths_-_2019.pdf` | Programme maths Seconde |
| `programme_bacpro_seconde_sciences_-_2019-2.pdf` | Programme sciences Seconde |
| `programme_bacpro_premiere_maths_-_2020 (1).pdf` | Programme maths Première |
| `programme_bacpro_premiere_maths_-_2020-2.pdf` | Programme maths Première (copie) |
| `programme_bacpro_premiere_sciences_-_2020-2.pdf` | Programme sciences Première |
| `programme_bacpro_terminale_maths_-_2020 (1).pdf` | Programme maths Terminale |
| `programme_bacpro_terminale_sciences_-_2020.pdf` | Programme sciences Terminale |
| `BTS_ProgrammeMathematiques.pdf` | Programme maths BTS |
| `tableau_programmes_bts.pdf` | Tableau programmes BTS |
| `grille-ccf-maths-physique.pdf` | Grille d'évaluation CCF |
| `liste_groupements_bac_pro_.xlsx` | Liste des groupements |

---

## 1. Mathématiques — Seconde

### Programme officiel (3 domaines, 6 modules + transversaux)

| Domaine | Module officiel | Chapitre site | Statut |
|---|---|---|---|
| Stat & Probas | Statistique à une variable | ch02 (Statistiques), ch03 (Indicateurs stats) | Couvert |
| Stat & Probas | Fluctuations d'une fréquence, probabilités | ch04 (Probabilités) | Couvert |
| Algèbre-Analyse | Résolution d'un problème du 1er degré | ch05 (Équations), ch06 (Inéquations) | Couvert |
| Algèbre-Analyse | Fonctions (linéaire, affine, carrée, notion de fonction, systèmes) | ch07 (Notion de fonction), ch08 (Fonction linéaire), ch09 (Fonction affine), ch10 (Fonction carrée) | Couvert |
| Algèbre-Analyse | Calculs commerciaux et financiers | — | Non applicable (spécialités sans physique-chimie) |
| Géométrie | Du plan à l'espace (Pythagore, Thalès, solides, volumes) | ch11 (Figures planes), ch12 (Pythagore), ch13 (Thalès), ch14 (Solides/volumes) | Couvert |
| Transversal | Proportionnalité | ch01 (Proportionnalité) | Couvert |

**Couverture : 100 %** (le module "Calculs commerciaux" est hors périmètre car réservé aux spécialités sans physique-chimie)

**Remarques :**
- Le site découpe les modules en sous-chapitres plus fins (ex : "Fonctions" → 4 chapitres), ce qui est pertinent pédagogiquement.
- ch01 (Proportionnalité) est un outil transversal traité en chapitre dédié — bon choix.

---

## 2. Mathématiques — Première

### Programme officiel (3 domaines, 9 modules pour groupements A/B)

| Domaine | Module officiel | Groupements | Chapitre site | Statut |
|---|---|---|---|---|
| Stat & Probas | Statistique à deux variables | A, B, C | ch01 (Stats 2 variables) | Couvert |
| Stat & Probas | Probabilités (conditionnelles, tableaux croisés) | A, B, C | ch02 (Probabilités) | Couvert |
| Algèbre-Analyse | Suites numériques (arithmétiques) | A, B, C | ch03 (Suites) | Couvert |
| Algèbre-Analyse | Résolution graphique d'équations et inéquations | A, B, C | ch04 (Résolution graphique) | Couvert |
| Algèbre-Analyse | Fonctions polynômes de degré 2 | A, B, C | ch05 (Polynômes degré 2) | Couvert |
| Algèbre-Analyse | Fonction dérivée et variations | A, B, C | ch06 (Dérivée) | Couvert |
| Géométrie | Géométrie dans l'espace | A, B, C | ch07 (Géométrie espace) | Couvert |
| Géométrie | Vecteurs du plan | A, B | ch08 (Vecteurs) | Couvert |
| Géométrie | Trigonométrie | A, B | ch09 (Trigonométrie) | Couvert |

**Couverture : 100 %**

---

## 3. Mathématiques — Terminale

### Programme officiel (3 domaines, 7 modules + programme complémentaire poursuite d'études)

| Domaine | Module officiel | Groupements | Chapitre site | Statut |
|---|---|---|---|---|
| Stat & Probas | Statistiques à deux variables (ajustement non affine) | A, B, C | ch01 (Stats 2 variables) | Couvert |
| Stat & Probas | Probabilités (arbres pondérés, indépendance) | A, B, C | ch02 (Probabilités) | Couvert |
| Algèbre-Analyse | Suites numériques (géométriques) | A, B, C | ch03 (Suites géométriques) | Couvert |
| Algèbre-Analyse | Fonctions polynômes de degré 3 | A, B, C | ch04 (Polynômes degré 3) | Couvert |
| Algèbre-Analyse | Fonctions exponentielles et logarithme décimal | A, B, C | ch05 (Expo/log décimal) | Couvert |
| Géométrie | Vecteurs (dans l'espace) | B seul | ch06 (Vecteurs) | Couvert |
| Géométrie | Trigonométrie (Fresnel, équations trigo) | A seul | ch07 (Trigonométrie) | Couvert |
| **Programme complémentaire** | Calcul intégral | Poursuite | ch08 (Calcul intégral) | Couvert |
| **Programme complémentaire** | Fonctions ln et exponentielle | Poursuite | ch09 (Fonctions ln/expo) | Couvert |
| **Programme complémentaire** | Nombres complexes | Poursuite | ch10 (Nombres complexes) | Couvert |
| **Programme complémentaire** | Produit scalaire | Poursuite | ch11 (Produit scalaire) | Couvert |

**Couverture : 100 %** (programme principal + programme complémentaire complet)

**Remarques :**
- Vecteurs (groupement B) et Trigonométrie (groupement A) sont proposés à tous — approche superset cohérente avec la poursuite d'études.
- Les 4 modules du programme complémentaire sont tous couverts.

---

## 4. Physique-Chimie — Seconde

### Programme officiel (7 domaines, tous communs)

| Domaine | Module officiel | Chapitre site | Statut |
|---|---|---|---|
| Sécurité | Travailler en toute sécurité | ch01 (Sécurité labo) | Couvert |
| Électricité | Grandeurs électriques (U, I, loi d'Ohm, capteurs) | ch02 (Grandeurs élec), ch03 (Loi d'Ohm), ch04 (Signaux alternatifs) | Couvert |
| Mécanique | Mouvement, trajectoire, vitesse | ch05 (Mouvement/trajectoire) | Couvert |
| Mécanique | Forces, équilibre, poids | ch06 (Forces/équilibre) | Couvert |
| Chimie | Structure matière, solutions, concentration, pH | ch07 (Structure matière), ch08 (Solutions chimiques) | Couvert |
| Acoustique | Signal sonore (fréquence, niveau, atténuation) | ch09 (Son) | Couvert |
| Thermique | Température, capteurs, transferts, changements d'état | ch10 (Température/capteurs), ch11 (Transferts thermiques), ch12 (Changements d'état) | Couvert |
| Optique | Réflexion, réfraction, spectre, lumière, couleurs | ch13 (Réflexion/réfraction), ch14 (Lumière/couleurs) | Couvert |

**Couverture : 100 %**

---

## 5. Physique-Chimie — Première ICCER (Groupement 1)

### Programme officiel (10 modules)

| Domaine | Module officiel | Chapitre site | Statut |
|---|---|---|---|
| Électricité | Distinguer énergie et puissance électrique | ch01 (Énergie/puissance élec) | Couvert |
| Électricité | Transporter l'énergie sous forme électrique | ch02 (Transport énergie élec) | Couvert |
| Thermique | Combustion du carbone et des hydrocarbures | ch03 (Combustion) | Couvert |
| Thermique | Distinguer les trois modes de transfert thermique | ch04 (Transfert thermique) | Couvert |
| Mécanique | Caractériser l'accélération et la vitesse | ch05 (Vitesse/accélération) | Couvert |
| Mécanique | Équilibre d'un solide en rotation (moments) | ch06 (Équilibre rotation) | Couvert |
| Mécanique | Distinguer pression et force pressante (Boyle-Mariotte) | ch07 (Pression) | Couvert |
| Mécanique | Exploiter la force d'Archimède | ch08 (Archimède) | Couvert |
| Chimie | Caractériser quantitativement une solution aqueuse (titrage) | ch09 (Solutions aqueuses) | Couvert |
| Signaux | Caractériser une onde électromagnétique | ch10 (Ondes EM) | Couvert |

**Couverture : 100 %**

---

## 6. Physique-Chimie — Première ERA-MA (Groupement 3)

### Programme officiel (10 modules)

| Domaine | Module officiel | Chapitre site | Statut |
|---|---|---|---|
| Électricité | Distinguer énergie et puissance électrique | ch01 (Énergie/puissance) | Couvert |
| Électricité | Évaluer la puissance consommée (régime sinusoïdal) | ch02 (Puissance consommée) | Couvert |
| Thermique | Combustion du carbone et des hydrocarbures | ch03 (Combustion) | Couvert |
| Thermique | Distinguer les trois modes de transfert thermique | ch04 (Transfert thermique) | Couvert |
| Thermique | Minimiser les transferts thermiques (conductance thermique) | ch05 (Minimiser transferts) | Couvert |
| Mécanique | Équilibre d'un solide en rotation (moments) | ch06 (Équilibre rotation) | Couvert |
| Mécanique | Distinguer pression et force pressante (Boyle-Mariotte) | ch07 (Pression) | Couvert |
| Chimie | Caractériser quantitativement une solution aqueuse (titrage) | ch08 (Solutions aqueuses) | Couvert |
| Signaux | Caractériser une onde électromagnétique | ch09 (Ondes EM) | Couvert |
| Signaux | Caractériser la propagation d'un signal sonore | ch10 (Signal sonore) | Couvert |

**Couverture : 100 %**

---

## 7. Physique-Chimie — Terminale ICCER (Groupement 1)

### Programme officiel (8 modules)

| Domaine | Module officiel | Chapitre site | Statut |
|---|---|---|---|
| Électricité | Évaluer la puissance consommée (régime sinusoïdal) | ch01 (Puissance consommée) | Couvert |
| Électricité | Obtenir un courant continu à partir d'un courant alternatif | ch02 (Courant AC/DC) | Couvert |
| Électricité | Obtenir de l'énergie mécanique (moteur) | ch03 (Moteur électrique) | Couvert |
| Thermique | Utiliser le rayonnement thermique, effet de serre | ch04 (Rayonnement thermique) | Couvert |
| Mécanique | Caractériser la pression dans un fluide immobile (Pascal) | ch05 (Pression fluide) | Couvert |
| Mécanique | Décrire le transport de masse/volume par un fluide (débit) | ch06 (Transport fluide) | Couvert |
| Chimie | Prévoir une réaction d'oxydoréduction et protéger les métaux | ch07 (Oxydoréduction) | Couvert |
| Signaux | Caractériser la propagation d'un signal sonore | ch08 (Signal sonore) | Couvert |

**Couverture : 100 %**

**Note** : CLAUDE.md indiquait ch01-ch11 mais le programme officiel prévoit bien 8 modules pour le groupement 1 en terminale. CLAUDE.md doit être corrigé (ch01-ch08).

---

## 8. Physique-Chimie — Terminale ERA-MA (Groupement 3)

### Programme officiel (8 modules)

| Domaine | Module officiel | Chapitre site | Statut |
|---|---|---|---|
| Électricité | Transporter l'énergie sous forme électrique | ch01 (Transport énergie élec) | Couvert |
| Électricité | Stocker l'énergie (système électrochimique) | ch02 (Stockage électrochimique) | Couvert |
| Thermique | Utiliser le rayonnement thermique, effet de serre | ch03 (Rayonnement thermique) | Couvert |
| Mécanique | Caractériser l'accélération et la vitesse | ch04 (Vitesse/accélération) | Couvert |
| Chimie | Prévoir une réaction d'oxydoréduction et protéger les métaux | ch05 (Oxydoréduction) | Couvert |
| Signaux | Choisir une source lumineuse (spectre, efficacité, laser) | ch06 (Source lumineuse) | Couvert |
| Signaux | Transmettre l'information (fibre optique, ondes) | ch07 (Transmettre info) | Couvert |
| Signaux | Atténuer une onde sonore (coefficient, indice affaiblissement) | ch08 (Atténuer onde sonore) | Couvert |

**Couverture : 100 %**

---

## Synthèse globale

| Section | Modules officiels | Chapitres site | Couverture | Manquants |
|---|---|---|---|---|
| Maths Seconde | 6 (+1 transv.) | 14 | **100 %** | 0 |
| Maths Première | 9 (grpt A/B) | 9 | **100 %** | 0 |
| Maths Terminale | 7 + 4 compl. | 11 | **100 %** | 0 |
| PC Seconde | 7 domaines | 14 | **100 %** | 0 |
| PC 1ère ICCER | 10 modules | 10 | **100 %** | 0 |
| PC 1ère ERA | 10 modules | 10 | **100 %** | 0 |
| PC Tle ICCER | 8 modules | 8 | **100 %** | 0 |
| PC Tle ERA | 8 modules | 8 | **100 %** | 0 |
| **TOTAL** | **65+ modules** | **84 chapitres** | **100 %** | **0** |

---

## Points forts

1. **Couverture intégrale** : tous les modules des programmes officiels sont présents, y compris les 4 modules du programme complémentaire de poursuite d'études en Terminale maths.
2. **Découpage fin** : 84 chapitres pour ~65 modules, ce qui facilite la progression pédagogique.
3. **Différenciation des groupements** : ICCER (Grpt 1) et ERA-MA (Grpt 3) ont des chapitres distincts et conformes.
4. **Cohérence des progressions** : l'ordre des chapitres suit la logique des programmes.

---

## Problemes identifies

### 1. Incohérence CLAUDE.md sur terminale ICCER

CLAUDE.md déclare ch01-ch11 pour `physique-chimie/terminale-iccer`, mais le programme officiel prévoit 8 modules et seuls ch01-ch08 existent. **CLAUDE.md doit être corrigé.**

### 2. Modules transversaux non vérifiés

Les modules transversaux (Algorithmique, Automatismes, Vocabulaire ensembliste) ne doivent pas avoir de chapitres dédiés (conforme au BO), mais leur intégration dans les chapitres existants n'a pas été vérifiée à l'échelle des pages.

### 3. Identification du programme complémentaire

Les 4 chapitres de poursuite d'études (ch08-ch11 en maths terminale) devraient être clairement identifiés comme "programme complémentaire" et non comme programme obligatoire pour tous les élèves.

### 4. Doublons dans les PDF

Deux fichiers semblent être des copies du même programme :
- `programme_bacpro_premiere_maths_-_2020 (1).pdf`
- `programme_bacpro_premiere_maths_-_2020-2.pdf`

### 5. Nommage des fichiers PDF

Les noms contiennent des espaces, des parenthèses et des suffixes incohérents (`-2`, `(1)`).

### 6. Pages fiche.html incomplètes en maths/premiere

| Section | fiche.html | Statut |
|---|---|---|
| maths/seconde | 14/14 | Complet |
| maths/premiere | 1/9 | **Incomplet** (ch02-ch09 manquants) |
| maths/terminale | 11/11 | Complet |
| physique-chimie/* | 0 | À clarifier (intentionnel ?) |

---

## Corrections realisees

- Aucune à ce stade.

---

## Ameliorations restantes

### Priorité haute
- [ ] Corriger CLAUDE.md : `physique-chimie/terminale-iccer` → ch01-ch08 (pas ch01-ch11)
- [ ] Identifier les chapitres ch08-ch11 de maths/terminale comme "programme complémentaire"

### Priorité moyenne
- [ ] Vérifier l'intégration des modules transversaux (algorithmique, automatismes) dans les chapitres
- [ ] Créer les fiche.html manquantes pour maths/premiere ch02-ch09
- [ ] Réaliser un audit capacités attendues vs contenu des cours, chapitre par chapitre
- [ ] Supprimer les doublons PDF et renommer avec convention cohérente

### Priorité basse
- [ ] Clarifier si les sections physique-chimie doivent avoir des fiche.html
- [ ] Ajouter un fichier `pdf/README.md` listant chaque PDF et son contenu
- [ ] Vérifier que les grilles CCF correspondent aux dernières circulaires
