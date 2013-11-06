#File:  sumpots.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-11-02
#License: GNU License
#Description:


def sumpots(pots):
    """Sum potentials into a single potential.
        pot = sumpots(pots)

    Args:
        pots: A list of potentials.

    Returns:
        pot: Return the sum of all the potentials.

    Raises:
        None
    """
    newpot = pots[0]
    for j in range(len(pots)-1):
        if newpot.variables.size != 0 and pots[j+1].table.size != 0:
            newpot = newpot + pots[j+1]
        else:
            newpot = pots[j+1]

    return newpot
