# Programme de mathematiques -- BTS

**Source :** Arrete du 4 juin 2013 (NOR : ESRS1312230A), paru au BO du 4 juillet 2013.
**Applicable :** rentree scolaire 2013 (premiere session 2015).

---

## Organisation generale

### Objectifs generaux

L'enseignement des mathematiques en BTS doit :

1. **Fournir les outils** necessaires pour suivre les autres enseignements utilisant des savoir-faire mathematiques.
2. **Contribuer a la formation scientifique** : mathematisation d'un probleme (modelisation), mise en oeuvre d'outils theoriques, analyse de la pertinence des resultats.
3. **Developper les capacites personnelles et relationnelles** : methodes de travail, expression ecrite et orale, methodes de representation, autonomie, outils informatiques.

### Structure du programme

Pour chaque specialite de BTS, le programme est constitue de **plusieurs modules**, chacun comportant :
- Un **bandeau** precisant les objectifs essentiels du module.
- Un **tableau en trois colonnes** : Contenus | Capacites attendues | Commentaires.

### Conventions du programme

- **"Hors programme"** : la notion ne doit pas etre abordee.
- **"Admis"** : la demonstration du resultat n'est pas un objectif du programme.
- **"Tout exces de technicite est exclu"** : limiter le niveau d'approfondissement.
- Le symbole **&#8644;** signale des themes d'ouverture interdisciplinaire.

### Organisation des etudes

- L'horaire est fixe par le reglement du BTS considere.
- La resolution de probleme doit etre au coeur de l'activite mathematique.
- Le cours doit etre bref ; une part importante est consacree aux travaux diriges et pratiques.
- Accompagnement des bacheliers professionnels en debut d'annee.

### Place des outils logiciels

Pour l'ensemble des specialites, le travail s'effectue a l'aide de :
- calculatrice programmable a ecran graphique
- ordinateur muni d'un tableur
- logiciels de calcul formel
- logiciels de geometrie
- logiciels d'application (modelisation, simulation...)

### Articulation avec les epreuves

- Les etudiants doivent connaitre l'enonce et la portee des resultats du programme, mais la demonstration n'est pas exigible.
- Pour les rubriques "Exemples de", seule la mise en oeuvre des methodes explicites dans l'enonce est exigible.

### Liste des modules

**Modules d'analyse :**
- Suites numeriques
- Fonctions d'une variable reelle
- Fonctions d'une variable reelle et modelisation du signal
- Calcul integral
- Equations differentielles
- Series de Fourier
- Transformation de Laplace
- Transformation en z

**Modules de statistique et probabilites :**
- Statistique descriptive
- Probabilites 1
- Probabilites 2
- Statistique inferentielle
- Fiabilite
- Plans d'experience

**Modules d'algebre et geometrie :**
- Configurations geometriques
- Calcul vectoriel
- Representations de l'espace
- Modelisation geometrique
- Nombres complexes
- Calcul matriciel
- Arithmetique
- Algebres de Boole
- Elements de la theorie des ensembles
- Graphes et ordonnancement
- Algorithmique appliquee

---

## Modules d'analyse

---

### Module : Suites numeriques

Les suites sont un outil indispensable pour l'etude des phenomenes discrets. Aucune difficulte theorique ne doit etre soulevee. Le programme se place dans le cadre des suites definies pour tout entier naturel non nul.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Mode de generation d'une suite et comportement global** | | |
| Exemples de generation d'une suite. | Calculer une liste de termes ou un terme de rang donne a l'aide d'un logiciel, d'une calculatrice ou d'un algorithme. | On privilegie les situations issues de la vie economique et sociale ou de la technologie pouvant etre modelisees a l'aide de suites. |
| Suites croissantes, suites decroissantes. | Realiser et exploiter, a l'aide d'une calculatrice ou d'un logiciel, une representation graphique des termes d'une suite. | On se limite a une approche graphique. |
| **Suites arithmetiques et geometriques** | | |
| Expression du terme general. | Ecrire le terme general d'une suite arithmetique ou geometrique definie par son premier terme et sa raison. | |
| | Calculer avec la calculatrice ou le tableur la somme de *n* termes consecutifs (ou des *n* premiers termes) d'une suite arithmetique ou geometrique. | Une expression de la somme de *n* termes consecutifs d'une suite arithmetique ou geometrique est donnee si necessaire. |
| **Limite d'une suite** | | |
| Limite d'une suite geometrique | Etant donne une suite geometrique (u_n), utiliser un tableur ou un algorithme pour determiner, lorsque cela est possible : un seuil a partir duquel u_n >= a ; un seuil a partir duquel |u_n| <= 10^(-p). | On approche experimentalement la notion de limite en utilisant les outils logiciels et en programmant des algorithmes. Selon les besoins, on peut resoudre un probleme de comparaison d'evolutions et de seuils pour des situations ne relevant pas d'une modelisation par une suite geometrique. |

---

### Module : Fonctions d'une variable reelle

On se place dans le cadre des fonctions a valeurs reelles, definies sur un intervalle ou une reunion d'intervalles de R. Le but est double : consolider les acquis sur les fonctions et apporter des complements utiles pour aborder de nouveaux concepts.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Fonctions de reference** | | |
| Fonctions affines. Fonctions polynomes de degre 2. Fonctions logarithme neperien et exponentielle de base e. Fonction racine carree. Fonctions sinus et cosinus. | Representer une fonction de reference et exploiter cette courbe pour retrouver des proprietes de la fonction. | En fonction des besoins, on met l'accent sur les fonctions de reference les plus utiles. En cas de besoin lie a la specialite, on peut etudier : la fonction logarithme decimal ; des fonctions puissances t -> t^alpha avec alpha dans R ou exponentielles de base a avec a dans ]0, +inf[. |
| **Derivation** | | |
| Derivee des fonctions de reference. Derivee d'une somme, d'un produit et d'un quotient. Derivee de fonctions de la forme x -> u^n(x) avec n entier naturel non nul, x -> ln(u(x)) et x -> e^(u(x)). | Calculer la derivee d'une fonction : a la main dans les cas simples ; a l'aide d'un logiciel de calcul formel dans tous les cas. Etudier les variations d'une fonction simple. | Il s'agit de completer et d'approfondir les connaissances anterieures sur la derivation. En particulier, il est important de rappeler et de travailler l'interpretation graphique du nombre derive. |
| | Exploiter le tableau de variation d'une fonction f pour obtenir : un eventuel extremum de f ; le signe de f ; le nombre de solutions d'une equation du type f(x) = k. | Les solutions d'une equation du type f(x) = k sont determinees : explicitement dans les cas simples ; de facon approchee sinon. |
| | Mettre en oeuvre un procede de recherche d'une valeur approchee d'une racine. | On etudie sur des exemples des methodes classiques : balayage, dichotomie, methode de Newton par exemple. C'est l'occasion de developper au moins un algorithme et d'utiliser des logiciels. |
| **Limites de fonctions** | | |
| Asymptotes paralleles aux axes : limite finie d'une fonction a l'infini ; limite infinie d'une fonction en un point. | Interpreter une representation graphique en termes de limite. Interpreter graphiquement une limite en termes d'asymptote. | La diversite des programmes du lycee doit inciter a veiller aux connaissances sur les limites acquises anterieurement ou non par les etudiants. |
| Limite infinie d'une fonction a l'infini. Cas d'une asymptote oblique. | | Toute etude de branche infinie, notamment la mise en evidence d'asymptote, doit comporter des indications sur la methode a suivre. |
| Limites et operations. | Determiner la limite d'une fonction simple. Determiner des limites pour des fonctions de la forme : x -> u^n(x), n entier naturel non nul ; x -> ln(u(x)) ; x -> e^(u(x)). | On se limite aux fonctions deduites des fonctions de reference par addition, multiplication ou passage a l'inverse et on evite tout exces de technicite. |
| **Approximation locale d'une fonction** | | |
| Developpement limite en 0 d'une fonction. | Determiner, a l'aide d'un logiciel, un developpement limite en 0 et a un ordre donne d'une fonction. | On introduit graphiquement la notion de developpement limite en 0 d'une fonction f en s'appuyant sur l'exemple de la fonction exponentielle sans soulever de difficulte theorique. |
| Developpement limite en 0 et tangente a la courbe representative d'une fonction. | Exploiter un developpement limite pour donner l'equation reduite de la tangente et preciser sa position par rapport a la courbe representative de la fonction. | L'utilisation et l'interpretation des developpements limites trouves doivent etre privilegiees. |
| **Courbes parametrees** | | |
| Exemples de courbes parametrees definies par des fonctions polynomiales. | Determiner un vecteur directeur de la tangente en un point ou le vecteur derive n'est pas nul. Tracer une courbe a partir des variations conjointes. | L'etude a pour objectif de familiariser les etudiants avec le role du parametre, la notion de courbe parametree et de variations conjointes. On se limite a quelques exemples ou les fonctions polynomes sont de degre inferieur ou egal a deux. Ouverture interdisciplinaire : trajectoire d'un solide, design. |

---

### Module : Fonctions d'une variable reelle et modelisation du signal

