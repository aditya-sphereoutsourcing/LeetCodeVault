"""
LeetCode Problem #33: Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Date: February 21, 2025

Problem Description:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index 
of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Time Complexity: O(log n) - We use a modified binary search algorithm.
Space Complexity: O(1) - We only use a constant amount of extra space.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left half
                else:
                    left = mid + 1   # Search right half
            # Otherwise, the right half is sorted
            else:
                # Check if target is in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right half
                else:
                    right = mid - 1  # Search left half
        
        # Target not found
        return -1