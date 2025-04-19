"""
LeetCode Problem #75: Sort Colors
https://leetcode.com/problems/sort-colors/

Date: March 8, 2025

Problem Description:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Time Complexity: O(n) - We iterate through the array once.
Space Complexity: O(1) - We sort the array in-place.
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag algorithm
        # This is a one-pass algorithm with O(n) time complexity
        
        # Initialize pointers
        left = 0       # Points to the position where 0 should go
        current = 0    # Current element being examined
        right = len(nums) - 1  # Points to the position where 2 should go
        
        # Iterate through the array
        while current <= right:
            if nums[current] == 0:
                # Swap current element with the element at left pointer
                nums[left], nums[current] = nums[current], nums[left]
                # Move both pointers
                left += 1
                current += 1
            elif nums[current] == 1:
                # 1 is already in the right position, just move the current pointer
                current += 1
            else:  # nums[current] == 2
                # Swap current element with the element at right pointer
                nums[current], nums[right] = nums[right], nums[current]
                # Only move the right pointer, as the swapped element still needs to be examined
                right -= 1
        
        # Alternative counting sort approach (commented but included for reference)
        """
        # Count the number of 0s, 1s, and 2s
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        
        # Fill the array with the correct number of each color
        index = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[index] = color
                index += 1
        """