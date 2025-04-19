"""
LeetCode Problem #101: Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Date: March 17, 2025

Problem Description:
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Time Complexity: O(n) - We need to visit each node exactly once.
Space Complexity: O(h) - The recursion stack can grow up to the height of the tree (h).
                       In the worst case, h = n for a skewed tree.
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Edge case: empty tree is symmetric
        if not root:
            return True
        
        # Approach 1: Recursive
        def isMirror(left, right):
            # If both nodes are None, they are symmetric
            if not left and not right:
                return True
            
            # If only one node is None, they are not symmetric
            if not left or not right:
                return False
            
            # Check if the values match and if the subtrees are symmetric
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        # Start the recursion from the two subtrees of the root
        return isMirror(root.left, root.right)
        
        # Approach 2: Iterative with Queue (commented out but included for reference)
        """
        # Edge case: empty tree is symmetric
        if not root:
            return True
        
        # Use a queue to perform level-order traversal
        queue = deque([root.left, root.right])
        
        while queue:
            # Pop two nodes at a time
            left = queue.popleft()
            right = queue.popleft()
            
            # If both are None, continue
            if not left and not right:
                continue
            
            # If only one is None or values don't match, return False
            if not left or not right or left.val != right.val:
                return False
            
            # Add the pairs of nodes that should be symmetric
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        return True
        """