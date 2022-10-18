"""
https://leetcode.com/problems/longest-common-subsequence/description/

1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is
no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                match = c1 == c2
                table[i+1][j+1] = max(table[i][j]+match, table[i][j+1], table[i+1][j])
        return table[-1][-1]