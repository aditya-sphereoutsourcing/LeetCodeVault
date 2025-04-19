/**
 * LeetCode Problem #200: Number of Islands
 * https://leetcode.com/problems/number-of-islands/
 * 
 * Date: February 11, 2025
 *
 * Problem Description:
 * Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), 
 * return the number of islands.
 * 
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
 * vertically. You may assume all four edges of the grid are all surrounded by water.
 *
 * Time Complexity: O(m*n) - We potentially visit each cell in the grid once.
 * Space Complexity: O(m*n) - In the worst case, the recursion stack could be as large as the grid.
 */

class Solution {
    // Helper function for depth-first search
    private void dfs(char[][] grid, int row, int col) {
        int numRows = grid.length;
        int numCols = grid[0].length;
        
        // Check if the current position is out of bounds or not land ('1')
        if (row < 0 || col < 0 || row >= numRows || col >= numCols || grid[row][col] != '1') {
            return;
        }
        
        // Mark the current land as visited by changing it to '2'
        grid[row][col] = '2';
        
        // Explore all four adjacent cells
        dfs(grid, row + 1, col);  // Down
        dfs(grid, row - 1, col);  // Up
        dfs(grid, row, col + 1);  // Right
        dfs(grid, row, col - 1);  // Left
    }
    
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int numRows = grid.length;
        int numCols = grid[0].length;
        int islandCount = 0;
        
        // Iterate through each cell in the grid
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                // If we find a land cell, do a DFS to mark the entire island
                if (grid[i][j] == '1') {
                    islandCount++;
                    dfs(grid, i, j);
                }
            }
        }
        
        // Optional: Restore the grid back to its original state (change '2' back to '1')
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                if (grid[i][j] == '2') {
                    grid[i][j] = '1';
                }
            }
        }
        
        return islandCount;
    }
}