#File :  demoCondindep.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-19
#License : BSD 3 clause
#Description :

"""Chest Clinic example: test independecies"""
print __doc__

import numpy as np
import scipy.io
import sys
sys.path.append("..")
from brml.Potential import Potential
from brml.Potential.cond_indep_pot import cond_indep_pot
from brml.Potential.multpots import multpots


mat = scipy.io.loadmat('../data/chestclinic.mat')
pots_list =  mat['pot'][0]
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
            print "enter"
            #variables = variables.tolist()
            #variables = variables[2:] + variables[0:2]
            new_axis = range(l_var-2, l_var) + range(l_var-2)
            table = np.transpose(table, new_axis)
            card = table.shape
    allpots.append(Potential(variables, card, table))

for i, pot in enumerate(allpots):
    print "\npot No.", i
    print "variables=", pot.variables
    print "table=", pot.table

two_pot = multpots(allpots[0:8])
three_pot = multpots(allpots[0:3])
threeaftertwo_pot = multpots([two_pot, allpots[2]])
#print "\nthe third:", allpots[2].table, allpots[2].variables
#print "\n2:", two_pot.table
#print "\n3 after 2:", threeaftertwo_pot.table
print "\n6:", two_pot.table
X = [1, 4]
Y = [2]
Z = [3, 5]

print cond_indep_pot(allpots[0:3], X, Y, Z)
