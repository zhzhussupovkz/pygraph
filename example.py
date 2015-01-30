# -*- coding: utf-8 -*-

from graph import *

edges = [Edge(0,1), Edge(0,2), Edge(2,3), Edge(3,1), Edge(3,0), Edge(1,4)]
myG = Graph(edges=edges)
myG.add_edge(Edge(2, 5))

print myG.adjacency_matrix()
print myG.incidence_matrix()

for n in myG.nodes:
    print n

for e in myG.edges:
    print e

print "\n"

for n in myG.nodes:
    print "key:" + str(n.key)
    print "deg:" + str(n.deg)

    print "neighbors"
    for i in n.neighbors:
        print i.key
    print "\n"