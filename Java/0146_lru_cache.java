/**
 * LeetCode Problem #146: LRU Cache
 * https://leetcode.com/problems/lru-cache/
 * 
 * Date: February 10, 2025
 *
 * Problem Description:
 * Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
 * 
 * Implement the LRUCache class:
 * - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
 * - int get(int key) Return the value of the key if the key exists, otherwise return -1.
 * - void put(int key, int value) Update the value of the key if the key exists. 
 *   Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity 
 *   from this operation, evict the least recently used key.
 * 
 * The functions get and put must each run in O(1) average time complexity.
 *
 * Time Complexity: 
 * - get: O(1) - Using a hash map to access nodes in constant time.
 * - put: O(1) - Using a hash map and a doubly linked list for constant time operations.
 * 
 * Space Complexity: O(capacity) - We store at most 'capacity' number of key-value pairs.
 */

import java.util.HashMap;
import java.util.Map;

class LRUCache {
    // Node class for our doubly linked list
    private class Node {
        int key;
        int value;
        Node prev;
        Node next;
        
        public Node(int key, int value) {
            this.key = key;
            this.value = value;
            this.prev = null;
            this.next = null;
        }
    }
    
    private int capacity;
    private Map<Integer, Node> cache; // HashMap for O(1) lookup
    private Node head; // Most recently used - dummy node
    private Node tail; // Least recently used - dummy node
    
    // Helper method to remove a node from the list
    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    // Helper method to add a node to the front (most recently used)
    private void addToFront(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
    
    // Helper method to move a node to the front (mark as recently used)
    private void moveToFront(Node node) {
        removeNode(node);
        addToFront(node);
    }
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>(capacity);
        
        // Initialize the doubly linked list with dummy head and tail nodes
        this.head = new Node(0, 0); // Dummy head
        this.tail = new Node(0, 0); // Dummy tail
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        // Check if the key exists in our cache
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            // Move the node to the front (mark as recently used)
            moveToFront(node);
            return node.value;
        }
        return -1; // Key not found
    }
    
    public void put(int key, int value) {
        // Check if the key already exists
        if (cache.containsKey(key)) {
            // Update the value and move to front
            Node node = cache.get(key);
            node.value = value;
            moveToFront(node);
            return;
        }
        
        // Check if we need to evict the least recently used item
        if (cache.size() >= capacity) {
            // Remove the least recently used (the node before tail)
            Node lru = tail.prev;
            removeNode(lru);
            cache.remove(lru.key);
        }
        
        // Create a new node and add it to the front
        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        addToFront(newNode);
    }
}