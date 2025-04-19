/**
 * LeetCode Problem #5: Longest Palindromic Substring
 * https://leetcode.com/problems/longest-palindromic-substring/
 * 
 * Date: February 7, 2025
 *
 * Problem Description:
 * Given a string s, return the longest palindromic substring in s.
 *
 * Time Complexity: O(n²) - For each center, we expand outwards checking for palindromes.
 * Space Complexity: O(1) - We use constant extra space.
 */

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (!s || s.length === 0) {
        return "";
    }
    
    // Variables to track the longest palindrome
    let start = 0;
    let maxLength = 1;  // Minimum palindrome length is 1 (a single character)
    
    // Helper function to expand around a center
    const expandAroundCenter = (left, right) => {
        // Expand outwards while characters match
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        
        // Calculate the length of the palindrome
        const length = right - left - 1;
        
        // Update if this palindrome is longer than the current longest
        if (length > maxLength) {
            maxLength = length;
            start = left + 1;
        }
    };
    
    // Iterate through each character as a potential center
    for (let i = 0; i < s.length; i++) {
        // Expand around center for odd-length palindromes (e.g., "aba")
        expandAroundCenter(i, i);
        
        // Expand around center for even-length palindromes (e.g., "abba")
        expandAroundCenter(i, i + 1);
    }
    
    // Return the longest palindromic substring
    return s.substring(start, start + maxLength);
};