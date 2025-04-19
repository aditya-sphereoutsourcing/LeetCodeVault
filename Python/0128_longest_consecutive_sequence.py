"""
LeetCode Problem #128: Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Date: March 23, 2025

Problem Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Time Complexity: O(n) - We process each number at most once.
Space Complexity: O(n) - We use a set to store all numbers for quick lookups.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case: empty array
        if not nums:
            return 0
        
        # Create a set from the input array for O(1) lookups
        num_set = set(nums)
        
        # Variable to store the length of the longest consecutive sequence
        longest_streak = 0
        
        # Check each number in the array
        for num in num_set:
            # Only start a streak from the smallest number in a potential sequence
            # If num-1 exists in the set, this number is not the start of a streak
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Extend the streak as far as possible
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
        
        # Alternative approach with sorting (commented out but included for reference)
        """
        # Edge case: empty array
        if not nums:
            return 0
        
        # Remove duplicates and sort the array
        nums = sorted(set(nums))
        
        longest_streak = 1
        current_streak = 1
        
        # Check for consecutive elements
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                # Extend current streak
                current_streak += 1
            else:
                # Break in consecutive sequence
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
        
        # Check if the last streak is the longest
        return max(longest_streak, current_streak)
        """