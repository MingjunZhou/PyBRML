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
from brml.utils.max_array import max_array


class MaxArrayTestCase(unittest.TestCase):
    def test_case1(self):
        array = np.arange(24)
        array = array.reshape([2, 3, 4])
        #max_val, max_state = max_array(array, [0, 2], return_states=True)
        max_val = max_array(array, [0, 2])
        ans = np.array([15, 19, 23])
        #print "max_state=", max_state
        assert np.allclose(ans, max_val)
    
    def test_case2(self):
        array = np.arange(24)
        array = array.reshape([2, 3, 4])
        max_val, max_state = max_array(array, [2], return_states=True)
        #max_val = max_array(array, [2])
        #print "max_val=", max_val
        ans = np.array([[3, 7, 11], [15, 19, 23]])
        #print "max_state=", max_state
        assert np.allclose(ans, max_val)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MaxArrayTestCase("test_case1"))
    suite.addTest(MaxArrayTestCase("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
