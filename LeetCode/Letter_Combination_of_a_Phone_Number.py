"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not
map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        curr = []
        prev = ['']
        for d in digits:
            for c in map[d]:
                for s in prev:
                    curr.append(s+c)
            prev = curr
            curr = []
        return prev
    
if __name__ == '__main__':
    solver = Solution()
    print(solver.letterCombinations('23'))