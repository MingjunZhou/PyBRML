#File :  cond_indep.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-12-02
#License : BSD 3 clause
#Description :


import numpy as np
from .ancestors import ancestors


def cond_indep(A, X, Y, Z):
    """Conditional Independence test p(X,Y|Z)=p(X|Z)p(Y|Z)?

    Usage :
        cindep = cond_indep(A, X, Y, Z=None)

    Parameters :
        A : array-like, shape: (n_nodes, n_nodes) :
            The adjacency matrix(directed or undirected).

        X : integer :
            The first variable.

        Y : integer :
            The second variable.

        Z : integer; or integer collections; or array-like,
            shape : n_evidences; or empty; optional, default : None :
            The given knowledge(s). Z may be empty.

    Returns :
        cindep : boolean :
            Return True if X and Y are independent givin Z, else return False.

    Raises :
        None

    """
    if not isinstance(A, np.ndarray):
        A = np.array(A)

    if isinstance(X, (int, long)):
        X = np.array([X])
    elif not isinstance(X, np.ndarray):
        X = np.array(X)

    if isinstance(Y, (int, long)):
        Y = np.array([Y])
    elif not isinstance(Y, np.ndarray):
        Y = np.array(Y)

    if Z is None:
        Z = np.array([])
    elif isinstance(Z, (int, long)):
        Z = np.array([Z])
    elif not isinstance(Z, np.ndarray):
        Z = np.array(Z)
    n_nodes = A.shape[0]
    U = np.concatenate((X, Y, Z))
    if np.mean(np.abs(A - A.transpose())) > 0:  # DAG
        # remove non ancestral nodes from the graph
        aset = np.array([])
        for node in U:
            aset = np.union1d(aset, ancestors(node, A))
        rnodes = np.setdiff1d(np.arange(n_nodes), np.concatenate((aset, U)))
        A[rnodes, :] = 0
        A[:, rnodes] = 0
        # moralise the remaining graph
        for i in range(n_nodes):
            parents, = A[:, i].nonzero()
            A[np.ix_(parents, parents)] = 1  # add links between parents

        idx = A + A.transpose() > 0
        A = np.zeros([n_nodes, n_nodes])
        A[idx] = 1.0
        A = A - np.diag(np.diag(A))

    # See if there is a path from X to Y, not via Z:
    # to do this, remove Z from the graph:
    A[Z, :] = 0
    A[:, Z] = 0
    # now find the connections between X and Y
    A = A + np.eye(n_nodes)
    newA = np.eye(n_nodes)
    for i in range(n_nodes):
        newA = np.dot(newA, A)
    idx = newA > 0
    A = np.zeros([n_nodes, n_nodes])
    A[idx] = 1
    A = A - np.diag(np.diag(A))
    cindep = False
    final_idxs, = A[X, Y].nonzero()
    if final_idxs.size == 0:
        cindep = True
    return cindep
