#!/usr/bin/env python

"""
same as intersect(a,b) in MATLAB
return the intersect set of set1 and set2
"""
import numpy as np
from ismember import ismember


def intersect(a,b):
    a = np.array(a)
    b = np.array(b)
    intersect = np.intersect1d(b,a)
    dummy, iA, alliA = ismember(intersect, a)
    dummy, iB, alliB = ismember(intersect, b)
    return intersect, iA, iB
