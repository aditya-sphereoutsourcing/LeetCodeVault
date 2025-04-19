/**
 * LeetCode Problem #142: Linked List Cycle II
 * https://leetcode.com/problems/linked-list-cycle-ii/
 * 
 * Date: March 27, 2025
 *
 * Problem Description:
 * Given the head of a linked list, return the node where the cycle begins. 
 * If there is no cycle, return null.
 *
 * There is a cycle in a linked list if there is some node in the list that can be reached 
 * again by continuously following the next pointer. Internally, pos is used to denote the 
 * index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there 
 * is no cycle. Note that pos is not passed as a parameter.
 *
 * Time Complexity: O(n) - We visit each node at most twice.
 * Space Complexity: O(1) - We use constant extra space with the two-pointer approach.
 */

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        // Approach: Two Pointers (Floyd's Cycle-Finding Algorithm)
        // This is a two-step approach:
        // 1. Determine if there is a cycle using slow and fast pointers
        // 2. If there is a cycle, find the entrance to the cycle
        
        // Edge case: empty list or list with only one node
        if (head == null || head.next == null) {
            return null;
        }
        
        // Step 1: Determine if there is a cycle
        ListNode slow = head;
        ListNode fast = head;
        
        // Move the pointers until they meet or fast reaches the end
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            // If they meet, there is a cycle
            if (slow == fast) {
                break;
            }
        }
        
        // If fast has reached the end, there is no cycle
        if (fast == null || fast.next == null) {
            return null;
        }
        
        // Step 2: Find the entrance to the cycle
        // Reset one pointer to the head
        slow = head;
        
        // Move both pointers at the same speed until they meet again
        // The meeting point is the entrance to the cycle
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        
        return slow;
        
        // Mathematical explanation of the algorithm:
        /*
        Let's denote:
        - The distance from head to the cycle entrance as 'a'
        - The distance from the cycle entrance to the meeting point as 'b'
        - The cycle length as 'c'
        
        When the slow and fast pointers meet:
        - The slow pointer has traveled a distance of (a + b)
        - The fast pointer has traveled a distance of (a + b + n*c), where n is an integer
        - Since the fast pointer moves twice as fast as the slow pointer:
          2(a + b) = a + b + n*c
          a + b = n*c
          a = n*c - b
        
        This means that the distance from the head to the cycle entrance ('a') is equal to
        the distance from the meeting point to the cycle entrance moving forward by n complete cycles.
        
        By setting one pointer back to the head and moving both pointers at the same speed,
        they will meet at the cycle entrance after traveling a distance of 'a'.
        */
    }
}