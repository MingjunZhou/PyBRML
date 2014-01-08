#File :  connected_components.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-15
#License : BSD 3 clause
#Description :


import numpy as np
from scipy import sparse


def connected_components(adj):
    """Find the connected components in an undirected graph

    Parameters :
        adj : array-like, shape = [n_nodes, n_nodes] :
            A dense matrix or rank-2 ndarray.

    Returns :
        cluster : np.ndarray, shape = [n_cc, ] :
            The connected components in the graph.

    Raises :
        None

    Notes :
        cluster = connected_components(adj)
    """
    A = sparse.csr_matrix(adj)
    n_node = A.shape[0]
    A = A + A.transpose()
    newA = A + sparse.eye(n_node, n_node)
    connected = A + sparse.eye(n_node, n_node)
    cl = 0
    cluster = np.zeros(n_node, dtype=int)
    for i in range(n_node - 1):
        connected = np.dot(connected, newA)
    for i in range(n_node):
        vars, redun = connected[:, i].nonzero()
        if vars.size != 0:
            cl += 1
            cluster[vars] = cl
            for var1 in vars:
                for var2 in vars:
                    connected[var1, var2] = 0
    return cluster
