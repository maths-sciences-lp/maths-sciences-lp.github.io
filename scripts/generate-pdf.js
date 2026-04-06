#!/usr/bin/env -S NODE_PATH=/opt/node22/lib/node_modules node
/**
 * generate-pdf.js — Génération de PDF imprimables depuis les pages du site
 *
 * Usage (fichier unique) :
 *   node scripts/generate-pdf.js <chemin-html> [--output <fichier.pdf>] [--no-corrections]
 *
 * Usage (batch) :
 *   node scripts/generate-pdf.js --all [--section <dossier>] [--type <types>] [--concurrency <n>] [--no-corrections]
 *
 * Exemples :
 *   node scripts/generate-pdf.js maths/seconde/ch01/lecon.html
 *   node scripts/generate-pdf.js maths/seconde/ch01/exercices.html --no-corrections -o exercices-ch01.pdf
 *   node scripts/generate-pdf.js --all --type lecon
 *   node scripts/generate-pdf.js --all --section maths/seconde --type lecon,exercices --concurrency 4
 *
 * Types disponibles : lecon, exercices, ds, fiche, qcm, interro, activite (défaut : lecon)
 *
 * Dépendances : playwright (npm install -g playwright)
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const http = require('http');

// ── Lecture des arguments ──
const args = process.argv.slice(2);

if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
  console.log(`
╔══════════════════════════════════════════════════════╗
║       Générateur de PDF — Maths & Sciences LP        ║
╚══════════════════════════════════════════════════════╝

Usage (fichier unique) :
  node scripts/generate-pdf.js <chemin-html> [options]

Usage (batch) :
  node scripts/generate-pdf.js --all [options]

Options communes :
  --no-corrections         Masquer les corrections dans le PDF
  --help, -h               Afficher cette aide

Options fichier unique :
  --output, -o <fichier>   Nom du fichier PDF de sortie

Options batch :
  --all                    Générer tous les PDF correspondant aux filtres
  --section <dossier>      Limiter à un sous-dossier (ex: maths/seconde)
  --type <types>           Types de pages séparés par virgule
                           (lecon, exercices, ds, fiche, qcm, interro, activite)
                           Défaut : lecon
  --concurrency <n>        Nombre de pages traitées en parallèle (défaut : 3)

Exemples :
  node scripts/generate-pdf.js maths/seconde/ch01/lecon.html
  node scripts/generate-pdf.js maths/seconde/ch01/exercices.html --no-corrections -o ex-ch01.pdf
  node scripts/generate-pdf.js --all --type lecon
  node scripts/generate-pdf.js --all --section maths/seconde --type lecon,exercices --concurrency 4
  node scripts/generate-pdf.js --all --section physique-chimie/terminale-iccer --type lecon,ds
`);
  process.exit(0);
}

const rootDir = path.resolve(__dirname, '..');

// ── Paramètres ──
const batchMode    = args.includes('--all');
const showCorrections = !args.includes('--no-corrections');

let htmlPath    = null;
let outputPath  = null;
let section     = null;
let types       = ['lecon'];
let concurrency = 3;

for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === '--output' || a === '-o') { outputPath  = args[++i]; }
  else if (a === '--section')         { section     = args[++i]; }
  else if (a === '--type')            { types       = args[++i].split(',').map(s => s.trim()); }
  else if (a === '--concurrency')     { concurrency = parseInt(args[++i], 10) || 3; }
  else if (!a.startsWith('--') && !batchMode) { htmlPath = a; }
}

// ── CSS d'impression ──
const printCssPath = path.join(rootDir, 'print.css');
const printCssRaw  = fs.existsSync(printCssPath) ? fs.readFileSync(printCssPath, 'utf8') : '';

// Extraire proprement le contenu du bloc @media print { ... }
function extractPrintCss(css) {
  const start = css.indexOf('@media print');
  if (start === -1) return css;
  const open = css.indexOf('{', start);
  if (open === -1) return '';
  // Trouver l'accolade fermante correspondante
  let depth = 1;
  let i = open + 1;
  while (i < css.length && depth > 0) {
    if (css[i] === '{') depth++;
    else if (css[i] === '}') depth--;
    i++;
  }
  return css.slice(open + 1, i - 1);
}

const printCssContent = extractPrintCss(printCssRaw);

// ── Serveur HTTP local ──
function createServer() {
  return new Promise((resolve) => {
    const mimeTypes = {
      '.html': 'text/html',
      '.css':  'text/css',
      '.js':   'application/javascript',
      '.json': 'application/json',
      '.png':  'image/png',
      '.jpg':  'image/jpeg',
      '.svg':  'image/svg+xml',
      '.woff2':'font/woff2',
      '.woff': 'font/woff',
      '.ttf':  'font/ttf',
    };

    const server = http.createServer((req, res) => {
      let filePath = path.join(rootDir, decodeURIComponent(req.url.split('?')[0]));
      if (filePath.endsWith('/')) filePath += 'index.html';

      const ext         = path.extname(filePath).toLowerCase();
      const contentType = mimeTypes[ext] || 'application/octet-stream';

      fs.readFile(filePath, (err, data) => {
        if (err) { res.writeHead(404); res.end('Not found'); return; }
        res.writeHead(200, { 'Content-Type': contentType });
        res.end(data);
      });
    });

    server.listen(0, '127.0.0.1', () => {
      resolve({ server, port: server.address().port });
    });
  });
}

// ── Résoudre le chemin de sortie PDF ──
function resolvePdfOutput(relHtmlPath, customOutput) {
  if (customOutput) {
    return path.isAbsolute(customOutput)
      ? customOutput
      : path.resolve(process.cwd(), customOutput);
  }
  const parts  = relHtmlPath.replace(/\.html$/, '').split('/').filter(Boolean);
  const pdfDir = path.join(rootDir, 'pdf', 'generated');
  if (!fs.existsSync(pdfDir)) fs.mkdirSync(pdfDir, { recursive: true });
  return path.join(pdfDir, parts.join('-') + '.pdf');
}

// ── Générer un PDF depuis une page déjà ouverte ──
async function renderPage(page, url, relHtmlPath, out, showCorr) {
  await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });

  // Attendre MathJax
  try {
    await page.waitForFunction(() => {
      if (typeof MathJax !== 'undefined' && MathJax.startup) {
        return MathJax.startup.promise !== undefined;
      }
      return true;
    }, { timeout: 15000 });

    await page.evaluate(() => {
      if (typeof MathJax !== 'undefined' && MathJax.startup && MathJax.startup.promise) {
        return MathJax.startup.promise;
      }
    });
  } catch {
    // MathJax timeout — on continue
  }

  // Attendre Chart.js
  await page.waitForTimeout(2000);

  // Canvas → image PNG
  await page.evaluate(() => {
    document.querySelectorAll('canvas').forEach((canvas) => {
      try {
        const dataUrl = canvas.toDataURL('image/png', 1.0);
        const img     = document.createElement('img');
        img.src       = dataUrl;
        img.style.cssText = 'max-width:100%;height:auto;display:block;margin:0 auto';
        canvas.parentNode.replaceChild(img, canvas);
      } catch { /* canvas tainted */ }
    });
  });

  // Styles d'impression
  await page.addStyleTag({ content: printCssContent });

  // Masquer navigation & interactivité
  await page.addStyleTag({
    content: `
      .sn-breadcrumb,.sn-ch-menu,.sn-ch-nav,.sn-back-top,.sn-toc,
      .nb,.nav-footer,.nav-bottom,.nav-links,.nav-btn,.nav-link,
      .nav-back,.nav-fwd,.bc,.bcq,.btn-corr,.flash-btn,
      .ctrl-vis,.slider-row,.anim-wrap button,.diff-toggle-wrap {
        display: none !important;
      }
      body { background:#fff; padding:0; margin:0; }
      .c,.container { max-width:100%; border:none; border-radius:0; box-shadow:none; padding:0; margin:0; }
    `,
  });

  // Corrections
  if (showCorr) {
    await page.addStyleTag({ content: `.corr,.correction,.qcm-corr,.flash-corr { display:block !important; }` });
  } else {
    await page.addStyleTag({ content: `.corr,.correction,.qcm-corr,.flash-corr,.corr-wrap,.corr-body,.corr-btn { display:none !important; }` });
  }

  await page.waitForTimeout(500);

  await page.pdf({
    path: out,
    format: 'A4',
    margin: { top: '18mm', right: '15mm', bottom: '20mm', left: '15mm' },
    printBackground: true,
    preferCSSPageSize: false,
    displayHeaderFooter: true,
    headerTemplate: `
      <div style="font-size:7pt;color:#999;width:100%;display:flex;justify-content:space-between;padding:0 15mm;">
        <span style="font-weight:600;">Maths &amp; Sciences LP</span>
        <span>Na\u00efm Azzouz</span>
      </div>`,
    footerTemplate: `
      <div style="font-size:7pt;color:#999;width:100%;display:flex;justify-content:space-between;padding:0 15mm;">
        <span>maths-sciences-lp.github.io</span>
        <span>Page <span class="pageNumber"></span> / <span class="totalPages"></span></span>
      </div>`,
  });
}

