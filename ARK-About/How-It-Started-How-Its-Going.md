---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "slide"} -->
# Econ-ARK: How It Started / ~~How~~ Where It's Going

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## How it Started

- Officially founded in 2017, formally organizing work by MNW, NMP, and DCL at CFPB in 2015-16
- Received generous grant from [Alfred P. Sloan Foundation](https://sloan.org) to develop/professionalize HARK package
  - [Heterogeneous Agents Resources and toolKit](https://github.com/econ-ark/HARK)
  - Software package for solving, simulating, estimating heterogeneous agents models
  - _Framework_ for working with models; all solution and simulation code is handcrafted
- Use [NumFocus](https://numfocus.org/) as fiscal sponsor: manager for various open source scientific computing projects
- Later received funding from [Think Forward Initiative](https://inomics.com/institution/think-forward-initiative-1258337) and [T. Rowe Price](https://www.troweprice.com/en)
- Largely achieved our original set of goals for HARK, but still improving!

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Big Next Steps

- Want to develop a _language_ or _schema_ for expressing dynamic structural models
  - Model content
  - Computational methods
  - Simulation procedure details
  - Specify model outputs
- Input as _model files_, just like [Dynare](https://www.dynare.org/)
  - We want to make "Dynare for heterogeneous agents"
  - (This is what many people thought HARK was "supposed to be" on first impression!)
- Precisely convey information in machine- and human-readable format
- Model file is independent of solution code, but:
  - Will develop software platform to parse models into implied code
  - Want it to connect to existing solvers/tools for specific problem types
- This is big and ambitious, but experience with HARK has set us up well

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Hasn't Someone Already Done This?

- Looked into whether _other_ academic fields (e.g. OR) have developed a dynamic modeling schema
- Nothing looked sufficient for using or expanding for our purposes
- _Many_ modeling- and optimization-adjacent software tools out there...
  - ...but they're diverse and diffuse, not connected
  - No scheme for "putting the blocks together"
  - Lots of hammers, drills and saws; no [CAD/CAM](https://www.autodesk.com/solutions/cad-cam)
- Analogous problem in AI: many (very new) tools, no platform for connecting them

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Goal 1: Transparency & Replicability

- All structural results depend on many ancillary numeric assumptions
  - Everyone knows it, loathe to admit it
  - Sometimes there's a secret ingredient in the soup
  - The soup probably has some rat droppings in it
- Now expected to publicly archive your code (and good journals require it)
  - But no one checks it!
  - Big difference between code being _available_ vs _accessible_
- Not even a guarantee that _model on paper_ matches _model in code_
- Econ doesn't have a "replicability crisis", but _some stuff_ has happened
- Our proposed platform enforces connection between human-readable model and computer-executed model
  - _And_ clearly specifies all of the "hidden assumptions"
  - Allows framework for testing/verification of alternate solution methods

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Goal 2: Accelerate Frontier Economic Applications

- New academic research teams/collaborations can better communicate ideas
  - Tear down the "Tower of Babel" programming problem!
- Policy-makers can more easily develop and iterate on internal HA models
  - Prospective analysis of potential policy actions/interventions/changes
  - (Some) central banks already do this, using their own toolsets
  - Financial regulators? Probably should, likely don't right now
- New uses for private financial institutions / consumer banks
  - Recommendations for retirement investing strategy not necessarily well founded
  - Could be based on structural lifecycle consumption-saving model w/ portfolio choice

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## ~~How~~ Where It's Going

- We have a good team and **big** plans
- Currently seeking next large tranche of funding / ongoing sources
- Potential sources from private entities
- Central bank funding / sponsorship?
  - Talk to your division head today!

<!-- #endregion -->
