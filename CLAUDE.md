# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Primary working rules

All code work in this project follows `ai-dev-prompt.md` (project root). Read it before touching any code. It overrides default behaviour on: reading before editing, single source of truth, deletion on replacement, dead code search, and cross-session context.

## Project

One-page Polish-only website (strona wizytówka) for DMSolutions — Damian Macur, Olsztyn. Window coverings (rolety, żaluzje, plisy, moskitiery), custom-made, free home visits. Supplier: Dekorama. First-ever website for this business.

## Commands

```bash
npm run dev      # dev server at localhost:4173
npm run build    # production build → dist/
npm run lint     # ESLint for browser JS in src/js and node scripts in scripts/
npm run preview  # preview the built dist/
npm run images:hero  # regenerate responsive hero image variants from JPG masters
```

No test suite yet. Deploy target: Vercel (`vercel.json` sets `outputDirectory: "dist"`).

## Architecture

Vanilla JS + CSS, bundled with Vite. No framework.

**Entry point:** `index.html` → loads `src/js/main.js` (ES module), `src/styles/main.css` via Vite, and shared local fonts from `/fonts/fonts.css`.

**JS — `src/js/`**
- `main.js` — imports and calls four init functions in sequence
- `modules/hero-carousel.js` — CSS scroll-snap carousel; controls, autoplay, dot sync, swipe, keyboard scoped to hero, ResizeObserver re-snap
- `modules/mobile-nav.js` — hamburger toggle aligned with the desktop nav media query (`56.25rem`)
- `modules/current-year.js` — fills `[data-current-year]` in the main page footer
- `modules/contact-form.js` — Web3Forms submission handler with loading/success/error states

**CSS — `src/styles/`**
- `main.css` — single import manifest, no own rules
- `variables.css` — all design tokens (colors, fonts, spacing, radii, shadows, container/hero dimensions)
- `reset.css`, `base.css`, `layout.css` — foundation
- `components/` — one file per section: header, buttons, sections, hero, trust, services, process, why, contact, footer

**Assets — `src/assets/images/`**
- 3 hero JPG masters (`hero-rolety.jpg`, `hero-zaluzje.jpg`, `hero-moskitiery-plisy.jpg`)
- generated hero delivery variants: `*-768w.webp/.jpg`, `*-1536w.webp/.jpg` (created by `npm run images:hero`)
- 4 service icons as WebP (`icon-rolety`, `icon-zaluzje`, `icon-plisy`, `icon-moskitiery`)
- `why-main.jpg` — photo for "Dlaczego my" section
- `realizacja-1..4.jpg` — photo strip (4 realization photos)
- first hero slide preloads the responsive WebP variant; later slides use lazy loading

**`public/` (copied directly to dist, not processed by Vite)**
- `favicon.svg` — DM monogram, geometric paths, no `<text>`
- `og-image.jpg` — 1200×630 for social previews
- `fonts/fonts.css` + `.woff2` files — shared local font delivery for both pages
- `icons.svg` — small local SVG sprite still used for lightweight inline CTA arrows
- `public/phosphor/` + `src/styles/vendor/phosphor-bold.css` — vendored local `Phosphor-Bold` subset used by the main page (`ph-bold` icons in "Dlaczego my" and contact)
- `polityka-prywatnosci.html` — standalone privacy policy page (own inline styles, no Vite, inline year script)

**External runtime services still in use:**
- Web3Forms — contact form delivery
- Google Maps embed — iframe in the contact section

## Code standards

- Semantic HTML, flat CSS — no redundant wrappers, no inline styles
- CSS animations/transitions preferred over JS
- JS only where CSS can't do it; no frameworks, no build-time abstractions
- Use stable lightweight integrations where they remove complexity (e.g. Web3Forms for forms), but prefer local assets over UI CDNs
- All design tokens live in `variables.css` — never hardcode colors, spacing, or radii elsewhere
- Files in `public/` are NOT processed by Vite — no JS module imports, no dependency on `/src`, no CSS vars from app styles; only self-contained HTML/CSS/JS plus static asset URLs from `public/` such as `/fonts/fonts.css` or `/icons.svg`

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
