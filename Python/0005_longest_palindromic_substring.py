"""
LeetCode Problem #5: Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Date: February 7, 2025

Problem Description:
Given a string s, return the longest palindromic substring in s.

Time Complexity: O(n²) - For each center, we expand outwards checking for palindromes.
Space Complexity: O(1) - We use constant extra space.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Variables to track the longest palindrome
        start = 0
        max_length = 1  # Minimum palindrome length is a single character
        
        # Helper function to expand around a center
        def expand_around_center(left: int, right: int) -> None:
            nonlocal start, max_length
            
            # Expand outwards while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # Calculate the length of the palindrome
            length = right - left - 1
            
            # Update if this palindrome is longer than the current longest
            if length > max_length:
                max_length = length
                start = left + 1
        
        # Iterate through each character as a potential center
        for i in range(len(s)):
            # Expand around center for odd-length palindromes (e.g., "aba")
            expand_around_center(i, i)
            
            # Expand around center for even-length palindromes (e.g., "abba")
            expand_around_center(i, i + 1)
        
        # Return the longest palindromic substring
        return s[start:start + max_length]