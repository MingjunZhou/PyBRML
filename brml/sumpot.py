#File:  sumpot.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-08-16
#License: GNU License
#Description:

import numpy as np
from .potential import potential
from ismember import ismember


def sumpot(pots, variables=None, sumover=1):
    """Sum(marginalise) a potential over variables.
        pots = sumpot(pots)
        pots = sumpot(pots, variables)
        pots = sumpot(pots, variables, sumover)

    If called with the additional argument: sumpot(pot, variables, sumover).
    If sumover=1 then potential is summed over variables, otherwise the
        potential is summed over everything except variables.
    If called as sumpot(pot), it is assumed that all variables of potential
        are to be summed over.

    Args:
        pots: A list of potentials.
        variables:(Optional) A np.array of variables to be summed(marginalized)
                    over.
        sumover:(Optional) If sumover=1 then potential is summed over
                variables, otherwise potential is summed over everything
                except variables.

    Returns:
        pots: If pots is one np.array, returns the new pots after
                marginalization.
              If pots is a list of potentials, returns the new pots list.

    Raises:
        None
    """
    if isinstance(pots, potential):
        pots = [pots]
    else:
        pots = list(pots)

    if variables is None:
        variables = []
    variables = np.array(variables)

    """
    if len(pots) == 1:
        dummy, pv_in_v, all_pv_in_v = ismember(pots[0].variables, variables)
        diff = dummy == False

        if sumover == 1:
            newvariables = pots[0].variables[dummy]
        else:
            newvariables = pots[0].variables[diff]
            diff = dummy
            
        dummy, v_in_pv, all_v_in_pv = ismember(newvariables,
                                                   pots[0].variables)

        pots[0].variables = pots[0].variables[diff]
        pots[0].card = pots[0].card[diff]
        pots[0].table = np.apply_over_axes(np.sum, pots[0].table, v_in_pv)
        pots[0].table = pots[0].table.reshape(pots[0].card)
    elif len(pots) > 1:
        for pot in pots:
            dummy, pv_in_v, all_pv_in_v = ismember(pot.variables, variables)
            diff = dummy == False

            if sumover == 1:
                newvariables = pot.variables[dummy]
            else:
                newvariables = pot.variables[diff]
                diff = dummy
                
            dummy, v_in_pv, all_v_in_pv = ismember(newvariables,
                                                       pot.variables)

            pot.variables = pot.variables[diff]
            pot.card = pot.card[diff]
            pot.table = np.apply_over_axes(np.sum, pot.table, v_in_pv)
            pot.table = pot.table.reshape(pot.card)
    """
    newpots = [potential() for i in range(len(pots))]
    for i, pot in enumerate(pots):
        dummy, pv_in_v, all_pv_in_v = ismember(pot.variables, variables)
        diff = dummy == False

        if sumover == 1:
            newvariables = pot.variables[dummy]
        else:
            newvariables = pot.variables[diff]
            diff = dummy
        
        dummy, v_in_pv, all_v_in_pv = ismember(newvariables,
                                               pot.variables)

        newpots[i].variables = pot.variables[diff]
        newpots[i].card = pot.card[diff]
        newpots[i].table = np.apply_over_axes(np.sum, pot.table, v_in_pv)
        newpots[i].table = newpots[i].table.reshape(newpots[i].card)

    if len(pots) == 1:
        return newpots[0]
    else:
        return newpots
