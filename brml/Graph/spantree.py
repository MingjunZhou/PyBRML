#File :  spantree.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-17
#License : BSD 3 clause
#Description :


import networkx as nx
import numpy as np


def spantree(adjacency):
    """Return a spanning tree from an undirected graph represented by an
    adjacency list or matrix.

    Usage :
        mst = spantree([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        mst = spantree({0 : [1, 2], 1 : [3, 4], 2 : [4,5]})

    Parameters :
        adjacency : array-like or dict :
            It's array-like for the adjacency matrixm, or a dict for the
            adjacency list.

    Returns :
        mst : networkx.Graph :
            A minimum spanning tree or forest.

    Raises :
        None

    """
    g = nx.Graph(adjacency)
    return nx.algorithms.mst.minimum_spanning_tree(g)
