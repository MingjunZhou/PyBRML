#File :  setminus.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version :
#Date : 2013-11-05
#License : BSD 3 clause
#Description :

"""
C=set_minus(A,B)
C is the set A, without the elements B. C preserves the ordering of A

Python:
diff is the set in A without the elemnts B.
"""
import numpy as np
from ismember import ismember


def set_minus(a,b):
	a = np.array(a)
	b = np.array(b)
        dummy, a_in_inter, all_a_in_inter = ismember(a, b)
        diff = a[dummy==False]
        return diff
