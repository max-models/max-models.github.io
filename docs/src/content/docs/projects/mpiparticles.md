---
title: mpiparticles
description: Distributed particle storage and migration for MPI codes
image: https://max-models.github.io/mpiparticles/full-examples/owner-map/plot-1.png
gallery:
  - page: https://max-models.github.io/mpiparticles/full-examples/owner-map/
    src: https://max-models.github.io/mpiparticles/full-examples/owner-map/plot-1.png
    caption: "Which rank owns which particle"
---

`mpiparticles` provides per-rank particle storage on NumPy or CuPy arrays, globally unique particle IDs, and migration between ranks. It also runs in serial without making MPI calls.

The basic workflow creates storage, pushes positions, then collectively migrates particles to the rank that owns their new positions:

```python
import cunumpy as xp
import maybempi
from mpiparticles import BoxDecomposition, IdAllocator, ParticleStore, migrate

comm = maybempi.get_mpi().COMM_WORLD
domain = BoxDecomposition(comm, [0.0, 0.0], [1.0, 1.0], proc_sizes=[1, comm.size])
store = ParticleStore(ndim=2, nvel=3, id_allocator=IdAllocator.from_comm(comm))
store.add(xp.asarray([[0.2, 0.7], [0.4, 0.9]]), xp.zeros((3, 2)))
store.positions[:, : store.length] += 0.1
sent, received = migrate(store, domain)
```

Particle IDs remain exact as 64-bit integers, and the same code runs with a single process or under `mpiexec`.

Documentation: [max-models.github.io/mpiparticles](https://max-models.github.io/mpiparticles/)

[View the code on GitHub](https://github.com/max-models/mpiparticles) · [PyPI](https://pypi.org/project/mpiparticles/)
