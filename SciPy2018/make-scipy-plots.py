import sys 
import os
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('./'))
import numpy as np
import matplotlib.pyplot as plt


import ConsumerParameters as Params
from HARKutilities import plotFuncsDer, plotFuncs
from time import clock

from ConsIndShockModel import PerfForesightConsumerType, IndShockConsumerType, KinkedRconsumerType

mystr = lambda number : "{:.4f}".format(number)


do_simulation           = True

# Make and solve an example perfect foresight consumer
PFexample = PerfForesightConsumerType(**Params.init_perfect_foresight)   
PFexample.cycles = 0 # Make this type have an infinite horizon

start_time = clock()
PFexample.solve()
end_time = clock()
print('Solving a perfect foresight consumer took ' + mystr(end_time-start_time) + ' seconds.')
PFexample.unpackcFunc()
PFexample.timeFwd()

# Plot the perfect foresight consumption function
print('Linear consumption function:')
mMin = PFexample.solution[0].mNrmMin

#plotFuncs(PFexample.cFunc[0],mMin,mMin+10)


###############################################################################

# Make and solve an example consumer with idiosyncratic income shocks
IndShockExample = IndShockConsumerType(**Params.init_idiosyncratic_shocks)
IndShockExample.cycles = 0 # Make this type have an infinite horizon

start_time = clock()
IndShockExample.solve()
end_time = clock()
print('Solving a consumer with idiosyncratic shocks took ' + mystr(end_time-start_time) + ' seconds.')
IndShockExample.unpackcFunc()
IndShockExample.timeFwd()

# Plot the consumption function and MPC for the infinite horizon consumer
#print('Concave consumption function:')
#plotFuncs(IndShockExample.cFunc[0],IndShockExample.solution[0].mNrmMin,5)
#print('Marginal consumption function:')
#plotFuncsDer(IndShockExample.cFunc[0],IndShockExample.solution[0].mNrmMin,5)

# Compare the consumption functions for the perfect foresight and idiosyncratic
# shock types.  Risky income cFunc asymptotically approaches perfect foresight cFunc.
print('Consumption functions for perfect foresight vs idiosyncratic shocks:')            
#plotFuncs([PFexample.cFunc[0],IndShockExample.cFunc[0]],IndShockExample.solution[0].mNrmMin,10)


fig, ax1 = plt.subplots()

# These are in unitless percentages of the figure size. (0,0 is bottom left)
left, bottom, width, height = [0.4, 0.19, 0.45, 0.19]
ax2 = fig.add_axes([left, bottom, width, height])

xmin = IndShockExample.solution[0].mNrmMin
xmax = 10
xmax_big = 500
xmax_big = 250
xmax_big = 250
N = 1000

x = np.linspace(xmin, xmax, N, endpoint=True)
x_big = np.linspace(xmin, xmax_big, N, endpoint=True)

y1 = PFexample.cFunc[0](x)
y2 = IndShockExample.cFunc[0](x)

y1_big = PFexample.cFunc[0](x_big)
y2_big = IndShockExample.cFunc[0](x_big)


ax1.plot(x, y1, label="Perfect foresight")
ax1.plot(x, y2, label="With uncertainty", linestyle='-.')

#ax1.axhline(linewidth=0.5)

ax2.plot(x_big, y1_big) #, linewidth=0.95)
ax2.plot(x_big, y2_big, linestyle='-.') #, linewidth=0.95)

#ax1.set_ylim([0,3.5])
#ax1.set_ylim([-.5,3.5])
ax1.set_ylim([-1,3.5])

ax1.set_xlabel(r"Market resources $M_t$")
ax1.set_ylabel(r"Consumption $C_t$")

#ax1.set_title("Consumption Functions\n")
ax2.set_title(r"Converge for high $M_t$")



ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_linewidth(0.5)
ax2.spines['right'].set_linewidth(0.5)
ax2.yaxis.tick_right()

#plt.xlim([xmin, xmax])

ax1.legend(loc="best", frameon=False)
#ax1.legend(loc="upper left", frameon=False)

plt.savefig("./consumption_functions.png")
plt.savefig("../../dissertation/HACK_docs_pandoc/consumption_functions.png")

plt.show()





'''
fig, ax1 = plt.subplots()

# These are in unitless percentages of the figure size. (0,0 is bottom left)
left, bottom, width, height = [0.25, 0.6, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])

ax1.plot(range(10), color='red')
ax2.plot(range(6)[::-1], color='green')

plt.show()




# Compare the value functions for the two types
if IndShockExample.vFuncBool:
    print('Value functions for perfect foresight vs idiosyncratic shocks:')
    plotFuncs([PFexample.solution[0].vFunc,IndShockExample.solution[0].vFunc],
                  IndShockExample.solution[0].mNrmMin+0.5,10)

'''

###########################################################################

if False:

    # Make and solve an idiosyncratic shocks consumer with a finite lifecycle
    LifecycleExample = IndShockConsumerType(**Params.init_lifecycle)
    LifecycleExample.cycles = 1 # Make this consumer live a sequence of periods exactly once

    start_time = clock()
    LifecycleExample.solve()
    end_time = clock()
    print('Solving a lifecycle consumer took ' + mystr(end_time-start_time) + ' seconds.')
    LifecycleExample.unpackcFunc()
    LifecycleExample.timeFwd()

    # Plot the consumption functions during working life
    print('Consumption functions while working:')
    mMin = min([LifecycleExample.solution[t].mNrmMin for t in range(LifecycleExample.T_cycle)])
    plotFuncs(LifecycleExample.cFunc[:LifecycleExample.T_retire],mMin,5)

    # Plot the consumption functions during retirement
    print('Consumption functions while retired:')
    plotFuncs(LifecycleExample.cFunc[LifecycleExample.T_retire:],0,5)
    LifecycleExample.timeRev()



    ###############################################################################        
        
    # Make and solve a "cyclical" consumer type who lives the same four quarters repeatedly.
    # The consumer has income that greatly fluctuates throughout the year.
    CyclicalExample = IndShockConsumerType(**Params.init_cyclical)
    CyclicalExample.cycles = 0

    start_time = clock()
    CyclicalExample.solve()
    end_time = clock()
    print('Solving a cyclical consumer took ' + mystr(end_time-start_time) + ' seconds.')
    CyclicalExample.unpackcFunc()
    CyclicalExample.timeFwd()

    # Plot the consumption functions for the cyclical consumer type
    print('Quarterly consumption functions:')
    mMin = min([X.mNrmMin for X in CyclicalExample.solution])
    plotFuncs(CyclicalExample.cFunc,mMin,5)



    ###############################################################################

    # NOTE: this is the one that is breaking currently!
    '''
    # Make and solve an agent with a kinky interest rate
    KinkyExample = KinkedRconsumerType(**Params.init_kinked_R)
    KinkyExample.cycles = 0 # Make the Example infinite horizon

    start_time = clock()
    KinkyExample.solve()
    end_time = clock()
    '''

