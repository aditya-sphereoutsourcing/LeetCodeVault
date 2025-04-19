"""
LeetCode Problem #76: Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Date: March 9, 2025

Problem Description:
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Time Complexity: O(m + n) - Where m is the length of s and n is the length of t.
Space Complexity: O(m + n) - We use dictionaries to store character frequencies.
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle edge cases
        if not s or not t:
            return ""
        
        # Count the frequency of each character in t
        t_counter = Counter(t)
        
        # Count of unique characters in t
        required = len(t_counter)
        
        # Initialize window start and end pointers
        left = 0
        
        # Variables to track the result
        min_len = float('inf')
        result_start = 0
        
        # Counter for characters found in the current window
        window_counts = {}
        
        # Count of characters in t that have been satisfied in the current window
        formed = 0
        
        # Slide the window
        for right, char in enumerate(s):
            # Update window counter for the current character
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if this character helps satisfy a character from t
            if char in t_counter and window_counts[char] == t_counter[char]:
                formed += 1
            
            # Try to minimize the window by moving the left pointer
            while left <= right and formed == required:
                char = s[left]
                
                # Update the result if this window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result_start = left
                
                # Reduce the window from the left
                window_counts[char] -= 1
                
                # If removing this character breaks the window's validity
                if char in t_counter and window_counts[char] < t_counter[char]:
                    formed -= 1
                
                # Move the left pointer
                left += 1
        
        # Return the minimum window substring
        return "" if min_len == float('inf') else s[result_start:result_start + min_len]