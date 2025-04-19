"""
LeetCode Problem #64: Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Date: March 6, 2025

Problem Description:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Time Complexity: O(m*n) - We need to fill out a 2D DP table of size m x n.
Space Complexity: O(m*n) - We use a 2D DP table of size m x n.
  Note: This can be optimized to O(n) by using a 1D DP array.
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Create a 2D DP table with the same dimensions as the grid
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Initialize the DP table with the value of the top-left cell
        dp[0][0] = grid[0][0]
        
        # Fill the first row (can only come from the left)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill the first column (can only come from above)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill the rest of the DP table using the recurrence relation:
        # dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        # Return the minimum path sum to the bottom-right corner
        return dp[m-1][n-1]
        
        # Space-optimized solution (commented out but included for reference)
        """
        # We can optimize space by using a 1D DP array
        # The idea is to update the array in-place for each row
        
        m, n = len(grid), len(grid[0])
        
        # Initialize a 1D DP array with the first row
        dp = [0] * n
        dp[0] = grid[0][0]
        
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        # Update the DP array for each subsequent row
        for i in range(1, m):
            dp[0] += grid[i][0]  # Update the first element for the current row
            
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        
        return dp[n-1]
        """