"""
LeetCode Problem #105: Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Date: March 20, 2025

Problem Description:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Time Complexity: O(n) - We process each node exactly once.
Space Complexity: O(n) - We use recursion and the recursion stack can go up to O(n) for a skewed tree.
                       We also use a hashmap to store the indices of inorder elements.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Edge case: empty arrays
        if not preorder or not inorder:
            return None
        
        # Create a hashmap to store the indices of inorder elements
        # This allows us to quickly find the root's position in the inorder array
        inorder_indices = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_start, pre_end, in_start, in_end):
            # Base case: no elements to process
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # The first element in preorder is the root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find the position of the root in inorder
            root_idx = inorder_indices[root_val]
            
            # Calculate the size of the left subtree
            left_subtree_size = root_idx - in_start
            
            # Recursively build the left and right subtrees
            # Left subtree:
            #   - preorder: [pre_start+1, pre_start+left_subtree_size]
            #   - inorder: [in_start, root_idx-1]
            root.left = helper(pre_start + 1, pre_start + left_subtree_size, in_start, root_idx - 1)
            
            # Right subtree:
            #   - preorder: [pre_start+left_subtree_size+1, pre_end]
            #   - inorder: [root_idx+1, in_end]
            root.right = helper(pre_start + left_subtree_size + 1, pre_end, root_idx + 1, in_end)
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
        
        # Alternative implementation without using the helper function (commented out but included for reference)
        """
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the position of the root in inorder
        root_idx = inorder.index(root_val)
        
        # Split the inorder array into left and right subtrees
        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx + 1:]
        
        # Split the preorder array into left and right subtrees
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
        """