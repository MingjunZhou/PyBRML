#File :  max_array_test.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-07
#License : BSD 3 clause
#Description :


import unittest
import numpy as np
import sys
sys.path.append("..")
from brml.Potential import Potential, maxpot
from brml.Potential.assert_pots import assert_two_pots


class MaxPotTestCase(unittest.TestCase):
    def test_case1(self):
        array = np.arange(24)
        array = array.reshape([2, 3, 4])
        pot = Potential([0, 1, 2], [2, 3, 4], array)
        newpot, max_state = maxpot(pot, [0, 2])
        #print "newpot.variables=", newpot.variables
        #print "newpot.card=", newpot.card
        #print "newpot.table=", newpot.table
        #print "max_state=", max_state
        anspot = Potential([1], [3], np.array([15, 19, 23]))
        assert_two_pots(anspot, newpot)

    def test_case2(self):
        array = np.arange(24)
        array = array.reshape([2, 3, 4])
        pot = Potential([0, 1, 2], [2, 3, 4], array)
        newpot, max_state = maxpot(pot, [2])
        #max_val = max_array(array, [2])
        #print "max_val=", max_val
        #print "newpot.variables=", newpot.variables
        #print "newpot.card=", newpot.card
        #print "newpot.table=", newpot.table
        #print "max_state=", max_state
        ans_table = np.array([[3, 7, 11], [15, 19, 23]])
        anspot = Potential([0, 1], [2, 3], ans_table)
        assert_two_pots(anspot, newpot)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MaxPotTestCase("test_case1"))
    suite.addTest(MaxPotTestCase("test_case2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
