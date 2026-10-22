---
title: maxplotlib
description: Python wrapper for Matplotlib/Plotly, produce figures with consistent formatting
image: https://raw.githubusercontent.com/max-models/maxplotlib/main/README_files/figure-commonmark/cell-3-output-1.png
sidebar:
  order: 8
---

Install from PyPI with

```sh
pip install maxplotlibx
```

Build a canvas with a familiar axes API, then render it with a selected backend:

```python
import numpy as np
from maxplotlib import Canvas

x = np.linspace(0, 2 * np.pi, 200)
canvas, ax = Canvas.subplots()
ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)")
ax.legend()
canvas.show()
```

The same figure can be rendered with Matplotlib, Plotly, plotext, or TikZ, keeping data and figure construction separate from the output backend.

![A sine curve rendered with maxplotlib](https://raw.githubusercontent.com/max-models/maxplotlib/main/README_files/figure-commonmark/cell-3-output-1.png)

You can find the documentation and examples [here](https://max-models.github.io/maxplotlib/).

[Check out the code on GitHub!](https://github.com/max-models/maxplotlib)

Links:

- https://pypi.org/project/maxplotlibx/
