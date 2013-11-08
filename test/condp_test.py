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
from brml.utils.condp import condp


class CondPTestCase(unittest.TestCase):
    def test_case1(self):
        array = np.array([[1, 1, 2], [2, 3, 4], [3, 2, 1]])
        #max_val, max_state = max_array(array, [0, 2], return_states=True)
        cond_array = condp(array, [0])
        ans = np.array([[0.1666667, 0.1666667, 0.2857143],
                        [0.3333333, 0.5000000, 0.5714286],
                        [0.5000000, 0.3333333, 0.1428571]])
        #print "max_state=", max_state
        assert np.allclose(ans, cond_array)

    def test_case2(self):
        array = np.arange(24) + 1
        array = array.reshape([2, 3, 4])
        cond_array = condp(array, [1])
        ans = np.array([[[0.06666667, 0.11111111, 0.14285714, 0.16666667],
                         [0.33333333, 0.33333333, 0.33333333, 0.33333333],
                         [0.60000000, 0.55555556, 0.52380952, 0.50000000]],
                        [[0.25490196, 0.25925926, 0.26315789, 0.26666667],
                         [0.33333333, 0.33333333, 0.33333333, 0.33333333],
                         [0.41176471, 0.40740741, 0.40350877, 0.40000000]]])
        assert np.allclose(ans, cond_array)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CondPTestCase("test_case1"))
    suite.addTest(CondPTestCase("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
