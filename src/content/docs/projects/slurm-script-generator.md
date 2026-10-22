---
title: slurm-script-generator
description: Generate Slurm scripts from the console
sidebar:
  order: 9
---

Check out the web version [here](https://slurm-script-generator.github.io).

Generate a batch script from the CLI:

```sh
generate-slurm-script --nodes 1 --ntasks-per-node 16 --output-path job.sh
```

Or construct a script in Python and add site-specific commands:

```python
from slurm_script_generator.slurm_script import SlurmScript

job = SlurmScript(
    nodes=2,
    ntasks_per_core=16,
    custom_commands=["module load python", "srun python simulation.py"],
)
print(job.generate_script())
```

You can install the CLI and Python API from PyPI with

```sh
pip install slurm-script-generator
```

[Check out the code on GitHub!](https://github.com/max-models/slurm-script-generator)

Links:

- https://pypi.org/project/slurm-script-generator/
