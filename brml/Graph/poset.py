#File :  poset.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-12
#License : BSD 3 clause
#Description :


import numpy as np


def poset(adj, root):
    """Identify a partial ordering among the nodes of a graph.

    Parameters :
        adj : np.ndarray, shape = [n_nodes, n_nodes] :
            Adjacency matrix.

        root : int :
            Node to start with.

    Returns :
        depth : np.ndarray[n_nodes, ] :
            Depth of the nodes.

    Raises :
        None

    Notes :
        depth = poset(adj, root)
    """
    if not isinstance(adj, np.ndarray):
        adj = np.array(adj)
    n_node = adj.shape[0]
    adj = adj + adj.transpose()
    depth = np.zeros(n_node, dtype=int)
    depth[root] = 1
    queue = [root]

    while queue:
        node = queue.pop(0)
        idx = adj[node, :].nonzero()
        idx2 = (depth[idx] == 0).nonzero()
        idx = np.array(idx[0])
        next_level = idx[idx2]
        for no in next_level:
            queue.append(no)
        depth[next_level] = depth[node] + 1

    return depth