Ce module vient en complement du module "fonctions d'une variable reelle" dont les objectifs restent valables. Il est a traiter en relation etroite avec les situations rencontrees dans les enseignements technologiques.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Fonctions de reference** | | |
| Fonctions tangente et arctangente. | Representer une fonction de reference. | |
| **Complements sur les fonctions** | | |
| Fonction paire, fonction impaire, fonction periodique : definition ; interpretation graphique. | Exploiter la representation graphique d'une fonction pour en determiner des proprietes de periodicite et parite. Representer graphiquement une fonction simple ayant des proprietes de parite ou de periodicite. | Le champ des fonctions etudiees se limite aux fonctions de la forme x -> f(ax+b) et aux fonctions qui se deduisent de facon simple des fonctions de reference par operations algebriques. On privilegie des exemples de fonctions issues de problematiques abordees dans les autres disciplines. |
| Calculs de derivees : derivee de x -> tan x et x -> arctan x ; derivee de t -> cos(omega*t + phi) et t -> sin(omega*t + phi), omega et phi etant reels ; derivee d'une fonction de la forme x -> arctan(u(x)). | Etudier les variations d'une fonction simple. | On etudie les limites d'une fonction de la forme x -> arctan(u(x)) sur des exemples. |
| Fonctions rationnelles : decomposition en elements simples. | Determiner la decomposition en elements simples d'une fonction rationnelle : a la main dans les cas simples ; a l'aide d'un logiciel de calcul formel dans tous les cas. | Aucun resultat theorique sur la decomposition en elements simples n'est au programme : la forme de la decomposition doit etre indiquee. On prepare ainsi la recherche d'originaux dans le cadre de la transformation de Laplace. |
| **Approximation globale d'une fonction sur un intervalle** | | |
| Approche de la notion a partir d'exemples. | | Sur des exemples varies et a l'aide d'outils informatiques, on aborde experimentalement la notion d'approximation globale d'une fonction. On prepare ainsi la notion de developpement en serie d'une fonction. Avec la fonction exponentielle, on illustre la diversite des approximations possibles d'une meme fonction. |

---

### Module : Calcul integral

Le programme se place dans le cadre de fonctions a valeurs reelles definies sur un intervalle ou une reunion d'intervalles de R. L'accent est mis sur la diversite des approches numerique, graphique et algorithmique.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Primitives** | | |
| Primitives de fonctions de reference, operations algebriques. | Determiner des primitives d'une fonction : a la main dans les cas simples ; a l'aide d'un logiciel de calcul formel dans tous les cas. | |
| | Determiner les primitives d'une fonction de la forme u'u^n (n entier relatif, different de -1), u'/u et u'e^u. | Pour les primitives de u'/u, on se limite au cas ou u est strictement positive. |
| Complement : primitives de t -> cos(omega*t + phi) et t -> sin(omega*t + phi), omega et phi etant reels. | | |
| **Integration** | | |
| Calcul integral : integrale de a a b de f(x) dx = F(b) - F(a) ou F est une primitive de f. | Determiner une integrale : a la main dans les cas simples ; a l'aide d'un logiciel de calcul formel dans tous les cas. | |
| Proprietes de l'integrale : relation de Chasles, linearite et positivite. | | |
| Calcul d'aires. | Determiner l'aire du domaine defini par {M(x, y), a <= x <= b et f(x) <= y <= g(x)} ou f et g sont deux fonctions telles que pour tout reel x de [a, b], f(x) <= g(x). | On etudie le cas ou f (resp. g) est la fonction nulle. On familiarise les etudiants avec quelques exemples d'algorithmes lies a des methodes elementaires d'approximation d'une integrale (point-milieu, trapezes, Monte-Carlo). |
| Valeur moyenne d'une fonction sur un intervalle : definition, interpretation geometrique. | Determiner et interpreter la valeur moyenne d'une fonction sur un intervalle. | Illustree par des exemples issus des disciplines professionnelles. Ouverture interdisciplinaire : valeur moyenne, valeur efficace dans un transfert energetique ; centre d'inertie, moment d'inertie. |
| Formule d'integration par parties. | Calculer une integrale par integration par parties. | |

---

### Module : Equations differentielles

On s'attache a relier les exemples etudies avec les enseignements scientifiques et technologiques. L'utilisation des outils logiciels est sollicitee. On developpe plus particulierement deux types d'equations differentielles (premier et second ordre). On introduit les nombres complexes et les equations du second degre a coefficients reels pour disposer de l'equation caracteristique.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Equations lineaires du premier ordre** | | En lien avec les autres disciplines, on habitue les etudiants a differentes ecritures : variable, fonction, notation differentielle. |
| Equation differentielle ay'+by = c(t) ou a, b sont des constantes reelles et c une fonction continue a valeurs reelles. | Representer a l'aide d'un logiciel la famille des courbes representatives des solutions d'une equation differentielle. Resoudre une equation differentielle du premier ordre : a la main dans les cas simples ; a l'aide d'un logiciel de calcul formel dans tous les cas. Determiner la solution verifiant une condition initiale donnee : a la main dans les cas simples ; a l'aide d'un logiciel de calcul formel dans tous les cas. | On presente sur un exemple la resolution approchee d'une equation differentielle par la methode d'Euler. Les indications permettant d'obtenir une solution particuliere sont donnees. En liaison avec les autres disciplines, on peut etudier des exemples simples d'equations differentielles non lineaires, du premier ordre a variables separables (mecanique, cinetique chimique), mais ce n'est pas un attendu du programme. Ouverture interdisciplinaire : loi de refroidissement, cinetique chimique. |
| **Nombres complexes** | | |
| Forme algebrique d'un nombre complexe : somme, produit, conjugue. | | On se limite a l'ecriture algebrique des nombres complexes. |
| Equation du second degre a coefficients reels. | Resoudre une equation du second degre a coefficients reels. | |
| **Equations lineaires du second ordre a coefficients reels constants** | | |
| Equation differentielle ay''+by'+cy = d(t) ou a, b et c sont des constantes reelles et d une fonction continue a valeurs reelles. | Representer a l'aide d'un logiciel la famille des courbes representatives des solutions. Resoudre une equation differentielle du second ordre : a la main dans les cas simples ; a l'aide d'un logiciel de calcul formel dans tous les cas. Determiner la solution verifiant des conditions initiales donnees : a la main dans les cas simples ; a l'aide d'un logiciel de calcul formel dans tous les cas. | La fonction d est une fonction polynome ou du type : t -> e^(alpha*t) ; t -> cos(omega*t + phi) ; t -> sin(omega*t + phi). Les indications permettant d'obtenir une solution particuliere sont donnees. Ouverture interdisciplinaire : resistance des materiaux, circuit electronique. |

---

### Module : Series de Fourier

Le but est d'etudier et exploiter la decomposition de signaux periodiques en series de Fourier. Ce module est en liaison etroite avec les autres disciplines : les series de Fourier sont un outil indispensable pour l'etude des phenomenes vibratoires en electricite, en optique et en mecanique.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Exemples de series numeriques** | | |
| Series geometriques : convergence, somme. | Reconnaitre une serie geometrique et connaitre la condition de convergence. | L'etude de ces deux exemples a pour objectifs : familiariser les etudiants avec les "sommes infinies" et la notation Sigma ; introduire la notion de convergence et de somme d'une serie numerique. Toute theorie generale sur les series numeriques est exclue. |
| Series de Riemann : convergence. | Connaitre la condition de convergence d'une serie de Riemann. | L'outil informatique est utilise pour conjecturer les resultats concernant les series de Riemann. Ces resultats sont admis. |
| **Series de Fourier** | | |
| Serie de Fourier associee a une fonction T-periodique continue par morceaux sur R : a_0 + Sigma(n>=1) [a_n cos(n*omega*t) + b_n sin(n*omega*t)]. | Representer graphiquement une fonction T-periodique continue par morceaux sur R. | En liaison avec les autres disciplines, on met en valeur le lien entre la notion de serie de Fourier et l'etude des signaux : composantes d'un signal dans une frequence donnee, reconstitution du signal a partir de ses composantes, spectre. |
| Cas d'une fonction paire, impaire. | Exploiter la representation graphique d'une fonction T-periodique affine par morceaux pour en determiner : la periodicite ; la parite ; une expression sur une periode ou une demi-periode. | On montre l'interet d'exploiter, dans le calcul integral, les proprietes des fonctions periodiques, des fonctions paires et des fonctions impaires. |
| Convergence d'une serie de Fourier lorsque f est de classe C^1 par morceaux sur R (conditions de Dirichlet). | Representer a l'aide d'un logiciel une somme partielle d'une serie de Fourier et la comparer a la fonction associee au signal etudie. Savoir identifier parmi plusieurs developpements proposes celui correspondant a une fonction donnee. | L'utilisation de l'outil informatique permet de visualiser graphiquement la convergence de la serie de Fourier. Aucune difficulte ne doit etre soulevee sur la convergence des series de Fourier. Dans les cas etudies, les conditions de convergence sont toujours remplies. |
| | Calculer les coefficients de Fourier d'une fonction : a la main dans le cas d'un signal en creneau ; a l'aide d'un logiciel de calcul formel dans tous les cas. | En complement, on traite a la main un exemple de calculs de coefficients de Fourier d'une fonction associee a un signal rampe pour faire comprendre les resultats fournis par les logiciels dans d'autres disciplines. C'est l'occasion de reinvestir les techniques de calcul integral. |
| Formule de Parseval | Calculer et comparer : la valeur exacte de (1/T) integrale de 0 a T de f^2(t) dt ; une valeur approchee de (1/T) integrale de 0 a T de f^2(t) dt a l'aide des coefficients de Fourier de f. | On met en relation la formule de Parseval et le calcul de la valeur efficace d'un signal. Ouverture interdisciplinaire : analyse harmonique d'un signal. |

---

### Module : Transformation de Laplace

