#File :  toposort.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-11
#License : BSD 3 clause
#Description :


import numpy as np


def toposort(adj):
    """ A topological ordering of nodes in a directed graph.
    
    Usage :
        seq = toposort(adj)

    Parameters :
        adj : int np.ndarray[n_node, n_node] :
            Adjacency matrix. adj[i, j] == 1 if there exists a directed edge
            from i to j.

    Returns:
        seq : int np.ndarray[n_node] :
            A topological ordered sequence of nodes. Empty if graph contains
            cycles.

    Raises:
        None

    """
    if not isinstance(adj, np.ndarray):
        adj = np.array(adj, dtype=np.int8)

    n_node = adj.shape[0]
    indeg = np.sum(adj, axis=0)
    outdeg = np.sum(adj, axis=1)

    seq = []


