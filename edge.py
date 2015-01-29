# -*- coding: utf-8 -*-

# edge realization
class Edge(object):

    def __init__(self, source = None, target = None, props = {}):
        self.props = props
        self.source = source
        self.target = target

        if self.source:
            self.add_node(self.source)

        if self.target:
            self.add_node(self.target)

    def __eq__(self, other):
        check_direct = False
        if self.source and other.source:
            check_direct = self.source == other.source
        if self.target and other.target:
            check_direct = check_direct and self.source == other.source
        return check_direct and (self.props == other.props)

    # set property
    def set_prop(self, key, val):
        self.props['key'] = val

    # get property
    def get_prop(self, key):
        return self.props.get(key)

    # add to node
    def add_node(self, node):
        node.add_edge(self)

    # set edge target
    def set_target(self, target):
        self.target = target

    # set edge source
    def set_source(self, source):
        self.source = source
