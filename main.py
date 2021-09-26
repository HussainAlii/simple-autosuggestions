from autosuggestions import SimpleAutosuggestions

def main():

    autosuggestions = SimpleAutosuggestions() # create new separate Trie

    autosuggestions.import_from_txt('words.txt') # add multiple words from .txt file
    autosuggestions.add("ayy") # or add word individually

    autosuggestions.get_suggestions("ay") # get suggestions

    autosuggestions.run() # try it out

if __name__ == '__main__':
    main()

