# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

One-page Polish-only website (strona wizytówka) for DMSolutions — Damian Macur, Olsztyn. Window coverings (rolety, żaluzje, plisy, moskitiery), custom-made, free home visits. Supplier: Dekorama. First-ever website for this business.

## Commands

```bash
npm run dev      # dev server at localhost:4173
npm run build    # production build → dist/
npm run preview  # preview the built dist/
```

No linter, no test suite. Deploy target: Vercel (`vercel.json` sets `outputDirectory: "dist"`).

## Architecture

Vanilla JS + CSS, bundled with Vite. No framework.

**Entry point:** `index.html` → loads `src/js/main.js` (ES module) and `src/styles/main.css` via Vite.

**JS — `src/js/`**
- `main.js` — imports and calls four init functions in sequence
- `modules/hero-carousel.js` — CSS scroll-snap carousel; controls, autoplay, dot sync, swipe, keyboard, ResizeObserver re-snap
- `modules/mobile-nav.js` — hamburger toggle
- `modules/current-year.js` — fills `[data-current-year]` in footer and privacy page
- `modules/contact-form.js` — Web3Forms submission handler with loading/success/error states

**CSS — `src/styles/`**
- `main.css` — single import manifest, no own rules
- `variables.css` — all design tokens (colors, fonts, spacing, radii, shadows, container/hero dimensions)
- `reset.css`, `base.css`, `layout.css` — foundation
- `components/` — one file per section: header, buttons, sections, hero, trust, services, process, why, contact, footer

**Assets — `src/assets/images/`**
- 3 hero JPGs (`hero-rolety.jpg`, `hero-zaluzje.jpg`, `hero-moskitiery-plisy.jpg`)
- 4 service icons as WebP (`icon-rolety`, `icon-zaluzje`, `icon-plisy`, `icon-moskitiery`)
- `why-main.jpg` — photo for "Dlaczego my" section
- `realizacja-1..4.jpg` — photo strip (4 realization photos)
- `hero-rolety.jpg` is `<link rel="preload" fetchpriority="high">` — the others use `loading="lazy"`

**`public/` (copied directly to dist, not processed by Vite)**
- `favicon.svg` — DM monogram, geometric paths, no `<text>`
- `og-image.jpg` — 1200×630 for social previews
- `polityka-prywatnosci.html` — standalone privacy policy page (own inline styles, no Vite)

**External CDN dependencies:**
- Google Fonts: Figtree (body) + Lora (headings)
- Phosphor Icons `ph-bold` — used in "Dlaczego my" and "Kontakt" sections

## Code standards

- Semantic HTML, flat CSS — no redundant wrappers, no inline styles
- CSS animations/transitions preferred over JS
- JS only where CSS can't do it; no frameworks, no build-time abstractions
- Use stable lightweight libraries over hand-rolling (e.g. Web3Forms for forms, Phosphor for icons)
- All design tokens live in `variables.css` — never hardcode colors, spacing, or radii elsewhere
- Files in `public/` are NOT processed by Vite — no imports, no CSS vars, inline styles only

## Pending (awaiting client)

- Logo file (.ai/.svg/.eps) → replaces text `DMSolutions` in header
- Domain registration → needed to generate `robots.txt` and `sitemap.xml` with correct URL
- Street address → to complete administrator data in `public/polityka-prywatnosci.html`
- Web3Forms access key → replace `TUTAJ_WSTAW_KLUCZ_WEB3FORMS` in `src/js/modules/contact-form.js`

## What's not done yet (known gaps)

- Contact form backend: key placeholder in `contact-form.js` line 2
- `robots.txt` and `sitemap.xml` — blocked on domain
- Logo in header — text `DMSolutions` is a placeholder
- Street address missing in privacy policy (currently just "Olsztyn")
