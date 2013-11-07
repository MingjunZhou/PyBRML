#File :  normpot.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-07
#License : BSD 3 clause
#Description :

import numpy as np


def norm_matrix(m):
    eps = np.finfo(float).eps
    m = m + eps
    mnew = m / np.sum(m)
    return mnew

if __name__ == "__main__":
    ma = np.array([0, 0, 0])
    ma = norm_matrix(ma)
    print ma
    ma = np.array([[1, 2, 3], [3, 4, 5]])
    ma = norm_matrix(ma)
    print ma
