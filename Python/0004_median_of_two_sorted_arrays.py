"""
LeetCode Problem #4: Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Date: February 6, 2025

Problem Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Time Complexity: O(log(min(m, n))) - We perform binary search on the smaller array.
Space Complexity: O(1) - We use constant extra space.
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for simplicity
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # Partition the smaller array
            partition_x = (low + high) // 2
            
            # Calculate the partition point for the larger array
            partition_y = (x + y + 1) // 2 - partition_x
            
            # Get the four values around the partition
            max_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_x = float('inf') if partition_x == x else nums1[partition_x]
            
            max_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_y = float('inf') if partition_y == y else nums2[partition_y]
            
            # Check if we've found the correct partition
            if max_x <= min_y and max_y <= min_x:
                # If combined length is odd
                if (x + y) % 2 != 0:
                    return max(max_x, max_y)
                # If combined length is even
                else:
                    return (max(max_x, max_y) + min(min_x, min_y)) / 2
            # Adjust the partition
            elif max_x > min_y:
                high = partition_x - 1
            else:
                low = partition_x + 1
        
        # This should never be reached if the input arrays are sorted
        return 0.0