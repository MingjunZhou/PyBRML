#File :  edges.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-14
#License : BSD 3 clause
#Description :


import numpy as np


def edges(adj):
    """Return edge list (excluding self edges) from adjacency matrix adj and
    associated non-zero edge weights.

    Parameters :
        adj : np.ndarray, shape = [n_nodes, n_nodes] :
            The adjacency matrix.

    Returns :
        e : np.ndarray, shape = [n_edges, 2] :
            n_edges entries in this array, each entry containes the head and
            tail node number.

        weight : np.ndarray, shape = [n_edges, ] :
            weight[i] is the weight of edge e[i].

    Raises :
        None

    Notes :
        e, weight = edges(adj)
    """
    adj_new = adj - np.diag(adj)
    edgea, edgeb = adj_new.nonzero()
    e = np.vstack([edgea, edgeb]).transpose()
    weight = adj_new[adj_new != 0]
    return e, weight
