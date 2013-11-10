#File :  isscalar_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-07
#License : BSD 3 clause
#Description :


import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.utils.isscalar import isscalar 


class IsscalarTestCase(unittest.TestCase):
    def test_case1(self):
        assert isscalar(3) == True
        assert isscalar([3]) == True
        assert isscalar([3, 1]) == False
        assert isscalar((3.1)) == True
        assert isscalar((3.0, 1.0)) == False
        assert isscalar(np.array(3)) == True
        assert isscalar(np.array([3.0])) == True
        assert isscalar(np.array([3, 1, 2])) == False 



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(IsscalarTestCase("test_case1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
