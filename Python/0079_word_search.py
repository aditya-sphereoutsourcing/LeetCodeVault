"""
LeetCode Problem #79: Word Search
https://leetcode.com/problems/word-search/

Date: March 11, 2025

Problem Description:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Time Complexity: O(m*n*4^L) - Where m and n are the dimensions of the board, and L is the length of the word.
                            For each cell, we potentially explore 4 directions for each character in the word.
Space Complexity: O(L) - The recursion depth is at most the length of the word.
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        
        # Define the DFS function
        def dfs(i: int, j: int, index: int) -> bool:
            # Base cases
            # If we've matched all characters in the word, return True
            if index == len(word):
                return True
            
            # If we're out of bounds or the current cell doesn't match the next character, return False
            if (i < 0 or i >= m or j < 0 or j >= n or 
                board[i][j] != word[index]):
                return False
            
            # Mark the current cell as visited by changing its value
            # This is more space efficient than using a visited set
            temp = board[i][j]
            board[i][j] = '#'  # Use a character that won't be in the word
            
            # Try all four directions
            found = (dfs(i+1, j, index+1) or 
                    dfs(i-1, j, index+1) or 
                    dfs(i, j+1, index+1) or 
                    dfs(i, j-1, index+1))
            
            # Restore the original character
            board[i][j] = temp
            
            return found
        
        # Try starting the search from each cell in the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        # If no path is found, return False
        return False
        
        # Optimization: Check if all characters in the word exist in the board
        """
        # Create a counter for characters in the word
        word_chars = Counter(word)
        
        # Create a counter for characters in the board
        board_chars = Counter(char for row in board for char in row)
        
        # Check if all characters in the word exist in sufficient quantities in the board
        for char, count in word_chars.items():
            if board_chars[char] < count:
                return False
        """