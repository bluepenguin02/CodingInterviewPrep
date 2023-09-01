"""
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix

You are given an m x n integer matrix matrix with the following two properties:

* Each row is sorted in non-decreasing order.
* The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""

# Method 1: be smart about indexing
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while l < r:
            mid = r - (r-l+1) // 2
            row = mid // n
            col = mid - row * n
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid

        row = l // n
        col = l - row * n
        if matrix[row][col] == target:
            return True
        else:
            return False
        
solver = Solution()
print(solver.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(solver.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))

# Method 2: find row then col
class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # first, determine row
        l = 0
        r = m-1
        while l < r:
            mid = r - (r-l+1) // 2
            if matrix[mid][n-1] < target:
                l = mid + 1
            else:
                r = mid
        row = l 

        # second, determine column
        l = 0
        r = n-1
        while l < r:
            mid = r - (r-l+1) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid
        col = l

        if matrix[row][col] == target:
            return True
        else:
            return False
        
solver = Solution2()
print(solver.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(solver.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))