"""
LeetCode Problem #48: Rotate Image
https://leetcode.com/problems/rotate-image/

Date: February 27, 2025

Problem Description:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Time Complexity: O(n²) - We must touch each element in the n x n matrix.
Space Complexity: O(1) - We perform the rotation in-place without using extra space.
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Approach: First transpose the matrix, then reverse each row
        
        # Step 1: Transpose the matrix (swap rows with columns)
        # We only need to traverse the upper triangular matrix
        for i in range(n):
            for j in range(i, n):
                # Swap matrix[i][j] with matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            # Two-pointer approach to reverse each row
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
        
        # Alternative approach: Rotate four cells at a time, layer by layer
        """
        # For each layer
        for layer in range(n // 2):
            first, last = layer, n - 1 - layer
            
            # For each element in the current layer
            for i in range(first, last):
                offset = i - first
                
                # Save the top element
                top = matrix[first][i]
                
                # Move left to top
                matrix[first][i] = matrix[last - offset][first]
                
                # Move bottom to left
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # Move right to bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # Move top to right
                matrix[i][last] = top
        """