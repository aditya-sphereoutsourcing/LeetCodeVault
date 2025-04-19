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

// Helper function for depth-first search
void dfs(char** grid, int row, int col, int numRows, int numCols) {
    // Check if the current position is out of bounds or not land ('1')
    if (row < 0 || col < 0 || row >= numRows || col >= numCols || grid[row][col] != '1') {
        return;
    }
    
    // Mark the current land as visited by changing it to '2'
    grid[row][col] = '2';
    
    // Explore all four adjacent cells
    dfs(grid, row + 1, col, numRows, numCols);  // Down
    dfs(grid, row - 1, col, numRows, numCols);  // Up
    dfs(grid, row, col + 1, numRows, numCols);  // Right
    dfs(grid, row, col - 1, numRows, numCols);  // Left
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    if (grid == NULL || gridSize == 0 || gridColSize == NULL) {
        return 0;
    }
    
    int numRows = gridSize;
    int numCols = gridColSize[0];
    int islandCount = 0;
    
    // Iterate through each cell in the grid
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            // If we find a land cell, do a DFS to mark the entire island
            if (grid[i][j] == '1') {
                islandCount++;
                dfs(grid, i, j, numRows, numCols);
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