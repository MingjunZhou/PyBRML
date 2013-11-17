#File :  spantree_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-12
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.spantree import spantree


class SpantreeTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        mst = spantree(adj)
        ans_edges = [(0, 1), (0, 2), (1, 3)]
        assert np.allclose(ans_edges, mst.edges())

    def test_case2(self):
        mst = spantree({0: [1, 2], 1: [3, 4], 2: [4, 5]})
        ans_edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
        assert np.allclose(ans_edges, mst.edges())


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SpantreeTestCase("test_case1"))
    suite.addTest(SpantreeTestCase("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
