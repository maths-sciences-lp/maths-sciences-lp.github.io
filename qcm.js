/* ============================================================
   qcm.js — Fonctions partagées pour les QCM interactifs
   maths-sciences-lp.github.io
   ============================================================ */

/**
 * Corrige un QCM : colorie les bonnes/mauvaises réponses,
 * affiche les explications et calcule le score.
 *
 * Chaque page QCM doit définir un objet global `explications`
 * dont les clés correspondent aux attributs `name` des radios.
 *
 * @param {string} formId  – id du <form> contenant les .q-block
 * @param {string} scoreId – id du <div class="score-box">
 */
function corriger(formId, scoreId) {
  var form = document.getElementById(formId);
  var blocks = form.querySelectorAll('.q-block');
  var score = 0;
  var total = blocks.length;
  var expls = (typeof explications !== 'undefined') ? explications : {};

  blocks.forEach(function (block) {
    var radios = block.querySelectorAll('input[type="radio"]');
    var qName = radios.length > 0 ? radios[0].name : '';
    var correct = block.getAttribute('data-correct');
    var selected = block.querySelector('input[type="radio"]:checked');
    var feedback = block.querySelector('.q-feedback');
    var labels = block.querySelectorAll('.options label');

    labels.forEach(function (l) { l.classList.remove('correct', 'incorrect'); });

    labels.forEach(function (l) {
      var input = l.querySelector('input');
      if (input.value === correct) l.classList.add('correct');
    });

    if (selected) {
      if (selected.value === correct) {
        score++;
        feedback.className = 'q-feedback ok';
        feedback.textContent = '\u2705 Bonne r\u00e9ponse\u00a0! ' + (expls[qName] || '');
      } else {
        selected.parentElement.classList.add('incorrect');
        feedback.className = 'q-feedback ko';
        feedback.textContent = '\u274c Mauvaise r\u00e9ponse. ' + (expls[qName] || '');
      }
    } else {
      feedback.className = 'q-feedback ko';
      feedback.textContent = '\u26a0\ufe0f Pas de r\u00e9ponse. ' + (expls[qName] || '');
    }
  });

  var scoreBox = document.getElementById(scoreId);
  var pct = Math.round(score / total * 100);
  scoreBox.textContent = 'Score\u00a0: ' + score + ' / ' + total + ' (' + pct + '\u00a0%)';
  scoreBox.className = 'score-box show ' + (pct >= 70 ? 'score-good' : pct >= 40 ? 'score-avg' : 'score-low');
  scoreBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/**
 * Réinitialise un QCM : décoche tout, efface les couleurs et le score.
 *
 * @param {string} formId  – id du <form>
 * @param {string} scoreId – id du <div class="score-box">
 */
function reinitialiser(formId, scoreId) {
  var form = document.getElementById(formId);
  form.querySelectorAll('.q-block').forEach(function (block) {
    block.querySelectorAll('.options label').forEach(function (l) { l.classList.remove('correct', 'incorrect'); });
    block.querySelectorAll('input[type="radio"]').forEach(function (r) { r.checked = false; });
    var feedback = block.querySelector('.q-feedback');
    feedback.className = 'q-feedback';
    feedback.textContent = '';
  });
  var scoreBox = document.getElementById(scoreId);
  scoreBox.className = 'score-box';
  scoreBox.textContent = '';
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
