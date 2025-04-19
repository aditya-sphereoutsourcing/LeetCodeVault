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

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // Ensure nums1 is the smaller array for simplicity
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    const x = nums1.length;
    const y = nums2.length;
    let low = 0;
    let high = x;
    
    while (low <= high) {
        // Partition the smaller array
        const partitionX = Math.floor((low + high) / 2);
        
        // Calculate the partition point for the larger array
        const partitionY = Math.floor((x + y + 1) / 2) - partitionX;
        
        // Get the four values around the partition
        const maxX = (partitionX === 0) ? Number.NEGATIVE_INFINITY : nums1[partitionX - 1];
        const minX = (partitionX === x) ? Number.POSITIVE_INFINITY : nums1[partitionX];
        
        const maxY = (partitionY === 0) ? Number.NEGATIVE_INFINITY : nums2[partitionY - 1];
        const minY = (partitionY === y) ? Number.POSITIVE_INFINITY : nums2[partitionY];
        
        // Check if we've found the correct partition
        if (maxX <= minY && maxY <= minX) {
            // If combined length is odd
            if ((x + y) % 2 !== 0) {
                return Math.max(maxX, maxY);
            } 
            // If combined length is even
            else {
                return (Math.max(maxX, maxY) + Math.min(minX, minY)) / 2;
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
    return 0;
};