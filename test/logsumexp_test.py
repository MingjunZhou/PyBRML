#File :  logsumexp_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-09
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.utils.logsumexp import logsumexp


class CondExpTestCase(unittest.TestCase):
    def test_case1(self):
        out = logsumexp([-1000, -1001, -998], [1, 2, 0.5])
        assert np.allclose(out, -998.308008025)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CondExpTestCase("test_case1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
