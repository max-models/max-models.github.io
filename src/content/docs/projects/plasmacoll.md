---
title: plasmacoll
description: Monte Carlo collisions of charged particles with neutral gases, on NumPy or CuPy arrays
image: https://max-models.github.io/plasmacoll/tutorials/03-ionization-attachment/1.png
sidebar:
  order: 14
---

Install from PyPI with

```sh
pip install plasmacoll
```

Null-collision Monte Carlo collisions (MCC) of charged particles with neutral gases: the collision step of a particle-in-cell code, or, with `ZeroDReactor`, a homogeneous reactor for testing cross-section sets.

- **Processes:** elastic, charge exchange, excitation, ionization, attachment, detachment, dissociation and more, with isotropic or forward-peaked scattering.
- **Cross sections** from text tables, LXCat files or functions.
- **Plain arrays:** markers are positions, velocities and weights, and [cunumpy](/projects/cunumpy/) runs the same code on CPU (NumPy) or GPU (CuPy).
- **Validated** against the closed-form relaxation, growth and decay rates of Maxwell-molecule gases and swarm drift in a field.

You can find the documentation and tutorials [here](https://max-models.github.io/plasmacoll/).

[Check out the code on GitHub!](https://github.com/max-models/plasmacoll)

Links:

- https://pypi.org/project/plasmacoll/

![Electron, H₂⁺ and H⁻ densities in a 0D reactor against the analytic growth rate](https://max-models.github.io/plasmacoll/tutorials/03-ionization-attachment/1.png)
