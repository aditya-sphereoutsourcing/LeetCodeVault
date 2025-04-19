"""
LeetCode Problem #72: Edit Distance
https://leetcode.com/problems/edit-distance/

Date: March 7, 2025

Problem Description:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Time Complexity: O(m*n) - Where m and n are the lengths of the two strings.
Space Complexity: O(m*n) - We use a 2D DP table of size (m+1) x (n+1).
  Note: This can be optimized to O(min(m,n)) by using a 1D DP array.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get the lengths of the strings
        m, n = len(word1), len(word2)
        
        # Create a 2D DP table
        # dp[i][j] represents the minimum edit distance between word1[0:i] and word2[0:j]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # Initialize the DP table for base cases
        # Converting an empty string to a string of length j requires j insertions
        for j in range(n + 1):
            dp[0][j] = j
        
        # Converting a string of length i to an empty string requires i deletions
        for i in range(m + 1):
            dp[i][0] = i
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters match, no operation is required
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Take the minimum of the three operations:
                    # 1. Replace: dp[i-1][j-1] + 1
                    # 2. Delete: dp[i-1][j] + 1
                    # 3. Insert: dp[i][j-1] + 1
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        # Return the minimum edit distance
        return dp[m][n]
        
        # Space-optimized solution (commented out but included for reference)
        """
        # We can optimize space by using a 1D DP array
        # Since we only need the previous row to calculate the current row
        
        m, n = len(word1), len(word2)
        
        # Ensure m <= n to minimize space usage
        if m > n:
            word1, word2 = word2, word1
            m, n = n, m
        
        # Create a 1D DP array for the previous row
        prev = list(range(n + 1))
        
        # Compute each row
        for i in range(1, m + 1):
            # Create a new array for the current row
            curr = [i]  # First element is i (base case)
            
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr.append(prev[j - 1])
                else:
                    curr.append(1 + min(prev[j - 1], prev[j], curr[-1]))
            
            # Update prev for the next iteration
            prev = curr
        
        return prev[n]
        """