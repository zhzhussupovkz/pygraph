# -*- coding: utf-8 -*-

from graph import *

edges = [Edge(0,1,10), Edge(0,2,3), Edge(2,3,2), Edge(3,1,5), Edge(3,0,1), Edge(1,4,4)]
myG = Graph(edges=edges)
myG.add_edge(Edge(2, 5, 1))
myG.add_edge(Edge(1, 6, 2))
myG.add_edge(Edge(6, 7, 3))

print "Graph:"
print myG

print "\nNodes:"
for n in myG.nodes:
    print n

print "\nEdges:"
for e in myG.edges:
    print e

print "\nAdjacency matrix:"
print myG.adjacency_matrix()

print "\nIncidence matrix:"
print myG.incidence_matrix()

print "\nPaths from node 2 to 7:"
print myG.dfs_paths(2, 7)

print "\nfloyd warshall:"
print myG.floyd_warshall()