#File : factor_graph.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-12-23
#License : BSD 3 clause
#Description :

import numpy as np
from scipy.sparse import csr_matrix
from ..Potential import potvariables
from ..Graph import istree


def factor_graph(pots, sparse=True):
    """Returns a factor graph adjacency matrix based on the given set of
    potentials.

    Usage :
        A = factor_graph(pots)

    Parameters :
        pots : sequence[n_pots, ] :
            This set of potentials make up the graph.

        sparse : boolean, optional, default : True
            If sparse == True, return the adj matrix in sparse format,
            otherwise in dense format.

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
        the variables in pot must be numbered 0, 1, 2, ... . Note that message
        number k is 1, 2, 3, 4 ... .

        See also demoSumProd, squeeze_pots.
    """
    F = len(pots)
    variables = potvariables(pots)[0]
    V = len(variables)
    N = V + F
    vnodes = -2 * np.ones((N,), dtype=int)
    vnodes[np.arange(V)] = np.arange(V)
    fnodes = -2 * np.ones((N, ), dtype=int)
    fnodes[np.arange(V, N)] = np.arange(F)
    A = np.zeros((N, N)) 
    for f in range(F):
        FGnodeA, = (fnodes == f).nonzero()
        FGnodeB = pots[f].variables
        A[np.ix_(FGnodeA, FGnodeB)] = 1
        A[np.ix_(FGnodeB, FGnodeA)] = 1
    
    # get a message passing sequence and initialise the messages
    tree, elimseq, forwardschedule = istree(A)
    reverseschedule = np.fliplr(np.flipud(forwardschedule))
    schedule = np.concatenate((forwardschedule, reverseschedule))
    # print "forward:", forwardschedule
    # print "reverse:", reverseschedule
    # print "schedule:",  schedule

    if tree:
        for count in range(len(schedule)):
            # setup the structure for a message from FGnodeA -> FGnodeB
            FGnodeA, FGnodeB = schedule[count, :]
            A[FGnodeA, FGnodeB] = count + 1  # starts from 1, not 0
    else:
        A[A==1] = -1

    if sparse:
        return csr_matrix(A)
    else:
        return A
