# max-models.github.io

Personal website of Max Lindqvist, built with [Astro](https://astro.build),
[Starlight](https://starlight.astro.build) and the shared max-models theme
[starlight-theme](https://github.com/max-models/starlight-theme), served at https://max-models.github.io.

`astro.config.mjs` uses the theme's `defineDocs`, with the base path set to `/` (a user site is
served at the root, not under `/<repo>/`). To update the theme, bump the tag:
`npm install github:max-models/starlight-theme#vX.Y.Z`.

## Running locally

Requires Node.js 22.12 or newer.

```sh
npm install
DOCS_VALIDATE_LINKS=false npm run dev   # http://localhost:4321, without the link check
npm run build    # static site in dist/, with the link check
npm run preview  # serve dist/
```

## Content

All pages are Markdown/MDX files in `src/content/docs/`; the path of a file is its URL.

| Directory       | Section                                                    |
| --------------- | ---------------------------------------------------------- |
| `index.mdx`     | Home page                                                  |
| `publications/` | One page per publication, listed on `/publications/`       |
| `projects/`     | One page per project, shown as cards on `/projects/`       |

The extra frontmatter fields are defined in `src/content.config.ts`:

```yaml
# publications/2024-03-25-particle-injection-methods.md
title: "Particle injection methods in 3D-PIC MCC simulations applied to plasma grid biasing"
date: 2024-03-25
category: manuscripts          # manuscripts | conferences | books
venue: "Physics of Plasmas"
doi: "10.1063/5.0187850"
citation: "**M. Lindqvist**, D. Wünderlich, ..., *Phys. Plasmas* 31, 033903 (2024)"
```

```yaml
# projects/onix.md
title: ONIX
description: 3D Particle-in-cell code for simulating negative ion extraction
image: https://...              # picture on the project card (optional)
sidebar:
  order: 1                      # position on /projects/ and in the sidebar
```

Static files (favicons, PDFs, ...) go in `public/`.

## Deployment

`.github/workflows/deploy.yml` builds the site and deploys it to GitHub Pages on every push to
`master`. In the repository settings, Pages → Source must be set to **GitHub Actions**.

The old academicpages URLs (`/publication/...`, `/portfolio/...`, `/posts/...`) redirect to their
new locations; see `redirects` in `astro.config.mjs`.
