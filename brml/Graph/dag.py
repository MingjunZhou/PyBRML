#!/usr/bin/env python

"""
DAG Return the adjacency matrix (zeros on diagonal) for a Belief Newtork
A=dag(pot)

Assumes that pot{i} contains the distribution p(i|pa(i))
"""
import numpy as np
from ..Potential import Potential 
	 
def dag(pot):
    if isinstance(pot, Potential):
        pot = [pot]
    vars = np.array([], dtype=int)
    for p in pot:
        vars = np.union1d(vars, p.variables)
    #print "variables:", vars
    N = vars.size
    #print "number of variables:", N
    A = np.zeros((N,N), dtype=int)
   # print "empty DAG matrix: \n", A
    for p in pot:
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
    A = A - A * np.eye(N, dtype=int);
    #print "A=", A
    return A
