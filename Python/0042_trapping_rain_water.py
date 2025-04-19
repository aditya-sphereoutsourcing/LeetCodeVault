"""
LeetCode Problem #42: Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Date: February 25, 2025

Problem Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Time Complexity: O(n) - We process each element in the array once.
Space Complexity: O(1) - We use constant extra space with the two-pointer approach.
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # If there are less than 3 bars, no water can be trapped
        if len(height) < 3:
            return 0
        
        # Initialize pointers and variables
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0
        
        # Process the array using two pointers
        while left < right:
            # Update the maximum height from the left
            left_max = max(left_max, height[left])
            
            # Update the maximum height from the right
            right_max = max(right_max, height[right])
            
            # Water trapped at the current position is determined by the smaller of left_max and right_max
            if left_max < right_max:
                # The amount of water trapped at position left is the difference between left_max and height[left]
                water += left_max - height[left]
                left += 1
            else:
                # The amount of water trapped at position right is the difference between right_max and height[right]
                water += right_max - height[right]
                right -= 1
                
        return water
        
        # Alternative approach using dynamic programming (commented out but included for reference)
        """
        n = len(height)
        if n < 3:
            return 0
            
        # Arrays to store the maximum height to the left and right of each position
        left_max = [0] * n
        right_max = [0] * n
        
        # Calculate the maximum height to the left of each position
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # Calculate the maximum height to the right of each position
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # Calculate the trapped water at each position
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
            
        return water
        """