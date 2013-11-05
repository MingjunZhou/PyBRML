#!/usr/bin/env python
"Basic Class: potential"
if __name__ == "__main__" and __package__ is None:
    __package__ = "brml.potential"
#if __name__ == '__main__':
#    print 'PotentialClass is running by itself'
#else:
#    print 'PotentialClass is imported as module'

import numpy as np
import copy
from ..utils.ismember import ismember
from ..reasoning.index_to_assignment import index_to_assignment
from ..assert_utilities import assert_var_card_table



class potential(object):
    def __init__(self, variables=None, card=None, table=None):
        if variables is None:
            variables = []
        if card is None:
            card = []
        if table is None:
            table = []

        if not isinstance(variables, np.ndarray):
            variables = np.array(variables)
        if not isinstance(card, np.ndarray):
            card = np.array(card)
        if not isinstance(table, np.ndarray):
            table = np.array(table)

        assert_var_card_table(variables, card, table)

        self.variables = variables
        self.card = card
        self.table = table

    def __add__(self, other):
        # check for empty potential
        if self.variables.size == 0:
            return copy.deepcopy(other)
        if other.variables.size == 0:
            return copy.deepcopy(self)

        commonitem = np.intersect1d(self.variables, other.variables)
        idx1 = np.in1d(self.variables, commonitem).nonzero()
        idx2 = np.in1d(other.variables, commonitem).nonzero()
        if commonitem.size > 0:
            assert np.allclose(self.card[idx1], other.card[idx2])

        new_var = np.union1d(self.variables, other.variables)
        dummy, mapA, all_mapA = ismember(self.variables, new_var)
        dummy, mapB, all_mapB = ismember(other.variables, new_var)

        new_card = np.zeros(new_var.size, 'int8')
        new_card[mapA] = list(self.card)
        new_card[mapB] = list(other.card)

        new_table = np.zeros(tuple(new_card))
        for i in range(np.prod(new_card)):
            assignment = IndexToAssignment(i, new_card)
            assign1 = np.array(assignment)[mapA]
            assign2 = np.array(assignment)[mapB]
            new_table[tuple(assignment)] = self.table[tuple(assign1)] +\
                other.table[tuple(assign2)]

        newpot = potential(new_var, new_card, new_table)
        return newpot

    def __mul__(self, other):
        # check for empty potential
        if self.variables.size == 0:
            return copy.deepcopy(other)
        if other.variables.size == 0:
            return copy.deepcopy(self)

        commonitem = np.intersect1d(self.variables, other.variables)
        idx1 = np.in1d(self.variables, commonitem).nonzero()
        idx2 = np.in1d(other.variables, commonitem).nonzero()
        if commonitem.size > 0:
            assert np.allclose(self.card[idx1], other.card[idx2])

        newpot = potential()
        #FIX ME: dimension consistency not checked
        #FIX ME: only 1-D multiply considered

        newpot.variables = np.union1d(self.variables, other.variables)
        # sorted union of input arrays
        dummy, mapA, all_mapA = ismember(self.variables, newpot.variables)
        dummy, mapB, all_mapB = ismember(other.variables, newpot.variables)

        newpot.card = np.zeros(newpot.variables.size, 'int8')
        newpot.card[mapA] = list(self.card)
        newpot.card[mapB] = list(other.card)

        newpot.table = np.zeros(tuple(newpot.card))
        for i in range(np.prod(newpot.card)):
            assignment = IndexToAssignment(i, newpot.card)
            assign1 = np.array(assignment)[mapA]
            assign2 = np.array(assignment)[mapB]
            newpot.table[tuple(assignment)] = self.table[tuple(assign1)] *\
                other.table[tuple(assign2)]

        return newpot

    def __div__(self, other):
        # It only makes senses in undirected graph.
        # Reference: BRMLtoolbox/+brml/@array/mrdivide.m
        if other.variables.size == 0:
            return copy.deepcopy(self)
        if self.variables.size == 0:
            newpot = copy.deepcopy(other)
            newpot.table = 1 / newpot.table
            return newpot

        nother = copy.deepcopy(other)
        nother.table = 1 / nother.table
        newpot = self * nother
        return newpot

    def size(self):
        return self.card
