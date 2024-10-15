import sys 
import os
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../FashionVictim'))
sys.path.insert(0, os.path.abspath('./'))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from HARKutilities import plotFuncsDer, plotFuncs
from FashionVictimModel import *
from HARKcore import AgentType, Solution, NullFunc
from HARKinterpolation import LinearInterp
from HARKutilities import approxUniform, plotFuncs
import numpy as np
import scipy.stats as stats
import FashionVictimParams as Params
from copy import copy


from time import clock
from HARKcore import Market
mystr = lambda number : "{:.4f}".format(number)
import matplotlib.pyplot as plt
from copy import deepcopy

do_many_types = True

# Make a test case and solve the micro model
TestType = FashionVictimType(**Params.default_params)
print('Utility function:')
plotFuncs(TestType.conformUtilityFunc,0,1)

t_start = clock()
TestType.solve()
t_end = clock()
print('Solving a fashion victim micro model took ' + mystr(t_end-t_start) + ' seconds.')

'''
print('Jock value function:')
plotFuncs(TestType.VfuncJock,0,1)
print('Punk value function:')
plotFuncs(TestType.VfuncPunk,0,1)
print('Jock switch probability:')
plotFuncs(TestType.switchFuncJock,0,1)
print('Punk switch probability:')
plotFuncs(TestType.switchFuncPunk,0,1)
'''
    
# Make a list of different types
AltType = deepcopy(TestType)
AltType(uParamA = Params.uParamB, uParamB = Params.uParamA, seed=20)
AltType.update()
AltType.solve()
type_list = [TestType,AltType]
u_vec = np.linspace(0.02,0.1,5)
if do_many_types:
    for j in range(u_vec.size):
        ThisType = deepcopy(TestType)
        ThisType(punk_utility=u_vec[j])
        ThisType.solve()
        type_list.append(ThisType)
        ThisType = deepcopy(AltType)
        ThisType(punk_utility=u_vec[j])
        ThisType.solve()
        type_list.append(ThisType)
    for j in range(u_vec.size):
        ThisType = deepcopy(TestType)
        ThisType(jock_utility=u_vec[j])
        ThisType.solve()
        type_list.append(ThisType)
        ThisType = deepcopy(AltType)
        ThisType(jock_utility=u_vec[j])
        ThisType.solve()
        type_list.append(ThisType)

# Now run the simulation inside a Market 
TestMarket = Market(agents        = type_list,
                    sow_vars      = ['pNow'],
                    reap_vars     = ['sNow'],
                    track_vars    = ['pNow'],
                    dyn_vars      = ['pNextIntercept','pNextSlope','pNextWidth'],
                    millRule      = calcPunkProp,
                    calcDynamics  = calcFashionEvoFunc,
                    act_T         = 1000,
                    tolerance     = 0.01)
TestMarket.pNow_init = 0.5
    
TestMarket.solve()
plt.plot(TestMarket.pNow_hist)

"Proportion of punks in the population."

plt.show()


pPunks_smooth = pd.rolling_mean(pPunks,25)
plt.plot(pPunks_smooth, label="Punks")
plt.ylim([0.46,0.54])
plt.axhline(y=.5, linewidth=0.8)
#plt.title("Proportion of punks in the population")
plt.ylabel("Fraction")
#plt.figtext(x=0.01, y=0.005, s="*Smoothed with 25-period moving average.")
plt.xlabel("Time")
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

#plt.tight_layout()
plt.savefig("./fraction_of_punks.png")
plt.savefig("../../dissertation/HACK_docs_pandoc/fraction_of_punks.png")

plt.show()



'''
pPunks = np.array(TestMarket.pNow_hist[1:])
pJocks = 1.0 - pPunks
plt.plot(pJocks, label="Jocks")
plt.plot(pPunks, label="Punks")
plt.show()


pPunks = np.array(TestMarket.pNow_hist[1:])
pJocks = 1.0 - pPunks

plt.plot(pJocks, label="Jocks")
plt.ylim([0.42,0.58])
plt.axhline(y=.5, linewidth=0.8)
#plt.axhline(y=0.002, xmin=0, xmax=1, hold=None)
plt.show()

pPunks_smooth_a = pd.rolling_mean(pPunks,20)
plt.plot(pPunks_smooth, label="Punks")
plt.ylim([0.4,0.6])
plt.axhline(y=.5, linewidth=0.8)
plt.show()
'''


