"""
395. Longest Substring with At Least K Repeating Characters
leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters

Given a string s and an integer k, return the length of the longest substring of s
such that the frequency of each character in this substring is greater than or equal to k.

"""

from collections import Counter
class Solution(object):
    def longestSubstring(self, s: str, k: int) -> int:
      max_len = 0
      def helper(substr: str) -> None:
        nonlocal max_len
        counts = Counter(substr)
        if all(c >= k for c in counts.values()):
          max_len = max(max_len, len(substr))
          return
        split_chars = set(char for char, count in counts.items() if count < k)
        i = 0
        for j, c in enumerate(substr):
          if c in split_chars:
            helper(substr[i:j])
            i = j+1
        helper(substr[i:j+1])
        
      helper(s)
      return max_len
  
solver = Solution()
print(solver.longestSubstring("aaabb", 3))
print(solver.longestSubstring("ababbc", 2))