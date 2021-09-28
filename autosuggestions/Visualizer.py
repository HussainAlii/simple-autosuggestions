import networkx as nx
from pylab import plt

from autosuggestions.LinkedList import LinkedList


class GraphVisualizer:

    def __init__(self, tree):
        self.graph = nx.Graph()
        self.__labels = {}
        self.__colors = ['red']  # add root color

        self.graph.add_node(0)  # create root node
        self.__labels[0] = "Root"  # add root label

        print("Please wait...")
        self.traverse_nodes(nodes=tree.root.nodes, root_index=0)

    def traverse_nodes(self, nodes: LinkedList, root_index):
        for node in nodes:
            self.graph.add_edge(root_index, node.key)
            self.__labels[node.key] = node.char
            self.__colors.append('#FF00FF' if node.isWord else '#00b4d9')
            self.traverse_nodes(nodes=node.nodes, root_index=node.key)

    def visualize(self):
        nx.draw_shell(self.graph, labels=self.__labels, with_labels=True, node_color=self.__colors, node_size=100)
        # plt.tight_layout()
        plt.savefig("graph.pdf", bbox_inches='tight',pad_inches = 0, dpi = 200)
        print('Graph saved as graph.pdf!')
        plt.show()
