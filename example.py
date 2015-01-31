# -*- coding: utf-8 -*-

from graph import *

edges = [Edge('a','b',10), Edge('a','c',3), Edge('c','d',2), Edge('d','b',5), Edge('d','a', 3), Edge('b', 'f',4)]
myG = Graph(edges=edges)
myG.add_edge(Edge('e', 'k', 1))
myG.add_edge(Edge('b', 'k', 2))
myG.add_edge(Edge('f', 'e', 3))
myG.add_edge(Edge('e', 'c', 1))


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

print "\nPaths from node a to c:"
print myG.dfs_paths('a', 'c')

print "\nfloyd warshall:"
print myG.floyd_warshall()

print "\nbellman-ford:"
print myG.bellman_ford('b')