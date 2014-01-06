#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import numpy as np
import copy
from ..utils.index_to_assignment import index_to_assignment
from ..utils.ismember import ismember
from .Potential import Potential


def orderpot(pot, varargin=None):
    """Return Potential with variables reordered according to orderpot.

    Parameters :
        pot : Potential :
            The target Potential.

        varargin: sequence[n_variables] or np.ndarray[n_variables], optional, default : None :
            An array_like of new orders. If varagin is missing or empty,
            the variables are sorted (low to high).

    Returns :
        newpot : Potential :
            The new Potential.

    Raises :
        None

    Notes :
        newpot = orderpot(pot, <order>)
        If order is missing or empty, the variables are sorted (low to high).
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
    newpot = Potential(newvs, newca, newta)
    #pot.variables = newvs
    #pot.card = newca
    #pot.table = newta

    return newpot
