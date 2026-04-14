# DMSolutions — Project Plan

**Client:** Damian Macur / DMSolutions, Olsztyn  
**Type:** One-page website (strona wizytówka)  
**Language:** Polish only  
**Manager:** Yury Luzhkouski / NODE48  

---

## Methodology

- Work phase by phase — never jump ahead
- Every decision gets logged in LOG.md (success and failure both)
- Every phase has a clear exit condition before moving on
- Code is written component by component, not page by page
- Mobile-first from line one
- Deployable as pure static files on any host at any time

---

## Tech Stack (locked)

| Layer | Choice | Why |
|---|---|---|
| Build tool | **Vite** | Zero-config, outputs pure static `dist/`, works on any host |
| HTML | **Vanilla HTML** (Vite partials) | No runtime framework needed for one-page |
| CSS | **CSS custom properties** + component files | Design tokens, no framework bloat |
| JS | **Vanilla JS** | Minimal, readable, no bundle weight |
| Carousel | **Swiper.js** (CDN or npm) | Mature, reliable, responsive |
| Icons | **Lucide** (CDN) | Lightweight SVG icon set, no custom drawing |
| Fonts | **Google Fonts** | CDN, free |
| Form | **Web3Forms** | Free tier, no backend, GDPR-friendly |
| Map | **Google Maps embed** (iframe) | Zero JS cost |
| Analytics | **Google Analytics 4** | Client requested |
| Cookie consent | **CookieYes** or custom minimal banner | GDPR required (Poland) |

---

## Project Structure

```
dmsolutions/
├── PLAN.md               ← this file
├── LOG.md                ← work diary (all steps, good and bad)
├── PROJECT_GUIDE.md      ← client context and decisions
├── src/
│   ├── index.html
│   ├── css/
│   │   ├── variables.css     ← design tokens (colors, spacing, type)
│   │   ├── reset.css         ← normalize
│   │   ├── base.css          ← body, typography base
│   │   ├── layout.css        ← grid, container, section spacing
│   │   └── components/
│   │       ├── nav.css
│   │       ├── hero.css
│   │       ├── about.css
│   │       ├── services.css
│   │       ├── carousel.css
│   │       ├── gallery.css
│   │       ├── contact.css
│   │       └── footer.css
│   ├── js/
│   │   ├── main.js           ← init, scroll behavior, nav toggle
│   │   ├── carousel.js       ← Swiper init and config
│   │   ├── form.js           ← form validation + Web3Forms submit
│   │   └── reveal.js         ← IntersectionObserver scroll reveal
│   └── assets/
│       ├── images/           ← client photos (optimized)
│       ├── logo/             ← logo files (.svg preferred)
│       └── favicon/
├── public/                   ← static files copied as-is to dist/
├── dist/                     ← build output (deploy this folder)
├── tests/
│   └── checklist.md          ← manual test checklist
└── package.json
```

---

## Sections (confirmed)

| # | Section | Notes |
|---|---|---|
| 1 | **Nav** | Logo + anchor links + mobile hamburger |
| 2 | **Hero** | Headline, subline, CTA button, background image |
| 3 | **About** | Who is Damian, individual approach, free visit |
| 4 | **Services** | Carousel — rolety, żaluzje, plisy, moskitiery |
| 5 | **Why us** | 3–4 trust arguments (free measure, Dekorama catalog, personal approach) |
| 6 | **Gallery** | Photo grid — client has professional photos |
| 7 | **Coverage** | Map + service area (powiat olsztynski) |
| 8 | **Contact** | Form + phone + email + Google Maps embed |
| 9 | **Footer** | Logo, links, copyright, NODE48 credit |

---

## Phases

### PHASE 0 — Setup & Architecture
**Exit condition:** Project boots locally, folder structure created, design tokens drafted

- [ ] Initialize Vite project
- [ ] Create folder structure (src/, css/, js/, assets/)
- [ ] Create CSS variables file (colors, spacing, type scale, breakpoints)
- [ ] Create CSS reset
- [ ] Create base HTML template with all sections stubbed
- [ ] Verify `npm run dev` and `npm run build` work
- [ ] Commit initial structure to LOG.md

---

### PHASE 1 — Design Tokens & Visual Direction
**Exit condition:** Color palette, typography, spacing system defined and approved

