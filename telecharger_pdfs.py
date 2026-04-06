#!/usr/bin/env python3
"""
telecharger_pdfs.py — Génération batch de PDF depuis les pages HTML du site
Utilise Playwright (Python) + un serveur HTTP local.

Usage :
  python3 telecharger_pdfs.py                    # tous les chapitres
  python3 telecharger_pdfs.py --section maths/seconde
  python3 telecharger_pdfs.py --types lecon exercices
  python3 telecharger_pdfs.py --file maths/seconde/ch01/lecon.html
  python3 telecharger_pdfs.py --corrections       # inclure les corrections
  python3 telecharger_pdfs.py --dry-run           # afficher la liste sans générer
"""

import argparse
import glob
import http.server
import os
import re
import sys
import threading
import time
import unicodedata
from pathlib import Path

# ── Vérification Playwright ──────────────────────────────────
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("❌  Playwright non installé. Exécuter : pip3 install playwright && python3 -m playwright install chromium")
    sys.exit(1)

# ── Configuration ────────────────────────────────────────────
ROOT = Path(__file__).parent.resolve()
PDF_OUT = ROOT / "pdf" / "generated"

# Pages à générer par défaut (types de fichiers par chapitre)
DEFAULT_TYPES = ["lecon", "exercices", "ds", "fiche", "interro", "qcm",
                 "activite", "exercices-capacites", "simulation"]

# Sections à inclure par défaut
DEFAULT_SECTIONS = [
    "maths/seconde",
    "maths/premiere",
    "maths/terminale",
    "maths/lgt-terminale",
    "maths/cap",
    "maths/bts",
    "physique-chimie/seconde",
    "physique-chimie/premiere-iccer",
    "physique-chimie/premiere-era",
    "physique-chimie/premiere-gpt2",
    "physique-chimie/premiere-gpt4",
    "physique-chimie/premiere-gpt6",
    "physique-chimie/terminale-iccer",
    "physique-chimie/terminale-era",
    "physique-chimie/terminale-gpt2",
    "physique-chimie/terminale-gpt4",
    "physique-chimie/terminale-gpt5",
    "physique-chimie/cap",
]

# CSS injecté pour masquer la navigation et nettoyer pour l'impression
NAV_CSS = """
  .sn-breadcrumb, .sn-ch-menu, .sn-ch-nav, .sn-back-top, .sn-toc,
  .nb, .nav-footer, .nav-bottom, .nav-links, .nav-btn, .nav-link,
  .nav-back, .nav-fwd,
  .bc, .bcq, .btn-corr, .flash-btn,
  .ctrl-vis, .slider-row,
  .anim-wrap button { display: none !important; }
  body { background: #fff; padding: 0; margin: 0; }
  .c, .container {
    max-width: 100%; border: none; border-radius: 0;
    box-shadow: none; padding: 0; margin: 0;
  }
"""

CORR_SHOW_CSS = ".corr, .correction, .qcm-corr, .flash-corr { display: block !important; }"
CORR_HIDE_CSS = ".corr, .correction, .qcm-corr, .flash-corr { display: none !important; }"

HEADER_HTML = """
  <div style="font-size:7pt;color:#999;width:100%;display:flex;
              justify-content:space-between;padding:0 15mm;">
    <span style="font-weight:600;">Maths &amp; Sciences LP</span>
    <span>Naïm Azzouz</span>
  </div>
"""
FOOTER_HTML = """
  <div style="font-size:7pt;color:#999;width:100%;display:flex;
              justify-content:space-between;padding:0 15mm;">
    <span>maths-sciences-lp.github.io</span>
    <span>Page <span class="pageNumber"></span> / <span class="totalPages"></span></span>
  </div>
"""


