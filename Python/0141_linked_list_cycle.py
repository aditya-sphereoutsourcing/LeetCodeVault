"""
LeetCode Problem #141: Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Date: March 26, 2025

Problem Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Time Complexity: O(n) - We visit each node at most once.
Space Complexity: O(1) - We use constant extra space with the two-pointer approach.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Approach 1: Two Pointers (Floyd's Cycle-Finding Algorithm)
        # The idea is to use two pointers, slow and fast, where slow moves one step at a time
        # and fast moves two steps at a time. If there is a cycle, the fast pointer will
        # eventually catch up to the slow pointer.
        
        # Edge case: empty list or list with only one node
        if not head or not head.next:
            return False
        
        # Initialize slow and fast pointers
        slow = head
        fast = head.next
        
        # Move the pointers until they meet or fast reaches the end
        while slow != fast:
            # If fast has reached the end, there is no cycle
            if not fast or not fast.next:
                return False
            
            # Move slow one step and fast two steps
            # We've already checked that these are not None in the condition above
            slow = slow.next  # type: ignore
            fast = fast.next.next  # type: ignore
        
        # If the loop exits, it means slow and fast have met, indicating a cycle
        return True
        
        # Approach 2: Hash Set (commented out but included for reference)
        # Note: This solution has O(n) space complexity
        """
        # Create a set to store visited nodes
        visited = set()
        
        # Traverse the list
        current = head
        while current:
            # If we've seen this node before, there's a cycle
            if current in visited:
                return True
            
            # Add the current node to the visited set
            visited.add(current)
            
            # Move to the next node
            current = current.next
        
        # If we reach the end of the list, there is no cycle
        return False
        """