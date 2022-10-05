"""
https://leetcode.com/problems/counting-bits/

338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

This is a linear time (O(n)) algorithm.  It starts with 0 in the list, then for every power of 2,
goes back to the start of the list, then appends a copy of the list, but adds 1 to every element in the copy.
"""

from math import log2

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0]
        if n > 0:
            max_power = int(log2(n))
            for power in range(max_power+1):
                for i in range(min(2**power, n-2**power+1)):
                    result.append(1+result[i])
        return result