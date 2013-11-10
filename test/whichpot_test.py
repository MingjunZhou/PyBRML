#File :  max_array_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-07
#License : BSD 3 clause
#Description :


import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Potential import Potential, whichpot


class WhichPotTestCase(unittest.TestCase):
    def test_case1(self):
        pot1 = Potential()
        pot2 = Potential()
        pot3 = Potential()
        pot4 = Potential()
        pot1.variables = [0, 1]
        pot2.variables = [0, 1, 3, 4]
        pot3.variables = [0, 1, 4, 5]
        pot4.variables = [1, 2, 3, 4]
        pot_num = whichpot([pot2, pot1, pot3, pot4], [1, 0])
        ans = [1, 0, 2]
        assert np.allclose(pot_num, np.array(ans))

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(WhichPotTestCase("test_case1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
