"""
https://leetcode.com/problems/climbing-stairs/description/

70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: I generalized it by adding a max_step variable, so the youcan take anywhere from 1 to max_step each time.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        max_step = 2
        ways = [0] * (n+1)
        ways[0] = 1
        for i in range(0, n):
            for j in range(1, max_step+1):
                if i + j <= n:
                    ways[i+j] += ways[i]
        return ways[n]