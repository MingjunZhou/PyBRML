#File :  ancestors.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-13
#License : BSD 3 clause
#Description :


import numpy as np
from .parents import parents
import collections


def ancestors(x, adj):
    """Find the ancestors of a node x in a DAG adj.

    Parameters :
        x : int :
            The node.

        adj : np.ndarray[n_node, n_node] :
            Adjacency matrix.

    Returns :
        a : np.ndarray[n_a, ] :
            Ancestors of x.

    Raises :
        None

    Notes :
        a = maxpot(pot, invariables)
    """
    if not isinstance(adj, np.ndarray):
        adj = np.array(adj)

    done = False
    a = parents(x, adj)
    while not done:
        aold = a
        a = np.union1d(a, parents(a, adj))
        done = np.setdiff1d(a, aold).size == 0
    if not isinstance(x, collections.Sequence):
        a = np.setdiff1d(a, np.array([x]))
    else:
        a = np.setdiff1d(a, x)
    return a
