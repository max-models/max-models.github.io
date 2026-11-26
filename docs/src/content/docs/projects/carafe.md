---
title: carafe
description: Global and fluid models of low-temperature plasmas
image: /thumbnails/carafe.png
gallery:
  - page: https://max-models.github.io/carafe/full-examples/rf-driver-inductive-field-2d/
    src: https://max-models.github.io/carafe/full-examples/rf-driver-inductive-field-2d/plot-3.png
    caption: "Magnetic field and absorbed RF power of two drivers with a prescribed plasma"
  - page: https://max-models.github.io/carafe/full-examples/rf-driver-inductive-field-2d/
    src: https://max-models.github.io/carafe/full-examples/rf-driver-inductive-field-2d/plot-2.png
    caption: "RF power transfer efficiency against the distance from the coil to the shield"
  - page: https://max-models.github.io/carafe/full-examples/rf-driver-rz/
    src: https://max-models.github.io/carafe/full-examples/rf-driver-rz/plot-1.png
    caption: "Absorbed power in the BUG driver, with cold and viscous electrons"
  - page: https://max-models.github.io/carafe/full-examples/spoke-drift-fluid-2d/
    src: https://max-models.github.io/carafe/full-examples/spoke-drift-fluid-2d/plot-1.png
    caption: "Growth of spoke modes in the 2D drift fluid against theory"
  - page: https://max-models.github.io/carafe/full-examples/hipims-global-model/
    src: https://max-models.github.io/carafe/full-examples/hipims-global-model/plot-1.png
    caption: "A HiPIMS magnetron global model: rarefaction, metal ions and self-sputtering"
---

`carafe` provides global (0D), 1D drift-diffusion, and 2D drift-fluid models for low-temperature plasmas, including magnetron models and plasma chemistry.

Use the global model for fast steady-state calculations and parameter scans; the 1D and 2D models resolve spatial transport and magnetron spokes. The models include reaction networks, wall and cusp losses, gas feed and pumping, and beam sources for coupled studies.

It is used alongside [beamtracer](/projects/beamtracer/) to model plasma neutralizers.

Documentation: [max-models.github.io/carafe](https://max-models.github.io/carafe/)

[View the code on GitHub](https://github.com/max-models/carafe) · [PyPI](https://pypi.org/project/plasma-carafe/)
