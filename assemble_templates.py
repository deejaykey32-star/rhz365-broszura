# -*- coding: utf-8 -*-
"""
assemble_templates.py
Generuje wszystkie szablony HTML w folderze templates/ z wykorzystaniem page_components.py
i make_master_brochures.py
"""

import os
from make_master_brochures import wrap_html
import page_components as pc

os.makedirs('templates', exist_ok=True)

# 1. Ulotka 4 strony
pages_4 = [
    pc.get_page_cover_title(),
    pc.get_page_digital_and_theology_4p(pnum=2),
    pc.get_page_six_products_grid(pnum=3),
    pc.get_page_testimony_and_store(pnum=4)
]
with open('templates/interior_4.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Różaniec Historii Zbawienia - Folder 4 Strony A5", "\n\n".join(pages_4)))
print("interior_4.html generated.")

# 2. Broszura 8 stron
pages_8 = [
    pc.get_page_cover_title(),
    pc.get_page_four_volumes(pnum=2),
    pc.get_page_calendar_architecture(pnum=3),
    pc.get_page_rgb_theology(pnum=4),
    pc.get_page_paired_products(1, 2, pnum=5),
    pc.get_page_paired_products(3, 4, pnum=6),
    pc.get_page_paired_products(5, 6, pnum=7),
    pc.get_page_testimony_and_store(pnum=8)
]
with open('templates/interior_8.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Różaniec Historii Zbawienia - Broszura 8 Stron A5", "\n\n".join(pages_8)))
print("interior_8.html generated.")

# 3. Broszura 12 stron
pages_12 = [
    pc.get_page_cover_title(),
    pc.get_page_intro(pnum=2),
    pc.get_page_four_volumes(pnum=3),
    pc.get_page_digital_dimension(pnum=4),
    pc.get_page_calendar_architecture(pnum=5),
    pc.get_page_rgb_theology(pnum=6),
    pc.get_page_cmyk_theology(pnum=7),
    pc.get_page_paired_products(1, 2, pnum=8),
    pc.get_page_paired_products(3, 4, pnum=9),
    pc.get_page_paired_products(5, 6, pnum=10),
    pc.get_page_practice(pnum=11),
    pc.get_page_testimony_and_store(pnum=12)
]
with open('templates/interior_12.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Różaniec Historii Zbawienia - Broszura 12 Stron A5", "\n\n".join(pages_12)))
print("interior_12.html generated.")

# 4. Broszura 16 stron
toc_16 = [
    ("3", "Wprowadzenie i Misja Dzieła", "Fundament"),
    ("4", "Cztery Tomy „Widoków na Raj” (WnR365)", "Refleksja"),
    ("5", "Wymiar Cyfrowy & Serwis widokinaraj.pl", "Platforma"),
    ("6", "Harmonogram Roku i 175 Tajemnic", "Rytm Roku"),
    ("7", "Teologia Światła: Addytywny Schemat RGB", "Mistyka"),
    ("8", "Odwrócony CMYK i Cud Zbawienia na Krzyżu", "Pascha"),
    ("9", "Model 1: Pełny z Białym Krzyżem (RGB)", "Różaniec I"),
    ("10", "Model 2: Pełny z Czarnym Krzyżem (CMYK)", "Różaniec II"),
    ("11", "Model 3: Okrągła Dziesiątka Czarna", "Dziesiątka"),
    ("12", "Model 4: Okrągła Dziesiątka Biała", "Dziesiątka"),
    ("13", "Model 5: Lina z Czarnym Krzyżem", "Lina"),
    ("14", "Model 6: Lina z Białym Krzyżem", "Lina"),
    ("15", "Przewodnik Codziennej Praktyki (4 Kroki)", "Praktyka"),
    ("16", "Świadectwo Dominika i Oli & Sklep", "Kontakt")
]
pages_16 = [
    pc.get_page_cover_title(),
    pc.get_page_toc(toc_16, pnum=2),
    pc.get_page_intro(pnum=3),
    pc.get_page_four_volumes(pnum=4),
    pc.get_page_digital_dimension(pnum=5),
    pc.get_page_calendar_architecture(pnum=6),
    pc.get_page_rgb_theology(pnum=7),
    pc.get_page_cmyk_theology(pnum=8),
    pc.get_page_single_product(1, pnum=9),
    pc.get_page_single_product(2, pnum=10),
    pc.get_page_single_product(3, pnum=11),
    pc.get_page_single_product(4, pnum=12),
    pc.get_page_single_product(5, pnum=13),
    pc.get_page_single_product(6, pnum=14),
    pc.get_page_practice(pnum=15),
    pc.get_page_testimony_and_store(pnum=16)
]
with open('templates/interior_16.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Różaniec Historii Zbawienia - Broszura 16 Stron A5", "\n\n".join(pages_16)))
print("interior_16.html generated.")

# 5. Broszura 20 stron
toc_20 = [
    ("3", "Wprowadzenie do Drogi ku Światłu", "Fundament"),
    ("4", "Cztery Tomy „Widoków na Raj”", "Refleksja"),
    ("5", "Architektura 175 Tajemnic i Zegar 365 Dni", "Kalendarz"),
    ("6", "Centrum Chrystologiczne i Tajemnice Ciszy", "Etap IV"),
    ("7", "Dzieje Kościoła i Nowe Niebo (Paruzja)", "Etapy V–VII"),
    ("8", "Wymiar Cyfrowy: Serwis widokinaraj.pl", "Platforma"),
    ("9", "Teologia Światła: Schemat RGB", "Mistyka"),
    ("10", "Odwrócony CMYK i Odkupienie na Krzyżu", "Symbolika"),
    ("11", "Przewodnik po Rzemiośle i Kolekcji RHZ", "Rzemiosło"),
    ("12–17", "Katalog 6 Modeli Różańców RHZ", "Kolekcja"),
    ("18", "Cztery Kroki Codziennej Praktyki", "Praktyka"),
    ("19", "Modlitewnik RHZ i Akty Zawierzenia", "Modlitwy"),
    ("20", "Świadectwo Twórców & Oficjalny Sklep", "Kontakt")
]
pages_20 = [
    pc.get_page_cover_title(),
    pc.get_page_toc(toc_20, pnum=2),
    pc.get_page_intro(pnum=3),
    pc.get_page_four_volumes(pnum=4),
    pc.get_page_calendar_architecture(pnum=5),
    pc.get_page_christological_center(pnum=6),
    pc.get_page_church_and_parousia(pnum=7),
    pc.get_page_digital_dimension(pnum=8),
    pc.get_page_rgb_theology(pnum=9),
    pc.get_page_cmyk_theology(pnum=10),
    pc.get_page_collection_guide(pnum=11),
    pc.get_page_single_product(1, pnum=12),
    pc.get_page_single_product(2, pnum=13),
    pc.get_page_single_product(3, pnum=14),
    pc.get_page_single_product(4, pnum=15),
    pc.get_page_single_product(5, pnum=16),
    pc.get_page_single_product(6, pnum=17),
    pc.get_page_practice(pnum=18),
    pc.get_page_prayer_book(pnum=19),
    pc.get_page_testimony_and_store(pnum=20)
]
with open('templates/interior_20.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Różaniec Historii Zbawienia - Wydanie 20 Stron A5", "\n\n".join(pages_20)))
print("interior_20.html generated.")

# 6. Broszura 24 strony (Amazon KDP Minimum)
toc_24 = [
    ("3", "Wprowadzenie Teologiczne i Duchowe", "Fundament"),
    ("5", "Cztery Tomy „Widoków na Raj”", "Refleksja"),
    ("6", "Architektura 175 Tajemnic i Rytm 365 Dni", "Kalendarz"),
    ("7", "Centrum Chrystologiczne i Tajemnice Ciszy", "Etap IV"),
    ("8", "Dzieje Kościoła i Nowe Niebo (Paruzja)", "Etapy V–VII"),
    ("9", "Wymiar Cyfrowy: Serwis widokinaraj.pl", "Platforma"),
    ("10", "Teologia Światła i Addytywny Schemat RGB", "Mistyka"),
    ("11", "Odwrócony CMYK i Odkupienie na Krzyżu", "Symbolika"),
    ("12", "Święte Inskrypcje: „IN LOVE”, „M” i „J”", "Inskrypcje"),
    ("13", "Przewodnik po Rzemiośle Jubilerskim RHZ", "Rzemiosło"),
    ("14–19", "Katalog 6 Modeli Różańców (Strony 14–19)", "Katalog"),
    ("20", "Przewodnik Codziennej Praktyki (4 Kroki)", "Praktyka"),
    ("21", "Modlitewnik RHZ i Akty Oddania", "Modlitwy"),
    ("22", "Rachunek Sumienia w Świetle Barw", "Formacja"),
    ("23", "Świadectwa Modlących Się i Owoce Wiary", "Wspólnota"),
    ("24", "Świadectwo Dominika i Oli, Sklep & Błogosławieństwo", "Kontakt")
]
pages_24 = [
    pc.get_page_cover_title(),
    pc.get_page_editorial(pnum=2),
    pc.get_page_intro(pnum=3),
    pc.get_page_toc(toc_24, pnum=4),
    pc.get_page_four_volumes(pnum=5),
    pc.get_page_calendar_architecture(pnum=6),
    pc.get_page_christological_center(pnum=7),
    pc.get_page_church_and_parousia(pnum=8),
    pc.get_page_digital_dimension(pnum=9),
    pc.get_page_rgb_theology(pnum=10),
    pc.get_page_cmyk_theology(pnum=11),
    pc.get_page_inscriptions(pnum=12),
    pc.get_page_collection_guide(pnum=13),
    pc.get_page_single_product(1, pnum=14),
    pc.get_page_single_product(2, pnum=15),
    pc.get_page_single_product(3, pnum=16),
    pc.get_page_single_product(4, pnum=17),
    pc.get_page_single_product(5, pnum=18),
    pc.get_page_single_product(6, pnum=19),
    pc.get_page_practice(pnum=20),
    pc.get_page_prayer_book(pnum=21),
    pc.get_page_examination_of_conscience(pnum=22),
    pc.get_page_testimonies_list(pnum=23),
    pc.get_page_testimony_and_store(pnum=24)
]
with open('templates/interior_24.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Różaniec Historii Zbawienia - Amazon KDP 24 Strony A5", "\n\n".join(pages_24)))
print("interior_24.html generated.")

# 7. Broszura 28 stron (Amazon KDP Rozszerzone)
toc_28 = [
    ("3", "Wprowadzenie Teologiczne i Duchowe", "Fundament"),
    ("5", "Cztery Tomy „Widoków na Raj”", "Refleksja"),
    ("6", "Architektura 175 Tajemnic i Zegar 365 Dni", "Kalendarz"),
    ("7", "Siedem Epok Historii Zbawienia (Szczegóły)", "Struktura"),
    ("8", "Centrum Chrystologiczne i Zmartwychwstanie", "Etap IV"),
    ("9", "Mistyka Tajemnic Ciszy w Sercu Maryi", "Kontemplacja"),
    ("10", "Dzieje Kościoła i Nowe Niebo (Paruzja)", "Etapy V–VII"),
    ("11", "Wymiar Cyfrowy: Serwis widokinaraj.pl", "Platforma"),
    ("12", "Teologia Światła i Addytywny Schemat RGB", "Mistyka"),
    ("13", "Odwrócony CMYK i Zbawienie na Krzyżu", "Symbolika"),
    ("14", "Święte Inskrypcje: „IN LOVE”, „M” i „J”", "Inskrypcje"),
    ("15", "Przewodnik po Rzemiośle Jubilerskim RHZ", "Rzemiosło"),
    ("16–21", "Katalog 6 Modeli Różańców (Strony 16–21)", "Katalog"),
    ("22", "Przewodnik Codziennej Praktyki (4 Kroki)", "Praktyka"),
    ("23", "Rachunek Sumienia w Świetle Barw", "Formacja"),
    ("24", "Modlitewnik RHZ i Akty Oddania", "Modlitwy"),
    ("25", "Świadectwa Modlących Się i Owoce Wiary", "Wspólnota"),
    ("26", "Pakiety Formacyjne i Zestawy Podarunkowe", "Sklep"),
    ("27", "Świadectwo Dominika i Oli & Sklep Oficjalny", "Kontakt"),
    ("28", "Uroczyste Błogosławieństwo na Drogę Wiary", "Zwieńczenie")
]

page_28_blessing = """  <!-- STRONA 28: UROCZYSTE BŁOGOSŁAWIEŃSTWO -->
  <div class="page" style="justify-content: space-between; text-align: center;">
    <div class="page-header">
      <span>Zwieńczenie Drogi</span>
      <span>Błogosławieństwo</span>
    </div>

    <div>
      <svg width="44" height="62" viewBox="0 0 100 140" style="margin: 0 auto 8px auto; display: block; filter: drop-shadow(0 0 8px rgba(212,175,55,0.7));">
        <rect x="42" y="10" width="16" height="120" rx="4" fill="url(#goldGrad)" />
        <rect x="15" y="38" width="70" height="16" rx="4" fill="url(#goldGrad)" />
        <circle cx="50" cy="46" r="14" fill="none" stroke="#aa8214" stroke-width="2.5" />
      </svg>

      <h2 class="section-title" style="margin-bottom: 4px;">Niech Jasność Pana Cię Prowadzi</h2>
      <h3 class="section-subtitle" style="margin-bottom: 10px;">Błogosławieństwo na każdy dzień całorocznej wędrówki</h3>

      <div class="card" style="background: #fdfaf2; border: 1.5px solid var(--gold); padding: 10px 14px; margin-bottom: 10px; text-align: justify;">
        <p style="font-style: italic; line-height: 1.52; margin-bottom: 6px;">
          „Niech Pan ci błogosławi i niech cię strzeże. Niech Pan rozjaśni oblicze swe nad tobą i niech ci będzie miłościwy. Niech Pan zwróci ku tobie swoje oblicze i niech cię obdarzy pokojem.”
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.9); color: var(--gold-dark); font-weight: 700; margin: 0; text-align: right;">
          (Księga Liczb 6, 24–26)
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); text-align: justify; margin-bottom: 10px;">
        <p style="margin: 0; line-height: 1.48;">
          Wyruszając na drogę 365 dni z Różańcem Historii Zbawienia, pamiętaj: nie jesteś sam. Każdego dnia razem z Tobą modlą się tysiące serc w całym kraju, a Matka Boża otacza Cię swoim płaszczem miłości.
        </p>
      </div>

      <div style="margin-top: 8px;">
        <p style="font-family: 'Cinzel', serif; font-size: 11pt; color: var(--navy-deep); font-weight: 700; margin-bottom: 2px;">
          WWW.WIDOKINARAJ.PL
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.9); color: var(--text-muted); margin: 0;">
          Wydawnictwo „Widoki na Raj” &bull; Rok Pański 2026
        </p>
      </div>
    </div>

    <div class="page-footer">
      <span>AMAZON KDP EDITION</span>
      <span class="page-num">28</span>
    </div>
  </div>"""

pages_28 = [
    pc.get_page_cover_title(),
    pc.get_page_editorial(pnum=2),
    pc.get_page_intro(pnum=3),
    pc.get_page_toc(toc_28, pnum=4),
    pc.get_page_four_volumes(pnum=5),
    pc.get_page_calendar_architecture(pnum=6),
    pc.get_page_seven_stages_detail(pnum=7),
    pc.get_page_christological_center(pnum=8),
    pc.get_page_silence_mysteries(pnum=9),
    pc.get_page_church_and_parousia(pnum=10),
    pc.get_page_digital_dimension(pnum=11),
    pc.get_page_rgb_theology(pnum=12),
    pc.get_page_cmyk_theology(pnum=13),
    pc.get_page_inscriptions(pnum=14),
    pc.get_page_collection_guide(pnum=15),
    pc.get_page_single_product(1, pnum=16),
    pc.get_page_single_product(2, pnum=17),
    pc.get_page_single_product(3, pnum=18),
    pc.get_page_single_product(4, pnum=19),
    pc.get_page_single_product(5, pnum=20),
    pc.get_page_single_product(6, pnum=21),
    pc.get_page_practice(pnum=22),
    pc.get_page_examination_of_conscience(pnum=23),
    pc.get_page_prayer_book(pnum=24),
    pc.get_page_testimonies_list(pnum=25),
    pc.get_page_gift_packs(pnum=26),
    pc.get_page_testimony_and_store(pnum=27),
    page_28_blessing
]
with open('templates/interior_28.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Różaniec Historii Zbawienia - Amazon KDP 28 Stron A5", "\n\n".join(pages_28)))
print("interior_28.html generated.")

print("\n>>> ALL 7 INTERIOR TEMPLATES GENERATED SUCCESSFULLY! <<<")
