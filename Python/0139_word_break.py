"""
LeetCode Problem #139: Word Break
https://leetcode.com/problems/word-break/

Date: March 25, 2025

Problem Description:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Time Complexity: O(n²) - For each starting position, we may need to check substrings of all possible lengths.
Space Complexity: O(n) - We use a dp array of size n+1.
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        
        # Create a dp array where dp[i] indicates whether s[0:i] can be segmented
        # using words from the dictionary
        n = len(s)
        dp = [False] * (n + 1)
        
        # Empty string is always breakable
        dp[0] = True
        
        # Fill the dp array
        for i in range(1, n + 1):
            # Try all possible word endings at position i
            for j in range(i):
                # If s[0:j] is breakable and s[j:i] is a word in the dictionary,
                # then s[0:i] is breakable
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
        
        # Alternative recursive approach with memoization (commented out but included for reference)
        """
        # Create a memo dictionary to store results of subproblems
        memo = {}
        
        def can_break(start):
            # Base case: reached the end of the string
            if start == len(s):
                return True
            
            # Check if we've already computed this subproblem
            if start in memo:
                return memo[start]
            
            # Try all possible words starting at 'start'
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and can_break(end):
                    memo[start] = True
                    return True
            
            # If no valid word ending was found
            memo[start] = False
            return False
        
        return can_break(0)
        """
        
        # Alternative BFS approach (commented out but included for reference)
        """
        # Create a queue for BFS
        from collections import deque
        queue = deque([0])
        
        # Create a visited set to avoid duplicate computations
        visited = set()
        
        while queue:
            start = queue.popleft()
            
            # If we've already processed this starting position, skip it
            if start in visited:
                continue
            
            # Mark as visited
            visited.add(start)
            
            # Try all possible words starting at 'start'
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    # If we've reached the end of the string, return True
                    if end == len(s):
                        return True
                    
                    # Otherwise, add the new starting position to the queue
                    queue.append(end)
        
        # If we've exhausted all possibilities without finding a valid segmentation
        return False
        """