class Edge:
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        """use Graphs's insert_edge(u, v, x)"""
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """Return (u,v) tuple for vertices u and v"""
        return self._origin, self._destination

    def opposite(self, v):
        """
        :param v:
        :return: element associated with the edge
        """
        return self._destination if v is self._origin else self._origin

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))
