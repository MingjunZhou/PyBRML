#File :  parents.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-13
#License : BSD 3 clause
#Description :


import numpy as np
import collections

def parents(x, adj):
    """Parents of a node given an adjacency matrix."""
    if not isinstance(adj, np.ndarray):
        adj = np.array(adj)
    if isinstance(x, (collections.Sequence, np.ndarray)):
        p = np.array([], dtype=int)
        for i in x:
            t, = adj[:, i].nonzero()
            #if not t:
            #    t = []
            #else:
            #    t = t[0]
            p = np.concatenate((p, t))
    #elif x:
    #    p = np.array([])
    else:
        p, = adj[:, x].nonzero()
        #if not p:
        #    p = []
        #else:
        #    p = p[0]
    p = np.unique(p)
    return p
