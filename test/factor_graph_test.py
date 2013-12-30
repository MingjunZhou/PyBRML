#File : factor_graph_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-12-23
#License : BSD 3 clause
#Description :


import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Inference.factor_graph import factor_graph
from brml.Potential import Potential

class FactorGraphTestCase(unittest.TestCase):
    def test_case1(self):
        a, b, c, d, e = [i for i in range(5)]
        nstates = np.ceil(3 * np.random.random((5,)) + 1)
        nstates = nstates.astype(int)
        pots = []
        variables_list = [[a, b], [b, c, d], [c], [e, d], [d]]
        for variables in variables_list:
            variables = np.array(variables)
            pots.append(Potential(variables, nstates[variables],
                        np.random.random(nstates[variables])))
        # for i, pot in enumerate(pots):
        #    print "pot", i, ':', pot.variables, pot.card, pot.table
        fg = factor_graph(pots)
        fg_dense = fg.todense()
        answer = np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 16, 4, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 6, 14, 0, 0],
                           [0, 0, 0, 0, 0, 0, 12, 0, 11, 9],
                           [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                           [18, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 15, 13, 7, 0, 0, 0, 0, 0, 0],
                           [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 8, 17, 0, 0, 0, 0, 0],
                           [0, 0, 0, 10, 0, 0, 0, 0, 0, 0]])
        assert np.allclose(fg_dense, answer)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(FactorGraphTestCase("test_case1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
