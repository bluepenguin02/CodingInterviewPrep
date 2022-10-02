"""
https://leetcode.com/problems/3sum/

15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Note: There is a faster way to do this, by sorting the numbers, iterating over them, then working
your way in from the ends to find the other numbers.
"""

from collections import Counter

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        table = Counter(nums)
        result = set()
        for num1, count1 in table.items():
            for num2 in table.keys():
                if num1 != num2 or count1 > 1:
                    triplet = ()
                    target = -num1 - num2
                    if target in table:
                        count_target = table[target]
                    else:
                        count_target = 0
                        
                    if num1 == num2 == target and count_target >= 3:
                        triplet = tuple([num1, num2, target])
                    elif (num1 == target or num2 == target) and num1 != num2 and count_target >= 2 or \
                            num1 != num2 and num1 != target and num2 != target and count_target > 0:
                        triplet = tuple(sorted([num1, num2, target]))
                    result.add(triplet)
        result.discard(())
        return list(result)