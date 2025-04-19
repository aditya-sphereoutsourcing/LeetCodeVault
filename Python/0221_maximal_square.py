"""
LeetCode Problem #221: Maximal Square
https://leetcode.com/problems/maximal-square/

Date: April 7, 2025

Problem Description:
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Time Complexity: O(m * n) - We visit each cell in the matrix once.
Space Complexity: O(m * n) - We use a 2D DP array of the same size as the input matrix.
"""

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Approach: Dynamic Programming
        # The key insight is that the side length of the largest square ending at (i, j)
        # depends on the minimum of the side lengths of squares ending at (i-1, j),
        # (i, j-1), and (i-1, j-1).
        
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return 0
        
        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Initialize the DP array
        # dp[i][j] represents the side length of the largest square
        # whose bottom-right corner is at cell (i, j) in the original matrix
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the maximum side length seen so far
        max_side = 0
        
        # Fill the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the current cell is '1', we can potentially extend a square
                if matrix[i - 1][j - 1] == '1':
                    # The side length of the new square is the minimum of the squares
                    # ending at (i-1, j), (i, j-1), and (i-1, j-1) plus 1
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    
                    # Update the maximum side length
                    max_side = max(max_side, dp[i][j])
        
        # Return the area of the maximal square
        return max_side * max_side
        
        # Approach 2: Optimized Dynamic Programming (commented out but included for reference)
        # Time Complexity: O(m * n), Space Complexity: O(n) - Using a 1D DP array
        """
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return 0
        
        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Initialize the DP array (just one row)
        # prev_row[j] represents the side length of the largest square
        # whose bottom-right corner is at cell (i-1, j) in the original matrix
        prev_row = [0] * (n + 1)
        
        # Initialize the maximum side length seen so far
        max_side = 0
        
        # Fill the DP array row by row
        for i in range(1, m + 1):
            # Initialize the current row
            curr_row = [0] * (n + 1)
            
            for j in range(1, n + 1):
                # If the current cell is '1', we can potentially extend a square
                if matrix[i - 1][j - 1] == '1':
                    # The side length of the new square is the minimum of the squares
                    # ending at (i-1, j), (i, j-1), and (i-1, j-1) plus 1
                    curr_row[j] = min(prev_row[j], curr_row[j - 1], prev_row[j - 1]) + 1
                    
                    # Update the maximum side length
                    max_side = max(max_side, curr_row[j])
            
            # Update prev_row for the next iteration
            prev_row = curr_row
        
        # Return the area of the maximal square
        return max_side * max_side
        """