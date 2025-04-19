"""
LeetCode Problem #32: Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/

Date: February 20, 2025

Problem Description:
Given a string containing just the characters '(' and ')', find the length of the longest valid 
(well-formed) parentheses substring.

Time Complexity: O(n) - We iterate through the string once.
Space Complexity: O(n) - In the worst case, we might push all characters onto the stack.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Approach using a stack
        stack = [-1]  # Initialize with -1 as a base index
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:  # s[i] == ')'
                # Pop the top element (matching '(' or base index)
                stack.pop()
                
                if not stack:
                    # If stack is empty, push current index as new base
                    stack.append(i)
                else:
                    # Calculate the length of valid parentheses ending at current position
                    # stack[-1] is the index of the last unmatched '(' or the base index
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
        
        # Alternative approach using dynamic programming (commented out but included for reference)
        """
        n = len(s)
        if n == 0:
            return 0
            
        # dp[i] represents the length of the longest valid substring ending at index i
        dp = [0] * n
        max_length = 0
        
        for i in range(1, n):
            if s[i] == ')':
                # Case 1: If s[i-1] is '(', then we have a valid pair "()"
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                # Case 2: If s[i-1] is ')', we may have situations like "(())"
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2
                    # Add the length of any valid substring before the matching '('
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] += dp[i - dp[i-1] - 2]
                        
                max_length = max(max_length, dp[i])
                
        return max_length
        """