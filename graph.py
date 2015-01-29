# -*- coding: utf-8 -*-

# node realization
class Node(object):

    def __init__(self, name = "Node"):
        self.deg = 0
        self.neighbors = { "from" : [], "to" : [] }
        self.edges = []
        self.props = {"name" : name}

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

    # add edge to current node from another
    def add_edge_from_node(self, node):
        if (isinstance(node, Node)):
            self.neighbors['to'].append(node)

            # add edge
            edge = Edge(source = node, target = self)
            self.edges.append(edge)
            self.deg += 1
            self.__set_neighbor(edge = edge, direction = 'to')
            return True
        return False

    # add edge from current node to another
    def add_edge_to_node(self, node):
        if (isinstance(node, Node)):
            self.neighbors['from'].append(node)

            # add edge
            edge = Edge(source = self, target = node)
            self.edges.append(edge)
            self.deg += 1
            self.__set_neighbor(edge = edge, direction = 'from')
            return True
        return False

    # check if another node is neighbor
    def is_neighbor(self, node):
        if (isinstance(node, Node)):
            if (node in self.neighbors.get('from') or node in self.neighbors.get('to')):
                return True
        return False

    # check if have edge
    def exists_edge(self, edge):
        if (isinstance(edge, Edge)):
            if (edge in self.edges):
                return True
        return False

# edge realization
class Edge(object):

    def __init__(self, source = None, target = None):
        self.source = source
        self.target = target

    # set edge target
    def set_target(self, target):
        if (isinstance(target, Node)):
            self.target = target
            return True
        return False

    # set edge source
    def set_source(self, source):
        if (isinstance(source, Node)):
            self.source = source
            return True
        return False


# graph
class Graph(object):

    def __init__(self, nodes = None, edges = None):
        # nodes
        if not nodes:
            self.nodes = []
        else:
            self.nodes = nodes

        # edges
        if not edges:
            self.edges = []
        else:
            self.edges = edges

    # add node to graph
    def add_node(self, node):
        if (isinstance(node, Node)):
            self.nodes.append(node)
            return True
        return False

    # delete node from graph
    def delete_node(self, node):
        if (isinstance(node, Node)):
            self.nodes.remove(node)
            return True
        return False

    # add edge
    def add_edge(self, source, target):
        if (isinstance(source, Node) or isinstance(target, Node)):
            edge = Edge(source, target)
            self.edges.append(edge)
            return True
        return False

    # delete edge from graph
    def delete_edge(self, edge):
        if (isinstance(edge, Edge)):
            self.edges.remove(edge)
            return True
        return False
