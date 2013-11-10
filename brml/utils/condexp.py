#File : condxexp.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-08
#License : BSD 3 clause
#Description :

import numpy as np
from .condp import condp


def condexp(logp):
    """Compute the conditional distribution of a log-form probability table."""
    logp = logp.astype(float)
    pmax = logp.flatten(1).max()
    logp = logp - pmax
    pnew = condp(np.exp(logp))
    return pnew

