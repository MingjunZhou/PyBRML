#File :  setminus.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version :
#Date : 2013-11-05
#License : BSD 3 clause
#Description :

import numpy as np
from ismember import ismember


def set_minus(a, b):
    """Get the elements in the first set but not in the second set.

    Parameters :
        a : sequence[n_a, ] or nd.ndarray[n_a, ].
            The first set.

        b : sequence[n_b, ] or nd.ndarray[n_b, ].
            The second set.

    Returns :
        c : nd.ndarray[n_c, ] :
            All the elements in set a but not in set b.

    Raises :
        None

    Notes :
        c = set_minus(a, b)
        c is the set A, without the elements B. C preserves the ordering of A.
    """
    a = np.array(a)
    b = np.array(b)
    dummy, a_in_inter, all_a_in_inter = ismember(a, b)
    diff = a[dummy == False]
    return diff
