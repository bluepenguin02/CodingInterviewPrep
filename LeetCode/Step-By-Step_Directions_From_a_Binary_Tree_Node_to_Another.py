"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. 
You are also given an integer startValue representing the value of the start node s, and a different integer
destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path 
as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node s to node t.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from copy import copy

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = []
        final_path = []

        def dfs(root, value: int):
            nonlocal final_path
            if root is None:
                return
            if root.val == value:
                final_path = copy(path)
                return

            path.append('L')
            dfs(root.left, value)
            path.pop()
            path.append('R')
            dfs(root.right, value)
            path.pop()

        dfs(root, startValue)
        path_to_start = final_path
        dfs(root, destValue)
        path_to_dest = final_path

        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1

        us = 'U'*(len(path_to_start)-i)
        result = us + ''.join(path_to_dest[i:])
        return result
