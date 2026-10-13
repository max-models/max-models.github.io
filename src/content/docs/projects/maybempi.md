---
title: maybempi
description: Use MPI only when launched under MPI, and a serial stand-in for mpi4py otherwise
sidebar:
  order: 11
---

Install from PyPI with

```sh
pip install maybempi            # serial runs only
pip install "maybempi[mpi]"     # with mpi4py, for MPI runs
```

The same code runs under `mpirun`/`srun` and as a plain `python script.py`, and the serial run never starts MPI:

```python
from maybempi import MPI  # instead of: from mpi4py import MPI

# mpi4py.MPI under mpirun/mpiexec/srun, a serial stand-in otherwise
comm = MPI.COMM_WORLD
total = comm.allreduce(local_total, op=MPI.SUM)  # local_total in a serial run
```

Importing `mpi4py.MPI` calls `MPI_Init`, which costs close to a second and makes every collective cost something, even on one process. maybempi decides from the environment variables that MPI launchers export, without importing mpi4py, and in a serial run returns a stand-in whose collectives give the results MPI gives on one process. It is pure Python with no dependencies.

You can find the documentation [here](https://max-models.github.io/maybempi/).

[Check out the code on GitHub!](https://github.com/max-models/maybempi)

Links:

- https://pypi.org/project/maybempi/
