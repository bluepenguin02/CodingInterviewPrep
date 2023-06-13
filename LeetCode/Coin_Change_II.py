"""
518. Coin Change II
leetcode.com/problems/coin-change-ii

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        combos = [0]*(amount+1)
        combos[0] = 1
        for c in coins:
            for a in range(amount+1-c):
                combos[a+c] += combos[a]
        return combos[-1]
    
solver = Solution()
print(solver.change(5, [1,2,5]))
print(solver.change(3, [2]))
print(solver.change(10,[10]))
