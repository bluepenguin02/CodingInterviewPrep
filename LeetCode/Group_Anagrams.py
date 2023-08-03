"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      anagrams = defaultdict(list)
      for str in strs:
        anagrams[''.join(sorted(str))].append(str)

      return anagrams.values()
  
solver = Solution()
print(solver.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))