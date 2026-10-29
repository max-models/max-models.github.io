---
title: STRUPHY
description: Structure-preserving finite elements and particle-in-cell methods for fluid, kinetic and hybrid plasma models, on CPUs and GPUs
image: https://struphy-hub.github.io/images/stellarator-hero.webp
featured: true
sidebar:
  order: 1
gallery:
  - page: https://struphy-hub.github.io/
    src: https://struphy-hub.github.io/images/stellarator-hero.webp
    caption: "Field lines in a GVEC stellarator, with the same ions followed as guiding centres (red) and as full orbits (blue)"
  - page: https://struphy-hub.github.io/examples/gvec-equilibrium/
    src: https://struphy-hub.github.io/images/examples/gvec-equilibrium.png
    plotly: https://struphy-hub.github.io/examples/gvec-equilibrium.plotly.json
    caption: "Guiding-centre orbits on the nested flux surfaces of a five-field-period stellarator"
  - page: https://struphy-hub.github.io/examples/vlasov-tokamak/
    src: https://struphy-hub.github.io/images/examples/vlasov-tokamak.png
    caption: "Full-orbit particle trajectories gyrating around a tokamak"
  - page: https://struphy-hub.github.io/examples/gyromotion/
    src: https://struphy-hub.github.io/images/examples/gyromotion-helices.png
    plotly: https://struphy-hub.github.io/examples/gyromotion-helices.plotly.json
    caption: "Helical orbits of charged particles around a uniform magnetic field"
  - page: https://struphy-hub.github.io/examples/two-stream-instability/
    src: https://struphy-hub.github.io/images/examples/two-stream-instability-phasespace.png
    caption: "The phase-space vortex of the two-stream instability"
  - page: https://struphy-hub.github.io/examples/orszag-tang-vortex/
    src: https://struphy-hub.github.io/images/examples/orszag-tang-vortex.png
    caption: "Density and magnetic field lines in the Orszag–Tang vortex"
---

**STRUPHY** stands for **STRU**cture-**P**reserving **HY**brid code (or **STRU**cture-preserving **PHY**sics code). It is an open-source Python package, developed at the Max Planck Institute for Plasma Physics, for fluid, kinetic and hybrid plasma models such as

- Maxwell's equations
- Magneto-hydrodynamics (MHD)
- Vlasov-Poisson and Vlasov-Maxwell kinetic models
- Drift-kinetic models for strongly magnetized plasma
- MHD-kinetic hybrid models

Fields are discretized with B-spline finite elements that form a discrete de Rham complex, so that gradient, curl and divergence hold exactly and the discretization keeps the structure of the equations. Kinetic species are particle-in-cell markers. The 36 models share their substeps, and run on mapped domains from slabs and cylinders to tokamaks and stellarators. The models are written in Python; the loops over particles, cells and spline coefficients are kernels compiled to Fortran or C with [Pyccel](https://github.com/pyccel/pyccel), parallelized with MPI and OpenMP.

**My part:** I am one of the core developers and authors of STRUPHY, and its second-largest contributor. I ported STRUPHY to NVIDIA GPUs: the particle pushers, charge and current accumulation, geometry and spline evaluation and the field diagnostics run as CUDA kernels through [cunumpy](/projects/cunumpy/), markers move between ranks with CUDA-aware MPI, and GPU tests run in CI on the GPU runners at MPCDF. I also work on the performance, testing and tooling of the code, and its plotting through [plasma-plots](/projects/plasma-plots/).

Documentation and examples: [struphy-hub.github.io](https://struphy-hub.github.io/)

[Check out the code on GitHub!](https://github.com/struphy-hub/struphy) · [PyPI](https://pypi.org/project/struphy/)
