#File :  draw_layout_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-12
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.ancestors import ancestors


class AncestorsTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        p = ancestors(0, adj)
        ans = np.array([1, 2, 3])
        assert np.allclose(ans, p)

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        p = ancestors([0, 2], adj)
        ans = np.array([1])
        assert np.allclose(ans, p)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AncestorsTestCase("test_case1"))
    suite.addTest(AncestorsTestCase("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
