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

import java.util.Stack;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        // Create a mapping of closing brackets to their corresponding opening brackets
        Map<Character, Character> bracketMap = new HashMap<>();
        bracketMap.put(')', '(');
        bracketMap.put('}', '{');
        bracketMap.put(']', '[');
        
        // Initialize a stack to keep track of open brackets
        Stack<Character> stack = new Stack<>();
        
        // Iterate through each character in the string
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            // If it's a closing bracket
            if (bracketMap.containsKey(c)) {
                // Pop the top element from the stack if it's not empty, else use a dummy value
                char topElement = stack.isEmpty() ? '#' : stack.pop();
                
                // Check if the popped element matches the corresponding open bracket
                if (topElement != bracketMap.get(c)) {
                    return false;
                }
            } 
            // If it's an opening bracket, push it onto the stack
            else {
                stack.push(c);
            }
        }
        
        // If the stack is empty, all brackets were properly closed
        return stack.isEmpty();
    }
}