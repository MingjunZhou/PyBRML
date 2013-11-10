#File :  whichpot.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-07
#License : BSD 3 clause
#Description :

from ..utils.ismember import ismember
import numpy as np


def whichpot(pots, variables, most_n=None):
    pot_num = []
    nvars = []
    for i, pot in enumerate(pots):
        tf, idx1, idx2 = ismember(variables, pot.variables)
        if all(tf):
            nvars.append(len(pot.variables))
            pot_num.append(i)

    ind = np.argsort(nvars)
    if most_n == None:
        n = len(pot_num)
    else:
        n = np.min([most_n, len(pot_num)])
    pot_num = np.array(pot_num)
    pot_num = pot_num[ind[0:n]]
    return pot_num
