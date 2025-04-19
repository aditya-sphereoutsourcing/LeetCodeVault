"""
LeetCode Problem #23: Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Date: February 18, 2025

Problem Description:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Time Complexity: O(N log k) where N is the total number of nodes across all lists and k is the number of lists.
We have log k levels of merging, and at each level, we process N nodes.

Space Complexity: O(1) - We only use a constant amount of extra space (excluding the recursion stack).
"""

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Approach 1: Using a min-heap (Priority Queue)
        # This implementation demonstrates the heap-based approach
        
        # Custom wrapper for ListNode to make it comparable for the heap
        # Python's heapq requires that elements be comparable
        class NodeWrapper:
            def __init__(self, node):
                self.node = node
            
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Initialize the min-heap with the first node from each list
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, NodeWrapper(lst))
        
        # Continue until the heap is empty
        while heap:
            # Pop the smallest node from the heap
            wrapper = heapq.heappop(heap)
            node = wrapper.node
            
            # Add this node to the merged list
            current.next = node
            current = current.next
            
            # If there are more nodes in this list, add the next one to the heap
            if node.next:
                heapq.heappush(heap, NodeWrapper(node.next))
        
        return dummy.next
    
        # Approach 2: Divide and Conquer (commented out but included for reference)
        """
        # Base cases
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # Divide the lists into two halves and recursively merge them
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        # Merge the two halves
        return self.mergeTwoLists(left, right)
        """
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to merge two sorted lists (used in the divide and conquer approach)
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach the remaining nodes
        current.next = l1 if l1 else l2
        
        return dummy.next