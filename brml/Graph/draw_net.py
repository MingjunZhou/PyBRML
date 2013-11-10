#File :  draw_net.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-10
#License : BSD 3 clause
#Description :

import networkx as nx


def draw_net():
    """Maximise a potential over variables.

    Usage :
        newpot, maxstate = maxpot(pot, invariables)

    Parameters :
        pot : Potential class :
            The target potential to be maximised. After the maximisation, the
            origin pot is not changed, instead we get a newpot.

        varargin : sequence[n_variables, ] or nd.ndarray[n_variables, ] :
            Several variales to maximise the potential over.

        maxover : int, optional, default: 1 :
            If maxover == 1 the potential is maxed over variables, otherwise
            potential is maxed over everything except variables.

    Returns :
        newpot : Potential class :
            A new pot that maximised the origin potential.

        maxstate : nd.array[n_variables, ] :
            When the variables in varargin equal to the states in maxstate,
            we get the maximised potential.

    Raises :
        None

    """

     
