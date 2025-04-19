/**
 * LeetCode Problem #20: Valid Parentheses
 * https://leetcode.com/problems/valid-parentheses/
 * 
 * Date: February 12, 2025
 *
 * Problem Description:
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
 * determine if the input string is valid.
 *
 * An input string is valid if:
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 * 3. Every close bracket has a corresponding open bracket of the same type.
 *
 * Time Complexity: O(n) - We iterate through the string once.
 * Space Complexity: O(n) - In the worst case, we'll push all characters onto the stack.
 */

class Solution {
public:
    bool isValid(string s) {
        // Create a mapping of closing brackets to their corresponding opening brackets
        unordered_map<char, char> bracketMap = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        
        // Initialize a stack to keep track of open brackets
        stack<char> stack;
        
        // Iterate through each character in the string
        for (char c : s) {
            // If it's a closing bracket
            if (bracketMap.find(c) != bracketMap.end()) {
                // If the stack is empty, there's no matching open bracket
                if (stack.empty()) {
                    return false;
                }
                
                // Get the top element from the stack
                char topElement = stack.top();
                stack.pop();
                
                // Check if the popped element matches the corresponding open bracket
                if (topElement != bracketMap[c]) {
                    return false;
                }
            } 
            // If it's an opening bracket, push it onto the stack
            else {
                stack.push(c);
            }
        }
        
        // If the stack is empty, all brackets were properly closed
        return stack.empty();
    }
};