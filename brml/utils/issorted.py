#File:  issorted.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-08-17
#License: BSD 3 Clause
#Description: Is the variables field in the Potential is sorted(low to high)?

import numpy as np


def issorted(pot, variables=[]):
    variables = np.array(variables)
    originVar = pot.variables
    if np.size(variables) == 0:
        return np.equal(np.sort(originVar), originVar)
    else:
        return np.equal(originVar, variables)
