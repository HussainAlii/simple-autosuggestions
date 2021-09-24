from autosuggestions.Trie import Trie
def main():
    trie = Trie()
    trie.import_from_txt('words.txt')
    trie.run()

if __name__ == '__main__':
    main()

