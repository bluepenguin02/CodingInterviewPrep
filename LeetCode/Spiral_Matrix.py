"""
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

"""

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    last_top = -1
    last_right = len(matrix[0])
    last_bottom = len(matrix)
    last_left = -1
    
    result = []
    
    
    while last_top+1 < last_bottom and last_left+1 < last_right:
        # top
        result.extend(matrix[last_top+1][last_left+1:last_right])
        last_top += 1
        
        # right
        for i in range(last_top+1, last_bottom):
            result.append(matrix[i][last_right-1])
        last_right -= 1
        
        # bottom
        result.extend(reversed(matrix[last_bottom-1][last_left+1:last_right]))
        last_bottom -= 1
        
        # left
        for i in range(last_bottom-1, last_top, -1):
            result.append(matrix[i][last_left+1])
        last_left += 1
        
    r = len(matrix)
    c = len(matrix[0])
    return result[:r*c]

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))