---
title: 'The Heterogeneous-Agent Resources toolKit (HARK): An Extensible Framework for
  Solving and Estimating Heterogeneous-Agent Economic Models'
author: 
  - Christopher D. Carroll
  - Alexander M. Kaufman
  - Jacqueline Kazil
  - David C. Low
  - Nathan M. Palmer
  - Matthew N. White
date: "July 9, 2018"
documentclass: article
classoption: 
  - twocolumn
  - 10pt
output: 
    pdf_document:
        number_sections: true
        keep_tex: yes
bibliography: bibfile.bib
link-citations: yes             
geometry: margin=0.68in
header-includes:
  - \usepackage{cancel}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \usepackage[round]{natbib}
abstract: |
  We present initial work on a modular and extensible toolkit for solving and estimating heterogeneous-agent partial- and general-equilibrium models. Heterogeneous-agent models have grown increasingly valuable for both policy and research purposes, but code to solve such models can be difficult to penetrate for researchers new to the topic. As a result it may take years of human capital development for researchers to become proficient in these methods and contribute to the literature. The goal of the HARK toolkit is to ease this burden by providing an extensible framework in which a few common models are solved, and clear documentation, testing, and estimation examples provide guidance for new researchers to develop their own work in a robust and replicable manner. We outline key elements of the HARK framework, including the API, structure, and illustrate with two examples.
---

\
\centerline{JEL codes E21, C61, E63}


# Introduction

The Heterogeneous-Agent Resources toolKit (HARK) is a modular programming 
framework for solving and estimating macroeconomic and macro-financial models in 
which economic agents can be heterogeneous in a large number of ways. Models 
with extensive heterogeneity among agents can be extremely useful for policy and 
research purposes. For example, @carroll2012implications, @carroll2014representing, 
@carroll2014imfheterogeneousagentmacro,
and @carroll2017distribution demonstrate how aggregate consumption and 
output can be heavily influenced by 
heterogeneity. @geanakoplos2010leverage outlines how heterogeneity drives the 
leverage cycle, and @geanakoplos2012getting applies these insights to 
large-scale model of the housing and mortgage markets. However the most commonly 
published macroeconomic and macro-finance models have very limited heterogeneity 
or none at all (this includes the large class of representative agent models), 
in large part because these are the only models that can be easily solved with 
existing toolkits.^[Dynare is the most popular toolkit for representative-agent 
models. For more details see @adjemian2011dynare.] In contrast, models with 
extensive heterogeneity among agents have no central toolkit and must be solved 
in a bespoke way. This requires a significant investment of time and human 
capital before a researcher can produce publishable or usable work. This results 
in needless code duplication, increasing the chance for error and wasting 
valuable research time.

The HARK project addresses these concerns by providing a set of well-documented 
code modules that can be composed together to solve a range of 
heterogeneous-agent models. Methodological advances in the computational 
literature allow many types of models to be solved using similar  approaches -- 
the HARK project simply brings these together in one place. The key is 
identifying methodologies that are both "modular" (in a sense to be described 
below) as well as robust to model misspecification. These include both solution 
methods as well as estimation methods.

In addition to these methodological advances, the HARK project adopts modern 
practices from the field of software development to ease the burden of code 
review, code sharing,  and programming collaboration for researchers dealing in 
computational methods. Researchers who must review the scientific and technical 
code written by others are keenly aware that the time required to review and 
understand another's code can easily dwarf the time required to simply re-write 
the code from scratch (conditional on understanding the underlying concepts). 
This can be particularly important when multiple researchers may need to work on 
parts of the same codebase, either across time or distance. This problem is not 
confined to scientific computing alone. Fortunately the software development 
community, and particularly the open-source community, has spent decades perfecting 
tools for programmers to quickly consume and understand code written by others, 
verify that it is correct, and proceed to contribute back to a large and diverse 
codebase without fear of introducing bugs. The tools used by these professional 
developers include formal code documentation, unit testing structures, modern 
versioning systems for automatically tracking changes to code and content, and  
low-cost systems of communicating ideas, such as interactive programming notebooks 
that combine formatted mathematics with executable code and descriptive content. 
These tools often operate in concert with one another, forming a powerful 
infrastructure that can greatly accelerate project development for both individuals 
and collaborative teams. These technical tools are not new -- the HARK project 
simply aims to apply the best of them to scientific code in a structured way to 
increase researcher productivity, particularly when interacting with other 
researchers' code.

