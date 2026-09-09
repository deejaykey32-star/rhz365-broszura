# Różaniec Historii Zbawienia (RHZ365) • Generator Broszury A5 & Amazon KDP

Oficjalny generator publikacji drukarskiej A5 (broszura zeszytowa oraz książka Amazon KDP Paperback) dla projektu **Różaniec Historii Zbawienia** (`widokinaraj.pl`).

---

## 🌟 Możliwości Aplikacji

1. **Formaty i Profile Publikacji:**
   - **Druk Lokalny (16 stron)** – standardowa broszura zeszytowa (oprawa szyta drutem), spad 3.0 mm, margines wewnętrzny 0 mm.
   - **Druk Lokalny Rozszerzony (20 stron)** – wersja z dodatkową stroną redakcyjną i spisem tomów.
   - **Amazon KDP Paperback (24 strony - MINIMUM KDP)** – format spełniający rygorystyczne wytyczne Amazon KDP (min. 24 strony), spad 3.175 mm (0.125"), margines wewnętrzny (gutter) 9.5 mm (0.375").
   - **Amazon KDP Rozszerzone (28 stron)** – pełne wydanie z dedykowanymi stronami modlitewnymi i intencjami.

2. **Pełna Rozkładówka Okładki KDP (Wrap-around Cover Spread):**
   - Jednolity plik PDF obejmujący: Tylną okładkę + Grzbiet (Spine) + Przednią okładkę + Spad zewnętrzny 3.175 mm.
   - Dedykowane, bezpieczne pole na automatyczny kod kreskowy Amazon KDP (50.8 × 30.5 mm).

3. **Kompletna Teologia i Treść (Misja Barw i Kolorów):**
   - Prezentacja 6 modeli fizycznych różańców (Pełny RGB/CMYK biały i czarny, Dziesiątka okrągła biała i czarna, Różaniec-Lina biały i czarny).
   - Symbolika liter `I` i `N` oraz `M` i `J`.
   - Zestawienie 4 tomów „Widoki na Raj” (Ziemia, Wiosna, Lato, Jesień).
   - Kalendarium 365 dni i 175 tajemnic historii zbawienia.
   - Świadectwo Dominika i Oli oraz modlitwa o dar potomstwa.

4. **Elastyczność Uruchomienia:**
   - **Cloudflare Pages:** 100% statyczna aplikacja z podglądem na żywo, natywnym drukiem do PDF (`window.print()`) oraz bezpośrednimi linkami do pobrania gotowych plików.
   - **Lokalne Środowisko Python (Flask + WeasyPrint/Chrome):** Dynamiczne generowanie plików PDF w 300 DPI za pomocą `server.py` i `start_app.bat`.

---

## 🚀 Uruchomienie

### Opcja 1: Cloudflare Pages (Statycznie)
Aplikacja jest w pełni przystosowana do hostingu w Cloudflare Pages:
- Otwórz `index.html` w dowolnej przeglądarce lub wdróż za pomocą Cloudflare Pages / Wrangler:
  ```bash
  wrangler pages deploy . --project-name rhz365-broszura
  ```

### Opcja 2: Lokalny Serwer Python
1. Zainstaluj wymagane biblioteki:
   ```bash
   pip install flask jinja2
   ```
2. Uruchom serwer:
   ```bash
   start_app.bat
   ```
   lub:
   ```bash
   python server.py
   ```
3. Otwórz w przeglądarce: `http://localhost:5000`

---

## 📁 Struktura Projektu

- `index.html` – główny panel sterowania i dashboard aplikacji dla Cloudflare Pages
- `preview.html` – responsywny, dynamiczny podgląd stron wnętrza broszury (16, 20, 24, 28 stron)
- `cover.html` – interaktywny podgląd rozkładówki okładki Amazon KDP
- `downloads/` – prekompilowane, gotowe do druku pliki PDF w wysokiej rozdzielczości oraz pakiet ZIP
- `images/` – zdjęcia wszystkich 6 modeli różańców i wektorowy krzyż
- `templates/` – szablony HTML dla lokalnego silnika renderującego
- `server.py` – lokalny serwer Flask do generowania plików PDF offline
- `wrangler.toml` – konfiguracja dla Cloudflare Pages
