/**
 * LeetCode Problem #3: Longest Substring Without Repeating Characters
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * 
 * Date: February 5, 2025
 *
 * Problem Description:
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * Time Complexity: O(n) - We need to visit each character in the string once.
 * Space Complexity: O(min(m, n)) - We need space for the sliding window (HashSet),
 * where m is the size of the character set and n is the size of the string.
 */

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Edge case: empty string
        if (s.empty()) {
            return 0;
        }
        
        int n = s.length();
        int maxLength = 0;
        int start = 0;
        
        // Map to track character indices
        unordered_map<char, int> charIndex;
        
        for (int end = 0; end < n; end++) {
            // If the character is already in our current window, move the start pointer
            if (charIndex.find(s[end]) != charIndex.end() && charIndex[s[end]] >= start) {
                start = charIndex[s[end]] + 1;
            }
            
            // Update the position of the current character
            charIndex[s[end]] = end;
            
            // Update the maximum length if needed
            int currentLength = end - start + 1;
            maxLength = max(maxLength, currentLength);
        }
        
        return maxLength;
    }
};