[](TODO: Insert literature review of software development practices as well as the baseline models employed.)

The project presented here is not an attempt to create new methodology either on 
the software development front or the research front (although we expect new 
methodological contributions to emerge from the effort). Rather the HARK project 
brings together many well-understood and proven methodologies to bear in an easily 
used and extended toolkit. The rest of this paper will first outline the useful 
concepts we adopt from software development, with examples of each, and then 
demonstrate how these concepts are applied in turn to the key solution and 
estimation methods required to solve general heterogeneous-agent models.

The sections are organized as follows: \mbox{Section \ref{sec:hark-structure}} 
discusses the natural modular structure of the types of problems HARK solves and 
overviews the code structure that implements these solutions. \mbox{Section \ref{sec:tool-modules} }
outlines details of the core code modules used by HARK. \mbox{Section \ref{sec:model-modules}} 
outlines two example models that illustrate models in the HARK framework. 
\mbox{Section \ref{sec:tools-from-software-development}} outlines key tools from 
professional software development and how these are used in HARK, and 
\mbox{Section \ref{sec:summary-conclusion}} summarizes and concludes.

## An Aside on Speed

Python is an interpreted scripting language and at inception was many hundreds or 
thousands of times slower than compiled languages such as C++. As the scientific 
community adopts Python, a number of projects have emerged that allow Python to 
be compiled. At the time of this writing, there are a number of options for 
accelerating Python code. This is reflected in @aruoba2015comparison, 
specifically their Table 1. The authors compares a number of programming languages 
against C++ for a loop-intensive task. When sorted by relative time against the 
fastest C++ implementation, Python occupies the fastest two spots that are not 
other C++ or FORTRAN.^[The first five spots in the relative ranking are occupied 
by different compiler implementations of C++ and FORTRAN. The 6th and 7th ranks 
are occupied by two of the most popular Python compilers, Cython and Numba, 
respectively, which are 1.41 and 1.65 times slower than the fastest C++ 
implementation. Notably, two C++ implementations are 1.38 times slower than the 
fastest, and one of the two FORTRAN implementations is 1.30 times slower than 
the fastest C++ implementation. That is, the fastest Python implementation is 
only about 3% slower than two of the three C++ implementations.] This is not a 
definitive illustration of the speed capabilities of Python, as there are many 
caveats that must be considered in the problem setup and execution (as noted by 
the authors themselves). However it does serve to illustrate that Python is 
capable of very high speeds when compiled. Furthermore, even aside from 
compilation, when Python is vectorized using the major numerical libraries, 
NumPy and SciPy, all vectorized calculations are executed in optimized, compiled 
C and FORTRAN.^[Note that if the speed advantage of the individual function 
comes from vectorization versus compilation, the most gain may actually be 
achieved by simply copy-and-pasting the function contents into the class method. 
See @sheppard2018introduction, Chapter 24, for an excellent overview of Python performance 
and code optimization.] 



# HARK Structure \label{sec:hark-structure}
[](Methodological Framework ... of the HARK Framework)


The type of theoretical economic problem that HARK solves is extremely modular by 
construction. There are approximately these steps in creating a heterogneous-agents 
rational model:


1. Write down individual agent problem
2. Solve the individual agent problem
3. For general equilibrium, also solve for aggregate interations and beliefs
4. Estimate the model using Simulated Method of Moments (SMM)

Under the solution and estimation method used by HARK, each of these steps is 
highly modular. The structure of the solution method suggests a natural division 
of the code. The rest of this section outlines the code structure HARK employs, 
and the next section outlines the theory behind these models.

HARK is written in Python, an object-oriented programming (OOP) language that
has experienced increasing popularity in the scientific community in the past
several years. A significant reason for the adoption of Python is the `numpy`
and `scipy` packages, which offer a wide array of mathematical and statistical
functions and tools; HARK makes liberal use of these libraries. Python's
object-oriented nature allows models in HARK to be easily extended: more complex 
models can inherit functions and methods from more fundamental "parent" models, 
eliminating the need to reproduce or repurpose code.

