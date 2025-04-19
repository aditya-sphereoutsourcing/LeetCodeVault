"""
LeetCode Problem #21: Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Date: February 16, 2025

Problem Description:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Time Complexity: O(n + m) - where n and m are the lengths of the two lists.
Space Complexity: O(1) - We only use a constant amount of extra space.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        # Current node to build the merged list
        current = dummy
        
        # Traverse both lists and compare nodes
        while list1 and list2:
            if list1.val <= list2.val:
                # Add the smaller node from list1 to the merged list
                current.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # Add the smaller node from list2 to the merged list
                current.next = list2
                # Move to the next node in list2
                list2 = list2.next
            
            # Move the current pointer to the newly added node
            current = current.next
        
        # If one of the lists is empty, add all remaining nodes from the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the head of the merged list (skipping the dummy node)
        return dummy.next