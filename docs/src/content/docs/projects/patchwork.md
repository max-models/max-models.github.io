---
title: patchwork
description: 2D block-structured adaptive meshes backed by mpiarray
image: https://max-models.github.io/patchwork/figures/two_level_mesh.png
featured: true
sidebar:
  order: 13
gallery:
  - page: https://max-models.github.io/patchwork/getting-started/quickstart/
    src: https://max-models.github.io/patchwork/figures/two_level_mesh.png
    caption: "Density on a coarse grid with a fine patch"
  - page: https://max-models.github.io/patchwork/getting-started/quickstart/
    src: https://max-models.github.io/patchwork/figures/composite_poisson.png
    caption: "Composite Poisson solution on a refined patch"
  - page: https://max-models.github.io/patchwork/tutorials/06-regridding/
    src: https://max-models.github.io/patchwork/tutorials/06-regridding/4.gif
    caption: "Patches following a moving blob as the mesh is regridded"
  - page: https://max-models.github.io/patchwork/tutorials/06-regridding/
    src: https://max-models.github.io/patchwork/tutorials/06-regridding/2.png
    caption: "Properly nested patches over a ring of tagged cells"
  - page: https://max-models.github.io/patchwork/tutorials/04-non-rectangular-domains/
    src: https://max-models.github.io/patchwork/tutorials/04-non-rectangular-domains/3.png
    caption: "Potential in a non-rectangular domain, refined at the corners"
---

Install from GitHub with

```sh
pip install git+https://github.com/max-models/patchwork
```

Patchwork stores cell-centered or node-centered fields on nested rectangular patches using [mpiarray](/projects/mpiarray/). The same API works with and without MPI; under `mpiexec`, each patch lives on the ranks you give it, and `exchange_halos` fills every patch's halo from its neighbours and the level below.

```python
from patchwork import AMRHierarchy, plot_patches

mesh = AMRHierarchy(base_shape=(32, 24))
fine = mesh.add_patch(level=1, box=((16, 48), (12, 36)))
mesh.allocate_field("density")
fine.field("density").local[:] = 1.0
fig, ax = plot_patches(mesh, field="density")
```

It includes composite Poisson solvers (cell-centered finite volumes, and a node-centered solver with Dirichlet and Neumann faces, periodic axes and embedded bodies, factorized once for particle-in-cell codes), and `regrid`, which places properly nested patches over tagged cells with Berger-Rigoutsos clustering.

You can find the documentation [here](https://max-models.github.io/patchwork/).

[Check out the code on GitHub!](https://github.com/max-models/patchwork)
