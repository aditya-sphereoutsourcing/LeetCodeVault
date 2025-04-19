"""
LeetCode Problem #146: LRU Cache
https://leetcode.com/problems/lru-cache/

Date: February 10, 2025

Problem Description:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity 
  from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Time Complexity: 
- get: O(1) - Using a hash map to access nodes in constant time.
- put: O(1) - Using a hash map and a doubly linked list for constant time operations.

Space Complexity: O(capacity) - We store at most 'capacity' number of key-value pairs.
"""

from typing import Optional, Dict, cast

class Node:
    """
    A doubly linked list node for our LRU cache implementation.
    """
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with the given capacity.
        """
        self.capacity = capacity
        self.cache: Dict[int, Node] = {}  # HashMap for O(1) lookup
        
        # Create dummy head and tail nodes for easier list operations
        self.head = Node(0, 0)  # Most recently used - dummy node
        self.tail = Node(0, 0)  # Least recently used - dummy node
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node: Node) -> None:
        """
        Remove a node from the doubly linked list.
        """
        # Type assertions to help the type checker
        assert node.prev is not None, "Node's prev cannot be None during removal"
        assert node.next is not None, "Node's next cannot be None during removal"
        
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_front(self, node: Node) -> None:
        """
        Add a node to the front of the doubly linked list (most recently used).
        """
        assert self.head.next is not None, "Head's next cannot be None"
        
        node.next = self.head.next
        node.prev = self.head
        
        # Type assertion since we know head.next is not None
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_front(self, node: Node) -> None:
        """
        Move a node to the front of the list (mark as recently used).
        """
        self._remove_node(node)
        self._add_to_front(node)
    
    def get(self, key: int) -> int:
        """
        Get the value of the key if the key exists, otherwise return -1.
        """
        if key in self.cache:
            # Move the node to the front (mark as recently used)
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1  # Key not found
    
    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity, evict the least recently used key.
        """
        # Check if the key already exists
        if key in self.cache:
            # Update the value and move to front
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return
        
        # Check if we need to evict the least recently used item
        if len(self.cache) >= self.capacity:
            # Remove the least recently used (the node before tail)
            assert self.tail.prev is not None, "Tail's prev cannot be None when cache is not empty"
            lru = self.tail.prev
            self._remove_node(lru)
            del self.cache[lru.key]
        
        # Create a new node and add it to the front
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)