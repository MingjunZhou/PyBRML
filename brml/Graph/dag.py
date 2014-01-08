#!/usr/bin/env python

import numpy as np
from ..Potential import Potential


def dag(pots):
    """Get the adjacency matrix (zeros on diagonal) for a Belief Network.

    Parameters :
        pots : list of Potential :
            This list of Potential represents the belief network.

    Returns :
        A : np.ndarray, shape = [n_nodes, n_nodes] :
            The adjacency matrix.

    Raises :
        None

    Notes :
        A = dag(pots)

        Assumes that pots[i] contains the distribution p(i|pa(i)).
    """
    if isinstance(pots, Potential):
        pots = [pots]
    vars = np.array([], dtype=int)
    for p in pots:
        vars = np.union1d(vars, p.variables)
    #print "variables:", vars
    N = vars.size
    #print "number of variables:", N
    A = np.zeros((N, N), dtype=int)
   # print "empty DAG matrix: \n", A
    for p in pots:
        cond = p.variables[0]
        evid = p.variables[1:]
        #print "cond=", cond
        #print "evid=", evid
        #print "vars=", vars
        cond = np.in1d(vars, cond).nonzero()
        evid = np.in1d(vars, evid).nonzero()
        #print "cond=", cond
        #print "evid=", evid
        #print "\n"
        A[evid, cond] = 1
    A = A - A * np.eye(N, dtype=int)
    #print "A=", A
    return A
