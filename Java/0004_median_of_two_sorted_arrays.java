/**
 * LeetCode Problem #4: Median of Two Sorted Arrays
 * https://leetcode.com/problems/median-of-two-sorted-arrays/
 * 
 * Date: February 6, 2025
 *
 * Problem Description:
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, 
 * return the median of the two sorted arrays.
 * The overall run time complexity should be O(log (m+n)).
 *
 * Time Complexity: O(log(min(m, n))) - We perform binary search on the smaller array.
 * Space Complexity: O(1) - We use constant extra space.
 */

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array for simplicity
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int x = nums1.length;
        int y = nums2.length;
        int low = 0;
        int high = x;
        
        while (low <= high) {
            // Partition the smaller array
            int partitionX = (low + high) / 2;
            
            // Calculate the partition point for the larger array
            int partitionY = (x + y + 1) / 2 - partitionX;
            
            // Get the four values around the partition
            int maxX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
            int minX = (partitionX == x) ? Integer.MAX_VALUE : nums1[partitionX];
            
            int maxY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];
            int minY = (partitionY == y) ? Integer.MAX_VALUE : nums2[partitionY];
            
            // Check if we've found the correct partition
            if (maxX <= minY && maxY <= minX) {
                // If combined length is odd
                if ((x + y) % 2 != 0) {
                    return Math.max(maxX, maxY);
                } 
                // If combined length is even
                else {
                    return (Math.max(maxX, maxY) + Math.min(minX, minY)) / 2.0;
                }
            } 
            // Adjust the partition
            else if (maxX > minY) {
                high = partitionX - 1;
            } else {
                low = partitionX + 1;
            }
        }
        
        // This should never be reached if the input arrays are sorted
        return 0.0;
    }
}