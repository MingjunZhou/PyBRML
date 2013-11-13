#File :  parents.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-13
#License : BSD 3 clause
#Description :


import numpy as np
import collections

def parents(x, adj):
    """Parents of anode given an adjacency matrix."""
    if not isinstance(adj, np.ndarray):
        adj = np.array(adj, dtype=int)
    if isinstance(x, collections.Sequence):
        p = np.array([], dtype=int)
        for i in x:
            t = adj[:, i].nonzero()
            if not t:
                t = []
            else:
                t = t[0]
            p = np.concatenate((p, t))
    else:
        p = adj[:, x].nonzero()[0]
    p = np.unique(p)
    return p
