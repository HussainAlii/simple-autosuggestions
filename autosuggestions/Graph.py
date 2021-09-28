class Graph:
    def __init__(self):
        self.__num_of_nodes = 0
        self.__num_of_edge = 0
        self.__adjacent_list = {}

    @property
    def nodes(self):
        return self.__num_of_nodes

    @property
    def edges(self):
        return self.__num_of_edge

    def add_vertex(self, node):
        self.__adjacent_list[node] = []
        self.__num_of_nodes += 1

    def add_edge(self, node1, node2):
        self.__adjacent_list[node1].append(node2)
        self.__adjacent_list[node2].append(node1)
        self.__num_of_edge += 1

    def showConnections(self):
        print(self.__adjacent_list)
        print("---------------")
        for k, v in self.__adjacent_list.items():
            print("Vertex " + str(k) + " --> " + ",".join(str(s) for s in v))

        print("# of Total Nodes: {n}\n# of Total Edges: {e}".format(n=self.nodes, e=self.edges))

    def get_edge_list(self):
        return self.__adjacent_list