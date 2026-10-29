---
title: cunumpy
description: One NumPy-style codebase for the CPU and the GPU, with CUDA, Metal and Pyccel kernels
sidebar:
  order: 7
---

Install from PyPI with

```sh
pip install cunumpy
```

Replace `import numpy as np` with `import cunumpy as xp`, and the same array code runs on NumPy arrays on the CPU or on CuPy arrays on an NVIDIA GPU:

```python
import cunumpy as xp

values = xp.arange(5, dtype=xp.float64)
print(values * 2)
print(xp.get_backend())  # 'numpy', or 'cupy' with CUNUMPY_BACKEND=cupy

with xp.use_backend("cupy"):
    signal = xp.asarray(host_signal)  # one explicit transfer to the GPU
    spectrum = xp.fft.rfft(signal)
    result = xp.to_numpy(spectrum)  # and one back
```

The backend is chosen once, at the entry point of a program, and transfers between CPU and GPU are always explicit, so it is clear where the data lives. When CUDA is not available, cunumpy falls back to NumPy, and a fake CuPy backend runs the GPU code paths in tests on machines without a GPU.

For the hot loops that array operations cannot express, cunumpy pairs each host kernel with its GPU version and calls the one matching the backend, so a code can be ported to the GPU one kernel at a time:

- **CUDA kernels** written next to the Pyccel or Python kernels they mirror, compiled with NVRTC, with their arguments checked against the C signature on every call.
- **Metal kernels** for the GPU of an Apple silicon Mac.
- **Pyccel kernels** that run on CuPy arrays through host copies, for kernels that are not ported yet.
- **C structs and strided array views** generated from the Python argument classes, so kernels ported from Pyccel keep their `markers[ip, j]` indexing.

Around the kernels are the building blocks of GPU particle codes: random number streams, sorting and segmented reductions, Morton keys, CUDA-aware MPI buffers, host and device staging, NVTX ranges and transfer counting.

The GPU port of [STRUPHY](/projects/struphy/) is built on cunumpy, and so are [mpiarray](/projects/mpiarray/), [plasmacoll](/projects/plasmacoll/) and [beamtracer](/projects/beamtracer/).

You can find the documentation [here](https://max-models.github.io/cunumpy/).

[Check out the code on GitHub!](https://github.com/max-models/cunumpy)

Links:

- https://pypi.org/project/cunumpy/
