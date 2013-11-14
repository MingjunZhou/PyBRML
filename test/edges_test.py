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
from brml.Graph.edges import edges


class EdgesTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        e, w = edges(adj)
        e_ans = np.array([[0, 1], [0, 2], [1, 0], [1, 2], [1, 3],
                          [2, 0], [2, 1], [2, 3], [3, 1], [3, 2]])
        w_ans = np.ones(10) 
        assert np.allclose(e_ans, e)
        assert np.allclose(w_ans, w)

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        e, w = edges(adj)
        e_ans = np.array([[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]])
        w_ans = np.ones(5)
        assert np.allclose(e_ans, e)
        assert np.allclose(w_ans, w)

    def test_case3(self):
        adj = np.array([[0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]])
        e, w = edges(adj)
        e_ans = np.array([[0, 2], [0, 3], [1, 3], [3, 5], [3, 6], [4, 6]])
        w_ans = np.ones(6)
        assert np.allclose(e_ans, e)
        assert np.allclose(w_ans, w)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(EdgesTestCase("test_case1"))
    suite.addTest(EdgesTestCase("test_case2"))
    suite.addTest(EdgesTestCase("test_case3"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
