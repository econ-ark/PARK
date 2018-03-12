# What Is the Difference Between the Econ-ARK/HARK and [AB-CE](https://github.com/AB-CE/abce)

HARK's starting point is the rational, forward looking, optimizing framework that is at the heart of neoclassical economics.  

On the individual level, our approach is to first specify a dynamic problem that the agent faces:
   0. The situations he might find himself in ("state space")
      * e.g., how much wealth does he have, what is his income
   0. The actions he can actually take in each state ("budget correspondence")
      * There is some budget constraint that restricts feasible actions
   0. What types of actions he can take ("control space")
      * e.g., how much does he choose to spend
   0. His preferences over states and control variables
      * e.g., a utility function that says more consumption is better, or that the state of being a homeowner yields some pleasure
   0. The ways in which choices of variables under his control affect his future and the ways in which his state (say, his wealth) changes depending on the choices of control variables (say, his consumption spending). 

These elements imply an optimal policy function -- the plan (say, for consumption spending given income and wealth) that best satisfies the agent's preferences. 

Then we construct an environment in which many agents act on this optimal policy and, we see what the result is.

There's sometimes an additional layer to the problem, where agents have "beliefs" about how the world works, and those beliefs affect their optimal decision. But the truth about how the world works depends on the actions of all the agents (via some aggregation). 

The traditional "rational expectations" assumption is the default in our modeling setup.  In this case, agents are endowed with the beliefs such that, if everyone holds those beliefs, the actual true outcome 
corresponds to those beliefs. (The "rational expectations" beliefs are in a sense a self-fulfilling prophecy).

The toolkit allows us to deviate from this framework, in the sense that agents might make mistakes, or not have full information, or have incorrect perceptions of the problem they face, etc. But everything we do in HARK is grounded in the concept of agents who are *trying* to make themselves as best off as possible.

Most of the machinery in HARK is the set of tools required to solve this "optimal choice in a stochastic world" problem. Most of the rest of the tools are those required to simulate a population of agents behaving according to some  set of rules.

AB-CE is a general-purpose "agent-based" modeling toolkit. The agents in ABCE are "rule obeyers" -- they take actions according to some "policy function" that has been given to them. Why do they do the things they do? Because that's how they're wired. In principle, if you could solve for the optimal choices, you could put some optimizing policy in as their "action logic," and in that case you should get the same result from AB-CE as you would get from the corresponding problem in HARK.

As of this writing (2018-03-12), AB-CE has a much more extensive set of tools for creating and modeling the economic environment in which agents make choices, including extenstive tools for direct interaction between individual agetns. The Econ-ARK roadmap envisions creation of a richer set of tools like those in AB-CE, in a projected future "agent-based" modeling component, but built from the ground up to be interoperable with the tools for optimization and aggregation that are already in HARK.
