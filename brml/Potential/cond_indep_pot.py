#File :  cond_indep_pot.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-19
#License : BSD 3 clause
#Description :


from .sumpot import sumpot
from .condpot import condpot
from .multpots import multpots
import numpy as np


def cond_indep_pot(pot, X, Y, Z):
    """Returns the mean absolute deviation between p(X|Z)p(Y|Z)p(Z) and
    p(X,Y,Z).

    Parameters :
        pot : Potential :
            The target potential.

        X : sequence[n_variables, ] or nd.ndarray[n_variables, ] :
            First group of variables.

        Y : sequence[n_variables, ] or nd.ndarray[n_variables, ] :
            Second group of variables.

        Z : sequence[n_variables, ] or nd.ndarray[n_variables, ] :
            Third group of variables.

    Returns :
        deviation : float :
            The mean absolute deviation.

    Raises :
        None
    """
    allvariables = np.concatenate((X, Y, Z))
#    mp = multpots(pot)
#    print "mp.variables=", mp.variables
#    print "mp.card=", mp.card
#    print "mp.table=", mp.table
    jointpot = sumpot(multpots(pot), allvariables, 0)
#    print "jointpot.variables=", jointpot.variables
#    print "jointpot.card=", jointpot.card
    #print "jointpot.table=", jointpot.table
    pXgZ = condpot(jointpot, X, Z)
    #print "pXgZ", pXgZ.table
    pYgZ = condpot(jointpot, Y, Z)
    pZ = condpot(jointpot, Z)
    pXgZpYgZpZ = multpots([pXgZ, pYgZ, pZ])
    #print "pXgZpYgZpZ.table=", pXgZpYgZpZ.table
    c = np.mean(np.abs(pXgZpYgZpZ.table.flatten() - jointpot.table.flatten()))
    return c
