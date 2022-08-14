class Graph:
    def __init__(self):
        self.adj_list = {}
        self.mylist = []

    def add_node(self, node):
        if node not in self.mylist:
            self.mylist.append(node)

        else:
            print("Node ", node, " already exists!")

    def add_edge(self, node1, node2):
        temp = []
        if node1 in self.mylist and node2 in self.mylist:
            if node1 not in self.adj_list:
                temp.append(node2)
                self.adj_list[node1] = temp

            elif node1 in self.adj_list:
                temp.extend(self.adj_list[node1])
                temp.append(node2)
                self.adj_list[node1] = temp

        else:
            print("Nodes don't exist!")

    def graph(self):
        for node in self.adj_list:
            print(node, " ---> ", [i for i in self.adj_list[node]])


if __name__ == '__main__':
    g = Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    # Adding edges
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(3, 4)
    g.add_edge(4, 0)

    # Printing the graph
    g.graph()

    # Printing the adjacency list
    print(g.adj_list)
