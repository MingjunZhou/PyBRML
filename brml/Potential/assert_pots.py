import numpy as np


def assert_two_pots(pot_a, pot_b):
    """Assert whether two potentials are equal.

    Parameters :
        pot_a : Potential :
            The first potential.

        pot_b : Potential :
            The second potential.

    Returns :
        None

    Raises :
        AssertionError :
            When pot_a is not equal to pot_b.

    Usage :
        assert_two_pots(pot_a, pot_b)
    """
    assert np.allclose(pot_a.variables, pot_b.variables)
    assert np.allclose(pot_a.card, pot_b.card)
    assert np.allclose(pot_a.table, pot_b.table)


def assert_var_card_table(variables, card, table):
    """Assert whether variables are in accordance with card and table.

    Parameters :
        variables : np.ndarray[n_variables, ] :
            The variables of one potential.

        card : np.ndarray[n_card, ] :
            The cardinality of each variable.

        table : np.ndarray[card[0], card[1], card[2], ...] :
            The table of the poetntial.

    Returns :
        None

    Raises :
        AssertionError :
            When variables, card, table are not in accordance.

    Usage :
        assert_two_pots(variables, card, table)
    """
    assert np.allclose(variables.size, card.size)
    assert np.allclose(card, table.shape)


def assert_pot_aligned(pot):
    assert_var_card_table(pot.variables, pot.card, pot.table)
