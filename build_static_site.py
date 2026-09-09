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

# 2. Extract CSS from interior_16.html and adapt for preview.html
from make_master_brochures import CSS_TEMPLATE

preview_css = CSS_TEMPLATE.replace('{{ bleed_mm }}', '3.0')
preview_css = preview_css.replace('{{ gutter_mm }}', '0.0')
preview_css = preview_css.replace('{{ page_width_mm }}', '154')
preview_css = preview_css.replace('{{ page_height_mm }}', '216')
preview_css = preview_css.replace('{% if show_guides %}', '/* guides */')
preview_css = preview_css.replace('{% endif %}', '')

preview_js = """
  const params = new URLSearchParams(window.location.search);
  const pages = parseInt(params.get('pages') || '16');
  const bleed = parseFloat(params.get('bleed') || '3.0');
  const gutter = parseFloat(params.get('gutter') || '0.0');
  const fontsize = parseFloat(params.get('fontsize') || '12');
  const guides = params.get('guides') === '1';
  const website = params.get('website') || 'WWW.WIDOKINARAJ.PL';

  const totalW = (148 + (2 * bleed)).toFixed(2);
  const totalH = (210 + (2 * bleed)).toFixed(2);

  document.documentElement.style.setProperty('--bleed', bleed + 'mm');
  document.documentElement.style.setProperty('--gutter', gutter + 'mm');
  document.documentElement.style.setProperty('--page-width', totalW + 'mm');
  document.documentElement.style.setProperty('--page-height', totalH + 'mm');
  document.documentElement.style.setProperty('--base-font-size', fontsize + 'pt');

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
print("preview.html updated successfully with dynamic font regulation and full layouts!")

# 3. Update cover.html directly from templates/kdp_cover.html
with open('templates/kdp_cover.html', 'r', encoding='utf-8') as f:
    kdp_tmpl = f.read()

kdp_static = kdp_tmpl.replace('{{ bleed_mm }}', '3.175')
kdp_static = kdp_static.replace('{{ spine_width_mm }}', '1.368')
kdp_static = kdp_static.replace('{{ total_cover_width_mm }}', '303.718')
kdp_static = kdp_static.replace('{{ total_cover_height_mm }}', '216.35')
kdp_static = kdp_static.replace('{% if show_guides %}', '<script>/* guides */</script>')
kdp_static = kdp_static.replace('{% endif %}', '')
kdp_static = kdp_static.replace('{{ website_url }}', 'WWW.WIDOKINARAJ.PL')

script_tag = """
<script>
  const params = new URLSearchParams(window.location.search);
  const pages = parseInt(params.get('pages') || '24');
  const bleed = parseFloat(params.get('bleed') || '3.175');
  const fontsize = parseFloat(params.get('fontsize') || '12');
  const guides = params.get('guides') === '1';
  const website = params.get('website') || 'WWW.WIDOKINARAJ.PL';

  const spineWidth = (pages * 0.057).toFixed(3);
  const totalW = (148 + parseFloat(spineWidth) + 148 + (2 * bleed)).toFixed(3);
  const totalH = (210 + (2 * bleed)).toFixed(2);

  document.documentElement.style.setProperty('--bleed', bleed + 'mm');
  document.documentElement.style.setProperty('--spine-width', spineWidth + 'mm');
  document.documentElement.style.setProperty('--total-width', totalW + 'mm');
  document.documentElement.style.setProperty('--total-height', totalH + 'mm');
  document.documentElement.style.setProperty('--base-font-size', fontsize + 'pt');

  if (guides) {
    document.body.classList.add('show-guides');
  }
</script>
"""
kdp_static = kdp_static.replace('</body>', script_tag + '\n</body>')

with open('cover.html', 'w', encoding='utf-8') as f:
    f.write(kdp_static)
print("cover.html updated successfully with dynamic font regulation!")
