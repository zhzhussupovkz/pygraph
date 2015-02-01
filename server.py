# -*- coding: utf-8 -*-

from bottle import route, run, template, static_file
from graph.graph import *

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def graph():
    data = {}
    edges = [Edge('a','b',10), Edge('a','c',3), Edge('c','d',2), Edge('d','b',5), Edge('d','a', 3), Edge('b', 'f',4)]
    myG = Graph(edges=edges)
    myG.add_edge(Edge('e', 'k', 1))\
            .add_edge(Edge('b', 'k', 2))\
            .add_edge(Edge('f', 'e', 3))\
            .add_edge(Edge('e', 'c', 1))
    data['data'] = myG.to_json()
    data['title'] = 'Graph'
    return template('views/graph', data)

@route('/graph')
def graph():
    edges = [Edge('a','b',10), Edge('a','c',3), Edge('c','d',2), Edge('d','b',5), Edge('d','a', 3), Edge('b', 'f',4)]
    myG = Graph(edges=edges)
    myG.add_edge(Edge('e', 'k', 1))\
            .add_edge(Edge('b', 'k', 2))\
            .add_edge(Edge('f', 'e', 3))\
            .add_edge(Edge('e', 'c', 1))
    return myG.to_json()

run(host='localhost', port=8080)
