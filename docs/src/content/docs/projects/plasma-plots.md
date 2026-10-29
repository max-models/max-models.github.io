---
title: plasma-plots
description: Plots and diagnostics of labeled xarray output from plasma simulations, such as Struphy
image: https://max-models.github.io/plasma-plots/figures/2d_isosurface.gif
sidebar:
  order: 15
gallery:
  - page: https://max-models.github.io/plasma-plots/guides/3d-views/
    src: https://max-models.github.io/plasma-plots/figures/2d_isosurface.gif
    caption: "A rotating mode in a 2D cross-section"
  - page: https://max-models.github.io/plasma-plots/guides/desc/
    match: "|B| on the surface rho = 0.5 of W7-X"
    caption: "|B| of W7-X on the surface ρ = 0.5 and three poloidal cuts, from DESC"
  - page: https://max-models.github.io/plasma-plots/guides/gvec/
    match: "|B| on the last flux surface"
    caption: "|B| on the last flux surface of a three-period stellarator, from GVEC"
  - page: https://max-models.github.io/plasma-plots/guides/3d-views/
    match: "Magnetic field lines in a torus"
    caption: "Magnetic field lines in a torus"
  - page: https://max-models.github.io/plasma-plots/guides/3d-views/
    match: "Guiding-center orbits"
    caption: "Guiding-center orbits: passing, trapped and lost"
  - page: https://max-models.github.io/plasma-plots/guides/field-lines/
    match: "A Poincaré section"
    caption: "A Poincaré section with nested flux surfaces and a chain of two islands"
  - page: https://max-models.github.io/plasma-plots/
    match: "A 3-D equilibrium view"
    caption: "A 3D equilibrium"
---

Install from PyPI with

```sh
pip install plasma-plots
pip install "plasma-plots[netcdf,plotly]"   # netCDF files and interactive plots
```

Plots and diagnostics of labeled xarray data from plasma simulations: the output of [STRUPHY](/projects/struphy/), and of any code whose arrays follow the same conventions. It also reads [GVEC](https://gvec.readthedocs.io)'s equilibrium evaluations directly. Plots can be rendered with Matplotlib, Plotly, PyVista, or as TikZ/pgfplots through [maxplotlib](/projects/maxplotlib/).

You can find the documentation [here](https://max-models.github.io/plasma-plots/).

[Check out the code on GitHub!](https://github.com/max-models/plasma-plots)

Links:

- https://pypi.org/project/plasma-plots/
