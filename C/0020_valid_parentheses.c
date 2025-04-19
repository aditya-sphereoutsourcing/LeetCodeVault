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

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool isValid(char* s) {
    int len = strlen(s);
    
    // Edge case: Empty string is valid
    if (len == 0) {
        return true;
    }
    
    // Edge case: Odd length string cannot be valid
    if (len % 2 != 0) {
        return false;
    }
    
    // Initialize a stack to keep track of open brackets
    // We can use an array as a stack in C
    char* stack = (char*)malloc(len * sizeof(char));
    int top = -1;  // Stack pointer
    
    // Iterate through each character in the string
    for (int i = 0; i < len; i++) {
        char c = s[i];
        
        // If it's an opening bracket, push it onto the stack
        if (c == '(' || c == '{' || c == '[') {
            stack[++top] = c;
        } 
        // If it's a closing bracket
        else {
            // If the stack is empty, there's no matching open bracket
            if (top == -1) {
                free(stack);
                return false;
            }
            
            // Get the top element from the stack
            char topElement = stack[top--];
            
            // Check if the popped element matches the corresponding open bracket
            if ((c == ')' && topElement != '(') ||
                (c == '}' && topElement != '{') ||
                (c == ']' && topElement != '[')) {
                free(stack);
                return false;
            }
        }
    }
    
    // If the stack is empty, all brackets were properly closed
    bool result = (top == -1);
    free(stack);
    return result;
}