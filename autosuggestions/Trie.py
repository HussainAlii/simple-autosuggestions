from autosuggestions.LinkedList import LinkedList
from autosuggestions.Visualizer import GraphVisualizer


class TrieNode:
    def __init__(self, char, key: int, nodes=None, isWord=False, called_times=0):
        self.char = char
        self.isWord = isWord
        self.nodes = nodes
        self.key = key
        self.called_times = called_times  # number of times this node has been called

        if nodes is None:
            self.nodes = LinkedList()  # create an empty LinkedList if not exist

    def increment_called_times(self, increment_by: int = 1):
        self.called_times = self.called_times + increment_by

    def __str__(self):
        return str(self.char)


class TrieTree:
    def __init__(self):
        self.root = TrieNode('', key=0)  # create an empty root node
        self.__length = 1

    def __len__(self):
        return self.__length

    def print_all(self, currentNode=None):
        if currentNode is None:
            currentNode = self.root
        print(currentNode.char)
        if currentNode.nodes:
            for c in currentNode.nodes:
                self.print_all(currentNode=c)

    def add(self, string):
        currentNode = self.root
        for i, c in enumerate(string):
            node = self.__get_node_from_char(currentNode, c)

            if node:
                node, _ = node
            else:
                node = TrieNode(c, key=self.__length, isWord=len(string) == i + 1)
                self.__length += 1
                currentNode.nodes.append(node)

            currentNode = node

            if len(string) == i + 1:
                currentNode.isWord = True
                return

    def search_node(self, string, currentNode=None):
        if currentNode is None:
            currentNode = self.root

        prev_node = currentNode
        index = None

        for i, c in enumerate(string):
            if len(string) - 1 == i:
                prev_node = currentNode

            result = self.__get_node_from_char(currentNode, char=c)
            if result:
                currentNode, index = result

            else:
                return False
        return currentNode, prev_node, index

    def get_suggestions(self, string, top: int = None):
        self.__list = LinkedList()
        self.__num_of_words = 0
        result = self.search_node(string)
        if result:
            node, prev_list, prev_index = result
            self.__get_word(node, string, original=string, nodes_List=prev_list.nodes, node_index=prev_index, top=top)

        return [string for string, _ in self.__list]

    def __get_word(self, node, string="", nodes_List: LinkedList = None, node_index: int = None, original="", top=None):
        if node:
            if node.isWord and string != "":
                if original == string:  # if the string same as the search one increment by Two
                    node.increment_called_times(5)  # increment by 5
                else:  # if the string similar to the search one increment by One
                    node.increment_called_times(2)  # increment by 1

                if nodes_List is not None:
                    nodes_List.sort_by_popularity(node_index=node_index,
                                                  called_times=node.called_times)  # sort linkedlist after incrementing the called_times

                if top is not None and self.__num_of_words > top - 1:
                    return

                self.__list.add_by_popularity(string, node.called_times)
                self.__num_of_words += 1

            for index, n in enumerate(node.nodes):
                string += n.char
                self.__get_word(node=n, string=string, nodes_List=node.nodes, node_index=index, top=top)
                string = string[:len(string) - 1]

    def __get_node_from_char(self, current_node, char):  # return node from multiple nodes that have specific char
        if current_node:
            for i, node in enumerate(current_node.nodes):
                if node.char == char:
                    return node, i

        return None

    def import_from_txt(self, fileLocation: str):
        with open(fileLocation) as file:
            for line in file:
                self.add(line.strip())

    def run(self):
        x = input("Write Any String, or 0 to exit:\n")
        while x:
            x = self.get_suggestions(x)
            print(x)
            x = input("Write Any String, or 0 to exit:\n")

    def visualize(self):
        visual = GraphVisualizer(self)
        visual.visualize()
