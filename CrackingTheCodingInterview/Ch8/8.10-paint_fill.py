"""
CTCI 8.10: Paint Fill
"""

def paint_fill(image: list, point: tuple, color: int):
    old = image[point[0]][point[1]]
    paint_fill_helper(image, point, old, color)


def paint_fill_helper(image: list, point: tuple, old: int, new: int) -> None:
    deltas = ((-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1), (1, 0),   (1, 1))
    if image[point[0]][point[1]] == old:
        image[point[0]][point[1]] = new
        for delta in deltas:
            next_point = (point[0] + delta[0], point[1] + delta[1])
            paint_fill_helper(image, next_point, old, new)


if __name__ == '__main__':
    test = [[0, 1, 0, 0, 0],
            [3, 0, 1, 1, 3],
            [3, 1, 1, 1, 3],
            [3, 1, 1, 1, 3],
            [2, 2, 2, 2, 2]]
    paint_fill(test, (2, 2), 4)
    print(test)
