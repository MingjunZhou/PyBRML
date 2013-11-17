#File :  single_parent_tree.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-17
#License : BSD 3 clause
#Description :


import numpy as np
from .children import children
from .connected_components import connected_components
from .istree import istree


def single_parent_connected_tree(Atree, start):
    elimseq = np.array([start], dtype=int)
    n_node = Atree.shape[0]
    spTree = np.array(Atree)
    v = np.zeros(n_node)
    v[start] = 1
    A = Atree + np.eye(n_node)
    kids = children(elimseq.tolist(), spTree)
    spTree[np.ix_(kids, elimseq)] = 0
    while not np.allclose(np.prod(v), 1.0):
        v = np.real(np.inner(A, v) > 0)
        vidx, = v.nonzero()
        nodes = np.setdiff1d(vidx, elimseq)
        elimseq = np.concatenate((elimseq, nodes))
        kids = children(nodes.tolist(), spTree)
        spTree[np.ix_(kids, nodes)] = 0
    return spTree, elimseq


def single_parent_tree(Atree, start=0):
    """From an undirected tree, form a directed tree with at most one parent.

    Usage :
        spTree, elimseq = single_parent_tree(Atree, orient=0)

    Parameters :
        Atree : array-like :
            Adjacency matrix for the tree.

        orient : int, optioanl, default : 0 :
            Several variales to maximise the potential over.

    Returns :
        spTree : array-like :
            Adjacency matrix for the single parent tree.

        elimseq : int sequence :
            Get an elimination elimseq such that each eliminated node has at
            most 1 parent. By default consistently orients away from node 0.

    Raises :
        None

    """
    newAtree = (Atree + Atree.transpose()) > 0
    cc = connected_components(newAtree)
    n_cc = np.max(cc)
    elimseq = np.array([], dtype=int)
    spTree = np.array(Atree)
    for c in range(1, n_cc + 1):
        comp_vars, = (cc == c).nonzero()
        if start > comp_vars.size:
            comp_start = 0
        else:
            comp_start = start
        newcc = newAtree[np.ix_(comp_vars, comp_vars)]
        tree, eli, sch = istree(newcc)
        if not tree:
            raise ValueError("some connected components in the graph is not tree")
        spTree[np.ix_(comp_vars, comp_vars)], comp_elimseq = single_parent_connected_tree(newcc, comp_start)
        elimseq = np.concatenate((elimseq, comp_vars[comp_elimseq]))
    return spTree, elimseq
