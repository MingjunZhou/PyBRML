import numpy as np


def assert_two_pots(pot_a, pot_b):
    assert np.allclose(pot_a.variables, pot_b.variables)
    assert np.allclose(pot_a.card, pot_b.card)
    assert np.allclose(pot_a.table, pot_b.table)


def assert_var_card_table(variables, card, table):
    assert np.allclose(variables.size, card.size)
    assert np.allclose(card, table.shape)

def assert_pot_aligned(pot):
    assert_var_card_table(pot.variables, pot.card, pot.table)
