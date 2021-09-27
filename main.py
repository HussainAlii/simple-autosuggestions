from autosuggestions import SimpleAutosuggestions
from autosuggestions.LinkedList import LinkedList


def main():
    autosuggestions = SimpleAutosuggestions()  # create new separate Trie

    autosuggestions.import_from_txt('words.txt')  # add multiple words from .txt file
    autosuggestions.add("autosuggestions")  # or add word individually

    print(autosuggestions.get_suggestions("a"))  # get all suggestions
    print(autosuggestions.get_suggestions("a", top=5))  # get top 5 popular suggestions

    autosuggestions.run()  # try it out


if __name__ == '__main__':
    main()
