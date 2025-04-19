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

class Solution {
    // Helper function to expand around a center
    private void expandAroundCenter(String s, int left, int right, int[] result) {
        // Expand outwards while characters match
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        
        // Calculate the length of the palindrome
        int length = right - left - 1;
        
        // Update if this palindrome is longer than the current longest
        if (length > result[1]) {
            result[1] = length;
            result[0] = left + 1;
        }
    }
    
    public String longestPalindrome(String s) {
        if (s == null || s.isEmpty()) {
            return "";
        }
        
        // result[0] is start index, result[1] is length
        int[] result = new int[]{0, 1};
        
        // Iterate through each character as a potential center
        for (int i = 0; i < s.length(); i++) {
            // Expand around center for odd-length palindromes (e.g., "aba")
            expandAroundCenter(s, i, i, result);
            
            // Expand around center for even-length palindromes (e.g., "abba")
            expandAroundCenter(s, i, i + 1, result);
        }
        
        // Return the longest palindromic substring
        return s.substring(result[0], result[0] + result[1]);
    }
}