# -*- coding: utf-8 -*-

from bottle import route, run, template, static_file
from graph.graph import *

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def graph():
    edges = [Edge('a','b',10), Edge('a','c',3), Edge('c','d',2), Edge('d','b',5), Edge('d','a', 3), Edge('b', 'f',4)]
    myG = Graph(edges=edges)
    myG.add_edge(Edge('e', 'k', 1))\
            .add_edge(Edge('b', 'k', 2))\
            .add_edge(Edge('f', 'e', 3))\
            .add_edge(Edge('e', 'c', 1))
    return template('views/graph', title = "Graph")

@route('/graph')
def graph():
    return template('views/graph', title = "Graph")

run(host='localhost', port=8080)
