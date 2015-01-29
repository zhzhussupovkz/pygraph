# -*- coding: utf-8 -*-

# edge realization
class Edge(object):

    def __init__(self, source = None, target = None, props = {}):
        self.props = props
        self.source = source
        self.target = target
        self.add_node(self.source)
        self.add_node(self.target)

    def __eq__(self, other):
        check_direct = self.source == other.source and self.target == other.target
        return check_direct and (self.props == other.props)

    # add to node
    def add_node(self, node):
        node.add_edge(self)

    # set edge target
    def set_target(self, target):
        self.target = target

    # set edge source
    def set_source(self, source):
        self.source = source