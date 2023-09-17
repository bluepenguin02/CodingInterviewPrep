"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


def maxArea(height: list[int]) -> int:
    max_height = max(height)
    i, j = 0, len(height) - 1
    max_area = 0
    while i < j and (j-i) * max_height > max_area:
        max_area = max(max_area, (j-i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
