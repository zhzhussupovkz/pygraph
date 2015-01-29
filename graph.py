# -*- coding: utf-8 -*-

from node import *

# graph
class Graph(object):

    def __init__(self, edges = []):
        # nodes
        self.nodes = set()

        # edges
        self.edges = edges
        for k in edges:
            self.nodes.add(k.source)
            self.nodes.add(k.target)
        self.nodes = filter(None, list(self.nodes))

    # is complete
    def is_complete(self):
        n_count = len(self.nodes)
        e_count = len(self.edges)
        check = n_count * (n_count -1)/2
        if e_count == check:
            return True
        return False

    # get adjacency matrix
    def adjacency_matrix(self):
        im = []
        n_count = len(self.nodes)
        e_count = len(self.edges)
        if e_count > 1 and n_count > 1:
            im = [[1 if n.has_edge_from_node(k) else -1 for n in self.nodes] for k in self.nodes]
        return im

    # get incidence matrix
    def incidence_matrix(self):
        im = [[0 for n in self.nodes] for k in self.edges]
        n_count = len(self.nodes)
        e_count = len(self.edges)
        if e_count > 1 and n_count > 1:
            for i in range(0, len(self.nodes)):
                for j in range(0, len(self.edges)):
                    if self.nodes[i].is_edge_from(self.edges[j]):
                        im[j][i] = 1
                    elif self.nodes[i].is_edge_to(self.edges[j]):
                        im[j][i] = -1
                    else:
                        im[j][i] = 0
        return im

    # add node to graph
    def add_node(self, node):
        self.nodes.append(node)

    # delete node from graph
    def delete_node(self, node):
        self.nodes.remove(node)

    # add edge
    def add_edge(self, source = None, target = None):
        if source and source not in self.nodes:
            self.nodes.append(source)
        if target and target not in self.nodes:
            self.nodes.append(target)
        edge = Edge(source, target)
        self.edges.append(edge)

    # delete edge from graph
    def delete_edge(self, edge):
        self.edges.remove(edge)
