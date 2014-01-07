#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause

import numpy as np


def assignment_to_index(assignment, dim):
    """Get the index of the assignment in the full table.

    Parameters :
        assignment : list of int :
            The assignment value to each variable.

        dim : list of int :
            The dimensionality of each variable.

    Returns :
        index : int :
            The index number for the variables with the assignment in the full
            table.

    Raises :
        None

    Notes :
        index = assignment_to_index(assignment, dim)
    """

    I = 0
    for i, a in enumerate(assignment):
        I += a * int(np.prod(dim[i+1:]))
    return I
