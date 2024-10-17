---
title: Econ-ARK for Central Banks
author:
  - name: Christopher D. Carroll
    orcid: 0000-0003-3732-9312
    email: ccarroll@llorracc.org
    affiliations: 
        - Johns Hopkins University
        - Econ-ARK
format: 
    metropolis-revealjs: default
html-math-method:
  method: mathjax
  url: "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
date: last-modified
date-format: "MMMM DD, YYYY"
footer: <https://econ-ark.org>
slide-number: true
embed-resources: true
logo: ../numfocus-logo.png
reveal-header:
    sc-sb-title: true
    header-logo: ../econ-ark-logo.png
    header-text: Powered by Econ-ARK
incremental: true
---


## Microfoundations in a Nutshell (1/2)

### Prehistory

* Modigliani and Brumberg (1954), Friedman (1957), Diamond (1964)
* Perfect Foresight models: 1960s-70s
	
### Bewley (1977)

* Formalization of Friedman PIH
* Rigorous treatment of uncertainty, liq constr
* Entirely qualitative/analytical


## Microfoundations in a Nutshell (2/2)

### Early 1990s: Numerical computation of SS dist'n of wealth

* Life Cycle / OLG:
    + Zeldes (1989); Hubbard, Skinner, and Zeldes (1994, 1995);
    + Huggett (1996); Carroll (1997)
* Infinite Horizon
    + Deaton (1991); Carroll (1992); Aiyagari (1994)
* Aggregate **dynamics**? Hopeless:
    + requires predicting evolution of entire **distribution**


## Dynamics

### [Krusell-Smith (1998)](https://econ-ark.org/materials/krusellsmith/):

* _mean_ of distribution $\bar{k}$ is good enough!
* still excruciatingly slow

### Reiter (2010):

* SS Micro and Dyn Macro *can be solved independently*
    + *Why*? Idiosyncratic shocks 100x larger than agg
    + So agg shocks cause 'small' perturbation of dstn
