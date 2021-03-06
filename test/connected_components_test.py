#File :  connected_components_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-15
#License : BSD 3 clause
#Description :

import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Graph.connected_components import connected_components


class ConnectedComponentsTestCase(unittest.TestCase):
    def test_case1(self):
        adj = np.array([[0, 0, 1.2, 1.4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3.1, 0],
                        [0, 0, 0, 0, 0, 0, 1.0], [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]])
        cc = connected_components(adj)
        cc_ans = np.array([1, 2, 1, 1, 3, 1, 3])
        assert np.allclose(cc_ans, cc)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ConnectedComponentsTestCase("test_case1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
