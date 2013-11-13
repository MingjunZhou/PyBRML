#File :  draw_layout.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-10
#License : BSD 3 clause
#Description :


import networkx as nx
import numpy as np
from .make_layout import make_layout


def topological_layout(adj, g):
    x, y = make_layout(adj, g)
    coord = np.vstack((x, y))
    coord = coord.transpose()
    pos_dict = {i: co for i, co in enumerate(coord)}
    return pos_dict


def custom_layout(coord):
    return {i: co for i, co in enumerate(coord)}


def draw_layout(adj, gtype='directed', layout='topological',
                labels=None, node_type=None, coord=None):
    """Draw a layout for the graph represented by the adjacency matrix.

    Usage :
        g, coord = draw_layout(adj<, labels, node_t, coord>)

    Parameters :
        adj : 2-d nd.ndarray[n_node, n_node]
            Adjacency matrix, the row is source, and the coloumn is sink.

        gtype : string, optional, default : 'directed' :
            'directed' for the directed graph, 'undirected' for the undirected
            graph

        layout : string, optional, default : 'topological' :
            Graph layout which gives the nodes' positions.
            'circular': Position nodes on a circle.
            'random': Position nodes uniformly at random in the unit square.
            'shell': Position nodes in concentric circles.
            'spring': Position nodes using Fruchterman-Reingold force-dircted
                      algorithm.
            'spectral': Position nodes using the eigenvectors of the graph
                        Laplacian.
            'topological': Position nodes in the levels given by
                           topological_sort algorithm.
            'custom': Position nodes given by the 'coord' parameter.

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
    square_nodes = node_type.nonzero()[0]
    circle_nodes = (node_type == 0).nonzero()[0]

    graph_layout = {'circular': lambda g: nx.circular_layout(g),
                    'random': lambda g: nx.random_layout(g),
                    'shell': lambda g: nx.shell_layout(g),
                    'spring': lambda g: nx.spring_layout(g),
                    'spectral': lambda g: nx.spectral_layout(g)}
    if layout == 'topological':
        pos_dict = topological_layout(adj, g)
    elif layout == 'custom':
        pos_dict = custom_layout(coord)
    else:
        pos_dict = graph_layout[layout](g)

    label_dict = {i: la for i, la in enumerate(labels)}
    if square_nodes.size != 0:
        nx.draw_networkx_nodes(g, pos=pos_dict,
                               nodelist=list(square_nodes), node_shape='s')
    if circle_nodes.size != 0:
        nx.draw_networkx_nodes(g, pos=pos_dict,
                               nodelist=list(circle_nodes), node_shape='o')

    nx.draw_networkx_edges(g, pos=pos_dict)
    nx.draw_networkx_labels(g, pos=pos_dict, labels=label_dict)
    return g, coord
