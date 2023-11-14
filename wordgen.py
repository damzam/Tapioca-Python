#!/usr/bin/env python3
"""
Please write a function that accepts a single string as input,
and that returns a list of English words that can be created
using some combination of the letters in the input string.
 
Example input: "oogd"
Example output: ["good", "god", "dog", "goo", "do", "go"]
 
You can assume you'll be given an array of strings that
enumerates all valid English words. To determine whether a
word is a valid word, you can simply check for its presence
in the array (e.g., `WORDS.includes(word)`)
"""
WORDLIST = set(open('words.txt').read().split())


def generate_words(chars, pre=''):
    """
    Recursively create a tree for all permutations of characters with:
      - chars: the remaining characters that can be appended to the prefix
      - pre: the ordered characters descending down the tree recursively...
            can be checked against WORDLIST to see if a valid word is formed
    Return a *set* of words (to avoid duplicates) based on the intersection
    of sets of valid words found by traversing the tree of charcacter
    permutations recursively.
    """
    words = set()
    if pre in WORDLIST:
        # Awesome! We've found a valid word going down this path :)
        words.add(pre)
    for i, char in enumerate(chars):
        # Now let's branch off for each character, removing it from chars
        # and adding it to the sorted prefix `pre`, and make the appropriate
        # recursive calls. Collate the valid words found from the branches
        # of the tree by using python's set intersection operator |=
        words |= generate_words(chars[:i] + chars[i + 1:], pre + char)
    return words
        

def test_generate_words():
    chars = 'oogd'
    valid_words = ['good', 'god', 'dog', 'goo', 'do', 'go']
    results = generate_words(chars)
    for word in valid_words:
        assert word in results

    # Hey, let's make sure the results are all valid words
    for word in results:
        assert word in WORDLIST

    # Let's test to ensure that characters are not used more times
    # than they appear in provided string by removing an 'o'
    chars = 'ogd' 
    results = generate_words(chars)
    for word in ['god', 'dog', 'do', 'go']:
        assert word in results
    for word in ['good', 'goo']:
        assert word not in results


if __name__ == '__main__':
    test_generate_words()