For users unfamiliar with OOP, we strongly encourage you to review the
background material on OOP provided by the good people at [QuantEcon](http
://quant-econ.net/) at this link: [Object
Oriented Programming](http://quant-econ.net/py/python_oop.html). Unlike non-
OOP languages, OOP bundles together data and functions into objects. These can
be accessed via: `object_name.data` and `object_name.method_name()`, respectively.
For organizational purposes, definitions of multiple objects are stored in
modules, which are simply files with a .py extension. Modules can be accessed
in Python via:


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{.python}
import module_name as import_name  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This imports the module and gives it a local name of `import_name`. We can
access a function within this module by simply typing:
`import_name.function_name()`. The following example will illustrate the usage
of these commands. `CRRAutility` is the function object for calculating CRRA
utility supplied by `HARKutilities` module. `CRRAutility` is called attributes 
of the module `HARKutilities`. In order to calculate CRRA utility with a
consumption of 1 and a coefficient of risk aversion of 2 we run:  


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{.python}
import HARKutilities as Hutil

Hutil.CRRAutility(1,2)  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python modules in HARK can generally be categorized into three types: tools,
models, and applications. **Tool modules** contain functions and classes with
general purpose tools that have no inherent "economic content", but that can
be used in many economic models as building blocks or utilities; they could
plausibly be useful in non-economic settings. Tools might include functions
for data analysis (e.g. calculating Lorenz shares from data, or constructing a
non-parametric kernel regression), functions to create and manipulate discrete
approximations to continuous distributions, or classes for constructing
interpolated approximations to non-parametric functions. Tool modules
generally reside in HARK's root directory and have names like `HARKsimulation`
and `HARKinterpolation`; they do not necessarily do anything when run. The core
functionality of HARK is encored in the tools modules; these will be discussed in 
detail in the following section. 

**Model modules** specify particular economic models, including classes to
represent agents in the model (and the "market structure" in which they
interact) and functions for solving the "one period problem" of those models.
For example, `ConsIndShockModel.py` concerns consumption-saving models in which
agents have CRRA utility over consumption and face idiosyncratic shocks to
permanent and transitory income. The module includes classes for representing
"types" of consumers, along with functions for solving (several flavors of)
the one period consumption-saving problem. When run, model modules might
demonstrate example specifications of their models, filling in the model
parameters with arbitrary values. When `ConsIndShockModel.py` is run, it
specifies an infinite horizon consumer with a particular discount factor,
permanent income growth rate, coefficient of relative risk aversion (etc), who
faces lognormal shocks to permanent and transitory income each period with a
particular standard deviation; it then solves this consumer's problem and
graphically displays the results.^[Running `ConsIndShockModel.py` also 
demonstrates other variations of the consumption-saving problem, but their
description is omitted here for brevity.] Model modules generally have 
`Model` in their name. The two examples discussed in the "microeconomic" and
"macroeconomic" sections below come from "Model modules."

**Application modules** use tool and model modules to solve, simulate, and/or
estimate economic models *for a particular purpose*. While tool modules have no
particular economic content and model modules describe entire classes of
economic models, applications are uses of a model for some research purpose.
For example, `/SolvingMicroDSOPs/StructEstimation.py` uses a consumption-saving
model from `ConsIndShockModel.py`, calibrating it with age-dependent sequences
of permanent income growth, survival probabilities, and the standard deviation
of income shocks (etc); it then estimates the coefficient of relative risk
aversio n and shifter for an age-varying sequence of discount factors that best
fits simulated wealth profiles to empirical data from the Survey of Consumer
Finance. A particular application might have multiple modules associated with
it, all of which generally reside in one directory. Particular application 
modules will not be discussed in this paper further; please see the Github page
and associated documentation for references to the application modules. 


# Tool Modules \label{sec:tool-modules}


HARK's root directory contains the following tool modules, each containing a 
variety of functions and classes that can be used in many economic models, or 
even for mathematical purposes that  have nothing to do with economics. We expect 
that all of these modules will grow considerably in the near future, as new 
tools are "low hanging fruit" for contribution to the project.

## HARKcore

As the name suggests, this modules contains core classes used by the rest of the 
HARK ecosystem. A key goal of the project is to create modularity and interoperability 
between models, making them easy to combine, adapt, and extend. To this end, the
`HARKcore` module specifies a framework for economic models in HARK, creating a
common structure for them on two levels that can be called "microeconomic" and
"macroeconomic", which are described in detail in the next section. 

Beyond the model frameworks, `HARKcore` also defines a "supersuperclass" called
`HARKobject`. When solving a dynamic economic model, it is often required
to consider whether two solutions are sufficiently close to each other to
warrant stopping the process (i.e. approximate convergence). HARK specifies
that classes should have a `distance` method that takes a single input and
returns a non-negative value representing the (generally dimensionless)
distance between the object in question and the input to the method. As a
convenient default, `HARKobject` provides a "universal distance metric" that
should be useful in many contexts.^[Roughly speaking, the universal distance 
metric is a recursive supnorm, returning the largest distance between two
instances, among attributes named in `distance_criteria`. Those attributes 
might be complex objects themselves rather than real numbers, generating a 
recursive call to the universal distance metric.] When defining a
new subclass of `HARKobject`, the user simply defines the attribute
distance_criteria as a list of strings naming the attributes of the class that
should be compared when calculating the distance between two instances of that
class. See [here](https://econ-
ark.github.io/HARK/generated/HARKcore.html) for online documentation.

## HARKutilities


The `HARKutilities` module carries a double meaning in its name, as it contains
both utility functions (and their derivatives, inverses, and combinations
thereof) in the economic modeling sense as well as utilities in the sense of
general tools. Utility functions include constant relative risk aversion (CRRA) 
and  constant absolute risk aversion (CARA). Other functions in `HARKutilities` 
include data manipulation tools, functions for constructing discrete state space 
grids,  and basic plotting tools. The module also includes functions for 
constructing discrete approximations to continuous distributions as well as 
manipulating these representations. 


## HARKinterpolation


The `HARKinterpolation` module defines classes for representing interpolated
function approximations. Interpolation methods in HARK all inherit from a
superclass such as `HARKinterpolator1D` or `HARKinterpolator2D`, wrapper classes 
that ensures interoperability across interpolation methods. Each interpolator 
class in HARK must define a `distance` method that takes as an input another 
instance of the same class and returns a non-negative real number representing 
the "distance" between the two.^[Interpolation methods 
currently implemented in HARK include (multi)linear interpolation up to 4D, 1D 
cubic spline interpolation, 2D curvilinear interpolation over irregular grids, a
1D "lower envelope" interpolator, and others.]


**HARKsimulation**


The HARKsimulation module provides tools for generating simulated data or
shocks for post-solution use of models. Currently implemented distributions
include normal, lognormal, Weibull (including exponential), uniform,
Bernoulli, and discrete. 


**HARKestimation**

Methods for optimizing an objective function for the purposes of estimating a
model can be found in `HARKestimation`. As of this writing, the implementation
includes minimization by the Nelder-Mead simplex method, minimization by a 
derivative-free Powell method variant, and two tools for resampling data (i.e. 
for a bootstrap). Future functionality will include global search methods, 
including genetic algorithms, simulated annealing, and differential evolution. 


**HARKparallel**

By default, processes in Python are single-threaded, using only a single CPU
core. The HARKparallel module provides basic tools for using multiple CPU
cores simultaneously, with minimal effort.^[`HARKparallel` uses two packages 
that aren???t currently included in the default distribution of Anaconda: `joblib`
and  `dill`. They can be installed with `conda`.] The module also has functions
for a parallel implementation of the Nelder-Mead simplex algorithm, as
described in Wiswall and Lee (2011).


# Model Modules \label{sec:model-modules}

*Microeconomic* models in HARK use the `AgentType` class to represent agents with
an intertemporal optimization problem. Each of these models specifies a
subclass of `AgentType`; an instance of the subclass represents agents who are
ex-ante homogeneous (they have common values for all parameters that describe
the problem, such as risk aversion). The `AgentType` class has a `solve` method 
that acts as a "universal microeconomic solver" for any properly formatted model,
making it easier to set up a new model and to combine elements from different models; 
the solver is intended to encompass any model that can be framed as a sequence of one
period problems.^[See @carroll2017harkmanual for a much more thorough discussion.]


*Macroeconomic* models in HARK use the `Market` class to represent a market or 
other mechanisms by which agents interactions are aggregated to produce 
"macro-level" outcomes. For example, the market in a consumption-saving
model might combine the individual asset holdings of all agents in the market
to generate aggregate savings and capital in the economy, which in turn 
produces the interest rate that agents care about. Agents then learn
the aggregate capital level and interest rate, which affects their future actions.
Thus objects that *microeconomic* agents treat as exogenous when solving their 
individual-level problems (such as the interest rate) are made *endogenous* at 
at the macroeconomic level through the `Market` aggregator. Like `AgentType`, 
the `Market` class also has a `solve` method, which seeks out a dynamic general 
equilibrium rule governing the dynamic evolution of the macroeconomic object.^[See 
@carroll2017harkmanual for a much more thorough discussion.]


Each of these are explored via example in the following.


##  Microeconomics: the AgentType Class

The core of our microeconomic dynamic optimization framework is a flexible
object-oriented representation of economic agents. The `HARKcore` module defines
a superclass called `AgentType`; each model defines a subclass of `AgentType`,
specifying additional model-specific features and methods while inheriting the
methods of the superclass. Most importantly, the method `solve` acts as a
"universal solver" applicable to any (properly formatted) discrete time model.
This section provides a brief example of a problem solved by a microeconomic 
instance of `AgentType`.^[For a much more detailed discussion please see Carroll 
et al. (2017).]

### Sample Model: Perfect Foresight Consumption-Saving

To provide a concrete example of how the AgentType class works, consider the
very simple case of a perfect foresight consumption-saving model. The agent
has time-separable, additive CRRA preferences over consumption $C_t$, discounting
future utility at a constant rate; he receives a particular stream of labor
income each period $Y_t$, and knows the interest rate $\mathsf{R}$ on assets 
$A_t$ that he holds from one period to the next. His decision about how much 
to consume in a particular period $C_t$ out of total market resources $M_t$ 
can be expressed in Bellman form as:

$$
\begin{aligned}
V_t(M_t) &= \max_{C_t} \; \mathrm{u}(C_t)  + \beta  \cancel{\mathsf{D}}_t E [V_{t+1}(M_{t+1}) ], \\
A_t &= M_t - C_t, \\
M_{t+1} &= \mathsf{R} A_t + Y_{t+1}, \\
Y_{t+1} &= \Gamma_{t+1} Y_t, \\
\mathrm{u}(C) &= \frac{C^{1-\rho}}{1-\rho}.
\end{aligned}
$$

An agent's problem is thus characterized by values of $\rho$, $\mathsf{R}$, and 
$\beta$, plus sequences of survival probabilities $\cancel{\mathsf{D}}_t$ and
income growth factors $\Gamma_t$ for $t = 0, ... ,T$. This problem has an 
analytical solution for both the value function and the consumption function.

The `ConsIndShockModel` module defines the class `PerfForesightConsumerType` as a
subclass of `AgentType` and provides `solver` functions for several variations of
a consumption-saving model, including the perfect foresight problem. A HARK user 
could specify and solve a ten period perfect foresight model with the following 
two commands (the first command is split over multiple lines) :

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{.python}
MyConsumer = PerfForesightConsumerType(
    time_flow=True, cycles=1, Nagents = 1000,
    CRRA = 2.7, Rfree = 1.03, DiscFac = 0.98,
    LivPrb = [0.99,0.98,0.97,0.96,0.95,0.94,0.93,
              0.92,0.91,0.90],
    PermGroFac = [1.01,1.01,1.01,1.01,1.01,1.02,
                  1.02,1.02,1.02,1.02] )

MyConsumer.solve()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first line makes a new instance of ConsumerType,
specifies that time is currently "flowing" forward, specfies that the sequence 
of periods happens exactly once, and that the simulation-based solution will use 
1,000 agents. The next five lines (all part of the same command) set the time 
invariant (CRRA is $\rho$, Rfree is $\mathsf{R}$, and DiscFac is $\beta$) and time 
varying parameters (LivPrb is $\cancel{\mathsf{D}}_t$, PermGroFac is $\Gamma_{t}$). 
After running the `solve method`, `MyConsumer` will have an attribute called 
`solution`, which will be a list with eleven `ConsumerSolution` objects, 
representing the period-by-period solution to the model.^[The solution to a 
dynamic optimal control problem is a set of policy functions and a value functions,
one for each period. The policy function for this consumption-savings problem is
how much to consume $C_t$ for a given amount of market resources $M_t$.]

The consumption function for a perfect foresight consumer is a linear function of 
market resources -- not terribly exciting. The marginal propensity to consume out
of wealth doesn't change whether theconsumer is rich or poor. When facing *uncertain* 
income, however, the consumption function is concave -- the marginal propensity to 
consume is very high when agents are poor, and lower when they are rich. In addition, 
agents facing uncertainty save more than agents under certainty. However as agents 
facing uncertainty get richer, their consumption function converges to the perfect 
foresight consumption function -- rich but uncertain agents act like agents who 
have certainty. In \mbox{Figure \ref{fig:consumption-functions}}, the solid blue 
line is consumption under certainty, while the dashed orange line is consumption 
under uncertainty. The inset plot demonstrates that these two functions converge
as the x-axis of this plot are extended.


![Consumption Functions\label{fig:consumption-functions}](./consumption_functions.png)

## Macroeconomics: the Market Class

The modeling framework of `AgentType` is called "microeconomic" because it
pertains only to the dynamic optimization problem of individual agents, treating 
all inputs of the problem from their environment as exogenously fixed. In what 
we label as "macroeconomic" models, some of the inputs for the microeconomic
models are endogenously determined by the collective states and choices of 
other agents in the model. In a rational dynamic general equilibrium, there must
be consistency between agents' beliefs about these macroeconomic objects, their 
individual behavior, and the realizations of the macroeconomic objects that 
result from individual choices.

The Market class in `HARKcore` provides a framework for such macroeconomic
models, with a `solve` method that searches for a rational dynamic general 
equilibrium. An instance of `Market` includes a list of `AgentTypes` that compose 
the economy, a method for transforming microeconomic outcomes (states, controls, 
and/or shocks) into macroeconomic outcomes, and a method for interpreting a history
or sequence of macroeconomic outcomes into a new "dynamic rule" for agents to
believe. Agents treat the dynamic rule as an input to their microeconomic
problem, conditioning their optimal policy functions on it. A dynamic general
equilibrium is a fixed point dynamic rule: when agents act optimally while
believing the equilibrium rule, their individual actions generate a
macroeconomic history consistent with the equilibrium rule.

###  Down on the Farm

The `Market` class uses a farming metaphor to conceptualize the process for
generating a history of macroeconomic outcomes in a model. Suppose all
`AgentTypes` in the economy believe in some dynamic rule (i.e. the rule is
stored as attributes of each `AgentType`, which directly or indirectly enters
their dynamic optimization problem), and that they have each found the
solution to their microeconomic model using their `solve` method. Further, the
macroeconomic and microeconomic states have been reset to some initial
orientation.

To generate a history of macroeconomic outcomes, the `Market` repeatedly loops
over the following steps a set number of times:

1. `sow`: Distribute the macroeconomic state variables to all `AgentTypes` in the market. 
2. `cultivate`: Each `AgentType` executes their `marketAction` method, likely corresponding to simulating one period of the microeconomic model. 
3. `reap`: Microeconomic outcomes are gathered from each `AgentType` in the market. 
4. `mill`: Data gathered by `reap` is processed into new macroeconomic states according to some "aggregate market process". 
5. `store`: Relevant macroeconomic states are added to a running history of outcomes.

This procedure is conducted by the `makeHistory` method of `Market` as a
subroutine of its `solve` method. After making histories of the relevant
macroeconomic variables, the market then executes its `calcDynamics` function
with the macroeconomic history as inputs, generating a new dynamic rule to
distribute to the `AgentTypes` in the market. The process then begins again,
with the agents solving their updated microeconomic models given the new
dynamic rule; the `solve` loop continues until the "distance" between successive
dynamic rules is sufficiently small.

### Sample Model: Fashion Victim


We illustrate the `Market` class with a summary of an example from the full 
[HARK manual](https://github.com/econ-ark/HARK/blob/master/Documentation/HARKmanual.pdf).
To illustrate the `Market` class consider a simple example in the emerging economic 
sub-field of aesthemetrics, the `FashionVictimModel`. This model is inspired by 
the paper ["The hipster effect: When anticonformists all look the same" by Jonathan Touboul](https://arxiv.org/abs/1410.8001v1).^[The [HARK manual](https://github.com/econ-ark/HARK/blob/master/Documentation/HARKmanual.pdf)
outlines the full problem and solution method in much more detail than the summary 
provided here. For a more traditional macroeconomic model, the `ConsAggShocksModel` 
module includes a consumption-saving model with both idiosyncratic and aggregate 
shocks, in which individual asset holdings are aggregated into total productive 
capital, endogenizing the interest and wage rate.] 

Each period, fashion victims make a binary choice of style $s$: to dress as a 
jock (0) or punk (1).  They receive utility directly from the outfit they wear 
and as a function of the proportion of the population who *just wore* the same 
style; they also pay switching costs ($c_{pj}$,$c_{jp}$) if they change styles 
rather than keep the same as the previous period.

The search for a dynamic general equilibrium is implemented in HARK's `Market`
class. The `marketAction` method of `FashionVictimType` simulates one period of 
the microeconomic model: each agent receives style preference shocks $\eta_0$ 
and $\eta_1$, sees the current proportion of punks $p_t$ (sown to them as `pNow`), 
and chooses which style to wear.

When the `solve` method is run, the solver successively solves each agent's 
microeconomic problem conditional on their beliefs about the next periods, 
runs the `makeHistory` method to generate a 1000 period history of $p_t$, and 
calculates a new punk belief rule based on this history. This entire process is 
repeated until the solver terminates when consecutive belief rules differ by 
less than 0.01 in any dimension. \mbox{Figure \ref{fig:fraction-of-punks}} shows
the fraction of punks in the population over time after the model is solved.^[Smoothed 
with 25-period moving average.]

![Fraction of Punks in Population over Time\label{fig:fraction-of-punks}](./fraction_of_punks.png)



# Tools from Software Development \label{sec:tools-from-software-development}

One of the most striking practices to emerge from the history of software 
development is the open open-source software moement: the decentralized 
collaboration of many independent programmers on a single project, often with 
little or no immediate monetary reward. Along with fascinating theoretical 
questions about incentive structures, the open-source movement has spurred the 
development of a wide array of excellent utilities that make decentralized code 
development robust and efficient. This section briefly overviews a number of tools
from traditional and open-source software development that enable collabortion 
between researchers in many places. 

## Documentation

Good documentation is the key to communication between two programmers, whether 
between two distinct individuals or with oneself over time. In Python, as in 
many scripting languages, strings written on the first line after a function 
declaration are automatically employed as system documentation. HARK currently 
uses a slight variation on the [PEP 257](https://www.python.org/dev/peps/pep-0257/)
style guide. 

In addition to traditional code documentation described above, notebook-style 
interfaces similar to those in Mathematica and Maple allow scientific programmers 
to directly communicate math ideas, and code in a single place. The HARK project 
uses [Jupyter](https://jupyter.org/), a language-agnostic, browser-based notebook 
system spun off of the the IPython project. 

## Unit Testing

Many programs are composed of a number of small functions that accomplish 
specific tasks. Testing at the individual function level is key to ensuring that 
the overall program executes correctly. This is all the more important for 
scientific computing, where a mistake deep in the code (eg. with a numerical 
approximation) may be extremely difficult to track down. Unit testing is the 
formal practice whereby each individual function is directly bundled with a set 
of tests. In scientific programming, this can serve an additional purpose: peer 
review of code. Uncovering bugs in code, even one's own code, can be notoriously 
difficult. This is many times more true when one is examining the code written 
by another. 

Unit testing can ease the burden of scientific code review in at least two ways. 
First, it can aid documentation in immediately outlining simple examples of code 
execution. Second, it can outline the pitfalls and testing procedures a reviewer 
may want to undertake to ensure that the code is correct. Instead of starting 
with a "blank page," a reviewer can take the unit tests written by the original 
author, run them, and then (assuming they all pass), examine the tests to see if 
any particular cases appear to be excluded. If so, the reviewer can use the unit 
tests as a template to quickly write another test case and run that as well. 
This can greatly accelerate both the verification of work done, as well as new 
testing of the code, all in a well-established and minimally costly framework.

In Python there are two built-in ways to write tests for a function: internally 
to the documentation, in a "[doctest](https://docs.python.org/2/library/doctest.html)," 
and externally in a more formal unit testing framework, 
"[unittest](https://docs.python.org/2/library/unittest.html)." HARK employs both 
where appropriate. 


## Application Programming Interface (API)

When contributing a module or a function to a larger code library, a programmer 
needs to know how this function or module fits into the overall framework of the 
codebase. Any large computational project with multiple developers can benefit 
from an Application Programming Interface (API). This is simply another form of 
language documentation, but one that is aimed at programmers for extending or 
using a codebase. 

The HARK project forms an API for the codebase organized around the modules 
required to run a partial-equilibrium or general-equilibrium estimation. 
Specifically, the simple API employed by the HARK defined by the main functions 
and data structures employed in the Estimation module, which is displayed and 
discussed in greater detail below. To extend the HARK library the user must 
replace or otherwise replicate these main functions in the Estimation module.^[A further use of APIs is to define an interface between a programming language and a particular dataset. This second use of APIs is just as important as its usage in organizing code. Organizations such as the [Open Economics Working Group](http://openeconomics.net/) may provide a unified approach for public economic datasets, but this is not part of HARK yet.]


## Version Control

An essential tool in distributed software development is a system that can automatically archive versions of code, as well as allow the merging of changes to a document by two different programmers. Such a system is known as a version control system. The HARK project uses the Git version control system, and uses the popular online repository service Github to archive its codebase. @chacon2014pro is an excellent overview of version control in general and Git and Github in particular. ]


## Bringing It Together: Reproducible Research

Many of the tools above are used to create research that can be immediately reproduced, even entirely in a web browser. This [gallery of interesting IPython Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks) outlines a number of research projects that combine code, discussion, data visualization, and descriptive mathematics to make science as transparent and reproducible as possible. For example @ram2015probability reproduce a section of their work in an IPython notebook, which can be found [here](http://nbviewer.ipython.org/url/www.sciencedirect.com/science/MiamiMultiMediaURL/1-s2.0-S0040580914000811/1-s2.0-S0040580914000811-mmc1.txt/272364/FULL/S0040580914000811/471cf02085a52c248dc76ae65ad4409d/mmc1.txt). 


# Summary and Conclusion \label{sec:summary-conclusion}

The HARK project is a modular code library for constructing microeconomic and macroeconomic models with heterogeneous agents. Portfolio choice under uncertainty is central to nearly all academic models, including modern DSGE models (with and without financial sectors), models of asset pricing (eg. CAPM and C-CAPM), models of financial frictions (eg. Bernanke et al. 1999), and many more. Under strict assumptions many of these models can be solved by aggregating agent decision-making and employing the representative agent. However when individual agents look very different from one another - for example, different wealth levels, preferences, or exposures to different types of shocks - assumptions required for aggregation can quickly fail and a representative agent is no longer appropriate. Code to solve the required heterogeneous-agent models tends to be bespoke and idiosyncratic, often reinvented by different researchers working on similar problems. This needless code duplication increases the chance for errors and wastes valuable researcher time.

Researchers should spend their valuable time producing research, not reinventing the wheel when it comes to computational tools. The goal of the HARK toolkit is to ease this burden by providing a simple and easily extensible framework in which a few common models are solved, and clear documentation, testing, and estimation frameworks provide guidance for new researchers to develop their own work in a robust and replicable manner. The final goals of the project are to create a collaborative codebase that can serve both researchers and policymakers alike, employing the best of modern software development tools to accelerate understanding and implementation of cutting edge research tools. The solution methods employed in HARK are not the only methods available, and those who have additional methodological suggestions are strongly encouraged to contribute! Increasing returns to production is one of the few "non-dismal" possibilities in economic thought -- we hope to capture this feature of code production in the HARK framework. Key next steps include finalizing the general-equilibrium HARK modules, identifying additional baseline models to replicate in HARK, and encouraging a new generation of students to learn from, use, and contribute to the collaborative construction of heterogeneous-agent models.


# Bibliography

