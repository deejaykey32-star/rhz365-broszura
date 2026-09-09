# -*- coding: utf-8 -*-
"""
page_components.py - Kompletny zestaw komponentów stron dla wszystkich 7 wariantów broszur RHZ365.
Wszystkie strony korzystają z var(--base-font-size, 12pt) i są zbalansowane pionowo.
"""

def get_page_cover_title(website_url="{{ website_url }}"):
    return f"""  <!-- STRONA 1: OKŁADKA / STRONA TYTUŁOWA Z PEŁNĄ TREŚCIĄ -->
  <div class="page cover-dark" style="justify-content: space-between; text-align: center;">
    <div>
      <div style="border: 1.5px solid var(--gold); padding: 4px 8px; border-radius: 4px; margin-bottom: 5px;">
        <p style="font-family: 'Cinzel', serif; font-size: 9pt; letter-spacing: 2px; color: var(--gold-light); margin: 0; text-align: center; text-transform: uppercase;">
          Oficjalny Przewodnik Duchowy i Wydawniczy
        </p>
      </div>

      <svg width="38" height="52" viewBox="0 0 100 140" style="margin: 0 auto 4px auto; display: block; filter: drop-shadow(0 0 8px rgba(212,175,55,0.7));">
        <rect x="42" y="10" width="16" height="120" rx="4" fill="url(#goldGrad)" />
        <rect x="15" y="38" width="70" height="16" rx="4" fill="url(#goldGrad)" />
        <circle cx="50" cy="46" r="14" fill="none" stroke="#fff" stroke-width="3" opacity="0.85" />
        <defs>
          <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fff4cc"/>
            <stop offset="50%" stop-color="#d4af37"/>
            <stop offset="100%" stop-color="#8a6409"/>
          </linearGradient>
        </defs>
      </svg>

      <h1 style="font-size: 15.5pt; letter-spacing: 1.2px; color: #ffffff; text-shadow: 0 2px 8px rgba(0,0,0,0.8); margin-bottom: 2px;">
        RÓŻANIEC HISTORII ZBAWIENIA
      </h1>
      <div style="width: 50px; height: 2px; background: var(--gold); margin: 2px auto 4px auto;"></div>
      <h2 style="font-size: 10.5pt; font-weight: 600; color: var(--gold-light); letter-spacing: 1.2px; margin-bottom: 5px;">
        RHZ365 &bull; WIDOKI NA RAJ &bull; 175 TAJEMNIC
      </h2>

      <!-- Blok wprowadzający: wymiar cyfrowy i fizyczny -->
      <div class="card-dark" style="text-align: justify; margin-bottom: 5px; background: rgba(12,23,40,0.78); border: 1px solid rgba(212,175,55,0.45); padding: 6px 9px;">
        <p style="font-size: var(--base-font-size); line-height: 1.42; color: #f1f5f9; margin-bottom: 4px;">
          <strong>Różaniec Historii Zbawienia</strong> to całoroczna droga kontemplacji dziejów zbawienia od stworzenia świata po Paruzję. Dzieło łączy w sobie dwa nierozerwalne wymiary:
        </p>
        <p style="font-size: var(--base-font-size); line-height: 1.4; color: #e2e8f0; margin-bottom: 4px;">
          🌐 <strong>Wymiar Cyfrowy (widokinaraj.pl):</strong> Nowoczesny portal z automatycznym odczytem przez lektora audio, interaktywną reprezentacją paciorków i rozważaniami z 4 tomów „Widoków na Raj”.
        </p>
        <p style="font-size: var(--base-font-size); line-height: 1.4; color: #e2e8f0; margin: 0;">
          📿 <strong>Wymiar Fizyczny (6 Modeli):</strong> Unikalna kolekcja różańców niosących tajemnicę Misji Barw i Kolorów (RGB i CMYK) – od białego i czarnego krzyża po inskrypcje miłości „IN LOVE”.
        </p>
      </div>

      <!-- Pismo Święte i Zachęta do zakupu -->
      <div class="card-dark" style="text-align: center; margin-bottom: 5px; background: rgba(212,175,55,0.12); border: 1.5px solid var(--gold); padding: 5px 9px;">
        <p style="font-size: var(--base-font-size); font-style: italic; color: #fef08a; margin-bottom: 2px;">
          „Światłość w ciemności świeci i ciemność jej nie ogarnęła.” (J 1, 5)
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.92); color: #ffffff; margin: 0;">
          Wybierz swój różaniec na <strong>{website_url}</strong> i wejdź na drogę codziennej modlitwy, która przemienia serce i wnosi Boży pokój.
        </p>
      </div>
    </div>

    <div>
      <div style="display: flex; justify-content: center; gap: 6px; flex-wrap: wrap; margin-bottom: 4px;">
        <span class="badge" style="background: rgba(255,255,255,0.16); color: #fff; border: 1px solid var(--gold);">365 Dni Modlitwy</span>
        <span class="badge" style="background: rgba(255,255,255,0.16); color: #fff; border: 1px solid var(--gold);">Lektor Online</span>
        <span class="badge" style="background: rgba(255,255,255,0.16); color: #fff; border: 1px solid var(--gold);">6 Modeli Różańców</span>
        <span class="badge" style="background: rgba(255,255,255,0.16); color: #fff; border: 1px solid var(--gold);">Tomy I–IV WnR</span>
      </div>
      <div class="page-footer" style="border-top-color: rgba(212,175,55,0.4); color: var(--gold-light);">
        <span>{website_url}</span>
        <span>WYDANIE DRUKARSKIE &bull; AMAZON KDP</span>
      </div>
    </div>
  </div>"""

