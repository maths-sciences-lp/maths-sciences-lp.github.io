/**
 * features.js — Fonctionnalités UX du site
 * - Mode sombre (toggle + localStorage)
 */
(function () {
  'use strict';

  /* ══════════════════════════════════════════════════════════════════
     MODE SOMBRE
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
  dbc.textContent = '#ft-dark{position:fixed;bottom:20px;right:20px;width:48px;height:48px;border-radius:50%;border:none;background:#f1f5f9;font-size:1.3rem;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.15);z-index:999;transition:transform .2s}#ft-dark:hover{transform:scale(1.1)}body.dark #ft-dark{background:#334155}@media print{#ft-dark{display:none!important}}';
  document.head.appendChild(dbc);
})();
