#File :  single_parent_tree_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-17
#License : BSD 3 clause
#Description :


import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.single_parent_tree import single_parent_tree


class SingleParentTreeTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        try:
            spt, eli = single_parent_tree(adj)
        except ValueError:
            pass
        else:
            assert False

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 0, 1],
                        [1, 0, 0, 0], [0, 1, 0, 0]])
        spt, eli = single_parent_tree(adj)
        spt_ans = np.array([[0, 1, 1, 0], [0, 0, 0, 1],
                            [0, 0, 0, 0], [0, 0, 0, 0]])
        assert np.allclose(spt_ans, spt)

    def test_case3(self):
        adj = np.array([[0, 0, 1.2, 1.4, 0, 0, 0], [0, 0, 0, 5.1, 0, 0, 0],
                        [1.2, 0, 0, 0, 0, 0, 0], [1.4, 5.1, 0, 0, 0, 3.1, 4.2],
                        [0, 0, 0, 0, 0, 0, 1.0], [0, 0, 0, 3.1, 0, 0, 0],
                        [0, 0, 0, 4.2, 1.0, 0, 0]])
        spt, eli = single_parent_tree(adj)
        spt_ans = np.array([[0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0]])
        assert np.allclose(spt_ans, spt)

    def test_case4(self):
        adj = np.array([[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]])
        spt, eli = single_parent_tree(adj)
        spt_ans = np.array([[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]])
        assert np.allclose(spt_ans, spt)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SingleParentTreeTestCase("test_case1"))
    suite.addTest(SingleParentTreeTestCase("test_case2"))
    suite.addTest(SingleParentTreeTestCase("test_case3"))
    suite.addTest(SingleParentTreeTestCase("test_case4"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
