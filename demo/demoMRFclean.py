#!/usr/bin/env python

# Python implementation of BRMLtoolbox
# Author: Mingjun Zhou
# License: GNU License

"""
DEMOMRFCLEAN demo of image denoising using a binary state Markov Random Field
"""

print __doc__

import numpy as np
import sys
sys.path.append("..")
from brml.Potential import Potential
