# Audit Pedagogique Approfondi — Physique-Chimie

**Date** : 2026-03-16
**Derniere mise a jour** : 2026-03-16 (session 2)
**Perimetre** : Toutes les pages lecon.html de physique-chimie (seconde, 1ere ICCER, 1ere ERA, Tle ICCER, Tle ERA)
**Methode** : Lecture integrale ou partielle de 25+ fichiers, analyses statistiques CSS sur 50 fichiers

---

## 1. Physique-Chimie Seconde (14 chapitres)

**Note globale : 4/5**

### Chapitres couverts
| Ch | Titre | Domaine |
|----|-------|---------|
| 01 | Securite en laboratoire et en atelier | Transversal |
| 02 | Grandeurs electriques et circuits | Electricite |
| 03 | Loi d'Ohm et caracteristiques d'un dipole | Electricite |
| 04 | Signaux electriques alternatifs | Electricite |
| 05 | Mouvement et trajectoire | Mecanique |
| 06 | Forces et equilibre | Mecanique |
| 07 | Structure de la matiere | Chimie |
| 08 | Solutions chimiques et concentration | Chimie |
| 09 | Caracteristiques d'un son | Acoustique |
| 10 | Temperature et capteurs thermiques | Thermique |
| 11 | Transferts thermiques et equilibre thermique | Thermique |
| 12 | Changements d'etat et energie thermique | Thermique |
| 13 | Reflexion, refraction et signaux lumineux | Optique |
| 14 | Lumiere, couleurs et photodetecteurs | Optique |

