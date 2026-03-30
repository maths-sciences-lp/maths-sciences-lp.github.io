/**
 * features.js — Fonctionnalités UX du site
 * - Barre de recherche globale (Ctrl+K)
 * - Mode sombre (toggle + localStorage)
 * - Progression élève (exercices cochés en localStorage)
 */
(function () {
  'use strict';

  /* ══════════════════════════════════════════════════════════════════
     1. BASE DE DONNÉES DE RECHERCHE
     ══════════════════════════════════════════════════════════════════ */
  var PAGES = [
    {t:'Proportionnalité et pourcentages',s:'Maths 2nde · Ch01',u:'/maths/seconde/ch01/lecon.html'},
    {t:'Statistiques à une variable',s:'Maths 2nde · Ch02',u:'/maths/seconde/ch02/lecon.html'},
    {t:'Indicateurs statistiques',s:'Maths 2nde · Ch03',u:'/maths/seconde/ch03/lecon.html'},
    {t:'Probabilités et fluctuation',s:'Maths 2nde · Ch04',u:'/maths/seconde/ch04/lecon.html'},
    {t:'Équations du premier degré',s:'Maths 2nde · Ch05',u:'/maths/seconde/ch05/lecon.html'},
    {t:'Inéquations du premier degré',s:'Maths 2nde · Ch06',u:'/maths/seconde/ch06/lecon.html'},
    {t:'Notion de fonction',s:'Maths 2nde · Ch07',u:'/maths/seconde/ch07/lecon.html'},
    {t:'Fonction linéaire',s:'Maths 2nde · Ch08',u:'/maths/seconde/ch08/lecon.html'},
    {t:'Fonction affine',s:'Maths 2nde · Ch09',u:'/maths/seconde/ch09/lecon.html'},
    {t:'Fonction carré et variations',s:'Maths 2nde · Ch10',u:'/maths/seconde/ch10/lecon.html'},
    {t:'Figures planes : périmètres et aires',s:'Maths 2nde · Ch11',u:'/maths/seconde/ch11/lecon.html'},
    {t:'Théorème de Pythagore',s:'Maths 2nde · Ch12',u:'/maths/seconde/ch12/lecon.html'},
    {t:'Théorème de Thalès',s:'Maths 2nde · Ch13',u:'/maths/seconde/ch13/lecon.html'},
    {t:'Solides, volumes et agrandissement',s:'Maths 2nde · Ch14',u:'/maths/seconde/ch14/lecon.html'},
    {t:'Suites numériques',s:'Maths 1ère · Ch01',u:'/maths/premiere/ch01/lecon.html'},
    {t:'Fonctions de référence',s:'Maths 1ère · Ch02',u:'/maths/premiere/ch02/lecon.html'},
    {t:'Statistiques à deux variables',s:'Maths 1ère · Ch03',u:'/maths/premiere/ch03/lecon.html'},
    {t:'Probabilités conditionnelles',s:'Maths 1ère · Ch04',u:'/maths/premiere/ch04/lecon.html'},
    {t:'Dérivation',s:'Maths 1ère · Ch05',u:'/maths/premiere/ch05/lecon.html'},
    {t:'Fonction dérivée',s:'Maths 1ère · Ch06',u:'/maths/premiere/ch06/lecon.html'},
    {t:'Géométrie du plan',s:'Maths 1ère · Ch07',u:'/maths/premiere/ch07/lecon.html'},
    {t:'Polynômes du second degré',s:'Maths 1ère · Ch08',u:'/maths/premiere/ch08/lecon.html'},
    {t:'Calculs commerciaux',s:'Maths 1ère · Ch09',u:'/maths/premiere/ch09/lecon.html'},
    {t:'Suites arithmétiques et géométriques',s:'Maths Term · Ch01',u:'/maths/terminale/ch01/lecon.html'},
    {t:'Fonctions exponentielles et logarithme',s:'Maths Term · Ch02',u:'/maths/terminale/ch02/lecon.html'},
    {t:'Polynômes de degré 3',s:'Maths Term · Ch04',u:'/maths/terminale/ch04/lecon.html'},
    {t:'Calcul intégral',s:'Maths Term · Ch05',u:'/maths/terminale/ch05/lecon.html'},
    {t:'Probabilités et loi binomiale',s:'Maths Term · Ch06',u:'/maths/terminale/ch06/lecon.html'},
    {t:'Vecteurs dans le plan',s:'Maths Term · Ch07',u:'/maths/terminale/ch07/lecon.html'},
    {t:'Vecteurs dans l\'espace',s:'Maths Term · Ch08',u:'/maths/terminale/ch08/lecon.html'},
    {t:'Sécurité en laboratoire',s:'PC 2nde · Ch01',u:'/physique-chimie/seconde/ch01/lecon.html'},
    {t:'Grandeurs électriques et circuits',s:'PC 2nde · Ch02',u:'/physique-chimie/seconde/ch02/lecon.html'},
    {t:'Loi d\'Ohm',s:'PC 2nde · Ch03',u:'/physique-chimie/seconde/ch03/lecon.html'},
    {t:'Signal alternatif sinusoïdal',s:'PC 2nde · Ch04',u:'/physique-chimie/seconde/ch04/lecon.html'},
    {t:'Mouvement et trajectoire',s:'PC 2nde · Ch05',u:'/physique-chimie/seconde/ch05/lecon.html'},
    {t:'Forces et équilibre',s:'PC 2nde · Ch06',u:'/physique-chimie/seconde/ch06/lecon.html'},
    {t:'Structure de la matière',s:'PC 2nde · Ch07',u:'/physique-chimie/seconde/ch07/lecon.html'},
    {t:'Solutions chimiques et concentration',s:'PC 2nde · Ch08',u:'/physique-chimie/seconde/ch08/lecon.html'},
    {t:'Caractéristiques du son',s:'PC 2nde · Ch09',u:'/physique-chimie/seconde/ch09/lecon.html'},
    {t:'Température et capteurs',s:'PC 2nde · Ch10',u:'/physique-chimie/seconde/ch10/lecon.html'},
    {t:'Transferts thermiques',s:'PC 2nde · Ch11',u:'/physique-chimie/seconde/ch11/lecon.html'},
    {t:'Changements d\'état',s:'PC 2nde · Ch12',u:'/physique-chimie/seconde/ch12/lecon.html'},
    {t:'Réflexion et réfraction',s:'PC 2nde · Ch13',u:'/physique-chimie/seconde/ch13/lecon.html'},
    {t:'Lumière et couleurs',s:'PC 2nde · Ch14',u:'/physique-chimie/seconde/ch14/lecon.html'},
    {t:'Puissance consommée',s:'PC Term ICCER · Ch01',u:'/physique-chimie/terminale-iccer/ch01/lecon.html'},
    {t:'Courant continu et alternatif',s:'PC Term ICCER · Ch02',u:'/physique-chimie/terminale-iccer/ch02/lecon.html'},
    {t:'Moteur électrique',s:'PC Term ICCER · Ch03',u:'/physique-chimie/terminale-iccer/ch03/lecon.html'},
    {t:'Rayonnement thermique',s:'PC Term ICCER · Ch04',u:'/physique-chimie/terminale-iccer/ch04/lecon.html'},
    {t:'Pression dans un fluide',s:'PC Term ICCER · Ch05',u:'/physique-chimie/terminale-iccer/ch05/lecon.html'},
    {t:'Débit et transport de fluide',s:'PC Term ICCER · Ch06',u:'/physique-chimie/terminale-iccer/ch06/lecon.html'},
    {t:'Oxydoréduction et corrosion',s:'PC Term ICCER · Ch07',u:'/physique-chimie/terminale-iccer/ch07/lecon.html'},
    {t:'Signal sonore',s:'PC Term ICCER · Ch08',u:'/physique-chimie/terminale-iccer/ch08/lecon.html'},
    {t:'Transporter l\'énergie électrique',s:'PC Term ERA · Ch01',u:'/physique-chimie/terminale-era/ch01/lecon.html'},
    {t:'Stockage électrochimique',s:'PC Term ERA · Ch02',u:'/physique-chimie/terminale-era/ch02/lecon.html'},
    {t:'Atténuation d\'une onde sonore',s:'PC Term ERA · Ch08',u:'/physique-chimie/terminale-era/ch08/lecon.html'},
    {t:'Simulations interactives',s:'Outils',u:'/simulations.html'},
    {t:'Automatismes',s:'Outils',u:'/automatismes/index.html'},
    {t:'Groupements PC',s:'Outils',u:'/groupements.html'}
  ];

  /* ══════════════════════════════════════════════════════════════════
     2. BARRE DE RECHERCHE (Ctrl+K / Cmd+K)
     ══════════════════════════════════════════════════════════════════ */
  var ov = document.createElement('div');
  ov.id = 'ft-search';
  ov.innerHTML = '<div id="ft-box"><input id="ft-input" type="text" placeholder="Rechercher un chapitre, une notion... (Échap pour fermer)" autocomplete="off"><div id="ft-results"></div></div>';
  document.body.appendChild(ov);

  var sc = document.createElement('style');
  sc.textContent =
    '#ft-search{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:9999;justify-content:center;align-items:flex-start;padding-top:15vh}' +
    '#ft-search.open{display:flex}' +
    '#ft-box{background:#fff;border-radius:12px;width:90%;max-width:560px;box-shadow:0 20px 60px rgba(0,0,0,.3);overflow:hidden}' +
    '#ft-input{width:100%;padding:16px 20px;border:none;font-size:1.05rem;outline:none;font-family:inherit}' +
    '#ft-results{max-height:50vh;overflow-y:auto}' +
    '#ft-results a{display:block;padding:12px 20px;text-decoration:none;color:#1e293b;border-top:1px solid #f1f5f9;transition:background .1s}' +
    '#ft-results a:hover,#ft-results a.act{background:#eff6ff}' +
    '#ft-results .rt{font-weight:600;font-size:.95rem}' +
    '#ft-results .rs{font-size:.78rem;color:#64748b;margin-top:2px}' +
    '#ft-results .re{padding:20px;text-align:center;color:#94a3b8;font-size:.9rem}' +
    'body.dark #ft-box{background:#1e293b}body.dark #ft-input{background:#1e293b;color:#e2e8f0}' +
    'body.dark #ft-results a{color:#e2e8f0;border-color:#334155}body.dark #ft-results a:hover{background:#334155}';
  document.head.appendChild(sc);

  var inp = document.getElementById('ft-input');
  var res = document.getElementById('ft-results');
  var aidx = -1;

  function openS() { ov.classList.add('open'); inp.value = ''; res.innerHTML = ''; aidx = -1; setTimeout(function () { inp.focus(); }, 50); }
  function closeS() { ov.classList.remove('open'); }
  function norm(s) { return s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }

  function doSearch(q) {
    if (!q) { res.innerHTML = ''; aidx = -1; return; }
    var n = norm(q);
    var f = PAGES.filter(function (p) { return norm(p.t).indexOf(n) !== -1 || norm(p.s).indexOf(n) !== -1; }).slice(0, 8);
    if (!f.length) { res.innerHTML = '<div class="re">Aucun résultat pour « ' + q + ' »</div>'; aidx = -1; return; }
    res.innerHTML = f.map(function (p) { return '<a href="' + p.u + '"><div class="rt">' + p.t + '</div><div class="rs">' + p.s + '</div></a>'; }).join('');
    aidx = -1;
  }

  inp.addEventListener('input', function () { doSearch(this.value); });
  inp.addEventListener('keydown', function (e) {
    var lk = res.querySelectorAll('a');
    if (e.key === 'ArrowDown') { e.preventDefault(); aidx = Math.min(aidx + 1, lk.length - 1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); aidx = Math.max(aidx - 1, 0); }
    else if (e.key === 'Enter' && aidx >= 0 && lk[aidx]) { e.preventDefault(); lk[aidx].click(); return; }
    else if (e.key === 'Escape') { closeS(); return; }
    lk.forEach(function (l, i) { l.classList.toggle('act', i === aidx); });
  });
  ov.addEventListener('click', function (e) { if (e.target === ov) closeS(); });
  document.addEventListener('keydown', function (e) { if ((e.ctrlKey || e.metaKey) && e.key === 'k') { e.preventDefault(); openS(); } });

  var sb = document.createElement('button');
  sb.id = 'ft-sbtn'; sb.innerHTML = '🔍'; sb.title = 'Rechercher (Ctrl+K)';
  sb.addEventListener('click', openS);
  document.body.appendChild(sb);

  var sbc = document.createElement('style');
  sbc.textContent = '#ft-sbtn{position:fixed;bottom:70px;right:20px;width:48px;height:48px;border-radius:50%;border:none;background:#2563eb;color:#fff;font-size:1.3rem;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.2);z-index:999;transition:transform .2s}#ft-sbtn:hover{transform:scale(1.1)}body.dark #ft-sbtn{background:#7c3aed}';
  document.head.appendChild(sbc);

  /* ══════════════════════════════════════════════════════════════════
     3. MODE SOMBRE
     ══════════════════════════════════════════════════════════════════ */
  var dk = localStorage.getItem('ms-dark') === 'true';
  var dcs = document.createElement('style');
  dcs.textContent =
    'body.dark{background:#0f172a!important;color:#e2e8f0!important}' +
    'body.dark .c{background:#0f172a}body.dark header{background:#1e293b!important}' +
    'body.dark .def,.dark .prop,.dark .meth,.dark .att,.dark .retenir,.dark .formule-box,.dark .exo,.dark .situation{background:#1e293b!important;border-color:#334155!important;color:#e2e8f0!important}' +
    'body.dark .corr{background:#1a2e1a!important;border-color:#2d5a2d!important;color:#d1fae5!important}' +
    'body.dark h1,.dark h2,.dark h3{color:#93c5fd!important}body.dark a{color:#93c5fd}' +
    'body.dark .bc{background:#475569!important;color:#e2e8f0!important}' +
    'body.dark table,.dark th,.dark td{border-color:#334155!important;color:#e2e8f0!important}body.dark th{background:#1e293b!important}' +
    'body.dark input,.dark select,.dark textarea{background:#1e293b;color:#e2e8f0;border-color:#475569}' +
    'body.dark .controls,.dark .results,.dark .card{background:#1e293b!important;border-color:#334155!important}';
  document.head.appendChild(dcs);

  function setDark(on) {
    document.body.classList.toggle('dark', on);
    localStorage.setItem('ms-dark', on ? 'true' : 'false');
    dk = on;
    if (db) db.innerHTML = on ? '☀️' : '🌙';
  }
  if (dk) setDark(true);

  var db = document.createElement('button');
  db.id = 'ft-dark'; db.innerHTML = dk ? '☀️' : '🌙'; db.title = 'Mode sombre';
  db.addEventListener('click', function () { setDark(!dk); });
  document.body.appendChild(db);

  var dbc = document.createElement('style');
  dbc.textContent = '#ft-dark{position:fixed;bottom:130px;right:20px;width:48px;height:48px;border-radius:50%;border:none;background:#f1f5f9;font-size:1.3rem;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.15);z-index:999;transition:transform .2s}#ft-dark:hover{transform:scale(1.1)}body.dark #ft-dark{background:#334155}';
  document.head.appendChild(dbc);

  /* ══════════════════════════════════════════════════════════════════
     4. PROGRESSION ÉLÈVE (localStorage)
     ══════════════════════════════════════════════════════════════════ */
  var pk = 'ms-progress';
  function getP() { try { return JSON.parse(localStorage.getItem(pk) || '{}'); } catch (e) { return {}; } }
  function setP(d) { localStorage.setItem(pk, JSON.stringify(d)); }

  var exos = document.querySelectorAll('.exo');
  if (exos.length > 0) {
    var pid = window.location.pathname;
    var prog = getP();
    var pp = prog[pid] || {};

    exos.forEach(function (exo, i) {
      var k = 'e' + i;
      var cb = document.createElement('input');
      cb.type = 'checkbox'; cb.checked = pp[k] === true;
      cb.className = 'ft-cb'; cb.title = pp[k] ? 'Exercice fait ✓' : 'Cocher quand terminé';
      cb.addEventListener('change', function () {
        var p = getP(); if (!p[pid]) p[pid] = {};
        p[pid][k] = this.checked; setP(p); upd();
      });
      exo.style.position = 'relative';
      exo.insertBefore(cb, exo.firstChild);
    });

    var ctr = document.createElement('div');
    ctr.id = 'ft-ctr';
    document.body.appendChild(ctr);

    function upd() {
      var p = getP(); var pp2 = p[pid] || {}; var d = 0;
      exos.forEach(function (_, i) { if (pp2['e' + i]) d++; });
      var pct = Math.round(d / exos.length * 100);
      ctr.innerHTML = '✅ ' + d + '/' + exos.length + ' <span style="font-size:.75em;opacity:.7">(' + pct + '%)</span>';
      ctr.style.background = pct === 100 ? '#16a34a' : '#2563eb';
    }
    upd();

    var cc = document.createElement('style');
    cc.textContent = '#ft-ctr{position:fixed;bottom:20px;right:20px;padding:8px 16px;border-radius:20px;background:#2563eb;color:#fff;font-size:.85rem;font-weight:700;box-shadow:0 4px 12px rgba(0,0,0,.2);z-index:999}.ft-cb{position:absolute;top:8px;right:8px;width:20px;height:20px;cursor:pointer;accent-color:#16a34a;z-index:10}@media print{#ft-ctr,.ft-cb,#ft-sbtn,#ft-dark{display:none!important}}';
    document.head.appendChild(cc);
  }
})();
