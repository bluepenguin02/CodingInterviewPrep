"""
283. Move Zeroes
leetcode.com/problems/move-zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        j = i
        for i in range(j+1,len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return
    
solver = Solution()
nums = [0,1,0,3,12]
solver.moveZeroes(nums)
print(nums)
nums = [0]
solver.moveZeroes(nums)
print(nums)