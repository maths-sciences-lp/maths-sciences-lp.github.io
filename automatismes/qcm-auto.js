/* ============================================================
   qcm-auto.js — Fonction partagée pour les QCM auto-corrigés
   des pages d'automatismes (feedback immédiat au clic).
   maths-sciences-lp.github.io
   ============================================================ */

/**
 * Corrige un bouton de QCM au clic : désactive les autres options,
 * applique la classe ok/ko et affiche l'explication dans le <p class="fb">
 * situé juste après le conteneur .qcm-opts.
 *
 * Utilisation dans le HTML :
 *   <button class="qo" onclick="qcm(this, true,  'Explication...')">A) Réponse</button>
 *   <button class="qo" onclick="qcm(this, false, '')">B) Mauvaise</button>
 *
 * @param {HTMLButtonElement} btn  – bouton cliqué
 * @param {boolean}           ok   – true si la réponse est correcte
 * @param {string}            expl – explication à afficher (optionnelle)
 */
function qcm(btn, ok, expl) {
  var opts = btn.closest('.qcm-opts');
  opts.querySelectorAll('.qo').forEach(function (b) { b.disabled = true; });
  var fb = opts.nextElementSibling;
  if (ok) {
    btn.classList.add('ok');
    fb.className = 'fb ok';
    fb.textContent = '\u2713 Correct ! ' + (expl || '');
  } else {
    btn.classList.add('ko');
    fb.className = 'fb ko';
    fb.textContent = '\u2717 Incorrect. ' + (expl || '');
  }
}
