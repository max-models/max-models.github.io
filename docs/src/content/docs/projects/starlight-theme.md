---
title: starlight-theme
description: The shared Astro + Starlight docs setup of the max-models projects, including this website
sidebar:
  order: 16
---

One Astro + Starlight configuration, look and notebook pipeline for the documentation of the max-models projects (simgeometry, maybempi, mpiarray, patchwork, plasmacoll, ...), installed into each project's `docs/` instead of copied there. This website uses it too.

```sh
npm install github:max-models/starlight-theme#v0.4.0
```

```js
// docs/astro.config.mjs
import { defineDocs } from '@max-models/starlight-theme';

export default defineDocs({
	repo: 'simgeometry',
	title: 'simgeometry',
	description: 'Shapes, structured grids, and domains for numerical simulations.',
	pythonPackage: 'simgeometry', // adds an "API reference" sidebar group
	nav: [{ label: 'Tutorials', link: '/tutorials/' }],
	sidebar: [{ label: 'Tutorials', items: [{ autogenerate: { directory: 'tutorials' } }] }],
});
```

It brings KaTeX math, a header with section links, the API reference of a Python package, a link check, executed Jupyter notebooks as pages, and a reusable GitHub Actions workflow that builds and deploys the site.

You can find the example site [here](https://max-models.github.io/starlight-theme/).

[Check out the code on GitHub!](https://github.com/max-models/starlight-theme)
