"""
136. Single Number
https://leetcode.com/problems/single-number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

# Method 1: use XOR
class Solution: # type: ignore
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
    
solver = Solution()
print(solver.singleNumber([2,2,1]))
print(solver.singleNumber([4,1,2,1,2]))
print(solver.singleNumber([1]))

# Method 2: use quick select (much slower)

from random import randint

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        piv_count = 0
        while piv_count % 2 == 0:
            piv_i = randint(l, r)
            piv = nums[piv_i]
            nums[l], nums[piv_i] = nums[piv_i], nums[l]
            i = l+1
            j = l+1
            k = l+1
            while k <= r:
                if nums[k] < piv:
                    nums[j], nums[k] = nums[k], nums[j]
                    j += 1
                elif nums[k] == piv:
                    nums[i], nums[k], nums[j] = nums[k], nums[j], nums[i]
                    i += 1
                    j += 1
                k += 1
            piv_count = i - l
            if piv_count % 2 != 0:
                return piv
            if (k - j) % 2 != 0:
                l = j
            else:
                l = i
                r = k - 1
        return -1

solver = Solution()
print(solver.singleNumber([2,2,1]))
print(solver.singleNumber([4,1,2,1,2]))
print(solver.singleNumber([1]))