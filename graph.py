# -*- coding: utf-8 -*-

from node import *
from edge import *

# graph
class Graph(object):

    def __init__(self, edges = []):
        # nodes
        self.nodes = set()

        # edges
        self.edges = set(edges)

        for e in edges:
            self.add_edge(e)

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
        adm = []
        n_count = len(self.nodes)
        e_count = len(self.edges)
        if e_count > 1 and n_count > 1:
            adm = [[1 if self.is_neighbor(n.key, k.key) else 0 for n in list(self.nodes)] for k in list(self.nodes)]
        return adm

    # get incidence matrix
    def incidence_matrix(self):
        edges = list(self.edges)
        im = [[0 for n in list(self.nodes)] for k in edges]
        n_count = len(self.nodes)
        e_count = len(self.edges)
        if e_count > 1 and n_count > 1:
            for i in range(0, len(self.nodes)):
                for j in range(0, len(edges)):
                    if i == edges[j].source:
                        im[j][i] = 1
                    elif i == edges[j].target:
                        im[j][i] = -1
                    else:
                        im[j][i] = 0
        return im

    # connect two nodes
    def connect(self, source, target):
        e = Edge(source, target)
        self.add_edge(e)

    # is neighbor
    def is_neighbor(self, a, b):
        if a == b:
            return True
        f = Edge(a, b)
        t = Edge(b, a)
        if f in self.edges or t in self.edges:
            return True
        return False

    # add node to graph
    def add_node(self, node):
        self.nodes.add(node.key)

    # edge exist
    def edge_exist(self, source, target):
        if source == target:
            return True
        e = Edge(source, target)
        if e in self.edges:
            return True
        return False

    # delete node from graph
    def delete_node(self, key):
        self.nodes.remove(Node(key))

    # add edge
    def add_edge(self, edge):
        self.edges.add(edge)
        s = Node(edge.source)
        t = Node(edge.target)
        s.neighbors.add(t)
        s.deg += 1
        t.deg += 1
        t.neighbors.add(s)
        self.nodes.add(s)
        self.nodes.add(t)

    # delete edge from graph
    def delete_edge(self, edge):
        self.edges.remove(edge)
