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
import matplotlib.pyplot as plt


class DrawLayoutTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        draw_layout(adj, layout='spring', node_type=[1, 1, 1, 1])
        plt.show()

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        draw_layout(adj)
        plt.show()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(DrawLayoutTestCase("test_case1"))
    suite.addTest(DrawLayoutTestCase("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
