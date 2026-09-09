import os
import re

# 1. Read templates
with open('templates/interior_4.html', 'r', encoding='utf-8') as f:
    html_4 = f.read()
with open('templates/interior_8.html', 'r', encoding='utf-8') as f:
    html_8 = f.read()
with open('templates/interior_12.html', 'r', encoding='utf-8') as f:
    html_12 = f.read()
with open('templates/interior_16.html', 'r', encoding='utf-8') as f:
    html_16 = f.read()
with open('templates/interior_20.html', 'r', encoding='utf-8') as f:
    html_20 = f.read()
with open('templates/interior_24.html', 'r', encoding='utf-8') as f:
    html_24 = f.read()
with open('templates/interior_28.html', 'r', encoding='utf-8') as f:
    html_28 = f.read()

def extract_body(html):
    m = re.search(r'<div class="booklet-container">(.*?)</div>\s*</body>', html, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""

body_4 = extract_body(html_4)
body_8 = extract_body(html_8)
body_12 = extract_body(html_12)
body_16 = extract_body(html_16)
body_20 = extract_body(html_20)
body_24 = extract_body(html_24)
body_28 = extract_body(html_28)

# 2. Build preview.html
preview_css = """
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap');

    :root {
      --gold: #d4af37;
      --gold-dark: #aa8214;
      --gold-light: #f7e7a9;
      --navy-deep: #070d18;
      --navy-main: #0c1728;
      --navy-light: #16263f;
      --parchment: #faf8f5;
      --parchment-card: #ffffff;
      --text-dark: #1e242d;
      --text-muted: #57606f;
      --border-gold: rgba(212, 175, 55, 0.4);
      --red-rgb: #e02424;
      --green-rgb: #0e9f6e;
      --blue-rgb: #1a56db;
      --cyan-cmyk: #06b6d4;
      --magenta-cmyk: #d946ef;
      --yellow-cmyk: #eab308;
      
      --bleed: 3mm;
      --gutter: 0mm;
      --page-width: 154mm;
      --page-height: 216mm;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #2b3038;
      color: var(--text-dark);
      line-height: 1.42;
      font-size: 8.6pt;
      -webkit-font-smoothing: antialiased;
    }

    @media screen {
      .booklet-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
        padding: 30px 10px;
      }
      .page {
        box-shadow: 0 10px 35px rgba(0,0,0,0.5);
      }
    }

    @media print {
      body { background-color: transparent !important; }
      .booklet-container { display: block !important; padding: 0 !important; }
      .page {
        box-shadow: none !important;
        page-break-after: always !important;
        page-break-inside: avoid !important;
        break-after: page !important;
      }
    }

    .page {
      width: var(--page-width);
      height: var(--page-height);
      max-height: var(--page-height);
      position: relative;
      overflow: hidden;
      background-color: var(--parchment);
      padding: calc(11mm + var(--bleed)) calc(13mm + var(--bleed)) calc(10mm + var(--bleed)) calc(13mm + var(--bleed));
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .page:nth-child(odd) {
      padding-left: calc(13mm + var(--bleed) + var(--gutter));
      padding-right: calc(13mm + var(--bleed));
    }
    .page:nth-child(even) {
      padding-left: calc(13mm + var(--bleed));
      padding-right: calc(13mm + var(--bleed) + var(--gutter));
    }

    .show-guides .page::before {
      content: '';
      position: absolute;
      top: var(--bleed);
      left: var(--bleed);
      right: var(--bleed);
      bottom: var(--bleed);
      border: 1px dashed rgba(220, 38, 38, 0.7);
      pointer-events: none;
      z-index: 9999;
    }
    .show-guides .page::after {
      content: 'Linia Cięcia (A5)';
      position: absolute;
      top: calc(var(--bleed) + 2px);
      right: calc(var(--bleed) + 4px);
      font-size: 5.5pt;
      color: rgba(220, 38, 38, 0.85);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      pointer-events: none;
      z-index: 9999;
    }

    .page.cover-dark {
      background: radial-gradient(circle at 50% 25%, #182b49 0%, #0c1728 55%, #050a12 100%);
      color: #ffffff;
      padding: calc(12mm + var(--bleed)) calc(13mm + var(--bleed)) calc(10mm + var(--bleed)) calc(13mm + var(--bleed));
    }

    .page.cover-dark h1, .page.cover-dark h2, .page.cover-dark h3 { color: var(--gold-light); }
    .page-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-gold); padding-bottom: 3px; margin-bottom: 8px; font-size: 6.8pt; text-transform: uppercase; letter-spacing: 1.2px; color: var(--gold-dark); font-weight: 600; }
    .page.cover-dark .page-header { border-bottom-color: rgba(212, 175, 55, 0.3); color: var(--gold-light); }
    .page-footer { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-gold); padding-top: 3px; margin-top: 6px; font-size: 6.8pt; color: var(--text-muted); letter-spacing: 0.8px; }
    .page.cover-dark .page-footer { border-top-color: rgba(212, 175, 55, 0.3); color: rgba(255,255,255,0.6); }
    .page-num { font-weight: 700; color: var(--gold-dark); font-family: 'Cinzel', serif; font-size: 7.5pt; }
    .page.cover-dark .page-num { color: var(--gold-light); }

    h1, h2, h3, h4 { font-family: 'Cinzel', serif; font-weight: 700; color: var(--navy-deep); line-height: 1.18; }
    .section-title { font-size: 12.5pt; letter-spacing: 0.5px; margin-bottom: 2px; text-transform: uppercase; color: var(--navy-deep); }
    .section-subtitle { font-family: 'Playfair Display', serif; font-style: italic; font-size: 8.2pt; color: var(--gold-dark); margin-bottom: 7px; font-weight: 600; }
    p { margin-bottom: 5px; text-align: justify; hyphens: auto; }
    p.lead { font-size: 9pt; font-weight: 500; color: var(--navy-light); line-height: 1.38; }

    .card { background: var(--parchment-card); border: 1px solid var(--border-gold); border-radius: 5px; padding: 6px 8px; margin-bottom: 6px; }
    .card-dark { background: rgba(255,255,255,0.05); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 5px; padding: 7px 9px; margin-bottom: 6px; }
    .gold-box { border-left: 3px solid var(--gold); background: #fdfaf2; padding: 5px 8px; margin: 5px 0; border-radius: 0 4px 4px 0; font-size: 8pt; }

    .badge { display: inline-block; padding: 1px 5px; border-radius: 3px; font-size: 6.8pt; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; }
    .badge-rgb-r { background: #fee2e2; color: #991b1b; border: 1px solid #f87171; }
    .badge-rgb-g { background: #dcfce7; color: #166534; border: 1px solid #4ade80; }
    .badge-rgb-b { background: #dbeafe; color: #1e40af; border: 1px solid #60a5fa; }
    .badge-gold { background: #fef9c3; color: #854d0e; border: 1px solid #facc15; }

    .product-layout { display: flex; gap: 9px; align-items: stretch; flex: 1; min-height: 0; }
    .product-image-container { width: 44%; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #ffffff; border: 1px solid var(--border-gold); border-radius: 5px; padding: 5px; }
    .product-image-container img { max-width: 100%; max-height: 122mm; object-fit: contain; border-radius: 3px; }
    .product-info { width: 56%; display: flex; flex-direction: column; justify-content: space-between; }
    .product-spec-list { list-style: none; font-size: 7.8pt; margin-bottom: 5px; }
    .product-spec-list li { margin-bottom: 4px; padding-left: 11px; position: relative; }
    .product-spec-list li::before { content: '◆'; position: absolute; left: 0; color: var(--gold); font-size: 5.5pt; top: 1.5px; }

    .buy-card { background: linear-gradient(135deg, #fefcf6 0%, #f7f1e1 100%); border: 1.5px solid var(--gold); border-radius: 5px; padding: 6px 8px; text-align: center; }
    .buy-card h4 { font-size: 8.2pt; color: var(--gold-dark); margin-bottom: 2px; text-transform: uppercase; }
    .buy-card p { font-size: 7.3pt; margin-bottom: 4px; text-align: center; }
    .buy-btn { display: inline-block; background: linear-gradient(135deg, #aa8214 0%, #d4af37 100%); color: #ffffff; font-weight: 700; font-size: 7pt; text-transform: uppercase; padding: 3.5px 9px; border-radius: 4px; text-decoration: none; }
    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; }

    /* Styles for 4-page grid */
    .rosaries-grid-6 { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin: 4px 0; }
    .rosary-item-box { background: #ffffff; border: 1px solid var(--border-gold); border-radius: 4px; padding: 5px 6px; display: flex; gap: 6px; align-items: center; }
    .rosary-item-box img { width: 32mm; height: 32mm; object-fit: contain; border-radius: 3px; background: #faf8f5; padding: 2px; border: 1px solid #f0e6d2; flex-shrink: 0; }
    .rosary-item-text { flex: 1; font-size: 6.8pt; line-height: 1.3; }
    .rosary-item-text h4 { font-size: 7.2pt; color: var(--navy-deep); margin-bottom: 2px; }
    .buy-btn-mini { display: inline-block; background: linear-gradient(135deg, #aa8214 0%, #d4af37 100%); color: #ffffff; font-weight: 700; font-size: 6pt; text-transform: uppercase; padding: 2px 6px; border-radius: 3px; text-decoration: none; margin-top: 3px; }

    /* Styles for 8 and 12-page pairs */
    .pair-layout { display: flex; flex-direction: column; gap: 8px; flex: 1; justify-content: space-around; }
    .product-row-card { display: flex; gap: 10px; background: #ffffff; border: 1px solid var(--border-gold); border-radius: 5px; padding: 7px 9px; align-items: center; }
    .product-row-card img { width: 38mm; height: 48mm; object-fit: contain; border-radius: 3px; background: #faf8f5; padding: 3px; border: 1px solid #f0e6d2; flex-shrink: 0; }
    .product-row-info { flex: 1; display: flex; flex-direction: column; justify-content: space-between; height: 100%; }
    .product-row-info h4 { font-size: 8.5pt; color: var(--navy-deep); margin-bottom: 2px; }
    .product-row-info p { font-size: 7.4pt; line-height: 1.35; margin-bottom: 4px; }
    .product-row-info ul { list-style: none; font-size: 7.2pt; margin-bottom: 5px; }
    .product-row-info ul li { padding-left: 10px; position: relative; margin-bottom: 2px; }
    .product-row-info ul li::before { content: '◆'; position: absolute; left: 0; color: var(--gold); font-size: 5pt; top: 1.5px; }
    .buy-btn-small { display: inline-block; background: linear-gradient(135deg, #aa8214 0%, #d4af37 100%); color: #ffffff; font-weight: 700; font-size: 6.8pt; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; text-decoration: none; align-self: flex-start; }
"""

preview_js = """
  const params = new URLSearchParams(window.location.search);
  const pages = parseInt(params.get('pages') || '16');
  const bleed = parseFloat(params.get('bleed') || '3.0');
  const gutter = parseFloat(params.get('gutter') || '0.0');
  const guides = params.get('guides') === '1';
  const website = params.get('website') || 'WWW.WIDOKINARAJ.PL';

  const totalW = (148 + (2 * bleed)).toFixed(2);
  const totalH = (210 + (2 * bleed)).toFixed(2);

  document.documentElement.style.setProperty('--bleed', bleed + 'mm');
  document.documentElement.style.setProperty('--gutter', gutter + 'mm');
  document.documentElement.style.setProperty('--page-width', totalW + 'mm');
  document.documentElement.style.setProperty('--page-height', totalH + 'mm');

  document.getElementById('dynamic-print-page-style').innerHTML = '@page { size: ' + totalW + 'mm ' + totalH + 'mm; margin: 0; }';

  if (guides) {
    document.body.classList.add('show-guides');
  }

  let targetId = 'wrapper-16';
  if (pages >= 28) targetId = 'wrapper-28';
  else if (pages >= 24) targetId = 'wrapper-24';
  else if (pages >= 20) targetId = 'wrapper-20';
  else if (pages >= 16) targetId = 'wrapper-16';
  else if (pages >= 12) targetId = 'wrapper-12';
  else if (pages >= 8) targetId = 'wrapper-8';
  else targetId = 'wrapper-4';

  const el = document.getElementById(targetId);
  if (el) {
    el.style.display = 'flex';
    el.innerHTML = el.innerHTML.split('{{ website_url }}').join(website);
  }
"""

preview_html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <title>Podgląd Wnętrza Broszury A5 • RHZ365</title>
  <style>
{preview_css}
  </style>
  <style id="dynamic-print-page-style"></style>
</head>
<body>

<div id="content-wrapper">
  <div id="wrapper-4" class="booklet-container" style="display:none;">{body_4}</div>
  <div id="wrapper-8" class="booklet-container" style="display:none;">{body_8}</div>
  <div id="wrapper-12" class="booklet-container" style="display:none;">{body_12}</div>
  <div id="wrapper-16" class="booklet-container" style="display:none;">{body_16}</div>
  <div id="wrapper-20" class="booklet-container" style="display:none;">{body_20}</div>
  <div id="wrapper-24" class="booklet-container" style="display:none;">{body_24}</div>
  <div id="wrapper-28" class="booklet-container" style="display:none;">{body_28}</div>
</div>

<script>
{preview_js}
</script>

</body>
</html>"""

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(preview_html)
print("preview.html updated successfully with 7 page variants (4, 8, 12, 16, 20, 24, 28)!")
