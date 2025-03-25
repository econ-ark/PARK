---
title: "Econ-ARK: Open-Source Tools for Heterogeneous Agent Modeling"
subtitle: "Advancing Economic Research & Industry Applications"
author:
  - name: Alan Lujan
    orcid: 0000-0002-5289-7054
    email: alujan@jhu.edu
    affiliations:
      - Johns Hopkins University
      - Econ-ARK (Core Developer & Maintainer)
format:
  metropolis-revealjs
html-math-method:
  method: mathjax
  url: "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
date: March 25, 2025
date-format: "MMMM DD, YYYY"
footer: "https://econ-ark.org"
embed-resources: true
logo: econ-ark-logo.png

---

## Introduction & Motivation

- **[Econ-ARK](https://econ-ark.org/)** is an open-source toolkit for **heterogeneous agent modeling**.  

- Principal Investigator: **[Prof. Chris Carroll](https://www.econ2.jhu.edu/people/ccarroll/) (JHU)** --- known for groundbreaking work on **consumption** and the **Endogenous Grid Method (EGM)**.  
- Presenter: **[Alan Lujan, PhD](https://advanced.jhu.edu/directory/alan-lujan/) (JHU)** --- Core Developer & Maintainer of Econ-ARK.
- Fiscal Sponsor: [NumFOCUS](https://numfocus.org/) --- Corporate Sponsor: [T. Rowe Price](https://www.troweprice.com/en/us) (TRP)  

- **Goal**: Reduce coding overhead so economists, students, and policymakers, can focus on **economic insights** --- spanning **macro**, **micro**, and **policy** questions.



## Econ-ARK Overview


- **Vision**: Provide a unified platform for **modeling, simulating, and analyzing** heterogeneous individual behavior and its **aggregate implications**.
- **Open-Source**: Encourages transparency, reproducibility, and fosters a growing community.
- **Python-Based**: Leverages the scientific computing ecosystem (NumPy, SciPy, Pandas, etc.).
- **Modular & Extensible**: Easily adapt or extend existing models; share solutions across academia and industry.


## HARK: The Core Python Library

- **HARK (Heterogeneous Agents Resources and toolKit)**:
  - Offers **pre-built** agent models (e.g., consumption-saving, portfolio choice, **lifecycle**).
  - Implements an **object-oriented** approach for defining and simulating new agent types.
  - Based on and expands **Chris Carroll’s** pioneering methods (e.g., **EGM** for solving consumption problems).
- **REMARK (Replications and Explorations Made using ARK)**:
  - Bundled Jupyter notebooks, data, and instructions enable **replicable** research and teaching.
  - Ideal for sharing open research workflows.


## Key Academic Use Cases

- **Structural Modeling**: Rapid experimentation with established or novel frameworks (buffer-stock saving, consumption-savings models, etc.).
- **Heterogeneous Agent New Keynesian (HANK)**: Analyze policy experiments under rich micro-level heterogeneity.
- **Lifecycle Modeling**: Incorporate realistic income processes, demographics, retirement choices, and policy uncertainty.
- **Facilitating Cutting-Edge Research**: Focus on the economics rather than building modeling infrastructure from scratch.
- **Open Science**: Encourage collaboration and reproducibility.


## Key Industry Use Cases

- **Financial Services**: Personalized wealth management, retirement advice, and product design.
- **Risk Analytics**: Scenario analysis for insurance, mortgage, and consumer credit markets.
- **Policy Evaluation**: Model macro-level outcomes (e.g., consumption, default risk, wealth distribution) from heterogeneous micro-level behavior.
- **Rapid Prototyping**: Adapt academic-grade models to real-world data and scale them for commercial applications.
- **Forecasting**: Use macro models to predict future economic conditions and policy decisions.


## Example: Consumption-Saving over the Life Cycle

A **consumption-saving** model with persistent income shocks, where all variables are “normalized” (i.e., **divided by permanent income**).

$$
v_t(m_t) = \max_{c_t} \Bigl\{ u(c_t) + \beta \,\mathbb{E}_t \Bigl[(\Gamma_{t+1}\,\psi_{t+1})^{1-\rho}\,v_{t+1}(m_{t+1})\Bigr]\Bigr\}
$$

$$
m_{t+1} = \frac{R_{t+1}}{\Gamma_{t+1}\,\psi_{t+1}}\,(m_t - c_t) + \theta_{t+1}
$$

- **$m_t$**: normalized wealth  
- **$c_t$**: consumption choice  
- **$\Gamma_{t+1}, \psi_{t+1}, \theta_{t+1}$**: growth factors & shocks  
- **$R_{t+1}$**: risky return on savings


## Quick Demo

```python
from HARK.ConsumptionSaving.ConsIndShockModel import IndShockConsumerType

## This code defines, solves, and simulates a basic consumption-saving model

## Define parameters
params = {
    'CRRA': 2.0,
    'Rfree': 1.03,
    'DiscFac': 0.96,
    'PermShkStd': [0.1],
    'TranShkStd': [0.1],
    'cycles': 0  ## Infinite horizon for demo
}

## Create and solve the consumer instance
consumer = IndShockConsumerType(**params)
consumer.solve()
consumer.simulate(50) ## Simulate 50 periods

```

- **Takeaway**: HARK handles much of the infrastructure for defining, solving, and simulating agent-based models.


## Open Science & Community

- **REMARKs (Replications and Explorations Made using ARK)**:
  - Integrated notebooks, datasets, instructions for fully reproducible projects.
- **Get Involved**:
  - Contribute ideas, report issues, or submit pull requests on [GitHub](https://github.com/econ-ark/HARK).
  - Build and share new models or improvements with a global community.
- **Events & Collaboration**:
  - Community calls, workshops, and conferences to discuss use cases and best practices.



## Key Takeaways

1. **Econ-ARK** accelerates the development of **heterogeneous agent models** for research and industry.
2. **HARK** integrates **Chris Carroll’s** EGM approach and supports structural modeling, including **HANK** and **lifecycle** frameworks.
3. **Open-source** fosters transparency, reproducibility, and an engaged community.

 We're always looking for collaborators, partners, and additional corporate sponsors for advanced modeling and applications!

- **Website**: [econ-ark.org](https://econ-ark.org)  
- **Repository**: [github.com/econ-ark/HARK](https://github.com/econ-ark/HARK)  
- **Contact**: Alan Lujan ([alujan@jhu.edu](mailto:alujan@jhu.edu)) – Core Developer & Maintainer  
