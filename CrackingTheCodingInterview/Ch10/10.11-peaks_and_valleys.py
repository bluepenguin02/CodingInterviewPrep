"""
CTCI 10.11: Peaks and Valleys

Note: I did two solutions to this.  One using a heap and the other just linearly traversing through the array and
swapping adjacent elements.
"""


import heapq
from random import randint


def peaks_and_valleys(array: str) -> list:
    """I think we can just call heapify and in-order traverse the heap.  The problem comes when a leaf node
    doesn't have a sibling, in which case we need to swap the parent and leaf."""
    if len(array) < 3:
        return array

    heapq.heapify(array)
    have_problem_child = False
    if len(array) % 2 == 0:
        have_problem_child = True
        problem_child = array.pop()
    result = []
    in_order_traverse(array, 0, result)
    if have_problem_child:
        add_problem_child(result, problem_child)

    return result


def in_order_traverse(heap: list, node: int, result: list) -> None:
    if 2*node+1 < len(heap):
        in_order_traverse(heap, 2 * node + 1, result)
    result.append(heap[node])
    if 2*node+2 < len(heap):
        in_order_traverse(heap, 2 * node + 2, result)


def add_problem_child(result: list, problem_child: int) -> None:
    result.append(problem_child)
    if result[-3] < result[-2] < result[-1] or result[-3] > result[-2] > result[-1]:
        result[-2], result[-1] = result[-1], result[-2]


def build_random(n: int) -> list:
    result = [0]*n
    a = -20
    b = 100
    for i in range(n):
        result[i] = randint(a, b)
    return result


def test_result(result: list) -> bool:
    if len(result) < 3:
        return True

    for i in range(1, len(result)-1):
        if not (result[i-1] >= result[i] <= result[i+1] or result[i-1] <= result[i] >= result[i+1]):
            return False

    return True


def peaks_and_valleys2(array: list) -> None:
    """The dead simple solution to the problem.  If it's not a trough or valley, make it one."""
    if len(array) < 3:
        return

    for i in range(1, len(array)-1):
        if array[i-1] > array[i] > array[i+1] or array[i-1] < array[i] < array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]


if __name__ == '__main__':
    for _ in range(100):
        test_len = randint(1, 100)
        tester = build_random(test_len)
        # print(f"test={tester}")
        # ordered = peaks_and_valleys(tester)
        # print(f"ordered={ordered}")
        # print(test_result(ordered))
        peaks_and_valleys2(tester)
        # print(f"ordered={tester}")
        assert test_result(tester)
