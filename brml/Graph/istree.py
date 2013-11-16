#File :  istree.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-16
#License : BSD 3 clause
#Description :


import numpy as np
from .neighbour_size import neighbour_size


def istree(adj, root=-1):
    """Check if graph is singly-connected (a polytree).

    Usage :
        tree, elimseq, schedule = istree(adj, root=0)

    Parameters :
        adj : array-like :
            Adjacency matrix(directed or undirected).

        root : int, optional, default : -1 :
            Root node.

    Returns :
        tree : boolean :
            True if graph is singly connected, otherwise tree = False.

        elimseq : int sequence :
            A variable elimination sequence in which simplical nodes of the
            tree are listed, as each simplical node is removed from the tree.

        schedule : int sequence :
            The sequence of messages from node to node corresponding to
            elimseq.

    Raises :
        None

    Notes :
        If adj is directed, the elimination schedule begins with the nodes
        with no children.
        If root is specified, the last node eliminated is root.
        If the graph is connected and the number of edges is less than the
        number of nodes, it must be a tree.
        However, to deal with the general case in which it is unknown if the
        graph is connected we check using elimination.
        A tree/singly-connected graph must admit a recursive simplical node
        elimination. That is at any stage in the elimination there must be a
        node with either zero or 1 neighbour in the remaining graph.

    """
    n_node = adj.shape[0]
    schedule = np.zeros([n_node, 2], dtype=int)
    tree = True
    newadj = adj + adj.transpose()
    elimseq = []
    for node in range(n_node):
        # now find the number of neighbours
        nn = (n_node + 1) * np.ones(n_node)  # ensures that we don't pick
                                             # eliminated nodes
        s = np.arange(n_node)
        r = np.zeros(n_node, dtype=int)
        r[elimseq] = 1
        s = s[r == 0]
        nn[s] = neighbour_size(newadj.transpose(), s)
        if root >= 0:
            nn[root] = n_node + 1
        elim = np.argmin(nn)
        neigh, = newadj[:, elim].nonzero()
        if neigh.size > 1:
            tree = False
            break
        newadj[elim, :] = 0
        newadj[:, elim] = 0
        elimseq.append(elim)
        if neigh.size == 0:
            schedule[node, :] = elim
        else:
            schedule[node, 0] = elim
            schedule[node, 1] = neigh

    if not tree:
        elimseq = []
    # remove any self-elimination
    schedule = schedule[schedule[:, 0] != schedule[:, 1], :]
    if schedule.shape[0] == 0:
        schedule = np.array([[], []])
    return tree, elimseq, schedule
