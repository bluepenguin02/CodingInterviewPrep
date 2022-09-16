"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        max_length = 0
        substr_chars = {}
        for i, c in enumerate(s):
            if c not in substr_chars:
                substr_chars[c] = i
                length += 1
            else:
                for j in range(i-length, substr_chars[c]):
                    substr_chars.pop(s[j])
                length = i - substr_chars[c]
                substr_chars[c] = i
            max_length = max(length, max_length)
        return max_length
    
if __name__ == '__main__':
    test = 'abba'
    solu = Solution()
    print(solu.lengthOfLongestSubstring(test))
