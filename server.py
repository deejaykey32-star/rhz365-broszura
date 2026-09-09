import os
import sys
import json
import zipfile
import subprocess
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

PORT = 3456
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

os.makedirs(OUTPUT_DIR, exist_ok=True)

jinja_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=False)

def find_browser():
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

BROWSER_PATH = find_browser()

class GeneratorHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path == '/' or path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            template = jinja_env.get_template('index.html')
            rendered = template.render()
            self.wfile.write(rendered.encode('utf-8'))
            return

        elif path == '/preview':
            doc_type = query.get('type', ['interior'])[0]
            pages = int(query.get('pages', ['16'])[0])
            bleed = float(query.get('bleed', ['3'])[0])
            gutter = float(query.get('gutter', ['0'])[0])
            show_guides = (query.get('guides', ['0'])[0] == '1')
            website = query.get('website', ['WWW.WIDOKINARAJ.PL'])[0]

            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()

            if doc_type == 'cover':
                spine = round(max(1.4, pages * 0.057), 2)
                total_w = round((2 * 148) + spine + (2 * bleed), 2)
                total_h = round(210 + (2 * bleed), 2)
                tmpl = jinja_env.get_template('kdp_cover.html')
                rendered = tmpl.render(
                    bleed_mm=bleed,
                    spine_width_mm=spine,
                    total_cover_width_mm=total_w,
                    total_cover_height_mm=total_h,
                    show_guides=show_guides,
                    website_url=website,
                    page_count=pages
                )
            else:
                # Interior
                total_w = round(148 + (2 * bleed), 2)
                total_h = round(210 + (2 * bleed), 2)
                if pages <= 16:
                    template_name = 'interior_16.html'
                elif pages <= 20:
                    template_name = 'interior_20.html'
                elif pages <= 24:
                    template_name = 'interior_24.html'
                else:
                    template_name = 'interior_28.html'

                tmpl = jinja_env.get_template(template_name)
                rendered = tmpl.render(
                    page_width_mm=total_w,
                    page_height_mm=total_h,
                    bleed_mm=bleed,
                    gutter_mm=gutter,
                    show_guides=show_guides,
                    website_url=website,
                    page_count=pages
                )

            self.wfile.write(rendered.encode('utf-8'))
            return

        elif path.startswith('/images/'):
            filename = path[len('/images/'):]
            filepath = os.path.join(IMAGES_DIR, filename)
            if os.path.exists(filepath):
                self.send_response(200)
                if filepath.endswith('.jpg') or filepath.endswith('.jpeg'):
                    self.send_header('Content-Type', 'image/jpeg')
                elif filepath.endswith('.png'):
                    self.send_header('Content-Type', 'image/png')
                elif filepath.endswith('.svg'):
                    self.send_header('Content-Type', 'image/svg+xml')
                self.end_headers()
                with open(filepath, 'rb') as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_error(404, "Image not found")
                return

        elif path.startswith('/output/'):
            filename = path[len('/output/'):]
            filepath = os.path.join(OUTPUT_DIR, filename)
            if os.path.exists(filepath):
                self.send_response(200)
                if filepath.endswith('.pdf'):
                    self.send_header('Content-Type', 'application/pdf')
                    self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                elif filepath.endswith('.zip'):
                    self.send_header('Content-Type', 'application/zip')
                    self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                self.end_headers()
                with open(filepath, 'rb') as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_error(404, "File not found")
                return

        # Fallback default
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == '/api/generate-pdf':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body)

            doc_type = params.get('type', 'interior')
            pages = int(params.get('pages', 16))
            bleed = float(params.get('bleed', 3.0))
            gutter = float(params.get('gutter', 0.0))
            website = params.get('website', 'WWW.WIDOKINARAJ.PL')

            res = compile_pdf(doc_type, pages, bleed, gutter, website)

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(res).encode('utf-8'))
            return

        elif path == '/api/generate-zip':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body)

            pages = int(params.get('pages', 24))
            bleed = float(params.get('bleed', 3.175))
            gutter = float(params.get('gutter', 9.5))
            website = params.get('website', 'WWW.WIDOKINARAJ.PL')

            # Compile interior
            res_interior = compile_pdf('interior', pages, bleed, gutter, website)
            # Compile cover
            res_cover = compile_pdf('cover', pages, bleed, gutter, website)

            zip_filename = f"Pakiet_Drukarski_RHZ365_{pages}stron.zip"
            zip_path = os.path.join(OUTPUT_DIR, zip_filename)

            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
                if res_interior.get('success'):
                    z.write(os.path.join(OUTPUT_DIR, res_interior['filename']), res_interior['filename'])
                if res_cover.get('success'):
                    z.write(os.path.join(OUTPUT_DIR, res_cover['filename']), res_cover['filename'])
                
                # Instruction txt
                readme = f"""PAKIET DRUKARSKI I AMAZON KDP
RÓŻANIEC HISTORII ZBAWIENIA (RHZ365 & WIDOKI NA RAJ)
Oficjalna strona: {website}

Zawartość paczki:
1. Wnętrze PDF: {res_interior.get('filename')}
   - Format: A5 ze spadem ({bleed} mm)
   - Liczba stron: {pages}
   - Margines wewnętrzny (Gutter): {gutter} mm

2. Okładka KDP Wrap-around PDF: {res_cover.get('filename')}
   - Układ: Tył + Grzbiet + Przód + Spad ({bleed} mm)
   - Szerokość grzbietu (Spine): ok. {round(max(1.4, pages * 0.057), 2)} mm

WYTYCZNE DLA AMAZON KDP:
- Trim size: A5 (5.83 x 8.27 in / 148 x 210 mm)
- Bleed: Bleed (PDF includes bleed)
- Paper: Standard Color lub Premium Color (Biały papier)
- Cover finish: Glossy lub Matte (Błyszczący / Matowy)
- Minimalna wymagana liczba stron dla KDP Paperback: 24 strony.

Wygenerowano automatycznie przez Generator Broszur RHZ365.
"""
                z.writestr("INSTRUKCJA_KDP_I_DRUKARNI.txt", readme)

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": True,
                "filename": zip_filename,
                "download_url": f"/output/{zip_filename}"
            }).encode('utf-8'))
            return

