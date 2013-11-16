#File :  neighbour_size_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-16
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.neighbour_size import neighbour_size


class NeighbourSizeTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        ns = neighbour_size(adj)
        ans = np.array([2, 3, 3, 2])
        assert np.allclose(ans, ns)

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        ns = neighbour_size(adj, node=0)
        ans = np.array([0])
        assert np.allclose(ans, ns)

    def test_case3(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        ns = neighbour_size(adj, node=[1, 2])
        ans = np.array([1, 2])
        assert np.allclose(ans, ns)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(NeighbourSizeTestCase("test_case1"))
    suite.addTest(NeighbourSizeTestCase("test_case2"))
    suite.addTest(NeighbourSizeTestCase("test_case3"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
