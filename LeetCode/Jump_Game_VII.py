"""
1871. Jump Game VII
leetcode.com/problems/jump-game-vii

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

* i + minJump <= j <= min(i + maxJump, s.length - 1), and
* s[j] == '0'.

Return true if you can reach index s.length - 1 in s, or false otherwise.
"""

from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        queue = deque([0])
        for i, c in enumerate(s[minJump:], start=minJump):
            if queue[0] < i-maxJump:
                queue.popleft()
            if not queue:
                return False
            if c=='0' and i-maxJump <= queue[0] <= i-minJump:
                queue.append(i)
        return queue[-1] == len(s)-1

solver = Solution()
print(solver.canReach("011010", 2, 3))
print(solver.canReach("01101110", 2, 3))