#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import numpy as np
import copy
from ..utils.index_to_assignment import index_to_assignment
from ..utils.ismember import ismember
from .potential import potential


def orderpot(pot, varargin=None):
    """
    Return potential with variables reordered according to orderpot. If order
    is missing or empty, the variables are sorted (low to high).
        newpot = orderpot(pot, <order>)

    Parameters
    ----------

    pot: brml.potential.potential object
        An object with fileds variables and table.
        pot.variables is a list of integer that indicates variables's name.
        pot.table is a np.ndarray of probability distribution.

    varargin: array_like (optional)
        An array_like of new orders.
        If varagin is missing or empty, the variables are sorted (low to high)

    Returns
    -------

    newpot: brml.potential.potential
        the new potential object
    """
    if not pot:
        return

    if varargin is None:
        varargin = []

    oldvs = pot.variables
    oldca = pot.card
    oldta = pot.table

    if not varargin:  # varargin is empty or missing
        varargin = copy.deepcopy(oldvs)
        varargin.sort()

    newvs = np.array(varargin)
    newta = copy.deepcopy(oldta)
    newta.resize(np.prod(oldca))
    #newns = copy.deepcopy(oldns)

    dummy, old_in_new, all_old_in_new = ismember(oldvs, newvs)
    dummy, new_in_old, all_new_in_old = ismember(newvs, oldvs)
    newca = oldca[list(new_in_old)]

    for i in range(np.prod(newca)):
        newass = np.array(index_to_assignment(i, newca))
        oldass = newass[list(old_in_new)]
        newta[i] = oldta[tuple(oldass)]

    newta.resize(newca)
    newpot = potential(newvs, newca, newta)
    #pot.variables = newvs
    #pot.card = newca
    #pot.table = newta

    return newpot
