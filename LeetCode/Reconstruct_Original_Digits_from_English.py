"""
423. Reconstruct Original Digits from English
leetcode.com/problems/reconstruct-original-digits-from-english

Given a string s containing an out-of-order English representation
of digits 0-9, return the digits in ascending order.

"""

from collections import Counter

# The first way I came up with, more general and slower
class Solution:
    def originalDigits(self, s: str) -> str:
        max_num = 9
        numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        order_check = [0, 2, 4, 3, 5, 6, 7, 8, 1, 9]
        num_counts = []
        for num in numbers:
            num_counts.append(Counter(num))
        s_counts = Counter(s)

        result = []
        for num in order_check:
            while not num_counts[num] - s_counts:
                s_counts -= num_counts[num]
                result.append(str(num))
        
        result.sort()
        return ''.join(result)
    
solver = Solution()
print(solver.originalDigits("owoztneoer"))
print(solver.originalDigits("fviefuro"))

# The second way, faster but very problem-specific
class Solution2:
    def originalDigits(self, s: str) -> str:
        s_counts = Counter(s)
        res = [0]*10

        res[0] = s_counts['z']
        res[2] = s_counts['w']
        res[4] = s_counts['u']
        res[6] = s_counts['x']
        res[8] = s_counts['g']

        res[1] = s_counts['o'] - res[0] - res[2] - res[4]
        res[3] = s_counts['h'] - res[8]
        res[5] = s_counts['f'] - res[4]
        res[7] = s_counts['v'] - res[5]
        res[9] = s_counts['i'] - res[5] - res[6] - res[8]

        return ''.join([str(i)*res[i] for i in range(10)])
    
solver = Solution2()
print(solver.originalDigits("owoztneoer"))
print(solver.originalDigits("fviefuro"))