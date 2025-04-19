"""
LeetCode Problem #104: Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Date: March 19, 2025

Problem Description:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Approach 1: Recursive DFS
        if not root:
            return 0
        
        # The maximum depth is the maximum depth of the left or right subtree, plus 1 for the root
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1
        
        # Approach 2: Iterative BFS (commented out but included for reference)
        """
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            # Increment depth for each level
            depth += 1
            
            # Process all nodes at the current level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
        """
        
        # Approach 3: Iterative DFS with Stack (commented out but included for reference)
        """
        if not root:
            return 0
        
        stack = [(root, 1)]  # (node, depth)
        max_depth = 0
        
        while stack:
            node, current_depth = stack.pop()
            
            # Update the maximum depth
            max_depth = max(max_depth, current_depth)
            
            # Add children to the stack with incremented depth
            if node.right:
                stack.append((node.right, current_depth + 1))
            if node.left:
                stack.append((node.left, current_depth + 1))
        
        return max_depth
        """