## Tapioca-Python

### Overview

This is my solution to the most enjoyable take-home problem provided by Tapioca:

> Please write a function that accepts a single string as input, and that returns a list of English words that can be created using some combination of the letters in the input string.
>
> Example input: "oogd"
> Example output: ["good", "god", "dog", "goo", "do", "go"]
> 
> You can assume you'll be given an array of strings that enumerates all valid English words. To determine whether a word is a valid word, you can simply check for its presence in the array (e.g., `WORDS.includes(word)`)

I fully intended to write the code in both Python and Typescript, but life got in the way and I've only written my solution in Python as of yet. I found a sample [wordlist on Github](https://github.com/dwyl/english-words) that was helpful for testing, but it's a little more expansive than the standard Scrabble wordlist.

### Usage

The code is limited to a single file `wordgen.py`. In order to run the code, 

1) clone the git repo:

`git clone git@github.com:damzam/Tapioca-Python.git`

2) cd into into `Tapioca-Python`

`cd Tapioca-Python`

3) and run the tests in `wordgen.py`

`python3 wordgen.py`

### Notes on Code Structure and Performance

The algorithm in the function `generate_words` performs a recursive depth-first search of a tree that represents each permutation of the characters provided (obviating the need to resort to [itertools](https://docs.python.org/3/library/itertools.html)). With O(1) checks for membership to the `WORDLIST` set, the computational complexity is the number of permutations (which corresponds to the number of leaf nodes on the tree): O(len(chars)!). But because we're performing a depth-first search as opposed to a BFS, the memory/space complexity is far cheaper: O(min(len(chars)|results)).

I've made use of sets to avoid duplicates in cases where multiple identical characters are in the provided query string (as there would be paths in the tree with identical values), and I have made no effort to eliminate this potential inefficiency given that premature optimizations are the root of all evil and such. If a sorted list is the desired output, one could just invoke the function with:

`print(sorted(generate_words('oogd')))`

If you have any questions, please don't hesitate to reach out to me!