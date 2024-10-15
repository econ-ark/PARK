---
title: "Econ-ARK for Central Banks"
author: "Christopher D. Carroll"
format:
    revealjs:
        smaller: true
        scrollable: true
---

# Econ-ARK for Central Banks

Presentation at Sveriges Riksbank

2024-10


Christopher Carroll

Johns Hopkins University 

[Powered By Econ-ARK](link to button)

## Microfoundations in a Nutshell

### Prehistory

* Modigliani and Brumberg (1954), Friedman (1957), Diamond (1964)
* Perfect Foresight models: 1960s-70s
	
### Bewley (1977)

* Formalization of Friedman PIH
* Rigorous treatment of uncertainty, liq constr
* Entirely qualitative/analytical

### Early 1990s: Numerical computation of SS dist'n of wealth

* Life Cycle/OLG:
    + Zeldes (1989); Hubbard, Skinner, and Zeldes (1994, 1995);
    + Huggett (1996); Carroll (1997)
* Infinite Horizon
    + Deaton (1991); Carroll (1992); Aiyagari (1994)
* Aggregate _dynamics_? Hopeless:
    + requires predicting evolution of entire **distribution**

## Dynamics

### Krusell-Smith (1998): <!-- somebody add link to our KS replication -->

* _mean_ of distribution $\bar{k}$ is good enough!
* still excruciatingly slow

### Reiter (2010):

* SS Micro and Dyn Macro _can be solved independently_
    + _Why_? Idiosyncratic shocks 100x larger than agg
    + So agg shocks cause 'small' perturbation of dstn
* $\Rightarrow$ Reiter Singularity: 2014-2018
    + Culmination: "Sequence Space Jacobian" Toolkit: <!-- link -->
    + Bring us your micro SS ...
        - With Jacobians wrt PF aggregate shocks
        - ...We'll give you the dynamic macro

## Where Does Econ-ARK Fit in this Narrative?

### Rich Set of Tools for SS Micro ...

<!-- Somebody please make links to relevant docs or REMARKs or DemARKs -->
* [Consumption/Saving](link me)
* [Portfolio Choice](link me)
* [Liquid and Illiquid Assets](link me)
* [Discrete-Continuous Problems](link me)
    + [DCEGM](link me)
* [Labor Supply](link me)
    + [Keane and Imai](link me)
* [Medical Expense Risk](link me)
* [Life Cycle Modeling](link me)
    + [Solutions](link me)
    + [Datasets](All the SCFs, with tools)
* Sophisticated Liquidity Constraints
    + [Higher rate for borrowing vs saving](link me)
    + [withdrawal penalties for retirement saving](Mateo VG JMP)
* etc etc

## ... Easy to Connect to SSJ toolkit

1. Econ-ARK/HARK:
   1. solve for micro steady state
   1. Compute Jacobians 
1. Feed results to SSJ toolkit

* Documentation Notebooks
    + (links to all three of our SSJ documentation notebooks)

<!-- Here I will divert to a live demo of the notebook Akshay is working on -->

* Papers:
    + Will Du: JMP
        [HANK with Scarring](link me)
    + Bence Barosczy and Mateo Velasquez-Giraldo:
	- "HANK Comes of Age"
    + In progress:
	- [Welfare and Spending Effects of Consumption Stimulus Policies](https://llorracc.github.io/HAFiscal)

## But Wait, There's More: Indirect Inference (MSM)

### Life Cycle Model (Gourinchas-Parker; Cagetti)

- [SolvingMicroDSOPs-Estimation](link me)

- With Bequests? (DeNardi)
  - [TRP Model Notebook](link me)

### REMARKs

- An easy-to-use standard for guaranteed replicability
  - on any computer (Mac, Win, Linux) 
  - using any open-source language
	- python, R, julia, ...
  - [About 26](https://econ-ark.org/materials)

- Builds on industry standards
  - Docker
  - cff
  - conda 
  - pip
  
- Aim:
  - Set a standard for journals
	- Now every journal has different requirements
  - Results should be replicable _on submission_
	- Editors, referees can 'kick the tires'
	- Readers can easily stand on your giant shoulders
	- Central Banks can exchange and compare models

### Where Are We Going?

'DYNARK': 
- Model specification tools for ANY Bellman Problem
- [mockup](link me to latest pseudocode)

Three layers:
1. Abstract mathematical description
  - The symbolic version that appears in the text
  - Describes the 'Platonic Ideal' of the model
  - What you would solve with $\infty$ computing power
2. Numerical/Approximation Details
   - Metaparameters like \# of gridpoints for approx
   - Restrictions on ranges of parameters:
	 - 1 < CRRA < 10
	 - 0.00 < DiscFac < 1.00
	 - 0.05 < $\sigma$ < 0.20
3. Specify Your Claims:
   - Concrete assertion about results:
   - 'Model requires CRRA > 8 to match portfolio share'
   
## Why These Elements?

(2) and (3) allow AUTOMATIC robustness testing
- For each approx
  - does claim fail as gridpoints increase?
- For each restriction
  - 'parameter sweep' of values in allowed ranges

## Underlying Motivation: Tower of Babel problem

1. Lack of transparency
	- What exactly _is_ your model?
	- Lots of buried assumptions
		- Gridpoints, boundaries, distributions
2. Lack of replicability
	- Some notorious stories 
	- Only runs on Win 8.1 w Matlab 8.7.6.5 etc etc
	
Causes:
	- Everyone writes their own code
		- Often inherited from advisor
		- Barriers to entry
	- Can take months just to get someone else's model working
		- quicker to build on your own Byzantine legacy code

