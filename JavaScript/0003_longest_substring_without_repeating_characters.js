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

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    // Edge case: empty string
    if (!s) {
        return 0;
    }
    
    const n = s.length;
    let maxLength = 0;
    let start = 0;
    
    // Map to track character indices
    const charIndex = new Map();
    
    for (let end = 0; end < n; end++) {
        const currentChar = s[end];
        
        // If the character is already in our current window, move the start pointer
        if (charIndex.has(currentChar) && charIndex.get(currentChar) >= start) {
            start = charIndex.get(currentChar) + 1;
        }
        
        // Update the position of the current character
        charIndex.set(currentChar, end);
        
        // Update the maximum length if needed
        const currentLength = end - start + 1;
        maxLength = Math.max(maxLength, currentLength);
    }
    
    return maxLength;
};