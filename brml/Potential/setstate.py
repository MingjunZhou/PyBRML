#!/usr/bin/env python

import numpy as np
import copy as copy
from ..utils.ismember import ismember
from ..utils.subv2ind import subv2ind


def setstate(pot, variables, state, val):
    """Set a Potential's specified joint state to a specified value.

    Parameters :
        pots : sequence of Potential :
            The target potentials to be set.

        variables : int :
            One variable to set.

        state : int :
            The state of the variable to be set.

        value : float :
            Variable in that state is set with the value.

    Returns :
        newpot : Potential :
            The result Potential.

    Raises :
        None

    Notes :
        p = setstate(pot, variables, states, val)

        All states of the Potential that match the given (sub)state are set to
        val.

        eg: pot=array([1 2], rand(2, 2)

            newpot = setstate(pot, 1, 2, 0.5)
 
        then for newpot.table all table entries matching variable 1 in state 2
        will be set to value 0.5.
    """
    variables = np.array([variables])
    state = np.array([state])
    print type(variables)
    print "original variables:", variables
    print "input state:", state
    p = copy.copy(pot)
    a, tmp = ismember(variables, pot.variables)
    print "tmp=", tmp
    variables = variables[tmp]
    state = state[tmp]
    print "effective variables:", variables
    dum, iperm = ismember(variables, pot.variables)
    print "original variables item in pot:", pot.variables
    print "original table in pot", pot.table
    print "effective variables' index in pot:", iperm
    nstates = pot.table.shape
    nstates = np.array([2])
    print "effective variables in pot NSTATES:", nstates
    permstates = np.empty((1, np.size(nstates)))
    permstates = np.empty(1)
    permstates[:] = np.nan
    print "initial effective variables states: \n", permstates
    permstates[iperm] = state
    print "set effective variables states: \n", permstates
    # set effective var-states to val
    print "permstates=", permstates
    print "permstates.all()=", permstates.all()
    # MATLAB: if all(permstates>0) % if the state is unique
    allcondition = np.logical_not(np.isnan(permstates)).all()
    print "allcondition=", allcondition
    if allcondition:  # if the state is unique
        print "Before setstate: p.table= \n", p.table
        watch_ndx = np.asarray([subv2ind(nstates, permstates)])
        watch_ndx = np.int8(watch_ndx)
        print "Callback watch_ndx = subv2ind(nstates,permstates)=", watch_ndx
        print "val= ", val
        p.table[watch_ndx] = val
        print "After setstate: p.table= \n", p.table

    return p
