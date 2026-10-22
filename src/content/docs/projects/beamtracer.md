---
title: beamtracer
description: Self-consistent ion beam extraction, transport and neutralization
---

Trace steady positive or negative ion beams through electrodes and solenoids while solving their self-consistent space-charge field. `beamtracer` supports planar and cylindrical geometry, multiple compute backends, and design optimization.

Define the grid, electrode potentials, and injected species, then run the self-consistent Vlasov iteration:

```python
from beamtracer import BeamOptics, BeamOpticsConfig, BeamSpecies, FieldBCs, FieldBoundaryCondition, GridParams

zero_flux = FieldBoundaryCondition.neumann(0.0)
config = BeamOpticsConfig(
    grid=GridParams(num_gridpoints=(41, 21), upper_bound=(10e-3, 5e-3)),
    bcs_field=FieldBCs(
        x_lower=FieldBoundaryCondition.dirichlet(0.0),
        x_upper=FieldBoundaryCondition.dirichlet(-1000.0),
        y_lower=zero_flux,
        y_upper=zero_flux,
    ),
    beams=[BeamSpecies("H+", 10.0, (0.0, 0.0), (0.0, 5e-3), energy=0.01, num_particles=40)],
)
model = BeamOptics(config).run()
```

Example cases include proton extraction, H⁻ beamlets with co-extracted electrons, and transport through a neutralizer. The compute kernels can use NumPy, CUDA, Metal, or Pyccel through [cunumpy](/projects/cunumpy/).

Documentation: [max-models.github.io/beamtracer](https://max-models.github.io/beamtracer/)

[View the code on GitHub](https://github.com/max-models/beamtracer) · [PyPI](https://pypi.org/project/beamtracer/)
