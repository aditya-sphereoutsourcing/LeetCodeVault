"""
LeetCode Problem #160: Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Date: March 31, 2025

Problem Description:
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.

Time Complexity: O(m + n) - Where m and n are the lengths of the two lists.
Space Complexity: O(1) - We use constant extra space.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Approach 1: Two Pointer Technique
        # The idea is to have two pointers initially pointing to the heads of the two lists.
        # We traverse both lists, and when one reaches the end, we redirect it to the head
        # of the other list. Eventually, they will meet at the intersection node or both
        # will reach null if there's no intersection.
        
        # Edge case: if either list is empty, there can't be an intersection
        if not headA or not headB:
            return None
        
        # Initialize pointers to the heads of the two lists
        ptrA = headA
        ptrB = headB
        
        # Traverse until the pointers meet or both reach null
        while ptrA != ptrB:
            # If ptrA reaches the end of list A, redirect it to the head of list B
            # Otherwise, move to the next node in list A
            ptrA = headB if ptrA is None else ptrA.next
            
            # If ptrB reaches the end of list B, redirect it to the head of list A
            # Otherwise, move to the next node in list B
            ptrB = headA if ptrB is None else ptrB.next
        
        # ptrA will either be at the intersection node or null if there's no intersection
        return ptrA
        
        # Approach 2: Hash Set (commented out but included for reference)
        # Time Complexity: O(m + n), Space Complexity: O(m) or O(n)
        """
        # Create a set to store nodes from the first list
        nodes_in_A = set()
        
        # Traverse list A and add all nodes to the set
        current = headA
        while current:
            nodes_in_A.add(current)
            current = current.next
        
        # Traverse list B and check if any node is in the set
        current = headB
        while current:
            if current in nodes_in_A:
                return current
            current = current.next
        
        # If we've traversed both lists without finding an intersection, return null
        return None
        """
        
        # Approach 3: Calculate Length Difference (commented out but included for reference)
        # Time Complexity: O(m + n), Space Complexity: O(1)
        """
        # Helper function to get the length of a linked list
        def get_length(head):
            length = 0
            current = head
            while current:
                length += 1
                current = current.next
            return length
        
        # Get the lengths of both lists
        lenA = get_length(headA)
        lenB = get_length(headB)
        
        # Determine which list is longer and calculate the difference in length
        if lenA > lenB:
            longer = headA
            shorter = headB
            diff = lenA - lenB
        else:
            longer = headB
            shorter = headA
            diff = lenB - lenA
        
        # Advance the pointer for the longer list by the difference in length
        for _ in range(diff):
            longer = longer.next
        
        # Now both pointers are at the same distance from the end of their respective lists
        # Traverse both lists until we find the intersection or reach the end
        while longer and shorter:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        
        # If we've traversed both lists without finding an intersection, return null
        return None
        """