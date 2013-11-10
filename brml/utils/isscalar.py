#File :  isscalar.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-09
#License : BSD 3 clause
#Description :

import numpy as np
import collections

def isscalar(a):
    if isinstance(a, collections.Sequence):
        if len(a) == 1:
            return True
        else:
            return False
    elif isinstance(a, np.ndarray):
        if a.size == 1:
            return True
        else:
            return False
    else:
        return np.isscalar(a)
