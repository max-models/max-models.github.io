---
title: scope-profiler
description: Profile Python code with mpi4py and LIKWID
image: https://max-models.github.io/scope-profiler/figures/cli/durations_plot_total.png
sidebar:
  order: 6
---

Install from PyPI with

```sh
pip install scope-profiler
```

Mark the regions you want to measure, then run the script through the CLI to save an HDF5 profile and print a summary:

```python
import scope_profiler as sp

with sp.session():
    @sp.profile("main")
    def main():
        with sp.region("work"):
            sum(range(100))

    main()
```

```sh
scope-profiler run app.py
scope-profiler inspect profiling_data.h5 --sort total
```

The same API supports MPI, native code instrumentation, tags, sampling, pytest profiling, and notebook workflows. Results can be explored with the [profiling catalogue](/projects/scope-profiler-catalog/).

[Check out the code on GitHub!](https://github.com/max-models/scope-profiler)

Links:

- https://pypi.org/project/scope-profiler/

![Profile duration chart](https://max-models.github.io/scope-profiler/figures/cli/durations_plot_total.png)
