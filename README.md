# DMSolutions

Landing page for `DMSolutions` built with `Vite + Vanilla HTML/CSS/JS`.

## Current Status

- Single-page Polish website is implemented and builds correctly with `npm run build`
- ESLint is configured and passing through `npm run lint`
- Hero uses a custom CSS scroll-snap carousel, not Splide
- Hero images are delivered through responsive `picture/srcset` variants instead of the original multi-megabyte JPGs
- Fonts are served locally, and the main-page UI icons use a vendored local `Phosphor-Bold` subset instead of an external CDN
- The `Dlaczego my` and `Kontakt` sections are back on the original connected Phosphor icon language instead of a custom SVG replacement
- Hero keyboard handling is scoped to the carousel context, not the whole document
- Base CSS loads directly from `index.html`, so layout does not depend on JavaScript execution
- Contact form UI is implemented, but submission is blocked until the real Web3Forms key is provided
- Privacy policy exists as a standalone static page in `public/` and no longer depends on `/src` JS
- Manual browser verification passed on desktop, laptop, tablet, mobile, and the privacy page with no runtime errors or Vite overlay
- First-screen verification also passed without JavaScript: hero content remains visible before `main.js` runs

## Current Blockers

- Web3Forms access key for the contact form
- Logo file for replacing the text brand in the header
- Final domain for `robots.txt`, `sitemap.xml`, and `og:url`
- Full company legal data: address, NIP, RODO contact email

## Architecture Overview

- `index.html` is the single page entry point
- `src/js/main.js` initializes: current year, mobile nav, hero carousel, contact form
- `src/js/modules/hero-carousel.js` keeps keyboard handling local to hero interactions
- `src/js/modules/mobile-nav.js` follows the same `56.25rem` desktop breakpoint as CSS
- `src/styles/main.css` is the CSS import manifest
- `src/styles/variables.css` contains design tokens
- `src/styles/components/` contains one stylesheet per section
- `public/` contains static assets copied as-is by Vite, including `polityka-prywatnosci.html`, `/fonts/fonts.css`, font files, the vendored `phosphor/` icon font files, and the small `icons.svg` sprite still used for inline CTA arrows

## Project Docs

- `CLAUDE.md` — repository-specific working context and constraints
- `PLAN.md` — current execution plan and open priorities
- `LOG.md` — change log aligned with the current architecture
- `ai-dev-prompt.md` — primary working rules for code changes in this project

## Stack

- Vite
- Vanilla HTML
- Modular CSS
- Modular JavaScript

## Local development

```bash
npm install
npm run dev
npm run lint
npm run images:hero
```

`npm run images:hero` regenerates the responsive hero image variants from the original JPG masters in `src/assets/images/`.

## Production build

```bash
npm run build
```

Build output is generated in `dist/`.

## Known Technical Gaps

- No automated test suite yet
- Privacy page still lacks full company legal data

## Vercel

This repository is ready for deployment on Vercel.

Recommended settings:

- Framework Preset: `Vite`
- Install Command: `npm install`
- Build Command: `npm run build`
- Output Directory: `dist`

`vercel.json` already defines the output directory.

## GitHub Actions deployment

Automatic production deployment is configured in `.github/workflows/vercel-production.yml`.

Required one-time repository secret:

- `VERCEL_TOKEN`

The workflow already includes the correct Vercel project ID and team ID for this repository.
