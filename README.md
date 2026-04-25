# Autocomplete-Search-Engine
A Python implementation of a prefix-based autocomplete system using a Trie data structure.

How to run:
Run the command to import dictionary: curl -o words.txt https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt

Then run: python main.py

Required input:
A plain text file with one word per line, with blank lines and whitespace ignored.

Algorithm:
The program uses Trie Prefix Search:
1. To begin, every word from file is inserted into a Trie, where each edge represents a character and each path is a prefix
2. When the user enters a prefix, the search walks down the tree one character at a time following the prefix path
3. From the node where the prefix ends, the recursive traversal collects the words beneath that node
4. Results are returned alphabetically

Running complexity:
Insert a word of length k -> O(k)
