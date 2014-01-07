#File:  sumpots.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-11-02
#License: GNU License
#Description:


def sumpots(pots):
    """Sum Potentials into a single Potential.

    Parameters :
        pots : list of Potentials :
            The target Potentials.

    Returns :
        pot : Potential :
            The sum Potential.

    Raises :
        None

    Notes :
        pot = sumpots(pots)
    """
    newpot = pots[0]
    for j in range(len(pots) - 1):
        if newpot.variables.size != 0 and pots[j + 1].table.size != 0:
            newpot = newpot + pots[j + 1]
        else:
            newpot = pots[j + 1]

    return newpot
