""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.

Attributes:
directed
start node
goal node

kept as a dictionary where the key is the name
and the value is the custom node object
"""

"""
    Consider creating a custom node class
    Could keep track of visited nodes for ending animation stuff
"""

class Graph(object):

    def __init__(self, graph_dict=None, isDirected=False, num_nodes=1):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict
        self.isDirected = isDirected
        self.num_nodes = num_nodes

    def set_start(self, start):
        self.start = start

    def get_start(self):
        return self.start

    def get_num_nodes(self):
        return self.num_nodes

    def get_vertice(self, key):
        return self._graph_dict[key]

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        """ returns the vertices of a graph as a list """
        verts = []
        for key in self._graph_dict:
            verts.append(self._graph_dict[key])
        return verts

    def all_edges(self):
        """ returns the edges of a graph """
        return self.generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex.name not in self._graph_dict:
            self._graph_dict[vertex.name] = vertex

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        self._graph_dict[str(vertex1)].add_edge(node=self._graph_dict[str(vertex2)], isDirected=self.isDirected)

    def generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = set()
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex].edges:
                if (neighbour.name, vertex) not in edges:
                    edges.add((vertex, neighbour.name))
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        res += "\nobjects: \n"
        for key in self._graph_dict:
            res += str(self._graph_dict[key]) + "\n"
        return res