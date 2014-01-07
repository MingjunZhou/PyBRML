#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import numpy as np


def index_to_assignment(index, dim):
    """Get the assignment values for the entry of the table with the index.

    Parameters :
        index : int :
            The index number of the entry.

        dim : list of int :
            The dimensionality of each variable.

    Returns :
        assignment : list of int :
            The assignment value to each variable.

    Raises :
        None

    Notes :
        assignment = index_to_assignment(index, dim)
    """

    A = []
    for i, d in enumerate(dim):
        A.append(index / int(np.prod(dim[i+1:])))
        index = index % int(np.prod(dim[i+1:]))
    return A
