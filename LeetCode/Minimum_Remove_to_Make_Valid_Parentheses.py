"""
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = []
        for i, c in enumerate(s):
          if c == '(':
            stack.append(i)
          elif c == ')':
            if stack:
              stack.pop()
            else:
              to_remove.append(i)

        to_remove.extend(stack)
        to_remove.sort()

        j = 0
        result = []
        for i, c in enumerate(s):
          if j<len(to_remove) and i==to_remove[j]:
            j+=1
          else:
            result.append(c)

        return ''.join(result)
    
solver = Solution()
print(solver.minRemoveToMakeValid("lee(t(c)o)de)"))
print(solver.minRemoveToMakeValid("a)b(c)d"))
print(solver.minRemoveToMakeValid("))(("))