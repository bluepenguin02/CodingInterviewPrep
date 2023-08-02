"""
67. Add Binary
https://leetcode.com/problems/add-binary

Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add2(c1, c2):
            if c1 == c2 == '0':
                return ('0', '0')
            if (c1 == '1') ^ (c2 == '1'):
                return ('0', '1')
            return ('1', '0')

        if len(a) < len(b):
            s1 = b
            s2 = '0'*(len(b)-len(a)) + a
        else:
            s1 = a
            s2 = '0'*(len(a)-len(b)) + b

        result = []
        carry = '0'

        for c1, c2 in zip(reversed(s1), reversed(s2)):
            old_carry = carry
            carry1, v1 = add2(c1, c2)
            carry2, v2 = add2(v1, old_carry)
            result.append(v2)
            carry = '1' if (carry1 == '1') ^ (carry2 == '1') else '0'

        if carry == '1':
            result.append(carry)

        result.reverse()
        return ''.join(result)


solver = Solution()
print(solver.addBinary("11", "1"))
print(solver.addBinary("1010", "1011"))