// ── Trouver les fichiers HTML à générer (mode batch) ──
function findHtmlFiles(searchRoot, targetTypes) {
  const results = [];

  function walk(dir) {
    let entries;
    try { entries = fs.readdirSync(dir, { withFileTypes: true }); }
    catch { return; }

    for (const entry of entries) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        // Ne pas descendre dans pdf/, scripts/, .git/, simulations/ (pas de chapitres)
        if (['pdf', 'scripts', '.git', 'node_modules', 'prompts', 'audits', '.claude'].includes(entry.name)) continue;
        walk(full);
      } else if (entry.isFile() && entry.name.endsWith('.html')) {
        const base = path.basename(entry.name, '.html');
        if (targetTypes.includes(base)) {
          results.push(path.relative(rootDir, full));
        }
      }
    }
  }

  walk(searchRoot);
  return results;
}

// ── Exécuter une queue avec concurrence limitée ──
async function runWithConcurrency(tasks, limit, worker) {
  const results = [];
  const queue   = [...tasks];
  let active    = 0;
  let idx       = 0;

  return new Promise((resolve) => {
    function next() {
      while (active < limit && idx < queue.length) {
        const task = queue[idx++];
        active++;
        worker(task, idx - 1, queue.length)
          .then((r) => { results.push(r); active--; next(); })
          .catch((e) => { results.push({ ...task, error: e.message }); active--; next(); });
      }
      if (active === 0) resolve(results);
    }
    next();
  });
}

