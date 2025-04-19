"""
LeetCode Problem #232: Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Date: April 10, 2025

Problem Description:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue
should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack, which means only push to top, peek/pop from top,
  size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using
  a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Time Complexity:
- push: O(1) - Amortized (averaged over all operations)
- pop: O(1) - Amortized
- peek: O(1)
- empty: O(1)

Space Complexity: O(n) - Where n is the number of elements in the queue.
"""

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Stack for pushing elements (input stack)
        self.s1 = []
        # Stack for popping elements (output stack)
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # Simply push to the input stack
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # If output stack is empty, transfer all elements from input stack
        if not self.s2:
            self._transfer()
        
        # Pop from the output stack (which now has elements in FIFO order)
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # If output stack is empty, transfer all elements from input stack
        if not self.s2:
            self._transfer()
        
        # Return the top element of the output stack without removing it
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # Queue is empty if both stacks are empty
        return len(self.s1) == 0 and len(self.s2) == 0
    
    def _transfer(self) -> None:
        """
        Helper method to transfer elements from input stack to output stack.
        """
        # Pop all elements from input stack and push to output stack
        # This reverses the order, allowing FIFO behavior
        while self.s1:
            self.s2.append(self.s1.pop())

# Alternative implementation with lazy transfer (commented out but included for reference)
"""
class MyQueue:
    def __init__(self):
        # Stack for pushing elements
        self.push_stack = []
        # Stack for popping elements
        self.pop_stack = []

    def push(self, x: int) -> None:
        # Simply push to the push_stack
        self.push_stack.append(x)

    def pop(self) -> int:
        # Ensure pop_stack has elements
        self._ensure_pop_stack_has_elements()
        
        # Pop from the pop_stack
        return self.pop_stack.pop()

    def peek(self) -> int:
        # Ensure pop_stack has elements
        self._ensure_pop_stack_has_elements()
        
        # Peek at the top element of pop_stack
        return self.pop_stack[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.push_stack and not self.pop_stack
    
    def _ensure_pop_stack_has_elements(self) -> None:
        # If pop_stack is empty, transfer all elements from push_stack
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
"""

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()