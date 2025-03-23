---
jupyter:
  jupytext:
    cell_metadata_filter: -all
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

<font size="10"><b><center>Heterogeneity and Macro Modeling</center></b></font>
<font size="10"><b><center>In Policymaking Institutions</center></b></font>
<br><br>
<font size="6"><b><center>Christopher Carroll</center></b></font>
<font size="6"><b><center>Johns Hopkins University</center></b></font>
<br><br>
<font size="6"><b><center>"Heads of Research of the European Central Banks"</center></font>
     <font size="6"><b><center>London, June 24, 2019</center></b></font><br>



# Bottom lines

1. Rep Agent ('RA') models are badly wrong
   * Inconsistent with basic (micro) theory _and_ evidence
   * $\Rightarrow$ least reliable when most urgently needed 
   <!-- Not hard to match reality in Great Moderation: Nothing ever happened, many models can reproduce that! -->
1. New tools can solve these problems
   * Now: Hand-crafted, bespoke "works of art"
      * "Irreproducible": a compliment for artworks
      * For models, not so much
      <!-- spoke to someone from Very Important CB who said had spent weeks trying to understand zip file of code for one well known model and finally gave up -->
   * Need: "Open source" tools for HA models
      * Like DYNARE for RA
      * Creatable, maintainable by staff economists

<!-- 1:30 -->


# Teaser

Bayer and Luetticke (2019): What Made Great Recession Great?

Two models:

* RANK: Sudden, massive, highly persistent neg pty shock
   * Why?  Where did it come from?  
* HANK: Sudden, massive neg aggregate demand shock
   * Interpretation: Uncertainty _a la_ Nick Bloom
   * Dynamics are endogenous instead of assumed
      * Recovery is _autonomously_ slow <!-- Fed forecasts overpredicted recovery for 3 years running -->


<font size="5"><b><center>Representative Agent New Keyensian ('RANK')</center></b></font>

<center><img src="./BayerLuetticke/RANK_DS_Smoother_of_logY.png" width="600">


<!-- #region -->
<font size="5"><b><center>Heterogeneous Agent New Keyensian ('HANK')</center></b></font>


<center><img src="./BayerLuetticke/HANK_DS_Smoother_of_logY.png" width="600">
<!-- #endregion -->

### Diametrically opposite policy prescriptions:

* RANK: Austerity
* HANK: Stimulus

IMF: "Stimulus worked; austerity didn't"


## Framing: It's All About the MPC ('$\kappa$')

### "Old Keynesian ('OK')" Cross ($\approx$ ZLB)

\begin{eqnarray}
\texttt{Period 0:   } \hat{Y} & = & 1 \\
\texttt{Period 1:   } \phantom{\hat{Y}} & = & 1 + \kappa \\
\texttt{Period 2:   } \phantom{\hat{Y}} & = & 1 + \kappa + \kappa^2
\end{eqnarray}

<!--
|  $\phantom{.}$     | $\phantom{Periods:}$  | Date of Unit Shock <br> 0    | <br> 1   | <br> 2   | <br> ... |
| :---:     | :---:    | :---: | --- | --- | --- | 
| $\Delta Y$ |  =    |  1    |
| . |  = | 1   |  + $\kappa$   |     |
| . |  = | 1   |  + $\kappa$   |  +$\kappa^{2}$   |
| $\vdots$ |
| . |  = | $\frac{1}{(1-\kappa)}$   | |
|   .     | Periods:  | 0 (date of shock)    | 1   | 2   | 3   |  ... |
| . |  = | 1   |  + $\kappa$   |  +$\kappa^{2}$   | +$\kappa^{3}$   | -->

Suppose "period" is a year and $\kappa = 0.75$

2-year "Multipliers"
  * $G = 1.75$
  * $T \approx 1.3 (= 0.75+0.75^2)$


#### Anti-Old-Keynesians ('New Classicals'):

$\kappa=0.75$ has "no microfoundations"
   * Perf Foresight unconstrained model $\Rightarrow \kappa \approx 0.04$  
   <!-- More like 0.01 in models with habit formation -->


#### "RA New Keynesian" (RANK) Models

Fiscal Policy ('FP')?

Doesn't work because $\kappa \approx 0.04$ and
  1. Ricardian Equivalence for taxes
  1. $G$ mostly changes _split_ of $Y$ between $C$, $I$, $G$


#### "RA New Keynesian" (RANK) Models

Monetary Policy ('MP')?

Only works via Intertemporal Elasticity of Substitution (IES)
  * Problem: All micro and macro estimates are IES $\approx$ 0
     * $\Rightarrow$ MP doesn't work either
     * Kludge: Assume high IES despite evidence
<!-- Excuse: It's macroeconomics so we can do this if we want
       * Blanchard, Eichenbaum
       * One of the earliest criticisms of RA models
           * No satisfactory excuse ever given -->
  * No "redistribution" channel (everyone identical)


#### "Two Agent New Keynesian" (TANK) Models <!-- Will discuss role below -->

* "Savers" like RA in RANK model
* "Spenders" like in OK model


### Recent Update (Last 10 Years)

#### Theory and Data Finally Agree

##### Theory (with uncertainty, liq constraints, illiquid assets, heterogeneity):

   * Easy to get $\bar{\kappa} = 0.5$ or more
   * Lots of heterogeneity in $\kappa$

