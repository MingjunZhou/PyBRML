#File :  cond_indep_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-19
#License : BSD 3 clause
#Description :

import unittest
import scipy.io
import sys
sys.path.append("..")
from brml.Potential import Potential
from brml.Graph.cond_indep import cond_indep
from brml.Graph.dag import dag


class CondIndepTestCase(unittest.TestCase):
    def setUp(self):
        mat = scipy.io.loadmat('../data/chestclinic.mat')
        pots_list = mat['pot'][0]
        allpots = []
        for pot in pots_list:
            variables = pot[0][0]
            table = pot[1]
            if table.shape[0] == 1:
                card = [table.shape[1]]
                table = table[0]
            else:
                card = table.shape
                l_var = len(variables)
                if l_var > 2:
                    card = table.shape
            allpots.append(Potential(variables, card, table))
        self.A = dag(allpots)

    def test_case1(self):
        X = [0, 3]
        Y = [1]
        Z = [2, 4]
        assert cond_indep(self.A, X, Y, Z) is False

    def test_case2(self):
        X = [5]
        Y = [6]
        Z = [7]
        assert cond_indep(self.A, X, Y, Z) is True

    def test_case3(self):
        X = [1]
        Y = [7]
        Z = [3]
        assert cond_indep(self.A, X, Y, Z) is True

    def test_case4(self):
        X = [1]
        Y = [7]
        Z = [3, 6]
        assert cond_indep(self.A, X, Y, Z) is False


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CondIndepTestCase("test_case1"))
    suite.addTest(CondIndepTestCase("test_case2"))
    suite.addTest(CondIndepTestCase("test_case3"))
    suite.addTest(CondIndepTestCase("test_case4"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
