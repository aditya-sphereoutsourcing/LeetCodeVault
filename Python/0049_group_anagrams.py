"""
LeetCode Problem #49: Group Anagrams
https://leetcode.com/problems/group-anagrams/

Date: February 28, 2025

Problem Description:
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Time Complexity: O(n * k * log k) where n is the length of strs and k is the maximum length of a string in strs.
  - For each string, we sort it which takes O(k log k) time.
  - We do this for all n strings, so total complexity is O(n * k * log k).
  
Space Complexity: O(n * k) to store all the strings.
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a defaultdict to group anagrams
        # The key will be a tuple of character counts (essentially a sorted representation of the string)
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Method 1: Sort the string and use it as a key
            # Since anagrams have the same sorted form, they'll be grouped together
            sorted_s = ''.join(sorted(s))
            anagram_groups[sorted_s].append(s)
            
            # Method 2: Count characters and use the count tuple as a key (commented out)
            """
            # Initialize a count array for a-z
            count = [0] * 26
            
            # Count occurrences of each character
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            # Use the count tuple as a key
            anagram_groups[tuple(count)].append(s)
            """
        
        # Convert the values of the dictionary (the groups) into a list
        return list(anagram_groups.values())