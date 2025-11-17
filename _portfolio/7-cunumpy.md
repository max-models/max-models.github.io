---
title: "cunumpy"
excerpt: "Simple wrapper for numpy and cupy"
collection: portfolio
---

Install from pypi with

````
pip install cunumpy
```

Simple wrapper for numpy and cupy. Replace `import numpy as np` with `import cunumpy as xp`.

Example usage:

```
export ARRAY_BACKEND=cupy
```

```python
import cunumpy as xp
arr = xp.array([1,2])

print(type(arr))
print(xp.__version__)
```

[Check out the code on Github!](https://github.com/max-models/cunumpy)

Links:
- https://pypi.org/project/cunumpy/