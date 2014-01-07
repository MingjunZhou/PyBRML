#!/usr/bin/env python

import numpy as np
from ismember import ismember


def intersect(a, b):
    """Get the intersect set of set1 and set2.

    Parameters :
        a : sequence[n_a, ] or np.ndarray[n_a, ] :
            The first set.

        b : sequence[n_b, ] or np.ndarray[n_b, ] :
            The second set.

    Returns :
        intersect : np.ndarray[n_intersect, ] :
            The intersect of set a and set b.

        iA : nd.array[n_variables1, ] :
            a[iA] == intersect.

        iB : nd.array[n_variables2, ] :
            b[iB] == intersect.

    Raises :
        None

    Notes :
        intersect, iA, iB = intersect(a, b)
    """
    a = np.array(a)
    b = np.array(b)
    intersect = np.intersect1d(b, a)
    dummy, iA, alliA = ismember(intersect, a)
    dummy, iB, alliB = ismember(intersect, b)
    return intersect, iA, iB
