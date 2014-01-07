#!/usr/bin/env python

import numpy as np
from .Potential import Potential
from ..utils.set_minus import set_minus
from .sumpot import sumpot
import copy


def condpot(pots, X=None, Y=None):
    """Return P(X|Y), a potential conditioned on another variable.

    Parameters :
        pots : sequence[n_pots] of Potential :
            The target potential.

        X : sequence[n_x, ] or np.ndarray[n_x, ], optional, default : None :
            The target variables.

        Y : sequence[n_y, ] or np.ndarray[n_y, ], optional, default : None :
            The evidence variables.

    Returns :
        newpot : Potential :
            A new pot.

    Raises :
        None

    Notes :
        If Y is empty, return the marginal P(X). If both X and Y are missing,
        just return the normalised table.
    """
    if isinstance(pots, Potential):
        pots = [pots]
    else:
        pots = list(pots)

    if X is None:
        x = np.array([])
    else:
        x = np.array(X)

    if Y is None:
        y = np.array([])
    else:
        y = np.array(y)

    newpots = [Potential() for i in range(len(pots))]
    for i, pot in enumerate(pots):
        other_axis = set_minus(pot.variables, y)
        other_axis = set_minus(other_axis, x)
        #if y.size != 0:
        pxy = sumpot(pot, other_axis)
        #print "pxy.variables:", pxy.variables
        py = copy.deepcopy(pxy)
        py = sumpot(py, x)
        #print "py.variables:", py.variables
        #print "pxy.table:", pxy.table
        #print "py.table:", py.table
        newpots[i] = pxy / py
        #newpots[i].table = newpots[i].table / np.sum(newpots[i].table)
    #np.sum
    if len(pots) == 1:
        return newpots[0]
    else:
        return newpots
    """"
    other_axis = setminus(pots
    if y.size == 0:
        intersection, ix, ipot = intersect(x, pot.variables)
        newpot.variables = intersection
        FULL_axis = np.arange(pot.variables.size)
        axis_intersection = ipot
        other_axis = setminus(FULL_axis, axis_intersection)
        newpot.table = np.apply_over_axes(np.sum, pot.table, other_axis)
        newpot.table = newpot.table / np.sum(newpot.table)
    else:

    return newpot
    """
