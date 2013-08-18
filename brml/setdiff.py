#File:  setdiff.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-08-17
#License: GNU License
#Description:

import numpy as np
from ismember import ismember


def setdiff(a, b):
    a = np.array(a)
    b = np.array(b)
    diff = np.setdiff1d(a, b)
    dummy, iA, alliA = ismember(diff, a)
    return diff, iA
