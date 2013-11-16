#File :  neighbour_size.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-16
#License : BSD 3 clause
#Description :


import numpy as np


def neighbour_size(adj, node=None):
    if isinstance(node, int):
        node = [node]
    if node is None:
        return np.sum(adj != 0, axis=0)
    else:
        return np.sum(adj[:, node] !=0, axis=0)
