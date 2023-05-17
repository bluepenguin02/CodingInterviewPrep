"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      start = 0
      seen = set()
      longest = 0
      for end, c in enumerate(s):
        while c in seen:
          seen.remove(s[start])  
          start += 1
        seen.add(c)
        longest = max(longest, end-start+1)
      return longest

if __name__ == "__main__":
  solver = Solution()
  print(solver.lengthOfLongestSubstring('pwwkewp'))
