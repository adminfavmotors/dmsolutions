# DMSolutions — Release Checklist

Run this checklist before every client review and before final handoff.

---

## Responsive / Device

| Test | 390px | 768px | 1024px | 1440px |
|---|---|---|---|---|
| Header and nav render correctly | | | | |
| Hero copy is readable and CTA is visible | | | | |
| Carousel controls / dots behave correctly | | | | |
| Services grid keeps correct spacing | | | | |
| `Dlaczego my` layout and photo strip are intact | | | | |
| `Dlaczego my` / `Kontakt` icons match the local Phosphor style | | | | |
| Contact form fits without overflow | | | | |
| Footer is intact and aligned | | | | |
| No horizontal scroll | | | | |

## Progressive Enhancement

- [ ] First screen renders correctly with JavaScript disabled
- [ ] Hero heading and CTA stay above the fold without JavaScript
- [ ] Privacy policy page renders correctly without any `/src` dependency

## Functionality

- [ ] Anchor links scroll to the correct sections
- [ ] Mobile nav opens, closes, and closes on link click
- [ ] Carousel advances with controls and dots
- [ ] Keyboard arrows change slides only inside the hero context
- [ ] Contact form shows loading / success / error state correctly
- [ ] Form submission works after inserting the real Web3Forms key
- [ ] Google Maps embed loads
- [ ] Privacy policy footer shows the current year

## Content

- [ ] No placeholder text (`TODO`, `INSERT`, unfinished client data) on public pages
- [ ] All images load correctly
- [ ] Phone number is clickable (`tel:`)
- [ ] Email is clickable (`mailto:`)
- [ ] Privacy policy reflects the current technical setup
- [ ] Full legal/business data is filled in after the client provides it

## Performance

- [ ] `npm run images:hero` has been run after changing hero masters
- [ ] Browser loads responsive hero variants (`768w` / `1536w`) instead of original JPG masters
- [ ] No external requests to Google Fonts / `unpkg` are made during page render
- [ ] Lighthouse run captured for homepage

## SEO / Metadata

- [ ] `<title>` is present and descriptive
- [ ] `<meta name="description">` is present
- [ ] Open Graph tags are present
- [ ] LocalBusiness JSON-LD is present in `<head>`
- [ ] `robots.txt` is available after domain setup
- [ ] `sitemap.xml` is available after domain setup
- [ ] `og:url` is filled after domain setup

## Security / Privacy

- [ ] No secrets or production keys are exposed in source files
- [ ] External links that open new tabs use `rel="noopener"`
- [ ] Privacy policy still matches actual external services in use (`Web3Forms`, Google Maps)

## Code Quality

- [ ] `npm run build` passes
- [ ] `npm run lint` passes
- [ ] No console errors on load
- [ ] No console errors during interaction
- [ ] No dead assets / files created during the work session
- [ ] `PLAN.md`, `README.md`, and `CLAUDE.md` reflect the current system state

---

## Sign-off

- [ ] All applicable items above are checked
- [ ] `LOG.md` is updated if a commit-worthy architectural change was made
- [ ] Client blockers are listed clearly before handoff
