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
from brml.Graph.draw_layout import draw_layout


class DrawLayoutTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        draw_layout(adj, node_type=[1,1,1,1])
        ans = np.array([1, 2, 2, 3])
        #assert np.allclose(ans, depth)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(DrawLayoutTestCase("test_case1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
