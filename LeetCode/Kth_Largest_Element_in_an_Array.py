"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

"""

# Method 1: min heap
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