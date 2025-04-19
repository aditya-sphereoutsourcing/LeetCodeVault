/**
 * LeetCode Problem #148: Sort List
 * https://leetcode.com/problems/sort-list/
 * 
 * Date: March 28, 2025
 *
 * Problem Description:
 * Given the head of a linked list, return the list after sorting it in ascending order.
 *
 * Time Complexity: O(n log n) - Merge sort algorithm.
 * Space Complexity: O(log n) - The recursion stack space for the merge sort.
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    // Approach: Merge Sort
    // Merge sort is an efficient, stable sorting algorithm that 
    // performs well on linked lists because it doesn't require 
    // random access to elements.
    
    // Base cases: empty list or list with only one node
    if (!head || !head.next) {
        return head;
    }
    
    // Step 1: Split the list into two halves
    // Find the middle of the linked list using the slow and fast pointer technique
    let slow = head;
    let fast = head.next;
    
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // 'slow' is now at the middle of the list
    // Split the list into two parts
    const mid = slow.next;
    slow.next = null;  // Terminate the first half
    
    // Step 2: Recursively sort both halves
    const left = sortList(head);
    const right = sortList(mid);
    
    // Step 3: Merge the sorted halves
    return merge(left, right);
};

/**
 * Helper function to merge two sorted linked lists
 * @param {ListNode} l1 - First sorted linked list
 * @param {ListNode} l2 - Second sorted linked list
 * @return {ListNode} - Merged sorted linked list
 */
function merge(l1, l2) {
    // Create a dummy node to serve as the head of the merged list
    const dummy = new ListNode(0);
    let curr = dummy;
    
    // Traverse both lists and compare values
    while (l1 && l2) {
        if (l1.val < l2.val) {
            curr.next = l1;
            l1 = l1.next;
        } else {
            curr.next = l2;
            l2 = l2.next;
        }
        curr = curr.next;
    }
    
    // Attach the remaining nodes
    if (l1) {
        curr.next = l1;
    } else {
        curr.next = l2;
    }
    
    return dummy.next;
}