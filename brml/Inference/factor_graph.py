#File : factor_graph.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-12-23
#License : BSD 3 clause
#Description :

import numpy as np
from ..Potential import potvariables


def factor_graph(pots):
    """Returns a factor graph adjacency matrix based on the given set of
    potentials.

    Usage :
        A = factor_graph(pots)

    Parameters :
        pots : sequence[n_pots, ] :
            This set of potentials make up the graph.

    Returns :
        A : nd.array[V+F, V+F] :
            The adjacency matrix of the factor graph.

    Raises :
        None

    Notes :
        The size of A is equal to (V+F)*(V+F) where V are the total number of
        variables and F the total number of factors. A[0:V-1, 0:V-1] are empty;
        A[0:V-1, V:] contains the variabe to factor message indices and A[V:,
        0:V-1] contains the factor to variable message indices. If the set of
        potentials is not singly-connected, all message indices are -1.

        A[i, j] = k means that message number k is from FGnodei -> FGnodej.
        Going through the messages in sequence corresponds to a valid forward-
        backward procedure over all variable nodes in the Factor Graph. See
        also factor_connecting_variable, variable_connecting_factor. Note that
        the variables in pot must be numbered 0, 1, 2, ...

        See also demoSumProd, squeeze_pots.
    """
    F = len(pots)
    pass
