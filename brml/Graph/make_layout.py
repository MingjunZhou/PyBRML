#File :  make_layout.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-11
#License : BSD 3 clause
#Description :


import networkx as nx
from networkx.algorithms.dag import topological_sort
import numpy as np


def make_layout(adj, g=None, gtype='directed'):
    """Creates a layout from an adjacency matrix.

    Usage :
        coord = make_layout(adj<, g, gtype='directed'>)

    Parameters :
        adj : integer nd.ndarray[n_node, n_node] :
            Adjacency matrix.

        g : nx.DiGraph or nx.Graph, optional, default : None :
            If g is None, use adj to generate the graph.

        gtype : 2-value string, optional, default: 'directed' :
            'directed' if g is directed, 'undirected' if g is undirected.

    Returns :
        coord : 2-d nd.ndarray[n_node, 2] :
            Positions of nodes.

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
    except nx.NetworkXUnfeasible:
        seq = []

    if not seq:  # seq is empty
        level = poset(adj)' + 1
