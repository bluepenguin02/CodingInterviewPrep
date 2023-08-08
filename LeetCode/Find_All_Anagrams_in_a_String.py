"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p) or not s or not p:
            return []
        result = []
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
                            
        if self.counters_match(s_count, p_count):
            result.append(0)

        for i in range(1, len(s)-len(p)+1):
            s_count[s[i-1]] -= 1
            s_count[s[i+len(p)-1]] += 1
            if self.counters_match(s_count, p_count):
                result.append(i)

        return result

    def counters_match(self, s_count: Counter, p_count: Counter) -> bool:
        match = True
        for c, count in p_count.items():
            if s_count[c] != count:
                match = False
        return match

solver = Solution()

print(solver.findAnagrams(s = "cbaebabacd", p = "abc"))
print(solver.findAnagrams(s = "abab", p = "ab"))