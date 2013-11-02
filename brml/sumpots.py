#File:  sumpots.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-11-02
#License: GNU License
#Description:

import numpy as np
from .potential import potential


def sumpots(pots):
    """Sum potentials into a single potential.
        pot = sumpots(pots)

    Args:
        pots: A list of potentials.

    Returns:
        pot: Return the sum of all the potentials.

    Raises:
        None
    """

    
