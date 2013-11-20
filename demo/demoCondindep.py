#File :  demoCondindep.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-19
#License : BSD 3 clause
#Description :

"""Chest Clinic example: test independecies"""
print __doc__

import matplotlib.pyplot as plt
import scipy.io
import sys
sys.path.append("..")
from brml.Potential import Potential
from brml.Potential.cond_indep_pot import cond_indep_pot
from brml.Graph.dag import dag
from brml.Graph.draw_layout import draw_layout


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
#            print "enter"
            #variables = variables.tolist()
            #variables = variables[2:] + variables[0:2]
            #new_axis = range(l_var-2, l_var) + range(l_var-2)
            #axis1 = range(l_var-2, l_var)
            #axis2 = range(l_var-2)
            #axis2.reverse()
            #new_axis = axis1 + axis2 
            #table = np.transpose(table, new_axis)
            card = table.shape
    allpots.append(Potential(variables, card, table))


#two_pot = multpots(allpots)
#tt_pot = multpots(allpots[0:6])
#print "\n6_table:", two_pot.table
#print "\n6_variables:", two_pot.variables
#print "tt_pot.value=", tt_pot.table[0,1,0,1,0,1,1]
#print "t7.value=", allpots[6].table[0,1,0]
#print "\none_value:", two_pot.table[0,1,0,1,0,1,0,1]
#print "\n6_card:", two_pot.table.shape

#for i, pot in enumerate(allpots):
#    print "\npot No.", i
#    print "variables=", pot.variables
#    print "table=", pot.table
A = dag(allpots)
draw_layout(A, layout='spring', labels=range(1, 9))
plt.show()
X = [1, 4]
Y = [2]
Z = [3, 5]

print cond_indep_pot(allpots[0:8], X, Y, Z)