def compile_pdf(doc_type, pages, bleed, gutter, website):
    if not BROWSER_PATH:
        return {"success": False, "error": "Nie znaleziono przeglądarki Chrome lub Edge do generowania PDF."}

    # Prepare rendered HTML
    if doc_type == 'cover':
        spine = round(max(1.4, pages * 0.057), 2)
        total_w = round((2 * 148) + spine + (2 * bleed), 2)
        total_h = round(210 + (2 * bleed), 2)
        tmpl = jinja_env.get_template('kdp_cover.html')
        html_code = tmpl.render(
            bleed_mm=bleed,
            spine_width_mm=spine,
            total_cover_width_mm=total_w,
            total_cover_height_mm=total_h,
            show_guides=False,
            website_url=website,
            page_count=pages
        )
        out_name = f"RHZ365_Okladka_KDP_Spread_{pages}str.pdf"
    else:
        total_w = round(148 + (2 * bleed), 2)
        total_h = round(210 + (2 * bleed), 2)
        if pages <= 16:
            template_name = 'interior_16.html'
        elif pages <= 20:
            template_name = 'interior_20.html'
        elif pages <= 24:
            template_name = 'interior_24.html'
        else:
            template_name = 'interior_28.html'

        tmpl = jinja_env.get_template(template_name)
        html_code = tmpl.render(
            page_width_mm=total_w,
            page_height_mm=total_h,
            bleed_mm=bleed,
            gutter_mm=gutter,
            show_guides=False,
            website_url=website,
            page_count=pages
        )
        out_name = f"RHZ365_Wnetrze_A5_{pages}str.pdf"

    # Replace relative image URLs with absolute file URIs for headless browser
    img_dir_uri = IMAGES_DIR.replace('\\', '/')
    html_code = html_code.replace('src="/images/', f'src="file:///{img_dir_uri}/')
    html_code = html_code.replace('src="images/', f'src="file:///{img_dir_uri}/')

    temp_html_path = os.path.join(OUTPUT_DIR, f"temp_{doc_type}.html")
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(html_code)

    pdf_output_path = os.path.join(OUTPUT_DIR, out_name)
    file_uri = f"file:///{temp_html_path.replace('\\', '/')}"

    cmd = [
        BROWSER_PATH,
        '--headless=new',
        '--disable-gpu',
        '--allow-file-access-from-files',
        '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_output_path}',
        file_uri
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if os.path.exists(pdf_output_path) and os.path.getsize(pdf_output_path) > 0:
            actual_pages = 1
            if fitz:
                try:
                    doc = fitz.open(pdf_output_path)
                    actual_pages = doc.page_count
                    doc.close()
                except Exception as e:
                    pass
            return {
                "success": True,
                "filename": out_name,
                "download_url": f"/output/{out_name}",
                "pages": actual_pages,
                "file_size": os.path.getsize(pdf_output_path)
            }
        else:
            return {"success": False, "error": f"Chrome failed to generate PDF. Stderr: {proc.stderr}"}
    except Exception as ex:
        return {"success": False, "error": str(ex)}

if __name__ == '__main__':
    print(f"Starting RHZ365 Brochure Generator Server on port {PORT}...")
    print(f"Browser engine: {BROWSER_PATH}")
    print(f"Open in browser: http://localhost:{PORT}")
    server = HTTPServer(('127.0.0.1', PORT), GeneratorHandler)
    server.serve_forever()
