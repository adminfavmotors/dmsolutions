# DMSolutions — Test Checklist

Run this checklist before every client review and before final handoff.

---

## Responsive / Device

| Test | 375px | 768px | 1024px | 1440px | 1920px |
|---|---|---|---|---|---|
| Nav renders correctly | | | | | |
| Hero readable, CTA visible | | | | | |
| Carousel works (swipe/drag) | | | | | |
| Gallery grid looks correct | | | | | |
| Contact form fits without overflow | | | | | |
| Footer not broken | | | | | |
| No horizontal scroll | | | | | |

## Cross-Browser

| Test | Chrome | Firefox | Edge | Safari |
|---|---|---|---|---|
| Layout correct | | | | |
| Carousel works | | | | |
| Animations play | | | | |
| Form submits | | | | |
| Map loads | | | | |

## Functionality

- [ ] Contact form submits — email received at dmsolutions.olsztyn@gmail.com
- [ ] Form shows success state after submit
- [ ] Form honeypot field hidden and not submitted
- [ ] All anchor links (#about, #services, etc.) scroll to correct section
- [ ] Mobile nav opens and closes
- [ ] Mobile nav closes on link click
- [ ] Cookie consent banner appears on first visit
- [ ] GA fires only after consent given
- [ ] All external links open in new tab
- [ ] Google Maps embed loads

## Content

- [ ] No placeholder text (Lorem ipsum, TODO, [INSERT])
- [ ] All images load (no broken src)
- [ ] Logo displays correctly on all backgrounds
- [ ] Phone number is clickable (tel: link) on mobile
- [ ] Email is clickable (mailto: link)
- [ ] Favicon shows in browser tab

## Performance (Lighthouse — all must be ≥ 90)

| Metric | Score | Pass? |
|---|---|---|
| Performance | | |
| Accessibility | | |
| Best Practices | | |
| SEO | | |

## SEO

- [ ] `<title>` present and descriptive
- [ ] `<meta description>` present (150–160 chars)
- [ ] Open Graph tags present
- [ ] `canonical` link present
- [ ] `robots.txt` accessible at /robots.txt
- [ ] `sitemap.xml` accessible at /sitemap.xml
- [ ] LocalBusiness JSON-LD present in `<head>`
- [ ] All images have `alt` attributes

## Security

- [ ] No API keys or sensitive data in JS files
- [ ] All external links have `rel="noopener noreferrer"`
- [ ] CSP meta tag present
- [ ] Form honeypot in place

## Code Quality

- [ ] No console errors on page load
- [ ] No console errors during interaction
- [ ] HTML validates at validator.w3.org
- [ ] No unused CSS files
- [ ] `dist/` builds without errors (`npm run build`)

---

**Sign-off before handoff:**

- [ ] All items above checked
- [ ] LOG.md updated with final test results
- [ ] DEPLOY.md written and reviewed
- [ ] Client reviewed and approved
