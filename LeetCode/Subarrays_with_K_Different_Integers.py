"""
992. Subarrays with K Different Integers
leetcode.com/problems/subarrays-with-k-different-integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
"""

from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k-1)

    def atMostKDistinct(self, nums: list[int], k: int) -> int:
        tracker = defaultdict(int)
        count = 0
        j = 0
        for i, num in enumerate(nums):
            tracker[num] += 1
            while len(tracker) > k:
                tracker[nums[j]] -= 1
                if tracker[nums[j]] == 0: del tracker[nums[j]]
                j += 1
            count += i - j + 1
        return count
    
solver = Solution()
print(solver.subarraysWithKDistinct([1,2,1,2,3], 2))
print(solver.subarraysWithKDistinct([1,2,1,3,4], 3))