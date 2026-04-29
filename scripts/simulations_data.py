"""
Données curées pour la génération des pages simulation.html par chapitre.

Format :
- SIMULATIONS : métadonnées intrinsèques de chaque simulation (titre, icône, description, tags).
  Ces données décrivent ce que la simulation FAIT, indépendamment du chapitre dans lequel
  elle est utilisée.
- CHAPTER_SIMS : pour chaque chapitre, la liste des simulations à présenter, avec une note
  pédagogique chapitre-spécifique (à quoi ça sert, dans le contexte de CE chapitre).
"""

# =============================================================================
# Métadonnées des simulations (intrinsèques au fichier)
# =============================================================================

SIMULATIONS = {
    # ─── MATHS ───────────────────────────────────────────────────────────────
    "proportionnalite.html": {
        "title": "Proportionnalité et pourcentages",
        "icon": "📐",
        "description": "Manipule des situations de proportionnalité (recettes, prix, mélanges) et observe le coefficient en action. Calcule des pourcentages, des augmentations et des réductions sur des cas concrets.",
        "tags": ["Coefficient", "Règle de trois", "Pourcentages"],
    },
    "statistiques.html": {
        "title": "Statistiques — Diagrammes et indicateurs",
        "icon": "📊",
        "description": "Saisis une série statistique et visualise instantanément l'histogramme, le diagramme en bâtons et les indicateurs (moyenne, médiane, étendue). Modifie les valeurs pour observer leur effet sur les indicateurs.",
        "tags": ["Moyenne", "Médiane", "Diagrammes"],
    },
    "probabilites.html": {
        "title": "Probabilités et fluctuation des fréquences",
        "icon": "🎲",
        "description": "Lance des expériences aléatoires (dés, pièces, urnes) un grand nombre de fois et observe la fluctuation des fréquences autour de la probabilité théorique. Visualise la loi des grands nombres en action.",
        "tags": ["Fréquence", "Probabilité", "Loi des grands nombres"],
    },
    "entrainement.html": {
        "title": "Entraînement — Équations du premier degré",
        "icon": "⚖️",
        "description": "Série d'équations du premier degré tirées au hasard, avec correction étape par étape. Travaille la résolution à ton rythme, avec feedback immédiat.",
        "tags": ["Entraînement", "Équations", "1er degré"],
    },
    "equations.html": {
        "title": "Résolveur d'équations",
        "icon": "🧮",
        "description": "Saisis une équation et observe sa résolution détaillée, étape par étape, avec justification de chaque opération.",
        "tags": ["Résolution", "Étapes", "Justification"],
    },
    "entrainement-ineq.html": {
        "title": "Entraînement — Inéquations",
        "icon": "≤",
        "description": "Série d'inéquations du premier degré avec correction. Insiste sur le changement de sens lors de la division par un nombre négatif.",
        "tags": ["Inéquations", "Entraînement", "Sens d'inégalité"],
    },
    "inegalite.html": {
        "title": "Inéquations sur la droite graduée",
        "icon": "↔️",
        "description": "Représente l'ensemble solution d'une inéquation sur la droite graduée. Manipule les bornes et observe l'effet sur l'intervalle solution.",
        "tags": ["Droite graduée", "Intervalles", "Solutions"],
    },
    "fonction-machine.html": {
        "title": "La machine à fonctions",
        "icon": "⚙️",
        "description": "Une machine reçoit une valeur d'entrée x et renvoie une valeur de sortie f(x). Choisis la fonction (linéaire, affine, carrée…) et observe le lien entre x et son image.",
        "tags": ["Image", "Antécédent", "Fonction"],
    },
    "droite-affine.html": {
        "title": "Fonctions linéaire et affine",
        "icon": "📈",
        "description": "Trace une droite y = mx + p en faisant varier la pente m et l'ordonnée à l'origine p. Visualise l'effet de chaque coefficient sur l'allure de la droite.",
        "tags": ["Pente", "Ordonnée à l'origine", "Droite"],
    },
    "traceur.html": {
        "title": "Traceur de fonction du second degré",
        "icon": "📉",
        "description": "Trace la parabole y = ax² + bx + c et fais varier a, b, c avec des curseurs. Observe le sommet, l'axe de symétrie, les racines et l'effet de chaque coefficient.",
        "tags": ["Parabole", "Sommet", "Discriminant"],
    },
    "graphe-equation.html": {
        "title": "Résolution graphique d'équations",
        "icon": "📊",
        "description": "Résous f(x) = k graphiquement en cherchant les points d'intersection de la courbe avec une droite horizontale. Outil idéal pour comprendre l'idée de solution graphique.",
        "tags": ["Intersection", "Lecture graphique", "Solutions"],
    },
    "figures-planes.html": {
        "title": "Figures planes — Périmètres et aires",
        "icon": "▲",
        "description": "Manipule les dimensions des figures usuelles (carré, rectangle, triangle, cercle, trapèze) et observe l'évolution du périmètre et de l'aire en temps réel.",
        "tags": ["Périmètre", "Aire", "Figures usuelles"],
    },
    "pythagore.html": {
        "title": "Théorème de Pythagore",
        "icon": "📐",
        "description": "Fais varier les côtés d'un triangle rectangle et vérifie l'égalité a² + b² = c². Une démonstration visuelle par les aires permet de comprendre pourquoi c'est vrai.",
        "tags": ["Triangle rectangle", "Hypoténuse", "Démonstration"],
    },
    "thales.html": {
        "title": "Théorème de Thalès",
        "icon": "△",
        "description": "Configure une situation classique de Thalès (triangles emboîtés ou opposés par le sommet) et observe les rapports de longueurs égaux. Calcule la longueur inconnue.",
        "tags": ["Triangles semblables", "Rapports", "Configuration"],
    },
    "solides.html": {
        "title": "Solides usuels — Volumes et agrandissement",
        "icon": "🧊",
        "description": "Manipule les dimensions des solides courants (pavé, cylindre, cône, sphère, pyramide) et observe le volume en temps réel. Étudie l'effet d'un agrandissement de coefficient k sur le volume (×k³).",
        "tags": ["Volume", "Solides", "Agrandissement"],
    },
    "stats-2var.html": {
        "title": "Statistiques à deux variables",
        "icon": "📈",
        "description": "Saisis un nuage de points (x, y) et trace la droite d'ajustement par moindres carrés. Calcule le coefficient de corrélation et fais des prévisions par interpolation/extrapolation.",
        "tags": ["Nuage de points", "Régression", "Corrélation"],
    },
    "suites.html": {
        "title": "Suites numériques",
        "icon": "⋯",
        "description": "Génère les termes d'une suite arithmétique ou géométrique en faisant varier le premier terme et la raison. Trace le nuage de points (n, uₙ) et observe le sens de variation.",
        "tags": ["Arithmétique", "Géométrique", "Sens de variation"],
    },
    "derivee.html": {
        "title": "Fonction dérivée et tangente",
        "icon": "ƒ′",
        "description": "Trace la courbe d'une fonction et la tangente en un point que tu déplaces. Observe le lien entre le signe de la dérivée et le sens de variation de la fonction.",
        "tags": ["Tangente", "Sens de variation", "Nombre dérivé"],
    },
    "trigonometrie.html": {
        "title": "Trigonométrie",
        "icon": "📐",
        "description": "Manipule un triangle rectangle (angles, côtés) ou le cercle trigonométrique. Visualise sin, cos et tan d'un angle aigu, et résous des problèmes de hauteur, de pente ou de chevron.",
        "tags": ["sin / cos / tan", "Cercle", "Triangle rectangle"],
    },
    "polynome3.html": {
        "title": "Fonctions polynômes de degré 3",
        "icon": "ƒ(x)",
        "description": "Trace y = ax³ + bx² + cx + d en faisant varier les quatre coefficients. Visualise le tableau de variations, les extremums locaux et le lien avec la dérivée f'(x) = 3ax² + 2bx + c.",
        "tags": ["Cubique", "Extremums", "Dérivée"],
    },
    "exp-log.html": {
        "title": "Fonctions exponentielle et logarithme",
        "icon": "eˣ",
        "description": "Compare les courbes de eˣ et ln(x) sur un même graphique. Manipule les paramètres pour modéliser une décroissance radioactive, un séchage ou une capitalisation continue.",
        "tags": ["Exponentielle", "Logarithme", "Modélisation"],
    },
    "vecteurs.html": {
        "title": "Vecteurs",
        "icon": "→",
        "description": "Construis et combine des vecteurs dans le plan. Visualise la somme, la multiplication par un scalaire, la colinéarité et la décomposition selon une base.",
        "tags": ["Somme", "Colinéarité", "Coordonnées"],
    },
    "integrale.html": {
        "title": "Calcul intégral — Aires sous courbe",
        "icon": "∫",
        "description": "Choisis une fonction et un intervalle, puis observe l'aire sous la courbe. Compare avec l'évaluation par primitive F(b) − F(a) et avec une approximation par rectangles.",
        "tags": ["Aire", "Primitive", "Théorème fondamental"],
    },
    "complexes.html": {
        "title": "Nombres complexes",
        "icon": "ℂ",
        "description": "Place un nombre complexe z = a + ib dans le plan. Calcule son module, son argument, son conjugué et observe l'effet géométrique de l'addition et de la multiplication.",
        "tags": ["Module", "Argument", "Plan complexe"],
    },
    "scalaire.html": {
        "title": "Produit scalaire",
        "icon": "·",
        "description": "Manipule deux vecteurs dans le plan et calcule leur produit scalaire par les trois méthodes (norme/angle, coordonnées, projection). Vérifie l'orthogonalité.",
        "tags": ["Orthogonalité", "Angle", "Projection"],
    },

    # ─── PHYSIQUE-CHIMIE — ÉLECTRICITÉ ───────────────────────────────────────
    "circuit-electrique.html": {
        "title": "Grandeurs électriques et circuits",
        "icon": "🔌",
        "description": "Construis un circuit en série ou en parallèle, branche un voltmètre et un ampèremètre, et mesure les tensions et intensités. Découvre les lois d'unicité et d'additivité.",
        "tags": ["Tension", "Intensité", "Série / Parallèle"],
    },
    "ohm.html": {
        "title": "Loi d'Ohm — Laboratoire virtuel",
        "icon": "Ω",
        "description": "Trace la caractéristique U = f(I) d'un dipôle ohmique et vérifie expérimentalement la proportionnalité U = R × I. Identifie la résistance comme pente de la droite.",
        "tags": ["Résistance", "Caractéristique", "Proportionnalité"],
    },
    "signal-alternatif.html": {
        "title": "Signal alternatif — Oscilloscope virtuel",
        "icon": "∿",
        "description": "Visualise une tension sinusoïdale sur un oscilloscope virtuel. Mesure l'amplitude, la période, la fréquence, et compare valeur efficace et valeur maximale.",
        "tags": ["Sinusoïde", "Période", "Valeur efficace"],
    },
    "puissance.html": {
        "title": "Puissance électrique",
        "icon": "⚡",
        "description": "Calcule la puissance d'un appareil à partir de U et I, puis l'énergie consommée sur une durée donnée. Compare en kWh et en joules, et calcule le coût au tarif EDF.",
        "tags": ["P = UI", "kWh", "Coût"],
    },
    "transformateur.html": {
        "title": "Transformateur et transport d'énergie",
        "icon": "🔁",
        "description": "Manipule un transformateur idéal (rapport de transformation, conservation de la puissance) et comprends pourquoi le transport en très haute tension réduit les pertes Joule.",
        "tags": ["Transformateur", "Très haute tension", "Pertes Joule"],
    },
    "effet-joule.html": {
        "title": "Effet Joule",
        "icon": "🔥",
        "description": "Observe la dissipation thermique P_J = R × I² dans un conducteur. Visualise pourquoi doubler le courant multiplie les pertes par quatre.",
        "tags": ["Pertes", "R × I²", "Dissipation"],
    },
    "redressement.html": {
        "title": "Redressement du courant",
        "icon": "⚡↘",
        "description": "Suis le signal d'une tension alternative à travers un pont de Graetz, puis un filtrage par condensateur. Compare la valeur moyenne avant et après lissage.",
        "tags": ["Pont de Graetz", "Condensateur", "Tension moyenne"],
    },
    "dephasage.html": {
        "title": "Déphasage et triangle des puissances",
        "icon": "△⚡",
        "description": "Visualise le déphasage entre tension et courant dans un circuit alternatif. Décompose la puissance en active (P), réactive (Q) et apparente (S), et observe le facteur de puissance cos φ.",
        "tags": ["Déphasage", "P, Q, S", "cos φ"],
    },
    "moteur.html": {
        "title": "Moteur électrique",
        "icon": "⚙️",
        "description": "Manipule un moteur asynchrone : vitesse synchrone, glissement, couple. Calcule le rendement à partir de la puissance absorbée et de la puissance utile.",
        "tags": ["Vitesse synchrone", "Rendement", "Couple"],
    },
    "transmission-info.html": {
        "title": "Transmettre l'information",
        "icon": "📡",
        "description": "Module et démodule un signal en bande passante. Compare transmissions analogique et numérique, et observe les effets de l'atténuation et du bruit.",
        "tags": ["Modulation", "Numérique", "Bande passante"],
    },

    # ─── PHYSIQUE-CHIMIE — CHIMIE ────────────────────────────────────────────
    "atome.html": {
        "title": "Constructeur d'atomes et d'ions",
        "icon": "⚛️",
        "description": "Construis n'importe quel atome de la table périodique en ajoutant protons, neutrons et électrons. La simulation indique en temps réel l'élément, le nombre de masse, la charge et la stabilité.",
        "tags": ["Composition", "Ions", "Tableau périodique"],
    },
    "atome-couches.html": {
        "title": "Configuration électronique",
        "icon": "🌀",
        "description": "Visualise la répartition des électrons sur les couches K, L, M des 18 premiers éléments. La simulation respecte la règle du remplissage en commençant par la couche la plus proche du noyau.",
        "tags": ["Couches K-L-M", "Stabilité", "Règle de l'octet"],
    },
    "modeles-atome.html": {
        "title": "Histoire du modèle de l'atome",
        "icon": "📜",
        "description": "Parcours interactif des cinq grands modèles : Dalton, Thomson, Rutherford, Bohr et le modèle quantique. Chaque modèle est animé avec les arguments expérimentaux qui ont conduit à le rejeter ou à l'améliorer.",
        "tags": ["Histoire des sciences", "Démarche scientifique"],
    },
    "combustion.html": {
        "title": "Combustion du carbone et des hydrocarbures",
        "icon": "🔥",
        "description": "Équilibre les équations de combustion (méthane, propane, butane) en ajustant les coefficients stœchiométriques. Compare combustion complète et incomplète, et observe les produits formés.",
        "tags": ["Équation bilan", "CH₄ / C₃H₈", "Combustion"],
    },
    "concentration.html": {
        "title": "Solutions chimiques et concentration",
        "icon": "🧪",
        "description": "Prépare une solution par dissolution ou par dilution. Manipule la concentration en masse Cm = m/V et la dilution C₁V₁ = C₂V₂ avec un protocole interactif.",
        "tags": ["Cm = m/V", "Dilution", "Protocole"],
    },
    "oxydoreduction.html": {
        "title": "Oxydoréduction",
        "icon": "🔄",
        "description": "Met en présence un métal et une solution d'ions. Observe les échanges d'électrons, identifie l'oxydant et le réducteur, et écris la demi-équation et l'équation bilan.",
        "tags": ["Oxydant", "Réducteur", "Couple"],
    },
    "pile-electrochimique.html": {
        "title": "Pile électrochimique",
        "icon": "🔋",
        "description": "Construis une pile (Daniell ou autre) en associant deux couples redox. Mesure la tension, identifie l'anode et la cathode, et observe la migration des ions.",
        "tags": ["Anode / Cathode", "Tension", "Couples"],
    },
    "liaisons-chimiques.html": {
        "title": "Liaisons chimiques",
        "icon": "⛓️",
        "description": "Forme des molécules en associant des atomes selon les règles de liaison. Distingue liaisons covalente, ionique et observe la formation des doublets liants et non liants.",
        "tags": ["Covalente", "Ionique", "Doublets"],
    },

    # ─── PHYSIQUE-CHIMIE — MÉCANIQUE ─────────────────────────────────────────
    "mouvement.html": {
        "title": "Mouvement et trajectoire",
        "icon": "🏃",
        "description": "Observe le déplacement d'un objet et identifie le type de mouvement : rectiligne uniforme, accéléré, décéléré, circulaire. Mesure la vitesse moyenne et la vitesse instantanée.",
        "tags": ["Trajectoire", "MRU", "Vitesse"],
    },
    "forces.html": {
        "title": "Forces et équilibre",
        "icon": "💪",
        "description": "Applique des forces (poids, tension, frottement) sur un solide et étudie l'équilibre. Décompose une force selon ses composantes et vérifie la 1ʳᵉ loi de Newton.",
        "tags": ["Équilibre", "Newton", "Décomposition"],
    },
    "vitesse-acceleration.html": {
        "title": "Vitesse et accélération",
        "icon": "🚗",
        "description": "Suis un mobile en mouvement rectiligne et trace les graphiques v(t) et a(t). Distingue mouvement uniforme, uniformément accéléré et décéléré.",
        "tags": ["MRU / MRUA", "Décélération", "Graphique v(t)"],
    },
    "moments.html": {
        "title": "Moments d'une force et équilibre en rotation",
        "icon": "⚙️",
        "description": "Place des forces sur un solide pouvant tourner autour d'un axe (balance, levier, grue). Calcule les moments M = F × d et vérifie l'équilibre par ΣM = 0.",
        "tags": ["Bras de levier", "Couple", "Équilibre"],
    },

    # ─── PHYSIQUE-CHIMIE — FLUIDES ───────────────────────────────────────────
    "pression.html": {
        "title": "Pression dans un fluide",
        "icon": "📏",
        "description": "Étudie la pression à différentes profondeurs dans un fluide (P = ρgh). Convertis entre Pa, hPa et bar, et applique le principe de Pascal.",
        "tags": ["P = F/S", "Hauteur d'eau", "Pascal"],
    },
    "archimede.html": {
        "title": "Force d'Archimède",
        "icon": "🛟",
        "description": "Plonge des objets de différentes densités dans plusieurs fluides. Mesure la poussée F_A = ρ × V × g et prévois si l'objet flotte, coule ou reste entre deux eaux.",
        "tags": ["Poussée", "Densité", "Flottabilité"],
    },
    "presse-hydraulique.html": {
        "title": "Presse hydraulique",
        "icon": "🔧",
        "description": "Manipule deux pistons de surfaces différentes reliés par un fluide. Vérifie la conservation de la pression et calcule le facteur d'amplification de la force.",
        "tags": ["Pascal", "Amplification", "Pistons"],
    },
    "boyle-mariotte.html": {
        "title": "Loi de Boyle-Mariotte",
        "icon": "🎈",
        "description": "Comprime ou dilate un gaz à température constante et observe la relation P × V = constante. Adapte le protocole à un compresseur ou à un vase d'expansion.",
        "tags": ["Gaz parfait", "P × V", "Isotherme"],
    },
    "gaz.html": {
        "title": "Gaz parfait — Influence de la température",
        "icon": "♨️",
        "description": "Fais varier la température, le volume ou la quantité d'un gaz et observe l'effet sur la pression. Visualise PV = nRT et le mouvement des molécules.",
        "tags": ["PV = nRT", "Agitation", "Mole"],
    },
    "debit.html": {
        "title": "Débit d'un fluide",
        "icon": "💧",
        "description": "Manipule un fluide circulant dans une canalisation. Calcule le débit volumique Qv = V/t et le débit massique Qm = ρ × Qv.",
        "tags": ["Débit volumique", "Débit massique", "Conservation"],
    },
    "debit-fluide.html": {
        "title": "Débit et équation de continuité",
        "icon": "🌊",
        "description": "Étudie le passage d'un fluide d'une section S₁ à une section S₂. Vérifie l'équation de continuité S₁v₁ = S₂v₂ et applique-la au dimensionnement d'un réseau.",
        "tags": ["Continuité", "Vitesse", "Section"],
    },

    # ─── PHYSIQUE-CHIMIE — THERMIQUE ─────────────────────────────────────────
    "chaleur.html": {
        "title": "Température et énergie thermique",
        "icon": "🌡️",
        "description": "Mesure l'élévation de température d'un corps en lui apportant une énergie. Distingue chaleur (transfert d'énergie) et température (état d'agitation).",
        "tags": ["Q = mcΔT", "Chaleur", "Capacité"],
    },
    "transferts-thermiques.html": {
        "title": "Transferts thermiques et équilibre",
        "icon": "♨️",
        "description": "Met en contact deux corps à températures différentes et observe la mise en équilibre. Identifie les trois modes de transfert (conduction, convection, rayonnement).",
        "tags": ["Conduction", "Convection", "Équilibre"],
    },
    "changement-etat.html": {
        "title": "Courbe de chauffage — Changements d'état",
        "icon": "🧊",
        "description": "Chauffe un corps pur ou un mélange et trace T = f(t). Observe les paliers de fusion et d'ébullition pour le corps pur, et leur absence pour un mélange.",
        "tags": ["Fusion", "Ébullition", "Palier"],
    },
    "conductance-thermique.html": {
        "title": "Conductance thermique et isolation",
        "icon": "🏠",
        "description": "Compare l'efficacité d'isolation de différents matériaux (laine de verre, polystyrène, bois, béton). Manipule λ et l'épaisseur pour minimiser le flux thermique.",
        "tags": ["λ (lambda)", "Isolation", "Flux"],
    },
    "paroi-multicouche.html": {
        "title": "Paroi multicouche",
        "icon": "🧱",
        "description": "Construis une paroi composée (placo, isolant, brique, parement) et calcule la résistance thermique totale R = Σ Rᵢ. Visualise l'évolution de la température en chaque point.",
        "tags": ["Résistance R", "Multicouche", "Profil de T"],
    },
    "comparateur-vitrages.html": {
        "title": "Comparateur de vitrages",
        "icon": "🪟",
        "description": "Compare simple, double et triple vitrage selon leurs coefficients Ug. Calcule les pertes thermiques annuelles et le retour sur investissement.",
        "tags": ["Ug", "Vitrage", "Pertes"],
    },
    "rayonnement.html": {
        "title": "Rayonnement thermique",
        "icon": "🌞",
        "description": "Étudie l'émission d'un corps chauffé selon sa température. Applique la loi de Wien (λmax = 2,898 × 10⁻³ / T) pour relier température et longueur d'onde maximale d'émission.",
        "tags": ["Loi de Wien", "Spectre", "Émission"],
    },
    "serre.html": {
        "title": "Effet de serre",
        "icon": "🌍",
        "description": "Modélise les échanges entre le Soleil, la Terre et l'atmosphère. Fais varier la concentration des gaz à effet de serre et observe l'équilibre thermique de la planète.",
        "tags": ["GES", "Albedo", "Bilan radiatif"],
    },
    "ctn-pt100-comparaison.html": {
        "title": "Capteurs de température : CTN vs Pt100",
        "icon": "🌡️",
        "description": "Compare deux capteurs : la CTN (résistance qui diminue avec T) et la Pt100 (résistance qui augmente linéairement). Trace R = f(T) et identifie le capteur adapté.",
        "tags": ["CTN", "Pt100", "Caractéristique"],
    },
    "ctn-etuve-regulation.html": {
        "title": "Régulation d'étuve avec CTN",
        "icon": "🔬",
        "description": "Pilote une étuve avec une CTN comme capteur. Règle un seuil de température et observe le comportement du système (tout-ou-rien, hystérésis).",
        "tags": ["Régulation", "Seuil", "Hystérésis"],
    },
    "dilatation-parquet.html": {
        "title": "Dilatation thermique du parquet",
        "icon": "📏",
        "description": "Calcule la dilatation d'un parquet bois selon la variation de température et d'humidité. Comprends pourquoi un joint de dilatation périphérique est obligatoire.",
        "tags": ["Dilatation", "Coefficient", "Joint"],
    },
    "anisotropie-bois.html": {
        "title": "Anisotropie du bois",
        "icon": "🌳",
        "description": "Visualise les trois directions du bois (radiale, tangentielle, longitudinale) et leurs comportements différents face à l'humidité, au retrait et aux contraintes.",
        "tags": ["Bois", "Retrait", "Directions"],
    },

    # ─── PHYSIQUE-CHIMIE — OPTIQUE & ONDES ───────────────────────────────────
    "refraction.html": {
        "title": "Réflexion et réfraction de la lumière",
        "icon": "🔬",
        "description": "Envoie un rayon lumineux à l'interface entre deux milieux et observe la réflexion et la réfraction. Vérifie la loi de Snell-Descartes et identifie l'angle limite.",
        "tags": ["Snell-Descartes", "Indice", "Angle limite"],
    },
    "sources-lumineuses.html": {
        "title": "Sources lumineuses",
        "icon": "💡",
        "description": "Compare les spectres d'émission de différentes sources : soleil, ampoule à incandescence, néon, LED. Distingue spectre continu et spectre de raies.",
        "tags": ["Spectre", "LED", "Raies"],
    },
    "melangeur.html": {
        "title": "Mélangeur RVB",
        "icon": "🎨",
        "description": "Mélange les trois lumières primaires (rouge, vert, bleu) en synthèse additive. Reproduis les couleurs secondaires (cyan, magenta, jaune) et le blanc.",
        "tags": ["RVB", "Synthèse additive", "Couleurs"],
    },
    "eclairage-atelier.html": {
        "title": "Éclairage d'atelier",
        "icon": "🔦",
        "description": "Dimensionne l'éclairage d'un atelier selon la surface et la tâche à réaliser. Calcule l'éclairement (lux) et compare différents types de luminaires.",
        "tags": ["Éclairement", "Lux", "Atelier"],
    },
    "son-2nde.html": {
        "title": "Caractéristiques d'un son",
        "icon": "🔊",
        "description": "Manipule un son virtuel : modifie la fréquence (hauteur), l'amplitude (volume) et la forme (timbre). Visualise simultanément la forme d'onde et le spectre.",
        "tags": ["Hauteur", "Volume", "Timbre"],
    },
    "son.html": {
        "title": "Signal sonore",
        "icon": "🎵",
        "description": "Génère un signal sonore et étudie sa fréquence, sa période et son intensité. Calcule le niveau sonore en décibels L = 10 × log(I/I₀).",
        "tags": ["Fréquence", "Décibels", "Intensité"],
    },
    "attenuation-sonore.html": {
        "title": "Atténuation sonore",
        "icon": "🔇",
        "description": "Étudie l'affaiblissement d'un son à travers une paroi (loi de masse) ou par distance. Calcule l'indice d'affaiblissement R en dB et compare différents matériaux acoustiques.",
        "tags": ["Loi de masse", "Affaiblissement", "Acoustique"],
    },
    "ondes-em.html": {
        "title": "Spectre électromagnétique",
        "icon": "📡",
        "description": "Parcours le spectre des ondes EM : ondes radio, micro-ondes, infrarouge, visible, UV, X, gamma. Pour chaque domaine : longueur d'onde, fréquence, applications.",
        "tags": ["λ = c/f", "Spectre", "Applications"],
    },

    # ─── DIVERS / TRANSVERSAL ────────────────────────────────────────────────
    "balance.html": {
        "title": "Balance et masse volumique",
        "icon": "⚖️",
        "description": "Pèse différents matériaux et calcule leur masse volumique ρ = m/V. Compare la densité de matériaux courants (bois, fer, plastique, eau).",
        "tags": ["Masse volumique", "Densité", "ρ = m/V"],
    },
    "calepinage.html": {
        "title": "Calepinage",
        "icon": "▦",
        "description": "Place des éléments (carreaux, panneaux, briques) sur une surface en respectant les contraintes de pose. Calcule le métré et les chutes.",
        "tags": ["Pose", "Métré", "Chutes"],
    },
    "ccf-bac-rangement.html": {
        "title": "CCF — Rangement (PSE)",
        "icon": "📦",
        "description": "Étude de cas de rangement d'atelier appliquant les principes d'ergonomie et de prévention des risques.",
        "tags": ["PSE", "Ergonomie", "CCF"],
    },
    "escalier-blondel.html": {
        "title": "Escalier — Formule de Blondel",
        "icon": "🪜",
        "description": "Dimensionne un escalier (giron, hauteur de marche, échappée) en respectant la formule de Blondel : 2h + g ≈ 64 cm. Vérifie la conformité aux normes de construction.",
        "tags": ["Blondel", "Giron", "Marches"],
    },
}


