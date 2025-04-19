"""
LeetCode Problem #206: Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Date: April 3, 2025

Problem Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Time Complexity: O(n) - We need to visit each node once.
Space Complexity: O(1) - We use constant extra space.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: Iterative
        # Initialize pointers
        prev = None
        curr = head
        
        # Iterate through the list and reverse the links
        while curr:
            # Store the next node temporarily
            next_temp = curr.next
            
            # Reverse the link: point the current node to the previous node
            curr.next = prev
            
            # Move the pointers forward
            prev = curr
            curr = next_temp
        
        # At the end, 'prev' will be the new head of the reversed list
        return prev
        
        # Approach 2: Recursive (commented out but included for reference)
        """
        # Base case: empty list or list with only one node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        # The 'rest' variable will be the new head of the reversed list
        rest = self.reverseList(head.next)
        
        # Reverse the link between the current node and the next node
        head.next.next = head
        
        # Set the next pointer of the current node to None to avoid cycles
        head.next = None
        
        # Return the new head of the reversed list
        return rest
        """
        
        # Approach 3: Using a Stack (commented out but included for reference)
        # Time Complexity: O(n), Space Complexity: O(n)
        """
        # Edge case: empty list or list with only one node
        if not head or not head.next:
            return head
        
        # Create a stack to store the nodes
        stack = []
        
        # Push all nodes onto the stack
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        # Pop nodes from the stack to reverse the list
        dummy = ListNode(0)
        curr = dummy
        
        while stack:
            node = stack.pop()
            curr.next = node
            curr = curr.next
        
        # Set the next pointer of the last node to None to avoid cycles
        curr.next = None
        
        return dummy.next
        """