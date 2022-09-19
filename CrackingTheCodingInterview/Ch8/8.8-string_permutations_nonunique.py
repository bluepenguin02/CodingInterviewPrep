"""
8.8: Permutations with Dups
"""

def string_permutations_nonunique(s: str) -> list:
    """Find all the permutations of a string with duplicate characters (no duplicate permutations allowed)."""
    chars = tabulate_characters(s)
    perms = ['']
    for c, repeats in chars.items():
        bases = perms
        perms = []
        for base in bases:
            new_perms = build_perms(base, c, repeats, len(base))
            perms.extend(new_perms)

    return perms


def tabulate_characters(s: str) -> dict:
    chars = {}
    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars


def build_perms(base: str, c: str, n: int, stop: int) -> list:
    """Create permutations of basis by inserting n copies of c up to stop."""
    if n < 1:
        return [base]

    result = []
    for pos in range(stop+1):
        perm = base[:pos] + c + base[pos:]
        perms = build_perms(perm, c, n-1, pos)
        result.extend(perms)

    return result


if __name__ == '__main__':
    test = 'aaaaaa'
    all_perms = string_permutations_nonunique(test)
    print(len(all_perms))
    print(all_perms)
