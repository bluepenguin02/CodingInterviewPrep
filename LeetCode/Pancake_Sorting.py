"""
969. Pancake Sorting
https://leetcode.com/problems/pancake-sorting

Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the
sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any
valid answer that sorts the array within 10 * arr.length flips will be judged as correct.
"""

class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        result = []
        for i in range(len(arr)-1, 0, -1):
            j_max = 0
            for j in range(1, i+1):
                j_max = j if arr[j] > arr[j_max] else j_max
            result.append(j_max+1)
            arr[:j_max+1] = arr[j_max::-1]
            result.append(i+1)
            arr[:i+1] = arr[i::-1]
        return result
    
solver = Solution()
print(solver.pancakeSort([3,2,4,1]))
print(solver.pancakeSort([1,2,3]))