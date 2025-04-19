"""
LeetCode Problem #36: Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Date: February 23, 2025

Problem Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Time Complexity: O(n²) - We need to traverse the entire 9x9 Sudoku board.
Space Complexity: O(n) - We use hash sets to track used numbers in each row, column, and 3x3 sub-box.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize hash sets to track used numbers in rows, columns, and 3x3 sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Iterate through the board
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == '.':
                    continue
                
                # Calculate the box index for the current cell
                # Box indices: 0 1 2
                #              3 4 5
                #              6 7 8
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check if the current value is already used in the current row, column, or box
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in boxes[box_idx]):
                    return False
                
                # Add the current value to the appropriate sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[box_idx].add(board[r][c])
        
        # If we get here, the board is valid
        return True