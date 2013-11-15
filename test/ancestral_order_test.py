#File :  ancestral_order_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-15
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.ancestral_order import ancestral_order


class ConnectedComponentsTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 0, 1.2, 1.4, 0, 0, 0], [0, 0, 0, 5.1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3.1, 4.1],
                        [0, 0, 0, 0, 0, 0, 1.0], [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]])
        order, noparents_vars = ancestral_order(adj)
        order_ans = np.array([4, 1, 0, 3, 6, 5, 2])
        assert np.allclose(order_ans, order)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ConnectedComponentsTestCase("test_case1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
