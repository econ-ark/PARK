
# Open Source Modeling in Economics and Other Social Sciences Using Python

## DESCRIPTION

Code for many areas of social science research, including economics, tends to be handcrafted and bespoke, and consequently is rarely validated in any meaningful way during the academic journal refereeing process.  While economics has not suffered a replication crisis to the degree faced in some other fields like social psychology, there are some recent instances of well known teams of economists addressing the same question with ostensibly similar models and coming to fundamentally different conclusions, for reasons that likely reflect subtle differences in the coding of the models.

The [Econ-ARK](http://github.com/econ-ark) project seeks to remedy this problem, and to head off a replication crisis in computational social science, by establishing an open source repository of Python code and other tools for solving, simulating, and estimating dynamic structural models of the kind used in economics and affiliated fields, including sociology, political science and epidemiology. The core aim of the project is to provide a modular, extendible, and interoperable framework that can be used across a wide array of models commonly used in these fields, including structural microeconomics, heterogeneous agent macroeconomics, game theory, and agent-based modeling of financial markets (including models of contagion drawn from epidemiology).  The aims are to reduce entry costs into computational modeling, to make replication transparent and straightforward, and to accelerate the pace of progress by creating a common framework for communication of results.


## AUDIENCE

Our target audience is Python developers who are interested in open science and want to get involved.  We know that there will be a dearth of PhD economists at PyCon (we're probably already friends with most of them), so the economics content of the talk will be high level and conceptual rather than 'in the weeds': We will say enough for a technically or scientifically minded listener to understand our aims and how to accomplish them.  Our goal is to persuade audience members to become involved in the project.  While we don't expect anyone there to program new economic models, a host of existing numerical methods that we would very much like added to the ARK should be programmable by anyone with a mathematical or scientific background.  Additionally, we are interested in meeting developers and making connections to open science projects using Python in other fields.

## OUTLINE

1. Preliminaries (2 mins)
    * Who we are
    * Econ-ARK and its funding
    * Check for economists in audience
2. Background (6 minutes)
    * Structural vs reduced form economics (3 minutes)
    * How structural economics is in the stone age of programming (2 minutes)
    * Problems that this generates (1 minute)
3. How Econ-ARK solves this with Python (5 minutes)
    * See description below
4. Technical details of HARK (12 minutes)
    * Representing agents: AgentType class (6 mins)
    * Representing environments: Market class (6 mins)
5. Object-oriented solution methods (5 minutes)
    * See 'WhyPython.pdf' document in [Econ-ARK/PARK](http://econ-ark/PARK/WhyPython.pdf) for sense of content


## ADDITIONAL NOTES

The code for HARK is open source and [available at github](http://www.github.com/econ-ark/HARK).  Slides from past presentations are posted at [Econ-ARK/PARK](http://www.github.com/econ-ark/PARK), including a four hour tutorial session at the Federal Reserve Board of Governors.  This would be the first presentation we would give to non-economists, so the nature of introductory material would be different here: no need to justify Python at PyCon, but we do need to bring the audience up to speed on some economic topics.

I am a university professor with experience teaching at the graduate and undergraduate levels, so public speaking is kind of my day job.  The norm in academic economics (and my classroom) is that audience members are free to interrupt with questions at any time; I will make this clear at the start of the talk, which is why I have not included Q&A time in the schedule.  The outline is ordered from most to least important material, and I am used to abbreviating talks on the fly.

The principals in the ARK project are mostly PhD economists, along with some affiliated computational social science PhD's and students.  The Econ-ARK project is relatively young, but we received a large, three-year grant from the Alfred P. Sloan Foundation this past summer to support and expand our efforts.

