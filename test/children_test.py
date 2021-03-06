#File :  children_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-12
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.children import children


class ChildrenTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        c = children(0, adj)
        ans = np.array([1, 2])
        assert np.allclose(ans, c)

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        c = children([0, 2], adj)
        ans = np.array([1, 2, 3])
        assert np.allclose(ans, c)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ChildrenTestCase("test_case1"))
    suite.addTest(ChildrenTestCase("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
