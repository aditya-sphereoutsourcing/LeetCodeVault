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
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        // Approach: Merge Sort
        // Merge sort is an efficient, stable sorting algorithm that 
        // performs well on linked lists because it doesn't require 
        // random access to elements.
        
        // Base cases: empty list or list with only one node
        if (head == null || head.next == null) {
            return head;
        }
        
        // Step 1: Split the list into two halves
        // Find the middle of the linked list using the slow and fast pointer technique
        ListNode slow = head;
        ListNode fast = head.next;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // 'slow' is now at the middle of the list
        // Split the list into two parts
        ListNode mid = slow.next;
        slow.next = null;  // Terminate the first half
        
        // Step 2: Recursively sort both halves
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        
        // Step 3: Merge the sorted halves
        return merge(left, right);
    }
    
    private ListNode merge(ListNode l1, ListNode l2) {
        // Create a dummy node to serve as the head of the merged list
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        
        // Traverse both lists and compare values
        while (l1 != null && l2 != null) {
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
        if (l1 != null) {
            curr.next = l1;
        } else {
            curr.next = l2;
        }
        
        return dummy.next;
    }
}