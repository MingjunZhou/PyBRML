#!/usr/bin/env python

"""
% ndx = subv2ind(siz,sub)
%
"""
import numpy as np


def subv2ind(siz, sub):
    """Legacy code. Please check doc for assignment_to_index.

    Notes :
        state to index : return the linear index of a state vector sub based
        on an array of size siz.
        If sub is a matrix, each row is taken as a state vector and the linear
        index returned in the corresponding row of ndx.
    """
    k = np.array([0])
    k = np.append(k, np.cumprod(siz[0:-1]))
    ndx = sub * k.T - k.sum()
    return ndx
