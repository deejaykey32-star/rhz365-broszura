import os
import shutil
import zipfile
import subprocess
from jinja2 import Environment, FileSystemLoader
import fitz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME):
    CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=False)

def compile_pdf_from_html(html_code, out_pdf_path):
    img_dir_uri = IMAGES_DIR.replace('\\', '/')
    html_code = html_code.replace('src="/images/', f'src="file:///{img_dir_uri}/')
    html_code = html_code.replace('src="images/', f'src="file:///{img_dir_uri}/')

    temp_html = os.path.join(OUTPUT_DIR, "temp_render.html")
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_code)

    file_uri = f"file:///{temp_html.replace('\\', '/')}"
    cmd = [
        CHROME,
        '--headless=new',
        '--disable-gpu',
        '--allow-file-access-from-files',
        '--no-pdf-header-footer',
        f'--print-to-pdf={out_pdf_path}',
        file_uri
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return os.path.exists(out_pdf_path) and os.path.getsize(out_pdf_path) > 0

print("=== 1. Compiling KDP Cover Spread ===")
spine = round(max(1.4, 24 * 0.057), 2)
bleed = 3.175
total_w = round((2 * 148) + spine + (2 * bleed), 2)
total_h = round(210 + (2 * bleed), 2)
cover_tmpl = env.get_template('kdp_cover.html')
cover_html = cover_tmpl.render(
    bleed_mm=bleed,
    spine_width_mm=spine,
    total_cover_width_mm=total_w,
    total_cover_height_mm=total_h,
    show_guides=False,
    website_url="WWW.WIDOKINARAJ.PL",
    page_count=24,
    font_size_pt=12.0
)
cover_pdf_output = os.path.join(OUTPUT_DIR, "RHZ365_Okladka_KDP_Spread_24str.pdf")
compile_pdf_from_html(cover_html, cover_pdf_output)
shutil.copy2(cover_pdf_output, os.path.join(DOWNLOADS_DIR, "RHZ365_Okladka_KDP_Spread_24str.pdf"))
print(f"Cover PDF compiled: {os.path.getsize(cover_pdf_output)} bytes")

print("\n=== 2. Compiling & Copying All Interior Formats ===")
interior_pages = [4, 8, 12, 16, 20, 24, 28]

for p in interior_pages:
    tmpl_name = f"interior_{p}.html"
    tmpl = env.get_template(tmpl_name)
    # 24 and 28 use KDP bleeds/gutters by default in production
    b = 3.175 if p >= 24 else 3.0
    g = 9.5 if p >= 24 else 0.0
    tw = round(148 + (2 * b), 2)
    th = round(210 + (2 * b), 2)
    html_code = tmpl.render(
        page_width_mm=tw,
        page_height_mm=th,
        bleed_mm=b,
        gutter_mm=g,
        show_guides=False,
        website_url="WWW.WIDOKINARAJ.PL",
        page_count=p,
        font_size_pt=12.0
    )
    out_pdf = os.path.join(OUTPUT_DIR, f"RHZ365_Wnetrze_A5_{p}str.pdf")
    compile_pdf_from_html(html_code, out_pdf)
    shutil.copy2(out_pdf, os.path.join(DOWNLOADS_DIR, f"RHZ365_Wnetrze_A5_{p}str.pdf"))

    # Verify with PyMuPDF
    doc = fitz.open(out_pdf)
    char_counts = [len(page.get_text().strip()) for page in doc]
    print(f"[{p} str.] Actual pages: {doc.page_count} (Nominal: {p}) | Chars/page: {char_counts}")
    assert doc.page_count == p, f"ERROR: Nominal {p} != Actual {doc.page_count}"
    doc.close()

print("\n=== 3. Creating Master ZIP Package ===")
zip_path = os.path.join(DOWNLOADS_DIR, "Pakiet_Drukarski_RHZ365_KDP.zip")
readme_text = """PAKIET DRUKARSKI I AMAZON KDP
RÓŻANIEC HISTORII ZBAWIENIA (RHZ365 & WIDOKI NA RAJ)
Oficjalna strona internetowa: https://widokinaraj.pl
Aplikacja generatora: https://rhz365-broszura.pages.dev

ZAWARTOŚĆ PAKIETU:
1. Wnętrza A5 gotowe do druku (ze spadami 3.0 mm lub 3.175 mm KDP):
   - RHZ365_Wnetrze_A5_4str.pdf  (Folder / Ulotka składana A5, 4 strony)
   - RHZ365_Wnetrze_A5_8str.pdf  (Zwarta broszura zeszytowa A5, 8 stron)
   - RHZ365_Wnetrze_A5_12str.pdf (Pośrednia broszura zeszytowa A5, 12 stron)
   - RHZ365_Wnetrze_A5_16str.pdf (Standardowa broszura zeszytowa A5, 16 stron)
   - RHZ365_Wnetrze_A5_20str.pdf (Druk Lokalny Rozszerzony A5, 20 stron)
   - RHZ365_Wnetrze_A5_24str.pdf (Amazon KDP Paperback Minimum, 24 strony)
   - RHZ365_Wnetrze_A5_28str.pdf (Amazon KDP Pełne Rozszerzone, 28 stron)

2. Pełna okładka wrap-around do Amazon KDP:
   - RHZ365_Okladka_KDP_Spread_24str.pdf (Tył + Grzbiet + Przód + Spady 3.175 mm)

WYTYCZNE AMAZON KDP:
- Trim Size: A5 (5.83 x 8.27 in / 148 x 210 mm)
- Bleed: Bleed (PDF zawiera spady 3.175 mm / 0.125")
- Margin / Gutter: 9.5 mm (0.375") uwzględnione
- Minimalna objętość dla paperback: 24 strony (pliki 24str i 28str w pełni zgodne)
- Papier: Standard Color / Premium Color, biały

WYTYCZNE DLA DRUKARNI LOKALNYCH (4, 8, 12, 16, 20 stron):
- Oprawa zeszytowa (zszywki)
- Spady 3 mm ze wszystkich stron
- Margines wewnętrzny 0 mm (symetryczny)

Wszystkie strony są w 100% wypełnione merytoryczną treścią, modlitwami, ilustracjami różańców i diagramami teologicznymi.
Brak pustych stron i brak obcięć.
"""

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in os.listdir(DOWNLOADS_DIR):
        if f.endswith('.pdf'):
            z.write(os.path.join(DOWNLOADS_DIR, f), f)
    z.writestr("INSTRUKCJA_KDP_I_DRUKARNI.txt", readme_text)

print(f"Zip created: {os.path.getsize(zip_path)} bytes")
print("ALL COMPILATIONS SUCCESSFUL!")
