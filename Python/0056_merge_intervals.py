"""
LeetCode Problem #56: Merge Intervals
https://leetcode.com/problems/merge-intervals/

Date: March 4, 2025

Problem Description:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Time Complexity: O(n log n) - Dominated by the sorting operation.
Space Complexity: O(n) - To store the result array.
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If the input is empty, return an empty array
        if not intervals:
            return []
        
        # Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result with the first interval
        merged = [intervals[0]]
        
        # Iterate through the remaining intervals
        for current in intervals[1:]:
            # Get the last merged interval
            previous = merged[-1]
            
            # If the current interval overlaps with the previous one, merge them
            if current[0] <= previous[1]:
                # Update the end time of the previous interval if needed
                previous[1] = max(previous[1], current[1])
            else:
                # If there's no overlap, add the current interval to the result
                merged.append(current)
        
        return merged