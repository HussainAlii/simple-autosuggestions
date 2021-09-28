import os

import networkx as nx
from pylab import plt

from autosuggestions.LinkedList import LinkedList


class GraphVisualizer:

    def __init__(self, tree, start_with):
        self.graph = nx.Graph()
        self.__labels = {}
        self.__colors = ['red']  # add root color

        self.graph.add_node(0)  # create root node
        self.__labels[0] = "Root"  # add root label

        print("Please wait...")
        if start_with == '':  # start with the root
            self.traverse_nodes(nodes=tree.root.nodes, root_index=0)
        else:
            result = tree.search_node(string=start_with)
            if result:
                node, _, index = result
                self.traverse_nodes(nodes=node.nodes, root_index=index)

    def __len__(self):
        return len(self.__colors)

    def traverse_nodes(self, nodes: LinkedList, root_index):
        for node in nodes:
            self.graph.add_edge(root_index, node.key)
            self.__labels[node.key] = node.char
            self.__colors.append('#FF00FF' if node.isWord else '#00b4d9')
            self.traverse_nodes(nodes=node.nodes, root_index=node.key)

    def visualize(self, font_size, figure_size, node_size):
        if font_size==5 and figure_size==(50, 50) and node_size==80: # if all default values
            if len(self) <= 500: # only 500 or less exist
                font_size, figure_size, node_size  = 10, (15,15), 100

        plt.figure(figsize=figure_size)

        nx.draw_kamada_kawai(self.graph, font_size=font_size, labels=self.__labels, with_labels=True,
                             node_color=self.__colors, node_size=node_size) # draw as kamada_kawai

        plt.savefig("graph.pdf", bbox_inches='tight', pad_inches=0)
        print('Graph saved as graph.pdf!')
        print('Opening File...')
        os.system("graph.pdf")
        plt.show()
