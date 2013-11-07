#File :  maxpot.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-06
#License : BSD 3 clause
#Description :

import numpy as np
from ..utils.max_array import max_array
from .Potential import Potential


def maxpot(pot, invariables, over_other=False):
    """Maximise a potential over variables.

    Usage :
        newpot, max_state = maxpot(pot, invariables[, over_other=False | True])

    Parameters :
        pot : Potential class :
            The target potential to be maximised. After the maximisation, the
            origin pot is not changed, instead we get a newpot.

        invariables : sequence[n_variables, ] or nd.ndarray[n_variables, ] :
            Several variables to maximise the potential over.

        maxover : boolean, optional, default: False :
            If maxover is False the potential is maxed over variables, otherwise
            potential is maxed over everything except invariables.

    Returns :
        newpot : Potential class :
            A new pot that maximised the origin potential.

        max_state : nd.array[n_variables, ] :
            pot.table[max_state[i, :]] = newpot.table[i]
    Raises :
        None

    """
    if not isinstance(invariables, np.ndarray):
        invariables = np.array(invariables)
    all_vars = pot.variables
    card = pot.card
    if over_other is False:
        over_vars = invariables
        left_vars = np.setdiff1d(all_vars, invariables)
    else:
        left_vars = invariables
        over_vars = np.setdiff1d(all_vars, invariables)
    new_table, new_state = max_array(pot.table, over_vars, return_states=True)
    new_card = card[left_vars]
    newpot = Potential(left_vars, new_card, new_table)
    return newpot, new_state
