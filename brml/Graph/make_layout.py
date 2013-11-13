#File :  make_layout.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-11
#License : BSD 3 clause
#Description :


import networkx as nx
from networkx.algorithms.dag import topological_sort
import numpy as np
from .poset import poset


def make_layout(adj, g=None, gtype='directed'):
    """Creates a layout from an adjacency matrix.

    Usage :
        x, y = make_layout(adj<, g, gtype='directed'>)

    Parameters :
        adj : integer nd.ndarray[n_node, n_node] :
            Adjacency matrix.

        g : nx.DiGraph or nx.Graph, optional, default : None :
            If g is None, use adj to generate the graph.

        gtype : 2-value string, optional, default: 'directed' :
            'directed' if g is directed, 'undirected' if g is undirected.

    Returns :
        x : 1-d nd.ndarray[n_node] :
            X Positions of nodes.
        
        y : 1-d nd.ndarray[n_node] :
            Y Positions of nodes.

    Raises :
        None

    """
    n_node = adj.shape[0]
    if g is None:
        if gtype == 'directed':
            g = nx.DiGraph(adj)
        else:
            g = nx.Graph(adj)

    try:
        seq = topological_sort(g)
    except (nx.NetworkXError, nx.NetworkXUnfeasible):
        seq = []
    if not seq:  # seq is empty
        level = poset(adj, 0) - 1
    else:  # not empty
        level = np.zeros(n_node, dtype=int)
        for node in seq:
            idx = adj[:, node].nonzero()[0]
            if idx.size != 0:
                l = np.max(level[idx])
                level[node] = l + 1
    y = (level + 1.0) / (np.max(level) + 2.0)
    y = 1.0 - y
    x = np.zeros(y.size, dtype=float)
    for i in range(np.max(level)):
        idx = (level == i).nonzero()[0]
        offset = (i % 2 - 0.5) / 10.0
        x[idx] = 1.0 * np.arange(idx.size) / (idx.size + 1) + offset
        #offset = 0.1
        #n_idx = idx.size 
        #for j, index in enumerate(idx):
        #    x[index] = offset * ( j - (n_idx - 1.0) / 2.0) 
    
    return x, y
