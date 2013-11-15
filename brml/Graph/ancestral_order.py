#File :  ancestral_order.py
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
    noparents_vars = np.array([], dtype=int)
    while len(order) < n_node:
        for i in range(n_node):
            nochildren = newadj[i, :].nonzero()[0].size == 0
            noparents = newadj[:, i].nonzero()[0].size == 0
            noparentsA = adj[:, i].nonzero()[0].size == 0
            if noparentsA:
                noparents_vars = np.unique(np.concatenate((noparents_vars, [i])))
            if not (noparents and nochildren):
                if nochildren:
                    newadj[:, i] = 0
                    order.append(i)
                    done[i] = 1
        if np.all(done):
            break
        rest = np.setdiff1d(np.arange(n_node), done.nonzero()[0])
        if newadj[:, rest].nonzero()[0].size == 0:
            break
    order = np.concatenate((order, rest))[::-1]
    return order, noparents_vars
