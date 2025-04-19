"""
LeetCode Problem #230: Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Date: April 9, 2025

Problem Description:
Given the root of a binary search tree, and an integer k, return the kth smallest value
(1-indexed) of all the values of the nodes in the tree.

Time Complexity: O(H + k) - Where H is the height of the tree (which could be n in the worst case)
                           and k is the input parameter.
Space Complexity: O(H) - For the recursion stack.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach 1: Inorder Traversal (Recursive)
        # The inorder traversal of a BST visits elements in ascending order.
        # We can find the kth smallest element by performing an inorder traversal
        # and stopping when we reach the kth element.
        
        # List to store the inorder traversal result
        result = []
        
        def inorder(node):
            if not node:
                return
            
            # Visit left subtree
            inorder(node.left)
            
            # Visit current node
            result.append(node.val)
            
            # If we've found k elements, we can stop
            if len(result) == k:
                return
            
            # Visit right subtree
            inorder(node.right)
        
        # Perform inorder traversal
        inorder(root)
        
        # Return the kth element (0-indexed array, k is 1-indexed)
        return result[k-1]
        
        # Approach 2: Iterative Inorder Traversal (commented out but included for reference)
        """
        # Initialize stack and current
        stack = []
        curr = root
        count = 0
        
        # Iterative inorder traversal
        while curr or stack:
            # Traverse to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Visit the current node
            curr = stack.pop()
            count += 1
            
            # If this is the kth element, return it
            if count == k:
                return curr.val
            
            # Move to the right subtree
            curr = curr.right
        
        # If k is invalid, return -1 (this case won't happen with valid inputs)
        return -1
        """
        
        # Approach 3: Optimized with Follow-up (commented out but included for reference)
        # If the BST is modified often (i.e., we can insert/delete nodes) and you need to
        # find the kth smallest frequently, augment the BST node to maintain the size
        # of the subtree rooted at the node.
        """
        class AugmentedTreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
                self.size = 1  # Number of nodes in the subtree rooted at this node
        
        def kthSmallest(self, root: AugmentedTreeNode, k: int) -> int:
            # Helper function to count the size of a subtree
            def count_nodes(node):
                if not node:
                    return 0
                node.size = 1 + count_nodes(node.left) + count_nodes(node.right)
                return node.size
            
            # Initialize the tree with counts
            count_nodes(root)
            
            # Helper function to find kth smallest element using subtree sizes
            def find_kth_smallest(node, k):
                if not node:
                    return -1
                
                # Count of nodes in the left subtree
                left_count = node.left.size if node.left else 0
                
                # If k equals left_count + 1, the current node is the kth smallest
                if k == left_count + 1:
                    return node.val
                
                # If k is less than or equal to left_count, the kth smallest is in the left subtree
                if k <= left_count:
                    return find_kth_smallest(node.left, k)
                
                # Otherwise, the kth smallest is in the right subtree
                # Adjust k to account for nodes already processed
                return find_kth_smallest(node.right, k - left_count - 1)
            
            return find_kth_smallest(root, k)
        """