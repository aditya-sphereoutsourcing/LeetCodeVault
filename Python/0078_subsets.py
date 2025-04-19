"""
LeetCode Problem #78: Subsets
https://leetcode.com/problems/subsets/

Date: March 10, 2025

Problem Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Time Complexity: O(n * 2^n) - There are 2^n subsets, and it takes O(n) time to create each subset.
Space Complexity: O(n * 2^n) - There are 2^n subsets, each requiring O(n) space.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result with an empty subset
        result = [[]]
        
        # Approach 1: Iterative
        # For each number in nums, add it to all existing subsets to create new subsets
        for num in nums:
            # Create new subsets by adding the current number to each existing subset
            result += [subset + [num] for subset in result]
        
        return result
        
        # Approach 2: Backtracking (commented out but included for reference)
        """
        result = []
        
        def backtrack(index, current):
            # Add the current subset to the result
            result.append(current[:])
            
            # Try adding each number (starting from the current index) to the subset
            for i in range(index, len(nums)):
                # Include nums[i] in the subset
                current.append(nums[i])
                
                # Recursively generate subsets with nums[i] included
                backtrack(i + 1, current)
                
                # Backtrack: remove nums[i] to try other options
                current.pop()
        
        # Start backtracking from index 0 with an empty subset
        backtrack(0, [])
        
        return result
        """
        
        # Approach 3: Bit Manipulation (commented out but included for reference)
        """
        n = len(nums)
        result = []
        
        # There are 2^n possible subsets
        for i in range(1 << n):
            # Create a subset based on the binary representation of i
            subset = []
            for j in range(n):
                # If the jth bit of i is set, include nums[j] in the subset
                if (i >> j) & 1:
                    subset.append(nums[j])
            
            result.append(subset)
        
        return result
        """