"""
LeetCode Problem #152: Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Date: March 29, 2025

Problem Description:
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Time Complexity: O(n) - We iterate through the array once.
Space Complexity: O(1) - We use constant extra space.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Edge case: empty array
        if not nums:
            return 0
        
        # Initialize variables to track the maximum product ending at the current position
        # and the minimum product ending at the current position (needed for negative numbers)
        max_so_far = nums[0]
        min_so_far = nums[0]
        
        # Initialize the result to the first element
        result = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is negative, swapping max and min is optimal
            # because multiplying a negative with a negative (min_so_far) could give a large positive
            if nums[i] < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            # Update max_so_far and min_so_far for the current position
            # max_so_far = max(current element, current element * max_so_far)
            # min_so_far = min(current element, current element * min_so_far)
            max_so_far = max(nums[i], max_so_far * nums[i])
            min_so_far = min(nums[i], min_so_far * nums[i])
            
            # Update the result if we found a larger product
            result = max(result, max_so_far)
        
        return result
        
        # Alternative approach with Kadane's algorithm (commented out but included for reference)
        """
        # Keep track of maximum and minimum products ending at the current position
        max_prod = [0] * len(nums)
        min_prod = [0] * len(nums)
        
        # Initialize the first element
        max_prod[0] = min_prod[0] = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            # Calculate candidates for max and min products ending at position i
            candidates_max = [nums[i], max_prod[i-1] * nums[i], min_prod[i-1] * nums[i]]
            candidates_min = [nums[i], max_prod[i-1] * nums[i], min_prod[i-1] * nums[i]]
            
            # Update max and min products ending at position i
            max_prod[i] = max(candidates_max)
            min_prod[i] = min(candidates_min)
            
            # Update the global maximum product
            result = max(result, max_prod[i])
        
        return result
        """