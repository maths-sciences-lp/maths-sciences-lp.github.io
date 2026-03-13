/**
 * diff.js — Différenciation pédagogique (socle / standard / approfondissement)
 *
 * UTILISATION : ajouter avant </body> sur les pages différenciées :
 *   <script src="../../../diff.js"></script>
 *
 * Le script :
 *  1. Détecte si la page contient des blocs .diff-socle, .diff-standard ou .diff-appro
 *  2. Si oui, injecte un toggle en haut du conteneur .c
 *  3. Mémorise le choix en localStorage (persistant entre les pages)
 *  4. Applique la classe body.mode-socle, body.mode-standard ou body.mode-appro
 *
 * Sans blocs différenciés, le script ne fait rien.
 */
(function () {
  'use strict';

  var KEY = 'diff-mode';
  var MODES = {
    socle:    { label: 'Socle',              cls: 'mode-socle' },
    standard: { label: 'Standard',           cls: 'mode-standard' },
    appro:    { label: 'Approfondissement',  cls: 'mode-appro' }
  };
  var ORDER = ['socle', 'standard', 'appro'];

  // Ne rien faire si aucun bloc différencié n'existe sur la page
  if (!document.querySelector('.diff-socle, .diff-standard, .diff-appro')) return;

  // Mode sauvegardé ou "tous" par défaut (rien masqué)
  var saved = localStorage.getItem(KEY);
  if (saved && MODES[saved]) {
    applyMode(saved);
  }

  // Créer le toggle
  var wrapper = document.createElement('div');
  wrapper.className = 'diff-toggle';

  var buttons = {};
  ORDER.forEach(function (mode) {
    var btn = document.createElement('button');
    btn.textContent = MODES[mode].label;
    btn.addEventListener('click', function () { setMode(mode); });
    buttons[mode] = btn;
    wrapper.appendChild(btn);
  });

  var btnAll = document.createElement('button');
  btnAll.textContent = 'Tout voir';
  btnAll.addEventListener('click', function () { setMode(null); });
  wrapper.appendChild(btnAll);

  updateActive(saved);

  // Injecter après le header (ou en début de .c)
  var container = document.querySelector('.c');
  if (container) {
    var header = container.querySelector('header');
    if (header && header.nextSibling) {
      container.insertBefore(wrapper, header.nextSibling);
    } else {
      container.insertBefore(wrapper, container.firstChild);
    }
  }

  function setMode(mode) {
    if (mode) {
      localStorage.setItem(KEY, mode);
    } else {
      localStorage.removeItem(KEY);
    }
    applyMode(mode);
    updateActive(mode);
  }

  function applyMode(mode) {
    ORDER.forEach(function (m) {
      document.body.classList.remove(MODES[m].cls);
    });
    if (mode && MODES[mode]) {
      document.body.classList.add(MODES[mode].cls);
    }
  }

  function updateActive(mode) {
    ORDER.forEach(function (m) {
      buttons[m].classList.toggle('active', mode === m);
    });
    btnAll.classList.toggle('active', !mode);
  }
})();
