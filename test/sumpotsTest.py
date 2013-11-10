#File:  sumpotTest.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-08-17
#License: BSD 3 Clause
#Description:


import unittest
import sys
sys.path.append("..")
from brml.Potential import sumpots
from brml.Potential import Potential
import numpy as np
from brml.Potential import assert_two_pots


class sumpotsTestCase(unittest.TestCase):
    def setUp(self):
        self.pot = Potential()
        self.pot.variables = np.array([3, 2, 1])
        self.pot.card = np.array([2, 3, 4])
        self.pot.table = np.arange(0, 24).reshape(2, 3, 4)

    def tearDown(self):
        self.pot = None

    def test_two_pots_sum(self):
        pot_a = Potential([1], [2], [0.1, 0.9])
        pot_b = Potential([2], [2], [0.3, 0.7])
        pot_c = Potential([2, 4], [2, 3], [[0.1, 0.2, 0.2], [0.3, 0.1, 0.1]])
        n = sumpots([pot_a, pot_b, pot_c])
        ans = Potential([1, 2, 4], [2, 2, 3], [[[0.5, 0.6, 0.6],\
                                                [1.1, 0.9, 0.9]],\
                                               [[1.3, 1.4, 1.4],\
                                                [1.9, 1.7, 1.7]]])
        assert_two_pots(n, ans)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(sumpotsTestCase("test_two_pots_sum"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
