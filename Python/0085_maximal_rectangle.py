"""
LeetCode Problem #85: Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

Date: March 13, 2025

Problem Description:
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle 
containing only 1's and return its area.

Time Complexity: O(m*n) - We process each cell exactly once.
Space Complexity: O(n) - We use an array to keep track of the heights of each column.
"""

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Initialize heights array with zeros
        heights = [0] * n
        max_area = 0
        
        # For each row, calculate the histogram and find the largest rectangle
        for i in range(m):
            # Update the heights array
            for j in range(n):
                # If the current cell is '1', increase the height
                # Otherwise, reset the height to 0
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Calculate the largest rectangle area for the current histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize the maximum area
        max_area = 0
        
        # Initialize a stack to keep track of the indices of the bars
        stack = []
        
        # Iterate through the bars
        for i, height in enumerate(heights):
            # While the current bar is shorter than the bar at the top of the stack
            while stack and heights[stack[-1]] > height:
                # Pop the top of the stack
                h = heights[stack.pop()]
                
                # Calculate the width of the rectangle
                # If the stack is empty, the width is i
                # Otherwise, the width is (i - stack[-1] - 1)
                w = i if not stack else i - stack[-1] - 1
                
                # Update the maximum area
                max_area = max(max_area, h * w)
            
            # Push the current index onto the stack
            stack.append(i)
        
        # Process the remaining bars in the stack
        n = len(heights)
        while stack:
            # Pop the top of the stack
            h = heights[stack.pop()]
            
            # Calculate the width of the rectangle
            w = n if not stack else n - stack[-1] - 1
            
            # Update the maximum area
            max_area = max(max_area, h * w)
        
        return max_area
        
        # Alternative DP approach (commented out but included for reference)
        """
        if not matrix or not matrix[0]:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        # Initialize three arrays to store the state for each row
        height = [0] * n  # height of current rectangle
        left = [0] * n    # left boundary of current rectangle
        right = [n] * n   # right boundary of current rectangle
        
        max_area = 0
        
        for i in range(m):
            # Update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            # Update left boundary
            curr_left = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curr_left)
                else:
                    left[j], curr_left = 0, j + 1
            
            # Update right boundary
            curr_right = n
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    right[j], curr_right = n, j
            
            # Calculate area
            for j in range(n):
                max_area = max(max_area, height[j] * (right[j] - left[j]))
        
        return max_area
        """