On etudie et exploite la transformation de Laplace en vue de determiner les solutions causales d'une equation differentielle lineaire. En liaison etroite avec les autres disciplines ou la transformation de Laplace permet d'obtenir la reponse d'un systeme lineaire usuel a un signal d'entree donne.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Transformation de Laplace** | | |
| Transformee de Laplace d'une fonction causale f. | | La theorie generale des integrales impropres est hors programme. |
| Transformee de Laplace des fonctions causales usuelles. | | On se limite aux fonctions usuelles suivantes : t -> U(t) ; t -> t^n U(t) ; t -> e^(at) U(t) ; t -> sin(omega*t)U(t) et t -> cos(omega*t)U(t) avec U la fonction unite, n un entier naturel, a et omega deux reels. |
| Proprietes de la transformation de Laplace : linearite ; effet d'une translation ou d'un changement d'echelle sur la variable ; effet de la multiplication par e^(-at). | Representer graphiquement une fonction causale donnee par une expression. Determiner une expression d'une fonction causale dont la representation graphique est de type "creneau" ou "rampe". Determiner la transformee de Laplace d'une fonction causale simple, dont les fonctions de type "creneau" et "rampe". Determiner la fonction causale (original) dont la transformee de Laplace est donnee. | On se limite au cas ou les fonctions donnees ou recherchees sont : soit des combinaisons lineaires a coefficients reels de fonctions de la forme t -> U(t-alpha) et t -> tU(t-alpha) ; soit de la forme t -> U(t-alpha)e^(rt) ; ou alpha est un nombre reel positif et r un reel. Dans les autres cas, le calcul est facilite par l'utilisation d'un logiciel. |
| Theoreme de la valeur initiale et theoreme de la valeur finale. | | L'exploitation de situations issues des autres disciplines permet d'illustrer la pertinence de ce theoreme. |
| Transformee de Laplace d'une derivee. | Exploiter la transformation de Laplace pour resoudre une equation differentielle lineaire d'ordre 1 ou 2 a coefficients constants. | Pour le second membre, on se limite au cas ou les fonctions donnees ou recherchees sont : soit des combinaisons lineaires a coefficients reels de fonctions de la forme t -> U(t-alpha) et t -> tU(t-alpha) ; soit de la forme t -> U(t-alpha)e^(rt) ; ou alpha est un nombre reel positif et r un reel. Ouverture interdisciplinaire : fonction de transfert d'un systeme lineaire, application a la stabilite. |
| Transformee de Laplace d'une primitive. | | En liaison avec les enseignements d'autres disciplines, on etudie un exemple d'equation differentielle de la forme a y'(t) + b y(t) + c integrale de 0 a t de y(s) ds = f(t) ou a, b, c sont des constantes reelles et f une fonction causale. |

---

### Module : Transformation en z

On se propose de familiariser les etudiants aux phenomenes discrets par la presentation de quelques signaux discrets et de leur transformation en z, en se limitant a des signaux causaux. L'etude de la reponse a des signaux discrets, de filtres numeriques regis par une equation aux differences lineaires a coefficients constants est completee par le passage du discret au continu et inversement.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Transformation en z** | | |
| Notion de serie entiere d'une variable reelle. Developpement en serie entiere des fonctions t -> e^t et t -> 1/(1-t). | | L'etude de ces deux exemples a pour objectifs : familiariser les etudiants avec les "sommes infinies" de fonctions et la notation Sigma ; introduire la notion de rayon de convergence et de somme d'une serie entiere. Toute theorie generale sur les series entieres est exclue. L'introduction des series entieres a pour seul but la presentation des resultats utiles a l'etude de la transformation en z. |
| Transformee en z d'un signal causal. | | |
| Transformee en z des signaux causaux usuels. | | On se limite aux signaux usuels suivants : n -> 1 ; n -> d(n) ou d(0) = 1 et d(n) = 0 sinon ; n -> n ; n -> n^2 ; n -> a^n avec a reel non nul. |
| Proprietes de la transformation en z : linearite ; effet de la multiplication par a^n avec a reel non nul ; effet d'une translation sur la variable. | Determiner la transformee en z d'un signal causal a partir des signaux causaux usuels. | On evite tout exces de technicite dans les calculs. Dans le cadre de la resolution de problemes, le calcul est facilite par l'utilisation d'un logiciel de calcul formel. |
| | Determiner le signal causal (original) dont la transformee en z est donnee. | Dans la recherche de l'original, pour obtenir la decomposition en elements simples, on donne des indications sur la methode a utiliser ou si necessaire, on utilise un logiciel de calcul formel. |
| Equations recurrentes. | Exploiter la transformation en z pour la resolution d'equations recurrentes. | On resout des equations de la forme : ay(n) + by(n-1) + cy(n-2) = alpha*x(n) + beta*x(n-1) ou ay(n+2) + by(n+1) + cy(n) = alpha*x(n+1) + beta*x(n) ou a, b, c, alpha, beta sont des nombres reels, x un signal causal discret connu et y un signal causal discret inconnu. En liaison avec les enseignements d'autres disciplines, on montre sur un exemple simple comment une de ces equations s'interprete en termes de "derivation discrete" ou d'"integration discrete". Ouverture interdisciplinaire : traitement numerique obtenu par echantillonnage d'un signal analogique. |

---

## Modules de statistique et probabilites

---

### Module : Statistique descriptive

Il s'agit de consolider et d'approfondir les connaissances acquises les annees anterieures. On s'attache d'une part a etudier des situations issues de la technologie, d'autre part a relier cet enseignement a celui de l'economie et de la gestion. L'utilisation de logiciels, notamment d'un tableur, et des calculatrices est necessaire.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Serie statistique a une variable** | | |
| | Utiliser un logiciel ou une calculatrice pour resumer et representer des series statistiques a une variable. Interpreter les resultats obtenus pour une serie statistique ou pour comparer deux series statistiques. Choisir des resumes numeriques ou graphiques adaptes a une problematique. | Il s'agit de reactiver les connaissances deja traitees au lycee : methodes de representation ; caracteristiques de position (mediane, moyenne) ; caracteristiques de dispersion (etendue, ecart interquartile, ecart type). Aucun cours specifique n'est donc attendu. L'utilisation des outils logiciels permet de faire reflechir les etudiants a la pertinence de regroupements par classes lors du traitement statistique. |
| **Serie statistique a deux variables** | | |
| Nuage de points ; point moyen. Ajustement affine par la methode des moindres carres. | Utiliser un logiciel ou une calculatrice pour representer une serie statistique a deux variables et en determiner un ajustement affine selon la methode des moindres carres. | Pour l'ajustement affine, on distingue liaison entre deux variables statistiques et relation de cause a effet. Pour la methode des moindres carres, on observe, a l'aide d'un logiciel, le caractere minimal de la somme des carres des ecarts. On fait observer la dissymetrie entre les deux variables statistiques qui conduit, suivant l'utilisation de l'ajustement, a privilegier l'une des deux droites. |
| | Realiser un ajustement se ramenant, par un changement de variable simple donne, a un ajustement affine. | |
| | Utiliser un ajustement pour interpoler ou extrapoler. | |
| Coefficient de correlation lineaire. | | On utilise le coefficient de correlation lineaire, obtenu a l'aide d'un logiciel ou d'une calculatrice, pour comparer la qualite de deux ajustements. Ouverture interdisciplinaire : controle qualite, mesures physiques sur un systeme reel, droite de Henry, etude economique ou mercatique. |

---

### Module : Probabilites 1

