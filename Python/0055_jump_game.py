"""
LeetCode Problem #55: Jump Game
https://leetcode.com/problems/jump-game/

Date: March 3, 2025

Problem Description:
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Time Complexity: O(n) - We need to iterate through the array once.
Space Complexity: O(1) - We use constant extra space.
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the maximum reachable position
        max_reach = 0
        n = len(nums)
        
        # Iterate through the array
        for i in range(n):
            # If the current position is beyond our max reach, we can't get here
            if i > max_reach:
                return False
            
            # Update the maximum reachable position
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach the last index or beyond, return true
            if max_reach >= n - 1:
                return True
        
        # If we've gone through the entire array and cannot reach the end
        return False
        
        # Alternative approach using greedy algorithm (commented out but included for reference)
        """
        n = len(nums)
        goal = n - 1  # Start from the last position
        
        # Work backwards from the goal
        for i in range(n - 2, -1, -1):
            # If we can reach the goal from position i, update the goal to i
            if i + nums[i] >= goal:
                goal = i
        
        # If the goal is the first position, we can reach the last index
        return goal == 0
        """