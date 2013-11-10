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
    """Dertermine whether the elements in a is also in b.

    idx_in_a_bool, idx_in_b, idx_redundant = ismember(a, b).
    a[idx_in_a_bool] == b[idx_in_b_bool].
    idx_in_b == idx_redundant[idx_redundant >= 0]

    Args:
        a: An 1-d nd.array.
        b: An 1-d nd.array.

    Returns:
        idx_in_a_bool : 1-d nd.array, boolean
            For arrays A and B returns an array of the same size as A
            containing true where the elements of A are in B and false
            otherwise.

        idx_in_b : 1-d nd.array, int
            idx_in_b == idx_redundant[idx_redundant >= 0]

        idx_redundant : 1-d nd,array, int
                returns an array containing the highest absolute index in
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
    idx_in_a_bool = np.in1d(a, b)  # for newer versions of numpy(v1.4+)
    idx_redundant = np.array([(np.where(b == i))[0][-1] if t else -1
                     for i, t in zip(a, idx_in_a_bool)])
    idx_in_b = idx_redundant[idx_redundant >= 0]
    return idx_in_a_bool, idx_in_b, idx_redundant
