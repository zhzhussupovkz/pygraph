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
        nodes = sorted(list(self.nodes), key=lambda n: n.key, reverse=False)
        n_count = len(self.nodes)
        e_count = len(self.edges)
        if e_count > 1 and n_count > 1:
            adm = [[1 if self.is_neighbor(n.key, k.key) else 0 for n in nodes] for k in nodes]
        return adm

    # get incidence matrix
    def incidence_matrix(self):
        nodes = sorted(list(self.nodes), key=lambda n: n.key, reverse=False)
        edges = sorted(list(self.edges), key=lambda e: e.source, reverse=False)
        im = [[0 for k in edges] for n in nodes]
        n_count = len(nodes)
        e_count = len(edges)
        if e_count > 1 and n_count > 1:
            for i in range(0, n_count):
                for j in range(0, e_count):
                    if nodes[i].key == edges[j].source:
                        im[i][j] = 1
                    elif nodes[i].key == edges[j].target:
                        im[i][j] = -1
                    else:
                        im[i][j] = 0
        return im

    # connect two nodes
    def connect(self, source, target):
        e = Edge(source, target)
        self.add_edge(e)

    # is neighbor
    def is_neighbor(self, a, b):

        # if source is equal target
        if a == b:
            return True
        f = Edge(a, b)
        t = Edge(b, a)
        if f in self.edges or t in self.edges:
            return True
        return False

    # if exist edge with given source and target
    def edge_exist(self, source, target):
        if source == target:
            return True
        e = Edge(source, target)
        if e in self.edges:
            return True
        return False

    # delete node from graph
    def delete_node(self, key):
        node = Node(key)
        if node in self.nodes:
            self.nodes.remove(node)
            for n in self.nodes:
                if node in n.neighbors:
                    n.neighbors.remove(node)
                f = Edge(key, n.key)
                t = Edge(n.key, key)
                if f in self.edges:
                    self.edges.remove(f)
                if t in self.edges:
                    self.edges.remove(t)

    # add edge
    def add_edge(self, edge):
        self.edges.add(edge)
        s = Node(edge.source)
        t = Node(edge.target)
        self.nodes.add(s)
        self.nodes.add(t)
        for n in self.nodes:
            if n.key == edge.source:
                n.neighbors.add(t)
                n.deg += 1
            if n.key == edge.target:
                n.neighbors.add(s)
                n.deg += 1

    # delete edge from graph
    def delete_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            s = Node(edge.source)
            t = Node(edge.target)
            for n in self.nodes:
                if n == s and t in n.neighbors:
                    n.neighbors.remove(t)
                    n.deg -= 1
                if n == t and s in n.neighbors:
                    n.neighbors.remove(s)
                    n.deg -= 1