On reinvestit et approfondit le travail sur les probabilites mene au lycee. L'objectif est que les etudiants sachent traiter quelques problemes simples mettant en oeuvre des probabilites conditionnelles ou des variables aleatoires dont la loi figure au programme. L'apprentissage doit largement faire appel a l'outil informatique.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Conditionnement et independance** | | |
| Conditionnement par un evenement de probabilite non nulle. Notation P_A(B). | Construire un arbre et/ou un tableau des probabilites en lien avec une situation donnee. Exploiter l'arbre et/ou le tableau des probabilites pour determiner des probabilites. Calculer la probabilite d'un evenement connaissant ses probabilites conditionnelles relatives a une partition de l'univers. | On represente une situation a l'aide d'un arbre pondere ou d'un tableau de probabilites. Un arbre de probabilites correctement construit constitue une preuve. La formule des probabilites totales n'est pas un attendu mais sa mise en oeuvre doit etre maitrisee. |
| Independance de deux evenements. | Utiliser ou justifier l'independance de deux evenements. | Ouverture interdisciplinaire : controle qualite, fausses alertes, tests biologiques. |
| **Exemple de loi discrete** | | |
| Variable aleatoire associee au nombre de succes dans un schema de Bernoulli. Loi binomiale. | Simuler un schema de Bernoulli. Reconnaitre et justifier qu'une situation releve de la loi binomiale. Representer graphiquement la loi binomiale a l'aide d'un logiciel. Calculer une probabilite dans le cadre de la loi binomiale a l'aide de la calculatrice ou d'un logiciel. | Aucun developpement theorique n'est attendu a propos de la notion de variable aleatoire. On utilise une calculatrice ou un logiciel pour calculer directement des probabilites et representer graphiquement la loi binomiale. La connaissance d'une expression explicite de la loi binomiale n'est pas attendue. |
| Esperance, variance et ecart type de la loi binomiale. | Interpreter l'esperance et l'ecart type d'une loi binomiale dans le cadre d'un grand nombre de repetitions. | Les formules donnant l'esperance et l'ecart type de la loi binomiale sont admises. On conforte experimentalement ces formules a l'aide de simulations de la loi binomiale. |
| **Exemples de lois a densite** | | Toute theorie generale des lois a densite est exclue. Pour les lois etudiees, on represente et on exploite la fonction de densite et la fonction de repartition. |
| Loi uniforme sur [a, b]. | Concevoir et exploiter une simulation dans le cadre d'une loi uniforme. | La definition de l'esperance et de la variance constituent un prolongement dans le cadre continu de celles d'une variable aleatoire discrete. |
| Esperance, variance et ecart type de la loi uniforme. | Interpreter l'esperance et l'ecart type d'une loi uniforme dans le cadre d'un grand nombre de repetitions. | |
| Loi normale d'esperance mu et d'ecart type sigma. | Utiliser une calculatrice ou un tableur pour calculer une probabilite dans le cadre de la loi normale. Connaitre et interpreter graphiquement une valeur approchee de la probabilite des evenements suivants : {X dans [mu-sigma, mu+sigma]}, {X dans [mu-2sigma, mu+2sigma]} et {X dans [mu-3sigma, mu+3sigma]}, lorsque X suit la loi normale d'esperance mu et d'ecart type sigma. | Toute theorie sur les integrales impropres est exclue. La loi normale est introduite a partir de l'observation, a l'aide d'un logiciel, du cumul des valeurs obtenues lors de la repetition a l'identique d'une experience aleatoire dont le resultat suit une loi uniforme. L'utilisation d'une table de la loi normale centree reduite n'est pas une necessite. On s'appuie sur des exemples issus des autres disciplines. On peut simuler la loi normale a partir de la loi uniforme sur [0, 1]. Ouverture interdisciplinaire : maitrise statistique des processus. |
| Approximation d'une loi binomiale par une loi normale. | Determiner les parametres de la loi normale approximant une loi binomiale donnee. | Toute theorie est exclue. On illustre cette approximation a l'aide de l'outil informatique. Les conditions d'approximation d'une loi binomiale par une loi normale ne sont pas exigibles. Il convient de mettre en evidence la raison d'etre de la correction de continuite lors de l'approximation d'une loi binomiale par une loi normale ; toutes les indications sont fournies. |
| Esperance et variance des lois de aX+b, X+Y, X-Y dans le cas ou X et Y sont des variables aleatoires independantes. | Savoir determiner les parametres des lois de aX+b, X+Y et X-Y dans le cas ou X et Y sont des variables aleatoires independantes. | Toute theorie concernant la notion de variables aleatoires independantes est exclue. Les resultats sont conjectures a l'aide de simulations, puis admis. |
| Theoreme de la limite centree. | Savoir determiner les parametres de la loi normale correspondant a une moyenne dans le cadre du theoreme de la limite centree. | Le theoreme, admis, s'enonce en termes d'approximation par une loi normale de la somme de n variables independantes de meme loi. L'outil informatique permet une approche experimentale. |

---

### Module : Probabilites 2

On approfondit la connaissance des lois de probabilites en etudiant la loi exponentielle et la loi de Poisson, dans le contexte de processus aleatoires a temps continu. Une initiation aux processus aleatoires discrets permet d'elargir le champ d'etude. L'apprentissage doit largement faire appel a l'outil informatique, notamment pour la simulation et la mise en oeuvre d'algorithmes.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Loi exponentielle** | | |
| | Exploiter une simulation dans le cadre de la loi exponentielle. Representer graphiquement la loi exponentielle. Calculer une probabilite dans le cadre de la loi exponentielle. | On peut simuler la loi exponentielle a partir de la loi uniforme sur [0, 1]. |
| Esperance, variance et ecart type de la loi exponentielle. | Interpreter l'esperance et l'ecart type d'une variable aleatoire suivant une loi exponentielle. | Ouverture interdisciplinaire : fiabilite, desintegration nucleaire. |
| **Loi de Poisson** | | |
| | Representer graphiquement la loi de Poisson. Calculer une probabilite dans le cadre de la loi de Poisson a l'aide de la calculatrice ou d'un logiciel. | La loi de Poisson est introduite comme correspondant au nombre de realisations observees, durant un intervalle de temps de longueur donnee, lorsque le temps d'attente entre deux realisations est fourni par une loi exponentielle. La connaissance d'une expression explicite de la loi de Poisson n'est pas attendue. |
| Esperance, variance et ecart type de la loi de Poisson. | Interpreter l'esperance et l'ecart type dans le cadre d'un grand nombre de repetitions. | |
| Approximation d'une loi binomiale par une loi de Poisson. | Determiner le parametre de la loi de Poisson approximant une loi binomiale donnee. | Les conditions d'approximation d'une loi binomiale par une loi de Poisson ne sont pas exigibles. On illustre cette approximation a l'aide de l'outil informatique. Ouverture interdisciplinaire : fiabilite, gestion de stocks ou de reseaux. |
| **Exemples de processus aleatoires** | | |
| Graphe probabiliste a N sommets. Exemples de chaines de Markov. | Representer un processus aleatoire simple par un graphe probabiliste. Exploiter un graphe probabiliste pour calculer la probabilite d'un parcours donne. Simuler un processus aleatoire simple. Exploiter une simulation d'un processus aleatoire pour estimer une probabilite, une duree moyenne ou conjecturer un comportement asymptotique. | On etudie des marches aleatoires sur un graphe a quelques sommets. Ouverture interdisciplinaire : pertinence d'une page web, gestion d'un reseau, fiabilite, etude genetique de populations, diffusion d'une epidemie. |

---

### Module : Statistique inferentielle

La statistique inferentielle permet de developper les competences des etudiants sur les methodes et les raisonnements statistiques permettant d'induire, a partir de faits observes sur un echantillon, des proprietes de la population dont il est issu. On approfondit la prise de decision en formalisant la notion de test d'hypothese et en se centrant sur la notion de risques d'erreur.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Estimation ponctuelle** | | |
| Estimation ponctuelle d'un parametre. | Estimer ponctuellement une proportion, une moyenne ou un ecart type d'une population a l'aide de la calculatrice ou d'un logiciel, a partir d'un echantillon. | La simulation d'echantillons permet de sensibiliser au choix de l'estimation de l'ecart type de la population. |
| **Tests d'hypothese** | | |
| Tests bilateraux et unilateraux relatifs a : une proportion dans le cas d'une loi binomiale puis dans le cas d'une loi binomiale approximable par une loi normale ; une moyenne. | Determiner la region de rejet de l'hypothese nulle et enoncer la regle de decision. | On souligne le fait que la decision prise, rejet ou non, depend des choix faits a priori par l'utilisateur : choix de l'hypothese nulle, du type de test et du seuil de signification. Ces choix sont fournis a l'etudiant dans les cas delicats. |
| Tests bilateraux et unilateraux de comparaison de deux proportions ou de deux moyennes dans le cadre de la loi normale. | Utiliser les tests bilateraux et unilateraux relatifs a une proportion ou a une moyenne ainsi qu'a la comparaison de deux proportions ou de deux moyennes. | En liaison avec les enseignements des disciplines professionnelles ou les situations rencontrees en entreprise, on peut traiter quelques exemples d'autres procedures, par exemple test du khi deux ou test de Student. Ouverture interdisciplinaire : maitrise statistique des procedes. |
| Risques d'erreur de premiere et de seconde espece. | Analyser les risques d'erreur de premiere et de seconde espece associes a la prise de decision. | On compare, a l'aide d'un algorithme ou de simulations, les differents seuils de signification et on met en evidence les risques d'erreur de premiere et de seconde espece. La notion de puissance d'un test est abordee. |
| **Estimation par intervalle de confiance** | | |
| Intervalle de confiance d'une proportion et d'une moyenne. | Determiner un intervalle de confiance a un niveau de confiance souhaite pour : une proportion, dans le cas d'une loi binomiale approximable par une loi normale ; une moyenne, dans le cas d'une loi normale quand l'ecart type de la population est connu ou dans le cas de grands echantillons. | On distingue confiance et probabilite : avant le tirage d'un echantillon, la procedure d'obtention de l'intervalle de confiance a une probabilite de 0,95 ou de 0,99 que cet intervalle contienne le parametre inconnu ; apres le tirage, le parametre est dans l'intervalle calcule avec une confiance de 95% ou 99%. La simulation permet de mieux comprendre la notion d'intervalle de confiance. |
| | Exploiter un intervalle de confiance. Determiner la taille necessaire d'un echantillon pour estimer une proportion ou une moyenne avec une precision donnee. | Ouverture interdisciplinaire : incertitude de mesure. |

---

### Module : Fiabilite

