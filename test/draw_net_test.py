#File :  draw_net_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-12
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.draw_net import draw_net
import matplotlib.pyplot as plt

class DrawNetTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 1], [0, 1, 1, 0]])
        draw_net(adj)
        plt.show()

    def test_case2(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 1, 1],
                        [0, 0, 0, 1], [0, 0, 0, 0]])
        draw_net(adj)
        plt.show()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(DrawNetTestCase("test_case1"))
    suite.addTest(DrawNetTestCase("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