##### Data (e.g., National registries)
   * Estimates are robustly $\bar{\kappa} = 0.5$ or more
   * Lots of heterogeneity in $\kappa$


### Auclert (2017)

_In a model where everyone is optimizing_:

FP that changes income:
   * $\bar{\kappa}$: is a 'sufficient statistic'

MP:
<!--* Channels: -->
  1. IES channel still exists
  1. _Also_ an "Old Keynesian"-like channel:
	    * Effects of redist _between_ people with *different* $\kappa$'s         


### Crawley (2019): Measure Auclert Stuff<!-- Kohn:"Monetary policy is like war -- conducted in a fog."  But at least engineers know how the guns work! --> 

Relative size of MP channels?
   * Danish registry data for hetero in $\kappa$
      * Mechanism: $i \uparrow$
         * Reduces $Y$ for debtors ($\kappa = 0.75$)
         * Increases $Y$ for creditors ($\kappa = 0.25$)
   * $\kappa$ hetero channel is $\approx$ 5 times size of IES channel


### Crawley and Moon (2019)
#### Does Auclert Decomposition Work in Theoretical Models?

Can theory reproduce Crawley (2019) empirical findings?

* Yes -- if you include heavily indebted consumers

<!-- #region -->
<font size="5"><b><center>Heterogeneous Agent New Keyensian ('HANK')</center></b></font>


<center><img src="./Figures/KeynesianDebt_sigma3.png" width="600">

<!-- #endregion -->

#### Policy Transmission Channels

Hetero $\kappa$:
   * crucial for _both_ MP _and_ FP

If: we know how a policy:
   1. Redistributes $Y$ betw groups w different $\kappa$'s
   1. Changes constraints (which can have $\kappa >> 1$)


Then: Micro evidence can _predict_:
   1. How previously untried _macro_ policies might work
   1. How effects of given policy should change over time
       * "Operation Twist" could have v diff effects:
	     * US vs UK
	     * 1960s vs 2020s


#### TANK: Combines Defects of Both Progenitors

1. No credible microfoundations
   * For either class <!-- $\Rightarrow$ little confidence in predictions OoS -->
   * Can't use micro data to think about macro questions
1. Dynamics are wrong
   * Fails to produce observed sluggish dynamics
      * Half life of $C$ shocks is maybe a year
1. Says nothing about dynamic roles of:
   * Uncertainty
   * Constraints
   * Finance

<!-- 25 mins to get here -->


<!-- So, why hasn't everybody already adopted HANK models?  Too hard! -->
## Challenge: HA Models Are Too Hard?

### That Can Change (Endogenously)

* DSGE RA models once viewed as 'too hard'
* Where there's a will there's a way: DYNARE
<!-- Like me, senior policymakers in this room are probably old enough to
remember when the same thing was said about RA RE macro models; we need to keep
our Old Keynesian econometric models because RE models are too complex for
government work -->


## Feasibility of 'DYNARE for HA models'?

A New Insight is Very Good News: <!-- Kaplan et al, Krusell, Bayer and Luetticke, cstwMPC -->
* Macro and Micro Largely Separable
* Solve micro model for steady-state ('StSt') ONCE
   * Using powerful micro tools
* Macro fluctuations?
   * Deviations from StSt
   * Not too hard to handle

[Econ-ARK/HARK](https://github.com/econ-ark.org) open source toolkit is a start
   * So far mostly focused on micro problem
   * Have begun to integrate with macro 


## Short Run

* CB's should build 'Toy' Models Now
   * Norway has a head start
   * FRB has a number of people
      * Crawley starts there in Sep
   * Crucial:
      * Need to be able to swap models
      * Learn from each other
      * $\Rightarrow$ common (open source) toolkit
   * Do not use TROLL!


## Long Run

#### 'Main model' key features: 
   1. Optimizing consumers subject to:
      1. Constraints
      1. Uncertainty
   1. Tracks Income (and perceptions thereof), wealth distributions
      1. 'seriously': resembles micro evidence

#### 'Auxiliary models'
   1. Fiscal policy (track distributional consequences)
   1. MacroPru
   1. Detailed monetary policy


## Digression on MacroPru

The _whole_ point is to understand how many _micro_ consumers will stop paying <!-- Not, of course, that MacroPru authorities care about their financial distress -- they (rightly) are concerned about the distress they may inflict on fin -->

Impossible to learn reliable answers using AR(1) models of aggregated data

U.S. micro data: "double trigger"

People don't default unless _both_:
1. Deeply underwater
1. Unemployment or other big neg income shock

Conclusion?

Optimal MacroPru rules:
-- Depend on relative sizes of $Y$ vs $P$ shocks

Micro modeling $\Rightarrow$ better macro policy

<!-- #region -->
## Getting There

* A long way to go yet
   * DYNARE wasn't built in a day


* Institutional support of infrastructure development
    * Like DYNARE has had
    * As is done in other scientific/technical fields
        * [Astronomy, Artificial Intelligence, Bayesian Statistics, Biology, ...](https://www.scipy.org/topical-software.html)

Feasible with modern collaborative software development tools:
   * Modular
   * Open-source
   * Platform-Independent
   * Automatic testing/debugging tools
   * Robust reproducibility
<!-- #endregion -->
