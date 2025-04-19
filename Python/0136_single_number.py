"""
LeetCode Problem #136: Single Number
https://leetcode.com/problems/single-number/

Date: March 24, 2025

Problem Description:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Time Complexity: O(n) - We iterate through the array once.
Space Complexity: O(1) - We use constant extra space.
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach: Using XOR operation
        # XOR has the following properties:
        # 1. x ^ 0 = x
        # 2. x ^ x = 0
        # 3. x ^ y ^ x = y (commutative)
        
        # Initialize result to 0
        result = 0
        
        # XOR all numbers together
        for num in nums:
            result ^= num
        
        # All paired numbers will cancel out (become 0)
        # The only number that appears once will remain
        return result
        
        # Alternative approach with hash map (commented out but included for reference)
        # Note: This solution has O(n) space complexity
        """
        # Create a hash map to store the frequency of each number
        frequency = {}
        
        # Count the frequency of each number
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        # Find the number with frequency 1
        for num, count in frequency.items():
            if count == 1:
                return num
        """
        
        # Alternative approach with math (commented out but included for reference)
        # Note: This solution only works if all paired numbers are the same
        """
        # 2 * sum(set(nums)) - sum(nums)
        return 2 * sum(set(nums)) - sum(nums)
        """