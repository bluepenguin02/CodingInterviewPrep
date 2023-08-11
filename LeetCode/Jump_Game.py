"""
55. Jump Game
https://leetcode.com/problems/jump-game

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_jump = 0
        for i, jump in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i+jump)
            if max_jump >= len(nums) - 1:
                return True
                
        return False
    
solver = Solution()
print(solver.canJump([2,3,1,1,4]))
print(solver.canJump([3,2,1,0,4]))