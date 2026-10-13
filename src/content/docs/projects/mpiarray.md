---
title: mpiarray
description: Distributed NumPy/CuPy arrays over MPI with halo exchange, created like NumPy arrays
image: https://max-models.github.io/mpiarray/guides/heat-equation/1.png
sidebar:
  order: 10
---

Install from PyPI with

```sh
pip install mpiarray
```

Distributed NumPy/CuPy arrays over MPI, with halo exchange, that you create like NumPy arrays. The same script runs under `mpiexec` and as a plain `python example.py`.

```python
import numpy as np

import mpiarray as mpa

a = mpa.array([1, 2, 3, 4])  # mpiexec -n 2: rank 0 holds [1, 2], rank 1 holds [3, 4]
b = mpa.zeros((64, 48), split=(0, 1), halo=1, periodic=(True, False))
c = 2 * a + np.sin(a)  # elementwise: no communication

total = c.sum()  # collective: the same value on every rank
full = c.gather()  # collective: the whole array on every rank
```

It covers halo updates for stencils and particle deposition, NumPy's operators, ufuncs and reductions, redistribution and load balancing, particle migration, and parallel `.npy`/HDF5 I/O. Arrays come from [cunumpy](/projects/cunumpy/), so the same code runs on the GPU.

You can find the documentation and guides [here](https://max-models.github.io/mpiarray/).

[Check out the code on GitHub!](https://github.com/max-models/mpiarray)

![Heat equation solved on a distributed mpiarray](https://max-models.github.io/mpiarray/guides/heat-equation/1.png)
