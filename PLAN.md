# PLAN.md — DMSolutions

Plan pracy nad stroną wizytówką. Aktualizowany na bieżąco.

## Fazy

### Faza 1 — Funkcjonalne komponenty ✅
- [x] Formularz kontaktowy (Web3Forms, stany loading/success/error)
- [x] Google Maps iframe (Olsztyn)
- [x] Footer — weryfikacja current-year JS

### Faza 2 — Materiały klienta ⏳ (czeka)
- [ ] Logo → podmiana tekstu DMSolutions w headerze
- [ ] Zdjęcia → why-media__main + photo-strip
- [ ] Klucz Web3Forms API → formularz gotowy do wysyłki
- [ ] Pełna lista usług + teksty

### Faza 3 — Wizualny audyt i polish ✅ / 🔄
- [x] why-grid: równe kolumny 1fr / 1fr
- [x] h2: clamp(3rem) → clamp(2.2rem)
- [x] h3: usunięto font-body override (process, why)
- [x] hero__lead: max-width 42ch
- [x] hero__dot: width → transform scaleX (compositor)
- [x] process: linia łącząca kroki
- [x] photo-strip: min-height → aspect-ratio 4/3
- [x] Hardcoded kolory → tokeny w variables.css
- [x] Magiczne liczby → zmienne CSS
- [x] Trust bar: ikony SVG 1rem → 1.25rem
- [x] services-note: akcentowa listwa + CTA-link + przepisany tekst
- [x] Favicon: żaluzje + monogram DM
- [ ] prefers-reduced-motion w JS karuzeli
- [ ] Accessibility: aria-hidden na SVG w trust-bar
- [ ] inputmode="tel" na polu telefonu
- [ ] skip-link: :focus → :focus-visible

### Faza 4 — Gotowość do wdrożenia
- [ ] robots.txt + sitemap.xml
- [ ] og:image
- [ ] Weryfikacja Lighthouse (performance, a11y, SEO)
- [ ] Vercel deploy test

### Faza 5 — Wymogi prawne (PL + UE)

#### Od klienta potrzebne:
- [ ] NIP firmy → dodać do stopki (obowiązek ustawowy)
- [ ] Adres siedziby → dodać do stopki
- [ ] Email do spraw RODO → do Polityki prywatności

#### Do zrobienia technicznie:
- [ ] Przenieść Google Fonts na self-hosted (Inter + Lora)
      → eliminuje konieczność cookie bannera dla czcionek
      → szybsze ładowanie, brak transferu IP do Google
      → narzędzie: https://gwfh.mranftl.com (google-webfonts-helper)
- [ ] Polityka prywatności (`/polityka-prywatnosci`)
      → administrator danych (imię, adres, NIP)
      → cel przetwarzania (odpowiedź na zapytanie)
      → czas przechowywania
      → prawa użytkownika (dostęp, usunięcie, sprzeciw)
      → kontakt RODO
- [ ] Zgoda na przetwarzanie danych w formularzu
      → checkbox NIE zaznaczony domyślnie
      → tekst: "Wyrażam zgodę na przetwarzanie moich danych osobowych..."
      → link do Polityki prywatności
- [ ] Cookie banner (jeśli zostanie CDN Google Fonts lub Google Analytics)
      → przyciski: Akceptuj / Tylko niezbędne / Ustawienia
      → nie ukrywać przycisku odrzucenia
- [ ] Wzmianka o braku prawa odstąpienia
      → usługi "na miarę" są wyłączone z 14-dniowego zwrotu
      → można dodać do stopki lub regulaminu

#### Uwaga prawna:
Brak danych rejestrowych (NIP, adres) na stronie to naruszenie
Ustawy o świadczeniu usług drogą elektroniczną (Art. 5).
Priorytet: zrobić zaraz po otrzymaniu NIP od klienta.