# =============================================================================
# Mapping chapitre → simulations + notes pédagogiques chapitre-spécifiques
# =============================================================================

CHAPTER_SIMS = {
    # ─── MATHS SECONDE ───────────────────────────────────────────────────────
    "maths/seconde/ch01": {
        "sims": ["proportionnalite.html"],
        "pedagogy": {
            "proportionnalite.html": "Utilise cette simulation pour t'approprier la notion de coefficient et la règle de trois sur des cas variés (recettes, prix, mélanges) avant d'aborder les exercices d'application.",
        },
    },
    "maths/seconde/ch02": {
        "sims": ["statistiques.html"],
        "pedagogy": {
            "statistiques.html": "Pour visualiser comment changer une valeur extrême modifie la moyenne mais peu la médiane — un argument visuel solide pour comprendre quand utiliser quel indicateur.",
        },
    },
    "maths/seconde/ch03": {
        "sims": ["statistiques.html"],
        "pedagogy": {
            "statistiques.html": "Mêmes outils que ch02, mais utilisés cette fois pour explorer l'étendue, l'écart-type et leur lien avec la dispersion. Modifie les valeurs et observe l'effet sur la dispersion.",
        },
    },
    "maths/seconde/ch04": {
        "sims": ["probabilites.html"],
        "pedagogy": {
            "probabilites.html": "Lance la simulation un grand nombre de fois et observe la stabilisation des fréquences. C'est la meilleure façon de saisir intuitivement la loi des grands nombres.",
        },
    },
    "maths/seconde/ch05": {
        "sims": ["entrainement.html", "equations.html"],
        "pedagogy": {
            "entrainement.html": "Pour s'entraîner sans sortir le cahier : la simulation génère des équations à la volée, avec correction immédiate. Idéal en autonomie ou en remédiation.",
            "equations.html": "Quand tu bloques sur une équation : entre-la et regarde la résolution étape par étape. Sert de modèle de rédaction pour tes propres copies.",
        },
    },
    "maths/seconde/ch06": {
        "sims": ["entrainement-ineq.html", "inegalite.html"],
        "pedagogy": {
            "entrainement-ineq.html": "Insiste sur le moment-clé du chapitre : le changement de sens lors d'une division par un nombre négatif. La simulation t'oblige à le faire à chaque exercice.",
            "inegalite.html": "Visualise un intervalle solution sur la droite graduée. Crochet ouvert, crochet fermé, demi-droite — tout devient évident graphiquement.",
        },
    },
    "maths/seconde/ch07": {
        "sims": ["fonction-machine.html"],
        "pedagogy": {
            "fonction-machine.html": "Mets-toi dans la peau de la fonction : reçois x, applique la règle, renvoie f(x). Idéal pour saisir l'idée d'image et d'antécédent avant le formalisme.",
        },
    },
    "maths/seconde/ch08": {
        "sims": ["droite-affine.html"],
        "pedagogy": {
            "droite-affine.html": "Manipule les curseurs m et p et observe l'effet : la pente m incline la droite, l'ordonnée p la translate. Ces deux paramètres résument tout sur les fonctions affines.",
        },
    },
    "maths/seconde/ch09": {
        "sims": ["droite-affine.html"],
        "pedagogy": {
            "droite-affine.html": "Utilisée ici pour résoudre graphiquement des équations f(x) = k et lire des solutions d'inéquations sur le graphique.",
        },
    },
    "maths/seconde/ch10": {
        "sims": ["traceur.html"],
        "pedagogy": {
            "traceur.html": "Joue avec le coefficient a pour voir l'orientation de la parabole, b pour le décalage, c pour la translation verticale. Une intuition graphique solide qui aide ensuite pour les calculs.",
        },
    },
    "maths/seconde/ch11": {
        "sims": ["figures-planes.html"],
        "pedagogy": {
            "figures-planes.html": "Manipule les dimensions et observe que doubler une longueur ne double pas l'aire (× 4). Concept-clé pour les exercices d'agrandissement.",
        },
    },
    "maths/seconde/ch12": {
        "sims": ["pythagore.html"],
        "pedagogy": {
            "pythagore.html": "La démonstration visuelle par les aires donne une compréhension intuitive du « pourquoi ça marche », au-delà de la formule.",
        },
    },
    "maths/seconde/ch13": {
        "sims": ["thales.html"],
        "pedagogy": {
            "thales.html": "Manipule les positions et observe que les rapports sont conservés. Pratique pour distinguer la configuration directe et la configuration en X (papillon).",
        },
    },
    "maths/seconde/ch14": {
        "sims": ["solides.html"],
        "pedagogy": {
            "solides.html": "Découvre la règle des coefficients d'agrandissement : longueur × k, aire × k², volume × k³. Les chiffres parlent mieux que les formules.",
        },
    },

    # ─── MATHS PREMIÈRE ──────────────────────────────────────────────────────
    "maths/premiere/ch01": {
        "sims": ["stats-2var.html"],
        "pedagogy": {
            "stats-2var.html": "Place tes points, ajoute un point aberrant et observe l'effet sur la droite d'ajustement et le coefficient de corrélation. Tu comprends en quelques secondes pourquoi un point extrême peut tout fausser.",
        },
    },
    "maths/premiere/ch03": {
        "sims": ["suites.html"],
        "pedagogy": {
            "suites.html": "Compare une suite arithmétique (croissance linéaire) et une suite géométrique (croissance exponentielle) sur le même graphique. La différence saute aux yeux.",
        },
    },
    "maths/premiere/ch04": {
        "sims": ["graphe-equation.html"],
        "pedagogy": {
            "graphe-equation.html": "Avant d'apprendre à résoudre algébriquement, comprends d'abord ce qu'est une solution : un point d'intersection. La résolution algébrique aura ensuite plus de sens.",
        },
    },
    "maths/premiere/ch05": {
        "sims": ["traceur.html"],
        "pedagogy": {
            "traceur.html": "Reprise du traceur de seconde, mais utilisé pour étudier les variations, le sommet, et résoudre ax² + bx + c = 0 avec le discriminant.",
        },
    },
    "maths/premiere/ch06": {
        "sims": ["derivee.html"],
        "pedagogy": {
            "derivee.html": "Déplace le point de tangence sur la courbe et observe la pente changer. Le lien dérivée ↔ tangente devient évident, et les variations se déduisent visuellement.",
        },
    },
    "maths/premiere/ch09": {
        "sims": ["trigonometrie.html"],
        "pedagogy": {
            "trigonometrie.html": "Utilise l'outil pour des problèmes pro : calcul d'une hauteur de bâtiment, d'une longueur de chevron, d'un angle de pente.",
        },
    },

    # ─── MATHS TERMINALE ─────────────────────────────────────────────────────
    "maths/terminale/ch01": {
        "sims": ["stats-2var.html"],
        "pedagogy": {
            "stats-2var.html": "Étend le travail de Première à des séries plus complexes. Discute de la pertinence de l'ajustement affine selon la valeur du coefficient de corrélation.",
        },
    },
    "maths/terminale/ch03": {
        "sims": ["suites.html"],
        "pedagogy": {
            "suites.html": "Calcule les sommes partielles et observe la convergence (ou divergence) selon la raison q. Concept-clé pour les exercices d'épargne et d'amortissement.",
        },
    },
    "maths/terminale/ch04": {
        "sims": ["polynome3.html"],
        "pedagogy": {
            "polynome3.html": "Manipule les quatre coefficients et observe : sens d'allure (selon le signe de a), nombre d'extremums (selon le discriminant de la dérivée), zéros de la fonction.",
        },
    },
    "maths/terminale/ch05": {
        "sims": ["exp-log.html"],
        "pedagogy": {
            "exp-log.html": "Observe l'allure des courbes y = aˣ et y = log(x), et leurs comportements asymptotiques. Très utile pour les exercices de modélisation pro (PCI, atténuation, décibels).",
        },
    },
    "maths/terminale/ch06": {
        "sims": ["vecteurs.html"],
        "pedagogy": {
            "vecteurs.html": "Construis les vecteurs et leurs sommes graphiquement (méthode du parallélogramme), puis vérifie avec les coordonnées. Lien direct avec les forces en physique.",
        },
    },
    "maths/terminale/ch07": {
        "sims": ["trigonometrie.html"],
        "pedagogy": {
            "trigonometrie.html": "En complément du cours, utilise la simulation pour le cercle trigonométrique et les valeurs remarquables (0, π/6, π/4, π/3, π/2).",
        },
    },
    "maths/terminale/ch08": {
        "sims": ["integrale.html"],
        "pedagogy": {
            "integrale.html": "Visualise l'aire sous la courbe en faisant glisser les bornes a et b. Compare avec l'évaluation par primitive — les deux approches donnent le même nombre, c'est le théorème fondamental.",
        },
    },
    "maths/terminale/ch09": {
        "sims": ["exp-log.html"],
        "pedagogy": {
            "exp-log.html": "Modélise des phénomènes du quotidien : refroidissement (Newton), séchage du bois, capitalisation continue. Ajuste les paramètres et compare au tableau de valeurs réel.",
        },
    },
    "maths/terminale/ch10": {
        "sims": ["complexes.html"],
        "pedagogy": {
            "complexes.html": "Place un complexe dans le plan, calcule son module et son argument. Application directe en électricité (impédance Z = R + jX en alternatif).",
        },
    },
    "maths/terminale/ch11": {
        "sims": ["scalaire.html"],
        "pedagogy": {
            "scalaire.html": "Manipule deux vecteurs et observe quand le produit scalaire est nul (orthogonalité) ou maximal (vecteurs colinéaires de même sens).",
        },
    },

    # ─── PC SECONDE ──────────────────────────────────────────────────────────
    "physique-chimie/seconde/ch02": {
        "sims": ["circuit-electrique.html"],
        "pedagogy": {
            "circuit-electrique.html": "Construis tes premiers circuits virtuels avant de manipuler le vrai matériel. Place les appareils de mesure et anticipe les valeurs avant de mesurer.",
        },
    },
    "physique-chimie/seconde/ch03": {
        "sims": ["ohm.html"],
        "pedagogy": {
            "ohm.html": "Trace toi-même la caractéristique d'un dipôle ohmique. La pente de la droite EST la résistance — un résultat expérimental que la simulation rend incontestable.",
        },
    },
    "physique-chimie/seconde/ch04": {
        "sims": ["signal-alternatif.html"],
        "pedagogy": {
            "signal-alternatif.html": "Manipule un oscilloscope virtuel sans craindre de le casser. Apprends à régler la base de temps et la sensibilité verticale, puis mesure période et amplitude.",
        },
    },
    "physique-chimie/seconde/ch05": {
        "sims": ["mouvement.html"],
        "pedagogy": {
            "mouvement.html": "Observe différents types de mouvements et apprends à les nommer. Utilise un chronométrage virtuel pour mesurer une vitesse moyenne.",
        },
    },
    "physique-chimie/seconde/ch06": {
        "sims": ["forces.html"],
        "pedagogy": {
            "forces.html": "Combine plusieurs forces (poids, tension, frottement) sur un objet et trouve la condition d'équilibre. La représentation vectorielle devient concrète.",
        },
    },
    "physique-chimie/seconde/ch07": {
        "sims": ["atome.html", "atome-couches.html", "modeles-atome.html"],
        "pedagogy": {
            "atome.html": "À utiliser pour comprendre la composition d'un atome neutre, distinguer un atome d'un ion, et observer comment la nature de l'élément dépend du nombre de protons.",
            "atome-couches.html": "Indispensable pour comprendre pourquoi certains éléments sont chimiquement stables et d'autres non. Sert aussi à prévoir les ions formés (gain ou perte d'électrons pour atteindre une couche externe pleine).",
            "modeles-atome.html": "Donne une perspective historique : la science n'est pas une vérité figée, mais une démarche d'amélioration progressive. Utile pour comprendre pourquoi nos modèles d'aujourd'hui sont des outils, pas des photographies de la réalité.",
        },
    },
    "physique-chimie/seconde/ch08": {
        "sims": ["concentration.html"],
        "pedagogy": {
            "concentration.html": "Prépare une solution virtuelle avec le bon protocole avant de passer au laboratoire. La simulation guide chaque étape (peser, dissoudre, compléter au trait de jauge).",
        },
    },
    "physique-chimie/seconde/ch09": {
        "sims": ["son-2nde.html"],
        "pedagogy": {
            "son-2nde.html": "Modifie la fréquence et entends la hauteur changer. Modifie l'amplitude et entends le volume changer. Le son devient mesurable et compréhensible.",
        },
    },
    "physique-chimie/seconde/ch10": {
        "sims": ["chaleur.html"],
        "pedagogy": {
            "chaleur.html": "Distingue les notions souvent confondues : chaleur (transfert d'énergie) vs température (état d'agitation). La simulation montre clairement la différence.",
        },
    },
    "physique-chimie/seconde/ch11": {
        "sims": ["transferts-thermiques.html"],
        "pedagogy": {
            "transferts-thermiques.html": "Mets en contact deux corps et observe l'évolution vers l'équilibre. Identifie chaque mode de transfert sur des exemples concrets (radiateur, fenêtre, chaudière).",
        },
    },
    "physique-chimie/seconde/ch12": {
        "sims": ["changement-etat.html"],
        "pedagogy": {
            "changement-etat.html": "Trace la courbe T = f(t) pour de l'eau pure et pour de l'eau salée. Observe la différence : palier net pour le corps pur, montée progressive pour le mélange.",
        },
    },
    "physique-chimie/seconde/ch13": {
        "sims": ["refraction.html"],
        "pedagogy": {
            "refraction.html": "Fais varier l'angle d'incidence et observe la réfraction au passage air→eau. Trouve l'angle limite à partir duquel la réfraction devient une réflexion totale.",
        },
    },
    "physique-chimie/seconde/ch14": {
        "sims": ["sources-lumineuses.html", "melangeur.html"],
        "pedagogy": {
            "sources-lumineuses.html": "Compare les spectres : continu pour le soleil et l'incandescence, raies pour le néon, peigne pour la LED. Chaque source a sa signature spectrale.",
            "melangeur.html": "Découvre la synthèse additive : R + V + B = blanc. Reproduis les couleurs secondaires. Application : éclairage de scène, écrans LED, signalétique.",
        },
    },

    # ─── PC 1ère ICCER ───────────────────────────────────────────────────────
    "physique-chimie/premiere-iccer/ch01": {
        "sims": ["puissance.html"],
        "pedagogy": {
            "puissance.html": "Calcule la puissance d'un appareil de chauffage et l'énergie consommée sur une saison. Compare en kWh et estime le coût annuel au tarif EDF.",
        },
    },
    "physique-chimie/premiere-iccer/ch02": {
        "sims": ["transformateur.html", "effet-joule.html"],
        "pedagogy": {
            "transformateur.html": "Comprends pourquoi le réseau électrique fonctionne en très haute tension : moins de courant pour la même puissance, donc moins de pertes Joule.",
            "effet-joule.html": "Observe la dépendance en I² des pertes : doubler le courant multiplie les pertes par quatre. Argument décisif pour le transport en haute tension.",
        },
    },
    "physique-chimie/premiere-iccer/ch03": {
        "sims": ["combustion.html"],
        "pedagogy": {
            "combustion.html": "Équilibre les équations de combustion des gaz utilisés en chauffage (méthane, propane, butane) et calcule les émissions de CO₂ par kWh produit.",
        },
    },
    "physique-chimie/premiere-iccer/ch04": {
        "sims": ["conductance-thermique.html"],
        "pedagogy": {
            "conductance-thermique.html": "Compare l'efficacité d'isolation des matériaux courants en chauffage. Choisis l'épaisseur d'isolant nécessaire pour atteindre une résistance R donnée.",
        },
    },
    "physique-chimie/premiere-iccer/ch05": {
        "sims": ["vitesse-acceleration.html"],
        "pedagogy": {
            "vitesse-acceleration.html": "Étudie le mouvement d'un fluide dans une canalisation, ou d'un véhicule de service en intervention. Distingue mouvement uniforme et accéléré.",
        },
    },
    "physique-chimie/premiere-iccer/ch06": {
        "sims": ["moments.html"],
        "pedagogy": {
            "moments.html": "Comprends pourquoi une clé longue serre mieux qu'une clé courte. Application pro : choix du couple de serrage pour les raccords de plomberie.",
        },
    },
    "physique-chimie/premiere-iccer/ch07": {
        "sims": ["pression.html"],
        "pedagogy": {
            "pression.html": "Étudie la pression dans un circuit de chauffage (manomètre chaudière, vase d'expansion). Convertis entre Pa, hPa et bar (l'unité métier).",
        },
    },
    "physique-chimie/premiere-iccer/ch08": {
        "sims": ["archimede.html"],
        "pedagogy": {
            "archimede.html": "Comprends pourquoi un flotteur de chasse d'eau monte ou descend selon le niveau. Applique le principe à des composants réels d'installation.",
        },
    },
    "physique-chimie/premiere-iccer/ch09": {
        "sims": ["concentration.html"],
        "pedagogy": {
            "concentration.html": "Prépare une solution antitartre ou un produit de nettoyage à la bonne concentration. Maîtrise le facteur de dilution pour économiser du produit.",
        },
    },
    "physique-chimie/premiere-iccer/ch10": {
        "sims": ["ondes-em.html"],
        "pedagogy": {
            "ondes-em.html": "Identifie le domaine d'utilisation des ondes en chauffage : infrarouge (panneaux radiants), micro-ondes (chauffage par induction), Wi-Fi (régulation à distance).",
        },
    },

    # ─── PC 1ère ERA ─────────────────────────────────────────────────────────
    "physique-chimie/premiere-era/ch01": {
        "sims": ["puissance.html"],
        "pedagogy": {
            "puissance.html": "Dimensionne l'alimentation électrique d'une machine d'atelier (toupie, scie circulaire, ponceuse) en calculant sa puissance et son courant absorbé.",
        },
    },
    "physique-chimie/premiere-era/ch02": {
        "sims": ["puissance.html"],
        "pedagogy": {
            "puissance.html": "Compare la consommation de différents équipements d'atelier sur une journée et calcule le coût électrique mensuel.",
        },
    },
    "physique-chimie/premiere-era/ch03": {
        "sims": ["combustion.html"],
        "pedagogy": {
            "combustion.html": "En menuiserie, applique la combustion aux poêles à bois et aux chaudières biomasse. Calcule le PCI du bois et compare aux énergies fossiles.",
        },
    },
    "physique-chimie/premiere-era/ch04": {
        "sims": ["conductance-thermique.html"],
        "pedagogy": {
            "conductance-thermique.html": "Compare les performances thermiques des matériaux bois (chêne, pin, panneau d'aggloméré) et choisis le bon assemblage pour un meuble exposé.",
        },
    },
    "physique-chimie/premiere-era/ch05": {
        "sims": ["conductance-thermique.html"],
        "pedagogy": {
            "conductance-thermique.html": "Dimensionne l'isolation d'un agencement intégré (placard adossé à un mur extérieur, cuisine sous combles) en respectant la RT 2020.",
        },
    },
    "physique-chimie/premiere-era/ch06": {
        "sims": ["moments.html"],
        "pedagogy": {
            "moments.html": "Application directe en menuiserie : dimensionner une étagère sans qu'elle ne bascule, choisir le couple de serrage pour les vis d'assemblage.",
        },
    },
    "physique-chimie/premiere-era/ch07": {
        "sims": ["pression.html"],
        "pedagogy": {
            "pression.html": "Comprends la pression dans un compresseur d'atelier et son rôle dans une cloueuse pneumatique ou une presse hydraulique.",
        },
    },
    "physique-chimie/premiere-era/ch08": {
        "sims": ["concentration.html"],
        "pedagogy": {
            "concentration.html": "Prépare une teinture, un vernis ou un décapant à la bonne concentration. Compétence pro directement utile pour la finition des ouvrages.",
        },
    },
    "physique-chimie/premiere-era/ch09": {
        "sims": ["ondes-em.html"],
        "pedagogy": {
            "ondes-em.html": "Identifie les radiations utilisées en menuiserie : UV (durcissement de vernis), infrarouge (séchage du bois), laser (découpe de précision).",
        },
    },
    "physique-chimie/premiere-era/ch10": {
        "sims": ["son.html"],
        "pedagogy": {
            "son.html": "Mesure le niveau sonore en atelier (scie, ponceuse) et identifie les seuils de protection auditive obligatoire (80 dB, 85 dB).",
        },
    },

    # ─── PC TERMINALE ICCER ──────────────────────────────────────────────────
    "physique-chimie/terminale-iccer/ch01": {
        "sims": ["puissance.html", "dephasage.html"],
        "pedagogy": {
            "puissance.html": "Reprends les bases avant d'aborder la puissance en alternatif. Solidifie U × I × cos φ et la relation entre puissance active, réactive et apparente.",
            "dephasage.html": "Comprends pourquoi un moteur a un facteur de puissance < 1 et comment compenser avec un condensateur. Réduction concrète de la facture EDF.",
        },
    },
    "physique-chimie/terminale-iccer/ch02": {
        "sims": ["redressement.html", "dephasage.html"],
        "pedagogy": {
            "redressement.html": "Suis le signal d'une tension alternative à travers un pont de Graetz puis un condensateur de filtrage. Application directe : alimentation des cartes électroniques de chaudières.",
            "dephasage.html": "Visualise le déphasage induit par une bobine ou un condensateur, et l'effet sur le facteur de puissance.",
        },
    },
    "physique-chimie/terminale-iccer/ch03": {
        "sims": ["moteur.html"],
        "pedagogy": {
            "moteur.html": "Dimensionne un moteur de circulateur de chauffage : vitesse synchrone, glissement, rendement. Lien direct avec les fiches techniques fabricant.",
        },
    },
    "physique-chimie/terminale-iccer/ch04": {
        "sims": ["rayonnement.html", "serre.html"],
        "pedagogy": {
            "rayonnement.html": "Applique la loi de Wien à un panneau radiant infrarouge : à quelle température fonctionne-t-il pour rayonner dans l'infrarouge moyen (longueur d'onde optimale pour chauffer un humain) ?",
            "serre.html": "Comprends pourquoi un bâtiment vitré au sud chauffe sans chauffage en journée, et pourquoi cet effet est désirable en hiver mais problématique en été.",
        },
    },
    "physique-chimie/terminale-iccer/ch05": {
        "sims": ["pression.html"],
        "pedagogy": {
            "pression.html": "Calcule la pression statique en bas d'une colonne d'eau (réseau ECS d'un bâtiment de plusieurs étages). Dimensionne le surpresseur si nécessaire.",
        },
    },
    "physique-chimie/terminale-iccer/ch06": {
        "sims": ["debit.html", "debit-fluide.html"],
        "pedagogy": {
            "debit.html": "Calcule le débit nécessaire pour un radiateur ou un plancher chauffant. Compétence pro essentielle pour le dimensionnement d'un réseau.",
            "debit-fluide.html": "Applique la conservation du débit dans un réseau qui se ramifie (canalisation principale → dérivations). Vérifie que la vitesse reste dans les normes (0,5 à 1,5 m/s).",
        },
    },
    "physique-chimie/terminale-iccer/ch07": {
        "sims": ["oxydoreduction.html", "pile-electrochimique.html"],
        "pedagogy": {
            "oxydoreduction.html": "Comprends pourquoi les canalisations rouillent en présence d'oxygène et d'eau, et comment la corrosion attaque le métal. Identifie l'oxydant et le réducteur.",
            "pile-electrochimique.html": "Étudie le couplage galvanique entre deux métaux différents (cuivre / acier en plomberie) et comprends la nécessité d'un anode sacrificielle ou d'un raccord diélectrique.",
        },
    },
    "physique-chimie/terminale-iccer/ch08": {
        "sims": ["son.html", "attenuation-sonore.html"],
        "pedagogy": {
            "son.html": "Mesure le niveau sonore d'une chaudière ou d'une pompe à chaleur. Vérifie le respect des nuisances sonores en limite de propriété (réglementation).",
            "attenuation-sonore.html": "Choisis l'épaisseur d'un isolant phonique pour réduire le bruit d'un local technique. Applique la loi de masse pour quantifier l'atténuation.",
        },
    },

    # ─── PC TERMINALE ERA ────────────────────────────────────────────────────
    "physique-chimie/terminale-era/ch01": {
        "sims": ["transformateur.html", "puissance.html"],
        "pedagogy": {
            "transformateur.html": "Comprends pourquoi le réseau atelier est souvent en triphasé 400 V et comment fonctionne le transformateur de poste qui ramène à 230 V monophasé.",
            "puissance.html": "Calcule la puissance d'une machine d'atelier en triphasé (P = √3 × U × I × cos φ).",
        },
    },
    "physique-chimie/terminale-era/ch02": {
        "sims": ["pile-electrochimique.html"],
        "pedagogy": {
            "pile-electrochimique.html": "Comprends le fonctionnement d'une batterie d'outillage (visseuse, perceuse) : pourquoi elle se décharge, pourquoi sa capacité diminue avec le temps.",
        },
    },
    "physique-chimie/terminale-era/ch03": {
        "sims": ["rayonnement.html", "serre.html"],
        "pedagogy": {
            "rayonnement.html": "Applique le rayonnement à la finition du bois : lampes UV pour durcir un vernis (longueur d'onde courte), infrarouge pour sécher (longueur d'onde longue).",
            "serre.html": "En agencement, comprends pourquoi une véranda chauffe excessivement en été (nécessite ombrage ou vitrage spécial) et reste agréable en hiver.",
        },
    },
    "physique-chimie/terminale-era/ch04": {
        "sims": ["vitesse-acceleration.html"],
        "pedagogy": {
            "vitesse-acceleration.html": "Étudie la cinématique de la lame d'une scie circulaire ou la course d'une tête de fraiseuse. Vitesse de coupe et accélération impactent la qualité de l'usinage.",
        },
    },
    "physique-chimie/terminale-era/ch05": {
        "sims": ["oxydoreduction.html"],
        "pedagogy": {
            "oxydoreduction.html": "Étudie la corrosion de la quincaillerie d'un agencement (charnières, vis) en milieu humide (cuisine, salle de bain). Choisis le métal et la finition adaptés (zingué, inox).",
        },
    },
    "physique-chimie/terminale-era/ch06": {
        "sims": ["sources-lumineuses.html"],
        "pedagogy": {
            "sources-lumineuses.html": "Compare LED, halogène et fluorescent pour l'éclairage d'un magasin ou d'un atelier. Critères : indice de rendu des couleurs, température de couleur, consommation.",
        },
    },
    "physique-chimie/terminale-era/ch07": {
        "sims": ["transmission-info.html"],
        "pedagogy": {
            "transmission-info.html": "Comprends comment fonctionne un capteur sans fil dans un atelier connecté : signal modulé, transmis radio, démodulé et exploité par l'automate.",
        },
    },
    "physique-chimie/terminale-era/ch08": {
        "sims": ["son.html", "attenuation-sonore.html"],
        "pedagogy": {
            "son.html": "Mesure le niveau sonore d'une scie, d'une ponceuse, d'un compresseur. Identifie les machines nécessitant une protection auditive (≥ 85 dB).",
            "attenuation-sonore.html": "Conçois un caisson d'insonorisation autour d'une machine bruyante. Choisis matériaux, épaisseur et forme pour atteindre l'atténuation souhaitée.",
        },
    },
}
