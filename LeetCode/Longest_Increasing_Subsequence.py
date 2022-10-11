"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence
of the array [0,3,1,6,2,2,7].

For a description of the solution, see:
https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326552/optimization-from-brute-force-to-dynamic-programming-explained
"""

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        working = [nums[0]]
        for num in nums[1:]:
            if num > working[-1]:
                working.append(num)
            else:
                i = bisect_left(working, num)
                working[i] = num
        return len(working)