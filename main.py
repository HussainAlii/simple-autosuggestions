import autosuggestions

def main():

    trie = autosuggestions.Trie() # create new separate Trie

    trie.import_from_txt('words.txt') # add multiple words from .txt file
    trie.add("ayy") # or add word individually

    trie.run() # try it out

if __name__ == '__main__':
    main()

