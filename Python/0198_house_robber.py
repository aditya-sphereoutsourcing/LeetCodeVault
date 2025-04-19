"""
LeetCode Problem #198: House Robber
https://leetcode.com/problems/house-robber/

Date: April 2, 2025

Problem Description:
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Time Complexity: O(n) - We process each house exactly once.
Space Complexity: O(1) - We use constant extra space.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach: Dynamic Programming with Constant Space
        # The key insight is that at each house, we have two options:
        # 1. Rob the current house and add its value to the maximum loot from houses [0...i-2]
        # 2. Skip the current house and keep the maximum loot from houses [0...i-1]
        
        # Edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize variables to keep track of the maximum loot
        # rob1 represents the maximum money if we rob up to the previous house
        # rob2 represents the maximum money if we rob up to the house before the previous house
        rob1, rob2 = 0, 0
        
        # Iterate through all houses
        for n in nums:
            # The maximum loot at the current house is the maximum of:
            # 1. The current house's value + the maximum loot up to the house before the previous house
            # 2. The maximum loot up to the previous house (if we skip the current house)
            temp = max(n + rob2, rob1)
            rob2 = rob1
            rob1 = temp
        
        # After iterating through all houses, rob1 contains the maximum possible loot
        return rob1
        
        # Approach 2: Dynamic Programming with Array (commented out but included for reference)
        # Time Complexity: O(n), Space Complexity: O(n)
        """
        # Edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize the DP array
        # dp[i] represents the maximum money we can rob up to the i-th house
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill the DP array
        for i in range(2, len(nums)):
            # The maximum money we can rob at house i is the maximum of:
            # 1. Rob house i and add the maximum money we can rob up to house i-2
            # 2. Skip house i and keep the maximum money we can rob up to house i-1
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        # The last element in the DP array contains the maximum possible loot
        return dp[-1]
        """
        
        # Approach 3: Recursive with Memoization (commented out but included for reference)
        # Time Complexity: O(n), Space Complexity: O(n)
        """
        # Edge case
        if not nums:
            return 0
        
        # Memoization dictionary to store results of subproblems
        memo = {}
        
        def rob_helper(i):
            # Base cases
            if i < 0:
                return 0
            
            # If we've already calculated this subproblem, return the result
            if i in memo:
                return memo[i]
            
            # The maximum money we can rob at house i is the maximum of:
            # 1. Rob house i and add the maximum money we can rob up to house i-2
            # 2. Skip house i and calculate the maximum money we can rob up to house i-1
            result = max(nums[i] + rob_helper(i-2), rob_helper(i-1))
            
            # Store the result in the memo dictionary
            memo[i] = result
            
            return result
        
        # Start the recursion from the last house
        return rob_helper(len(nums) - 1)
        """