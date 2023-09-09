"""
16.15: Master Mind

Valid colors are RGBY, but I don't check on that.
"""

from collections import namedtuple, defaultdict

Result = namedtuple('Result', ['hits', 'pseudo_hits'])

def master_mind(guess: str, solu: str) -> Result | None:
    """A hit is a direct match of a character in the same position in the guess and solution.
    For a pseudo-hit, a character in the guess is present in the solution, but in the wrong position,
    and the character in the solution was not used in a hit."""
    if len(guess) != len(solu):
        return None
    
    hits = 0
    pseudo_hits = 0
    color_count = defaultdict(int)
    for c in solu:
        color_count[c] += 1

    for c_g, c_s in zip(guess, solu):
        if c_g == c_s:
            hits += 1
            color_count[c_s] -= 1
            
    for c_g, c_s in zip(guess, solu):
        if color_count[c_g] > 0 and c_g != c_s:
            pseudo_hits += 1
            color_count[c_g] -= 1
            
    return Result(hits, pseudo_hits)


if __name__ == '__main__':
    print(master_mind('GGRR', 'RRGR'))