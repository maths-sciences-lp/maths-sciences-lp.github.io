/**
 * sujet.js — Toggle Sujet A / Sujet B pour les interrogations
 *
 * UTILISATION : ajouter avant </body> sur les pages interro.html :
 *   <script src="../../../sujet.js"></script>
 *
 * Le script :
 *  1. Détecte si la page contient des blocs .sujet-a et .sujet-b
 *  2. Si oui, injecte un toggle segmenté (boutons A | B) après le diff-toggle ou le header
 *  3. Mémorise le choix en localStorage (persistant entre les pages)
 *  4. Masque le sujet non sélectionné (compatible impression)
 *
 * Sans blocs .sujet-a/.sujet-b, le script ne fait rien.
 */
(function () {
  'use strict';

  var KEY = 'sujet-mode';

  // Ne rien faire si aucun bloc sujet n'existe
  if (!document.querySelector('.sujet-a') || !document.querySelector('.sujet-b')) return;

  // Mode sauvegardé ou "a" par défaut
  var current = localStorage.getItem(KEY) || 'a';
  applyMode(current);

  // Créer le toggle
  var wrapper = document.createElement('div');
  wrapper.className = 'sujet-toggle';

  var btnA = document.createElement('button');
  btnA.textContent = 'Sujet A';
  btnA.addEventListener('click', function () { setMode('a'); });

  var btnB = document.createElement('button');
  btnB.textContent = 'Sujet B';
  btnB.addEventListener('click', function () { setMode('b'); });

  wrapper.appendChild(btnA);
  wrapper.appendChild(btnB);

  updateActive(current);

  // Injecter après le diff-toggle s'il existe, sinon après le header
  var container = document.querySelector('.c');
  if (container) {
    var diffToggle = container.querySelector('.diff-toggle');
    var header = container.querySelector('header');
    var ref = diffToggle || header;
    if (ref && ref.nextSibling) {
      container.insertBefore(wrapper, ref.nextSibling);
    } else {
      container.insertBefore(wrapper, container.firstChild);
    }
  }

  function setMode(mode) {
    localStorage.setItem(KEY, mode);
    applyMode(mode);
    updateActive(mode);
  }

  function applyMode(mode) {
    document.body.classList.toggle('show-sujet-a', mode === 'a');
    document.body.classList.toggle('show-sujet-b', mode === 'b');
  }

  function updateActive(mode) {
    btnA.classList.toggle('active', mode === 'a');
    btnB.classList.toggle('active', mode === 'b');
  }
})();
