#!/usr/bin/env python

import collections


def multpots(pots):
    """Multiply Potentials into a single Potential.

    Parameters :
        pots : sequence[n_pots] of Potential :
            The target potentiald to be multiplied.

    Returns :
        newpot : Potential :
            The result Potential.

    Raises :
        None

    Notes :
        Potentials with empty tables are ignored. If a table of type 'zero' is
        encountered, the result is a table of type 'zero' with table 0, and
        empty variables.
    """
    # import copy
    if not isinstance(pots, collections.Sequence):
        pots = [pots]
    newpot = pots[0]
    for i in range(1, len(pots)):  # loop over all the Potentials
        #FIX ME: did not check dimension consistency
        newpot = newpot * pots[i]
    return newpot
