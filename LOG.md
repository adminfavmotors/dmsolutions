# LOG.md — DMSolutions

Dziennik zmian. Każdy wpis = jeden commit.

---

## 2026-04-16

### 9da572c — copy: шаг 1 процесса — расширен текст
- `index.html`: текст шага 1 дополнен ("jakie masz okna") — визуальный баланс с шагами 2–4

### ecac07d — hero dots: kontур для неактивных + акцентная активная
- `hero.css`: неактивные точки — прозрачный фон + белый контур `65%`; активная — заливка `--color-accent` (#b07d50)

### 99c8e30 — services-note: akcentowa listwa + CTA + przepisany tekst
- `index.html`: przepisany tekst na bardziej pewny ton; dodano link `.services-note__cta` → `#kontakt`
- `services.css`: `border` → lewa listwa `3px solid var(--color-accent)`; tło → `--color-accent-bg`; badge → kolor akcentu; tekst `color-text-muted` → `color-text`; dodano styl `.services-note__cta` z hover (przesunięcie strzałki)

### be5a2c5 — design: nowa favikona — żaluzje + monogram DM
- `public/favicon.svg`: 4 poziome listwy (gradient biel→niebieski) + tekst „DM" na dole; zastępuje niejasny podwójny kształt litery D

---

## 2026-04-15

### a231456 — Fix h3 font inconsistency
- `process.css`: usunięto `font-family: var(--font-body)` z `.process-step h3`
- `why.css`: usunięto `font-family: var(--font-body)` z `.benefit-item h3`
- Wszystkie h3 teraz jednolicie używają `var(--font-heading)` (Lora)

### a1f5855 — Phase 1 + visual audit: form, map, proportions
- `contact-form.js`: nowy moduł, async fetch → Web3Forms, stany loading/success/error
- `main.js`: dodano `initContactForm()`
- `index.html`: formularz bez `action="#"`, `form-status` z `aria-live`, iframe Google Maps
- `contact.css`: `.map-wrap` zastępuje `.map-placeholder`, style stanów formularza
- `why.css`: `grid-template-columns` → `1fr 1fr` (było: `minmax(0, 24rem) 1fr`)
- `sections.css`: h2 `clamp(1.9rem, 4vw, 3rem)` → `clamp(1.6rem, 3vw, 2.2rem)`
- Dodano `CLAUDE.md` i `potrzebne-od-klienta.docx`

### 6f94088 — Fix hero: lead max-width + dot compositor-friendly animation
- `hero.css`: `.hero__lead` dodano `max-width: 42ch`
- `hero.css`: `.hero__dot` animacja `width` → `transform: scaleX()` (compositor thread)

### 41a30f2 — Visual: process connector line + photo-strip aspect-ratio
- `process.css`: `.process-grid::before` — linia łącząca kółka kroków, ukryta na tablet/mobile
- `process.css`: `.process-step__number` — `position: relative; z-index: 1`
- `why.css`: `.photo-strip__item` — `min-height: 9rem` → `aspect-ratio: 4/3`

### d1e5f6a — Fix: tokeny, magiczne liczby, metodologia
- `variables.css`: dodano `--color-success`, `--color-error` i warianty bg/border
- `variables.css`: dodano `--process-step-size`, `--hero-dot-width`, `--hero-dot-height`
- `contact.css`: hardcoded kolory → tokeny CSS
- `process.css`: `3.4rem` → `var(--process-step-size)`
- `hero.css`: `scaleX(0.367)` → `calc(var(--hero-dot-height) / var(--hero-dot-width))`
- Dodano `PLAN.md` i `LOG.md`

### 9d78352 — A11y + trust icons + prefers-reduced-motion
- `index.html`: dodano `inputmode="tel"` na polu telefonu
- `trust.css`: ikony SVG `1rem` → `1.25rem`
- `base.css`: `.skip-link:focus` → `:focus-visible`
- `hero-carousel.js`: `scrollBehavior()` respektuje `prefers-reduced-motion`,
  autoplay wyłączony gdy użytkownik preferuje brak animacji

### 75ac3ab — Design: Figtree + warm accent color
- `index.html`: Google Fonts Inter → Figtree
- `variables.css`: `--font-body` → Figtree; dodano `--color-accent: #b07d50`,
  `--color-accent-bg: #f5ede4`
- `sections.css`: eyebrow pill → warm accent (border, kolor tekstu, tło)
- `trust.css`: ikony SVG → `--color-accent` (zamiast zimnego `--color-accent-soft`)
- `process.css`: pierścień kółka kroku → `--color-accent`

### [bieżący] — P1/P2: hover states + accent-hover token + breakpoint docs
- `variables.css`: dodano `--color-accent-hover: #8f6440` (ciemniejszy akcent do hover)
- `variables.css`: udokumentowano konwencję breakpoints (40/48/56.25/64 rem)
- `contact.css`: linki telefon/e-mail — hover `color → --color-accent-hover` z transition
- `footer.css`: linki stopki — hover `color → --color-text-inverse` z transition

### 6736134 — Tokenizacja: hero/services/contact/trust/header
- `hero.css`: hardcoded hex (#1b2a45, #2a4e8f, #1b3a6b, #243558, #1f304a, #2c5282) → `--color-primary*` tokeny; `letter-spacing: 0.12em` → `--tracking-wide`
- `services.css`: font-size'y i line-height'y, paddingi, gap'y → tokeny `--text-*`/`--space-*`/`--leading-*`
- `services.css`: `.services-note` gradient rgba → `var(--color-primary-soft)`
- `contact.css`: pełna migracja na tokeny, placeholder color `#8fa0bf` → `var(--color-text-muted)` z opacity; reassurance bg `rgba(255,255,255,0.75)` → `var(--color-surface)`
- `trust.css`: `1.25rem`/`1rem`/`2rem`/`0.65rem`/`0.9rem` → tokeny
- `header.css`: `1.2rem`/`0.3rem`/`0.75rem`/`1rem`/`1.25rem` → tokeny

### f3fa9a9 — P0 (9.1/9.2): typography tokens + gitignore cleanup
- `.gitignore`: dodano `.claude/`, `*.png`/`*.jpg` (z wyjątkiem `src/assets/**`), `ai-dev-prompt.md`
- usunięto z repo: ChatGPT/Gemini PNG, `ai-dev-prompt.md`, `.claude/settings.local.json`
- `variables.css`: dodano skalę `--text-xs/sm/body-sm/base/md/lg/xl/h3/h2/h1`
- `variables.css`: dodano `--leading-tight/snug/normal/relaxed/loose` i `--tracking-wide`
- `base.css`: `1rem` → `--text-base`, `1.6` → `--leading-normal`, `1.2` → `--leading-tight`
- `sections.css`: eyebrow font-size/letter-spacing → tokeny; h2 → `--text-h2`; section-copy line-height → `--leading-loose`; usunięto martwy `.section-placeholder` (80% pliku)
- `sections.css`: section-copy margin-top `0.9rem` → `--space-3` wspólnie dla wszystkich section-heading
- `why.css`: font-size'y i line-height'y → tokeny
- `process.css`: gap'y, font-size'y, line-height'y, magiczne odstępy → tokeny
- `footer.css`: `0.875rem` → `--text-sm`

### 4b8faae — P0 (4.1): remove placeholder-driven "Dlaczego my" architecture
- `index.html`: usunięto `.why-media` (pusty prostokąt 30rem) i `.photo-strip` (4 puste kwadraty)
- `index.html`: sekcja "Dlaczego my" → `section-heading--center` + `benefit-list` (spójna z innymi sekcjami)
- `why.css`: usunięto `.why-grid`, `.why-media*`, `.photo-strip*` — martwy kod po usunięciu plejshólderów
- `why.css`: `.benefit-list` → 2-kolumnowy grid na desktopie, 1 kolumna <48rem
- `why.css`: magiczne liczby (1.2rem, 1.75rem, 0.9rem, 0.3rem) → tokeny `--space-*`
- `why.css`: `.benefit-item h3` `1rem` → `1.15rem` (Lora czytelnie)
- Sekcja działa bez zdjęć klienta, gotowa na wstawienie galerii gdy zdjęcia nadejdą

### a1d0000 — Design polish: spacing, contact width, heading rhythm
- `variables.css`: dodano `--contact-shell-max: 46rem`
- `services.css`: gap kart `1.25rem` → `var(--space-6)` (1.5rem)
- `contact.css`: szerokość formularza `40rem` → `var(--contact-shell-max)`
- `base.css`: `line-height` nagłówków `1.15` → `1.2` (czytelność Lory)
