#File:  setdiff.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-08-17
#License: BSD 3 clause
#Description:

import numpy as np
from ismember import ismember


def set_diff(a, b):
    """Get the difference between SET a and SET b.
    
    Usage :
        diff, diff_index_in_a = set_diff(a, b)

    Parameters :
        a : A 1-d sequence or a 1-d nd.array. 
            SET a.

        a : A 1-d sequence or a 1-d nd.array. 
            SET b.

    Returns :
        diff : A 1-d nd.array.
            All the elements in SET a but not in SET b.

        diff_index_in_a : A 1-d nd.array with the same size of SET a.
            a(diff_index_in_a) == diff.

    Raises :
        None
    
    """

    a = np.array(a)
    b = np.array(b)
    diff = np.setdiff1d(a, b)
    dummy, iA, alliA = ismember(diff, a)
    return diff, iA
