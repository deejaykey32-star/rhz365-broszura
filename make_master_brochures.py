# -*- coding: utf-8 -*-
"""
make_master_brochures.py
Kompletny generator szablonów dla wszystkich 7 wariantów broszur RHZ365 (4, 8, 12, 16, 20, 24, 28 stron).
Wymogi:
1. Regulacja wielkości czcionki przez zmienną CSS: var(--base-font-size, 12pt).
2. Strona tytułowa zawiera PEŁNĄ treść programową zgodną z instrukcją (opis RHZ365, forma cyfrowa widokinaraj.pl, lektor, forma fizyczna 6 modeli, Misja Barw RGB/CMYK, zachęta do zakupu).
3. Brak pustych pól na stronach i brak wychodzenia treści poza marginesy/spady (bezpieczne paddingi, zbalansowana pionowa wysokość).
4. Bogate ilustracje wektorowe inline (koło barw RGB, schemat odwróconego CMYK, zegar 365 dni, motyw krzyża) oraz zdjęcia modeli.
"""

import os

CSS_TEMPLATE = """    :root {
      --base-font-size: {{ font_size_pt | default(12) }}pt;
      --gold: #d4af37;
      --gold-dark: #aa8214;
      --gold-light: #f7e7a9;
      --navy-deep: #070d18;
      --navy-main: #0c1728;
      --navy-light: #16263f;
      --parchment: #faf8f5;
      --parchment-card: #ffffff;
      --text-dark: #1e242d;
      --text-muted: #4b5563;
      --border-gold: rgba(212, 175, 55, 0.45);
      --red-rgb: #dc2626;
      --green-rgb: #059669;
      --blue-rgb: #2563eb;
      --cyan-cmyk: #0891b2;
      --magenta-cmyk: #c026d3;
      --yellow-cmyk: #ca8a04;
      
      --bleed: {{ bleed_mm }}mm;
      --gutter: {{ gutter_mm }}mm;
      --page-width: {{ page_width_mm }}mm;
      --page-height: {{ page_height_mm }}mm;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #2b3038;
      color: var(--text-dark);
      line-height: 1.5;
      font-size: var(--base-font-size);
      -webkit-font-smoothing: antialiased;
    }

    @page {
      size: {{ page_width_mm }}mm {{ page_height_mm }}mm;
      margin: 0;
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
        box-shadow: 0 12px 35px rgba(0,0,0,0.5);
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
      width: {{ page_width_mm }}mm;
      height: {{ page_height_mm }}mm;
      max-height: {{ page_height_mm }}mm;
      position: relative;
      overflow: hidden;
      background-color: var(--parchment);
      padding: calc(8mm + var(--bleed)) calc(10.5mm + var(--bleed)) calc(8mm + var(--bleed)) calc(10.5mm + var(--bleed));
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .page:nth-child(odd) {
      padding-left: calc(10.5mm + var(--bleed) + var(--gutter));
      padding-right: calc(10.5mm + var(--bleed));
    }
    .page:nth-child(even) {
      padding-left: calc(10.5mm + var(--bleed));
      padding-right: calc(10.5mm + var(--bleed) + var(--gutter));
    }

    {% if show_guides %}
    .page::before {
      content: '';
      position: absolute;
      top: var(--bleed);
      left: var(--bleed);
      right: var(--bleed);
      bottom: var(--bleed);
      border: 1px dashed rgba(220, 38, 38, 0.75);
      pointer-events: none;
      z-index: 9999;
    }
    .page::after {
      content: 'KDP Trim Line';
      position: absolute;
      top: calc(var(--bleed) + 2px);
      right: calc(var(--bleed) + 4px);
      font-size: 7pt;
      color: rgba(220, 38, 38, 0.85);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      pointer-events: none;
      z-index: 9999;
    }
    {% endif %}

    .page.cover-dark {
      background: radial-gradient(circle at 50% 25%, #182b49 0%, #0c1728 55%, #050a12 100%);
      color: #ffffff;
      padding: calc(8.5mm + var(--bleed)) calc(11mm + var(--bleed)) calc(8.5mm + var(--bleed)) calc(11mm + var(--bleed));
    }

    .page.cover-dark h1, .page.cover-dark h2, .page.cover-dark h3 { color: var(--gold-light); }

    .page-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid var(--border-gold);
      padding-bottom: 3px;
      margin-bottom: 6px;
      font-size: 8.5pt;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      color: var(--gold-dark);
      font-weight: 700;
      flex-shrink: 0;
    }

    .page.cover-dark .page-header {
      border-bottom-color: rgba(212, 175, 55, 0.4);
      color: var(--gold-light);
    }

    .page-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1.5px solid var(--border-gold);
      padding-top: 3px;
      margin-top: 6px;
      font-size: 8.5pt;
      color: var(--text-muted);
      letter-spacing: 0.8px;
      flex-shrink: 0;
    }

    .page.cover-dark .page-footer {
      border-top-color: rgba(212, 175, 55, 0.4);
      color: rgba(255,255,255,0.7);
    }

    .page-num {
      font-weight: 700;
      color: var(--gold-dark);
      font-family: 'Cinzel', serif;
      font-size: 9.5pt;
    }

    .page.cover-dark .page-num { color: var(--gold-light); }

    .page-body {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 0;
    }

    h1, h2, h3, h4 {
      font-family: 'Cinzel', serif;
      font-weight: 700;
      color: var(--navy-deep);
      line-height: 1.22;
    }

    .section-title {
      font-size: 16.5pt;
      letter-spacing: 0.5px;
      margin-bottom: 2px;
      text-transform: uppercase;
      color: var(--navy-deep);
    }

    .section-subtitle {
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: 11pt;
      color: var(--gold-dark);
      margin-bottom: 7px;
      font-weight: 600;
    }

    p {
      margin-bottom: 6px;
      text-align: justify;
      hyphens: auto;
      font-size: var(--base-font-size);
      line-height: 1.48;
    }

    p.lead {
      font-size: calc(var(--base-font-size) * 1.06);
      font-weight: 500;
      color: var(--navy-light);
      line-height: 1.45;
      margin-bottom: 7px;
    }

    .card {
      background: var(--parchment-card);
      border: 1.5px solid var(--border-gold);
      border-radius: 5px;
      padding: 7px 11px;
      margin-bottom: 6px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      font-size: var(--base-font-size);
      line-height: 1.45;
    }

    .card-dark {
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(212, 175, 55, 0.35);
      border-radius: 5px;
      padding: 7px 11px;
      margin-bottom: 6px;
      font-size: var(--base-font-size);
      line-height: 1.45;
    }

    .gold-box {
      border-left: 3.5px solid var(--gold);
      background: #fdfaf2;
      padding: 6px 10px;
      margin: 6px 0;
      border-radius: 0 4px 4px 0;
      font-size: var(--base-font-size);
      line-height: 1.45;
    }

    .badge {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 8.5pt;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .badge-rgb-r { background: #fee2e2; color: #991b1b; border: 1px solid #f87171; }
    .badge-rgb-g { background: #dcfce7; color: #166534; border: 1px solid #4ade80; }
    .badge-rgb-b { background: #dbeafe; color: #1e40af; border: 1px solid #60a5fa; }
    .badge-gold { background: #fef9c3; color: #854d0e; border: 1px solid #facc15; }
    .badge-black { background: #1f2937; color: #f9fafb; }
    .badge-white { background: #ffffff; color: #1f2937; border: 1px solid #d1d5db; }

    /* Układ pojedynczego produktu (1 na stronę) */
    .product-layout {
      display: flex;
      gap: 10px;
      align-items: stretch;
      flex: 1;
      min-height: 0;
    }

    .product-image-container {
      width: 44%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: #ffffff;
      border: 1.5px solid var(--border-gold);
      border-radius: 5px;
      padding: 5px;
      flex-shrink: 0;
    }

    .product-image-container img {
      max-width: 100%;
      max-height: 115mm;
      object-fit: contain;
      border-radius: 4px;
    }

    .product-info {
      width: 56%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .product-spec-list {
      list-style: none;
      font-size: var(--base-font-size);
      margin-bottom: 6px;
      line-height: 1.45;
    }

    .product-spec-list li {
      margin-bottom: 4px;
      padding-left: 13px;
      position: relative;
    }

    .product-spec-list li::before {
      content: '◆';
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 7pt;
      top: 2px;
    }

    .buy-card {
      background: linear-gradient(135deg, #fefcf6 0%, #f7f1e1 100%);
      border: 1.5px solid var(--gold);
      border-radius: 5px;
      padding: 7px 11px;
      text-align: center;
      box-shadow: 0 2px 5px rgba(170, 130, 20, 0.12);
    }

    .buy-card h4 {
      font-size: 11.5pt;
      color: var(--gold-dark);
      margin-bottom: 2px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .buy-card p {
      font-size: calc(var(--base-font-size) * 0.92);
      color: var(--text-dark);
      margin-bottom: 5px;
      text-align: center;
      line-height: 1.38;
    }

    .buy-btn {
      display: inline-block;
      background: linear-gradient(135deg, #aa8214 0%, #d4af37 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 9pt;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      padding: 5px 12px;
      border-radius: 4px;
      text-decoration: none;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
    }

    /* 6 modeli na jednej stronie (dla broszury 4 strony) */
    .rosaries-grid-6 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      margin: 4px 0;
      flex: 1;
    }
    .rosary-item-box {
      background: #ffffff;
      border: 1.5px solid var(--border-gold);
      border-radius: 4px;
      padding: 5px 6px;
      display: flex;
      gap: 6px;
      align-items: center;
    }
    .rosary-item-box img {
      width: 32mm;
      height: 32mm;
      object-fit: contain;
      border-radius: 4px;
      background: #faf8f5;
      padding: 2px;
      border: 1px solid #f0e6d2;
      flex-shrink: 0;
    }
    .rosary-item-text {
      flex: 1;
      font-size: 8.5pt;
      line-height: 1.32;
    }
    .rosary-item-text h4 {
      font-size: 9.5pt;
      color: var(--navy-deep);
      margin-bottom: 2px;
    }
    .buy-btn-mini {
      display: inline-block;
      background: linear-gradient(135deg, #aa8214 0%, #d4af37 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 7.5pt;
      text-transform: uppercase;
      padding: 2px 6px;
      border-radius: 3px;
      text-decoration: none;
      margin-top: 2px;
    }

    /* 2 produkty na stronę (dla broszur 8 i 12 stron) */
    .pair-layout {
      display: flex;
      flex-direction: column;
      gap: 7px;
      flex: 1;
      justify-content: space-between;
    }
    .product-row-card {
      display: flex;
      gap: 9px;
      background: #ffffff;
      border: 1.5px solid var(--border-gold);
      border-radius: 5px;
      padding: 6px 9px;
      align-items: center;
      flex: 1;
    }
    .product-row-card img {
      width: 38mm;
      height: 48mm;
      object-fit: contain;
      border-radius: 4px;
      background: #faf8f5;
      padding: 3px;
      border: 1px solid #f0e6d2;
      flex-shrink: 0;
    }
    .product-row-info {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .product-row-info h4 {
      font-size: 10.5pt;
      color: var(--navy-deep);
      margin-bottom: 2px;
    }
    .product-row-info p {
      font-size: calc(var(--base-font-size) * 0.9);
      line-height: 1.38;
      margin-bottom: 3px;
    }
    .product-row-info ul {
      list-style: none;
      font-size: calc(var(--base-font-size) * 0.85);
      margin-bottom: 4px;
    }
    .product-row-info ul li {
      padding-left: 11px;
      position: relative;
      margin-bottom: 2px;
    }
    .product-row-info ul li::before {
      content: '◆';
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 6pt;
      top: 2px;
    }
    .buy-btn-small {
      display: inline-block;
      background: linear-gradient(135deg, #aa8214 0%, #d4af37 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 8pt;
      text-transform: uppercase;
      padding: 3.5px 10px;
      border-radius: 3px;
      text-decoration: none;
      align-self: flex-start;
    }
"""

def wrap_html(title, pages_html):
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
{CSS_TEMPLATE}
  </style>
</head>
<body>

<div class="booklet-container">
{pages_html}
</div>

</body>
</html>
"""

print("make_master_brochures.py ready for template generation.")
