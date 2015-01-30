# -*- coding: utf-8 -*-

# edge realization
class Edge(object):

    # create edge from source key to target key with props
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            check_source = self.source == other.source
            check_target = self.target == other.target
            return check_source and check_target
        return False

    def __hash__(self):
        return hash((self.source, self.target))

    def __str__(self):
        return str(self.source) + '=>' + str(self.target)
