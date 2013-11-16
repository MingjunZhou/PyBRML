#File :  istree_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-12
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.istree import istree


class IstreeTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        tree, eli, sch = istree(adj)
        tree_ans = False
        eli_ans = []
        sch_ans = np.array([[], []])
        assert np.allclose(tree_ans, tree)
        assert np.allclose(eli_ans, eli)
        assert np.allclose(sch_ans, sch)

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        tree, eli, sch = istree(adj)
        tree_ans = False
        eli_ans = []
        sch_ans = []
        assert np.allclose(tree_ans, tree)
        assert np.allclose(eli_ans, eli)
        assert np.allclose(sch_ans, sch)

    def test_case3(self):
        adj = np.array([[0, 0, 1.2, 1.4, 0, 0, 0], [0, 0, 0, 5.1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3.1, 4.2],
                        [0, 0, 0, 0, 0, 0, 1.0], [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]])
        tree, eli, sch = istree(adj)
        tree_ans = True
        eli_ans = [1, 2, 0, 4, 5, 3, 6]
        sch_ans = [[1, 3], [2, 0], [0, 3], [4, 6], [5, 3], [3, 6]]
        assert np.allclose(tree_ans, tree)
        assert np.allclose(eli_ans, eli)
        assert np.allclose(sch_ans, sch)

    def test_case4(self):
        adj = np.array([[0, 0, 1.2, 1.4, 0, 0, 0, 0, 0],
                        [0, 0, 0, 5.1, 0.2, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 3.1, 4.2, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 2.3],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0.5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        tree, eli, sch = istree(adj)
        tree_ans = True
        eli_ans = [2, 0, 4, 1, 5, 3, 6, 7, 8]
        sch_ans = [[2, 0], [0, 3], [4, 1], [1, 3],
                   [5, 3], [3, 6], [6, 8], [7, 8]]
        assert np.allclose(tree_ans, tree)
        assert np.allclose(eli_ans, eli)
        assert np.allclose(sch_ans, sch)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(IstreeTestCase("test_case1"))
    suite.addTest(IstreeTestCase("test_case2"))
    suite.addTest(IstreeTestCase("test_case3"))
    suite.addTest(IstreeTestCase("test_case4"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
