"""
LeetCode Problem #46: Permutations
https://leetcode.com/problems/permutations/

Date: February 26, 2025

Problem Description:
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Time Complexity: O(n * n!) - We have n! permutations, and it takes O(n) time to build each permutation.
Space Complexity: O(n * n!) - We need to store all n! permutations, each of length n.
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Store the final result
        result = []
        
        # If the input is empty, return an empty result
        if not nums:
            return result
        
        # Helper function to generate permutations
        def backtrack(current_perm, remaining):
            # Base case: if no more elements remain, add current permutation to result
            if not remaining:
                result.append(current_perm[:])  # Make a copy of the current permutation
                return
            
            # Try each element in remaining as the next element in the permutation
            for i in range(len(remaining)):
                # Add current element to the permutation
                current_perm.append(remaining[i])
                
                # Recursively generate permutations with the remaining elements
                # Create a new list of remaining elements excluding the current one
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(current_perm, new_remaining)
                
                # Backtrack: remove the current element to try other possibilities
                current_perm.pop()
        
        # Start backtracking with an empty permutation and all elements in nums
        backtrack([], nums)
        
        return result
        
        # Alternative implementation using Python's built-in itertools (commented for learning purposes)
        """
        from itertools import permutations
        return list(map(list, permutations(nums)))
        """