# -*- coding: utf-8 -*-

from graph import *

# create nodes
admin = Node(name = "admin")
programmer = Node(name = "programmer")
designer = Node(name  = "designer")

# create edges
edge1 = Edge(source=admin, target=programmer)
edge2 = Edge(source=admin, target=designer)
edge3 = Edge(source=admin, target=programmer)

new_admin = Node(name = "new admin")

# add edge
new_admin.add_edge(edge1)
new_admin.add_edge(edge2)

# add new edge with direction
admin.add_edge_from_node(programmer)
admin.add_edge_from_node(designer)

print admin.props
print admin.deg
print admin.get_neighbors()
print admin.get_edges()

print "\n"
print programmer.props
print programmer.deg
print programmer.get_neighbors()
print programmer.get_edges()


print "\n"
print designer.props
print designer.deg
print designer.get_neighbors()
print designer.get_edges()

v = [admin, programmer, designer]
e = [edge1, edge2]

# create newgraph
myG = Graph(v, e)
print "\n myG"
print myG.nodes
print myG.edges

for k in myG.nodes:
    print k.get_prop('name')
    print k.deg
    print k.get_neighbors()
    print k.get_edges()
