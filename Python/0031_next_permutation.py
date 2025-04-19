"""
LeetCode Problem #31: Next Permutation
https://leetcode.com/problems/next-permutation/

Date: February 19, 2025

Problem Description:
Implement next permutation, which rearranges numbers into the lexicographically next 
greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible 
order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Time Complexity: O(n) - We need at most two scans of the array.
Space Complexity: O(1) - We modify the array in-place using constant extra space.
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the first pair of adjacent elements (i-1, i) from the right
        # such that nums[i-1] < nums[i]
        i = n - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
            
        if i > 0:
            # Step 2: Find the element in nums[i:] that is just larger than nums[i-1]
            j = n - 1
            while nums[j] <= nums[i-1]:
                j -= 1
                
            # Step 3: Swap nums[i-1] and nums[j]
            nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # Step 4: Reverse the subarray nums[i:]
        # This transforms the subarray into its lowest permutation
        left, right = i, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1