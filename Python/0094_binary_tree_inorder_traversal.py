"""
LeetCode Problem #94: Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Date: March 14, 2025

Problem Description:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Time Complexity: 
- O(n) - We need to visit each node exactly once.
Space Complexity: 
- O(n) - In the worst case, the tree could be completely unbalanced (e.g., a straight line),
  leading to a recursion stack or an explicit stack of depth n.
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Approach 1: Recursive
        result = []
        
        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Visit current node
            result.append(node.val)
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return result
        
        # Approach 2: Iterative (commented out but included for reference)
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Current is now None, so pop the stack
            current = stack.pop()
            
            # Visit the node
            result.append(current.val)
            
            # Move to the right subtree
            current = current.right
        
        return result
        """
        
        # Approach 3: Morris Traversal (O(1) space) (commented out but included for reference)
        """
        result = []
        current = root
        
        while current:
            # If there is no left child, visit the node and go right
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                # Find the rightmost node of the left subtree
                # or the node whose right child points to current
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                # If the right child of predecessor doesn't point to current,
                # make it point to current and move to the left child
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    # If the right child of predecessor points to current,
                    # it means we've visited the left subtree already
                    # Reset the right pointer to None, visit the current node,
                    # and move to the right child
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
        
        return result
        """