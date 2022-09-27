"""
https://leetcode.com/problems/sort-the-people/

2418. Sort the People

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.
"""


class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        idx = list(range(len(names)))
        idx.sort(reverse=True, key=lambda i: heights[i])
        result = []
        for i in idx:
            result.append(names[i])
        return result