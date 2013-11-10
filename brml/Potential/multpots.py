#!/usr/bin/env python

"""
MULTPOTS Multiply Potentials into a single Potential
newpot = multpots(pots)

multiply Potentials : pots is a cell of Potentials
Potentials with empty tables are ignored
if a table of type 'zero' is encountered, the result is a table of type
'zero' with table 0, and empty variables.
"""


def multpots(pots):
    # import copy
    newpot = pots[0]
    for i in range(1, len(pots)):  # loop over all the Potentials
        #FIX ME: did not check dimension consistency
        newpot = newpot*pots[i]
    return newpot
