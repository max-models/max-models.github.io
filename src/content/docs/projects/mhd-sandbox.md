---
title: mhd-sandbox
description: A finite-volume solver for two-dimensional ideal magnetohydrodynamics
image: https://max-models.github.io/mhd-sandbox/tutorials/orszag-tang/1.png
gallery:
  - page: https://max-models.github.io/mhd-sandbox/tutorials/orszag-tang/
    src: https://max-models.github.io/mhd-sandbox/tutorials/orszag-tang/1.png
    caption: "Orszag–Tang vortex"
  - page: https://max-models.github.io/mhd-sandbox/tutorials/test-problems/
    src: https://max-models.github.io/mhd-sandbox/tutorials/test-problems/5.png
    caption: "MHD rotor: magnetic pressure and plasma beta"
  - page: https://max-models.github.io/mhd-sandbox/tutorials/test-problems/
    src: https://max-models.github.io/mhd-sandbox/tutorials/test-problems/8.png
    caption: "Magnetized blast wave: magnetic pressure and fast Mach number"
  - page: https://max-models.github.io/mhd-sandbox/tutorials/multifluid/
    src: https://max-models.github.io/mhd-sandbox/tutorials/multifluid/1.png
    caption: "Thermal plasma and beam densities in a multifluid run"
---

A small NumPy-based solver for ideal MHD on a periodic 2D grid, with notebooks for the Orszag–Tang vortex, MHD rotor, and magnetized blast wave.

The solver uses first-order Rusanov fluxes, forward Euler time stepping, and a Fourier projection to keep the magnetic field divergence-free. Its intentionally compact implementation makes it useful for learning and experimenting with finite-volume MHD.

Run the Orszag–Tang vortex in a few lines:

```python
from mhd_sandbox import Grid, IdealMHD2DSolver

grid = Grid(lower_bound=(0.0, 0.0), upper_bound=(1.0, 1.0), num_gridpoints=(128, 128))
solver = IdealMHD2DSolver(grid, cfl=0.3)
solver.set_state(IdealMHD2DSolver.orszag_tang_initial_state(grid))
result = solver.solve(t_end=0.5)
print(result.steps, result.max_divergence_b)
```

Documentation: [max-models.github.io/mhd-sandbox](https://max-models.github.io/mhd-sandbox/)

[View the code on GitHub](https://github.com/max-models/mhd-sandbox) · [PyPI](https://pypi.org/project/mhd-sandbox/)
