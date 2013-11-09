#File :  condexp_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-09
#License : BSD 3 clause
#Description :


import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.utils.condexp import condexp


class CondExpTestCase(unittest.TestCase):
    def test_case1(self):
        array = np.array([[0.1666667, 0.1666667, 0.2857143],
                        [0.3333333, 0.5000000, 0.5714286],
                        [0.5000000, 0.3333333, 0.1428571]])
        cond_array = condexp(array)
        ans = np.array([[0.092973, 0.092973, 0.104727],
                        [0.109835, 0.129755, 0.139362],
                        [0.129755, 0.109835, 0.090786]])
        
        assert np.allclose(ans, cond_array)



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CondExpTestCase("test_case1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
