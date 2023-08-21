"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

* WordDictionary() Initializes the object.
* void addWord(word) Adds word to the data structure, it can be matched later.
* bool search(word) Returns true if there is any string in the data structure that matches
  word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""
from collections import defaultdict

class WordDictionary:

    def __init__(self):
      Trie = lambda : defaultdict(Trie)
      self.trie = Trie()

    def addWord(self, word: str) -> None:
      trie = self.trie
      for c in word:
        trie = trie[c]
      trie['$'] = None # type: ignore
      return

    def search(self, word: str) -> bool:
      def helper(i: int, trie):
        if i == len(word):
          if '$' in trie:
            return True
          else:
            return False
        if word[i] == '.':
          for c, subtrie in trie.items():
            if c != '$' and helper(i+1, subtrie):
              return True
        elif word[i] in trie:
          return helper(i+1, trie[word[i]])
        return False

      return helper(0, self.trie)
  
  
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))