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
    
    if not seq:

    

