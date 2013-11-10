#File :  draw_layout.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-10
#License : BSD 3 clause
#Description :


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def draw_layout(adj, labels=None, node_type=None, coord=None):
    """Maximise a potential over variables.

    Usage :
        h, coord = draw_layout(adj<, labels, node_t, coord>)

    Parameters :
        adj : 2-d nd.ndarray[n_node, n_node]
            Adjacency matrix, the row is source, and the coloumn is sink.

        labels : string sequence[n_node], optional, default : None :
            Labels for the nodes. Default is a integer list
            (0, 1, ..., n_node).

        node_type : int sequence[n_node], optional, default : None :
            If node_type[i] == 0, the i-th node is a circle, otherwise
            it's a box.

        coord : float np.ndarray[n_node, 2], optional, default : None :
            Coordinates of nodes on the unit square. When coord is set default,
            calls make_layout.

    Returns :
        h : Object handler

        coord : float np.ndarray[n_node, 2] :
            Coordinates of nodes on the unit square.
            A new pot that maximised the origin potential.

    Raises :
        None

    """
    if not isinstance(adj, np.ndarray):
        adj = np.array(adj)
    n_node = adj.shape[0]
    g = nx.Graph()
    for row in range(n_node):
        for col in range(row + 1, n_node):
            if adj[row, col] == 1:
                g.add_edge(row, col)
    nx.draw(g)
    plt.show()


if __name__ == "__main__":
    A = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                  [1, 1, 0, 1], [0, 1, 1, 0]])
    draw_layout(A)