// ── Point d'entrée ──
async function main() {
  const { server, port } = await createServer();

  let browser;
  try {
    browser = await chromium.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });

    // ── Mode fichier unique ──
    if (!batchMode) {
      if (!htmlPath) {
        console.error('Erreur : spécifier un fichier HTML ou utiliser --all');
        process.exit(1);
      }
      const absPath = path.resolve(rootDir, htmlPath);
      if (!fs.existsSync(absPath)) {
        console.error(`Erreur : fichier introuvable — ${absPath}`);
        process.exit(1);
      }
      const out = resolvePdfOutput(htmlPath, outputPath);
      const url = `http://127.0.0.1:${port}/${path.relative(rootDir, absPath)}`;

      console.log('🖨️  Génération du PDF...');
      console.log(`   Source : ${htmlPath}`);
      console.log(`   Sortie : ${out}`);
      if (!showCorrections) console.log('   Mode   : sans corrections');

      const page = await browser.newPage();
      await renderPage(page, url, htmlPath, out, showCorrections);
      await page.close();

      const size = (fs.statSync(out).size / 1024 / 1024).toFixed(2);
      console.log(`\n✅ PDF généré — ${out} (${size} Mo)`);
      return;
    }

    // ── Mode batch ──
    const searchRoot = section
      ? path.join(rootDir, section)
      : rootDir;

    if (!fs.existsSync(searchRoot)) {
      console.error(`Erreur : section introuvable — ${searchRoot}`);
      process.exit(1);
    }

    const files = findHtmlFiles(searchRoot, types);

    if (files.length === 0) {
      console.log(`Aucun fichier trouvé (types : ${types.join(', ')}${section ? `, section : ${section}` : ''}).`);
      return;
    }

    console.log(`\n╔══════════════════════════════════════════════════════╗`);
    console.log(`║       Génération PDF batch — Maths & Sciences LP     ║`);
    console.log(`╚══════════════════════════════════════════════════════╝`);
    console.log(`   Fichiers trouvés : ${files.length}`);
    console.log(`   Types            : ${types.join(', ')}`);
    if (section) console.log(`   Section          : ${section}`);
    console.log(`   Concurrence      : ${concurrency}`);
    console.log(`   Corrections      : ${showCorrections ? 'oui' : 'non'}\n`);

    const startTime = Date.now();
    const successes = [];
    const failures  = [];

    await runWithConcurrency(files, concurrency, async (relPath, doneIdx, total) => {
      const absPath = path.resolve(rootDir, relPath);
      const out     = resolvePdfOutput(relPath, null);
      const url     = `http://127.0.0.1:${port}/${relPath}`;
      const label   = `[${String(doneIdx + 1).padStart(String(total).length, ' ')}/${total}]`;

      try {
        const ctx  = await browser.newContext();
        const page = await ctx.newPage();
        await renderPage(page, url, relPath, out, showCorrections);
        await ctx.close();

        const size = (fs.statSync(out).size / 1024 / 1024).toFixed(2);
        console.log(`✅ ${label} ${relPath} (${size} Mo)`);
        successes.push({ relPath, out, size });
      } catch (err) {
        console.error(`❌ ${label} ${relPath} — ${err.message}`);
        failures.push({ relPath, error: err.message });
      }
    });

    const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);

    console.log(`\n${'─'.repeat(56)}`);
    console.log(`  Terminé en ${elapsed}s`);
    console.log(`  ✅ ${successes.length} PDF générés`);
    if (failures.length > 0) {
      console.log(`  ❌ ${failures.length} échecs :`);
      failures.forEach(f => console.log(`     • ${f.relPath} : ${f.error}`));
    }
    const totalSize = successes.reduce((s, f) => s + parseFloat(f.size), 0).toFixed(2);
    console.log(`  📦 Taille totale : ${totalSize} Mo`);
    console.log(`  📁 Dossier       : ${path.join(rootDir, 'pdf', 'generated')}`);

  } catch (err) {
    console.error('\n❌ Erreur fatale :', err.message);
    process.exit(1);
  } finally {
    if (browser) await browser.close();
    server.close();
  }
}

main();
