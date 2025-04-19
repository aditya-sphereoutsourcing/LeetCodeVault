"""
LeetCode Problem #17: Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Date: February 14, 2025

Problem Description:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Mapping:
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz

Time Complexity: O(4^n) where n is the length of the input digits string. 
In the worst case, each digit maps to 4 letters (as in the case of 7 and 9).

Space Complexity: O(n) for the recursion stack, where n is the length of the input digits string.
Plus O(4^n) for storing the output combinations.
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return empty list if input is empty
        if not digits:
            return []
        
        # Define the mapping of digits to letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # Initialize the result list
        result = []
        
        def backtrack(index: int, current_combination: str) -> None:
            # If we've processed all digits, add the combination to the result
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get the letters that the current digit maps to
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Try each letter for the current digit
            for letter in letters:
                # Add the letter to the current combination and move to the next digit
                backtrack(index + 1, current_combination + letter)
        
        # Start backtracking from the first digit
        backtrack(0, "")
        
        return result