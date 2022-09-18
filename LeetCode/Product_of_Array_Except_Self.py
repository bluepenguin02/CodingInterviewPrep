"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of
all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return [0]
                
        prod = [0] * len(nums)
        prod[-1] = nums[-1]
        for i in reversed(range(1, len(nums)-1)):
            prod[i] = nums[i]*prod[i+1]
        prod[0] = prod[1]
        cumprod = nums[0]
        for i in range(1, len(nums)-1):
            prod[i] = cumprod * prod[i+1]
            cumprod *= nums[i]
        prod[-1] = cumprod
        
        return prod