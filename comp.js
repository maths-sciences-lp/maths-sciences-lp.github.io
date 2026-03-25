/**
 * comp.js — Filtrage des exercices par capacité du programme
 * Utilisé sur les pages exercices-capacites.html
 *
 * Usage :
 *   <button class="btn-cap active" data-filtre="toutes">Toutes</button>
 *   <button class="btn-cap" data-filtre="C1">Calculer une image</button>
 *   <div class="exo" data-cap="C1">...</div>
 *
 * Le système masque les sections entières (.cap-section) dont le data-cap
 * ne correspond pas au filtre sélectionné.
 * En impression, seules les sections visibles sont imprimées.
 */

(function () {
  'use strict';

  function initCompFilter() {
    var buttons = document.querySelectorAll('.btn-cap');
    if (!buttons.length) return;

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var filtre = btn.dataset.filtre;

        // Mettre à jour le bouton actif
        buttons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');

        // Filtrer les sections de capacité
        var sections = document.querySelectorAll('.cap-section');
        sections.forEach(function (section) {
          if (filtre === 'toutes' || section.dataset.cap === filtre) {
            section.style.display = '';
          } else {
            section.style.display = 'none';
          }
        });

        // Mettre à jour le titre de la capacité active affichée
        var label = document.getElementById('cap-active-label');
        if (label) {
          if (filtre === 'toutes') {
            label.textContent = '';
          } else {
            label.textContent = btn.textContent;
          }
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCompFilter);
  } else {
    initCompFilter();
  }
})();
