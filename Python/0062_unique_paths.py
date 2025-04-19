"""
LeetCode Problem #62: Unique Paths
https://leetcode.com/problems/unique-paths/

Date: March 5, 2025

Problem Description:
There is a robot on an m x n grid. The robot is initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot 
can take to reach the bottom-right corner.

Time Complexity: O(m*n) - We fill out a 2D DP table of size m x n.
Space Complexity: O(m*n) - We use a 2D DP table of size m x n.
  Note: This can be optimized to O(n) by using a 1D DP array.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP table with dimensions m x n
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Initialize the first row and first column to 1
        # There's only one way to reach any cell in the first row or first column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the DP table using the recurrence relation:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the number of unique paths to the bottom-right corner
        return dp[m-1][n-1]
        
        # Space-optimized solution (commented out but included for reference)
        """
        # We can optimize space by using a 1D DP array
        # The idea is to update the array in-place for each row
        
        # Initialize a 1D DP array of size n
        dp = [1] * n
        
        # Update the DP array for each row
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        # Return the number of unique paths to the bottom-right corner
        return dp[n-1]
        """
        
        # Mathematical solution using combinatorics (commented out but included for reference)
        """
        # This problem can also be solved using combinatorics
        # To reach the bottom-right corner, the robot needs to make exactly (m-1) moves down
        # and (n-1) moves right, for a total of (m-1 + n-1) = (m+n-2) moves.
        # We need to choose when to make the (m-1) down moves from the (m+n-2) total moves.
        # This is equivalent to computing the binomial coefficient C(m+n-2, m-1).
        
        import math
        return math.comb(m + n - 2, m - 1)
        """