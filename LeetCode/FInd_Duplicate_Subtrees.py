"""
652. Find Duplicate Subtrees
leetcode.com/problems/find-duplicate-subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
"""
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        tuple_ids = {}
        seen_ids = defaultdict(int)
        result = []
        def traverse(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            subtree_tuple = (traverse(node.left), node.val, traverse(node.right))
            if subtree_tuple not in tuple_ids: 
                tuple_ids[subtree_tuple] = len(tuple_ids) + 1
            tuple_id = tuple_ids[subtree_tuple]
            if seen_ids[tuple_id] == 1:
                result.append(node)
            seen_ids[tuple_id] += 1
            return tuple_id
        traverse(root)
        return result
    
