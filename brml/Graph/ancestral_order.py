#File :  ancestralorder.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-14
#License : BSD 3 clause
#Description :


import numpy as np


def ancestral_order(adj):
    """Return the ancestral order of the DAG adj (oldest first)"""
    n_node = adj.shape[0]
    newadj = np.array(adj)
    done = np.zeros(n_node, dtype=int)
    order = []
    noparents_vars = []
    while len(order) < n_node:
        for i in range(n_node):
            nochildren = newadj[i, :].nonzero()[0].size == 0
            noparents = newadj[:, i].nonzero()[0].size == 0
            noparentsA = adj[:, i].nonzero()[0].size == 0
            if noparentsA:
                noparents_vars.append(i)
                noparents_vars = np.unique(noparents_vars)
            if not (noparents and nochildren):
                if nochildren:
                    newadj[:, i] = 0
                    order.append(i)
                    done[i] = 1
        if np.all(done):
            break
        rest = np.setdiff1d(np.arange(n_node)

