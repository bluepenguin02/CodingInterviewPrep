"""
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
a node to be a descendant of itself).”

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
      lca = None
      def dfs(node) -> bool:
        nonlocal lca
        if not node: 
          return False
        lbool = dfs(node.left)
        rbool = dfs(node.right)
        if (lbool and rbool) or ((lbool or rbool) and (node==p or node==q)):
          lca = node
        if lbool or rbool or node==p or node==q:
          return True
        return False

      dfs(root)
      return lca