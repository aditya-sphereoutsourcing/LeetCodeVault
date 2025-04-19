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
private:
    // Helper function to expand around a center
    void expandAroundCenter(const string& s, int left, int right, int& start, int& maxLength) {
        // Expand outwards while characters match
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        
        // Calculate the length of the palindrome
        int length = right - left - 1;
        
        // Update if this palindrome is longer than the current longest
        if (length > maxLength) {
            maxLength = length;
            start = left + 1;
        }
    }
    
public:
    string longestPalindrome(string s) {
        if (s.empty()) {
            return "";
        }
        
        // Variables to track the longest palindrome
        int start = 0;
        int maxLength = 1;  // Minimum palindrome length is 1 (a single character)
        
        // Iterate through each character as a potential center
        for (int i = 0; i < s.length(); i++) {
            // Expand around center for odd-length palindromes (e.g., "aba")
            expandAroundCenter(s, i, i, start, maxLength);
            
            // Expand around center for even-length palindromes (e.g., "abba")
            expandAroundCenter(s, i, i + 1, start, maxLength);
        }
        
        // Return the longest palindromic substring
        return s.substr(start, maxLength);
    }
};