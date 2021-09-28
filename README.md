# simple-autosuggestions
A simple and smart way to store, visualize words and get suggestions based on the popularity of the word and inputted characters. Built with Linked List and Trie data structure which helps efficiently store words with time complexity O(L * log N) where L is maximum string length and N is a number of keys in the tree, and retrieve words with time complexity O(L) where L is the maximum string length.

<b>A popular word is any word that has been searched multiple times and more than any other word.</b>

## Usage
  
``` r
# import package
from autosuggestions import SimpleAutosuggestions
  
# create new separate SimpleAutosuggestions
autosuggestions = SimpleAutosuggestions()  

# import multiple words from .txt file 
autosuggestions.import_from_txt('words.txt')
  
# or add word individually    
autosuggestions.add("autosuggestions")


# get all suggestions start with 'ax'.
autosuggestions.get_suggestions("ax")

## output:
['axons', 'axon', 'axminster', 'axles', 'axle', 'axis', 'axioms', 'axiomatic', 'axiom', 'axing', 'axially', 'axial', 'axes', 'axed', 'axe']


# get top 5 popular suggestions start with 'axe'.
autosuggestions.get_suggestions("axe", top=5)

## output:
['axe', 'axed', 'axes']


# try it out
autosuggestions.run()
  
```
  
### Search by popularity
  
<p>Now after searching for words that start with 'axe' in the last example, if we try again and search 'ax', we're going to get all words that start with 'ax' filtered by popularity.</p>
  
``` r
# get all suggestions start with 'ax'.
autosuggestions.get_suggestions("ax")

## output:
['axe', 'axes', 'axed', 'axons', 'axon', 'axminster', 'axles', 'axle', 'axiomatic', 'axioms', 'axiom', 'axing', 'axially', 'axial', 'axis']
  
## the three items in the list (['axe', 'axed', 'axes']) got at the begging of the list because they have been searched already before.
```
  
### visualize words
  
  ![Screenshot 2021-09-28 183028](https://user-images.githubusercontent.com/58237246/135119817-8a1ab149-d7a1-411e-92a4-6fd01eb16169.jpg)
  
  <p align="center" align="center">
  <a href="graph.pdf">Open Image</a>
  </p>
  
  - ![#1589F0](https://via.placeholder.com/15/ff0000/000000?text=+) Root
  - ![#1589F0](https://via.placeholder.com/15/FF00FF/000000?text=+) End of a word
  - ![#1589F0](https://via.placeholder.com/15/00b4d9/000000?text=+) Collection of characters
  
``` r
    # visualize graph
    autosuggestions.visualize(start_with='', font_size=5, figure_size=(50, 50), node_size=80) # default values
        ## start_with: Visualize nodes that start with... by default it visualize the root node.
        
```
  
