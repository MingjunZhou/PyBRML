#File :  edges.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-14
#License : BSD 3 clause
#Description :


import numpy as np


def edges(adj):
    """Return edge list (excluding self edges) from adjacency matrix adj and
    associated non-zero edge weights."""
    adj_new = adj - np.diag(adj)
    edgea, edgeb = adj_new.nonzero()
    e = np.vstack([edgea, edgeb]).transpose()
    weight = adj_new[adj_new != 0]
    return e, weight
