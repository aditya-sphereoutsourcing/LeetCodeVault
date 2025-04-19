"""
LeetCode Problem #102: Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Date: March 18, 2025

Problem Description:
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Time Complexity: O(n) - We visit each node exactly once.
Space Complexity: O(n) - In the worst case, the queue will contain all nodes in the last level,
                       which can be up to n/2 nodes for a complete binary tree.
"""

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        # BFS traversal
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            level_values = []
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                
                # Add children to the queue (for the next level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the current level's values to the result
            result.append(level_values)
        
        return result
        
        # Approach 2: Recursive (commented out but included for reference)
        """
        def traverse(node, level):
            if not node:
                return
            
            # If this is a new level, add a new list to result
            if len(result) == level:
                result.append([])
            
            # Add the current node's value to the current level's list
            result[level].append(node.val)
            
            # Recursively traverse the left and right subtrees
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        
        result = []
        traverse(root, 0)
        return result
        """