"""
LeetCode Problem #235: Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Date: April 11, 2025

Problem Description:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Time Complexity: O(h) - Where h is the height of the BST. In the worst case, the height can be O(n).
Space Complexity: O(h) - For the recursion stack in the recursive approach.
                        In the iterative approach, it's O(1).
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Approach 1: Recursive
        # The key insight is to use the BST property: all nodes in the left subtree are smaller
        # than the current node, and all nodes in the right subtree are larger.
        
        # If both p and q are smaller than the current node, LCA must be in the left subtree
        if p.val < root.val and q.val < root.val and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both p and q are larger than the current node, LCA must be in the right subtree
        if p.val > root.val and q.val > root.val and root.right:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are on different sides of the current node, or one of them is the current node,
        # then the current node is the LCA
        return root
        
        # Approach 2: Iterative (commented out but included for reference)
        """
        # Start from the root
        current = root
        
        # Traverse the tree
        while current:
            # If both p and q are smaller than the current node, go to the left subtree
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both p and q are larger than the current node, go to the right subtree
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # If p and q are on different sides of the current node, or one of them is the current node,
            # then the current node is the LCA
            else:
                return current
        
        # This should not be reached with valid inputs
        return None
        """
        
        # Approach 3: Without Using BST Property (commented out but included for reference)
        # This is a more general approach that works for any binary tree, not just BST
        """
        # If root is None or root is p or root is q, return root
        if not root or root == p or root == q:
            return root
        
        # Look for LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, root is the LCA
        if left and right:
            return root
        
        # If only one of them is non-null, return that one
        return left if left else right
        """