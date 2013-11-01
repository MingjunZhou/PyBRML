#!/usr/bin/env python

"""
%CONDPOT Return a potential conditioned on another variable
% newpot = condpot(pot,x,y)
% condition the potential to return potential with distribution p(x|y),
% summing over remaining variables. If y is empty (or missing), return the
% marginal p(x).
% If both x and y are missing, just return the normalised table
"""
import numpy as np
from .potential import potential
from setminus import setminus
from sumpot import sumpot
import copy


def condpot(pots, x=None, y=None):
    if isinstance(pots, potential):
        pots = [pots]
    else:
        pots = list(pots)
    
    if x is None:
        x = np.array([])
    else:
        x = np.array(x)

    if y is None:
        y = np.array([])
    else:
        y = np.array(y)
    
    newpots = [potential() for i in range(len(pots))] 
    for i, pot in enumerate(pots):
        other_axis = setminus(pot.variables, y)
        other_axis = setminus(other_axis, x)
        #if y.size != 0:
        pxy = sumpot(pot, other_axis)
        #print "pxy.variables:", pxy.variables
        py = copy.deepcopy(pxy)
        py = sumpot(py, x)
        #print "py.variables:", py.variables
        #print "pxy.table:", pxy.table
        #print "py.table:", py.table
        newpots[i]= pxy / py
        newpots[i].table = newpots[i].table / np.sum(newpots[i].table)

    if len(pots) == 1:
        return newpots[0]
    else:
        return newpots
    """
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
