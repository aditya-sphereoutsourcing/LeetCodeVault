"""
LeetCode Problem #15: 3Sum
https://leetcode.com/problems/3sum/

Date: February 12, 2025

Problem Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Time Complexity: O(n²) - We sort the array (O(n log n)) and then use a two-pointer technique 
which takes O(n²), resulting in an overall O(n²) time complexity.
Space Complexity: O(1) - Ignoring the space required for the output, we use constant extra space.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to allow for two-pointer technique and duplicate skipping
        nums.sort()
        result = []
        n = len(nums)
        
        # For each element as the first number in the triplet
        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # If the smallest possible sum (nums[i] + nums[i+1] + nums[i+2]) is > 0, break
            if nums[i] > 0:
                break
                
            # If the current element + the largest two elements is < 0, this element can't be used
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue
                
            # Two pointers: one starting after the current element, one at the end
            left, right = i + 1, n - 1
            target = -nums[i]  # Target sum for the two pointers
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum < target:
                    left += 1  # Sum too small, move left pointer right
                elif current_sum > target:
                    right -= 1  # Sum too large, move right pointer left
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
        
        return result