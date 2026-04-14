# DMSolutions

Landing page for `DMSolutions` built with `Vite + Vanilla HTML/CSS/JS`.

## Stack

- Vite
- Vanilla HTML
- Modular CSS
- Modular JavaScript

## Local development

```bash
npm install
npm run dev
```

## Production build

```bash
npm run build
```

Build output is generated in `dist/`.

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
