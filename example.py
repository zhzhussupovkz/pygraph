# -*- coding: utf-8 -*-

from graph import *

edges = [Edge(0,1), Edge(0,2), Edge(2,3), Edge(3,1), Edge(3,0), Edge(1,4)]
myG = Graph(edges=edges)

print myG.nodes
print myG.edges
print myG.adjacency_matrix()
print myG.incidence_matrix()
