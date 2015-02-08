# -*- coding: utf-8 -*-

import json
from node import *
from edge import *

# graph
class Graph(object):

    def __init__(self, edges = []):
        # nodes
        self.nodes = set()

        # edges
        self.edges = set(edges)

        for e in edges:
            self.add_edge(e)

    def __str__(self):
        return str({(e.source, e.target) : e.get_weight() for e in self.edges})

    # get adjacency matrix
    def adjacency_matrix(self):
        adm = []
        nodes = sorted(list(self.nodes), key=lambda n: n.key, reverse=False)
        n_count = len(self.nodes)
        e_count = len(self.edges)
        if e_count > 1 and n_count > 1:
            adm = [[1 if self.is_neighbor(n.key, k.key) else 0 for n in nodes] for k in nodes]
        return adm

    # get incidence matrix
    def incidence_matrix(self):
        nodes = sorted(list(self.nodes), key=lambda n: n.key, reverse=False)
        edges = sorted(list(self.edges), key=lambda e: e.source, reverse=False)
        im = [[0 for k in edges] for n in nodes]
        n_count = len(nodes)
        e_count = len(edges)
        if e_count > 1 and n_count > 1:
            for i in range(0, n_count):
                for j in range(0, e_count):
                    if nodes[i].key == edges[j].source:
                        im[i][j] = 1
                    elif nodes[i].key == edges[j].target:
                        im[i][j] = -1
                    else:
                        im[i][j] = 0
        return im

    # connect two nodes
    def connect(self, source, target):
        e = Edge(source, target)
        self.add_edge(e)

    # is neighbor
    def is_neighbor(self, a, b):

        # if source is equal target
        if a == b:
            return True
        f = Edge(a, b)
        t = Edge(b, a)
        if f in self.edges or t in self.edges:
            return True
        return False

    # if exist edge with given source and target
    def edge_exist(self, source, target):
        if source == target:
            return True
        e = Edge(source, target)
        if e in self.edges:
            return True
        return False

    # delete node from graph
    def delete_node(self, key):
        node = Node(key)
        if node in self.nodes:
            self.nodes.remove(node)
            for n in self.nodes:
                if node in n.neighbors:
                    n.neighbors.remove(node)
                f = Edge(key, n.key)
                t = Edge(n.key, key)
                if f in self.edges:
                    self.edges.remove(f)
                if t in self.edges:
                    self.edges.remove(t)
        return self

    # add edge
    def add_edge(self, edge):
        self.edges.add(edge)
        s = Node(edge.source)
        t = Node(edge.target)
        self.nodes.add(s)
        self.nodes.add(t)
        for n in self.nodes:
            if n.key == edge.source:
                n.neighbors.add(t)
                n.deg += 1
            if n.key == edge.target:
                n.neighbors.add(s)
                n.deg += 1
        return self

    # delete edge from graph
    def delete_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            s = Node(edge.source)
            t = Node(edge.target)
            for n in self.nodes:
                if n == s and t in n.neighbors:
                    n.neighbors.remove(t)
                    n.deg -= 1
                if n == t and s in n.neighbors:
                    n.neighbors.remove(s)
                    n.deg -= 1
        return self

    # incidence representation
    def inc(self):
        graph = {}
        for n in self.nodes:
            graph[n.key] = set(i.key for i in n.neighbors)
        return graph

    # weighted directed graph
    def weighted_directed_graph(self):
        graph = {}
        for e in self.edges:
            if e.source not in graph:
                graph[e.source] = {e.target : e.weight}
                graph[e.target] = {}
            else:
                graph[e.source].update({e.target : e.weight})
        return graph

    # depth-first search
    def dfs(self, start):
        visited = set()
        if Node(key = start) in self.nodes:
            graph = self.inc()
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.extend(graph[node] - visited)
        return visited

    # dfs paths from start to finish
    def dfs_paths(self, start, finish):
        result = []
        if Node(start) in self.nodes and Node(finish) in self.nodes:
            graph = self.inc()
            stack = [(start, [start])]
            while stack:
                (node, path) = stack.pop()
                for n in graph[node] - set(path):
                    if n == finish:
                        result.append(path + [n])
                    else:
                        stack.append((n, path + [n]))
        return result

    # breadth-first search
    def bfs(self, start):
        visited = set()
        if Node(start) in self.nodes:
            graph = self.inc()
            queue = [start]
            while queue:
                node = queue.pop(0)
                if node not in visited:
                    visited.add(node)
                    queue.extend(graph[node] - visited)
        return visited

    # bfs paths from start to finish
    def bfs_paths(self, start, finish):
        result = []
        if Node(start) in self.nodes and Node(finish) in self.nodes:
            graph = self.inc()
            queue = [(start, [start])]
            while queue:
                (node, path) = queue.pop(0)
                for n in graph[node] - set(path):
                    if n == finish:
                        result.append(path + [n])
                    else:
                        queue.append((n, path + [n]))
        return result

    # floyd-warshall
    def floyd_warshall(self):
        nodes = sorted([n.key for n in self.nodes])
        n_count = len(nodes)
        graph = [[float("inf") for n in range(n_count)] for n in range(n_count)]

        for i in range(0, n_count):
            for j in range(0, n_count):
                for e in self.edges:
                    if e.source == nodes[i] and e.target == nodes[j]:
                        graph[i][j] = e.weight
                    elif i == j:
                        graph[i][j] = 0


        for k in range(n_count):
            for i in range(n_count):
                for j in range(n_count):
                    if(graph[i][j] > graph[i][k] + graph[k][j]):
                        graph[i][j] = graph[i][k] + graph[k][j]

        return graph

    # bellman-ford alhorithm
    def bellman_ford(self, start):
        graph = self.weighted_directed_graph()
        if graph.has_key(start):

            dest = {}
            path = {}
            for node in graph:
                dest[node] = float('Inf')
                path[node] = None
            dest[start] = 0

            for i in range(len(graph)-1):
                for u in graph:
                    for v in graph[u]:
                        if dest[u] + graph[u][v] < dest[v]:
                            dest[v]  = dest[u] + graph[u][v]
                            path[v] = u

            return dest, path
        return None

    # find any path from start to finish
    def find_path(self, start, finish, path=[]):
        graph = self.weighted_directed_graph()
        if graph.has_key(start) and graph.has_key(finish):
            path = path + [start]
            if start == finish:
                return path
            for node in graph[start]:
                if node not in path:
                    newpath = self.find_path(node, finish, path)
                    if newpath:
                        return newpath
        return None

    # to json
    def to_json(self):
        graph = {
            'nodes' : [{"id" : n.key, "label" : n.key } for n in self.nodes],
            'edges' : [{"from" : e.source, "to" : e.target, "label" : e.weight} for e in self.edges]
        }
        return json.dumps(graph)