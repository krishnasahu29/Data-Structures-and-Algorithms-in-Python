from vertex import Vertex
from edge import Edge

class Graph:
    """Representation of a simple graph using an adjacent map"""

    def __init__(self, directed=False):
        """Create an empty (undirected, by default)

        Graph is directed if optional parameter is set to True
        """

        self._ongoing = {}
        # only create second map for directed graph, use alias for undirected
        self._incoming = {} if directed else self._ongoing

    def is_directed(self):
        """
        Property is based on the the original declaration of the graph, not its contents
        :return: True if graph is directed
        """
        return self._incoming is not self._ongoing

    def vertex_count(self):
        """Return the nunber of vertices in the graph"""
        return len(self._ongoing)

    def vertices(self):
        """:return: an iteration of all the vertices of the graph"""
        return self._ongoing.keys()

    def edge_count(self):
        """:return: no of edges in the graph"""
        total = sum(len(self._ongoing[v]) for v in self._ongoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        """:return: a set of all edges of the graph"""
        result = set()
        for secondary_map in self._ongoing.values():
            result.update(secondary_map.values())

        return result

    def get_edges(self, u, v):
        """:return: edge from u to v, or None if not adjacent"""
        return self._ongoing[u].get(v)

    def degree(self, v, ongoing=True):
        """:return: no of (outgoing) edges incident to vertex v in the graph

        If graph is directed, optional parameter used to count incoming edges
        """
        adj = self._ongoing if ongoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, ongoing=True):
        """:return: all (ongoing) edges incident to vertex v in the graph

        If graph is directed, optional parameter used to request incoming graph
        """
        adj = self._ongoing if ongoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x"""
        v = Vertex(x)
        self._ongoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = Edge(u, v, x)
        self._ongoing[u][v] = e
        self._incoming[v][u] = e
