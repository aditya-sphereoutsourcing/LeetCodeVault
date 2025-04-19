"""
LeetCode Problem #84: Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Date: March 12, 2025

Problem Description:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Time Complexity: O(n) - We process each bar exactly once.
Space Complexity: O(n) - In the worst case, all bars are in ascending order, and we push them all onto the stack.
"""

from typing import List

class Solution:
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
        
        # Alternative approach (brute force, not efficient) - O(n²)
        """
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            # Find the minimum height in the range [i, j]
            min_height = float('inf')
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                # Calculate the area with the minimum height and update max_area
                area = min_height * (j - i + 1)
                max_area = max(max_area, area)
        
        return max_area
        """