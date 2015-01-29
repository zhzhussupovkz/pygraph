# -*- coding: utf-8 -*-

from edge import *

# node realization
class Node(object):

    def __init__(self, name = "Node"):
        self.deg = 0
        self.neighbors = { "from" : [], "to" : [] }
        self.edges = []
        self.props = {"name" : name}

    def __eq__(self, other):
        check_class = isinstance(other, self.__class__)
        check_deg = (other.deg == self.deg)
        check_edges = (other.edges == self.edges)
        return check_class and check_deg and check_edges

    # set property
    def set_prop(self, key, val):
        self.props['key'] = val

    # get property
    def get_prop(self, key):
        return self.props.get(key)

    # get neighbors
    def get_neighbors(self):
        return self.neighbors

    # get edges
    def get_edges(self):
        return self.edges

    # set self as neighbor
    def __set_neighbor(self, edge, direction = 'to'):
        if direction == 'to':
            node = edge.source
            node.neighbors['from'].append(self)
            node.edges.append(edge)
        elif direction == 'from':
            node = edge.target
            node.neighbors['to'].append(self)
            node.edges.append(edge)
        node.deg += 1

    # add edge
    def add_edge(self, edge, direction = 'to'):
        if direction == 'to':
            self.neighbors['from'].append(edge.source)
        elif direction == 'from':
            self.neighbors['to'].append(edge.target)
        self.deg += 1
        self.edges.append(edge)

    # add edge to current node from another
    def add_edge_from_node(self, node):

        # add to neighbors
        self.neighbors['to'].append(node)

        # add edge
        edge = Edge(source = node, target = self)
        self.edges.append(edge)
        self.deg += 1
        self.__set_neighbor(edge = edge, direction = 'to')

    # add edge from current node to another
    def add_edge_to_node(self, node):

        # add to neighbors
        self.neighbors['from'].append(node)

        # add edge
        edge = Edge(source = self, target = node)
        self.edges.append(edge)
        self.deg += 1
        self.__set_neighbor(edge = edge, direction = 'from')

    # check if another node is neighbor
    def is_neighbor(self, node):
        return (node in self.neighbors.get('from') or node in self.neighbors.get('to'))

    # check if current node has edge to another
    def has_edge_to_node(self, node):
        return node in self.neighbors.get('from')

    # check if another node has edge to self
    def has_edge_from_node(self, node):
        return node in self.neighbors.get('to')

    # check if edge exists
    def has_edge(self, edge):
        return (edge in self.edges)

    # check if edge from self
    def is_edge_from(self, edge):
        return (edge.source == self)

    # check if edge to self
    def is_edge_to(self, edge):
        return (edge.target == self)