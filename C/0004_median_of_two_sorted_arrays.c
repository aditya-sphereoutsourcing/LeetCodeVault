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

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // Ensure nums1 is the smaller array for simplicity
    if (nums1Size > nums2Size) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }
    
    int low = 0;
    int high = nums1Size;
    int combinedLength = nums1Size + nums2Size;
    
    while (low <= high) {
        // Partition the smaller array
        int partitionX = (low + high) / 2;
        
        // Calculate the partition point for the larger array
        int partitionY = (combinedLength + 1) / 2 - partitionX;
        
        // Get the four values around the partition
        int maxX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
        int minX = (partitionX == nums1Size) ? INT_MAX : nums1[partitionX];
        
        int maxY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
        int minY = (partitionY == nums2Size) ? INT_MAX : nums2[partitionY];
        
        // Check if we've found the correct partition
        if (maxX <= minY && maxY <= minX) {
            // If combined length is odd
            if (combinedLength % 2 != 0) {
                return fmax(maxX, maxY);
            } 
            // If combined length is even
            else {
                return (fmax(maxX, maxY) + fmin(minX, minY)) / 2.0;
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