#!/usr/bin/env python

"""
tf: TRUE or FALSE
index: the index for each A in B
A[tf] == B[index]
"""
import numpy as np


if __name__ == "__main__" and __package__ is None:
    __package__ = "utils.ismember"


def ismember(a, b):
    """True for set member.
    LIA, LOCB_CUT, LOCB = ismember(a, b).
    a[tf] == b[index[index>=0]]

    Args:
        a: An 1-d nd.array.
        b: An 1-d nd.array.

    Returns:
        LIA: An 1-d nd.array.
            For arrays A and B returns an array of the same size as A
            containing true where the elements of A are in B and false
            otherwise.
        LOCB_CUT: An 1-d nd.array.
                    LOCB_CUT = LOCB[LOCB>=0]
        LOCB: An 1-d nd,array
                returns an array LOCB containing the highest absolute index in
                B for each element in A which is a member of B and -1 if there
                is no such index

    Raises:
        None
    """

    aa = a
    a = np.array(a)
    b = np.array(b)
    if a.ndim != b.ndim:
        a = np.array([aa])
    tf = np.in1d(a, b)  # for newer versions of numpy(v1.4+)
    index = np.array([(np.where(b == i))[0][-1] if t else -1
                     for i, t in zip(a, tf)])
    return tf, index[index >= 0], index
