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

// Define a node structure for our doubly linked list
typedef struct Node {
    int key;
    int value;
    struct Node* prev;
    struct Node* next;
} Node;

// Define the LRU Cache structure
typedef struct {
    int capacity;
    int count;
    Node* head;  // Most recently used
    Node* tail;  // Least recently used
    Node** map;  // Hash map (array of Node pointers)
    int mapSize;
} LRUCache;

// Create a new node
Node* createNode(int key, int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

// Add a node to the front of the list (most recently used)
void addToFront(LRUCache* cache, Node* node) {
    node->next = cache->head->next;
    node->prev = cache->head;
    cache->head->next->prev = node;
    cache->head->next = node;
}

// Remove a node from the list
void removeNode(Node* node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
}

// Move a node to the front of the list (mark as recently used)
void moveToFront(LRUCache* cache, Node* node) {
    removeNode(node);
    addToFront(cache, node);
}

// Remove the least recently used node (from the tail)
Node* popTail(LRUCache* cache) {
    Node* tailNode = cache->tail->prev;
    removeNode(tailNode);
    return tailNode;
}

// Simple hash function
int hash(int key, int size) {
    return key % size;
}

// Initialize the LRU Cache
LRUCache* lRUCacheCreate(int capacity) {
    LRUCache* cache = (LRUCache*)malloc(sizeof(LRUCache));
    cache->capacity = capacity;
    cache->count = 0;
    
    // Create dummy head and tail nodes
    cache->head = createNode(0, 0);
    cache->tail = createNode(0, 0);
    cache->head->next = cache->tail;
    cache->tail->prev = cache->head;
    
    // Initialize the hash map (simple implementation using an array)
    cache->mapSize = capacity * 2;  // Size the map to reduce collisions
    cache->map = (Node**)calloc(cache->mapSize, sizeof(Node*));
    
    return cache;
}

// Get value from cache
int lRUCacheGet(LRUCache* obj, int key) {
    // Find the node in our hash map
    int index = hash(key, obj->mapSize);
    Node* current = obj->map[index];
    
    // Traverse the linked list at this index to find the key
    while (current != NULL) {
        if (current->key == key) {
            // Move the node to the front (most recently used)
            moveToFront(obj, current);
            return current->value;
        }
        current = current->next;
    }
    
    return -1;  // Key not found
}

// Put value in cache
void lRUCachePut(LRUCache* obj, int key, int value) {
    // Check if key already exists
    int index = hash(key, obj->mapSize);
    Node* current = obj->map[index];
    
    while (current != NULL) {
        if (current->key == key) {
            // Update the value and move to front
            current->value = value;
            moveToFront(obj, current);
            return;
        }
        current = current->next;
    }
    
    // Create a new node
    Node* newNode = createNode(key, value);
    
    // Add to the hash map
    newNode->next = obj->map[index];
    obj->map[index] = newNode;
    
    // Add to the front of the list
    addToFront(obj, newNode);
    obj->count++;
    
    // If over capacity, remove the least recently used
    if (obj->count > obj->capacity) {
        Node* tailNode = popTail(obj);
        
        // Remove from the hash map
        int tailIndex = hash(tailNode->key, obj->mapSize);
        if (obj->map[tailIndex] == tailNode) {
            obj->map[tailIndex] = tailNode->next;
        } else {
            current = obj->map[tailIndex];
            while (current != NULL && current->next != tailNode) {
                current = current->next;
            }
            if (current != NULL) {
                current->next = tailNode->next;
            }
        }
        
        free(tailNode);
        obj->count--;
    }
}

// Free the LRU Cache
void lRUCacheFree(LRUCache* obj) {
    // Free all nodes in the hash map
    for (int i = 0; i < obj->mapSize; i++) {
        Node* current = obj->map[i];
        while (current != NULL) {
            Node* next = current->next;
            free(current);
            current = next;
        }
    }
    
    // Free the dummy head and tail
    free(obj->head);
    free(obj->tail);
    
    // Free the hash map and the cache structure
    free(obj->map);
    free(obj);
}