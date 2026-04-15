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
- [ ] Trust bar: ikony SVG 1rem → 1.25rem
- [ ] prefers-reduced-motion w JS karuzeli
- [ ] Accessibility: aria-hidden na SVG w trust-bar
- [ ] inputmode="tel" na polu telefonu
- [ ] skip-link: :focus → :focus-visible

### Faza 4 — Gotowość do wdrożenia
- [ ] robots.txt + sitemap.xml
- [ ] og:image
- [ ] Weryfikacja Lighthouse (performance, a11y, SEO)
- [ ] Vercel deploy test
