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
from brml.Graph.neigh import neigh


class NeighTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        n = neigh(0, adj)
        ans = np.array([1, 2])
        assert np.allclose(ans, n)

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        n = neigh([0, 2], adj)
        ans = np.array([1, 3])
        assert np.allclose(ans, n)

    def test_case3(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        n = neigh([0, 2], adj, rtype='set')
        ans = [np.array([1, 2]), np.array([0, 1, 3])]
        assert np.allclose(ans[0], n[0])
        assert np.allclose(ans[1], n[1])

    def test_case4(self):
        adj = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0],
                        [0, 0, 0, 1, 0], [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]])
        n = neigh([0, 2, 4], adj, rtype='set')
        ans = [np.array([1, 2]), np.array([0, 1, 3]), np.array([])]
        assert np.allclose(ans[0], n[0])
        assert np.allclose(ans[1], n[1])
        assert np.allclose(ans[2], n[2])


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(NeighTestCase("test_case1"))
    suite.addTest(NeighTestCase("test_case2"))
    suite.addTest(NeighTestCase("test_case3"))
    suite.addTest(NeighTestCase("test_case4"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
