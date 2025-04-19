"""
LeetCode Problem #155: Min Stack
https://leetcode.com/problems/min-stack/

Date: March 30, 2025

Problem Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Time Complexity: 
- push: O(1)
- pop: O(1)
- top: O(1)
- getMin: O(1)

Space Complexity: O(n) - Where n is the number of elements in the stack.
"""

class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Main stack to store the values
        self.stack = []
        # Stack to keep track of the minimum values
        # Each element is a tuple (value, min_value_up_to_this_element)
        self.min_stack = []
        
    def push(self, val: int) -> None:
        """
        Push element val onto the stack.
        """
        # Push the value onto the main stack
        self.stack.append(val)
        
        # If the min_stack is empty or the current value is smaller than the current minimum,
        # update the minimum value
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Otherwise, push the current minimum again
            self.min_stack.append(self.min_stack[-1])
        
    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        # Pop from both stacks
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]
        
    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        return self.min_stack[-1]

# Alternative implementation using a single stack with pair values
"""
class MinStack:

    def __init__(self):
        # Stack of pairs (value, current_min)
        self.stack = []
        
    def push(self, val: int) -> None:
        # If the stack is empty, the minimum is the value itself
        if not self.stack:
            self.stack.append((val, val))
        else:
            # Get the current minimum
            current_min = self.stack[-1][1]
            # Push the value and the new minimum
            self.stack.append((val, min(val, current_min)))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
"""

# Alternative optimized implementation to save space
"""
class MinStack:

    def __init__(self):
        # Main stack to store values
        self.stack = []
        # Stack to store only the minimum values with their counts
        self.min_stack = []  # (min_value, count)
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # If min_stack is empty or val is a new minimum
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append((val, 1))
        # If val equals the current minimum, increment its count
        elif val == self.min_stack[-1][0]:
            count = self.min_stack[-1][1]
            self.min_stack[-1] = (val, count + 1)
        
    def pop(self) -> None:
        if not self.stack:
            return
        
        val = self.stack.pop()
        
        # If the popped value is the current minimum
        if val == self.min_stack[-1][0]:
            # Decrement its count
            count = self.min_stack[-1][1]
            if count > 1:
                self.min_stack[-1] = (val, count - 1)
            else:
                self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1][0]
"""