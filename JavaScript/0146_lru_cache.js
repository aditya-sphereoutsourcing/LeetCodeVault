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

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.cache = new Map(); // JavaScript Map preserves insertion order for iteration
    
    // Create doubly linked list structure
    this.head = { key: 0, value: 0, prev: null, next: null }; // Most recently used - dummy node
    this.tail = { key: 0, value: 0, prev: null, next: null }; // Least recently used - dummy node
    this.head.next = this.tail;
    this.tail.prev = this.head;
};

// Helper method to remove a node from the list
LRUCache.prototype.removeNode = function(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
};

// Helper method to add a node to the front (most recently used)
LRUCache.prototype.addToFront = function(node) {
    node.next = this.head.next;
    node.prev = this.head;
    this.head.next.prev = node;
    this.head.next = node;
};

// Helper method to move a node to the front (mark as recently used)
LRUCache.prototype.moveToFront = function(node) {
    this.removeNode(node);
    this.addToFront(node);
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    // Check if the key exists in our cache
    if (this.cache.has(key)) {
        const node = this.cache.get(key);
        // Move the node to the front (mark as recently used)
        this.moveToFront(node);
        return node.value;
    }
    return -1; // Key not found
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    // Check if the key already exists
    if (this.cache.has(key)) {
        // Update the value and move to front
        const node = this.cache.get(key);
        node.value = value;
        this.moveToFront(node);
        return;
    }
    
    // Check if we need to evict the least recently used item
    if (this.cache.size >= this.capacity) {
        // Remove the least recently used (the node before tail)
        const lru = this.tail.prev;
        this.removeNode(lru);
        this.cache.delete(lru.key);
    }
    
    // Create a new node and add it to the front
    const newNode = { key, value, prev: null, next: null };
    this.cache.set(key, newNode);
    this.addToFront(newNode);
};