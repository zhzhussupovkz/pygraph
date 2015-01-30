# -*- coding: utf-8 -*-

# node realization
class Node(object):

    # create node with key and props
    def __init__(self, key):
        self.deg = 0
        self.key = key
        self.neighbors = set()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.key == self.key
        return False

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str({ "key" : self.key, "deg" : self.deg, "neighbors" : [n.key for n in self.neighbors]})

    # get neighbors
    def get_neighbors(self):
        return self.neighbors
