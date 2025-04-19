"""
LeetCode Problem #207: Course Schedule
https://leetcode.com/problems/course-schedule/

Date: April 4, 2025

Problem Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Time Complexity: O(V + E) - Where V is the number of vertices (courses) and E is the number of edges (prerequisites).
Space Complexity: O(V + E) - For storing the adjacency list and visited arrays.
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Approach 1: Depth-First Search (DFS) to detect cycles in a directed graph
        
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # Create a visited array to keep track of courses in the current DFS path
        # 0: not visited, 1: visiting (in current path), 2: visited (not in current path)
        visited = [0] * numCourses
        
        def has_cycle(course):
            # If the course is currently being visited, we found a cycle
            if visited[course] == 1:
                return True
            
            # If the course has already been fully visited, no cycle through this course
            if visited[course] == 2:
                return False
            
            # Mark the course as being visited (in the current path)
            visited[course] = 1
            
            # Check all prerequisites of this course
            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True
            
            # Mark the course as fully visited (no longer in the current path)
            visited[course] = 2
            
            return False
        
        # Check for cycles starting from each course
        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True
        
        # Approach 2: Breadth-First Search (BFS) with Topological Sort (Kahn's algorithm)
        # (commented out but included for reference)
        """
        # Create an adjacency list and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Create a queue of courses with no prerequisites
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        
        # Count of courses that can be finished
        count = 0
        
        # Process courses with no remaining prerequisites
        while queue:
            course = queue.popleft()
            count += 1
            
            # For each course that depends on this course
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                
                # If all prerequisites for next_course have been met
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # If count equals numCourses, we can finish all courses
        return count == numCourses
        """