Sous l'impulsion du mouvement de la qualite, les methodes statistiques sont aujourd'hui largement utilisees dans le domaine de la fiabilite. L'objectif essentiel est d'amener les etudiants a prendre du recul vis-a-vis des methodes utilisees. On evite les situations artificielles et on privilegie les exemples issus du domaine professionnel.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Vocabulaire de la fiabilite** | | |
| Variable aleatoire associee a la duree de vie. | Connaitre le vocabulaire de la fiabilite et en effectuer une traduction mathematique. | |
| Fonctions de fiabilite et de defaillance. | Representer des temps de bon fonctionnement a l'aide d'un logiciel. | |
| Taux d'avarie. | | |
| Moyenne des temps de bon fonctionnement (MTBF). | | La MTBF est definie comme l'esperance de la duree de vie. |
| **Loi exponentielle, loi de Weibull** | | |
| | A l'aide d'un logiciel, utiliser la regression lineaire pour ajuster une distribution observee a un modele exponentiel ou de Weibull et estimer les parametres de la loi correspondante. | Toutes les indications concernant le calcul des frequences empiriques (methode des rangs bruts, des rangs moyens, des rangs medians) sont fournies. On reinvestit les connaissances sur l'ajustement en se ramenant, selon un changement de variable indique, a un ajustement affine. Le probleme de l'adequation de donnees empiriques a un modele et des tests correspondants est hors programme. |
| | Calculer et interpreter des probabilites de panne et la MTBF dans le cas d'une loi exponentielle ou de Weibull. | Les coefficients permettant le calcul de la MTBF dans le cas de la loi de Weibull sont fournis. L'usage du papier semi-logarithmique ou du papier de Weibull n'est pas un attendu du programme. |
| | Calculer la periodicite d'une intervention fondee sur une fiabilite determinee. | |
| | Simuler une situation dans un contexte de fiabilite. | On fournit les formules permettant de simuler la loi exponentielle et la loi de Weibull. La simulation permet des previsions de rentabilite ou de maintenance au dela du simple calcul de la MTBF. |

---

### Module : Plans d'experience

La technique des plans d'experience est devenue d'usage courant dans la mise en place des procedes industriels. L'objectif est de montrer aux etudiants la necessite de planifier les experiences et de leur permettre d'apprehender la demarche mise en oeuvre afin d'obtenir une estimation optimale des parametres inconnus, quand les mesures faites ont un caractere aleatoire. On montre egalement l'importance du modele a priori.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Plan factoriel** | | |
| Actions principales, interactions, modele polynomial. | Mettre en oeuvre un plan d'experience complet a deux ou a trois facteurs, chacun a deux niveaux. | L'utilisation des methodes de l'algebre lineaire est hors programme. En liaison avec les enseignements des disciplines professionnelles, si le besoin apparait, on peut aborder la notion de plan fractionnaire. |
| Coefficients du modele. | Calculer l'effet d'un facteur. Representer graphiquement l'effet global d'un facteur. | On indique la methode de construction de la matrice d'experience selon l'ordre de l'algorithme de Yates : les coefficients du modele sont les effets des facteurs, l'interaction entre deux facteurs etant un nouveau facteur. On peut aborder la notion d'isoreponse et son trace a l'aide d'un logiciel informatique. |
| **Estimation des coefficients du modele par un intervalle de confiance** | | |
| | Determiner un intervalle de confiance de l'effet d'un facteur dans une situation relevant de la loi normale, l'ecart type des mesures etant connu. | Sur des exemples simples, on peut montrer quelles sont les conditions pour que l'ecart type puisse etre estime quand il est inconnu ; on peut alors etre amene a introduire la notion de degre de liberte et a utiliser la loi de Student. |
| **Test d'hypothese relatif a un coefficient du modele** | | |
| | Construire un test d'hypothese relatif a un effet dans une situation relevant de la loi normale, l'ecart type des mesures etant connu. | |

---

## Modules d'algebre et geometrie

---

### Module : Configurations geometriques

L'objectif est double : renforcer la vision dans l'espace en etudiant des objets constitues de solides connus ; mobiliser les acquis sur les configurations geometriques du plan en etudiant des figures planes extraites des objets precedents ; sensibiliser les etudiants a differents types de reperage.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Configurations du plan et de l'espace** | | |
| Exemples de problemes portant sur : l'analyse de la forme d'un objet de l'espace (par projection ou famille de sections planes) ; la section d'un solide par un plan ; la projection sur un plan ou sur une droite ; l'intersection, le parallelisme, l'orthogonalite ; les surfaces de revolution. | Lire et interpreter une representation d'un objet constitue de solides usuels. Representer, identifier et etudier la section d'un solide par un plan dans un cas simple. Isoler, representer et etudier une figure plane extraite d'un solide. Utiliser les acquis de geometrie pour : calculer la longueur d'un segment, la mesure d'un angle en degres, l'aire d'une surface et le volume d'un solide ; determiner les effets d'un agrandissement ou d'une reduction sur les longueurs, les aires et les volumes. | On etudie des problemes portant sur des objets issus des autres enseignements et constitues des solides usuels suivants : le cube, le parallelepipede rectangle, la pyramide, le cylindre, le cone et la sphere. On emploie un logiciel de visualisation et de construction afin de favoriser la vision dans l'espace des etudiants. Sur un exemple, on peut aborder la notion de plan tangent a une surface. On reactive les connaissances de geometrie plane en s'appuyant sur des figures planes extraites des objets de l'espace etudies. Sur un exemple, on peut decouvrir la relation d'Al-Kashi ou les relations liant les sinus des angles, les longueurs des cotes et l'aire d'un triangle. Ouverture interdisciplinaire : modelisation volumique. |
| **Reperage d'un point** | | |
| Exemples de problemes mettant en oeuvre le reperage d'un point : dans le plan (coordonnees cartesiennes, coordonnees polaires) ; dans l'espace (coordonnees cartesiennes, coordonnees cylindriques, coordonnees spheriques). | Utiliser un systeme de reperage d'un point dans le cadre de la resolution d'un probleme. | On s'appuie sur des exemples issus des autres disciplines pour justifier de la pertinence de l'emploi de systemes de reperage varies. Ouverture interdisciplinaire : cinematique. |

---

### Module : Calcul vectoriel

Le but est double : consolider les acquis de calcul vectoriel des annees precedentes ; apporter des complements utiles pour etudier des situations rencontrees dans les autres enseignements. On prend appui sur les enseignements scientifiques et technologiques.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Decomposition d'un vecteur dans une base du plan ou de l'espace** | | |
| | Decomposer un vecteur dans une base et exploiter une telle decomposition. | On ne se limite pas au cadre de la geometrie reperee. Ouverture interdisciplinaire : vecteur vitesse, force. |
| **Barycentre** | | |
| Barycentre de deux points ponderes du plan ou de l'espace. Coordonnees dans un repere. | Construire le barycentre de deux points ponderes. | On peut introduire la notion de barycentre en la reliant a l'equilibrage de masses ou a la moyenne ponderee. Selon les besoins, on etudie des reductions d'une somme de la forme alpha*MA + beta*MB avec alpha+beta different de 0. On fait remarquer que le barycentre de deux points distincts appartient a la droite definie par ces deux points. |
| Extension de la notion de barycentre a trois points ponderes. | Utiliser, sur des exemples simples lies aux enseignements technologiques, la notion de barycentre partiel. | Sur des exemples issus des enseignements technologiques, on met en place le theoreme du barycentre partiel. Ouverture interdisciplinaire : centre d'inertie d'un assemblage de solides. |
| **Produit scalaire** | | |
| Expressions du produit scalaire : a l'aide d'une projection orthogonale ; a l'aide des normes et d'un angle ; a l'aide des coordonnees. | Choisir l'expression du produit scalaire la plus adaptee en vue de la resolution d'un probleme. Calculer un angle ou une longueur a l'aide d'un produit scalaire. | On exploite des situations issues des domaines scientifiques et technologiques. On illustre en situation quelques proprietes du produit scalaire. Ouverture interdisciplinaire : travail, puissance d'une force. |
| **Produit vectoriel** | | |
| Orientation de l'espace. Produit vectoriel de deux vecteurs de l'espace : definition ; calcul des coordonnees dans une base orthonormale directe ; application a l'aire d'un triangle et d'un parallelogramme. | Calculer une aire a l'aide d'un produit vectoriel. | La decouverte du produit vectoriel, de ses proprietes et de ses applications est a mener en liaison etroite avec les autres enseignements. Les notions de vecteur glissant, de torseur et le produit mixte sont hors programme. Ouverture interdisciplinaire : moment d'une force. |

---

### Module : Representations de l'espace

