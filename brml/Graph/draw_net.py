#File :  draw_net.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-10
#License : BSD 3 clause
#Description :

from .draw_layout import draw_layout


def draw_net(adj):
    """Draw net for the adjacency matrix.

    Usage :
        draw_layout(adj, layout='topological')

    Parameters :
        adj : np.ndarray[n_node, n_node] :
            Adjacency matrix.

    Returns :
        None

    Raises :
        None

    """
    draw_layout(adj, layout='topological')
