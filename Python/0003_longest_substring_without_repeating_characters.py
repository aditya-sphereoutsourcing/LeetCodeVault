"""
LeetCode Problem #3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Date: February 5, 2025

Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n) - We need to visit each character in the string once.
Space Complexity: O(min(m, n)) - We need space for the sliding window (HashSet),
where m is the size of the character set and n is the size of the string.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge case: empty string
        if not s:
            return 0
        
        n = len(s)
        max_length = 0
        start = 0
        
        # Dictionary to track character indices
        char_index = {}
        
        for end in range(n):
            current_char = s[end]
            
            # If the character is already in our current window, move the start pointer
            if current_char in char_index and char_index[current_char] >= start:
                start = char_index[current_char] + 1
            
            # Update the position of the current character
            char_index[current_char] = end
            
            # Update the maximum length if needed
            current_length = end - start + 1
            max_length = max(max_length, current_length)
        
        return max_length