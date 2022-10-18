"""
https://leetcode.com/problems/word-break/description/

139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Note: My solution uses recursion.  There's a tabulation method that's faster.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        memo = {}
        def helper(s_start_i: int) -> bool:
            if s_start_i in memo:
                return memo[s_start_i]
            if s_start_i == len(s):
                return True
            j = s_start_i + 1
            while j <= len(s):
                if s[s_start_i:j] in word_set and helper(j):
                    return True
                j+=1
            memo[s_start_i] = False
            return False
        return helper(0)