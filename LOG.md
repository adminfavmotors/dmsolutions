# LOG.md — DMSolutions

Dziennik zmian dla aktualnego stanu kodu i architektury.
Po commicie: jeden wpis = jeden commit.
Dopóki zmiany są tylko w working tree, opisujemy je osobno w sekcji `Pending workspace updates`, żeby kolejna sesja AI miała prawdziwy kontekst zamiast zgadywania.

---

## Pending workspace updates (not committed yet)

- none

---

## 2026-04-18

### upcoming commit — stabilize runtime, verification, assets, and icon system
- P0 cleanup: usunięte równoległe i martwe warstwy (`src/content/services.md`, osierocone obrazy, martwe selektory CSS, katalog `site/`, robocze artefakty graficzne i screenshoty)
- P1 fixes: skróty klawiaturowe karuzeli działają tylko w hero, `mobile-nav.js` używa tego samego breakpointu co CSS, privacy page ma własny year script bez zależności od `/src`
- No-JS baseline: bazowy CSS został odpięty od inicjalizacji JS; pierwszy ekran renderuje się poprawnie jeszcze przed uruchomieniem `main.js`
- P2 assets/runtime: hero przeszedł na responsywne warianty `768w/1536w` (`webp` + `jpg`) generowane przez `npm run images:hero`
- Runtime dependencies: Google Fonts zostały usunięte z runtime; lokalne fonty idą z `/fonts/fonts.css`, a główna strona korzysta z lokalnie vendoryzowanego `Phosphor-Bold` bez zewnętrznego CDN
- Icons regression fix: sekcje „Dlaczego my” i „Kontakt” wróciły z ręcznie rysowanego sprite do lokalnie podpiętego `ph-bold`; `public/icons.svg` został ograniczony do małych ikon CTA
- Verification pipeline: dodany ESLint (`eslint.config.js`, `npm run lint`) dla browser JS w `src/js` i skryptów node w `scripts`
- Hero mobile composition i carousel: zmniejszony mobile stage, poprawiony loading slajdów hero i wygładzona synchronizacja karuzeli
- Dokumentacja projektu (`PLAN.md`, `README.md`, `CLAUDE.md`, `tests/checklist.md`) została zsynchronizowana z aktualną architekturą i faktycznymi ograniczeniami

---

## 2026-04-17

### ccad5f9 — design: uproszczony indykator karuzeli — białe kropki
- `hero.css`: aktywny i nieaktywny stan dots uproszczony do lekkiej, bardziej neutralnej wersji

---

## 2026-04-16

### 7d7e1e4 — revert: przywrócenie własnej karuzeli, usunięcie Splide
- `hero-carousel.js`: powrót do własnej implementacji opartej o scroll snap
- `index.html`: przywrócone własne strzałki i dots (`hero__control`, `hero__dot`)
- usunięta równoległa ścieżka oparta o Splide

### 7005595 — fix: przywrócenie poprawnej wysokości hero po migracji na Splide
- `variables.css` / `hero.css`: korekta wysokości stage po nieudanej migracji karuzeli

### bf7e89d — feat: migracja karuzeli hero na Splide
- historyczna próba uproszczenia karuzeli przez bibliotekę zewnętrzną
- później cofnięta w `7d7e1e4`, zostaje w logu jako kontekst decyzji

### bb72253 — feat: dodanie zdjęć realizacji do `photo-strip`
- `index.html`: sekcja „Dlaczego my” przestała być placeholderem, dostała realne zdjęcia realizacji
- `src/assets/images/realizacja-1..4.jpg`: wpięte do sekcji

### 18c09d5 — feat: usunięcie `hero__tag` ze wszystkich slajdów
- `index.html`: uproszczenie struktury hero, mniej dekoracyjnego DOM

### 9da572c — copy: rozszerzenie tekstu kroku 1 procesu
- `index.html`: krok „Kontakt” doprecyzowany o kontekst okien i potrzeb klienta

### 99c8e30 — feat: `services-note` — akcentowa listwa, CTA, poprawiony copy
- `index.html`: przepisany tekst sekcji i dodane CTA do kontaktu
- `services.css`: nota dostała wyraźniejszy akcent i lepszą hierarchię

### be5a2c5 — design: nowy favicon — żaluzje + monogram DM
- `public/favicon.svg`: zastąpienie wcześniejszej, mniej czytelnej wersji

---

## 2026-04-15

### 21ebede — P1/P2: hover states dla linków tekstowych + `accent-hover`
- `variables.css`: dodany `--color-accent-hover`
- `contact.css`, `footer.css`: czytelniejsze stany hover dla linków

### a231456 — fix: spójne fonty `h3`
- `process.css`, `why.css`: usunięte lokalne override `font-body`
- wszystkie `h3` wróciły do `var(--font-heading)`

### a1f5855 — phase 1: formularz, mapa, proporcje sekcji
- `contact-form.js`: obsługa wysyłki przez Web3Forms ze stanami formularza
- `index.html`: formularz bez `action="#"`, `aria-live`, mapa Google
- `contact.css`: style dla formularza i mapy

### 6f94088 — fix hero: max-width leadu + lżejsza animacja dots
- `hero.css`: ograniczenie szerokości leadu i poprawa czytelności hero copy

### 41a30f2 — visual: linia procesu + proporcje `photo-strip`
- `process.css`: linia łącząca kroki procesu na desktopie
- `why.css`: `photo-strip` przeszedł z `min-height` na `aspect-ratio`

### d1e5f6a — fix: tokeny, magiczne liczby, metodologia
- `variables.css`: nowe tokeny kolorów i wymiarów
- `contact.css`, `process.css`, `hero.css`: migracja z magicznych wartości do tokenów
- dodane `PLAN.md` i `LOG.md`

### 9d78352 — a11y + trust icons + prefers-reduced-motion
- `index.html`: `inputmode="tel"` w formularzu
- `base.css`: `skip-link` przeniesiony na `:focus-visible`
- `hero-carousel.js`: respektowanie `prefers-reduced-motion`

### 75ac3ab — design: Figtree + cieplejszy akcent
- `index.html`: zmiana body font na Figtree
- `variables.css`: dodane akcentowe kolory dla cieplejszego charakteru marki

### 6736134 — tokenizacja hero / services / contact / trust / header
- migracja hardcoded wartości do wspólnych tokenów w `variables.css`
- porządkowanie spacingu, kolorów i typografii w sekcjach

### f3fa9a9 — P0: tokeny typografii + porządki w repo
- `variables.css`: skala tekstu, leading i tracking
- `.gitignore`: czyszczenie repo z assetów roboczych i plików sesyjnych
- `sections.css`: usunięcie martwego `.section-placeholder`

### 4b8faae — P0: usunięcie placeholder-driven architektury sekcji „Dlaczego my”
- `index.html`, `why.css`: sekcja uproszczona do realnej struktury bez pustych boksów

### b935794 — design polish: spacing, szerokość kontaktu, rytm nagłówków
- `variables.css`: dodany `--contact-shell-max`
- `services.css`, `contact.css`, `base.css`: korekty rytmu i proporcji
