import abc
import numpy as np


class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

        @abc.abstractmethod
        def add_edge(self, V1, V2, weight):
            pass

        @abc.abstractmethod
        def get_adj_vertices(self, v):
            pass

        @abc.abstractmethod
        def get_indegree(self, v):
            pass

        @abc.abstractmethod
        def get_edge_weight(self, V1, V2):
            pass

        @abc.abstractmethod
        def display(self):
            pass


class node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set= set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)

        self.adjacency_set.add(v)

    def get_adj_vertices(self):
        return sorted(self.adjacency_set)


class adjacency_set_graph(Graph):

    def __init__(self, numVertices, directed=False):
        super(adjacency_set_graph, self).__init__(numVertices, directed)

        self.vertex_list = []
        for N in range(numVertices):
            self.vertex_list.append(node(N))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights >1")

        self.vertex_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def get_adj_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        return self.vertex_list[v].get_adj_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for N in range(self.numVertices):
            if v in self.get_adj_vertices(N):
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for val in range(self.numVertices):
            for v in self.get_adj_vertices(val):
                print(val, "--->", v)


class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("an edge cannot have weight < 1")

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adj_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adj_vertices(i):
                print(i, "--->", v)