def get_page_editorial(pnum=2, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: KARTA REDAKCYJNA I DEDYKACJA -->
  <div class="page" style="justify-content: space-between;">
    <div class="page-header">
      <span>Karta Redakcyjna</span>
      <span>Nota Wydawnicza</span>
    </div>

    <div>
      <h3 style="font-size: 13pt; color: var(--navy-deep); margin-bottom: 4px;">
        Różaniec Historii Zbawienia &bull; RHZ365
      </h3>
      <p class="lead" style="margin-bottom: 6px;">
        Integralna część dzieła i bloga <strong>„Widoki na Raj” (WnR365)</strong>.
      </p>

      <div class="card" style="margin-bottom: 6px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          Dedykacja Autorska
        </h4>
        <p style="font-style: italic; margin: 0; line-height: 1.42;">
          „Dzieło to z pokorą dedykujemy Matce Najświętszej oraz wszystkim rodzinom, małżonkom i osobom samotnym, które pośród trudów codzienności szukają światła nadziei. Niech każda odmówiona dziesiątka przynosi Boży pokój i umocnienie w wierze.”
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.88); color: var(--gold-dark); font-weight: 700; margin-top: 3px; text-align: right;">
          – Dominik i Ola
        </p>
      </div>

      <div class="card" style="background: #f8fafc; border-left: 3.5px solid var(--gold); margin-bottom: 6px;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          Nota Teologiczna i Prawna
        </h4>
        <p style="font-size: calc(var(--base-font-size) * 0.92); margin: 0; line-height: 1.4;">
          Autor tekstów i koncepcji duchowej pragnie z szacunkiem zaznaczyć, że publikacja nie stanowi nowego dogmatu wiary, lecz jest owocem osobistego natchnienia, medytacji Pisma Świętego i praktyki modlitewnej w łonie Kościoła Rzymskokatolickiego. Wszystkie prawa do koncepcji Misji Barw i Kolorów oraz układu RHZ365 są zastrzeżone.
        </p>
      </div>

      <div style="font-size: calc(var(--base-font-size) * 0.9); line-height: 1.4; color: var(--text-muted); border-top: 1px solid #e2e8f0; padding-top: 4px;">
        <p style="margin-bottom: 2px;"><strong>Oficjalny portal projektu:</strong> {website_url}</p>
        <p style="margin-bottom: 2px;"><strong>Format publikacji:</strong> A5 (148 &times; 210 mm) &bull; Druk na żądanie (Amazon KDP)</p>
        <p style="margin: 0;"><strong>Wydanie:</strong> I, 2026 &bull; Wszelkie prawa zastrzeżone.</p>
      </div>
    </div>

    <div class="page-footer">
      <span>NOTY WYDAWNICZE</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_intro(pnum=2, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: WPROWADZENIE & MISJA -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Różaniec Historii Zbawienia</span>
        <span>Wprowadzenie & Misja</span>
      </div>

      <h2 class="section-title">Droga ku Pełni Światła</h2>
      <h3 class="section-subtitle">Duchowy przewodnik po wielkich dziejach zbawienia człowieka</h3>

      <p class="lead">
        Trzymasz w dłoniach przewodnik po dziele niezwykłym. <strong>Różaniec Historii Zbawienia (RHZ365)</strong> to całoroczna wędrówka przez 175 tajemnic – od pierwszego błysku stworzenia w Księdze Rodzaju, przez przymierza patriarchów, Paschę Chrystusa, aż po chwalebny triumf Paruzji.
      </p>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 6px;">
        <h4 style="font-size: 11pt; color: var(--navy-deep); margin-bottom: 2px;">
          Dlaczego Różaniec Historii Zbawienia?
        </h4>
        <p style="margin: 0;">
          Tradycyjny różaniec koncentruje się na 20 tajemnicach Nowego Testamentu. RHZ365 rozszerza tę perspektywę na całą Biblię, ukazując, że całe dzieje świata są jednym wielkim poematem Bożej miłości ratującej człowieka z ciemności grzechu.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--gold); margin-bottom: 6px;">
        <h4 style="font-size: 11pt; color: var(--gold-dark); margin-bottom: 2px;">
          Nierozerwalna Jedność: Słowo, Dźwięk i Zmysły
        </h4>
        <p style="margin: 0;">
          Dzieło łączy lekturę czterech tomów rozważań <strong>„Widoki na Raj”</strong>, automatyczny odczyt przez lektora audio w serwisie <code>widokinaraj.pl</code> oraz fizyczny dotyk chłodnych paciorków z kamienia szlachetnego i drewna hebanowego.
        </p>
      </div>

      <div class="gold-box" style="margin: 0;">
        <strong>Zaproszenie do wędrówki:</strong> Nie musisz być teologiem ani mnichem. Wystarczy jeden kwadrans dziennie, by krok po kroku odnaleźć sens własnego życia w wielkim planie Boga.
      </div>
    </div>

    <div class="page-footer">
      <span>{website_url}</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_four_volumes(pnum=3, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: CZTERY TOMY WIDOKÓW NA RAJ -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Integralność Dzieła</span>
        <span>RHZ365 & WnR365</span>
      </div>

      <h2 class="section-title">Cztery Tomy „Widoków na Raj”</h2>
      <h3 class="section-subtitle">Duchowa literatura towarzysząca modlitwie w rytmie czterech pór roku</h3>

      <p class="lead">
        Modlitwie różańcowej RHZ365 towarzyszy czterotomowe dzieło literacko-duchowe <strong>„Widoki na Raj” (WnR365)</strong>. Każdy tom odpowiada porom roku w przyrodzie i etapom dojrzewania ludzkiej duszy:
      </p>

      <div style="display: flex; flex-direction: column; gap: 5px; margin-bottom: 6px;">
        <div style="background: #f1f5f9; padding: 6px 9px; border-radius: 4px; border-left: 3.5px solid #475569; font-size: var(--base-font-size);">
          <strong style="color: #1e293b;">Tom I – Ziemia (Zima):</strong> Czas ciszy, ogołocenia i tęsknoty za Utraconym Rajem. Odkrywanie korzeni wiary w przymierzach z Abrahamem, Izaakiem i Jakubem.
        </div>
        <div style="background: #f0fdf4; padding: 6px 9px; border-radius: 4px; border-left: 3.5px solid #16a34a; font-size: var(--base-font-size);">
          <strong style="color: #166534;">Tom II – Wiosna:</strong> Zwiastowanie, Wcielenie Słowa i publiczna działalność Jezusa. Rozkwit łaski, cudowne uzdrowienia i orędzie ośmiu błogosławieństw.
        </div>
        <div style="background: #fefce8; padding: 6px 9px; border-radius: 4px; border-left: 3.5px solid #ca8a04; font-size: var(--base-font-size);">
          <strong style="color: #854d0e;">Tom III – Lato:</strong> Pełnia światła i paschalny żar miłości. Wieczernik, Ogrójec, Męka na Krzyżu i poranek Zmartwychwstania – zwycięstwo życia nad śmiercią.
        </div>
        <div style="background: #fff7ed; padding: 6px 9px; border-radius: 4px; border-left: 3.5px solid #ea580c; font-size: var(--base-font-size);">
          <strong style="color: #9a3412;">Tom IV – Jesień:</strong> Zesłanie Ducha Świętego, misja apostolska Kościoła, świadectwo męczenników i zbieranie plonów wiary w perspektywie Paruzji.
        </div>
      </div>

      <div class="gold-box" style="margin: 0;">
        <strong>Skompletuj całą kolekcję:</strong> Cztery tomy rozważań są dostępne w wersji drukowanej oraz na platformie internetowej. Wspólnie z różańcem tworzą kompletną szkołę życia wewnętrznego.
      </div>
    </div>

    <div class="page-footer">
      <span>TOMY I–IV • WIDOKI NA RAJ</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_calendar_architecture(pnum=4, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: ARCHITEKTURA I KALENDARZ 365 DNI -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Architektura Modlitwy</span>
        <span>Cykl 365 Dni</span>
      </div>

      <h2 class="section-title">Architektura Roku Modlitwy</h2>
      <h3 class="section-subtitle">175 tajemnic ułożonych w matematycznie harmonijny rytm roku</h3>

      <div class="card" style="text-align: center; background: #fdfaf2; border: 1.5px solid var(--gold); padding: 5px 8px; margin-bottom: 5px;">
        <span style="font-family: 'Cinzel', serif; font-size: 11pt; font-weight: 700; color: var(--gold-dark);">
          7 Etapów &times; 5 Części &times; 5 Tajemnic = 175 Tajemnic Zbawienia
        </span>
        <p style="font-size: calc(var(--base-font-size) * 0.9); color: var(--text-muted); margin: 2px 0 0 0; text-align: center;">
          Dokładnie jedna tajemnica na każdy dzień &bull; Dwa pełne cykle w ciągu roku
        </p>
      </div>

      <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin: 3px 0 2px 0; text-transform: uppercase;">
        Struktura Siedmiu Wielkich Etapów
      </h4>
      <div style="font-size: var(--base-font-size); line-height: 1.4; margin-bottom: 4px;">
        <p style="margin-bottom: 2.5px;">
          <strong>Etapy I–III (Stary Testament):</strong> Od stworzenia świata, przez przymierza z Noem i Abrahamem, Wyjście z Egiptu, rządy królów i głosy proroków tęskniących za Mesjaszem.
        </p>
        <p style="margin-bottom: 2.5px;">
          <strong>Etap IV (Chrystus i Maryja):</strong> Serce historii zbawienia. Wcielenie, życie ukryte w Nazarecie, męka, śmierć, zmartwychwstanie oraz mistyczne <em>Tajemnice Ciszy</em>.
        </p>
        <p style="margin: 0;">
          <strong>Etapy V–VII (Kościół i Wieczność):</strong> Dzieje Apostolskie, świadectwo męczenników, zmagania wieków aż po ostateczny triumf Boga i Nowe Jeruzalem.
        </p>
      </div>

      <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin: 3px 0 2px 0; text-transform: uppercase;">
        Całoroczny Zegar Modlitwy (365 Dni)
      </h4>
      <div style="background: #ffffff; border: 1px solid var(--border-gold); border-radius: 4px; padding: 4px 7px; font-size: calc(var(--base-font-size) * 0.92); line-height: 1.38;">
        <div style="display: flex; justify-content: space-between;">
          <span><strong>I Cykl (175 dni):</strong> 25 grudnia – 17 czerwca</span>
          <span class="badge badge-gold">175 dni</span>
        </div>
        <div style="display: flex; justify-content: space-between; color: var(--text-muted);">
          <span><em>&bull; Letni Tydzień Ciszy i Refleksji:</em> 18 – 24 czerwca</span>
          <span>7 dni</span>
        </div>
        <div style="display: flex; justify-content: space-between;">
          <span><strong>II Cykl (175 dni):</strong> 25 czerwca – 16 grudnia</span>
          <span class="badge badge-gold">175 dni</span>
        </div>
        <div style="display: flex; justify-content: space-between; color: #991b1b;">
          <span><strong>&bull; Dzień Bożego Miłosierdzia:</strong> 17 grudnia (Koronka)</span>
          <span class="badge badge-rgb-r">1 dzień</span>
        </div>
        <div style="display: flex; justify-content: space-between; color: var(--text-muted);">
          <span><em>&bull; Tydzień Ciszy Adwentowej:</em> 18 – 24 grudnia</span>
          <span>7 dni</span>
        </div>
        <div style="border-top: 1px solid #e2e8f0; margin-top: 2px; padding-top: 2px; text-align: center; font-weight: 700; color: var(--navy-deep);">
          175 + 7 + 175 + 1 + 7 = 365 DNI BOŻEJ ŁASKI
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>{website_url}</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_seven_stages_detail(pnum=7, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: SZCZEGÓŁOWY WYKAZ 7 ETAPÓW -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Struktura RHZ365</span>
        <span>7 Etapów Zbawienia</span>
      </div>

      <h2 class="section-title">Siedem Epok Historii Zbawienia</h2>
      <h3 class="section-subtitle">Pełna panorama biblijna od Genesis po Dzień Pański</h3>

      <div style="display: flex; flex-direction: column; gap: 3px; font-size: calc(var(--base-font-size) * 0.94); line-height: 1.36; margin-bottom: 5px;">
        <div style="background: #ffffff; border: 1px solid var(--border-gold); padding: 4px 7px; border-radius: 4px;">
          <strong>Etap I &bull; Początek:</strong> Stworzenie świata, Eden, grzech pierworodny, obietnica Niewiasty (Protoewangelia) i przymierze z Noem.
        </div>
        <div style="background: #ffffff; border: 1px solid var(--border-gold); padding: 4px 7px; border-radius: 4px;">
          <strong>Etap II &bull; Przymierze:</strong> Wiara Abrahama, patriarchowie, Wyjście z Egiptu, prawo na Synaju i 40 lat wędrówki przez pustynię.
        </div>
        <div style="background: #ffffff; border: 1px solid var(--border-gold); padding: 4px 7px; border-radius: 4px;">
          <strong>Etap III &bull; Królestwo i Prorocy:</strong> Król Dawid, budowa Świątyni, niewola babilońska i pieśni proroków o Cierpiącym Słudze Jahwe.
        </div>
        <div style="background: #fdfaf2; border: 1.5px solid var(--gold); padding: 4px 7px; border-radius: 4px;">
          <strong>Etap IV &bull; Pełnia Czasu (Chrystus):</strong> Zwiastowanie, Boże Narodzenie, nauczanie, Tajemnice Ciszy, Męka, Krzyż i Zmartwychwstanie.
        </div>
        <div style="background: #ffffff; border: 1px solid var(--border-gold); padding: 4px 7px; border-radius: 4px;">
          <strong>Etap V &bull; Kościół:</strong> Zesłanie Ducha Świętego, chrzest pierwszych pogan, podróże św. Pawła i męczeństwo Piotra i Pawła.
        </div>
        <div style="background: #ffffff; border: 1px solid var(--border-gold); padding: 4px 7px; border-radius: 4px;">
          <strong>Etap VI &bull; Wieki Wiary:</strong> Zmagania z herezjami, ojcowie Kościoła, święci mistycy i świadectwo wiary w czasach wojen.
        </div>
        <div style="background: #ffffff; border: 1px solid var(--border-gold); padding: 4px 7px; border-radius: 4px;">
          <strong>Etap VII &bull; Paruzja:</strong> Ostateczny bój duchowy, zmartwychwstanie ciał, Sąd Ostateczny i wieczna chwała Nowego Jeruzalem.
        </div>
      </div>

      <div class="gold-box" style="margin: 0;">
        W każdym etapie znajduje się 25 tajemnic (5 części po 5 tajemnic), co daje łącznie dokładnie 175 dni modlitewnej kontemplacji.
      </div>
    </div>

    <div class="page-footer">
      <span>7 ETAPÓW &bull; STRUKTURA BIBLIJNA</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_digital_dimension(pnum=5, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: WYMIAR CYFROWY: WIDOKINARAJ.PL -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Forma Cyfrowa</span>
        <span>widokinaraj.pl</span>
      </div>

      <h2 class="section-title">Wymiar Cyfrowy Modlitwy</h2>
      <h3 class="section-subtitle">Platforma widokinaraj.pl – duchowe wsparcie dostępne o każdej porze</h3>

      <p class="lead">
        Współczesne tempo życia stawia przed nami wyzwanie pośpiechu i rozproszenia. Odpowiedzią na tę potrzebę jest dedykowany serwis <strong>widokinaraj.pl</strong>, który przenosi Różaniec Historii Zbawienia w intuicyjną, przejrzystą przestrzeń cyfrową.
      </p>

      <div class="card" style="border-left: 3.5px solid var(--gold-dark); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          🎧 Automatyczny Odczyt Przez Lektora Audio
        </h4>
        <p style="margin: 0;">
          Każdego dnia serwis oferuje odtworzenie pełnej modlitwy i rozważania czytanego przez profesjonalnego lektora. Spokojny głos pozwala modlić się podczas jazdy samochodem, spaceru, odpoczynku czy w chorobie, gdy czytanie bywa utrudnione.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--blue-rgb); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          📿 Cyfrowa Reprezentacja Różańca
        </h4>
        <p style="margin: 0;">
          Interaktywny interfejs na ekranie smartfona lub komputera dynamicznie wskazuje aktualną dziesiątkę, koralik oraz kolor przypisany do danej tajemnicy. Pozwala to śledzić modlitwę w skupieniu i uczyć się głębokiej symboliki Misji Barw i Kolorów.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--green-rgb); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          📖 Synchronizacja z Kalendarzem Liturgicznym
        </h4>
        <p style="margin: 0;">
          Po wejściu na stronę natychmiast wyświetla się tajemnica przypadająca na bieżący dzień roku. Masz wgląd w wersety Pisma Świętego, komentarze ojców Kościoła oraz pytania pomagające zastosować Słowo we własnym życiu.
        </p>
      </div>

      <div class="gold-box" style="text-align: center; margin: 0;">
        <span style="font-weight: 700; color: var(--navy-deep);">Bezpłatny dostęp na każdym urządzeniu:</span><br>
        <span style="font-family: 'Cinzel', serif; font-size: 11pt; color: var(--gold-dark); font-weight: 700;">
          {website_url}
        </span>
      </div>
    </div>

    <div class="page-footer">
      <span>SERWIS INTERNETOWY &bull; AUDIO & WEB</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_rgb_theology(pnum=6, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: TEOLOGIA ŚWIATŁA (RGB) -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Teologia Światła</span>
        <span>Misja Barw i Kolorów</span>
      </div>

      <h2 class="section-title">Teologia Światła: Schemat RGB</h2>
      <h3 class="section-subtitle">„Bóg oddzielił światłość od ciemności i było to dobre” (Rdz 1, 4)</h3>

      <p>
        Wszystkie 6 modeli różańców RHZ niosą w sobie tajemnicę <strong>Misji Barw i Kolorów</strong>. To głęboko przemyślana katecheza oparta na biblijnej prawdzie o stworzeniu, upadku i odkupieniu człowieka.
      </p>

      <!-- SVG Diagram RGB -->
      <div style="text-align: center; margin: 3px 0 5px 0;">
        <svg width="170" height="70" viewBox="0 0 240 100" style="margin: 0 auto; display: block;">
          <circle cx="95" cy="45" r="35" fill="rgba(220, 38, 38, 0.75)" />
          <circle cx="145" cy="45" r="35" fill="rgba(5, 150, 105, 0.75)" />
          <circle cx="120" cy="75" r="35" fill="rgba(37, 99, 235, 0.75)" />
          <circle cx="120" cy="52" r="13" fill="#ffffff" filter="drop-shadow(0 0 5px #fff)" />
          <text x="120" y="55" font-family="'Cinzel', serif" font-size="7" font-weight="700" fill="#1e293b" text-anchor="middle">BIEL</text>
          <text x="70" y="35" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="700" fill="#dc2626">R - Jezus</text>
          <text x="170" y="35" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="700" fill="#059669">G - Duch Św.</text>
          <text x="120" y="98" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="700" fill="#2563eb" text-anchor="middle">B - Ojciec</text>
        </svg>
      </div>

      <div class="card" style="background: #f8fafc; margin-bottom: 4px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          Addytywny Kod Światła Bożej Chwały
        </h4>
        <p style="margin: 0;">
          W optyce fizycznej barwy addytywne (Red, Green, Blue) to składowe czystego światła. Nałożone na siebie w pełni tworzą <strong>czystą Biel</strong> – symbol Bożej świętości. W połowie tworzą <strong>szarość</strong> (ludzka letniość), a wyłączone stają się <strong>przezroczystością w ciemności</strong>, gdyż światło w ciemności świeci.
        </p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 3px; margin-bottom: 4px;">
        <div style="display: flex; align-items: center; gap: 5px; background: #fff5f5; padding: 2.5px 5px; border-radius: 4px; border: 1px solid #fed7d7;">
          <span class="badge badge-rgb-r" style="width: 18px; text-align: center;">R</span>
          <span style="font-size: var(--base-font-size);"><strong>Czerwony &bull; Jezus Chrystus:</strong> Wiara, Krew Przymierza, miłość ofiarna aż po krzyż.</span>
        </div>
        <div style="display: flex; align-items: center; gap: 5px; background: #f0fdf4; padding: 2.5px 5px; border-radius: 4px; border: 1px solid #bbf7d0;">
          <span class="badge badge-rgb-g" style="width: 18px; text-align: center;">G</span>
          <span style="font-size: var(--base-font-size);"><strong>Zielony &bull; Duch Święty:</strong> Nadzieja, nowe życie, odnowienie oblicza ziemi.</span>
        </div>
        <div style="display: flex; align-items: center; gap: 5px; background: #eff6ff; padding: 2.5px 5px; border-radius: 4px; border: 1px solid #bfdbfe;">
          <span class="badge badge-rgb-b" style="width: 18px; text-align: center;">B</span>
          <span style="font-size: var(--base-font-size);"><strong>Niebieski &bull; Bóg Ojciec:</strong> Nieskończona Miłość Stwórcy, Królestwo Niebieskie.</span>
        </div>
      </div>

      <div class="gold-box" style="margin: 0;">
        Pomiędzy przezroczystymi koralikami początku różańca umieszczone są te trzy barwy RGB, wskazując, że całe dzieło stworzenia i odkupienia wypływa z Trójcy Przenajświętszej.
      </div>
    </div>

    <div class="page-footer">
      <span>SCHEMAT RGB &bull; ŚWIATŁO BOŻE</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_cmyk_theology(pnum=7, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: ODWRÓCONY CMYK & ODKUPIENIE -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Mistyka Odkupienia</span>
        <span>CMYK & Zbawienie Krzyża</span>
      </div>

      <h2 class="section-title">Zdrada i Cud Odkupienia</h2>
      <h3 class="section-subtitle">Odwrócony schemat CMYK oraz tajemnica przemiany Y w R</h3>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          Subtraktywny Schemat CMYK – Materia i Grzech
        </h4>
        <p style="margin: 0;">
          Podczas gdy RGB jest światłem niefizycznym, schemat CMYK stosowany w druku symbolizuje to, co ziemskie i zniszczalne. <strong>K (Kontrast)</strong> to czarny pigment ziemi – proch, z którego człowiek powstał i do którego wraca.
        </p>
      </div>

      <!-- SVG Diagram Y -> R -->
      <div style="text-align: center; margin: 3px 0 5px 0;">
        <svg width="210" height="38" viewBox="0 0 280 48" style="margin: 0 auto; display: block;">
          <rect x="10" y="8" width="55" height="30" rx="4" fill="#ca8a04" />
          <text x="37" y="28" font-family="'Cinzel', serif" font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">Y (Zdrada)</text>
          <path d="M 75 23 L 115 23" stroke="#aa8214" stroke-width="2.5" stroke-dasharray="4,3" />
          <polygon points="120,23 112,18 112,28" fill="#aa8214" />
          <text x="96" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="700" fill="#aa8214" text-anchor="middle">KRZYŻ</text>
          <rect x="130" y="8" width="55" height="30" rx="4" fill="#dc2626" />
          <text x="157" y="28" font-family="'Cinzel', serif" font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">R (Miłość)</text>
          <path d="M 195 23 L 225 23" stroke="#aa8214" stroke-width="2" />
          <polygon points="230,23 222,19 222,27" fill="#aa8214" />
          <rect x="235" y="8" width="38" height="30" rx="4" fill="#166534" />
          <text x="254" y="28" font-family="'Cinzel', serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="middle">ŻYCIE</text>
        </svg>
      </div>

      <div class="card" style="background: #fff8f8; border-left: 3.5px solid #dc2626; margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: #991b1b; margin-bottom: 2px;">
          Tajemnica Przejścia Judasza (Y &rarr; R)
        </h4>
        <p style="margin: 0;">
          W odwróconym schemacie barw <strong>Żółty (Y)</strong> to zdrada Judasza za 30 srebrników. <strong>Fiolet (M)</strong> to pycha człowieka, a <strong>Turkus (C)</strong> to gorzka rozpacz. Przejście koloru żółtego w czerwony jest szczytem Ewangelii: Bóg potrafi największy grzech zdrady człowieka przemienić w krew odkupienia na Krzyżu!
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--gold); margin: 0;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          Paciorki „IN LOVE” oraz „M” i „J”
        </h4>
        <p style="margin: 0;">
          Koraliki z literami <strong>„I”</strong> oraz <strong>„N”</strong> w połączeniu z rozdzielnikami <strong>„L”, „O”, „V”, „E”</strong> tworzą wyznanie: <strong>IN LOVE</strong> – człowiek zanurzony w Bożej Miłości. Litery <strong>„M”</strong> (Maryja / Miłość) i <strong>„J”</strong> (Jezus / Jedność) przypominają: przez Matkę Twoje „Ja” staje się świątynią Zbawiciela.
        </p>
      </div>
    </div>

    <div class="page-footer">
      <span>SYMBOLIKA &bull; CMYK I ODKUPIENIE</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_inscriptions(pnum=14, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: ŚWIĘTE INSKRYPCJE IN LOVE, M I J -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Święte Inskrypcje</span>
        <span>IN LOVE &bull; M &bull; J</span>
      </div>

      <h2 class="section-title">Tajemnica Miłości: IN LOVE</h2>
      <h3 class="section-subtitle">Mistyka inskrypcji literowych na paciorkach różańca RHZ</h3>

      <p class="lead">
        Paciorki różańca RHZ to nie tylko narzędzie odliczania modlitw, ale precyzyjny alfabet duchowy, w którym każda litera niesie głębokie przesłanie biblijne.
      </p>

      <div class="card" style="border-left: 3.5px solid var(--gold); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          Paciorki Wstępne: „I” oraz „N”
        </h4>
        <p style="margin: 0;">
          Na początku różańca, przed i za barwami RGB, umieszczone są przezroczyste paciorki z literami <strong>„I”</strong> oraz <strong>„N”</strong>. W połączeniu z rozdzielnikami <strong>„L”, „O”, „V”, „E”</strong> pomiędzy dziesiątkami, tworzą one święte zdanie: <strong>IN LOVE</strong>. Cały świat i całe Twoje życie jest zanurzone <em>W MIŁOŚCI</em> Boga.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          Paciorki Łącznikowe: „M” i „J”
        </h4>
        <p style="margin-bottom: 3px;">
          W dziesiątkach i sznurach modlitewnych kluczową rolę odgrywają litery <strong>„M”</strong> oraz <strong>„J”</strong>:
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.95); margin: 0;">
          &bull; <strong>„M” (Matka / Miłość / Maryja):</strong> Niewiasta, która zmiażdżyła głowę węża. Pośredniczka łask i wzór cichego zaufania.<br>
          &bull; <strong>„J” (Jezus / Jedność / Twoje „Ja”):</strong> Cel modlitwy. Twoje ludzkie „Ja” zostaje przez Serce Matki zjednoczone z Najświętszym Sercem Zbawiciela.
        </p>
      </div>

      <div class="gold-box" style="margin: 0;">
        <strong>Kielich z Hostią i Winem:</strong> Wszystkie litery i paciorki prowadzą do Kielicha – sakramentalnego Źródła Życia Wiecznego. Bez Eucharystii modlitwa usycha; w Eucharystii staje się źródłem wody żywej.
      </div>
    </div>

    <div class="page-footer">
      <span>{website_url}</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_collection_guide(pnum=8, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: PRZEWODNIK PO KOLEKCJI RÓŻAŃCÓW -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Kolekcja Rzemieślnicza</span>
        <span>6 Modeli Różańców</span>
      </div>

      <h2 class="section-title">Kolekcja Fizycznych Różańców</h2>
      <h3 class="section-subtitle">Szlachetne znaki wiary wykonane ręcznie w pracowni jubilerskiej</h3>

      <p class="lead">
        Dlaczego warto modlić się z fizycznym różańcem w dłoni? Ponieważ człowiek modli się całym sobą – duszą, umysłem i ciałem. Ciężar krzyża, chłód naturalnego kamienia i gładkość pereł pomagają wyciszyć gonitwę myśli i zakotwiczyć serce w Bożej obecności.
      </p>

      <div class="card" style="margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          💎 Wyselekcjonowane Materiały Szlachetne
        </h4>
        <p style="margin: 0;">
          Każdy egzemplarz powstaje z naturalnego <strong>czarnego onyksu</strong>, <strong>prawdziwych pereł</strong>, szlachetnego szkła optycznego o barwach rubinu, szmaragdu i szafiru oraz twardego <strong>drewna hebanowego</strong>, połączonych odporną na zerwanie linką stalową.
        </p>
      </div>

      <div style="font-size: var(--base-font-size); line-height: 1.4; margin-bottom: 5px;">
        <p style="margin-bottom: 2.5px;">
          <strong>1. Różańce Pełne (Modele 1 & 2):</strong> Klasyczny 50-paciorkowy wieniec modlitewny z kielichem przymierza. Dwa warianty: Droga ku Światłu (Biały Krzyż) oraz Odkupienie z Ciemności (Czarny Krzyż).
        </p>
        <p style="margin-bottom: 2.5px;">
          <strong>2. Okrągłe Dziesiątki (Modele 3 & 4):</strong> Zamknięta, poręczna pętla – niezastąpiona do modlitwy w samochodzie, torebce czy kieszeni garnituru.
        </p>
        <p style="margin: 0;">
          <strong>3. Proste w Formie Liny (Modele 5 & 6):</strong> Monastyczny sznur modlitewny inspirowany czotkami pustelników – prosty układ liniowy do trzymania w dłoni.
        </p>
      </div>

      <div class="buy-card" style="margin: 0;">
        <h4>Wybierz Swój Osobisty Znak Wiary</h4>
        <p>
          Różańce RHZ to piękny dar sakramentalny na chrzest, bierzmowanie, ślub lub jubileusz. Każdy różaniec dostarczany jest w welurowym etui z certyfikatem.
        </p>
        <span class="buy-btn">Kup na {website_url}</span>
      </div>
    </div>

    <div class="page-footer">
      <span>RZEMIOSŁO &bull; KOLEKCJA RHZ</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_six_products_grid(pnum=3, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: 6 MODELI RÓŻAŃCÓW (SIATKA) -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Fizyczny Wymiar Modlitwy</span>
        <span>Kolekcja 6 Modeli Różańców</span>
      </div>

      <h2 class="section-title">Kolekcja Fizycznych Różańców</h2>
      <h3 class="section-subtitle">Dotyk wiary – sześć unikalnych narzędzi kontemplacji Tajemnicy Zbawienia</h3>

      <div class="rosaries-grid-6">
        <!-- Model 1 -->
        <div class="rosary-item-box">
          <img src="images/model1_pelny_bialy.jpg" alt="Model 1">
          <div class="rosary-item-text">
            <h4>1. Pełny z Białym Krzyżem</h4>
            <p>Biały krzyż, 10 onyksów, 30 RGB, 10 pereł, paciorki IN LOVE. Mistyczny różaniec światłości.</p>
            <a href="https://widokinaraj.pl" class="buy-btn-mini">Zamów &raquo;</a>
          </div>
        </div>

        <!-- Model 2 -->
        <div class="rosary-item-box">
          <img src="images/model2_pelny_czarny.jpg" alt="Model 2">
          <div class="rosary-item-text">
            <h4>2. Pełny z Czarnym Krzyżem</h4>
            <p>Czarny hebanowy krzyż, odwrócony CMYK, przejście Judasza (Y&rarr;R). Różaniec pokuty i ofiary.</p>
            <a href="https://widokinaraj.pl" class="buy-btn-mini">Zamów &raquo;</a>
          </div>
        </div>

        <!-- Model 3 -->
        <div class="rosary-item-box">
          <img src="images/model3_okragly_czarny.jpg" alt="Model 3">
          <div class="rosary-item-text">
            <h4>3. Dziesiątka z Czarnym Krzyżem</h4>
            <p>Kompaktowa pętla z czarnym krzyżykiem. Idealna do kieszeni, w drogę i do samochodu.</p>
            <a href="https://widokinaraj.pl" class="buy-btn-mini">Zamów &raquo;</a>
          </div>
        </div>

        <!-- Model 4 -->
        <div class="rosary-item-box">
          <img src="images/model4_okragly_bialy.jpg" alt="Model 4">
          <div class="rosary-item-text">
            <h4>4. Dziesiątka z Białym Krzyżem</h4>
            <p>Biały krzyżyk z koralowca/ceramiki, sekwencja C-M-Y ku bieli RGB. Dyskretna i elegancka.</p>
            <a href="https://widokinaraj.pl" class="buy-btn-mini">Zamów &raquo;</a>
          </div>
        </div>

        <!-- Model 5 -->
        <div class="rosary-item-box">
          <img src="images/model5_lina_czarny.jpg" alt="Model 5">
          <div class="rosary-item-text">
            <h4>5. Lina z Czarnym Krzyżem</h4>
            <p>Otwarty sznur modlitewny inspirowany czotkami pustelników. Symbol pielgrzymiego trudu.</p>
            <a href="https://widokinaraj.pl" class="buy-btn-mini">Zamów &raquo;</a>
          </div>
        </div>

        <!-- Model 6 -->
        <div class="rosary-item-box">
          <img src="images/model6_lina_bialy.jpg" alt="Model 6">
          <div class="rosary-item-text">
            <h4>6. Lina z Białym Krzyżem</h4>
            <p>Biały sznur z czystym krzyżem Paruzji zwieńczającym modlitwę. Symbol zmartwychwstania.</p>
            <a href="https://widokinaraj.pl" class="buy-btn-mini">Zamów &raquo;</a>
          </div>
        </div>
      </div>

      <div style="background: #fdfaf2; border: 1px solid var(--border-gold); border-radius: 4px; padding: 4px 7px; text-align: center; margin-top: 3px; font-size: calc(var(--base-font-size) * 0.9);">
        Każdy różaniec wykonywany jest ręcznie z wyselekcjonowanych kamieni szlachetnych i hebanu.
      </div>
    </div>

    <div class="page-footer">
      <span>{website_url}</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_digital_and_theology_4p(pnum=2, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA 2 DLA 4 STRON: CYFROWY & TEOLOGIA BARW -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Wymiar Cyfrowy & Teologia Barw</span>
        <span>widokinaraj.pl &bull; RHZ365</span>
      </div>

      <h2 class="section-title">Cyfrowa Droga i Tajemnica Barw</h2>
      <h3 class="section-subtitle">Połączenie modlitwy online z mistyką kolorów Bożego Objawienia</h3>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          🌐 Serwis widokinaraj.pl & Lektor Audio
        </h4>
        <p style="margin-bottom: 3px;">
          Różaniec Historii Zbawienia to 175 tajemnic w rytmie 365 dni roku (I cykl 175 dni, tydzień ciszy, II cykl 175 dni, Dzień Bożego Miłosierdzia i tydzień adwentowy) z <strong>Czterema Tomami „Widoków na Raj”</strong>.
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.92); color: var(--text-muted); margin: 0;">
          &bull; <strong>Lektor Audio:</strong> Automatyczne odczytywanie medytacji bez konieczności przewijania.<br>
          &bull; <strong>Cyfrowy Różaniec:</strong> Wizualizacja koralików i prowadzenie przez każdy etap modlitwy.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--gold); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          ✨ Misja Barw: Addytywne RGB i Odwrócony CMYK
        </h4>
        <div class="grid-2" style="gap: 6px;">
          <div style="background: #fdfaf2; padding: 4px 6px; border-radius: 4px; border: 1px solid #f1e4c3; font-size: calc(var(--base-font-size) * 0.9);">
            <strong style="color: var(--navy-deep);">Biel Światła (RGB):</strong><br>
            Czyste światło Bożej chwały. Trzy barwy podstawowe:
            <span class="badge badge-rgb-r">R - Jezus</span>
            <span class="badge badge-rgb-g">G - Duch Św.</span>
            <span class="badge badge-rgb-b">B - Ojciec</span>.
            Wszystkie razem tworzą nieskalaną biel światłości.
          </div>
          <div style="background: #fdf8f6; padding: 4px 6px; border-radius: 4px; border: 1px solid #fed7aa; font-size: calc(var(--base-font-size) * 0.9);">
            <strong style="color: #9a3412;\">Odwrócony CMYK:</strong><br>
            Grzech jako rozbicie kryształu. <strong>K (proch)</strong>, <strong>Y (zdrada Judasza)</strong>, <strong>M (pycha)</strong>, <strong>C (rozpacz)</strong>. Cud Krzyża obraca zdradę (Y) w krew i miłość (R).
          </div>
        </div>
      </div>

      <div class="gold-box" style="margin: 0;">
        <strong>Inskrypcje „IN LOVE” oraz „M” i „J”:</strong> Koraliki „I” i „N” obejmujące barwy RGB tworzą zdanie: <em>Zanurzeni w Bożej Miłości</em>. Koraliki Maryi (M) i Jezusa (J) jednoczą ludzkie „Ja” z sercem Odkupiciela.
      </div>
    </div>

    <div class="page-footer">
      <span>{website_url}</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_paired_products(m1, m2, pnum, website_url="{{ website_url }}"):
    prod_data = {
        1: ("Model 1: Pełny z Białym Krzyżem", "images/model1_pelny_bialy.jpg",
            "Klasyczny pełny różaniec światłości Bożej. Zwieńczony śnieżnobiałym krzyżem Zmartwychwstania.",
            ["10 czarnych onyksów (przejście przez ciemność)", "30 paciorków w barwach RGB (światłość Boża)", "10 pereł oraz paciorki IN LOVE"]),
        2: ("Model 2: Pełny z Czarnym Krzyżem", "images/model2_pelny_czarny.jpg",
            "Różaniec z hebanowym krzyżem przypominającym o cenie odkupienia i odwróconym CMYK.",
            ["Paciorki CMYK obrazujące drogę wyjścia z grzechu", "Przemiana zdrady Judasza (Y) w krew Krzyża (R)", "Paciorki łącznikowe „M” i „J” w srebrnej oprawie"]),
        3: ("Model 3: Okrągła Dziesiątka Czarna", "images/model3_okragly_czarny.jpg",
            "Zamknięta pętla modlitewna z hebanowym krzyżykiem. Znakomity do kieszeni i do auta.",
            ["Pętla powracająca do kielicha przebaczenia", "Odporne kamienie w kodzie barwnym", "Solidne wiązanie na stalowej lince jubilerskiej"]),
        4: ("Model 4: Okrągła Dziesiątka Biała", "images/model4_okragly_bialy.jpg",
            "Elegancka dziesiątka zwieńczona białym krzyżykiem. Przypomnienie o czystości serca.",
            ["Sekwencja barw od ciemności CMY do światła RGB", "Subtelna, lekka i poręczna konstrukcja", "Idealny dar sakramentalny na bierzmowanie lub ślub"]),
        5: ("Model 5: Lina z Czarnym Krzyżem", "images/model5_lina_czarny.jpg",
            "Otwarta forma liny inspirowana czotkami mnichów. Pielgrzymi sznur modlitewny.",
            ["Gęsto plecione, odporne włókno spadochronowe", "Krzyż z surowego hebanu afrykańskiego", "Niezwykła trwałość w trudnych warunkach"]),
        6: ("Model 6: Lina z Białym Krzyżem", "images/model6_lina_bialy.jpg",
            "Świetlista lina zakończona białym krzyżem Paruzji. Lina ocalenia rzucona człowiekowi.",
            ["Śnieżnobiały splot z barwnymi akcentami RGB", "Biały krzyż Zmartwychwstania zwieńczający modlitwę", "Ulubiony model młodzieży i ewangelizatorów"])
    }

    t1, img1, desc1, b1 = prod_data[m1]
    t2, img2, desc2, b2 = prod_data[m2]

    li1 = "\n".join([f"                <li>{b}</li>" for b in b1])
    li2 = "\n".join([f"                <li>{b}</li>" for b in b2])

    return f"""  <!-- STRONA: MODELE {m1} & {m2} -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Kolekcja Różańców RHZ</span>
        <span>Modele {m1} & {m2}</span>
      </div>

      <h2 class="section-title">Modele {m1} i {m2} Różańców</h2>
      <h3 class="section-subtitle">Namacalne narzędzia modlitwy w kodzie barwnym RGB i CMYK</h3>

      <div class="pair-layout">
        <!-- Model {m1} -->
        <div class="product-row-card">
          <img src="{img1}" alt="{t1}">
          <div class="product-row-info">
            <div>
              <h4>{t1}</h4>
              <p>{desc1}</p>
              <ul>
{li1}
              </ul>
            </div>
            <a href="https://widokinaraj.pl" class="buy-btn-small">Zamów na widokinaraj.pl &raquo;</a>
          </div>
        </div>

        <!-- Model {m2} -->
        <div class="product-row-card">
          <img src="{img2}" alt="{t2}">
          <div class="product-row-info">
            <div>
              <h4>{t2}</h4>
              <p>{desc2}</p>
              <ul>
{li2}
              </ul>
            </div>
            <a href="https://widokinaraj.pl" class="buy-btn-small">Zamów na widokinaraj.pl &raquo;</a>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>{website_url}</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_single_product(model_num, pnum, website_url="{{ website_url }}"):
    specs = {
        1: {
            "title": "Model 1: Droga ku Światłu",
            "subtitle": "Pełny różaniec tradycyjny z białym krzyżem w schemacie RGB",
            "img": "images/model1_pelny_bialy.jpg",
            "bg": "#ffffff",
            "spec": [
                "<strong>Biały Krzyż:</strong> Prowadzi od ciemności do czystego światła Bożej chwały.",
                "<strong>Paciorki Wstępne:</strong> Przezroczyste „I” i „N”, a pomiędzy nimi barwy RGB (czerwony, zielony, niebieski).",
                "<strong>Łącznik:</strong> Złoty Kielich z Hostią i Winem Przymierza.",
                "<strong>Koronka 50 Paciorków:</strong> 10 onyksów, 30 paciorków RGB (Rubin, Szmaragd, Szafir), 10 pereł chwały.",
                "<strong>Napis „IN LOVE”:</strong> Koraliki rozdzielające L-O-V-E w dziesiątkach."
            ],
            "card_title": "Zamów Model 1",
            "card_desc": "Idealny do uroczystej modlitwy rodzinnej i osobistej kontemplacji.",
            "footer_tag": "MODEL 1 • BIAŁY KRZYŻ RGB"
        },
        2: {
            "title": "Model 2: Odkupienie z Ciemności",
            "subtitle": "Pełny różaniec z czarnym krzyżem w schemacie odwróconego CMYK",
            "img": "images/model2_pelny_czarny.jpg",
            "bg": "#09111e",
            "spec": [
                "<strong>Czarny Krzyż (Heban):</strong> Zstąpienie Chrystusa w mrok grzechu, by wyprowadzić nas do życia.",
                "<strong>Paciorki Wstępne:</strong> Koralik „I” &rarr; Czerwony (Wiara) &rarr; Zielony (Nadzieja) &rarr; Niebieski (Miłość) &rarr; „N”.",
                "<strong>Łącznik:</strong> Kielich z Hostią i Najświętszą Krwią.",
                "<strong>Koronka 50 Paciorków:</strong> 10 czarnych koralików ziemi, 30 paciorków w odwróconym CMYK, 10 pereł chwały.",
                "<strong>Tajemnica Krzyża:</strong> Przemiana zdrady Judasza (Y) w krew zbawienia (R)."
            ],
            "card_title": "Zamów Model 2",
            "card_desc": "Mocny znak wiary dla osób przeżywających trudne próby życiowe.",
            "footer_tag": "MODEL 2 • CZARNY KRZYŻ CMYK"
        },
        3: {
            "title": "Model 3: Okrągła Dziesiątka Czarna",
            "subtitle": "Kompaktowy różaniec pętlowy z czarnym krzyżykiem hebanowym",
            "img": "images/model3_okragly_czarny.jpg",
            "bg": "#ffffff",
            "spec": [
                "<strong>Czarny Krzyżyk:</strong> Znak wierności Bogu w prozie codziennych obowiązków.",
                "<strong>Paciorki „M” i „J”:</strong> Maryja (Miłość) prowadzi do zjednoczenia Twojego „Ja” z Jezusem.",
                "<strong>Łącznik:</strong> Miniaturowy Kielich eucharystyczny.",
                "<strong>10 Koralików Pętli:</strong> Czarny K, Szary, Y (żółty), M (fiolet), C (turkus), B (błękit), G (zieleń), R (czerwień), Szary, Biały &rarr; powrót do Kielicha.",
                "<strong>Przeznaczenie:</strong> Do kieszeni, torebki lub na lusterko w aucie."
            ],
            "card_title": "Zamów Model 3",
            "card_desc": "Niezastąpiony różaniec samochodowy na jedną dziesiątkę dziennie.",
            "footer_tag": "MODEL 3 • OKRĄGŁA DZIESIĄTKA"
        },
        4: {
            "title": "Model 4: Okrągła Dziesiątka Biała",
            "subtitle": "Świetlista dziesiątka z białym krzyżykiem z koralowca",
            "img": "images/model4_okragly_bialy.jpg",
            "bg": "#ffffff",
            "spec": [
                "<strong>Biały Krzyżyk:</strong> Znak chwały zmartwychwstania i obecności Anioła Stróża.",
                "<strong>Paciorki „M” i „J”:</strong> Przez Serce Maryi do zjednoczenia z Chrystusem.",
                "<strong>Kielich z Hostią:</strong> Sakramentalne źródło łaski.",
                "<strong>Sekwencja Dziesiątki:</strong> Ciemność materii (Czarny, Szary) &rarr; C-M-Y &rarr; przejście w R-G-B &rarr; Biel zbawienia.",
                "<strong>Wyjątkowa lekkość:</strong> Elegancka, trwała konstrukcja jubilerska."
            ],
            "card_title": "Zamów Model 4",
            "card_desc": "Subtelny podarunek na I Komunię, bierzmowanie lub ślub.",
            "footer_tag": "MODEL 4 • DZIESIĄTKA BIAŁA"
        },
        5: {
            "title": "Model 5: Lina z Czarnym Krzyżem",
            "subtitle": "Prosty sznur modlitewny w surowym stylu tradycji monastycznej",
            "img": "images/model5_lina_czarny.jpg",
            "bg": "#ffffff",
            "spec": [
                "<strong>Forma Liny (Układ Otwarty):</strong> Brak pętli – modlitwa biegnie wprost od krzyża ku wieczności.",
                "<strong>Krzyż z Hebanu:</strong> Surowe, naturalne drewno o głębokiej czerni.",
                "<strong>Paciorki „M” i „J”:</strong> Miłość Matki i Jedność ze Zbawicielem przedzielone RGB.",
                "<strong>10 Paciorków Liniowych:</strong> Czarny K &bull; Szary &bull; Y &bull; M &bull; C &bull; B &bull; G &bull; R &bull; Szary &bull; Biały.",
                "<strong>Chwyt Pielgrzyma:</strong> Niezwykle wygodny w zaciśniętej dłoni podczas marszu."
            ],
            "card_title": "Zamów Model 5",
            "card_desc": "Ulubiony model mężczyzn, pielgrzymów i osób ceniących prostotę.",
            "footer_tag": "MODEL 5 • LINA Z CZARNYM KRZYŻEM"
        },
        6: {
            "title": "Model 6: Lina z Białym Krzyżem",
            "subtitle": "Biała lina modlitewna zwieńczona krzyżem Paruzji i Zmartwychwstania",
            "img": "images/model6_lina_bialy.jpg",
            "bg": "#ffffff",
            "spec": [
                "<strong>Świetlista Lina Ocalenia:</strong> Symbol liny rzuconej tonącemu człowiekowi przez Boga.",
                "<strong>Biały Krzyż:</strong> Blask poranka wielkanocnego i obietnica życia wiecznego.",
                "<strong>Paciorki „M” i „J”:</strong> Połączenie z Maryją i Jezusem w kodzie barw światłości.",
                "<strong>Sekwencja Otwarta:</strong> 10 paciorków biegnących prosto ku wiecznemu odpocznieniu.",
                "<strong>Trwałość:</strong> Odporny na pot i deszcz gęsty splot rzemieślniczy."
            ],
            "card_title": "Zamów Model 6",
            "card_desc": "Świetlisty znak nadziei i zwycięstwa Chrystusa w Twoim życiu.",
            "footer_tag": "MODEL 6 • LINA Z BIAŁYM KRZYŻEM"
        }
    }

    s = specs[model_num]
    items_html = "\n".join([f"              <li>{it}</li>" for it in s["spec"]])

    return f"""  <!-- STRONA: MODEL {model_num} -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Model {model_num} &bull; Katalog RHZ</span>
        <span>widokinaraj.pl</span>
      </div>

      <h2 class="section-title">{s["title"]}</h2>
      <h3 class="section-subtitle">{s["subtitle"]}</h3>

      <div class="product-layout">
        <div class="product-image-container" style="background: {s["bg"]};">
          <img src="{s["img"]}" alt="{s["title"]}">
          <span style="font-size: 7.5pt; color: var(--text-muted); margin-top: 3px; text-align: center;">Oryginalna fotografia modelu RHZ-0{model_num}</span>
        </div>

        <div class="product-info">
          <div>
            <ul class="product-spec-list">
{items_html}
            </ul>
          </div>

          <div class="buy-card">
            <h4>{s["card_title"]}</h4>
            <p>{s["card_desc"]}</p>
            <span class="buy-btn">Kup teraz &bull; {website_url}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>{s["footer_tag"]}</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_christological_center(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: CENTRUM CHRYSTOLOGICZNE I TAJEMNICE CISZY -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Etap IV Zbawienia</span>
        <span>Tajemnice Ciszy</span>
      </div>

      <h2 class="section-title">Centrum Chrystologiczne</h2>
      <h3 class="section-subtitle">Serce historii zbawienia i wezwanie do modlitwy kontemplacyjnej</h3>

      <p class="lead">
        Czwarty etap Różańca Historii Zbawienia stanowi absolutne serce całego dzieła. To w Osobie Jezusa Chrystusa odwieczne Słowo Ojca staje się Ciałem, a cała dotychczasowa historia ludzkości zyskuje ostateczny sens i zbawcze wypełnienie.
      </p>

      <div class="card" style="border-left: 3.5px solid var(--gold); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          Tajemnice Ciszy w Sercu Maryi
        </h4>
        <p style="margin: 0;">
          Pomiędzy tajemnicami publicznej działalności a męką Zbawiciela pojawiają się mistyczne <strong>Tajemnice Ciszy</strong>. To zaproszenie, by na wzór Matki Bożej <em>„zachowywać wszystkie te sprawy i rozważać je w swoim sercu”</em> (Łk 2, 19). Cisza w RHZ365 nie jest brakiem dźwięku, lecz pełnią obecności Boga.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid #991b1b; margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: #991b1b; margin-bottom: 2px;">
          Pascha: Szczyt Miłości Ofiarnej
        </h4>
        <p style="margin: 0;">
          Męka, Krzyż i Chwalebne Zmartwychwstanie objawiają moc przemiany zła w dobro. To w ranach Ukrzyżowanego każda ludzka samotność, ból i zwątpienie zostają uleczone i zanurzone w blasku wielkanocnego poranka.
        </p>
      </div>

      <div class="gold-box" style="margin: 0;">
        <strong>Owoc modlitwy:</strong> Przejście przez Etap IV uczy pokory, zaufania w godzinie próby oraz niezłomnej nadziei, że żadna ciemność nie ma władzy nad zmartwychwstałym Panem.
      </div>
    </div>

    <div class="page-footer">
      <span>ETAP IV &bull; CHRYSTUS I CISZA</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_church_and_parousia(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: KOŚCIÓŁ I PARUZJA -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Etapy V–VII</span>
        <span>Kościół & Paruzja</span>
      </div>

      <h2 class="section-title">Dzieje Kościoła i Nowe Niebo</h2>
      <h3 class="section-subtitle">Od Zesłania Ducha Świętego do ostatecznego zwycięstwa Boga</h3>

      <p class="lead">
        Historia zbawienia nie zakończyła się w Wieczerniku ani w dniu Wniebowstąpienia. Trwa nadal w Kościele i w sercu każdego wierzącego, zmierzając ku chwalebnemu dopełnieniu na końcu czasów.
      </p>

      <div class="card" style="border-left: 3.5px solid var(--green-rgb); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: #166534; margin-bottom: 2px;">
          Etap V: Zesłanie Ducha Świętego i Apostołowie
        </h4>
        <p style="margin: 0;">
          Ogniste języki Pięćdziesiątnicy przemieniają zalęknionych uczniów w nieustraszonych świadków Ewangelii. Duch Święty rodzi Kościół, który niesie światło prawdy na krańce ówczesnego świata, pokonując pogański mrok.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          Etap VI: Zmagania Dziejowe i Świadectwo Świętych
        </h4>
        <p style="margin: 0;">
          Wieki prześladowań, sobory, wielcy doktorzy Kościoła i cisi męczennicy codzienności. To przypomnienie, że każdy z nas jest powołany do świętości w swoim własnym stanie i epoce.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--gold); margin: 0;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          Etap VII: Paruzja – Nowe Niebo i Nowa Ziemia (Ap 21)
        </h4>
        <p style="margin: 0;">
          Finał historii świata. Chrystus powraca w chwale, ociera z oczu wszelką łzę, a śmierć i piekło zostają na zawsze pokonane. Modlitwa RHZ365 kończy się radosnym okrzykiem wczesnego Kościoła: <em>Marana tha! Przyjdź, Panie Jezu!</em>
        </p>
      </div>
    </div>

    <div class="page-footer">
      <span>ETAPY V–VII &bull; PARUZJA</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_silence_mysteries(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: TAJEMNICE CISZY -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Mistyczne Skupienie</span>
        <span>Tajemnice Ciszy</span>
      </div>

      <h2 class="section-title">Mistyka Tajemnic Ciszy</h2>
      <h3 class="section-subtitle">Gdy milkną słowa, a zaczyna przemawiać obecność Boga</h3>

      <p class="lead">
        W świecie zdominowanym przez nieustanny hałas, powiadomienia i bodźce, człowiek traci zdolność słyszenia własnego serca i głosu Boga. Odpowiedzią RHZ365 są <strong>Tajemnice Ciszy</strong>.
      </p>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          Cisza w Nazarecie i pod Krzyżem
        </h4>
        <p style="margin: 0;">
          Przez trzydzieści lat Jezus żył w ukryciu i ciszy Nazaretu. Maryja stała w milczeniu pod Krzyżem. Ta cisza nie była pustką ani bezradnością – była najgłębszym aktem wiary, w którym człowiek oddaje kontrolę Bogu i pozwala Mu działać.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--gold); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          Dwa Tygodnie Ciszy w Roku
        </h4>
        <p style="margin: 0;">
          W całorocznym kalendarzu RHZ365 wydzielono dwa szczególne okresy: <strong>Letni Tydzień Ciszy (18–24 czerwca)</strong> oraz <strong>Adwentowy Tydzień Ciszy (18–24 grudnia)</strong>. To czas podsumowania, odpoczynku duchowego i zebrania owoców poprzednich miesięcy.
        </p>
      </div>

      <div class="gold-box" style="margin: 0;">
        <strong>Praktyczna wskazówka:</strong> Podczas odmawiania Tajemnic Ciszy nie wypowiadaj intencji na głos. Pozwól swojemu oddechowi uspokoić się, a dłoni spoczywać na paciorkach różańca w pełnym zaufaniu.
      </div>
    </div>

    <div class="page-footer">
      <span>KONTEMPLACJA &bull; CISZA SERCA</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_examination_of_conscience(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: RACHUNEK SUMIENIA RGB/CMYK -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Formacja Wewnętrzna</span>
        <span>Rachunek Sumienia</span>
      </div>

      <h2 class="section-title">Rachunek Sumienia w Świetle Barw</h2>
      <h3 class="section-subtitle">Rozeznawanie stanu duszy w oparciu o dynamikę RGB i CMYK</h3>

      <div class="card" style="border-left: 3.5px solid var(--red-rgb); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: #991b1b; margin-bottom: 2px;">
          Wymiar Czerwieni (R - Jezus / Wiara)
        </h4>
        <p style="margin: 0;">
          Czy w moim życiu jest gotowość do ofiary dla Boga i bliźnich? Czy nie wstydzę się Krzyża Chrystusa? Czy potrafię przebaczać tym, którzy mnie zranili, tak jak Jezus przebaczył z Krzyża?
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--green-rgb); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: #166534; margin-bottom: 2px;">
          Wymiar Zieleni (G - Duch Święty / Nadzieja)
        </h4>
        <p style="margin: 0;">
          Czy nie ulegam zniechęceniu, narzekaniu i rozpaczy? Czy pielęgnuję w sobie pokój i radość Ewangelii? Czy troszczę się o stworzony świat i ludzi słabszych?
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--blue-rgb); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: #1e40af; margin-bottom: 2px;">
          Wymiar Błękitu (B - Bóg Ojciec / Miłość)
        </h4>
        <p style="margin: 0;">
          Czy Bóg jest dla mnie kochającym Ojcem, czy odległym sędzią? Czy znajduję codziennie czas na modlitwę w izdebce serca? Czy moje plany poddaję Jego woli?
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid #ca8a04; margin: 0;">
        <h4 style="font-size: 10.5pt; color: #854d0e; margin-bottom: 2px;">
          Oczyszczenie z Barw Upadku (CMYK)
        </h4>
        <p style="margin: 0;">
          Gdzie w moim sercu ukryła się zdrada (Y)? Gdzie dałem dojść do głosu pysze (M)? Gdzie pozwoliłem rozpaczy zatruć duszę (C)? Oddaj to Chrystusowi w sakramencie pokuty.
        </p>
      </div>
    </div>

    <div class="page-footer">
      <span>RACHUNEK SUMIENIA &bull; ŚWIATŁO ŁASKI</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_testimonies_list(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: ŚWIADECTWA I OWOCE -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Owoce Modlitwy</span>
        <span>Głosy Wspólnoty</span>
      </div>

      <h2 class="section-title">Świadectwa Modlących Się RHZ</h2>
      <h3 class="section-subtitle">Jak całoroczna droga przemienia codzienne życie rodzin i małżeństw</h3>

      <div class="card" style="margin-bottom: 5px; background: #ffffff;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          „Odzyskaliśmy pokój w małżeństwie”
        </h4>
        <p style="font-style: italic; margin: 0; line-height: 1.4;">
          „Byliśmy o krok od rozstania. Wspólne wieczorne odmawianie jednej dziesiątki z lektorem i trzymanie w dłoniach różańca z hebanowym krzyżem otworzyło nas na przebaczenie, które po ludzku wydawało się niemożliwe. Dziś dziękujemy Bogu za ocaloną rodzinę.”
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.88); color: var(--gold-dark); font-weight: 700; margin-top: 2px; text-align: right;">
          – Anna i Marek, Kraków
        </p>
      </div>

      <div class="card" style="margin-bottom: 5px; background: #ffffff;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          „Lektor w drodze do pracy”
        </h4>
        <p style="font-style: italic; margin: 0; line-height: 1.4;">
          „Spędzam codziennie dwie godziny w samochodzie. Zamiast radia włączam serwis widokinaraj.pl. Spokojny głos lektora i rozważanie tajemnicy dnia sprawiają, że do pracy dojeżdżam wyciszony, z jasnym celem i wiarą.”
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.88); color: var(--gold-dark); font-weight: 700; margin-top: 2px; text-align: right;">
          – Tomasz, kierowca zawodowy
        </p>
      </div>

      <div class="card" style="background: #ffffff; margin: 0;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          „Cud poczęcia wyproszony modlitwą”
        </h4>
        <p style="font-style: italic; margin: 0; line-height: 1.4;">
          „Przez pięć lat staraliśmy się o dziecko. Dołączyliśmy do I Cyklu RHZ w grudniu. W lipcu, podczas letniego tygodnia ciszy, otrzymaliśmy radosną wiadomość. Dziś nasz synek ma już roczek!”
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.88); color: var(--gold-dark); font-weight: 700; margin-top: 2px; text-align: right;">
          – Katarzyna i Piotr, Poznań
        </p>
      </div>
    </div>

    <div class="page-footer">
      <span>ŚWIADECTWA &bull; WIDOKINARAJ.PL</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_gift_packs(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: PAKIETY PODARUNKOWE I SKLEP -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Pakiety Formacyjne</span>
        <span>widokinaraj.pl</span>
      </div>

      <h2 class="section-title">Pakiety i Zestawy Podarunkowe</h2>
      <h3 class="section-subtitle">Kompletne edycje formacyjne dla Ciebie i Twoich bliskich</h3>

      <div class="grid-2" style="margin-bottom: 6px;">
        <div class="card" style="border-top: 3px solid var(--gold);">
          <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
            Pakiet Całoroczny (Królewski)
          </h4>
          <p style="font-size: calc(var(--base-font-size) * 0.92); margin-bottom: 4px;">
            Pełny Różaniec RHZ (Model 1 lub 2) + Komplet 4 Tomów „Widoków na Raj” w ozdobnym etui.
          </p>
          <span class="badge badge-gold">Najchętniej wybierany</span>
        </div>

        <div class="card" style="border-top: 3px solid var(--navy-deep);">
          <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
            Zestaw Podróżny (Pielgrzym)
          </h4>
          <p style="font-size: calc(var(--base-font-size) * 0.92); margin-bottom: 4px;">
            Okrągła Dziesiątka (Model 3/4) lub Lina Modlitewna (Model 5/6) w welurowym woreczku.
          </p>
          <span class="badge badge-black">Idealny do auta</span>
        </div>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--green-rgb); margin-bottom: 6px;">
        <h4 style="font-size: 10.5pt; color: #166534; margin-bottom: 2px;">
          Gwarancja Jakości i Polska Pracownia
        </h4>
        <p style="margin: 0;">
          Wszystkie różańce składane są ręcznie z najwyższej próby kamieni i hebanu. Kupując w oficjalnym sklepie, wspierasz dalszy rozwój platformy cyfrowej oraz bezpłatny dostęp do lektora dla tysięcy osób w kraju i za granicą.
        </p>
      </div>

      <div class="buy-card" style="margin: 0;">
        <h4>Zamów Bezpiecznie Online</h4>
        <p>Szybka wysyłka, eleganckie pakowanie na prezent, bezpieczne płatności.</p>
        <span class="buy-btn">Przejdź do sklepu &bull; {website_url}</span>
      </div>
    </div>

    <div class="page-footer">
      <span>PAKIETY FORMACYJNE &bull; SKLEP</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_prayer_book(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: MODLITEWNIK RHZ -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Modlitewnik RHZ</span>
        <span>Akty Oddania</span>
      </div>

      <h2 class="section-title">Modlitwy i Akty Zawierzenia</h2>
      <h3 class="section-subtitle">Duchowe akty ofiarowania do odmawiania przed i po różańcu</h3>

      <div class="card" style="background: #fdfaf2; border: 1.5px solid var(--gold); margin-bottom: 6px;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px; text-transform: uppercase;">
          Akt Ofiarowania Dnia w Świetle Barw RGB
        </h4>
        <p style="font-style: italic; margin: 0; line-height: 1.45;">
          „Panie Jezu Chryste, w Twojej Krwi i Wierze (R) zanurzam moje dzisiejsze myśli i decyzje. Duchu Święty, w Twoim Życiu i Nadziei (G) powierzam moje siły i spotkania z bliźnimi. Ojcze Niebieski, w Twojej Nieskończonej Miłości (B) składam całe moje życie. Spraw, aby światło Twojej łaski świeciło we mnie pośród ciemności świata. Amen.”
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 6px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px; text-transform: uppercase;">
          Modlitwa o Uzdrowienie ze Zdrady i Bólu (Y &rarr; R)
        </h4>
        <p style="font-style: italic; margin: 0; line-height: 1.45;">
          „Jezu, który na Krzyżu przyjąłeś pocałunek Judasza i przemieniłeś zdradę w ofiarę przebaczenia – ulecz moje zranione serce. Oddaję Ci każdy żal, poczucie odrzucenia i gorycz. Wlej w moje rany Twoją krew odkupienia, abym potrafił wybaczyć i kochać czystą miłością. Amen.”
        </p>
      </div>

      <div class="gold-box" style="margin: 0;">
        <strong>Modlitwa za wstawiennictwem Maryi (M &rarr; J):</strong><br>
        „Matko Pięknej Miłości, prowadź moje słabe 'Ja' do całkowitego zjednoczenia z Twoim Synem, Jezusem.”
      </div>
    </div>

    <div class="page-footer">
      <span>MODLITEWNIK RHZ &bull; ZAUFANIE</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_toc(items_list, pnum=2, website_url="{{ website_url }}"):
    rows = []
    for num, title, cat in items_list:
        rows.append(f"""          <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed #e2e8f0; padding: 2px 0;">
            <span><strong>s. {num}</strong> &bull; {title}</span>
            <span style="color: var(--gold-dark); font-weight: 700;">{cat}</span>
          </div>""")
    rows_html = "\n".join(rows)

    return f"""  <!-- STRONA: SPIS TREŚCI -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Różaniec Historii Zbawienia</span>
        <span>Spis Treści Publikacji</span>
      </div>

      <h2 class="section-title">Spis Treści</h2>
      <h3 class="section-subtitle">Harmonijna struktura duchowego przewodnika</h3>

      <div class="card" style="margin-bottom: 5px;">
        <div style="font-size: calc(var(--base-font-size) * 0.95); line-height: 1.45;">
{rows_html}
        </div>
      </div>

      <div class="gold-box" style="margin: 0;">
        Publikacja przygotowana w pełnej zgodności ze standardem wydawniczym Amazon KDP oraz polskimi wytycznymi sztuki drukarskiej A5.
      </div>
    </div>

    <div class="page-footer">
      <span>{website_url}</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_practice(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: PRZEWODNIK CODZIENNEJ PRAKTYKI -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Przewodnik Formacyjny</span>
        <span>Codzienna Praktyka</span>
      </div>

      <h2 class="section-title">Cztery Kroki Codziennej Modlitwy</h2>
      <h3 class="section-subtitle">Jak w prosty i owocny sposób odprawiać Różaniec Historii Zbawienia</h3>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          Krok 1: Wejdź na serwis widokinaraj.pl
        </h4>
        <p style="margin: 0;">
          Strona automatycznie rozpozna datę i wskaże tajemnicę przypadającą na dany dzień w kalendarzu 365 dni. Zobaczysz przypisany fragment Pisma Świętego oraz krótki komentarz duchowy.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--gold-dark); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--gold-dark); margin-bottom: 2px;">
          Krok 2: Włącz lektora audio
        </h4>
        <p style="margin: 0;">
          Naciśnij przycisk „Odtwórz”. Spokojny głos lektora wprowadzi Cię w atmosferę wyciszenia, odczytując biblijne rozważanie bez potrzeby ciągłego wpatrywania się w ekran.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--red-rgb); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: #991b1b; margin-bottom: 2px;">
          Krok 3: Weź do ręki fizyczny różaniec RHZ
        </h4>
        <p style="margin: 0;">
          Przesuwaj paciorki według kodu barw RGB lub CMYK. Dotyk szlachetnego kamienia i krzyża pomoże zsynchronizować oddech, serce i myśli z historią zbawienia.
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--green-rgb); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: #166534; margin-bottom: 2px;">
          Krok 4: Wprowadź Słowo w czyn
        </h4>
        <p style="margin: 0;">
          Zwieńcz modlitwę ofiarowaniem intencji za swoich bliskich i postanowieniem jednego konkretnego uczynku miłości w ciągu dnia.
        </p>
      </div>

      <div class="gold-box" style="margin: 0;">
        <strong>Wystarczy 15 minut:</strong> Tyle trwa dziesiątka z rozważaniem. Ten kwadrans przynosi pokój, który promieniuje na całą resztę Twojego dnia.
      </div>
    </div>

    <div class="page-footer">
      <span>PRAKTYKA MODLITWY &bull; 4 KROKI</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""

def get_page_testimony_and_store(pnum, website_url="{{ website_url }}"):
    return f"""  <!-- STRONA: ŚWIADECTWO I SKLEP -->
  <div class="page">
    <div>
      <div class="page-header">
        <span>Świadectwo & Sklep</span>
        <span>widokinaraj.pl</span>
      </div>

      <h2 class="section-title">Świadectwo Łaski i Zamówienia</h2>
      <h3 class="section-subtitle">Osobista historia narodzin dzieła oraz kontakt z twórcami</h3>

      <div class="card" style="background: #fdfaf2; border: 1.5px solid var(--gold); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          ❤️ Świadectwo Dominika i Oli
        </h4>
        <p style="font-style: italic; line-height: 1.42; margin-bottom: 3px;">
          „Dzieło to zrodziło się z głębokiej potrzeby serca i ufnej, wielomiesięcznej modlitwy o dar potomstwa. Doświadczenie Bożej wierności w najtrudniejszych chwilach stało się dla nas impulsem do stworzenia Różańca Historii Zbawienia. Chcemy zaświadczyć, że w Chrystusie nie ma sytuacji bez wyjścia, a ciemność zawsze ustępuje przed Światłością.”
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.9); color: var(--gold-dark); font-weight: 700; margin: 0; text-align: right;">
          – Dominik i Ola, twórcy RHZ365 & WnR365
        </p>
      </div>

      <div class="card" style="border-left: 3.5px solid var(--navy-deep); margin-bottom: 5px;">
        <h4 style="font-size: 10.5pt; color: var(--navy-deep); margin-bottom: 2px;">
          Oficjalny Sklep Dzieła: {website_url}
        </h4>
        <p style="margin-bottom: 3px;">
          Na naszej stronie zamówisz wszystkie 6 modeli różańców, tomy rozważań oraz pakiety podarunkowe:
        </p>
        <p style="font-size: calc(var(--base-font-size) * 0.92); margin: 0;">
          &bull; <strong>Pakiety Formacyjne:</strong> Wybrany Różaniec RHZ + 4 Tomy „Widoków na Raj”.<br>
          &bull; <strong>Eleganckie Welurowe Etui:</strong> Bezpieczne przechowywanie różańca.<br>
          &bull; <strong>Certyfikat Autentyczności:</strong> Ręczne wykonanie w polskiej pracowni.
        </p>
      </div>

      <div class="buy-card" style="margin: 0;">
        <h4>Dołącz do Wspólnoty Modlitwy</h4>
        <p>Zamów swój różaniec i zacznij całoroczną wędrówkę już dzisiaj.</p>
        <a href="https://widokinaraj.pl" class="buy-btn" style="padding: 5px 16px;">Wejdź na widokinaraj.pl &raquo;</a>
      </div>
    </div>

    <div class="page-footer">
      <span>{website_url} &bull; NIECH BÓG CI BŁOGOSŁAWI!</span>
      <span class="page-num">{pnum}</span>
    </div>
  </div>"""
