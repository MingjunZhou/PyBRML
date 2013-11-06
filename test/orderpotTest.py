#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import unittest
import sys
sys.path.append("..")
from brml.potential import potential
from brml.potential import orderpot
import numpy as np


class orderpotTestCase(unittest.TestCase):
    def setUp(self):
        variables = np.array([3, 2, 1])
        card = np.array([2, 3, 4])
        table = np.arange(0, 24).reshape(2, 3, 4)
        self.pot = potential(variables, card, table)

    def tearDown(self):
        self.pot = None

    def assertTwoPot(self, pa, pb):
        assert np.allclose(pa.variables, pb.variables)
        assert np.allclose(pa.card, pb.card)
        assert np.allclose(pa.table, pb.table)

    def testNewOrder(self):
        neworder = [2, 1, 3]
        newpot = orderpot(self.pot, neworder)

        newtable = np.array([[[0, 12], [1, 13], [2, 14], [3, 15]],
                             [[4, 16], [5, 17], [6, 18], [7, 19]],
                             [[8, 20], [9, 21], [10, 22], [11, 23]]])
        answerpot = potential(neworder, [3, 4, 2], newtable)
        self.assertTwoPot(newpot, answerpot)

    def testSortedOrder(self):
        neworder = [1, 2, 3]
        newtable = np.array([[[0, 12], [4, 16], [8, 20]],
                             [[1, 13], [5, 17], [9, 21]],
                             [[2, 14], [6, 18], [10, 22]],
                             [[3, 15], [7, 19], [11, 23]]])
        newpot = orderpot(self.pot)
        answerpot = potential(neworder, [4, 3, 2], newtable)
        self.assertTwoPot(newpot, answerpot)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(orderpotTestCase("testNewOrder"))
    suite.addTest(orderpotTestCase("testSortedOrder"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
