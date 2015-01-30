# -*- coding: utf-8 -*-

# node realization
class Node(object):

    # create node with key and props
    def __init__(self, key, props = {}):
        self.deg = 0
        self.key = key
        self.neighbors = set()
        self.props = {}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.key == self.key
        return False

    def __hash__(self):
        return hash(self.key)

    # set property
    def set_prop(self, key, val):
        self.props[key] = val

    # get property
    def get_prop(self, key):
        return self.props.get(key)

    # get neighbors
    def get_neighbors(self):
        return self.neighbors
