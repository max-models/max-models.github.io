---
title: whereami
description: Detect the current HPC machine and load the right environment modules for it
sidebar:
  order: 17
---

A.k.a. overengineered `module load`. Install into `$HOME/.local/bin` with

```sh
curl -fsSL https://raw.githubusercontent.com/max-models/whereami/main/install.sh | bash
```

`whereami` identifies the current HPC system, CPU and GPU and exports environment variables describing it; `load_modules` reads a `modules.json` file and loads the right environment modules for the detected machine.

```sh
source whereami          # detect and export variables into the current shell
whereami -o machine.json # also save the detected parameters as JSON
```

```json
{
  "MACHINE_NAME": "Raven",
  "MACHINE_HOST": "MPCDF",
  "CPU_VENDOR": "Intel",
  "CHIP": "IceLake",
  "GPU_VENDOR": "NVIDIA",
  "GPU_NAME": "A100"
}
```

[Check out the code on GitHub!](https://github.com/max-models/whereami)