* $\Rightarrow$ Reiter Singularity: 2014-2018
    + Culmination: ["Sequence Space Jacobian" Toolkit](https://github.com/shade-econ/sequence-jacobian):
    + Bring us your micro SS and Jacobians wrt PF aggregate shocks
        - ...We'll give you the dynamic macro


## Where Does Econ-ARK Fit? (1/2)

### Rich Set of Tools for SS Micro ...

* [Consumption/Saving](https://docs.econ-ark.org/Documentation/reference/ConsumptionSaving/ConsIndShockModel.html)
* [Portfolio Choice](https://docs.econ-ark.org/Documentation/reference/ConsumptionSaving/ConsPortfolioModel.html)
* [Discrete-Continuous Problems](https://econ-ark.org/materials/dcegm-upper-envelope/): [DC-EGM tool](https://docs.econ-ark.org/Documentation/reference/tools/dcegm.html)
* [Labor Supply](https://docs.econ-ark.org/Documentation/reference/ConsumptionSaving/ConsLaborModel.html): [Keane and Imai](https://docs.econ-ark.org/Documentation/reference/tools/incomeprocess.html)
* [Medical Expense Risk](https://docs.econ-ark.org/Documentation/reference/ConsumptionSaving/ConsMedModel.html)
* Life Cycle Modeling: [solutions](https://docs.econ-ark.org/examples/LifecycleModel/Cycles_tutorial.html) and [datasets](https://docs.econ-ark.org/Documentation/reference/tools/incomeprocess.html)
* Sophisticated Liquidity Constraints
    + [Higher rate for borrowing vs saving](https://docs.econ-ark.org/Documentation/reference/ConsumptionSaving/ConsIndShockModel.html#HARK.ConsumptionSaving.ConsIndShockModel.KinkedRconsumerType)
    + [Withdrawal penalties for retirement saving](https://mateovg.com/files/pdf/JMP_VelasquezGiraldoM.pdf)
* Etc etc


## Where Does Econ-ARK Fit? (2/2) {.smaller}

### ...Easy to Connect to SSJ toolkit

1. Econ-ARK/HARK:
   1. solve for micro steady state
   1. compute Jacobians 
1. Feed results to SSJ toolkit

* Documentation Notebooks
    + [HARK and the Sequence Space Jacobian Method](https://docs.econ-ark.org/examples/ConsNewKeynesianModel/SSJ_example.html)
    + [Computing Heterogeneous Agent Jacobians in HARK](https://docs.econ-ark.org/examples/ConsNewKeynesianModel/Jacobian_Example.html)
    + [Solving Krusell-Smith Model with HARK and SSJ](https://docs.econ-ark.org/examples/ConsNewKeynesianModel/KS-HARK-presentation.html)

* Papers:
    + Will Du: [Macroeconomic Consequences of Unemployment Scarring](https://github.com/wdu9/JMP/blob/main/JMPDraft.pdf)
    + Bence Barosczy and Mateo Velasquez-Giraldo: [HANK Comes of Age](https://www.federalreserve.gov/econres/feds/hank-comes-of-age.htm)
    + In progress: [Welfare and Spending Effects of Consumption Stimulus Policies](https://llorracc.github.io/HAFiscal)


## But Wait, There's More: Indirect Inference

### Life Cycle Model (Gourinchas-Parker; Cagetti)

* [SolvingMicroDSOPs](https://github.com/econ-ark/SolvingMicroDSOPs) 

* With Bequests? (DeNardi)
  - [TRP Model Notebook](https://github.com/econ-ark/EstimatingMicroDSOPs/blob/main/src/notebooks/Model_Comparisons.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/econ-ark/EstimatingMicroDSOPs/HEAD?urlpath=https%3A%2F%2Fgithub.com%2Fecon-ark%2FEstimatingMicroDSOPs%2Fblob%2Fmain%2Fsrc%2Fnotebooks%2FModel_Comparisons.ipynb)


## But Wait, There's More: [REMARKS](https://github.com/econ-ark/REMARK/blob/main/README.md)

* An easy-to-use standard for guaranteed replicability
    + on any computer (Mac, Win, Linux) 
    + using any open-source language: Python, R, Julia, ...
    + [About 26 of them](https://econ-ark.org/materials/?select=REMARK)

* Builds on industry standards: Docker, cff, conda, pip, ...
  
* Aim:
    + Set a standard for journals
        - Now every journal has different requirements
    + Results should be replicable **on submission**
        - Editors, referees can "kick the tires"
        - Readers can easily stand on your giant shoulders
        - Central banks can exchange and compare models


## Where Are We Going? 'DYNARK':

* Model specification tools for **any** Bellman Problem [(mockup)](https://raw.githubusercontent.com/econ-ark/OverARK/refs/heads/master/Development/pablo/ModelOnlyBlockRework.yaml)
* Three layers:
    1. Abstract mathematical description
        - The symbolic version that appears in the text
        - Describes the "Platonic Ideal" of the model
        - What you would solve with $\infty$ computing power
    2. Numerical/approximation details
        - Metaparameters like \# of gridpoints for approx
        - Restrictions on ranges of parameters (e.g. 1 < CRRA < 10)
    3. Specify your claims:
        - Concrete assertion about results
        - "Model requires CRRA > 8 to match portfolio share"


## Why These Elements?

* 2 and 3 allow **AUTOMATIC** robustness testing
* For each approx:
    + does claim fail as gridpoints increase?
* For each restriction:
    + 'parameter sweep' of values in allowed ranges


## Underlying Motivation

### Tower of Babel problem

1. Lack of transparency: What exactly **is** your model?
    + Lots of buried assumptions: gridpoints, boundaries, dstns
2. Lack of replicability
    + Some notorious stories (only runs on Win 8.1 w/ Matlab 8.7.6.5)

### Causes:

* Everyone writes their own code
    + Often inherited from advisor
    + Barriers to entry
* Can take months just to get someone else's model working
    + Quicker to build on your own Byzantine legacy code
