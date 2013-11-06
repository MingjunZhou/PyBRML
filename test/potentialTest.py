#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import unittest
import sys
sys.path.append("..")
from brml.Potential import Potential
from brml.Potential.assert_pots import assert_two_pots
import numpy as np
import copy


class PotentialTestCase(unittest.TestCase):
    def setUp(self):
        self.pot = Potential()
        self.pot.variables = np.array([2, 1])
        self.pot.card = np.array([2, 2])
        self.pot.table = np.array([[0.2, 0.6], [0.8, 0.4]])

    def tearDown(self):
        self.pot = None

    def assertTwoPot(self, pa, pb):
        """
        print "\npa.variables:\n", pa.variables
        print "\npb.variables:\n", pb.variables
        print "\npa.card:\n", pa.card
        print "\npb.card:\n", pb.card
        print "\npa.table:\n", pa.table
        print "\npb.table:\n", pb.table
        """
        assert np.allclose(pa.variables, pb.variables)
        assert np.allclose(pa.card, pb.card)
        assert np.allclose(pa.table, pb.table)

    """
    def test_constructor(self):
        newpot = Potential(([2, 1], [2, 2], [[0.2, 0.6], [0.9, 0.4]]))
        assert_two_pots(newpot, self.pot)
    """

    def test_plus_operator(self):
        p = Potential([1], [2], [0.1, 0.9])
        q = Potential([2], [2], [0.3, 0.7])
        n = p + q
        ans = Potential([1, 2], [2, 2], [[0.4, 0.8], [1.2, 1.6]])
        assert_two_pots(n, ans)

    def testMultEmpty(self):
        newpot = self.pot * Potential()
        self.assertTwoPot(newpot, self.pot)
        newpot = None

        newpot = Potential() * self.pot
        self.assertTwoPot(newpot, self.pot)

    def testMult(self):
        otherpot = Potential()
        otherpot.variables = np.array([3])
        otherpot.card = np.array([3])
        otherpot.table = np.array([0.1, 0.4, 0.5])
        answerpot = Potential()
        answerpot.variables = np.array([1, 2, 3])
        answerpot.card = np.array([2, 2, 3])
        answerpot.table = np.array([[[0.02, 0.08, 0.1],
                                     [0.08, 0.32, 0.4]],
                                    [[0.06, 0.24, 0.3],
                                     [0.04, 0.16, 0.2]]])
        self.assertTwoPot(self.pot * otherpot, answerpot)

        otherpot = Potential()
        otherpot.variables = np.array([3, 1])
        otherpot.card = np.array([3, 2])
        otherpot.table = np.array([[0.2, 0.3], [0.2, 0.2], [0.6, 0.5]])
        answerpot = Potential()
        answerpot.variables = np.array([1, 2, 3])
        answerpot.card = np.array([2, 2, 3])
        answerpot.table = np.array([[[0.04, 0.04, 0.12],
                                     [0.16, 0.16, 0.48]],
                                    [[0.18, 0.12, 0.3],
                                     [0.12, 0.08, 0.2]]])
        self.assertTwoPot(self.pot * otherpot, answerpot)

    def testDivEmpty(self):
        otherpot = Potential()
        answerpot = copy.deepcopy(self.pot)
        self.assertTwoPot(self.pot / otherpot, answerpot)
        newpot = self.pot / otherpot
        newpot.table[0] = -1
        #print "newpot id:", id(newpot)
        #print "self.pot id:", id(self.pot)
        #print "newpot.table:", newpot.table
        #print "self.pot.table:", self.pot.table

        otherpot = copy.deepcopy(self.pot)
        answerpot = copy.deepcopy(self.pot)
        self.pot = Potential()
        answerpot.table = 1 / answerpot.table
        self.assertTwoPot(self.pot / otherpot, answerpot)

    def testDiv(self):
        otherpot = Potential()
        otherpot.variables = np.array([3])
        otherpot.card = np.array([3])
        otherpot.table = np.array([0.1, 0.4, 0.5])
        answerpot = Potential()
        answerpot.variables = np.array([1, 2, 3])
        answerpot.card = np.array([2, 2, 3])
        answerpot.table = np.array([[[2.0, 0.5, 0.4],
                                     [8.0, 2.0, 1.6]],
                                    [[6.0, 1.5, 1.2],
                                     [4.0, 1.0, 0.8]]])
        self.assertTwoPot(self.pot / otherpot, answerpot)

        otherpot = Potential()
        otherpot.variables = np.array([3, 1])
        otherpot.card = np.array([3, 2])
        otherpot.table = np.array([[0.2, 0.3], [0.2, 0.2], [0.6, 0.5]])
        answerpot = Potential()
        answerpot.variables = np.array([1, 2, 3])
        answerpot.card = np.array([2, 2, 3])
        answerpot.table = np.array([[[1.0, 1.0, 0.333333],
                                     [4.0, 4.0, 1.333333]],
                                    [[2.0, 3.0, 1.2],
                                     [1.333333, 2.0, 0.8]]])
        self.assertTwoPot(self.pot / otherpot, answerpot)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    #suite.addTest(PotentialTestCase("test_constructor"))
    suite.addTest(PotentialTestCase("test_plus_operator"))
    suite.addTest(PotentialTestCase("testMultEmpty"))
    suite.addTest(PotentialTestCase("testMult"))
    suite.addTest(PotentialTestCase("testDivEmpty"))
    suite.addTest(PotentialTestCase("testDiv"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
