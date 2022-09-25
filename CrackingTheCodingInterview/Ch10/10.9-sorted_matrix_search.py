"""
CTCI 10.9: Sorted Matrix Search

Much simpler solution in the book.
"""


def sorted_matrix_search(matrix: list, element: int) -> tuple:
    if not matrix or not matrix[0]:
        return -1, -1

    pos = [0, 0]
    rows = len(matrix)
    cols = len(matrix[0])
    while True:
        if matrix[pos[0]][pos[1]] == element:
            return tuple(pos)
        next_row = pos[0] + 1
        next_col = pos[1] + 1
        if next_row < rows and next_col < cols:
            colp1_val = matrix[pos[0]][next_col]
            rowp1_val = matrix[next_row][pos[1]]
            if colp1_val <= rowp1_val <= element or rowp1_val <= element < colp1_val:
                pos[0] += 1
            elif rowp1_val <= colp1_val <= element or colp1_val <= element < rowp1_val:
                pos[1] += 1
            else:
                return -1, -1
        elif next_row < rows:
            rowp1_val = matrix[next_row][pos[1]]
            if rowp1_val <= element:
                pos[0] += 1
            else:
                return -1, -1
        elif next_col < cols:
            colp1_val = matrix[pos[0]][next_col]
            if colp1_val <= element:
                pos[1] += 1
            else:
                return -1, -1
        else:
            return -1, -1


if __name__ == "__main__":
    test1 = [[1, 4, 7],
             [2, 5, 8],
             [3, 6, 9]]
    pos1 = sorted_matrix_search(test1, 5)
    print(f"Test1: {pos1}")

    test2 = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    pos2 = sorted_matrix_search(test2, 5)
    print(f"Test2: {pos2}")

    test3 = [[1, 4, 5],
             [2, 6, 7],
             [3, 8, 9]]
    pos3 = sorted_matrix_search(test3, 6)
    print(f"Test3: {pos3}")

    test4 = [[1, 2, 3],
             [2, 3, 4],
             [3, 4, 5]]
    pos4 = sorted_matrix_search(test4, 3)
    print(f"Test4: {pos4}")

