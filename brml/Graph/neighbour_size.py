#File :  neighbour_size.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-16
#License : BSD 3 clause
#Description :


import numpy as np


def neighbour_size(adj, node=None):
    """Compute the size of the neighbours of the node(s).

    Parameters :
        adj : np.ndarray, shape = [n_nodes, n_nodes] :
            The adjacency matrix.

        node : scalar or array-like, optional, default: None :
            If node is None, compute the sum of all the nodes' neighbours.

    Returns :
        s : int :
            The neighbours' _size.

    Raises :
        None

    Notes :
       s = neighbour_size(adj, node=[1, 2])
       s = neighbour_size(adj)
    """
    if isinstance(node, int):
        node = [node]
    if node is None:
        return np.sum(adj != 0, axis=0)
    else:
        return np.sum(adj[:, node] != 0, axis=0)
