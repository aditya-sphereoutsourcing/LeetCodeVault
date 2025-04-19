"""
LeetCode Problem #124: Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Date: March 22, 2025

Problem Description:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence 
has an edge connecting them. A node can only appear in the sequence at most once. 
The path sum is the sum of the node values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Time Complexity: O(n) - We need to visit each node exactly once.
Space Complexity: O(h) - The recursion stack can grow up to the height of the tree (h).
                       In the worst case, h = n for a skewed tree.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum path sum with a very small integer
        self.max_sum = -1000000  # A sufficiently small value for this problem
        
        def max_gain(node):
            # Base case: null node contributes 0 gain
            if not node:
                return 0
            
            # Calculate the maximum gain from the left and right subtrees
            # If the gain is negative, we can ignore that subtree by taking 0 instead
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # The maximum path sum that includes the current node as the root of the path
            # This path goes from left subtree -> current node -> right subtree
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum gain that can be contributed to a path 
            # that includes the current node and one of its subtrees
            return node.val + max(left_gain, right_gain)
        
        # Start the recursive calculation from the root
        max_gain(root)
        
        return self.max_sum