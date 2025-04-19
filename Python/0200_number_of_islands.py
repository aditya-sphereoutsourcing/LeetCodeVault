"""
LeetCode Problem #200: Number of Islands
https://leetcode.com/problems/number-of-islands/

Date: February 11, 2025

Problem Description:
Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
vertically. You may assume all four edges of the grid are all surrounded by water.

Time Complexity: O(m*n) - We potentially visit each cell in the grid once.
Space Complexity: O(m*n) - In the worst case, the recursion stack could be as large as the grid.
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        island_count = 0
        
        # Helper function for depth-first search
        def dfs(row: int, col: int) -> None:
            # Check if the current position is out of bounds or not land ('1')
            if (row < 0 or col < 0 or 
                row >= num_rows or col >= num_cols or 
                grid[row][col] != '1'):
                return
            
            # Mark the current land as visited by changing it to '2'
            grid[row][col] = '2'
            
            # Explore all four adjacent cells
            dfs(row + 1, col)  # Down
            dfs(row - 1, col)  # Up
            dfs(row, col + 1)  # Right
            dfs(row, col - 1)  # Left
        
        # Iterate through each cell in the grid
        for i in range(num_rows):
            for j in range(num_cols):
                # If we find a land cell, do a DFS to mark the entire island
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)
        
        # Optional: Restore the grid back to its original state (change '2' back to '1')
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '2':
                    grid[i][j] = '1'
        
        return island_count