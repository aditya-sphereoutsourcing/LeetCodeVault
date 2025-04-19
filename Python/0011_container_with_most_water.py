"""
LeetCode Problem #11: Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Date: February 13, 2025

Problem Description:
You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains 
the most water. Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Time Complexity: O(n) - We use a two-pointer approach, where each pointer traverses the array at most once.
Space Complexity: O(1) - We only use a constant amount of extra space.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the beginning and end of the array
        left = 0
        right = len(height) - 1
        
        # Initialize max area
        max_area = 0
        
        # Move pointers inward until they meet
        while left < right:
            # Calculate width between the lines
            width = right - left
            
            # Calculate the height of the container (limited by the shorter line)
            h = min(height[left], height[right])
            
            # Update the max area if current area is larger
            max_area = max(max_area, width * h)
            
            # Move the pointer pointing to the shorter line inward
            # This is the key insight: we always move the shorter line because
            # moving the taller line can only decrease the area (as width decreases
            # and height is still limited by the shorter line)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area