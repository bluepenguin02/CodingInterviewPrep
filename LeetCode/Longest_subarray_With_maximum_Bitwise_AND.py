"""
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

2419. Longest Subarray With Maximum Bitwise AND

You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums.
Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

Note: There is a way to do this in just 1 pass
"""

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_num = max(nums)
        low = -1
        max_len = 0
        for hi in range(len(nums)):
            if max_num & nums[hi] != max_num:
                low = hi
            else:
                max_len = max(max_len, hi - low)
        return max_len
                    