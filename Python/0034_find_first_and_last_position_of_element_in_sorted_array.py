"""
LeetCode Problem #34: Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Date: February 22, 2025

Problem Description:
Given an array of integers nums sorted in non-decreasing order, find the starting and ending 
position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Time Complexity: O(log n) - We perform two binary searches on the array.
Space Complexity: O(1) - We use a constant amount of extra space.
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the leftmost (first) position of target
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_pos = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    first_pos = mid  # Potential first position
                    right = mid - 1  # Continue searching in the left half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return first_pos
        
        # Helper function to find the rightmost (last) position of target
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_pos = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    last_pos = mid  # Potential last position
                    left = mid + 1  # Continue searching in the right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return last_pos
        
        # If the array is empty, return [-1, -1]
        if not nums:
            return [-1, -1]
            
        # Find the first and last positions of the target
        first = findFirst(nums, target)
        
        # If target is not found, return [-1, -1]
        if first == -1:
            return [-1, -1]
            
        # Find the last position of the target
        last = findLast(nums, target)
        
        return [first, last]