### Points forts
- **Couverture exhaustive** : 14 chapitres couvrant les 5 domaines du programme (electricite, mecanique, chimie, thermique, signaux)
- **Qualite des schemas SVG** : Les circuits electriques (ch02), les forces (ch06), l'installation electrique (ch01) sont remarquablement illustres avec des SVG inline clairs et pedagogiques
- **Graphiques Chart.js** : Les graphiques interactifs (niveaux sonores ch01/ch09, conductivite thermique) enrichissent la comprehension
- **Progressivite logique** : ch02 (circuits) → ch03 (loi d'Ohm) → ch04 (alternatif) forme une progression naturelle
- **Classes CSS correctement utilisees** : Chaque chapitre utilise `.def`, `.prop`, `.att`, `.meth`, `.retenir`, `.ex`, `.exo` de maniere coherente (78 `.def`, 65 `.prop`, 27 `.att` sur l'ensemble)
- **Exercices de verification** avec corrections cachees dans `<details>` — bonne pratique
- **Contextes professionnels menuiserie** bien ancres (ponceuse, scie circulaire, solvants, colle thermofusible, sechage du bois...)
- **Tableaux de synthese** en fin de chapitre : excellente pratique pour la revision
- **Encadres "A retenir"** systematiques

### Points faibles

1. **Redefinition CSS inline dans les 14 fichiers**
   - **Fichiers concernes** : TOUS les 14 fichiers seconde
   - **Probleme** : Les classes `.exo .exo-num`, `details.corr summary`, `details.corr .corr-body` sont redefinies dans le `<style>` inline de chaque fichier, alors qu'elles existent dans `styles.css`
   - **Impact** : Maintenance difficile, risque de divergence
   - **Exemple** (`ch01/lecon.html`, lignes 36-39) :
     ```css
     .exo .exo-num{font-weight:700;color:var(--p);...}
     details.corr summary{cursor:pointer;font-weight:600;...}
     ```

2. **Format du titre `<title>` inconsistant**
   - ch01-03, ch06-07 : `Ch0X – Titre – Cours`
   - ch04-05 : `Ch.X — Titre — Physique-Chimie 2nde Bac Pro`
   - ch08-14 : `Ch0X — Titre — 2nde Bac Pro`
   - Aucun format unifie

3. **Label place hors du bloc dans ch04 et ch05**
   - Dans `ch04/lecon.html` et `ch05/lecon.html`, le `<span class="label label-def">` est place AVANT le `<div class="def">` au lieu d'etre a l'interieur
   - Exemple (`ch04/lecon.html`, ligne 42-43) :
     ```html
     <span class="label label-def">Definition</span>
     <div class="def">
     ```
   - Devrait etre :
     ```html
     <div class="def">
       <span class="label label-def">Definition</span><br>
     ```

4. **Lien retour incorrect dans ch12**
   - `ch12/lecon.html` pointe vers `../../../index.html` au lieu de `../../../pc-2nde-pro.html`
   - Fichier : `physique-chimie/seconde/ch12/lecon.html`, ligne 26

5. **Absence de classe `.situation` en Seconde**
   - Aucun des 14 fichiers n'utilise la classe `.situation` pour les contextes professionnels
   - Les contextes pro sont integres directement dans `.ex`, `.prop` ou `.meth`
   - C'est un choix acceptable en Seconde mais diminue la visibilite des liens professionnels

---

## 2. Physique-Chimie Premiere ICCER (10 chapitres)

**Note globale : 4.5/5**

### Chapitres couverts
| Ch | Titre | Domaine |
|----|-------|---------|
| 01 | Energie et puissance electrique | Electricite |
| 02 | Transport de l'energie electrique | Electricite |
| 03 | Combustion du carbone et des hydrocarbures | Chimie |
| 04 | Les trois modes de transfert thermique | Thermique |
| 05 | Vitesse et acceleration en mouvement rectiligne | Mecanique |
| 06 | Equilibre d'un solide en rotation (moments) | Mecanique |
| 07 | Pression et force pressante | Mecanique fluides |
| 08 | La force d'Archimede | Mecanique fluides |
| 09 | Solutions aqueuses et concentration | Chimie |
| 10 | Ondes electromagnetiques | Signaux |

### Points forts
- **Situations professionnelles excellentes** : Chaque chapitre commence par une mise en situation professionnelle detaillee et realiste (Lea technicienne chauffagiste, Hugo en stage chez Flamme Energie, Lucas avec une grue de chantier, Emma en maintenance energetique)
- **Metiers reels correctement utilises** : technicien chauffagiste, installateur thermique, plombier chauffagiste, technicienne de maintenance energetique — aucun sigle de filiere dans le contenu
- **Structure tres coherente** : objectifs → situation pro → cours → exemples → methodes → a retenir
- **Qualite scientifique** : les formules sont correctement presentees, les exemples numeriques sont detailles et verifies
- **Ch03 (combustion)** : tres pertinent pour ICCER — lien direct avec les chaudieres a gaz, CO, analyseur de fumees
- **Ch09 (solutions)** : excellent ancrage pro (antigel propylene glycol, desembouant, durete de l'eau)
- **Formule-box** bien utilisees pour mettre en valeur les formules essentielles

### Points faibles

1. **Format des labels inconsistant**
   - **Probleme** : Utilise `<span class="label-def">` (classe unique) au lieu de `<span class="label label-def">` (double classe utilisee partout ailleurs)
   - **Fichiers concernes** : les 10 fichiers de premiere-iccer
   - **Impact** : Le style CSS peut differer de celui des autres sections si `styles.css` cible `.label.label-def`

2. **Classe `.situation` peu utilisee**
   - Seulement 3 occurrences de `class="situation"` sur 10 chapitres
   - 7 chapitres utilisent `class="situation-pro"` (classe personnalisee definie en inline) au lieu de la classe standard `.situation` de `styles.css`
   - Exemple (`ch06/lecon.html`, ligne 41) : `<div class="situation-pro">` avec CSS inline

3. **Pas d'exercices dans les lecons**
   - Contrairement a la Seconde qui inclut des mini-exercices en fin de cours, les lecons ICCER n'en contiennent pas (0 `.exo`)
   - C'est acceptable si les exercices sont dans `exercices.html`, mais les mini-exercices de verification sont pedagogiquement utiles

4. **Titre `<title>` parfois incomplet**
   - ch04 a ch10 : le titre ne mentionne pas "Premiere ICCER (Grpt 1)"
   - ch01-03 : format complet avec la filiere

---

## 3. Physique-Chimie Premiere ERA (10 chapitres)

**Note globale : 4/5**

### Chapitres couverts
| Ch | Titre | Domaine |
|----|-------|---------|
| 01 | Distinguer energie et puissance electrique | Electricite |
| 02 | Evaluer la puissance consommee par un appareil | Electricite |
| 03 | Combustion du carbone et des hydrocarbures | Chimie |
| 04 | Les trois modes de transfert thermique | Thermique |
| 05 | Minimiser les transferts thermiques | Thermique |
| 06 | Equilibre d'un solide en rotation | Mecanique |
| 07 | Pression et force pressante | Mecanique fluides |
| 08 | Solutions aqueuses et concentration | Chimie |
| 09 | Ondes electromagnetiques | Signaux |
| 10 | Propagation d'un signal sonore | Acoustique |

### Points forts
- **Contextes professionnels menuiserie parfaitement cibles** : defonceuse, scie a ruban, raboteuse, ponceuse, aspirateur a copeaux, presse hydraulique, double vitrage, isolation
- **Metiers reels** : menuisier agenceur, ebeniste, installateur d'agencement — aucun sigle de filiere
- **Ch04 (transferts thermiques)** : excellent — tableau de conductivite thermique avec bois (chene, resineux), polystyrene, laine de verre ; graphique Chart.js en echelle logarithmique
- **Ch07 (pression)** : exemples tres concrets (pied de meuble sur parquet, presse hydraulique, verin pneumatique, pistolet a colle)
- **Ch10 (son)** : bon ancrage atelier (bruit des machines, isolation phonique, choix de materiaux absorbants)
- **Classe `.situation` bien utilisee** (14 occurrences)
- **Bonne utilisation des classes CSS** : 49 `.def`, 26 `.prop`, 20 `.att`
- **Exercices integres dans les lecons** (20 `.exo`) — meilleure pratique que ICCER

### Points faibles

1. **Format des labels mixte**
   - 5 fichiers sur 10 utilisent `<span class="label label-def">` (double classe)
   - 5 fichiers utilisent `<span class="label-def">` (classe unique)
   - Manque de coherence au sein meme de la section

2. **Moins de methodes que les autres sections**
   - Seulement 10 blocs `.meth` contre 22 pour ICCER et 25 pour Seconde
   - Les chapitres ERA pourraient beneficier de plus d'encadres "Methode" pour guider les calculs

3. **Structure interne legrement differente de ICCER**
   - Les chapitres communs (ch01 energie/puissance, ch03 combustion, ch04 transferts thermiques, ch06 moments, ch07 pression) ont un decoupage different entre ICCER et ERA
   - ERA ch01 et ch02 traitent separement ce que ICCER traite en un seul ch01
   - Ce n'est pas un defaut en soi (les programmes different), mais la progression doit rester coherente

4. **Pas de chapitre Archimede (present en ICCER)**
   - ICCER a ch08 (Archimede) qui n'a pas d'equivalent en ERA — conforme au programme groupement 3

---

## 4. Physique-Chimie Terminale ICCER (8 chapitres)

**Note globale : 4.5/5**

### Chapitres couverts
| Ch | Titre | Domaine |
|----|-------|---------|
| 01 | Puissance consommee (regime sinusoidal) | Electricite |
| 02 | Courant alternatif / continu | Electricite |
| 03 | Moteur electrique | Electricite |
| 04 | Rayonnement thermique et effet de serre | Thermique |
| 05 | Pression dans un fluide immobile | Mecanique fluides |
| 06 | Transport par un fluide en mouvement | Mecanique fluides |
| 07 | Oxydoreduction et corrosion | Chimie |
| 08 | Signal sonore | Signaux |

### Points forts
- **Niveau scientifique eleve et adapte** : cos phi, triangle des puissances (ch01), loi de Wien et Stefan-Boltzmann (ch04), classification electrochimique (ch07) — contenu de qualite Terminale
- **Simulations interactives** : slider pour la loi de Wien (ch04), courbes sinusoidales SVG (ch01) — excellente interactivite
- **Ancrage professionnel ICCER exemplaire** :
  - Ch01 : dimensionner un disjoncteur et un cable pour un climatiseur
  - Ch04 : camera thermique pour diagnostiquer des ponts thermiques, GES et fluides frigorigenes
  - Ch07 : anodes sacrificielles en magnesium, galvanisation au zinc, protection des ballons ECS
- **Schemas SVG de qualite** : spectre electromagnetique (ch04), courbes sinusoidales (ch01), schema de la classification electrochimique (ch07)
- **Utilisation exemplaire de toutes les classes CSS** : 41 `.def`, 48 `.prop`, 30 `.att`, 23 `.meth`, 11 `.retenir`, 36 `.exo`
- **Exercices integres** : 36 `.exo` repartis dans les chapitres
- **Badges `.ticcer-badge`** correctement utilises dans les titres/liens, pas dans le contenu

### Points faibles

1. **Classe `.situation-pro` inline (1 fichier)**
   - ch01 utilise une classe inline `.situation-pro` au lieu de `.situation`
   - Les autres chapitres utilisent `.situation` (standard) — bonne coherence globale

2. **Titre `<title>` court pour certains chapitres**
   - ch04 : "Ch04 – Rayonnement thermique – Cours" — ne mentionne pas "Terminale ICCER"
   - Devrait inclure le niveau et la filiere pour le SEO et les onglets du navigateur

---

## 5. Physique-Chimie Terminale ERA (8 chapitres)

**Note globale : 3.5/5**

### Chapitres couverts
| Ch | Titre | Domaine |
|----|-------|---------|
| 01 | Transporter l'energie sous forme electrique | Electricite |
| 02 | Stocker l'energie electrochimique | Electricite |
| 03 | Rayonnement thermique et effet de serre | Thermique |
| 04 | Vitesse et acceleration | Mecanique |
| 05 | Oxydoreduction et protection des metaux | Chimie |
| 06 | Choisir une source lumineuse | Optique |
| 07 | Transmettre l'information | Signaux |
| 08 | Attenuer une onde sonore | Acoustique |

### Points forts
- **Diversite thematique** : 8 chapitres couvrant 6 domaines differents
- **Ch01 (transport electrique)** : schema SVG du reseau electrique complet et clair, bonne explication de l'interet de la haute tension via P_J = R * I^2
- **Ch05 (oxydoreduction)** : bien structure, schema SVG du transfert d'electrons entre Zn et Cu2+, methode pas-a-pas pour ecrire les demi-equations
- **Ch08 (attenuation sonore)** : tres pertinent pour ERA (isolation phonique, indice d'affaiblissement R, loi de masse) — ancrage menuiserie parfait
- **Schemas SVG** : bonne qualite (reseau electrique, transfert d'electrons, paroi acoustique)

### Points faibles

1. **Utilisation de la classe `.appli` au lieu de `.situation`**
   - **Fichiers concernes** : les 8 fichiers de terminale-era (28 occurrences totales)
   - **Probleme** : La classe `.appli` est definie dans `styles.css` mais n'est PAS la classe standard des contextes professionnels (qui est `.situation`). Les contextes pro sont presentes dans des blocs `.appli` au lieu de `.situation`
   - Cela diminue la coherence avec les autres sections

2. **Moins de contenu que les autres sections**
   - Seulement 37 `.def`, 19 `.prop`, 15 `.att`, 4 `.meth`, 16 `.ex`
   - Tres peu de `.meth` (4 seulement) : les eleves manquent de guidage methodologique
   - Moins de blocs `.retenir` (9) que les autres sections

3. **Format du titre `<title>` inconsistant**
   - ch01-02, ch05-06 : format "ChX – Titre | ERA-MA (Grpt 3)"
   - ch03-04, ch07-08 : format "Chapitre X – Titre | ERA-MA (Grpt 3)"
   - Pas d'uniformite

4. **Pas de situation professionnelle structuree**
   - Aucune occurrence de `class="situation"` ni de `class="situation-pro"`
   - Les contextes pro sont dans des blocs `.appli` generiques
   - Comparativement, les sections Premiere ERA et ICCER ont des situations pro detaillees avec personnages nommes

5. **Pas d'exercices integres dans les lecons ch01-ch04**
   - Les exercices (28 `.exo`) sont concentres dans les derniers chapitres

---

## Coherence ICCER / ERA

### Modules communs traites dans les deux filieres

| Theme | ICCER | ERA | Coherence |
|-------|-------|-----|-----------|
| Energie/puissance elec | 1ere ch01 | 1ere ch01+ch02 | **Bonne** — ERA decoupe en 2 chapitres mais couvre les memes notions |
| Combustion | 1ere ch03 | 1ere ch03 | **Bonne** — meme contenu, contextes pro differencies |
| Transferts thermiques | 1ere ch04 | 1ere ch04+ch05 | **Bonne** — ERA ajoute un chapitre sur la minimisation (pertinent menuiserie) |
| Moments/rotation | 1ere ch06 | 1ere ch06 | **Bonne** — ICCER = grue/radiateur, ERA = outils de menuiserie |
| Pression | 1ere ch07 | 1ere ch07 | **Bonne** — ICCER = circuits hydrauliques, ERA = presse/verin |
| Solutions chimiques | 1ere ch09 | 1ere ch08 | **Bonne** — ICCER = antigel/desembouant, ERA = produits de traitement du bois |
| Ondes EM | 1ere ch10 | 1ere ch09 | **Bonne** |
| Oxydoreduction | Tle ch07 | Tle ch05 | **Bonne** — ICCER = anode sacrificielle/ballon ECS, ERA = garde-corps/galvanisation |
| Rayonnement thermique | Tle ch04 | Tle ch03 | **Bonne** |
| Acoustique | Tle ch08 | Tle ch08 | **Bonne** — ICCER = signal, ERA = attenuation/isolation |

### Differences legitimes entre les groupements
- **ICCER specifique** : Archimede (1ere ch08), moteur electrique (Tle ch03), pression fluide immobile/mouvement (Tle ch05-06) — lies aux installations thermiques et hydrauliques
- **ERA specifique** : minimisation des transferts thermiques (1ere ch05), signal sonore/attenuation (1ere ch10, Tle ch08), source lumineuse (Tle ch06), transmission de l'information (Tle ch07) — lies a l'amenagement interieur et au batiment

### Bilan : Les contextes pro sont correctement differencies entre ICCER et ERA, sans chevauchement incoherent. Les modules communs sont traites avec un contenu scientifique identique mais des exemples adaptes a chaque filiere.

---

## Progression inter-niveaux

### Electricite : Seconde → Premiere → Terminale

| Niveau | Contenu | Progression |
|--------|---------|-------------|
| 2nde ch02-04 | Circuits, grandeurs U/I/R/P, loi d'Ohm, serie/parallele, Kirchhoff, alternatif | **Base solide** |
| 1ere ICCER ch01-02, ERA ch01-02 | Puissance electrique P=UI, energie E=Pt, kWh, transport HT | **Approfondissement** naturel |
| Tle ICCER ch01-03 | Regime sinusoidal, cos phi, P active/reactive/apparente, moteur | **Specialisation** tres pertinente |
| Tle ERA ch01-02 | Transport HT, stockage electrochimique | **Specialisation** differente mais coherente |

**Verdict** : Progression logique et bien calibree. Les rappels en Premiere sont suffisants. Le saut Premiere → Terminale est ambitieux en ICCER (cos phi, puissances) mais justifie par le profil professionnel.

### Thermique : Seconde → Premiere → Terminale

| Niveau | Contenu | Progression |
|--------|---------|-------------|
| 2nde ch10-12 | Temperature, echelles, capteurs, transferts thermiques, changements d'etat, Q=mL | **Base complete** |
| 1ere ch04 (commun) | 3 modes de transfert (conduction, convection, rayonnement), conductivite lambda | **Approfondissement** quantitatif |
| 1ere ERA ch05 | Minimiser les transferts, resistance thermique R_th | **Specialisation ERA** |
| Tle ch04 ICCER / ch03 ERA | Rayonnement thermique, Wien, Stefan-Boltzmann, camera thermique, GES | **Specialisation** avancee |

**Verdict** : Excellente progression. Le passage de la description qualitative (2nde) a la quantification (1ere) puis aux lois physiques (Tle) est bien calibre.

### Mecanique : Seconde → Premiere → Terminale

| Niveau | Contenu | Progression |
|--------|---------|-------------|
| 2nde ch05-06 | Mouvement, trajectoire, vitesse, forces, equilibre, poids P=mg | **Introduction** |
| 1ere ch05-08 ICCER | Vitesse/acceleration, moments, pression, Archimede | **Approfondissement** avec outils de calcul |
| 1ere ch06-07 ERA | Moments, pression | **Approfondissement** adapte |

**Verdict** : Bonne progression. La Seconde pose les bases qualitatives, la Premiere quantifie. L'absence de mecanique en Terminale (ERA et ICCER) est conforme aux programmes.

### Chimie : Seconde → Premiere → Terminale

| Niveau | Contenu | Progression |
|--------|---------|-------------|
| 2nde ch07-08 | Atome, ions, molecules, formules, solutions, concentration | **Bases** |
| 1ere ch03 (commun) | Combustion, equilibrage d'equations, CO2, CO | **Application** |
| 1ere ch09 ICCER / ch08 ERA | Concentration, dilution, titrage, mole | **Quantitatif** |
| Tle ch07 ICCER / ch05 ERA | Oxydoreduction, corrosion, protection | **Specialisation** |

**Verdict** : Progression logique. Chaque niveau approfondit le precedent. La chimie en Terminale est bien ciblee sur les besoins professionnels.

### Signaux (son, lumiere) : Seconde → Premiere → Terminale

| Niveau | Contenu | Progression |
|--------|---------|-------------|
| 2nde ch01, ch09, ch13-14 | Securite sonore/lumineuse, son (frequence, lambda, vitesse), reflexion/refraction, couleurs | **Decouverte** |
| 1ere ch09/10 ERA | Ondes EM, propagation sonore | **Approfondissement** |
| Tle ch08 ICCER / ch06-08 ERA | Signal sonore, sources lumineuses, attenuation sonore, transmission info | **Specialisation** |

**Verdict** : Bonne couverture. La Seconde est descriptive, la Premiere quantitative, la Terminale appliquee.

---

## Contextes professionnels — Bilan

### Respect de la regle "pas de sigles dans le contenu"
- **Aucune** occurrence de "technicien ICCER", "technicien ERA", "technicien ERA-MA", "technicien MAMA" dans le contenu pedagogique
- **Aucune** occurrence de "Contexte ERA-MA", "Application ICCER", etc.
- Les sigles sont correctement limites aux `<title>`, `<h1>`, `<p class="sous-titre">`, liens de retour et badges

### Metiers reels utilises

| Filiere | Metiers trouves dans le contenu | Conforme |
|---------|--------------------------------|----------|
| ICCER | technicien chauffagiste, technicienne chauffagiste, installateur thermique, plombier chauffagiste, technicienne de maintenance energetique | OUI |
| ERA | menuisier agenceur, ebeniste, menuisier metallier, charpentier-menuisier, fabricant de meubles | OUI |
| Seconde | menuisier (generique) — contextes menuiserie/ameublement | OUI |

### Variete des contextes
- **Seconde** : contextes essentiellement atelier menuiserie + quelques contextes quotidiens (eclair/tonnerre, voiture). Pourrait beneficier de plus de diversite (sport, sante, environnement)
- **Premiere ICCER** : tres bons contextes pro (chaudiere, ballon ECS, climatiseur, circuit de chauffage, grue). Quelques contextes mixtes
- **Premiere ERA** : excellents contextes (defonceuse, scie, presse hydraulique, isolation, menuiseries, double vitrage)
- **Terminale ICCER** : contextes tres specialises et realistes (camera thermique, GES, anode sacrificielle, disjoncteur)
- **Terminale ERA** : contextes bons mais moins detailles (garde-corps, isolation phonique, reseau electrique, chantier)

---

## Problemes identifies (resume hierarchise)

### Priorite HAUTE

1. **Redefinition CSS inline en Seconde** (14 fichiers)
   - `.exo .exo-num`, `details.corr summary`, `details.corr .corr-body` redefinies dans chaque fichier
   - Risque de divergence avec `styles.css`

2. **Inconsistance des classes label** (premiere-iccer : 10 fichiers)
   - `label-def` (classe unique) au lieu de `label label-def` (double classe)
   - Premiere ERA : 5 fichiers sur 10 en format mixte

3. **Classe `.appli` utilisee dans terminale-era** (8 fichiers, 28 occurrences)
   - Devrait etre `.situation` pour la coherence

### Priorite MOYENNE

4. **Terminale ERA : peu de `.meth`** (4 seulement)
   - Les eleves manquent de guidage methodologique
   - Comparer avec Tle ICCER (23 `.meth`)

5. **Titres `<title>` inconsistants** dans toutes les sections
   - Formats melanges (Ch0X vs Ch.X vs Chapitre X, tirets vs tirets longs, avec/sans filiere)

6. **Lien retour incorrect** : `physique-chimie/seconde/ch12/lecon.html` pointe vers `index.html`

7. **Labels hors des blocs** dans `physique-chimie/seconde/ch04/lecon.html` et `ch05/lecon.html`

### Priorite BASSE

8. **Pas de `.situation` en Seconde** (0 occurrences)
   - Les contextes pro existent mais ne sont pas balisees

9. **Terminale ERA : situations pro moins detaillees** que les autres sections
   - Pas de personnage nomme, pas de scenario structure

10. **Mini-exercices absents des lecons ICCER 1ere** (0 `.exo`)
    - Present en Seconde et en ERA, absent en ICCER

---

## Ameliorations restantes

### Priorite haute
- [x] Supprimer les redefinitions CSS inline (`.exo .exo-num`, `details.corr`) dans les 14 fichiers seconde (2026-03-16)
- [x] Uniformiser les labels en `label label-def` dans les 10 fichiers premiere-iccer (deja corrige session 1)
- [x] Uniformiser les labels dans les 5 fichiers premiere-era concernes (deja corrige session 1)
- [x] Remplacer `class="appli"` par `class="situation"` dans les 8 fichiers terminale-era (deja corrige session 1)
- [x] Corriger le lien retour de `physique-chimie/seconde/ch12/lecon.html` (2026-03-16, aussi ch13)

### Priorite moyenne
- [ ] Ajouter des blocs `.meth` dans les chapitres terminale-era (objectif : au moins 2 par chapitre)
- [ ] Uniformiser le format des `<title>` dans toutes les sections
- [ ] Corriger le placement des labels dans `seconde/ch04` et `seconde/ch05`
- [x] Remplacer `class="situation-pro"` par `class="situation"` dans les 7 fichiers premiere-iccer (deja corrige session 1)

### Priorite basse
- [ ] Ajouter des mini-exercices dans les lecons de premiere-iccer
- [ ] Enrichir les situations professionnelles de terminale-era (personnages, scenarios)
- [ ] Diversifier les contextes en Seconde (ajouter sport, sante, environnement)
- [ ] Ajouter la classe `.situation` aux contextes pro existants en Seconde
