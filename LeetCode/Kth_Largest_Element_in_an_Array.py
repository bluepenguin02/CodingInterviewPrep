"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

"""

# Method 1: min heap, O(k + (n-k)log(k))
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        return heap[0]
    
solver = Solution()
print(solver.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(solver.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))

# Method 2: O(n) on average
from random import randint
class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        k_mod = len(nums) - k + 1
        while r - l >= 0:
            piv_i = randint(l, r)
            piv = nums[piv_i]
            nums[l], nums[piv_i] = nums[piv_i], nums[l]
            i1 = l + 1
            i2 = l + 1
            for i3 in range(l + 1, r + 1):
                if nums[i3] < piv:
                    nums[i3], nums[i2] = nums[i2], nums[i3]
                    i2 += 1
                elif nums[i3] == piv:
                    nums[i1], nums[i3], nums[i2] = nums[i3], nums[i2], nums[i1]
                    i1 += 1
                    i2 += 1
            if l + (i2 - i1) < k_mod <= i2:  # equal to pivot
                return piv
            elif l < k_mod <= l + (i2 - i1): # less than pivot
                k_mod += i1 - l
                l = i1
                r = i2 -1
            else: # greater than pivot
                l = i2
        return -1
    
solver = Solution2()
print(solver.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(solver.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))