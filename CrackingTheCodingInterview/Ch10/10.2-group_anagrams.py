"""
10.2: Group Anagrams
"""

from collections import defaultdict

def group_anagrams(strings: list) -> list:
    """Given an array of strings, groups all the anagrams.  This method counts the characters in each string then sorts
    based on those counts.  It takes O(a*log(a) + a * s), where a is the length of the array and s is the longest string.
    The book suggests sorting each string, then throwing those sorts into a hash table.  It's O(a * s*log(s)).  I suppose
    we could count the characters then throw those counts into a hash table.  It'd be O(a * s), but I'm not sure if it'd
    actually be faster."""
    char_counts = []
    for i, s in enumerate(strings):
        char_count = count_chars(s)
        char_counts.append((char_count, s))

    char_counts.sort(key=lambda x: x[0])
    result = [s2 for _, s2 in char_counts]
    return result


def count_chars(s: str) -> list:
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1

    result = []
    for c in sorted(counts.keys()):
        result.append((c, counts[c]))
    return result


if __name__ == '__main__':
    tests = ['tommarvoloriddle', 'puppies', 'dog', 'iamlordvoldemort', 'suppiep']
    print(group_anagrams(tests))
