"""
115. Distinct Subsequences
leetcode.com/problems/distinct-subsequences

Given two strings s and t, return the number of distinct 
subsequences
 of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.
"""

from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        @cache
        def helper(pos_s: int, pos_t: int) -> int:
            if pos_t == n:
                return 1
            if m - pos_s < n - pos_t:
                return 0
            if s[pos_s] == t[pos_t]:
                return helper(pos_s+1, pos_t+1) + helper(pos_s+1, pos_t)
            else:
                return helper(pos_s+1, pos_t)
        return helper(0,0)
        
        # m, n = len(s), len(t)
        # prev = [0]*(n+1)
        # prev[0] = 1

        # for i in range(1,m+1):
        #     curr = [0]*(n+1)
        #     curr[0] = 1
        #     for j in range(1,n+1):
        #         if s[i-1] == t[j-1]:
        #             prev[j] += prev[j-1]
        #        else:
        #            curr[j] = prev[j]
        #     prev = curr
        # return curr[n]
        
solver = Solution()
print(solver.numDistinct("rabbbit", "rabbit"))
print(solver.numDistinct("babgbag", "bag"))