"""
https://leetcode.com/problems/combination-sum-iv/

377. Combination Sum IV

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums.sort()
        memo = {}

        def helper(curr_target: int) -> int:
            if curr_target in memo:
                return memo[curr_target]
            if curr_target == 0:
                return 1
            count = 0
            for num in nums:
                if num <= curr_target:
                    count += helper(curr_target - num)
                else:
                    break
            memo[curr_target] = count
            return count

        return helper(target)
