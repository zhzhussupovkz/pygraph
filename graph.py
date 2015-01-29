# -*- coding: utf-8 -*-

from node import *

# graph
class Graph(object):

    def __init__(self, nodes = [], edges = []):
        # nodes
        self.nodes = nodes

        # edges
        self.edges = edges

    # is complete
    def is_complete(self):
        n_count = len(nodes)
        e_count = len(edges)
        check = n_count * (n_count -1)/2
        if e_count == check:
            return True
        return False

    # add node to graph
    def add_node(self, node):
        self.nodes.append(node)

    # delete node from graph
    def delete_node(self, node):
        self.nodes.remove(node)

    # add edge
    def add_edge(self, source, target):
        edge = Edge(source, target)
        self.edges.append(edge)

    # delete edge from graph
    def delete_edge(self, edge):
        self.edges.remove(edge)
