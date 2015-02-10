# -*- coding: utf-8 -*-

from bottle import route, run, template, static_file
from graph.graph import *
import random

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def graph():
    data = {}
    data['title'] = 'Graph'
    data['header'] = 'PyGraph'
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

@route('/random')
def get_random_graph():
    data = {}
    data['title'] = 'Random Graph'
    data['header'] = 'PyGraph'
    return template('views/random', data)

@route('/rgraph')
def rgraph():
    edges = []
    labels = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']
    for i in range(1, 25):
        s = labels[random.randint(0, 10)]
        t = labels[random.randint(0, 10)]
        w = random.randint(2, 10)
        edges.append(Edge(str(s),str(t),w))

    myG = Graph(edges=edges)
    return myG.to_json()

run(host='localhost', port=8080)
