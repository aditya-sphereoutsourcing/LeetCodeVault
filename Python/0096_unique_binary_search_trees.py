"""
LeetCode Problem #96: Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/

Date: March 15, 2025

Problem Description:
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.

Time Complexity: O(n²) - We compute each G(i) exactly once, and each computation takes O(i) time.
Space Complexity: O(n) - We use an array of size n+1 to store the intermediate results.
"""

class Solution:
    def numTrees(self, n: int) -> int:
        # We'll use dynamic programming to solve this problem
        # G(n) = number of unique BSTs with n nodes
        # G(0) = 1 (empty tree)
        # G(1) = 1 (single node)
        
        # For n nodes, we can choose each node i as the root (1 <= i <= n)
        # Left subtree will have (i-1) nodes, right subtree will have (n-i) nodes
        # G(n) = sum(G(i-1) * G(n-i)) for i from 1 to n
        
        # Initialize DP array
        G = [0] * (n + 1)
        G[0] = 1  # Empty tree
        G[1] = 1  # Single node
        
        # Build up the table
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                # Number of nodes in left subtree = root - 1
                # Number of nodes in right subtree = nodes - root
                G[nodes] += G[root - 1] * G[nodes - root]
        
        return G[n]
        
        # Mathematical solution using Catalan number (commented out but included for reference)
        """
        # The number of unique BSTs with n nodes is the nth Catalan number
        # C(n) = (1 / (n+1)) * binomial(2n, n)
        
        # Calculate binomial coefficient (2n choose n)
        def binomial(n, k):
            result = 1
            for i in range(k):
                result *= (n - i)
                result //= (i + 1)
            return result
        
        # Calculate the nth Catalan number
        return binomial(2 * n, n) // (n + 1)
        """