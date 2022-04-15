"""
    Graph node class

Attributes (mostly used by animation driver):
    name (str)
    weight (int)
    visited (boolean)
    state (start, goal, working)
    - when goal is reached, all working should change color
    edges (list)
    - in and out edges if graph is undirected
    - only out edges if graph is directed
    - graph object has a flag

TODO:
- Deal with self loops?
"""

class Node:
    def __init__(self, name="noname", weight=None, state="default", visited=False, edges=None):
        self.name = name
        self.weight = weight
        self.state = state
        self.visited = visited
        self.edges = []

    def visit(self):
        self.visited = True

    def work(self):
        if self.state != "start" and self.state != "goal":
            self.state = "working"

    def set_start(self):
        self.state = 'start'
    
    def set_goal(self):
        self.state = 'goal'

    # adds an edge between this node and the supplied node
    # updates the target node if the graph isn't directed
    def add_edge(self, node=None, isDirected=False):
        if node is None or node in self.edges:
            return False
        self.edges.append(node)
        if not isDirected:
            return node.add_edge(self, True)
        return True

    # adds a list of edges (nodes)
    def add_edges(self, nodes=None, isDirected=False):
        for node in nodes:
            self.add_edge(node, isDirected)
        