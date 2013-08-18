#File:  sumpotTest.py
#Author: Mingjun Zhou <mingjun.zhou@gmail.com>
#Version: 1.0
#Date: 2013-08-17
#License: BSD 3 Clause
#Description:


import unittest
import sys
sys.path.append("..")
from brml.sumpot import sumpot
from brml.potential import potential
import numpy as np


class sumpotTestCase(unittest.TestCase):
    def setUp(self):
        self.pot = potential()
        self.pot.variables = np.array([3, 2, 1])
        self.pot.card = np.array([2, 3, 4])
        self.pot.table = np.arange(0, 24).reshape(2, 3, 4)

    def tearDown(self):
        self.pot = None

    def assertTwoPot(self, pa, pb):
        assert np.allclose(pa.variables, pb.variables)
        assert np.allclose(pa.card, pb.card)
        assert np.allclose(pa.table, pb.table)

    def testSinglePotOrder1(self):
        answerPot = potential()
        answerPot.variables = np.array([3, 1])
        answerPot.card = np.array([2, 4])
        answerPot.table = np.array([[12, 15, 18, 21], [48, 51, 54, 57]])

        self.assertTwoPot(sumpot(self.pot, [2]), answerPot)

    def testSinglePotOrder0(self):
        answerPot = potential()
        answerPot.variables = np.array([2])
        answerPot.card = np.array([3])
        answerPot.table = np.array([60, 92, 124])

        self.assertTwoPot(sumpot(self.pot, [2], sumover=0), answerPot)

    def testPotsOrder1(self):
        answerPot = potential()
        answerPot.variables = np.array([3, 1])
        answerPot.card = np.array([2, 4])
        answerPot.table = np.array([[12, 15, 18, 21], [48, 51, 54, 57]])

        for pot in sumpot([self.pot, self.pot], [2]):
            self.assertTwoPot(pot, answerPot)

    def testPotsOrder0(self):
        answerPot = potential()
        answerPot.variables = np.array([2])
        answerPot.card = np.array([3])
        answerPot.table = np.array([60, 92, 124])

        for pot in sumpot([self.pot, self.pot], [2], sumover=0):
            self.assertTwoPot(pot, answerPot)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(sumpotTestCase("testSinglePotOrder1"))
    suite.addTest(sumpotTestCase("testSinglePotOrder0"))
    suite.addTest(sumpotTestCase("testPotsOrder1"))
    suite.addTest(sumpotTestCase("testPotsOrder0"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
