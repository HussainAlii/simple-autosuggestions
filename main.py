from autosuggestions import SimpleAutosuggestions


def main():
    # create new separate SimpleAutosuggestions
    autosuggestions = SimpleAutosuggestions()

    # import multiple words from .txt file
    autosuggestions.import_from_txt('words.txt')

    # or add word individually
    autosuggestions.add("autosuggestions")

    # get all suggestions start with 'ax'.
    autosuggestions.get_suggestions("ax")

    # get top 5 popular suggestions start with 'axe'.
    autosuggestions.get_suggestions("axe", top=5)

    # try it out
    autosuggestions.run()

if __name__ == '__main__':
    main()
