

James:

Thank you for (an extended chunk of) your time today.  This email concerns
what resources / files you'll want to look at when beginning to tackle the
Jupyter notebooks.  My take is that there are four types of notebooks that
will be constructed (eventually):

1) Introduction to HARK: There might be only 1 to 3 of these, which would
simply be (slightly) interactive tutorials for the basic structures of
HARK: passing dictionaries to AgentType subclasses to make instances, what
goes into a subclass of AgentType, the solve method, the nature of time /
cycles and sequences, etc.  These might also point the reader to the
general purpose tools and where to find their documentation.

2) Model demonstrations: For each model module in HARK, the material that
is currently in the "if __main__" block of that file should be moved into a
notebook, with additional explanation.  This is what I began to describe
for you today; further down in this email I've copy-pasted part of an email
to Chris from a week ago with the full list of what I would eventually want
in them.

3) Simple example applications: Very simple examples of using HARK to
address a real world question.  Rather than arbitrarily chosen parameters,
these examples make some semi-sensible choices for most parameters, then do
some experiment to play with one (or some other small number) of remaining
parameters.  A few of these were cooked up for a presentation at the Fed,
and can be found in /ConsumptionSaving/Demos

4) Paper notebooks: As an accompaniment to a proper research paper (that
uses Econ-ARK tools), we would like authors to make a notebook that
demonstrates some of their results / methodology, and would let the reader
easily play with it a bit-- twiddle parameters, visualize the solution,
whatever.  This is sort of what Chris was showing you with in the document
from Paul Romer, but that wasn't about a research paper (as far as I could
tell).

What we really want for the "roadshow" is type 2 and type 3.  You should
not be concerned with type 4 at all-- that's part of the "we're going to
change the way that economists communicate their ideas to each other" pipe
dream.  Type 1 is also a big priority, but that's something I can develop
and/or we should talk to Software Carpentry people because that's kinda
their thing.

The /ConsumptionSaving folder has all of the (non-nonsense) model modules.
These are:

- ConsIndShockModel.py
- ConsPrefShockModel.py
- ConsAggShockModel.py
- ConsMarkovModel.py
- RepAgentModel.py
- ConsMedModel.py
- ConsGenIncProcessModel.py
- TractableBufferStockModel.py

The first of those is sort of the "root" of the consumption-saving family
tree, and the first module that should have a notebook developed for it.
The file /Documentation/ConsumptionSavingModels.pdf has writeups of some of
those models, but has some mistakes and outdated information.  I would like
the type 2 notebooks to combine the material from the Models.pdf document
with the examples from the "if __main__" block of each model module, along
with an in-line construction of the parameter dictionary that is used.

As is, all of the examples in the model modules draw on dictionaries
defined in ConsumerParameters.py.  That file has comments for each
parameter as it is defined.

The other document you should read (at least briefly) is
`/Documentation/HARKmanual.pdf`.  That will provide a good overview of the
structures we're using.  This document uses FashionVictimModel as a
non-economic example to demonstrate some HARK concepts.  It's weird, but I
think the documentation for it can be expanded and incorporated into the
type 1 intro lesson notebooks.  My intent was to have the absolute simplest
possible choice (binary) with a semi-entertaining premise and no economic
content on which a user might get hung up.

The repository called PARK contains slides from presentations that we have
given over the past couple years.  I *think* the most comprehensive of
these is
https://github.com/econ-ark/PARK/blob/master/Intro-To-HARK_MNW_20170508_JHU.pdf
... I'm not sure how much of it will be sensible to a non-economist.

---------------------------------------------------------

PARTIAL EMAIL TO CHRIS WITH TYPE 2 THOUGHTS:

...the time/place to add a lot of that is when we make nice Jupyter
notebooks for each model.  Each of these notebooks would include, in some
order:

1) A complete description of the model, in English
2) A complete and proper mathematical representation of the problem
3) A list of all of the inputs for the solution function (and which are
time varying)
4) The mapping between those inputs and the mathematical representation
5) Delineation between which inputs are passed directly vs which are
constructed
6) For constructed inputs, something about the method that constructs them
and which "primitive" parameters are used
7) One or more example dictionaries that can be passed to the agent class
to make a solveable instance
8) Demonstrations of solving and simulating those examples
9) Plots of the solution to the example
10) Commentary on the solution method and its limitations

Basically, an interactive combination of the models PDF, the examples in
each model module, and the example parameter file, plus extra stuff that
gets deep down into the weeds.

     -- mnw
