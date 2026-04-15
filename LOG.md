# LOG.md — DMSolutions

Dziennik zmian. Każdy wpis = jeden commit.

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

### [bieżący] — Design: Figtree + warm accent color
- `index.html`: Google Fonts Inter → Figtree
- `variables.css`: `--font-body` → Figtree; dodano `--color-accent: #b07d50`,
  `--color-accent-bg: #f5ede4`
- `sections.css`: eyebrow pill → warm accent (border, kolor tekstu, tło)
- `trust.css`: ikony SVG → `--color-accent` (zamiast zimnego `--color-accent-soft`)
- `process.css`: pierścień kółka kroku → `--color-accent`
