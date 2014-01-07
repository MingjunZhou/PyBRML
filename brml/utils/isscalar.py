#File :  isscalar.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-09
#License : BSD 3 clause
#Description :

import numpy as np
import collections


def isscalar(a):
    """Check whether the input set is scalar.

    Parameters :
        a : scalar or vector :
            Input to be check.

    Returns :
        isscalar : boolean :
            True for a is scalar, false for a is not scalar.

    Raises :
        None

    Notes :
        isscalar(1) == True
        isscalar([1]) == True
        isscalar([1, 2]) == False
        isscalar(np.ndarray([1])) == True
        isscalar(np.ndarray([1, 2])) == False
    """
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