# ── Utilitaires nommage ──────────────────────────────────────
def slugify(text: str) -> str:
    """Convertit un titre en slug ASCII minuscules avec tirets."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:50]


def get_chapter_title(html_path: Path) -> str:
    """Extrait le titre du chapitre depuis lecon.html du même dossier."""
    lecon = html_path.parent / "lecon.html"
    source = lecon if lecon.exists() else html_path
    try:
        content = source.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.DOTALL)
        if match:
            title = re.sub(r"<[^>]+>", "", match.group(1)).strip()
            # Supprimer le préfixe "Chapitre X –" ou "Ch X –"
            title = re.sub(r"^[Cc]hapitre\s+\w+\s*[–\-]\s*", "", title)
            title = re.sub(r"^[Cc]h\s*\w+\s*[–\-]\s*", "", title)
            return slugify(title)
    except Exception:
        pass
    return ""


# ── Serveur HTTP local ────────────────────────────────────────
class SilentHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass  # silencieux


def start_server(root: Path):
    os.chdir(root)
    server = http.server.HTTPServer(("127.0.0.1", 0), SilentHandler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, port


# ── Découverte des pages ──────────────────────────────────────
def discover_pages(sections: list[str], types: list[str]) -> list[Path]:
    pages = []
    for section in sections:
        section_path = ROOT / section
        if not section_path.exists():
            continue
        for ch_dir in sorted(section_path.glob("ch*")):
            if not ch_dir.is_dir():
                continue
            for t in types:
                p = ch_dir / f"{t}.html"
                if p.exists():
                    pages.append(p)
    return pages


def output_path(html_path: Path) -> Path:
    rel = html_path.relative_to(ROOT)
    # ex: maths/seconde/ch01/lecon.html -> maths-seconde/ch01/lecon.pdf
    parts = list(rel.parts)
    folder = "-".join(parts[:-2])   # maths-seconde ou physique-chimie-seconde
    ch = parts[-2]                  # ch01
    name = parts[-1].replace(".html", ".pdf")  # lecon.pdf
    return PDF_OUT / folder / ch / name


# ── CSS d'impression depuis print.css ────────────────────────
def load_print_css() -> str:
    css_path = ROOT / "print.css"
    if not css_path.exists():
        return ""
    raw = css_path.read_text(encoding="utf-8")
    # Extraire le contenu du @media print { ... }
    import re
    match = re.search(r'@media\s+print\s*\{(.+)\}\s*$', raw, re.DOTALL)
    if match:
        return match.group(1)
    return raw


# ── Génération d'un PDF ───────────────────────────────────────
def generate_pdf(page_obj, html_path: Path, out_path: Path,
                 port: int, show_corrections: bool, print_css: str) -> bool:
    rel = html_path.relative_to(ROOT)
    url = f"http://127.0.0.1:{port}/{rel.as_posix()}"

    try:
        page_obj.goto(url, wait_until="networkidle", timeout=60000)
    except Exception as e:
        print(f"     ⚠️  Impossible de charger : {e}")
        return False

    # Attendre MathJax
    try:
        page_obj.wait_for_function(
            """() => {
                if (typeof MathJax !== 'undefined' && MathJax.startup)
                    return MathJax.startup.promise !== undefined;
                return true;
            }""",
            timeout=15000,
        )
        page_obj.evaluate(
            """() => {
                if (typeof MathJax !== 'undefined' && MathJax.startup && MathJax.startup.promise)
                    return MathJax.startup.promise;
            }"""
        )
    except Exception:
        pass  # pas de MathJax ou timeout

    # Attendre Chart.js
    page_obj.wait_for_timeout(2000)

    # Convertir les <canvas> Chart.js en <img>
    page_obj.evaluate(
        """() => {
            document.querySelectorAll('canvas').forEach(canvas => {
                try {
                    const url = canvas.toDataURL('image/png', 1.0);
                    const img = document.createElement('img');
                    img.src = url;
                    img.style.cssText = 'max-width:100%;height:auto;display:block;margin:0 auto';
                    canvas.parentNode.replaceChild(img, canvas);
                } catch(e) {}
            });
        }"""
    )

    # Injecter les styles
    if print_css:
        page_obj.add_style_tag(content=print_css)
    page_obj.add_style_tag(content=NAV_CSS)
    page_obj.add_style_tag(content=CORR_SHOW_CSS if show_corrections else CORR_HIDE_CSS)

    page_obj.wait_for_timeout(300)

    out_path.parent.mkdir(parents=True, exist_ok=True)

    page_obj.pdf(
        path=str(out_path),
        format="A4",
        margin={"top": "18mm", "right": "15mm", "bottom": "20mm", "left": "15mm"},
        print_background=True,
        display_header_footer=True,
        header_template=HEADER_HTML,
        footer_template=FOOTER_HTML,
    )
    return True


# ── Main ──────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Génération batch de PDF depuis les pages HTML")
    parser.add_argument("--section", help="Limiter à une section (ex: maths/seconde)")
    parser.add_argument("--types", nargs="+", default=DEFAULT_TYPES,
                        help="Types de pages (lecon exercices ds fiche interro qcm)")
    parser.add_argument("--file", help="Générer un seul fichier HTML")
    parser.add_argument("--corrections", action="store_true",
                        help="Inclure les corrections dans le PDF")
    parser.add_argument("--dry-run", action="store_true",
                        help="Afficher la liste des pages sans générer")
    parser.add_argument("--output-dir", default=str(PDF_OUT),
                        help="Dossier de sortie (défaut: pdf/generated/)")
    args = parser.parse_args()

    pdf_out = Path(args.output_dir)

    # ── Construire la liste des pages ──
    if args.file:
        pages = [ROOT / args.file]
    else:
        sections = [args.section] if args.section else DEFAULT_SECTIONS
        pages = discover_pages(sections, args.types)

    if not pages:
        print("⚠️  Aucune page trouvée.")
        sys.exit(0)

    print(f"\n{'═'*60}")
    print(f"  Générateur PDF — Maths & Sciences LP")
    print(f"{'═'*60}")
    print(f"  Pages trouvées  : {len(pages)}")
    print(f"  Corrections     : {'oui' if args.corrections else 'non (masquées)'}")
    print(f"  Dossier sortie  : {pdf_out}")
    print(f"{'═'*60}\n")

    def out_path_for(p):
        rel = p.relative_to(ROOT)
        parts = list(rel.parts)
        folder = "-".join(parts[:-2])        # ex: maths-seconde
        ch = parts[-2]                       # ex: ch01
        name = parts[-1].replace(".html", ".pdf")  # ex: lecon.pdf
        title = get_chapter_title(p)
        ch_folder = f"{ch}-{title}" if title else ch
        return pdf_out / folder / ch_folder / name

    if args.dry_run:
        for p in pages:
            rel = p.relative_to(ROOT)
            out = out_path_for(p)
            print(f"  {rel}  →  {out.relative_to(ROOT)}")
        print(f"\nTotal : {len(pages)} fichiers (dry-run, rien généré)")
        return

    # ── Démarrer le serveur local ──
    server, port = start_server(ROOT)
    print_css = load_print_css()

    ok = 0
    errors = []
    t_start = time.time()

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"],
        )
        browser_page = browser.new_page()

        for i, html_path in enumerate(pages, 1):
            rel = html_path.relative_to(ROOT)
            out = out_path_for(html_path)
            label = str(rel)

            # Sauter si déjà généré et à jour
            if out.exists() and out.stat().st_mtime > html_path.stat().st_mtime:
                print(f"  [{i:3}/{len(pages)}] ⏭  {label} (à jour)")
                ok += 1
                continue

            print(f"  [{i:3}/{len(pages)}] ⏳  {label}", end="", flush=True)
            success = generate_pdf(browser_page, html_path, out, port,
                                   args.corrections, print_css)
            if success:
                size_kb = out.stat().st_size // 1024
                print(f"\r  [{i:3}/{len(pages)}] ✅  {label}  ({size_kb} Ko)")
                ok += 1
            else:
                print(f"\r  [{i:3}/{len(pages)}] ❌  {label}")
                errors.append(str(rel))

        browser.close()

    server.shutdown()

    elapsed = time.time() - t_start
    print(f"\n{'═'*60}")
    print(f"  ✅  {ok}/{len(pages)} PDF générés en {elapsed:.0f}s")
    if errors:
        print(f"  ❌  {len(errors)} erreur(s) :")
        for e in errors:
            print(f"       • {e}")
    print(f"  📁  {pdf_out}")
    print(f"{'═'*60}\n")


if __name__ == "__main__":
    main()
