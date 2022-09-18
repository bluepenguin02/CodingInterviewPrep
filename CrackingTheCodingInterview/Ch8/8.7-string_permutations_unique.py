"""
8.7: Permutations without Dups
"""

def string_permutations(s: str) -> list:
    """Find all the permutations of a string of unique characters"""
    perms = ['']
    for character in s:
        bases = perms
        perms = []
        for base in bases:
            for i in range(len(base) + 1):
                string = base[:i] + character + base[i:]
                perms.append(string)

    return perms


if __name__ == '__main__':
    test_str = 'abcd'
    permutations = string_permutations(test_str)
    print(len(permutations))
    print(permutations)
