#File :  logsumexp.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-09
#License : BSD 3 clause
#Description :

import numpy as np
from .isscalar import isscalar


def logsumexp(a, b=1):
    """Compute log(sum(exp(a).*b)) for large a.

    Notes :
        logsumexp(a<, b>)
        If b is missing it is assumed to be 1.

        example:
            logsumexp([-1000, 1000, -998], [1,2,0.5])

    """
    if isscalar(b):
        b = b * np.ones(a.shape)
    if not isinstance(a, np.ndarray):
        a = np.array(a, dtype=float)
    if not isinstance(b, np.ndarray):
        b = np.array(b, dtype=float)
    amax = a.flatten(1).max()
    anew = amax + np.log(np.sum(np.exp(a - amax) * b))
    return anew
