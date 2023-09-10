"""
2272. Substring With Largest Variance
https://leetcode.com/problems/substring-with-largest-variance

The variance of a string is defined as the largest difference between the number of occurrences of any
2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible
among all substrings of s.

A substring is a contiguous sequence of characters within a string.
"""

from collections import Counter, defaultdict

def largestVariance(s: str) -> int:
    char_counts = Counter(s)
    char_idxs = defaultdict(list)
    
    for i, c in enumerate(s):
        char_idxs[c].append(i)

    max_variance = 0
    for major in char_counts.keys():
        for minor in char_counts.keys():
            if major==minor or char_counts[major] <= max_variance + 1:
                continue
            major_count = 0
            minor_count = 0
            rest_minor = char_counts[minor]

            for i in sorted(char_idxs[major] + char_idxs[minor]):
                c = s[i] # type: ignore
                if c==major:
                    major_count += 1
                elif c==minor:
                    minor_count += 1
                    rest_minor -= 1
                if minor_count > 0:
                    max_variance = max(max_variance, major_count - minor_count)
                if major_count < minor_count and rest_minor > 0:
                    major_count = 0
                    minor_count = 0
            
    return max_variance

print(largestVariance("aababbb"))
print(largestVariance("abcde"))