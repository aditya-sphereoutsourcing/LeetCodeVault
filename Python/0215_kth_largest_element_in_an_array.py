"""
LeetCode Problem #215: Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Date: April 6, 2025

Problem Description:
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Time Complexity: O(n) average case for QuickSelect, O(n log n) worst case.
Space Complexity: O(1) for in-place partitioning.
"""

from typing import List
import heapq
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach 1: QuickSelect Algorithm
        # This is an optimized version of quicksort that only explores the
        # necessary partition to find the kth largest element
        
        # Convert k to the index in the sorted array
        # If we're finding the kth largest element, it corresponds to
        # the (n-k)th smallest element (0-indexed)
        k = len(nums) - k
        
        def quickSelect(left, right):
            # If the list contains only one element, return that element
            if left == right:
                return nums[left]
            
            # Choose a pivot index randomly
            pivot_index = random.randint(left, right)
            
            # Move the pivot to the right
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            # Elements less than or equal to the pivot will be moved to the left
            # Store index is where we'll put the pivot later
            store_index = left
            
            # Partition the array
            for i in range(left, right):
                if nums[i] <= nums[right]:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            
            # Move the pivot to its final place
            nums[store_index], nums[right] = nums[right], nums[store_index]
            
            # If we found the kth smallest element, return it
            if store_index == k:
                return nums[store_index]
            # If k is smaller, look in the left partition
            elif store_index > k:
                return quickSelect(left, store_index - 1)
            # If k is larger, look in the right partition
            else:
                return quickSelect(store_index + 1, right)
        
        return quickSelect(0, len(nums) - 1)
        
        # Approach 2: Using a Min Heap (commented out but included for reference)
        # Time Complexity: O(n log k), Space Complexity: O(k)
        """
        # Use a min heap to keep the k largest elements
        min_heap = []
        
        for num in nums:
            # Add the current element to the heap
            heapq.heappush(min_heap, num)
            
            # If the heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The smallest element in the heap is the kth largest element in the array
        return min_heap[0]
        """
        
        # Approach 3: Sorting (commented out but included for reference)
        # Time Complexity: O(n log n), Space Complexity: O(1) with in-place sort
        """
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Return the kth element (0-indexed)
        return nums[k-1]
        """