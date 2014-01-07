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

    Parameters :
        a : sequence[n_a, ] or nd.ndarray[n_a, ].
            The first set.

        b : sequence[n_b, ] or nd.ndarray[n_b, ].
            The second set.

    Returns :
        diff : nd.ndarray[n_diff, ] :
            All the elements in set a but not in set b.

        diff_index_in_a : nd.ndarray[n_a, ] of boolean :
            a[diff_index_in_a] == diff.

    Raises :
        None

    Notes :
        diff, diff_index_in_a = set_diff(a, b)

    """
    a = np.array(a)
    b = np.array(b)
    diff = np.setdiff1d(a, b)
    dummy, iA, alliA = ismember(diff, a)
    return diff, iA
