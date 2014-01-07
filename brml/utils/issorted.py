#File:  issorted.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-08-17
#License: BSD 3 Clause
#Description: Is the variables field in the Potential is sorted(low to high)?

import numpy as np


def issorted(pot, variables=[]):
    """Check whether the variables in the Potential is sorted.

    Parameters :
        pot : Potential :
            The target potential.

        variables : sequence[n_variables, ] or np.ndarray[n_variables, ], optional, default : None :
            The sorted sequence of variables to be compared with.

    Returns :
        issorted : boolean :
            True for pot is sorted, False otherwise.

    Raises :
        None

    Notes :
        If variables is not None, compare the variables of the pot with the
        given variables.
    """
    if variables is None:
        variables = np.array([])
    else:
        variables = np.array(variables)
    originVar = pot.variables
    if np.size(variables) == 0:
        return np.equal(np.sort(originVar), originVar)
    else:
        return np.equal(originVar, variables)
