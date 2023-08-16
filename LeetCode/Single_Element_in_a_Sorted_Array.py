"""
540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array

You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

"""

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l = 0
        r = len(nums)-1

        while r > l:
            mid = l + (r-l)//2
            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid-1] == nums[mid]):
                l = mid + 1
            else:
                r = mid
        
        return nums[l]
    
solver = Solution()
print(solver.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(solver.singleNonDuplicate([3,3,7,7,10,11,11]))