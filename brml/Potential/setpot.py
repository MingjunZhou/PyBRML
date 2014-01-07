#!/usr/bin/env python

import numpy as np
import copy as copy
from .Potential import Potential
from ..utils.ismember import ismember
from ..utils.intersect import intersect
from ..utils.set_minus import set_minus
from ..utils.index_to_assignment import index_to_assignment


def setpot(pot, evvariables, evidstates):
    """Set Potential variables to specified states.

    Parameters :
        pot : Potential :
            The target potential to be set.

        evvariables : sequence[n_variables, ] or np.ndarray[n_variables, ] :
            Several variales to be set.

        evidstates : sequence[n_variables,] or np.ndarray[n_variables, ] :
            The states that each variable in evvariables are set to.

    Returns :
        newpot : Potential :
            The new pot with the variables set.

    Raises :
        None

    Notes :
        The new Potential does not contain the evidential variables
    """
    #FIXME: data format needed to be unified
    vars = pot.variables
    #vars = np.array(pot.variables) # convert to ndarray format
    #evariables = np.array(evvariables)
    # convert to ndarray format
    #evidstates = np.array(evidstates) # convert to ndarray format
    #print "variables:", vars
    #table = pot.table
    nstates = pot.card
    #print "number of states:", nstates
    #print "vars:", vars
    #print "evvariables:", evvariables
    intersection, iv, iev = intersect(vars, evvariables)
    #iv = np.array(iv)
    #iev = np.array(iev)
    #print "intersection:", intersection
    #print "iv:", iv
    #print "iev:", iev
    #print "iv type:", type(iv)
    #print "number of intersection:", intersection.size
    if intersection.size == 0:
        newpot = copy.copy(pot)
    else:
        newvar = set_minus(vars, intersection)
        dummy, idx, allidx = ismember(newvar, vars)
        newns = nstates[idx]
        newpot = Potential()
        newpot.variables = newvar
        newpot.card = newns
        newpot.table = np.zeros(newns)
        #print "idx:", idx
        #print "iv:", iv
        for i in range(np.prod(newns)):
            newassign = index_to_assignment(i, newns)
            oldassign = np.zeros(nstates.size, 'int8')
            oldassign[idx] = newassign
            oldassign[iv] = evidstates
            #print "newpot.table.shape:", newpot.table.shape
            #print "newassign:", newassign
            #print "newassign type:", type(newassign)
            newpot.table[tuple(newassign)] = pot.table[tuple(oldassign)]

    return newpot
