"""
LeetCode Problem #19: Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Date: February 15, 2025

Problem Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Time Complexity: O(n) - We traverse the list once.
Space Complexity: O(1) - We only use a constant amount of extra space.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases (e.g., removing the head)
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers: first and second
        first: Optional[ListNode] = dummy
        second: Optional[ListNode] = dummy
        
        # Move the first pointer n+1 steps ahead
        for i in range(n + 1):
            # Check if we've reached the end of the list
            if first is None:
                return None  # This should never happen if n is valid
            first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            # At this point, second cannot be None because first becomes None first
            assert second is not None
            second = second.next
        
        # Remove the nth node from the end
        # At this point, second cannot be None and second.next cannot be None
        assert second is not None and second.next is not None
        second.next = second.next.next
        
        # Return the new head
        return dummy.next