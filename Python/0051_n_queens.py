"""
LeetCode Problem #51: N-Queens
https://leetcode.com/problems/n-queens/

Date: March 2, 2025

Problem Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that 
no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Time Complexity: O(N!) - There are N! possible arrangements of queens on the board.
Space Complexity: O(N) - We need to store the chessboard configuration.
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize the result list to store all valid board configurations
        results = []
        
        # Initialize the board with empty cells ('.')
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        # Sets to track occupied columns and diagonals
        cols = set()  # Columns where queens are placed
        pos_diag = set()  # Positive diagonals (r+c)
        neg_diag = set()  # Negative diagonals (r-c)
        
        def backtrack(row):
            # If we've placed queens in all rows, we have a valid solution
            if row == n:
                # Convert the board configuration to the required format
                solution = [''.join(row) for row in board]
                results.append(solution)
                return
            
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if placing a queen at (row, col) is valid
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                # Place the queen and mark the column and diagonals as occupied
                board[row][col] = 'Q'
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Backtrack: remove the queen and unmark the column and diagonals
                board[row][col] = '.'
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
        
        # Start backtracking from the first row
        backtrack(0)
        
        return results