"""
2434. Using a Robot to Print the Lexicographically Smallest String
https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string

You are given a string s and a robot that currently holds an empty string t.
Apply one of the following operations until s and t are both empty:

* Remove the first character of a string s and give it to the robot. The robot
  will append this character to the string t.
* Remove the last character of a string t and give it to the robot. The robot
  will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.

Example 1:
Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".

Example 2:
Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba".
Perform second operation twice p="ab", s="c", t="".
Perform first operation p="ab", s="", t="c".
Perform second operation p="abc", s="", t="".

Example 3:
Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".

Constraints:
1 <= s.length <= 10^5
s consists of only English lowercase letters.
"""

# Heap solution (slow) O(n*log(n))
import heapq


def robotWithString(s: str) -> str:
    heap = []
    for i, c in enumerate(s):
        heap.append((c, i))
    heapq.heapify(heap)

    t = []
    result = []
    offset = 0
    while heap:
        while t and t[-1] <= heap[0][0]:
            result.append(t.pop())
        if not t or t and heap[0][0] < t[-1]:
            c, i = heapq.heappop(heap)
            t.extend([*s[offset:i+1]])
            offset = i+1
            while heap and heap[0][1] < offset:
                heapq.heappop(heap)

    if t:
        result.extend(reversed(t))

    return ''.join(result)


print(robotWithString("zza"))
print(robotWithString("bac"))
print(robotWithString("bdda"))


# Sorting solution, faster but still (n*log(n))
def robotWithString2(s: str) -> str:
    s_enum = [(c, i) for i, c in enumerate(s)]
    s_enum.sort()

    t = []
    result = []
    offset = 0
    enum_idx = 0
    while enum_idx < len(s_enum):
        while t and t[-1] <= s_enum[enum_idx][0]:
            result.append(t.pop())
        if not t or t and s_enum[enum_idx][0] < t[-1]:
            c, i = s_enum[enum_idx]
            enum_idx += 1
            t.extend([*s[offset:i+1]])
            offset = i+1
            while enum_idx < len(s_enum) and s_enum[enum_idx][1] < offset:
                enum_idx += 1

    if t:
        result.extend(reversed(t))

    return ''.join(result)


print(robotWithString2("zza"))
print(robotWithString2("bac"))
print(robotWithString2("bdda"))


# Counter solution, O(n) (plus sorting counts, upper bound by a constant)
from collections import Counter


def robotWithString3(s: str) -> str:
    counts = Counter(s)
    alphabet = sorted(counts.keys())
    t = []
    result = []
    i = 0
    for c in s:
        while t and t[-1] <= alphabet[i]:
            result.append(t.pop())
        if c != alphabet[i]:
            t.append(c)
            counts[c] -= 1
            while i < len(alphabet) and counts[alphabet[i]] == 0:
                i += 1
        else:
            result.append(c)
            counts[c] -= 1
            while i < len(alphabet) and counts[alphabet[i]] == 0:
                i += 1

    result.extend(reversed(t))
    return ''.join(result)


print(robotWithString3("zza"))
print(robotWithString3("bac"))
print(robotWithString3("bdda"))
