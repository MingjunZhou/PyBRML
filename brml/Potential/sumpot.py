#File:  sumpot.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-08-16
#License: BSD 3 clause 
#Description:

import numpy as np
from .Potential import Potential
from ..utils.ismember import ismember


def sumpot(pots, variables=None, sumover=1):
    """Sum(marginalise) a Potential over variables.

    Parameters :
        pots : Potential :
            A list of Potentials.
        
        variables : np.ndarray[n_variables,], optional, default : None :
            Variables to be summed(marginalized) over.

        sumover : int, optional, default : 1 :
            If sumover=1 then Potential is summed over variables, otherwise
            Potential is summed over everything except variables.

    Returns:
        pots: sequence of Potential :
            If pots is one np.array, returns the new pots after marginalization.
            If pots is a list of Potentials, returns the new pots list.

    Raises:
        None
    
    Notes :
        pots = sumpot(pots)
        pots = sumpot(pots, variables)
        pots = sumpot(pots, variables, sumover)

        If called with the additional argument: sumpot(pot, variables, sumover).
        If sumover=1 then Potential is summed over variables, otherwise the
        Potential is summed over everything except variables.
        If called as sumpot(pot), it is assumed that all variables of Potential
        are to be summed over.

    """
    if isinstance(pots, Potential):
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
    newpots = [Potential() for i in range(len(pots))]
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
