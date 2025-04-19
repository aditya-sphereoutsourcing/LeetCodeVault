"""
LeetCode Problem #169: Majority Element
https://leetcode.com/problems/majority-element/

Date: April 1, 2025

Problem Description:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(1) - We use constant extra space with Boyer-Moore Voting Algorithm.
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 1: Boyer-Moore Voting Algorithm
        # This algorithm finds the majority element in linear time and constant space
        
        # Initialize the candidate and counter
        candidate = nums[0]
        count = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the counter reaches zero, update the candidate
            if count == 0:
                candidate = nums[i]
                count = 1
            # If the current element matches the candidate, increment the counter
            elif nums[i] == candidate:
                count += 1
            # If the current element doesn't match the candidate, decrement the counter
            else:
                count -= 1
        
        return candidate
        
        # Approach 2: Hash Map (commented out but included for reference)
        # Time Complexity: O(n), Space Complexity: O(n)
        """
        # Create a dictionary to count occurrences of each element
        counts = {}
        
        # Iterate through the array and count occurrences
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
            # If we found an element that appears more than n/2 times, return it immediately
            if counts[num] > len(nums) // 2:
                return num
        
        # This line should not be reached if the majority element always exists
        return -1
        """
        
        # Approach 3: Sorting (commented out but included for reference)
        # Time Complexity: O(n log n), Space Complexity: O(1) or O(n) depending on the sorting algorithm
        """
        # Sort the array
        nums.sort()
        
        # The middle element is guaranteed to be the majority element
        return nums[len(nums) // 2]
        """
        
        # Approach 4: Divide and Conquer (commented out but included for reference)
        # Time Complexity: O(n log n), Space Complexity: O(log n) for recursion stack
        """
        def majority_element_rec(lo, hi):
            # Base case: only one element in the array
            if lo == hi:
                return nums[lo]
            
            # Divide the array into two halves
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)
            
            # If the two halves agree on the majority element, return it
            if left == right:
                return left
            
            # Count occurrences of left and right candidates in the full subarray
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
            
            # Return the candidate with more occurrences
            return left if left_count > right_count else right
        
        return majority_element_rec(0, len(nums) - 1)
        """