"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

* Trie() Initializes the trie object.

* void insert(String word) Inserts the string word into the trie.

* boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
  and false otherwise.

* boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has
  the prefix prefix, and false otherwise.
"""

from collections import defaultdict

class Trie:
    def __init__(self):
      Trie = lambda: defaultdict(Trie)
      self.tree = Trie()

    def insert(self, word: str) -> None:
      t = self.tree
      for c in word:
        t = t[c]
      t['$'] = None # type: ignore
      return

    def search(self, word: str) -> bool:
      t = self.tree
      for c in word:
        if c not in t:
          return False
        else:
          t = t[c]
      if '$' in t:
        return True
      return False

    def startsWith(self, prefix: str) -> bool:
      t = self.tree
      for c in prefix:
        if c not in t:
          return False
        else:
          t = t[c]
      return True
  
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app") )    # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))     # return True