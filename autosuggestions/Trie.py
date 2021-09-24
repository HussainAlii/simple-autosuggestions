class TrieNode:
    def __init__(self, char, nodes=None, isWord=False, called_times=0):
        self.char = char
        self.isWord = isWord
        self.nodes = nodes
        self.__called_times = called_times  # number of times this node has been called
        if nodes is None:
            self.nodes = []

    @property
    def called_times(self):
        return self.__called_times

    def increment_called_times(self):
        self.__called_times += 1

    def __str__(self):
        return str(self.char)


class Trie:
    def __init__(self):
        self.root = TrieNode('')  # create an empty root node

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

            if not node:
                node = TrieNode(c, isWord=len(string) == i + 1)
                currentNode.nodes.append(node)

            currentNode = node

            if len(string) == i + 1:
                currentNode.isWord = True
                return

    def search_node(self, string, currentNode=None):
        if currentNode is None:
            currentNode = self.root
        for c in string:
            node = self.__get_node_from_char(currentNode, char=c)
            if node:
                currentNode = node
            else:
                return False
        return currentNode

    def get_suggestions(self, string):
        self.__list = []
        node = self.search_node(string)
        if node:
            self.__get_word(node, string)

        return self.__list

    def __get_word(self, node, s=""):
        if node:
            if node.isWord and s != "":
                node.increment_called_times() # increment by 1
                self.__list.append(s)

            for i in node.nodes:
                s += i.char
                self.__get_word(i, s)
                s = s[:len(s) - 1]

    def __get_node_from_char(self, current_node, char):
        if current_node:
            for node in current_node.nodes:
                if node.char == char:
                    return node

        return None

    def import_from_txt(self, fileLocation: str):
        with open(fileLocation) as file:
            for line in file:
                self.add(line.strip())

    def run(self):
        x = input("Write any chars, 0 to exit:\n")
        while x:
            x = self.get_suggestions(x)
            print(x)
            x = input("Write any chars, 0 to exit:\n")
