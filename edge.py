# -*- coding: utf-8 -*-

# edge realization
class Edge(object):

    # create edge from source key to target key with props
    def __init__(self, source, target, props = {}):
        self.props = props
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

    # set property
    def set_prop(self, key, val):
        self.props[key] = val

    # get property
    def get_prop(self, key):
        return self.props.get(key)
