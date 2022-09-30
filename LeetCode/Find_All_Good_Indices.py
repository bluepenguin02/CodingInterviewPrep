"""
https://leetcode.com/problems/find-all-good-indices/

2420. Find All Good Indices

You are given a 0-indexed integer array nums of size n and a positive integer k.

We call an index i in the range k <= i < n - k good if the following conditions are satisfied:

The k elements that are just before the index i are in non-increasing order.
The k elements that are just after the index i are in non-decreasing order.
Return an array of all good indices sorted in increasing order.
"""


class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        before_ok_idx = self.non_increasing_prefix(nums[:k])
        after_ok_idx = k + 1 + self.non_decreasing_suffix(nums[k+1:2*k+1])
        result = []
        
        for i in range(k, len(nums) - k - 1):
            if i-before_ok_idx == k and after_ok_idx == i+1:
                result.append(i)
            
            if nums[i-1] < nums[i]:
                before_ok_idx = i
            elif i - before_ok_idx == k:
                before_ok_idx += 1
            
            if nums[i+k] > nums[i+k+1]:
                after_ok_idx = i+k+1
            elif after_ok_idx == i+1:
                after_ok_idx += 1
        
        i = len(nums) - k - 1
        if i-before_ok_idx == k and after_ok_idx == i+1:
                result.append(i)
        
        return result
                
        
    def non_increasing_prefix(self, arr: list) -> bool:
        for i in reversed(range(1, len(arr))):
            if arr[i-1] < arr[i]:
                return i
        return 0
        
    def non_decreasing_suffix(self, arr: list) -> bool:
        for i in reversed(range(1, len(arr))):
            if arr[i-1] > arr[i]:
                return i
        return 0