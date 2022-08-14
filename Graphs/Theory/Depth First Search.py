from collections import defaultdict

# This class represents a directed graph using adjacency list representation

class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def dfs(self, visited, node):  # function for dfs
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbour in self.graph[node]:
                self.dfs(visited, neighbour)


# Driver code
# Create a graph given in the above diagram

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.dfs(node=2, visited=set())
