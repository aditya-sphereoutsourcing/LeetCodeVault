"""
LeetCode Problem #98: Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Date: March 16, 2025

Problem Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Time Complexity: O(n) - We need to visit each node exactly once.
Space Complexity: O(h) - Where h is the height of the tree. In the worst case, h = n for a skewed tree.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Approach 1: Recursive with Valid Range
        def validate(node, low=float('-inf'), high=float('inf')):
            # Empty trees are valid BSTs
            if not node:
                return True
            
            # Current node's value must be within the valid range
            if node.val <= low or node.val >= high:
                return False
            
            # Validate left subtree (all values must be less than node.val)
            # Validate right subtree (all values must be greater than node.val)
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)
        
        # Approach 2: Inorder Traversal (commented out but included for reference)
        """
        # In a BST, inorder traversal should yield a sorted array
        
        def inorder(node):
            if not node:
                return True
            
            # Check left subtree
            if not inorder(node.left):
                return False
            
            # Check current node (should be greater than the previous value)
            if node.val <= self.prev:
                return False
            
            # Update previous value to current value
            self.prev = node.val
            
            # Check right subtree
            return inorder(node.right)
        
        # Initialize prev to negative infinity
        self.prev = float('-inf')
        
        # Start the inorder traversal
        return inorder(root)
        """
        
        # Approach 3: Iterative Inorder Traversal (commented out but included for reference)
        """
        stack = []
        prev = float('-inf')
        curr = root
        
        while stack or curr:
            # Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Current is now None, so pop the stack
            curr = stack.pop()
            
            # Check if the current node's value is greater than the previous value
            if curr.val <= prev:
                return False
            
            # Update previous value
            prev = curr.val
            
            # Move to the right subtree
            curr = curr.right
        
        return True
        """