L'objectif est de favoriser l'aisance de l'etudiant dans le travail de creation, d'analyse et de representation des objets de l'espace et des scenes. Ce module est en liaison etroite avec les enseignements technologiques.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Representation de l'espace en perspective** | | |
| Exemples de problemes portant sur les codes perspectifs (perspective parallele, perspective centrale) en lien avec : l'analyse de la forme d'un objet de l'espace ; la section d'un solide par un plan ; l'intersection, le parallelisme, l'orthogonalite ; les surfaces de revolution ; les coniques (vues comme section d'un demi-cone par un plan). | Lire et interpreter une representation en perspective d'un objet constitue de solides usuels. Representer un objet ou une scene dans un cas simple : en perspective parallele ; en perspective centrale. Representer en perspective ou en vraie grandeur, identifier et etudier la section d'un solide usuel par un plan dans un cas simple. Isoler, representer et etudier une figure plane extraite d'un solide. | On etudie des problemes portant : sur des objets issus des autres enseignements et constitues de solides usuels ; sur des scenes composees de quelques objets et d'espaces vides. Les solides usuels sont : les prismes droits, la pyramide, le cylindre, le cone et la sphere. On peut aborder, sur un exemple, des solides platoniciens. On s'appuie sur la manipulation de solides et sur l'emploi de logiciels de visualisation et de construction. On renforce et complete alors les connaissances sur la translation, la rotation, les symetries et l'homothetie dans l'espace. On reactive les connaissances de geometrie plane en s'appuyant sur des figures planes extraites des objets de l'espace etudies. |
| **Reperage et calcul vectoriel** | | |
| Coordonnees d'un point dans un repere orthonormal de l'espace. Coordonnees d'un vecteur. | Reperer un point donne de l'espace. | On fait le lien avec l'affichage des coordonnees dans les logiciels de conception volumique, ainsi qu'avec le choix d'une couleur dans un logiciel de dessin. |
| **Produit scalaire** | | |
| Produit scalaire de deux vecteurs de l'espace. | Calculer le produit scalaire de deux vecteurs selon deux methodes : analytiquement ; a l'aide des normes et d'un angle. | On exploite des situations issues des domaines technologiques et artistiques. |
| Applications du produit scalaire. | Calculer des angles ou des longueurs. | |
| Equation cartesienne d'un plan. Vecteur normal. | Determiner une equation cartesienne d'un plan defini a partir d'un point et d'un vecteur normal. | Ouverture interdisciplinaire : modes de representation, modelisation volumique, infographie. |

---

### Module : Modelisation geometrique

Parmi les modeles mathematiques qui sont la base de la conception des courbes ou des surfaces en C.A.O. et en C.F.A.O., le modele de Bezier et celui des B-Splines sont les plus utilises. L'etude de ces deux modeles, restreinte aux courbes du plan, est suffisante pour comprendre leur interet dans la conception interactive des formes.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Courbe de Bezier** | | |
| Modele par vecteurs et contraintes. | Determiner un vecteur tangent en un point d'une courbe de Bezier. Etudier et construire une courbe de Bezier definie par vecteurs et contraintes. | |
| Modele par points de controle et polynomes de Bernstein. | Definir, sous forme parametrique, une courbe de Bezier a partir des points de controle. Etudier et construire une courbe de Bezier definies par des points de controle. | Le lien entre approche par vecteurs et contraintes d'une part et par points de controle d'autre part est explicite sur un exemple. En liaison avec les autres disciplines, il convient d'utiliser les outils informatiques pour mettre en evidence le role des points de controle dans la modification de la forme de la courbe. La formule donnant les polynomes de Bernstein n'est pas exigible. On limite a quatre le nombre de points de controle. |
| Construction barycentrique d'un point de la courbe. Barycentre de deux points ponderes. | Construire un point de la courbe par barycentres successifs. | Le lien entre le modele par points de controle et le point de vue barycentrique est admis. Des algorithmes associes a la construction geometrique par barycentres successifs peuvent etre proposes. On se limite a des coefficients compris entre 0 et 1. Ouverture interdisciplinaire : conception de formes. |
| **Courbe B-Spline** | | |
| Points de controle et polynomes de Riesenfeld (degre 2 ou 3). | Determiner un polynome de Riesenfeld a partir de la formule donnee. Etudier et construire des courbes B-Splines. | La formule donnant les polynomes de Riesenfeld n'est pas exigible. On traite un exemple de forme realisee par jonction d'arcs de courbes ; on met en evidence le passage du modele de Bezier qui deforme globalement l'arc a une utilisation ou l'on peut modifier localement chaque arc. Ouverture interdisciplinaire : conception de formes. |

---

### Module : Nombres complexes

Les premiers elements de l'etude des nombres complexes sont mis en place dans les classes de lycee. Les objectifs sont de mettre en oeuvre et de completer ces acquis pour fournir des outils utilises en electricite, en mecanique et en automatique, et pour mettre en evidence les interpretations geometriques et les interventions des nombres complexes en analyse.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Forme algebrique et representation geometrique** | | |
| Nombres a + ib avec i^2 = -1. Egalite, conjugue, somme, produit, quotient. | Effectuer des calculs algebriques avec des nombres complexes, notamment a l'aide d'une calculatrice. | Il s'agit de reactiver les connaissances deja traitees au lycee. Dans les situations issues des enseignements technologiques, on emploie la notation a + jb. |
| Equations du second degre a coefficients reels. | Resoudre une equation du second degre a coefficients reels. | |
| Representation geometrique. | Representer un nombre complexe par un point ou un vecteur. | |
| Ensemble de points dont l'affixe a une partie reelle ou imaginaire donnee. | Determiner et construire un ensemble de points dont l'affixe a une partie reelle ou imaginaire donnee. | |
| **Forme trigonometrique, forme exponentielle** | | |
| Module d'un nombre complexe, arguments d'un nombre complexe non nul. | Passer de la forme trigonometrique a la forme algebrique et inversement. | Il est attendu qu'un etudiant sache effectuer un calcul simple a la main et a la calculatrice dans tous les cas. |
| Forme exponentielle et forme trigonometrique d'un nombre complexe. | Utiliser la forme la plus adaptee a la resolution d'un probleme. | |
| Ensemble de points dont l'affixe z verifie |z-a| = k ou arg(z-a) = k, ou a designe un nombre complexe et k un nombre reel. | Determiner et construire un ensemble de points dont l'affixe z verifie |z-a| = k ou arg(z-a) = k. | On favorise l'utilisation de logiciels de geometrie dynamique. |
| **Transformations** | | |
| Exemples de transformations geometriques d'ecritures complexes suivantes : z -> z+b, z -> az, z -> conjugue(z) et z -> 1/z, ou a et b sont des nombres reels. | Representer, a l'aide d'un logiciel de geometrie dynamique, l'image d'un point ou d'une partie de droite par une transformation geometrique d'ecriture complexe z -> az+b ou z -> (az+b)/(cz+d). | L'intention n'est pas de developper une dexterite sur ce sujet mais, a l'aide de la notion mathematique introduite, de donner du sens aux resultats obtenus par le logiciel. Ouverture interdisciplinaire : diagrammes de Nyquist ou Bode en electronique. |

---

### Module : Calcul matriciel

Ce module consiste en une initiation au langage matriciel, s'appuyant sur l'observation de phenomenes issus de la vie courante ou d'exemples concrets. On introduit le calcul matriciel sur des matrices d'ordre 2. Les calculs sur des matrices d'ordre 3 ou plus sont effectues a l'aide d'une calculatrice ou d'un logiciel.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Matrices** | | |
| Egalite de deux matrices. Matrice nulle, matrice identite. | | Une matrice est introduite comme un tableau de nombres reels permettant de representer une situation comportant plusieurs "entrees" et "sorties". |
| Calcul matriciel elementaire : addition ; multiplication par un nombre reel ; multiplication. | Effectuer des calculs matriciels a l'aide d'une calculatrice ou d'un logiciel, y compris le calcul d'une puissance d'une matrice. Representer puis traiter une situation simple a l'aide d'une ecriture matricielle. | Le choix de la definition de chaque operation portant sur les matrices s'appuie sur l'observation de la signification du tableau de nombres ainsi obtenu. On signale le caractere associatif mais non commutatif de la multiplication. On peut notamment etudier des exemples de processus discrets, deterministes ou stochastiques, a l'aide de suites de matrices. |
| **Inverse d'une matrice** | | |
| Definition, existence eventuelle, unicite en cas d'existence. | | |
| Commutativite d'une matrice inversible et de son inverse. | Montrer qu'une matrice est l'inverse d'une autre. | |
| | Determiner a l'aide d'une calculatrice ou d'un logiciel l'inverse d'une matrice inversible. | La notion de determinant n'est pas au programme. Aucune condition d'inversibilite d'une matrice n'est a connaitre. |
| | Resoudre un systeme lineaire de n equations a n inconnues a l'aide d'une inversion de matrice. | On ne considere que le cas ou le systeme est de Cramer, sans qu'aucune justification ne soit requise. Ouverture interdisciplinaire : gestion d'un reseau, matrice d'inertie et changement de base en mecanique, processus aleatoires. |

---

### Module : Arithmetique

Le programme concerne les notions les plus utiles a l'informatique. La numeration est indispensable aux langages de bas niveau. L'arithmetique modulaire est utile a la cryptographie, aux corrections d'erreurs et plus generalement a de nombreux algorithmes.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Systemes de numeration** | | |
| Numeration en bases 10, 2 et 16 des entiers et des reels. Conversions entre ces bases. | Passer de l'ecriture d'un nombre dans une base a une autre. | Les nombres negatifs sont precedes du signe moins (-), quelle que soit la base utilisee. On fait le lien entre le calcul binaire et le calcul booleen : les booleens sont alors 1 et 0, interpretes comme signifiant "il y a, ou pas". |
| Notions d'arrondi et de precision. | Arrondir un entier ou un reel (par defaut, par exces, au plus pres...). Se conformer a un nombre de chiffres significatifs. | On se limite a des cas simples en base 10 et en base 2. On ne fait aucune theorie sur les calculs d'incertitude. |
| Addition, soustraction, multiplication et division des entiers naturels. | Calculer a la main : des additions en bases 2 et 16 ; des multiplications et des divisions par une puissance de deux, en base 2. | |
| **Arithmetique modulaire** | | On evite tout exces de technicite en s'efforcant d'utiliser des presentations concretes. |
| Division euclidienne : quotient, reste, existence, unicite. | | On se limite aux entiers naturels. |
| Nombres premiers, decomposition en produit de facteurs premiers, entiers premiers entre eux, PGCD de deux entiers. | Decomposer un entier naturel en produit de facteurs premiers et determiner tous ses diviseurs. Mettre en oeuvre un algorithme : de recherche de nombres premiers ; de decomposition en produit de facteurs premiers. | Aucune technique n'est censee etre connue. |
| Congruences. Compatibilite avec l'addition et la multiplication. Propriete : modulo n, les multiples de a sont les multiples de PGCD(a, n). | Mener un calcul de congruence modulo n. Parcourir une liste circulaire par sauts d'amplitude constante. | On montre l'efficacite du langage des congruences. On note que le parcours n'est exhaustif que quand la longueur du saut et la taille de la liste sont des entiers premiers entre eux. |

---

### Module : Algebres de Boole

#### 1. Calcul des propositions et des predicats

L'objectif est d'introduire quelques elements de logique en liaison avec l'enseignement de l'informatique. Il s'agit d'une breve etude destinee a familiariser les etudiants a une pratique elementaire du calcul portant sur des enonces.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Calcul propositionnel** | | |
| Proposition, valeur de verite. Connecteurs logiques : negation (non P, not P, P barre) ; conjonction (P et Q, P et Q) ; disjonction (P ou Q, P ou Q) ; implication ; equivalence. | Traiter un exemple simple de calcul portant sur un enonce. Utiliser des connecteurs logiques pour exprimer une condition. | On degage les proprietes fondamentales des operations introduites, de maniere a deboucher ensuite sur un exemple d'algebre de Boole. En situation, on aborde les lois de Morgan. On se limite au cas ou l'utilisation d'une table de verite ou de proprietes elementaires du calcul propositionnel permet de conclure sans exces de technicite. Cette capacite est egalement mise en oeuvre en algorithmique. |
| **Calcul des predicats** | | |
| Variable, constante. Quantificateurs pour tout, il existe. | Passer du langage courant au langage mathematique et inversement. | On se limite a des cas simples de predicats portant sur une, deux ou trois variables. |
| Negation de "pour tout x, p(x)" ; negation de "il existe x, p(x)". | Exprimer, dans un cas simple, la negation d'un predicat. | On met en valeur l'importance de l'ordre dans lequel deux quantificateurs interviennent. |

#### 2. Langage ensembliste

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Langage ensembliste** | | |
| Ensemble, appartenance, inclusion, ensemble vide. Ensemble P(E) des parties d'un ensemble E. Complementaire d'une partie, intersection et reunion de deux parties. | Traiter un exemple simple de calcul portant sur des ensembles finis. | On degage les proprietes fondamentales des operations ainsi introduites, de maniere a deboucher ensuite sur un exemple d'algebre de Boole. En situation, on aborde les lois de Morgan. |
| Ensemble des elements x d'un ensemble E satisfaisant a une proposition p(x). | | On interprete en termes ensemblistes l'implication, la conjonction et la disjonction de deux propositions, ainsi que la negation d'une proposition. |

#### 3. Calcul booleen

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Calcul booleen** | | On adopte les notations usuelles : a barre, a + b et ab. |
| Algebre de Boole : definition ; proprietes des operations, lois de Morgan. | Mener des calculs portant sur des variables booleennes. Simplifier une expression booleenne en utilisant : un tableau de Karnaugh ; les regles de calcul booleen. Passer d'une situation donnee a une expression booleenne correspondante et inversement. | On se limite a des cas simples, comportant au plus trois variables booleennes, pour lesquels on peut conclure sans exces de technicite. On signale l'interet des connecteurs non-ou (nor) et non-et (nand), ou exclusif ou (xor). |

---

### Module : Elements de la theorie des ensembles

Ce module vient completer, concernant les ensembles, celui relatif aux algebres de Boole. Il developpe les notions de produit cartesien, de relation et d'application en liaison avec les nombreuses utilisations qui en sont faites en informatique (codage, tri, compression...).

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Elements de la theorie des ensembles** | | Les exemples utilises sont choisis principalement en liaison avec l'enseignement de l'informatique. |
| Produit cartesien de deux ensembles : definition ; cardinal de E x F dans le cas ou E et F sont finis. | Determiner et denombrer les elements du produit cartesien de deux ensembles finis. | On generalise au cas du produit cartesien de n ensembles finis. |
| Relations binaires : definition ; proprietes ; relations d'equivalence, relations d'ordre. | Traiter un exemple ou les contraintes se traduisent en termes de relation d'ordre ou d'equivalence. | On evite un trop grand formalisme. On ne s'interesse qu'aux utilisations en informatique. |
| Application f d'un ensemble E dans un ensemble F : definition ; image d'une partie A de E ; image reciproque d'une partie B de F. | Determiner l'image ou l'image reciproque d'une partie finie par une application. | |
| Injection, surjection, bijection. | Traiter un exemple ou les contraintes se traduisent en termes d'injection, de surjection ou de bijection. | On attache plus d'importance a une caracterisation textuelle qu'a l'enonce de predicats. On souligne l'importance de la notion d'injection pour coder des informations. |
| Composition d'applications. | Ecrire une application sous forme de composee. Traiter un exemple de composition d'applications toutes deux soit injectives, soit surjectives, soit bijectives. | On souligne le fait que la composition d'applications n'est pas une operation commutative. On privilegieles situations issues des autres enseignements. |

---

### Module : Graphes et ordonnancement

#### 1. Graphes

L'objectif est d'introduire et de mettre en oeuvre, dans des situations concretes tres elementaires et sans theorie generale, des algorithmes permettant de resoudre les problemes figurant dans la colonne "Capacites attendues".

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Graphes** | | |
| Modes de representation d'un graphe fini simple oriente : representation geometrique, tableau des successeurs ou des predecesseurs, matrice d'adjacence booleenne. | Passer d'un mode de representation a un autre, pour un graphe donne. | La definition d'un graphe fini simple oriente est limitee a la donnee d'un ensemble de sommets et d'un ensemble d'arcs. |
| Chemin d'un graphe : definition, longueur, circuit, boucle, chemin hamiltonien. | | |
| Puissances entieres et booleennes de la matrice d'adjacence. | Obtenir et interpreter, pour une matrice d'adjacence M donnee, les coefficients : d'une puissance entiere de M ; d'une puissance booleenne de M. Mettre en oeuvre un algorithme permettant d'obtenir les chemins de longueur p d'un graphe. | On considere uniquement le cas d'un graphe non value (non pondere). A partir d'exemples tres elementaires et sans introduire une theorie generale, on montre l'interet des methodes matricielles mettant en oeuvre l'addition et la multiplication booleennes des matrices d'adjacence. |
| Fermeture transitive d'un graphe. | Mettre en oeuvre un algorithme permettant d'obtenir la fermeture transitive d'un graphe. | |
| Pour un graphe sans circuit : niveau d'un sommet, niveaux du graphe. | Mettre en oeuvre un algorithme permettant d'obtenir les niveaux dans un graphe sans circuit. Representer geometriquement un graphe en l'ordonnant par niveaux. | Il convient de savoir determiner les niveaux, sans qu'aucune methode ne soit imposee. |
| Arborescence. | | La notion de connexite etant hors programme, on se limite a la presentation d'exemples simples d'arborescences a partir de leur representation geometrique, sans recherche d'une caracterisation generale. |
| Chemin optimal en longueur. | Mettre en oeuvre un algorithme permettant d'obtenir une optimisation d'un graphe : en longueur ; en valeur (graphe value). | On observe l'importance du resultat : tout sous-chemin d'un chemin optimal est optimal. |
| Graphe value (pondere) : definition ; chemin optimal en valeur. | | On fait une simple presentation des graphes values, sans theorie particuliere. |

#### 2. Ordonnancement

L'objectif est double : sensibiliser l'etudiant aux problemes d'ordonnancement et traiter manuellement un algorithme. On abordera surtout la comprehension des mecanismes.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Ordonnancement** | | On presente quelques cas concrets simplifies et on les interprete. Aucune autre competence theorique n'est requise. |
| Ordonnancement : methode MPM ou methode PERT, principe de representation ; dates au plus tot, au plus tard ; taches et chemins critiques ; marge totale, libre, certaine. | Resoudre un probleme d'ordonnancement en mettant en oeuvre la methode des potentiels metra (MPM) ou la methode PERT, et interpreter les resultats obtenus a travers les notions abordees. Reconnaitre une contrainte non incluse dans la modelisation et en tenir compte lors de l'interpretation. | On se limite a des cas tres simples ou l'interpretation ne souleve aucune difficulte theorique. |

---

### Module : Algorithmique appliquee

L'objectif est de construire des algorithmes et de les programmer dans un langage informatique, dans le but de resoudre des problemes de niveau raisonnable. Ce module vise a developper les competences specifiques suivantes :
- comprendre un algorithme et expliquer ce qu'il fait ;
- modifier un algorithme existant pour obtenir un resultat different ;
- concevoir une procedure, un algorithme simple ;
- transcrire un algorithme dans un langage informatique ;
- s'interroger sur l'efficacite d'un algorithme.

| Contenu | Capacites attendues | Commentaires |
|---|---|---|
| **Types de donnees** | | |
| Types simples : entier naturel, entier relatif, reel, booleen. | Connaitre les modes de codage et gerer les differences entre donnees mathematiques et informatiques : domaine de valeurs ; representation exacte ou approchee, precision. | Il n'est pas necessaire de connaitre la representation exacte des donnees en machine, notamment en ce qui concerne les flottants. |
| Chaine de caracteres. | | On evite de considerer une chaine comme un tableau de caracteres. |
| Tableaux de donnees : de type homogene a une ou deux dimensions ; a deux dimensions dans lequel, soit les lignes soit les colonnes, peuvent etre de types differents. | Construire un tableau. Traiter les donnees d'un tableau : acceder a ses differents elements en lecture et en ecriture ; traiter les elements d'une ligne ou d'une colonne ; copier un tableau. | On adapte la construction et l'exploitation de ces tableaux aux possibilites de l'outil informatique utilise. Les structures de donnees et les objets ne sont pas au programme de mathematiques : ils figurent dans ceux des enseignements professionnels. |
| Procedure et fonction : parametres d'entree ; valeur(s) retournee(s) par une fonction ; variables globales ou locales. | Gerer les transferts en entree seule, en sortie seule, en entree et sortie. Utiliser les variables globales et locales. | Sans aborder la programmation objet, les concepts de modularite et d'interface doivent etre connus. |
| **Instructions elementaires** | | |
| Lecture, ecriture. Affectation, affectation recursive. | Saisir une donnee depuis le clavier, manipuler les variables et afficher sur l'ecran. Gerer la chronologie des valeurs contenues dans les variables et produire la trace d'un algorithme. | Les fichiers ne sont pas au programme de mathematiques. En standard, la mise en forme des affichages est limitee a l'utilisation de separateurs et de changements de ligne. La gestion des pointeurs n'est pas au programme. |
| **Operateurs** | | |
| Operateurs numeriques : addition, soustraction, multiplication, division, exponentiation, quotient et reste de la division entiere, signe. Fonctions mathematiques usuelles. | Transformer une expression mathematique en expression numerique en ligne et reciproquement. | "Fonctions mathematiques usuelles" doit etre entendu au sens informatique et inclure les fonctions d'arrondi, ainsi qu'un generateur de nombres pseudo-aleatoires uniforme dans un intervalle. |
| Operateurs de comparaison : =, <> ou !=, <, <=, >, >=. | | On compare soit des valeurs numeriques, soit des chaines de caracteres. |
| Operateurs booleens : non, et, ou, oux. | Traduire la condition (eventuellement composee) d'une iteration ou d'une alternative sous forme d'expression booleenne. | |
| Operateurs booleens bit a bit. | Appliquer des operations booleennes sur les bits. | On interprete notamment en termes de masque, de mise a un, de mise a zero, de changement d'etat. |
| Operateur de chaines : concatenation. Fonctions permettant l'extraction en debut, milieu ou fin, la recherche d'un motif. | Construire et manipuler des chaines et construire les messages affiches a l'ecran. | L'usage d'expressions regulieres simples est possible, mais l'etude des expressions regulieres est hors programme. |
| Transtypage | Gerer les differents types de donnees et effectuer des conversions d'un type vers un autre. | D'autres instructions, fonctions ou procedures peuvent etre introduites dans l'ecriture d'algorithmes. Les descriptions semantiques et syntaxiques precises sont alors mises a disposition de l'etudiant. |
| **Structures de controle et d'execution** | | |
| Execution sequentielle. Execution a structure conditionnelle (si-alors-sinon). Execution a structure iterative (pour) et (tant que / repeter jusqu'a ce que). | Mettre en oeuvre ces structures. | Afin d'en maitriser le fonctionnement, les structures d'execution sont elles-memes presentees sous forme d'algorithmes. |
| Construction des structures iteratives : raisonnement par recurrence, initialisation, mise a jour iterative, calcul iteratif, mise en forme finale. | Gerer une iteration en distinguant la preparation, l'iteration elle-meme et la mise en forme finale. | Le raisonnement par recurrence n'a pas a etre evalue pour des demonstrations. Il est introduit pour servir de base a une construction des iterations. Le calcul iteratif est souvent recursif. |
| Symboles Sigma et Pi, traduction algorithmique. | Gerer une somme ou un produit d'un nombre variable d'operandes dependant d'un parametre. | Generalement la variable affectee recursivement est initialisee a l'element neutre de l'operation utilisee, avant d'entrer dans l'iteration. |
| Structures imbriquees | Gerer des structures imbriquees. | On traite egalement des exemples ou les elements de controle des structures internes dependent de ceux des structures externes. Le nombre d'imbrications n'est pas limite, sauf pour les iterations en dependance, ou on se limite a deux. On evite les exces de complexite, ainsi que les constructions ne correspondant pas a un besoin concret. |
| | Traiter un produit matriciel. | La formule de calcul des coefficients d'un produit est donnee. |
| Recursivite. Necessite d'un test. Necessite de cas particuliers resolus sans appel a la recursivite. Finitude. | Mettre en oeuvre ou exploiter une fonction ou une procedure recursive simple. | On peut traiter des exemples de recursivite terminale, de conversion en algorithme non recursif, de recursivite non terminale. On ne presente pas de recursivite mutuelle entre plusieurs procedures. |
| **Analyse d'algorithmes** | | Ce paragraphe se veut une simple sensibilisation aux notions de complexite, de correction, de recherche d'erreur et de finalite d'un algorithme. En cas d'evaluation, on apporte suffisamment d'indications pour limiter les prerequis. |
| Notions de complexite temporelle et spatiale. | Calculer un nombre minimal ou maximal d'operations significatives ou la taille globale de donnees choisies. | On presente des variantes produisant les memes resultats avec des complexites tres differentes. Aucune connaissance theorique n'est exigible. |
| Validation et debogage. | Proceder a un suivi de variables par la production d'une trace ou l'utilisation de jeux d'essai pour le test d'un algorithme et la recherche d'erreur. | On propose des algorithmes deliberement errones dont les defauts sont reperes puis debogues. Selon le langage choisi, on peut montrer les fonctions permettant le suivi de variables, le debogage pas a pas. Afin de mieux sensibiliser a certains risques, on peut presenter des cas d'effets indesirables (effets de bord, evaluation partielle lors de calcul d'expressions booleennes, debordements ou approximations numeriques, transtypage, utilisation d'indices hors domaine...) et leurs consequences spectaculaires. Aucune theorie n'est au programme. |
| Interpretation d'algorithmes. | Savoir reconstituer le role d'un algorithme. | L'ajout d'une ou plusieurs procedures ou fonctions a un ensemble interdependant peut constituer une excellente base. On se limite a des cas simples. |

---

## Annexe II : Les capacites et competences

La formation mathematique des etudiants de STS vise essentiellement le developpement des six competences suivantes :

1. **S'informer** : face a un probleme donne et a une documentation, extraire un maximum de renseignements pertinents.
2. **Chercher** : se poser les bonnes questions, identifier les donnees, formuler des hypotheses, tester, experimenter.
3. **Modeliser** : traduire un probleme en langage mathematique, utiliser les outils mathematiques pour le traiter (suite, fonction, graphe, configuration geometrique, outil statistique, simulation informatique...).
4. **Raisonner, argumenter** : effectuer des inferences (inductives et deductives), conduire une demonstration, donner les justifications necessaires.
5. **Calculer, illustrer, mettre en oeuvre une strategie** : mener efficacement un calcul simple, manipuler des expressions contenant des symboles, analyser la pertinence d'un resultat obtenu.
6. **Communiquer** : clarte d'exposition, qualite de redaction, soin dans la presentation de tableaux, figures et representations graphiques, qualite de l'expression en francais a l'ecrit comme a l'oral.

---

## Annexe III : Repartition des modules selon les specialites de BTS

L'Annexe III du programme officiel detaille, pour chacune des specialites de BTS (plus de 60 specialites), les modules specifiques a enseigner. Chaque specialite precise :
- ses objectifs specifiques a la section ;
- l'organisation des contenus autour de poles significatifs ;
- l'horaire de mathematiques (variable selon les specialites).

**Exemple -- BTS Aeronautique :**
- Objectifs : etude de phenomenes continus, vision geometrique, methodes statistiques.
- Organisation autour de quatre poles : fonctions usuelles et equations differentielles ; problemes geometriques ; calcul des probabilites et statistique inferentielle ; aspects numeriques et graphiques.
- Horaire : 2h + 1h en premiere annee, 1h + 1h en seconde annee.

Les modules attribues varient fortement selon les specialites. Se reporter au PDF officiel (pages 63 a 180) pour la repartition exacte de chaque specialite.

### Liste des specialites detaillees dans l'Annexe III

Aeronautique, Agencement de l'environnement architectural, Amenagement finition, Analyses de biologie medicale, Apres-vente automobile, Assistance technique d'ingenieur, Batiment, Bio-analyses et controles, Biotechnologie, Charpente-couverture, Chimiste, Communication et industries graphiques, Comptabilite et gestion des organisations, Concepteur en art et industrie ceramique, Conception de produits industriels, Conception et industrialisation en microtechniques, Conception et realisation de carrosseries, Conception et realisation des systemes automatiques, Conception et realisation en chaudronnerie industrielle, Construction navale, Constructions metalliques, Controle industriel et regulation automatique, Design d'espace, Design de communication espace et volume, Design de produits, Developpement et realisation bois, Domotique, Electrotechnique, Enveloppe du batiment (facades-etancheite), Environnement nucleaire, Etude et realisation d'outillages de mise en forme des materiaux, Etudes et economie de la construction, Fluides-energies-environnements, Fonderie, Genie optique, Geologie appliquee, Geometre topographe, Industrialisation des produits mecaniques, Industries ceramiques, Industries papetieres, Industries plastiques "europlastic", Informatique et reseaux pour l'industrie et les services techniques, Maintenance et apres-vente des engins de travaux publics et de manutention, Maintenance industrielle, Metiers de l'eau, Metiers de la mode (chaussure maroquinerie), Metiers de la mode (vetement), Mise en forme des materiaux par forgeage, Moteurs a combustion interne, Opticien-lunetier, Peintures encres et adhesifs, Productique textile, Qualite dans les industries alimentaires et les bio-industries, Services informatiques aux organisations, Systemes constructifs bois et habitat, Systemes electroniques, Techniques et services en materiels agricoles, Techniques physiques pour l'industrie et le laboratoire, Traitement des materiaux, Travaux publics.
