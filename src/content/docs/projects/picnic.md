---
title: PICNIC
description: Particle-in-cell tools for negative ions and charged particles
---

PICNIC is a particle-in-cell simulation toolkit for negative ion sources and other charged-particle systems, with field solvers that run on CPUs and GPUs.

Build a model, run it, then evaluate saved quantities from the output:

```python
from picnic import Simulation
from picnic.models.vlasov_poisson import VlasovPoisson
from picnic.parameters import OutputParams

model = VlasovPoisson(dt=1e-11)  # add grid, species, solver and boundary conditions
simulation = Simulation(model, t_end=1e-8, output=OutputParams(every=50))
output = simulation.run()
potential = output.evaluate("potential", t=-1)
```

The package includes matrix-free and PETSc field solvers, optional GPU support, command-line tools, and runnable examples. It connects with [tree-d-3d](/projects/tree-d-3d/) for open-boundary fields and [patchwork](/projects/patchwork/) for adaptive meshes.

Documentation: [max-models.github.io/picnic](https://max-models.github.io/picnic/)

[View the code on GitHub](https://github.com/max-models/picnic)
