/**
 * nav.js  —  Navigation automatique pour pages de cours / exercices / DS
 *
 * UTILISATION (ajouter à chaque page HTML) :
 *   Avant </body> : <script src="/nav.js"></script>
 *
 * Le script détecte automatiquement la page courante via le chemin URL,
 * puis injecte : fil d'Ariane, menu du chapitre, navigation ch. précédent/suivant,
 * bouton retour en haut.
 *
 * Structure attendue :
 *   /maths/seconde/ch01/lecon.html
 *   /physique-chimie/terminale-iccer/ch01/exercices.html
 *   /simulations/equations.html
 */
/* ── Fonction toggle globale pour boutons « Voir la correction » ──── */
/* Définie AVANT toute IIFE pour qu'elle soit toujours disponible,    */
/* y compris sur les activités à nom non standard (activite-2-…, etc.) */
if (typeof window.toggle !== 'function') {
  window.toggle = function (btn) {
    var c = btn.nextElementSibling;
    if (c.style.display === 'block') {
      c.style.display = 'none';
      btn.textContent = 'Voir la correction';
    } else {
      c.style.display = 'block';
      btn.textContent = 'Masquer la correction';
    }
  };
}

(function () {
  'use strict';

  /* ── Base de données des séries ────────────────────────────────────── */
  var SERIES = {

    /* Mathématiques — 2nde Pro MAMA */
    'maths/seconde': {
      summary:      'maths-2nde-mama.html',
      summaryLabel: '2nde Pro MAMA',
      subject:      'Mathématiques',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', fiche: 'Fiche résumé', qcm: 'QCM', interro: 'Interrogation', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Proportionnalité et pourcentages' },
        { id: '02', title: 'Statistiques à une variable' },
        { id: '03', title: 'Indicateurs statistiques' },
        { id: '04', title: 'Fluctuations et probabilités' },
        { id: '05', title: 'Équations du premier degré' },
        { id: '06', title: 'Inéquations du premier degré' },
        { id: '07', title: 'Notion de fonction' },
        { id: '08', title: 'Fonction linéaire et proportionnalité' },
        { id: '09', title: 'Fonction affine' },
        { id: '10', title: 'Fonction carré et variations' },
        { id: '11', title: 'Figures planes : périmètres et aires' },
        { id: '12', title: 'Théorème de Pythagore et réciproque' },
        { id: '13', title: 'Théorème de Thalès dans le triangle' },
        { id: '14', title: 'Solides, volumes et agrandissement' }
      ]
    },

    /* Mathématiques — 1ère Bac Pro */
    'maths/premiere': {
      summary:      'maths-1ere-pro.html',
      summaryLabel: '1ère Bac Pro',
      subject:      'Mathématiques',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', fiche: 'Fiche résumé', qcm: 'QCM', interro: 'Interrogation', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Statistique à deux variables' },
        { id: '02', title: 'Probabilités' },
        { id: '03', title: 'Suites numériques' },
        { id: '04', title: 'Résolution graphique d\'équations et d\'inéquations' },
        { id: '05', title: 'Fonctions polynômes de degré 2' },
        { id: '06', title: 'Fonction dérivée et étude des variations' },
        { id: '07', title: 'Géométrie dans l\'espace' },
        { id: '08', title: 'Vecteurs du plan' },
        { id: '09', title: 'Trigonométrie' }
      ]
    },

    /* Mathématiques — Terminale Bac Pro (TICCER & TERA-TMA) */
    'maths/terminale': {
      summary:      'maths-term-iccer.html',
      summaryLabel: 'Terminale Bac Pro',
      subject:      'Mathématiques',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', fiche: 'Fiche résumé', qcm: 'QCM', interro: 'Interrogation', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Statistiques à deux variables' },
        { id: '02', title: 'Probabilités' },
        { id: '03', title: 'Suites numériques' },
        { id: '04', title: 'Fonctions polynômes de degré 3' },
        { id: '05', title: 'Fonctions exponentielles et logarithme décimal' },
        { id: '06', title: 'Vecteurs' },
        { id: '07', title: 'Trigonométrie' },
        { id: '08', title: 'Calcul intégral' },
        { id: '09', title: 'Fonctions logarithme népérien et exponentielle' },
        { id: '10', title: 'Nombres complexes' },
        { id: '11', title: 'Produit scalaire' }
      ]
    },

    /* Mathématiques — BTS (tous groupements) */
    'maths/bts': {
      summary:      'maths-bts.html',
      summaryLabel: 'BTS',
      subject:      'Mathématiques',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', qcm: 'QCM', interro: 'Interrogation' },
      chapters: [
        { id: '01', title: 'Suites numériques' },
        { id: '02', title: 'Fonctions d\'une variable réelle' },
        { id: '03', title: 'Fonctions pour le traitement du signal' },
        { id: '04', title: 'Calcul intégral' },
        { id: '05', title: 'Équations différentielles' },
        { id: '06', title: 'Séries de Fourier' },
        { id: '07', title: 'Transformée de Laplace' },
        { id: '08', title: 'Probabilités 1' },
        { id: '09', title: 'Probabilités 2' },
        { id: '10', title: 'Statistique descriptive' },
        { id: '11', title: 'Statistique inférentielle' },
        { id: '12', title: 'Nombres complexes' },
        { id: '13', title: 'Configurations géométriques' },
        { id: '14', title: 'Modélisation géométrique' },
        { id: '15', title: 'Calcul vectoriel' },
        { id: '16', title: 'Matrices et systèmes linéaires' },
        { id: '17', title: 'Calcul et algorithmique' },
        { id: '18', title: 'Fiabilité' },
        { id: '19', title: 'Transformation en z' },
        { id: '20', title: 'Plans d\'expérience' },
        { id: '21', title: 'Représentation de l\'espace' },
        { id: '22', title: 'Algèbres de Boole' },
        { id: '23', title: 'Éléments de théorie des ensembles' },
        { id: '24', title: 'Graphes et ordonnancement' },
        { id: '25', title: 'Algorithmique appliquée' }
      ]
    },

    /* Mathématiques — CAP */
    'maths/cap': {
      summary:      'maths-cap.html',
      summaryLabel: 'CAP',
      subject:      'Mathématiques',
      types: { lecon: 'Cours', exercices: 'Exercices', qcm: 'QCM', fiche: 'Fiche résumé', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Statistiques à une variable' },
        { id: '02', title: 'Probabilités' },
        { id: '03', title: 'Proportionnalité et pourcentages' },
        { id: '04', title: 'Équations du premier degré' },
        { id: '05', title: 'Fonctions' },
        { id: '06', title: 'Géométrie' },
        { id: '07', title: 'Calculs numériques' }
      ]
    },

    /* Physique-Chimie — CAP */
    'physique-chimie/cap': {
      summary:      'pc-cap.html',
      summaryLabel: 'CAP',
      subject:      'Physique-Chimie',
      types: { lecon: 'Cours', exercices: 'Exercices', qcm: 'QCM', fiche: 'Fiche résumé', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Sécurité' },
        { id: '02', title: 'Électricité' },
        { id: '03', title: 'Mécanique' },
        { id: '04', title: 'Chimie' },
        { id: '05', title: 'Acoustique' },
        { id: '06', title: 'Thermique' },
        { id: '07', title: 'Optique' }
      ]
    },

    /* Physique-Chimie — 2nde Pro MAMA */
    'physique-chimie/seconde': {
      summary:      'pc-2nde-pro.html',
      summaryLabel: '2nde Pro MAMA',
      subject:      'Physique-Chimie',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', fiche: 'Fiche résumé', qcm: 'QCM', interro: 'Interrogation', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Sécurité en laboratoire et en atelier' },
        { id: '02', title: 'Grandeurs électriques et circuits' },
        { id: '03', title: 'Loi d\'Ohm et caractéristiques d\'un dipôle' },
        { id: '04', title: 'Signaux électriques alternatifs' },
        { id: '05', title: 'Mouvement et trajectoire' },
        { id: '06', title: 'Forces et équilibre' },
        { id: '07', title: 'Structure de la matière : atomes, ions et molécules' },
        { id: '08', title: 'Solutions chimiques et concentration' },
        { id: '09', title: 'Caractéristiques d\'un son' },
        { id: '10', title: 'Température et capteurs thermiques' },
        { id: '11', title: 'Transferts thermiques et équilibre thermique' },
        { id: '12', title: 'Changements d\'état et énergie thermique' },
        { id: '13', title: 'Réflexion, réfraction et signaux lumineux' },
        { id: '14', title: 'Lumière, couleurs et photodétecteurs' }
      ]
    },

    /* Physique-Chimie — 1ère ICCER */
    'physique-chimie/premiere-iccer': {
      summary:      'pc-1ere-iccer.html',
      summaryLabel: '1ère ICCER',
      subject:      'Physique-Chimie',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', fiche: 'Fiche résumé', qcm: 'QCM', interro: 'Interrogation', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Distinguer énergie et puissance électrique' },
        { id: '02', title: 'Transporter l\'énergie sous forme électrique' },
        { id: '03', title: 'Combustion du carbone et des hydrocarbures' },
        { id: '04', title: 'Les trois modes de transfert thermique' },
        { id: '05', title: 'Vitesse et accélération en mouvement rectiligne' },
        { id: '06', title: 'Équilibre d\'un solide en rotation autour d\'un axe fixe' },
        { id: '07', title: 'Pression et force pressante' },
        { id: '08', title: 'La force d\'Archimède' },
        { id: '09', title: 'Solutions aqueuses et concentration' },
        { id: '10', title: 'Ondes électromagnétiques' }
      ]
    },

    /* Physique-Chimie — 1ère ERA-MA */
    'physique-chimie/premiere-era': {
      summary:      'pc-1ere-erama.html',
      summaryLabel: '1ère ERA-MA',
      subject:      'Physique-Chimie',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', fiche: 'Fiche résumé', qcm: 'QCM', interro: 'Interrogation', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Distinguer énergie et puissance électrique' },
        { id: '02', title: 'Évaluer la puissance consommée par un appareil électrique' },
        { id: '03', title: 'Combustion du carbone et des hydrocarbures' },
        { id: '04', title: 'Les trois modes de transfert thermique' },
        { id: '05', title: 'Minimiser les transferts thermiques pour économiser l\'énergie' },
        { id: '06', title: 'Équilibre d\'un solide en rotation autour d\'un axe fixe' },
        { id: '07', title: 'Pression et force pressante' },
        { id: '08', title: 'Solutions aqueuses et concentration' },
        { id: '09', title: 'Ondes électromagnétiques' },
        { id: '10', title: 'Propagation d\'un signal sonore' }
      ]
    },

    /* Physique-Chimie — Terminale ICCER */
    'physique-chimie/terminale-iccer': {
      summary:      'pc-term-iccer.html',
      summaryLabel: 'Terminale ICCER',
      subject:      'Physique-Chimie',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', fiche: 'Fiche résumé', qcm: 'QCM', interro: 'Interrogation', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Évaluer la puissance consommée' },
        { id: '02', title: 'Obtenir un courant continu à partir d\'un courant alternatif et inversement' },
        { id: '03', title: 'Obtenir de l\'énergie mécanique à l\'aide d\'un moteur électrique' },
        { id: '04', title: 'Utiliser le rayonnement thermique et comprendre l\'effet de serre' },
        { id: '05', title: 'Caractériser la pression dans un fluide immobile' },
        { id: '06', title: 'Décrire le transport de masse et de volume par un fluide en mouvement' },
        { id: '07', title: 'Oxydoréduction et protection des métaux contre la corrosion' },
        { id: '08', title: 'Caractériser la propagation d\'un signal sonore' }
      ]
    },

    /* Physique-Chimie — Terminale ERA-MA */
    'physique-chimie/terminale-era': {
      summary:      'pc-term-erama.html',
      summaryLabel: 'Terminale ERA-MA',
      subject:      'Physique-Chimie',
      types: { lecon: 'Cours', exercices: 'Exercices', 'exercices-capacites': 'Capacités', ds: 'Devoir surveillé', fiche: 'Fiche résumé', qcm: 'QCM', interro: 'Interrogation', activite: 'Activité', simulation: 'Simulation' },
      chapters: [
        { id: '01', title: 'Transporter l\'énergie sous forme électrique' },
        { id: '02', title: 'Stocker l\'énergie à l\'aide d\'un système électrochimique' },
        { id: '03', title: 'Rayonnement thermique et effet de serre' },
        { id: '04', title: 'Caractériser la vitesse et l\'accélération' },
        { id: '05', title: 'Oxydoréduction et protection des métaux' },
        { id: '06', title: 'Choisir une source lumineuse' },
        { id: '07', title: 'Transmettre l\'information' },
        { id: '08', title: 'Atténuer une onde sonore par transmission' }
      ]
    }
  };

  /* ── Pages sommaires (affichage simple ← Accueil) ──────────────────── */
  var SUMMARY_PAGES = {
    'maths-2nde-mama.html':  { label: 'Mathématiques — 2nde Pro MAMA' },
    'maths-1ere-pro.html':   { label: 'Mathématiques — 1ère Bac Pro' },
    'maths-term-iccer.html': { label: 'Mathématiques — Terminale ICCER' },
    'maths-term-erama.html': { label: 'Mathématiques — Terminale ERA-MA' },
    'pc-2nde-pro.html':      { label: 'Physique-Chimie — 2nde Pro' },
    'pc-1ere-iccer.html':    { label: 'Physique-Chimie — 1ère ICCER' },
    'pc-1ere-erama.html':    { label: 'Physique-Chimie — 1ère ERA-MA' },
    'pc-term-iccer.html':    { label: 'Physique-Chimie — Terminale ICCER' },
    'pc-term-erama.html':    { label: 'Physique-Chimie — Terminale ERA-MA' },
    'simulations.html':      { label: 'Simulations interactives' },
    'maths-bts.html':        { label: 'Mathématiques — BTS' },
    'maths-cap.html':        { label: 'Mathématiques — CAP' },
    'pc-cap.html':           { label: 'Physique-Chimie — CAP' }
  };

  /* ── Détection du chemin courant ───────────────────────────────────── */
  var pathname = window.location.pathname;
  var parts    = pathname.split('/').filter(function (p) { return p !== ''; });

  if (!parts.length) return;

  /* Calcul du préfixe racine (ex : '../../../' depuis un chapitre depth 4) */
  var rootPrefix = parts.length > 1 ? '../'.repeat(parts.length - 1) : '';

  /* ── Helpers ───────────────────────────────────────────────────────── */
  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function injectCss() {
    var links = document.querySelectorAll('link[rel="stylesheet"]');
    for (var j = 0; j < links.length; j++) {
      if (links[j].href && links[j].href.indexOf('nav.css') !== -1) return;
    }
    var cssLink  = document.createElement('link');
    cssLink.rel  = 'stylesheet';
    cssLink.href = rootPrefix + 'nav.css';
    document.head.appendChild(cssLink);
  }

  /* ── Cas 1 : page sommaire (à la racine) ───────────────────────────── */
  var filename = parts[parts.length - 1];
  if (SUMMARY_PAGES[filename]) {
    var info   = SUMMARY_PAGES[filename];
    var sumBC  = document.createElement('nav');
    sumBC.className = 'sn-breadcrumb';
    sumBC.setAttribute('aria-label', "Fil d'Ariane");
    sumBC.innerHTML =
      '<a href="' + rootPrefix + 'index.html">Accueil</a>' +
      '<span class="sn-sep">›</span>' +
      '<span class="sn-bc-current">' + esc(info.label) + '</span>';

    var wrap = document.querySelector('.container') ||
               document.querySelector('.c') ||
               document.body;
    wrap.insertBefore(sumBC, wrap.firstChild);
    var sumAuthor = document.createElement('footer');
    sumAuthor.className = 'sn-author';
    sumAuthor.innerHTML = 'Na\u00efm Azzouz';
    wrap.appendChild(sumAuthor);
    injectCss();
    return;
  }

  /* ── Cas 2 : page chapitre ─────────────────────────────────────────── */
  /* Attendu : parts = ['matiere', 'niveau', 'chXX', 'type.html'] */
  if (parts.length < 4) return;

  var pageFile = parts[parts.length - 1];            /* lecon.html       */
  var chFolder = parts[parts.length - 2];            /* ch01             */
  var pageType = pageFile.replace('.html', '');       /* lecon            */
  var chId     = chFolder.replace('ch', '');          /* 01               */
  var serieKey = parts.slice(0, parts.length - 2).join('/'); /* maths/seconde */

  var serie = SERIES[serieKey];
  if (!serie) return;

  /* Vérifier que le type est valide */
  if (!serie.types[pageType]) return;

  /* Trouver le chapitre dans la liste */
  var chIndex = -1;
  for (var i = 0; i < serie.chapters.length; i++) {
    if (serie.chapters[i].id === chId) { chIndex = i; break; }
  }
  if (chIndex === -1) return;

  var chapter = serie.chapters[chIndex];

  function typeLabel(t) { return serie.types[t] || t; }

  /* ── Fil d'Ariane ──────────────────────────────────────────────────── */
  function buildBreadcrumb() {
    return [
      '<nav class="sn-breadcrumb" aria-label="Fil d\'Ariane">',
        '<a href="' + rootPrefix + 'index.html">Accueil</a>',
        '<span class="sn-sep">›</span>',
        '<a href="' + rootPrefix + serie.summary + '">' +
          esc(serie.subject) + ' — ' + esc(serie.summaryLabel) +
        '</a>',
        '<span class="sn-sep">›</span>',
        '<span>Ch' + chId + ' — ' + esc(chapter.title) + '</span>',
        '<span class="sn-sep">›</span>',
        '<span class="sn-bc-current">' + esc(typeLabel(pageType)) + '</span>',
      '</nav>'
    ].join('');
  }

  /* ── Menu du chapitre (onglets Cours / Exercices / DS / QCM…) ──────── */
  /* Types « optionnels » : l'onglet n'apparaît que si le fichier existe */
  var OPTIONAL_TYPES = { qcm: true, interro: true, activite: true, simulation: true, 'exercices-capacites': true };

  function buildChMenu() {
    var menuEl = document.createElement('div');
    menuEl.className = 'sn-ch-menu';

    Object.keys(serie.types).forEach(function (t) {
      if (OPTIONAL_TYPES[t]) return; /* traité plus bas en async */
      var active = (t === pageType) ? ' sn-tab-active' : '';
      var a = document.createElement('a');
      a.href = t + '.html';
      a.className = 'sn-tab' + active;
      a.textContent = typeLabel(t);
      menuEl.appendChild(a);
    });

    /* Vérifier l'existence des fichiers optionnels (QCM…) */
    Object.keys(serie.types).forEach(function (t) {
      if (!OPTIONAL_TYPES[t]) return;
      var url = t + '.html';
      fetch(url, { method: 'HEAD' }).then(function (r) {
        if (r.ok) {
          var active = (t === pageType) ? ' sn-tab-active' : '';
          var a = document.createElement('a');
          a.href = url;
          a.className = 'sn-tab' + active;
          a.textContent = typeLabel(t);
          menuEl.appendChild(a);
        }
      }).catch(function () { /* fichier absent → pas d'onglet */ });
    });

    return menuEl;
  }

  /* ── Boutons Précédent / Sommaire / Suivant ─────────────────────────── */
  function buildChNav() {
    var prev = chIndex > 0 ? serie.chapters[chIndex - 1] : null;
    var next = chIndex < serie.chapters.length - 1 ? serie.chapters[chIndex + 1] : null;

    var prevBtn = prev
      ? '<a href="../ch' + prev.id + '/' + pageType + '.html" class="sn-btn sn-btn-prev" title="' + esc(prev.title) + '">' +
          '&#8592; Ch' + prev.id + ' — ' + esc(prev.title) +
        '</a>'
      : '<span class="sn-btn-disabled">&#8592; Premier chapitre</span>';

    var summaryBtn = '<a href="' + rootPrefix + serie.summary +
                    '" class="sn-btn sn-btn-summary">&#9783; Sommaire</a>';

    var nextBtn = next
      ? '<a href="../ch' + next.id + '/' + pageType + '.html" class="sn-btn sn-btn-next" title="' + esc(next.title) + '">' +
          'Ch' + next.id + ' — ' + esc(next.title) + ' &#8594;' +
        '</a>'
      : '<span class="sn-btn-disabled">Dernier chapitre &#8594;</span>';

    return '<div class="sn-ch-nav">' + prevBtn + summaryBtn + nextBtn + '</div>';
  }

  /* ── Bouton retour en haut ─────────────────────────────────────────── */
  function buildBackTop() {
    return '<a href="#" id="sn-back-top" class="sn-back-top" ' +
           'title="Retour en haut de la page" aria-label="Retour en haut">&#8679;</a>';
  }

  /* ── Injection dans la page ────────────────────────────────────────── */
  var container = document.querySelector('.c') ||
                  document.querySelector('.container') ||
                  document.body;

  /* Bloc supérieur */
  var topBlock = document.createElement('div');
  topBlock.className = 'sn-top-block';
  topBlock.innerHTML = buildBreadcrumb() + buildChNav();
  /* Le menu chapitre est un élément DOM (onglets optionnels chargés en async) */
  var chMenuEl = buildChMenu();
  /* Insérer le menu après le breadcrumb, avant la nav ch. précédent/suivant */
  var chNavEl = topBlock.querySelector('.sn-ch-nav');
  topBlock.insertBefore(chMenuEl, chNavEl);
  container.insertBefore(topBlock, container.firstChild);

  /* ── Sommaire automatique (pages Cours uniquement) ─────────────────── */
  if (pageType === 'lecon') {
    var h2s = container.querySelectorAll('h2');
    if (h2s.length >= 3) {
      var tocItems = [];
      for (var k = 0; k < h2s.length; k++) {
        var h = h2s[k];
        if (!h.id) h.id = 'sn-sec-' + k;
        tocItems.push('<li><a href="#' + h.id + '">' + esc(h.textContent.trim()) + '</a></li>');
      }
      var tocEl = document.createElement('details');
      tocEl.className = 'sn-toc';
      tocEl.setAttribute('open', '');
      tocEl.innerHTML =
        '<summary class="sn-toc-title">&#9776;&nbsp; Sommaire</summary>' +
        '<ol class="sn-toc-list">' + tocItems.join('') + '</ol>';
      container.insertBefore(tocEl, topBlock.nextSibling);
    }
  }

  /* Masquer l'ancien lien "← Retour au sommaire" s'il existe */
  var oldBack = container.querySelector('.nb');
  if (oldBack) oldBack.style.display = 'none';

  /* ── Barre d'impression ────────────────────────────────────────────── */
  var hasCorrections = (pageType === 'exercices' || pageType === 'ds' || pageType === 'interro');
  var printBar = document.createElement('div');
  printBar.className = 'print-bar';
  if (hasCorrections) {
    printBar.innerHTML =
      '<span>Imprimer / G\u00e9n\u00e9rer un PDF</span>' +
      '<button class="print-btn" onclick="window.print()">' +
        '\uD83D\uDCC4 Version \u00e9l\u00e8ve (sans correction)' +
      '</button>' +
      '<button class="print-btn print-btn-corr" id="sn-print-corr">' +
        '\u2705 Version corrig\u00e9 (avec corrections)' +
      '</button>';
  } else {
    printBar.innerHTML =
      '<span>Imprimer / G\u00e9n\u00e9rer un PDF</span>' +
      '<button class="print-btn" onclick="window.print()">' +
        '\uD83D\uDCC4 Imprimer cette page' +
      '</button>';
  }
  container.appendChild(printBar);
  if (hasCorrections) {
    document.getElementById('sn-print-corr').addEventListener('click', function () {
      /* Forcer l'affichage de chaque correction via style inline !important */
      var corrs = document.querySelectorAll('.corr, .correction, .qcm-corr, .flash-corr');
      for (var i = 0; i < corrs.length; i++) {
        corrs[i].style.setProperty('display', 'block', 'important');
      }
      window.addEventListener('afterprint', function cleanup() {
        for (var j = 0; j < corrs.length; j++) {
          corrs[j].style.removeProperty('display');
        }
        window.removeEventListener('afterprint', cleanup);
      });
      setTimeout(function () { window.print(); }, 100);
    });
  }

  /* Bloc inférieur */
  var footerBlock = document.createElement('div');
  footerBlock.className = 'sn-footer-block';
  footerBlock.innerHTML = buildChNav() +
    '<p style="text-align:center;margin-top:14px">' + buildBackTop() + '</p>';
  container.appendChild(footerBlock);

  /* ── Signature auteur ────────────────────────────────────────────── */
  var authorFooter = document.createElement('footer');
  authorFooter.className = 'sn-author';
  authorFooter.innerHTML = 'Na\u00efm Azzouz';
  container.appendChild(authorFooter);

  /* ── Comportement du bouton retour en haut ─────────────────────────── */
  var btn = document.getElementById('sn-back-top');
  if (btn) {
    window.addEventListener('scroll', function () {
      var show = window.scrollY > 400;
      btn.style.opacity       = show ? '1'    : '0';
      btn.style.pointerEvents = show ? 'auto' : 'none';
    }, { passive: true });
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ── Chargement de nav.css ─────────────────────────────────────────── */
  injectCss();

  /* (toggle défini en début de fichier, hors IIFE) */

})();

/* ── GoatCounter — Statistiques de visites ─────────────────────────── */
/* Créer un compte gratuit sur https://www.goatcounter.com              */
/* Remplacer VOTRE-IDENTIFIANT par votre code site (ex: maths-sciences) */
(function () {
  if (window.location.host.indexOf('github.io') === -1) return; // skip en local
  var s = document.createElement('script');
  s.async = true;
  s.dataset.goatcounter = 'https://maths-sciences.goatcounter.com/count';
  s.src = '//gc.zgo.at/count.js';
  document.head.appendChild(s);
})();
