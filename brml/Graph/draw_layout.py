#File :  draw_layout.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-10
#License : BSD 3 clause
#Description :


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from .make_layout import make_layout


def draw_layout(adj, gtype='directed',
                labels=None, node_type=None, coord=None):
    """Draw a layout for the graph represented by the adjacency matrix.

    Usage :
        g, coord = draw_layout(adj<, labels, node_t, coord>)

    Parameters :
        adj : 2-d nd.ndarray[n_node, n_node]
            Adjacency matrix, the row is source, and the coloumn is sink.

        gtype : 2-value string : 'directed' | 'undirected', optional :
        'directed' :
            'directed' for the directed graph, 'undirected' for the undirected
            graph

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
        g : networkx graph

        coord : float np.ndarray[n_node, 2] :
            Coordinates of nodes on the unit square.
            A new pot that maximised the origin potential.

    Raises :
        None

    """
    n_node = adj.shape[0]

    if gtype == 'directed':
        g = nx.DiGraph(adj)
    else:
        g = nx.Graph(adj)

    if labels is None:
        labels = []
        for i in range(n_node):
            labels.append(str(i))

    if node_type is None:
        node_type = np.zeros(n_node, dtype=np.int8)
    else:
        node_type = np.array(node_type, dtype=np.int8)
    print "node_type=", node_type
    square_nodes = node_type.nonzero()[0]
    circle_nodes = (node_type == 0).nonzero()[0]

    if coord is None:
        x, y = make_layout(adj, g)
        coord = np.vstack((x, y))
        coord = coord.transpose()
    pos1 = nx.spring_layout(g)
    print "pos1=", pos1
    pos_dict = {i: co for i, co in enumerate(coord)}
    label_dict = {i: la for i, la in enumerate(labels)}
    print "pos_dict=", pos_dict
    print "sqaure_nodes=", square_nodes
    print "circle_nodes=", circle_nodes
    if square_nodes.size != 0:
        nx.draw_networkx_nodes(g, pos=pos_dict,
                               nodelist=list(square_nodes), node_shape='s')
    if circle_nodes.size != 0:
        nx.draw_networkx_nodes(g, pos=pos_dict,
                               nodelist=list(circle_nodes), node_shape='o')
 
    nx.draw_networkx_edges(g, pos=pos_dict)
    nx.draw_networkx_labels(g, pos=pos_dict, labels=label_dict)
    plt.show()
    #return g

if __name__ == "__main__":
    A = np.array([[0, 1, 1, 0], [1, 0, 1, 1],
                  [1, 1, 0, 1], [0, 1, 1, 0]])
    draw_layout(A, node_type=[1,1,1,1])
