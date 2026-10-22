---
title: simgeometry
description: Shapes, structured grids and simulation domains for numerical simulations
image: https://max-models.github.io/simgeometry/tutorials/shapes-and-node-masks/1.png
sidebar:
  order: 12
gallery:
  - page: https://max-models.github.io/simgeometry/tutorials/shapes-and-node-masks/
    src: https://max-models.github.io/simgeometry/tutorials/shapes-and-node-masks/1.png
    caption: "Grid nodes selected by Circle.node_mask"
  - page: https://max-models.github.io/simgeometry/tutorials/shapes-and-node-masks/
    src: https://max-models.github.io/simgeometry/tutorials/shapes-and-node-masks/3.png
    caption: "A tilted cylinder, a tube with rounded edges, a cone and a tilted torus"
  - page: https://max-models.github.io/simgeometry/tutorials/building-composite-shapes/
    src: https://max-models.github.io/simgeometry/tutorials/building-composite-shapes/5.png
    caption: "Union, intersection and difference of shapes"
  - page: https://max-models.github.io/simgeometry/tutorials/inspecting-geometry/
    src: https://max-models.github.io/simgeometry/tutorials/inspecting-geometry/4.png
    caption: "A torus, a post and a ring"
  - page: https://max-models.github.io/simgeometry/tutorials/parallel-grids/
    src: https://max-models.github.io/simgeometry/tutorials/parallel-grids/1.png
    caption: "Eight subdomains, one colour per rank, around a sphere"
  - page: https://max-models.github.io/simgeometry/tutorials/sampling-export-and-diagnostics/
    src: https://max-models.github.io/simgeometry/tutorials/sampling-export-and-diagnostics/2.png
    caption: "Interior and surface samples of two tori"
---

Install from GitHub with

```sh
pip install git+https://github.com/max-models/simgeometry
```

Geometry primitives for numerical simulations: bounded domains, structured grids, MPI domain decomposition, multipatch geometry, and 1D, 2D and 3D shapes. Box, ball and polygon containment have NumPy, Pyccel, CUDA and Metal implementations.

```python
from simgeometry.grid import Grid
from simgeometry.objects import Circle

boundary = Circle(midpoint=(0.5, 0.5), radius=0.25)
grid = Grid(ndim=2, lower_bound=(0, 0), upper_bound=(1, 1), num_gridpoints=(32, 32))
mask = boundary.node_mask(grid)
```

Shapes support Boolean operations, affine transforms, slicing, surface queries, point sampling and mesh export.

You can find the documentation and tutorials [here](https://max-models.github.io/simgeometry/).

[Check out the code on GitHub!](https://github.com/max-models/simgeometry)
