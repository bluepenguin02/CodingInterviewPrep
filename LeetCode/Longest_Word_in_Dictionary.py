"""
720. Longest Word in Dictionary
leetcode.com/problems/longest-word-in-dictionary

Given an array of strings words representing an English Dictionary, return the longest word in words that
can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end
of a previous word. 
"""

class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort(key=len)
        valids = set()

        result = ''
        for w in words:
            prefix = w[:-1]
            if not prefix or prefix in valids:
                valids.add(w)
                if len(w) > len(result) or len(w) == len(result) and w < result:
                    result = w

        return result
    
solver = Solution()
print(solver.longestWord(["w","wo","wor","worl","world"]))
print(solver.longestWord(["a","banana","app","appl","ap","apply","apple"]))