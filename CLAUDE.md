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
- `main.js` — imports and calls three init functions in sequence
- `modules/hero-carousel.js` — CSS scroll-snap carousel; controls, autoplay, dot sync, swipe, keyboard, ResizeObserver re-snap
- `modules/mobile-nav.js` — hamburger toggle
- `modules/current-year.js` — fills `[data-current-year]` in footer

**CSS — `src/styles/`**
- `main.css` — single import manifest, no own rules
- `variables.css` — all design tokens (colors, fonts, spacing, radii, shadows, container/hero dimensions)
- `reset.css`, `base.css`, `layout.css` — foundation
- `components/` — one file per section: header, buttons, sections, hero, trust, services, process, why, contact, footer

**Assets — `src/assets/images/`**
- 3 hero JPGs (`hero-rolety.jpg`, `hero-zaluzje.jpg`, `hero-moskitiery-plisy.jpg`)
- 4 service icons as WebP (`icon-rolety`, `icon-zaluzje`, `icon-plisy`, `icon-moskitiery`)
- `hero-rolety.jpg` is `<link rel="preload" fetchpriority="high">` — the others use `loading="lazy"`

**External CDN dependencies:**
- Google Fonts: Inter (body) + Lora (headings)
- Phosphor Icons `ph-bold` — used in "Dlaczego my" and "Kontakt" sections

## Code standards

- Semantic HTML, flat CSS — no redundant wrappers, no inline styles
- CSS animations/transitions preferred over JS
- JS only where CSS can't do it; no frameworks, no build-time abstractions
- Use stable lightweight libraries over hand-rolling (e.g. Formspree/Web3Forms for forms, Phosphor for icons)
- All design tokens live in `variables.css` — never hardcode colors, spacing, or radii elsewhere

## Pending (awaiting client)

- Logo file (.ai/.svg/.eps) → replaces text `DMSolutions` in header
- Product/service photos → `why-media__main` and `photo-strip` placeholders
- Full services list and copywriting materials
- Domain registration

## What's not done yet (known gaps)

- Contact form has no backend — needs Formspree/Web3Forms integration
- Google Maps embed is a placeholder (`map-placeholder`)
- `photo-strip` and `why-media__main` are visual placeholders
- No `og:image` set in meta tags
- `robots.txt` and `sitemap.xml` not yet generated
