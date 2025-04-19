"""
LeetCode Problem #226: Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Date: April 8, 2025

Problem Description:
Given the root of a binary tree, invert the tree, and return its root.
Inverting a binary tree means swapping each node's left and right children.

Time Complexity: O(n) - We visit each node in the tree once.
Space Complexity: O(h) - Where h is the height of the tree, which is the space used by the recursion stack.
                        In the worst case, h can be n for a skewed tree.
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Approach 1: Recursive
        # Base case: empty tree or leaf node
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the inverted tree's root
        return root
        
        # Approach 2: Iterative using a Queue (BFS) (commented out but included for reference)
        """
        # Edge case: empty tree
        if not root:
            return None
        
        # Create a queue and add the root node
        queue = deque([root])
        
        # Process nodes level by level
        while queue:
            # Remove the front node from the queue
            node = queue.popleft()
            
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            
            # Add the children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Return the inverted tree's root
        return root
        """
        
        # Approach 3: Iterative using a Stack (DFS) (commented out but included for reference)
        """
        # Edge case: empty tree
        if not root:
            return None
        
        # Create a stack and add the root node
        stack = [root]
        
        # Process nodes in depth-first order
        while stack:
            # Remove the top node from the stack
            node = stack.pop()
            
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            
            # Add the children to the stack
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        # Return the inverted tree's root
        return root
        """