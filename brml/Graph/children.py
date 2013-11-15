#File :  children.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-14
#License : BSD 3 clause
#Description :


import numpy as np
import collections

def children(x, adj):
    if isinstance(x, collections.Sequence):
        c = np.array([], dtype=int)
        for i in x:
            t, = adj[i, :].nonzero()
            #if not t:
            #    t = []
            #else:
            #    t = t[0]
            c = np.concatenate((c, t))
    else:
        c, = adj[x, :].nonzero()
        #if not c:
        #    c = []
        #else:
        #    c = c[0]
    c = np.unique(c)
    return c
