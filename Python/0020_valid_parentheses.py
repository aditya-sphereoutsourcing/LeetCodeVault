"""
LeetCode Problem #20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Date: February 12, 2025

Problem Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(n) - We iterate through the string once.
Space Complexity: O(n) - In the worst case, we'll push all characters onto the stack.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Create a mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Initialize a stack to keep track of open brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the corresponding open bracket
                if top_element != bracket_map[char]:
                    return False
            # If it's an opening bracket, push it onto the stack
            else:
                stack.append(char)
        
        # If the stack is empty, all brackets were properly closed
        return not stack