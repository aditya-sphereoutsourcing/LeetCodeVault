"""
LeetCode Problem #39: Combination Sum
https://leetcode.com/problems/combination-sum/

Date: February 24, 2025

Problem Description:
Given an array of distinct integers candidates and a target integer target, return a list of 
all unique combinations of candidates where the chosen numbers sum to target. You may return 
the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations 
are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 
combinations for the given input.

Time Complexity: O(N^(T/M + 1)) where N is the number of candidates, T is the target value, and 
M is the minimum value among the candidates. This represents the number of combinations we might generate.
Space Complexity: O(T/M) for the recursion stack, plus additional space to store the output.
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to optimize the solution
        candidates.sort()
        result = []
        
        def backtrack(remaining, combo, start):
            # Base case 1: If remaining becomes 0, we've found a valid combination
            if remaining == 0:
                result.append(combo[:])  # Make a copy of the current combination
                return
            
            # Base case 2: If remaining is negative, this path is invalid
            if remaining < 0:
                return
            
            # Try each candidate starting from the 'start' position
            for i in range(start, len(candidates)):
                # If the current candidate is already too large, break out
                # (since the array is sorted, all subsequent candidates will also be too large)
                if candidates[i] > remaining:
                    break
                
                # Include the current candidate in the combination
                combo.append(candidates[i])
                
                # Recursively explore with the updated remaining sum
                # We pass i (not i+1) because we can reuse the same element
                backtrack(remaining - candidates[i], combo, i)
                
                # Backtrack: Remove the current candidate to try other candidates
                combo.pop()
        
        # Start the backtracking process with the full target and an empty combination
        backtrack(target, [], 0)
        
        return result