# PLAN.md — DMSolutions

Aktualny plan utrzymania i doprowadzenia strony do publikacji.

## Stan systemu

### Rdzeń strony
- [x] One-page site na `Vite + Vanilla HTML/CSS/JS`
- [x] Własna karuzela hero oparta o CSS scroll snap
- [x] Sekcje: hero, trust bar, oferta, proces, dlaczego my, kontakt, footer
- [x] Zdjęcia realizacji i główne zdjęcie sekcji „Dlaczego my”
- [x] Formularz kontaktowy z obsługą stanów loading/success/error
- [x] Polityka prywatności jako osobna strona w `public/`

### Blokery od klienta
- [ ] Klucz Web3Forms → aktywacja formularza
- [ ] Logo (`.svg/.ai/.eps`) → podmiana tekstu `DMSolutions` w headerze
- [ ] Domena → `robots.txt`, `sitemap.xml`, `og:url`
- [ ] Pełne dane firmy: adres, NIP, e-mail do spraw RODO

## Priorytety techniczne

### P0 — integralność systemu
- [x] Usunięcie nieużywanego źródła treści (`src/content/services.md`)
- [x] Usunięcie martwych selektorów CSS i osieroconych assetów
- [x] Synchronizacja `PLAN.md` i `LOG.md` z aktualnym stanem repo

### P1 — spójność działania
- [x] Ograniczyć skróty klawiaturowe karuzeli do kontekstu hero, nie całego dokumentu
- [x] Naprawić `current-year` na stronie polityki prywatności przez usunięcie zależności od osobnego JS
- [x] Ujednolicić kontrakt breakpointów między CSS a `mobile-nav.js`

### P2 — performance i release hardening
- [x] Zoptymalizować hero image (`WebP/AVIF`, mniejsze pliki, ewentualnie `<picture>`)
- [x] Ograniczyć zależność od zewnętrznych CDN-ów (Google Fonts, Phosphor Icons)
- [ ] Dodać `robots.txt` i `sitemap.xml` po poznaniu domeny
- [ ] Uzupełnić dane prawne i biznesowe po otrzymaniu danych od klienta

## Weryfikacja po zmianach
- [x] `npm run build`
- [x] `npm run lint`
- [x] Kontrola martwego kodu / osieroconych assetów
- [x] Przegląd mobile → tablet → laptop → desktop
- [x] Kontrola pierwszego ekranu bez zależności od JS

Uwagi po przeglądzie:
- Viewport review przeszedł: desktop, laptop, tablet, mobile i strona prywatności renderują się bez overlayu i bez błędów w konsoli.
- No-JS baseline został naprawiony przez odpięcie bazowego CSS od inicjalizacji JS: pierwszy ekran renderuje się poprawnie jeszcze przed uruchomieniem `main.js`.
- Hero korzysta teraz z responsywnych wariantów `768w/1536w` (`webp` + `jpg`) generowanych skryptem `npm run images:hero`; desktop ładuje `1536w.webp`, mobile `768w.webp`.
- Google Fonts zostały usunięte z runtime, a Phosphor wrócił jako lokalnie vendoryzowany `Phosphor-Bold`: obie strony ładują lokalne fonty z `/fonts/fonts.css`, główna strona bierze ikony z lokalnego `ph-bold`, a `public/icons.svg` został zredukowany do małych ikon inline używanych w CTA.
- ESLint działa jako podstawowy quality gate dla `src/js` i `scripts/`; aktualny stan przechodzi `npm run lint`.
