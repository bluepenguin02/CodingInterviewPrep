"""
326. Power of Three
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        base = 3
        if n < 1:
            return False
        
        while n >= 1:
            if int(n) != n:
                return False
            if n == 1:
                return True
            n = n/base # type: ignore
    
        return False
    
solver = Solution()
print(solver.isPowerOfThree(27))
print(solver.isPowerOfThree(0))
print(solver.isPowerOfThree(-1))