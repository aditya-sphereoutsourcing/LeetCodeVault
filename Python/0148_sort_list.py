"""
LeetCode Problem #148: Sort List
https://leetcode.com/problems/sort-list/

Date: March 28, 2025

Problem Description:
Given the head of a linked list, return the list after sorting it in ascending order.

Time Complexity: O(n log n) - Merge sort algorithm.
Space Complexity: O(log n) - The recursion stack space for the merge sort.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: Merge Sort
        # Merge sort is an efficient, stable sorting algorithm that 
        # performs well on linked lists because it doesn't require 
        # random access to elements.
        
        # Base cases: empty list or list with only one node
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves
        # Find the middle of the linked list using the slow and fast pointer technique
        slow, fast = head, head.next
        
        while fast and fast.next:
            # We've verified that slow and fast are not None
            slow = slow.next  # type: ignore
            fast = fast.next.next  # type: ignore
        
        # 'slow' is now at the middle of the list
        # Split the list into two parts
        mid = slow.next  # type: ignore
        slow.next = None  # type: ignore  # Terminate the first half
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 3: Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        curr = dummy
        
        # Traverse both lists and compare values
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # Attach the remaining nodes
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return dummy.next
        
        # Approach 2: Convert to array, sort, and convert back (commented out but included for reference)
        # Note: This solution has O(n) space complexity
        """
        # Edge case: empty list or list with only one node
        if not head or not head.next:
            return head
        
        # Step 1: Convert linked list to array
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # Step 2: Sort the array
        arr.sort()
        
        # Step 3: Convert array back to linked list
        dummy = ListNode(0)
        curr = dummy
        
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next
        """