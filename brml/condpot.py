#!/usr/bin/env python

"""
%CONDPOT Return a potential conditioned on another variable
% newpot = condpot(pot,x,y)
% condition the potential to return potential with distribution p(x|y),
% summing over
% remaining variables. If y is empty (or missing), return the marginal p(x)
% If both x and y are missing, just return the normalised table
"""
import numpy as np
from .potential import potential
from intersect import intersect
from setminus import setminus


def condpot(pot, varargin):
    newpot = potential()
    y = []
    x = varargin
    intersection, ix, ipot = intersect(x, pot.variables)
    newpot.variables = intersection
    FULL_axis = np.arange(pot.variables.size)
    axis_intersection = ipot
    other_axis = setminus(FULL_axis, axis_intersection)
    newpot.table = np.apply_over_axes(np.sum, pot.table, other_axis)

    newpot.table = newpot.table / np.sum(newpot.table)

    return newpot
