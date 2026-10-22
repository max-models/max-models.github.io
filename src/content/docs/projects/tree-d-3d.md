---
title: tree-d-3d
description: Barnes–Hut trees and fast multipole methods for charged particles
---

Tree Dynamics in 3D computes particle fields with Barnes–Hut trees and fast multipole methods, using NumPy, CuPy, or Apple GPU backends. It grew out of PICNIC.

The package offers a flat quadtree for point- and line-charge fields, a direct all-pairs reference calculation, and an electrostatic particle simulation with magnetic fields and absorbing boundaries. The fast multipole method accelerates line-charge field calculations to linear complexity.

It also supplies open-boundary field calculations for [PICNIC](/projects/picnic/).

Documentation: [max-models.github.io/tree-d-3d](https://max-models.github.io/tree-d-3d/)

[View the code on GitHub](https://github.com/max-models/tree-d-3d) · [PyPI](https://pypi.org/project/tree-d-3d/)
