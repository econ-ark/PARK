# HARK and dolo and dolARK

This is an update to my thoughts about foundations of "HARK 2.0" and the relation to dolo/dolARK. What I have now realized is that much of what I articulated in [this document](https://github.com/econ-ark/PARK-make/blob/master/Roadmaps/HARK/20180402_CDC-to-MNW-NMP-PXW.md) last year is already in place, and much more besides.  Dolo is advanced enough that we can already begin moving in the direction of making `dolo` the "engine" that powers HARK even before Pablo has a draft of the `dolARK` specification.

I came to understand what a general-purpose tool dolo already is by figuring out how to construct in dolo the solution to the core model that we solve in HARK, the buffer stock model solved by the `IndShockConsumerType` class. 

A link to the relevant notebook is [here](https://github.com/llorracc/dolo/blob/master/examples/notebooks/BufferStock-HARK-vs-dolo.ipynb).  (In order for it to work, you will need to follow the installation instructions for dolo that are linked at the beginning of the document)

In fact, in principle I think most of what we do in HARK now could already be done using dolo as the solution engine.  So, I'm dividing this document into two parts.  First, a discussion of how we can (and should) already begin moving HARK toward the use of the existing dolo tools.  Second, a discussion of part of what I perceive needs to be added to dolo to make the dolARK tool that will provide a full description of all the kinds of models we want to be solvable in HARK.

## Incorporating Dolo in current HARK

I'm not going to recap here what is in dolo -- it is quite well documented
already.  If you are not very familiar with dolo, I'd urge you to spend a few
days getting up to speed on it (as I have finally done).

The dolo "model" object already contains all of the elements needed to completely define a generic infinite horizon Bellman equation problem, in a sufficiently abstract way that the model can in principle be solved by any generic technique capable of solving it, e.g. time iteration or value function iteration or perturbation methods or whatever.  (Of course, a method that is incapable of solving a model will break down when that attempt is made.)

So, for any infinite horizon HARK model, we could in principle add as an option, right now, a choice to use dolo to solve it (rather than the default of using our own handcrafted tools). 

I think we should start by making a full-fledged example of this, building on the solution to the IndShockConsumerType example that I constructed in the notebook linked above.

The way I envision this working is that we could add to the options the user can provide when invoking the tool, an option like "solvemethod=dolo" or something like that, and can also add optional inputs corresponding to the options that the user can specify when using dolo to solve the model (like, whether to use value function iteration, or time iteration).  The class can then have two blocks, one of which consists of the current code, and the other of which basically sets up the configuration info necessary to feed the model to dolo and get dolo to solve.  (Actually, probably the two choices -- solve using our built-ins, or using dolo -- should be determined by a boolean so that if the user wishes the model can be solved using both methods simultaneously and the solutions compared.)

I think we should aim to make this our first team "sprint" where all (or most) of us set aside a few hours to focus intently on it.  I think it would not take longer
than that to get a crude working version of this.  Once we have a crude version hammered out, we can refine it asynchronously, and it should provide a template
for how to do the same thing for other existing infinite horizon tools.

## What DolARK Will Need to add

There are several kinds of things that, so far as I can tell, dolo is not able to represent, and that dolARK will need to define descriptions of.

### Finite Horizons

The first is finite-horizon problems (life cycle in particular; and also "cyclical" problems where for example there are four seasons of the year or twelve months, in which circumstances -- and maybe even the problem being solved -- are different).

### Populations 

Another is that there needs to be some way of representing population distributions and their evolution; in the existing HA literature everybody does this a different way and that is a major barrier to portability of code and
results. 

### Aggregation and Equilibrium

Furthermore, there needs to be a tool that connects the micro distributions and the macro dynamics. There are a number of options here, ranging from something like the "market" class that exists now in HARK to the kinds of thing that Michael Reiter has done, to the new approach that Per Krusell and Kurt Mitman have proposed in which we allow ourselves to assume that the effects of aggregate variables are linear and all shocks are "MIT shocks" which has the potential to radically simplify things.

To get started thinking about this concretely, I propose that we should run with the example we already have in python of a Reiter-type model, the BayerLuetticke tool. So the next steps would be to think about how to represent the elements of models of that kind in an abstract dolo-like way.
