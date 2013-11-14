#File :  neigh.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-14
#License : BSD 3 clause
#Description :


import numpy as np
import collections


def neigh(v, adj, rtype='union'):
    """Find the neighbours of a vertex v on an undirected graph with
     adjacency matrix adj.

    Usage :
        n = neigh(adj, v, rtype='set')

    Parameters :
        adj : array-like :
            Undirected adjacency matrix.

        v : int or sequence :
            The target node(s).

        rtype : string, optional, default : 'union' :
            If rtype == 'set', then n[i] contains the neighbours of vertex
            v(i). By default return the union of all neighbours of the nodes.

    Returns :
        n : array-like :
            The neighbours.

    Raises :
        None

    """
    if not isinstance(v, collections.Sequence):
        v = [v]
    if rtype == 'union':
        n = np.array([], dtype=int)
        for vi in v:
            a = (adj[:, vi] + adj[vi, :]).nonzero()
            if not a:
                a = []
            else:
                a = a[0]
            n = np.concatenate((n, a))
        n = np.unique(np.setdiff1d(n, v))
    else:
        n = []
        for vi in v:
            a = (adj[:, vi] + adj[vi, :]).nonzero()
            if not a:
                a = []
            else:
                a = a[0]
            n.append(np.setdiff1d(a, [vi]))
    return n
