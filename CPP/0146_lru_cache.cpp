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

class LRUCache {
private:
    // Define the structure for our doubly linked list nodes
    struct Node {
        int key;
        int value;
        Node* prev;
        Node* next;
        Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
    };
    
    int capacity;
    unordered_map<int, Node*> cache; // Hash map for O(1) lookup
    Node* head; // Most recently used
    Node* tail; // Least recently used
    
    // Helper method to remove a node from the list
    void removeNode(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
    
    // Helper method to add a node to the front (most recently used)
    void addToFront(Node* node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }
    
    // Helper method to move a node to the front (mark as recently used)
    void moveToFront(Node* node) {
        removeNode(node);
        addToFront(node);
    }
    
    // Helper method to remove the least recently used node (from the tail)
    void removeLRU() {
        Node* lru = tail->prev;
        removeNode(lru);
        cache.erase(lru->key);
        delete lru;
    }
    
public:
    LRUCache(int capacity) : capacity(capacity) {
        // Create dummy head and tail nodes for easier list operations
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }
    
    ~LRUCache() {
        // Clean up all nodes to prevent memory leaks
        Node* current = head;
        while (current) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
    
    int get(int key) {
        // Check if the key exists in our cache
        if (cache.find(key) != cache.end()) {
            Node* node = cache[key];
            // Move the node to the front (most recently used)
            moveToFront(node);
            return node->value;
        }
        return -1; // Key not found
    }
    
    void put(int key, int value) {
        // Check if the key already exists
        if (cache.find(key) != cache.end()) {
            // Update the value and move to front
            Node* node = cache[key];
            node->value = value;
            moveToFront(node);
            return;
        }
        
        // Check if we need to evict the least recently used item
        if (cache.size() >= capacity) {
            removeLRU();
        }
        
        // Create a new node and add it to the front
        Node* newNode = new Node(key, value);
        cache[key] = newNode;
        addToFront(newNode);
    }
};