- [ ] Define color palette (primary, accent, neutral, background, text)
- [ ] Define typography scale (H1–H4, body, caption, label)
- [ ] Define spacing scale (4px base grid)
- [ ] Define breakpoints (mobile 375, tablet 768, laptop 1024, desktop 1440)
- [ ] Define border-radius, shadow, transition defaults
- [ ] Log design decisions in LOG.md

---

### PHASE 2 — Component Development (section by section)
**Exit condition:** All sections built, responsive on all breakpoints

- [ ] Nav — logo + anchor links + mobile hamburger menu
- [ ] Hero — headline, subline, CTA, background
- [ ] About — text + photo, individual approach messaging
- [ ] Services — Swiper carousel with product cards
- [ ] Why us — trust block (icons via Lucide, short text)
- [ ] Gallery — responsive photo grid (CSS columns or grid)
- [ ] Coverage — service area text + Google Maps embed
- [ ] Contact — Web3Forms form + phone/email display
- [ ] Footer — minimal, clean
- [ ] Cookie consent banner (GDPR)

---

### PHASE 3 — Integrations
**Exit condition:** Form sends, analytics fires, map loads, cookies work

- [ ] Web3Forms — connect form to client email (dmsolutions.olsztyn@gmail.com)
- [ ] Google Analytics 4 — add tracking tag
- [ ] Google Maps embed — powiat olsztynski / office location
- [ ] Cookie consent — block GA until consent given

---

### PHASE 4 — SEO & Meta
**Exit condition:** All meta tags present, Lighthouse SEO score ≥ 90

- [ ] `<title>` — descriptive, Polish, includes city
- [ ] `<meta description>` — 150–160 chars, includes main services
- [ ] Open Graph tags (og:title, og:description, og:image)
- [ ] `<link rel="canonical">`
- [ ] `robots.txt`
- [ ] `sitemap.xml`
- [ ] Structured data — LocalBusiness schema (JSON-LD)
- [ ] Favicon set (16, 32, 180, 192, 512px)

---

### PHASE 5 — Security
**Exit condition:** Basic security measures in place for a static site

- [ ] Honeypot field on contact form (anti-spam)
- [ ] Form submission rate limiting (Web3Forms handles server-side)
- [ ] No sensitive data exposed in frontend code (no API keys in JS)
- [ ] Content Security Policy meta tag
- [ ] `rel="noopener noreferrer"` on all external links
- [ ] HTTPS — enforce on hosting (let hosting provider handle SSL)

---

### PHASE 6 — Performance
**Exit condition:** Lighthouse Performance score ≥ 90 on mobile

- [ ] Optimize all images (WebP format, correct dimensions)
- [ ] Lazy-load images below the fold (`loading="lazy"`)
- [ ] `preconnect` hints for Google Fonts and GA
- [ ] Verify no render-blocking resources
- [ ] `prefers-reduced-motion` support in CSS animations
- [ ] Verify hero content is visible before any JS runs (no opacity:0 trap)

---

### PHASE 7 — Testing
**Exit condition:** All checklist items in tests/checklist.md pass

- [ ] Cross-browser: Chrome, Firefox, Edge, Safari (if available)
- [ ] Responsive: 375px, 768px, 1024px, 1440px, 1920px
- [ ] Contact form — sends correctly, success state shows
- [ ] All anchor links scroll correctly
- [ ] Carousel works on touch (mobile swipe) and mouse drag
- [ ] All images load, no broken src
- [ ] No console errors
- [ ] Lighthouse audit (Performance, Accessibility, Best Practices, SEO) — all ≥ 90
- [ ] HTML validation (validator.w3.org)

---

### PHASE 8 — Deployment Prep & Handoff
**Exit condition:** Client can host this on any standard provider without help

- [ ] `npm run build` produces clean `dist/` folder
- [ ] Test `dist/` served locally (no paths broken)
- [ ] Write DEPLOY.md — step-by-step for cPanel, Netlify, Vercel, GitHub Pages
- [ ] Confirm all assets are in `dist/` (fonts, images, favicon)
- [ ] Final client review
- [ ] Transfer: domain setup instructions, hosting login, source files, dist/

---

## Pending from client

- [ ] Logo file (.svg / .ai / .eps / .pdf)
- [ ] Full services list with descriptions (promised via email)
- [ ] Existing texts / materials (promised via email)
- [ ] Domain name decision

---

## Out of scope (base price)

- CMS / blog
- English version
- Video production
- WhatsApp widget (can add later, +150 zł)
