"""
LeetCode Problem #114: Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Date: March 21, 2025

Problem Description:
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node 
  in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Time Complexity: O(n) - We need to visit each node exactly once.
Space Complexity: O(h) - The recursion stack can grow up to the height of the tree (h).
                       In the worst case, h = n for a skewed tree.
                       For the iterative approach, the space complexity is O(1).
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Approach 1: Recursive with global prev pointer
        # We traverse the tree in reverse preorder (right, left, root)
        # and connect each node to the previously visited node
        
        # Initialize the previous node as None
        self.prev = None
        
        def dfs(node):
            if not node:
                return
            
            # Process the right subtree first
            dfs(node.right)
            
            # Then process the left subtree
            dfs(node.left)
            
            # Process the current node:
            # 1. Set the right child to the previous node
            # 2. Set the left child to None
            # 3. Update the previous node to be the current node
            node.right = self.prev
            node.left = None
            self.prev = node
        
        dfs(root)
        
        # Approach 2: Iterative (commented out but included for reference)
        """
        # Edge case: empty tree
        if not root:
            return
        
        curr = root
        
        while curr:
            # If the current node has a left child
            if curr.left:
                # Find the rightmost node in the left subtree
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Connect the rightmost node to the current's right subtree
                rightmost.right = curr.right
                
                # Move the left subtree to the right
                curr.right = curr.left
                curr.left = None
            
            # Move to the next node in the flattened tree
            curr = curr.right
        """
        
        # Approach 3: Using a stack (commented out but included for reference)
        """
        # Edge case: empty tree
        if not root:
            return
        
        # Initialize a stack with the root
        stack = [root]
        
        # Process the stack until it's empty
        while stack:
            # Pop the top node
            curr = stack.pop()
            
            # Push the right child first (so it's processed after the left child)
            if curr.right:
                stack.append(curr.right)
            
            # Push the left child
            if curr.left:
                stack.append(curr.left)
            
            # Connect the current node to the next node in the stack
            if stack:
                curr.right = stack[-1]
                curr.left = None
            else:
                curr.left = None
        """