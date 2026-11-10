---
title: plasma-posters
description: Scientific posters from Python, a layout of text, figures and equations written to a print-ready PDF
sidebar:
  order: 18
---

Build a poster from blocks of text and figures in columns. Text, titles and captions are LaTeX, so equations look as they do in a paper:

```python
from plasma_posters import Poster

poster = Poster(
    "Speeds in a thermal plasma",
    authors="Max Lindqvist",
    institute="Max Planck Institute for Plasma Physics",
    columns=2,
)
poster.block("The distribution", r"$f(v) \propto v^2 \exp(-m v^2 / 2 k_B T)$")
poster.figure("Three temperatures", "maxwellian.pdf", caption="Normalised to its peak.", column=1)
poster.build("poster.pdf")
```

The poster is a [tikzposter](https://ctan.org/pkg/tikzposter) LaTeX file, compiled with lualatex on A0, A1 or A2 paper; figures come from Matplotlib, [plasma-plots](/projects/plasma-plots/) or [maxplotlib](/projects/maxplotlib/).

You can find the documentation [here](https://max-models.github.io/plasma-posters/).

[Check out the code on GitHub!](https://github.com/max-models/plasma-posters)
