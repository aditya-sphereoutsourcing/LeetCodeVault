"""
LeetCode Problem #22: Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Date: February 17, 2025

Problem Description:
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Time Complexity: O(4^n / √n) - This is the nth Catalan number, which is the number of 
valid parentheses combinations for n pairs.
Space Complexity: O(n) - For the recursion stack, plus O(4^n / √n) to store all valid combinations.
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: if the length of the current string equals 2*n,
            # we have used all n pairs of parentheses
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # If we can add an open parenthesis (if open_count < n)
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # If we can add a closing parenthesis (if close_count < open_count)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        # Start backtracking with an empty string and no parentheses used
        backtrack('', 0, 0)
        
        return result