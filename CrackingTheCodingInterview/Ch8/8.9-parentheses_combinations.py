"""
8.9: Parens
"""

def parentheses_combinations(pairs: int) -> list:
    return parentheses_combinations_helper(pairs, pairs)


def parentheses_combinations_helper(left: int, right: int) -> list:
    if left == right == 0:
        return ['']

    result = []
    if left >= right > 0:
        combinations = parentheses_combinations_helper(left, right-1)
        for combination in combinations:
            combo = combination + ')'
            result.append(combo)    
            
    if left > right:
        combinations = parentheses_combinations_helper(left-1, right)
        for combination in combinations:
            combo = combination + '('
            result.append(combo)

    return result


if __name__ == '__main__':
    print(parentheses_combinations(3))
