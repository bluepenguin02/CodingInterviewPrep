"""
307. Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable

Given an integer array nums, handle multiple queries of the following types:

1. Update the value of an element in nums.
2. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

* NumArray(int[] nums) Initializes the object with the integer array nums.
* void update(int index, int val) Updates the value of nums[index] to be val.
* int sumRange(int left, int right) Returns the sum of the elements of nums between indices
left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


I use a tree to efficiently allow keeping track of the range sum.
"""

from math import ceil, log2

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.levels = ceil(log2(len(nums))) + 1
        self.tree = [[] for _ in range(self.levels)]
        self.tree[self.levels-1] = nums
        for level in range(self.levels-2, -1, -1):
            self.tree[level] = [0]*ceil(len(self.tree[level+1])/2)
            for i, num in enumerate(self.tree[level+1]):
                self.tree[level][i//2] += num

    def update(self, index: int, val: int) -> None:
        prev_num = self.tree[self.levels-1][index]
        i = index
        for level in range(self.levels-1, -1, -1):
            self.tree[level][i] += val-prev_num
            i = i//2

    def sumRange(self, left: int, right: int) -> int:
        cum_sum_left = 0
        if left > 0:
            cum_sum_left = self.cumSum(left-1)

        cum_sum_right = self.cumSum(right)
        return cum_sum_right - cum_sum_left

    def cumSum(self, index: int) -> int:
        to_subtract = 0
        left_i = index
        for level in range(self.levels-2, -1, -1):
            prev_i = left_i
            left_i//=2
            if prev_i % 2 == 0 and prev_i + 1 < len(self.tree[level+1]):
                to_subtract += self.tree[level+1][prev_i+1]
        return self.tree[0][0] - to_subtract