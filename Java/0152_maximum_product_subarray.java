/**
 * LeetCode Problem #152: Maximum Product Subarray
 * https://leetcode.com/problems/maximum-product-subarray/
 * 
 * Date: March 29, 2025
 *
 * Problem Description:
 * Given an integer array nums, find a subarray that has the largest product, and return the product.
 * The test cases are generated so that the answer will fit in a 32-bit integer.
 *
 * Time Complexity: O(n) - We iterate through the array once.
 * Space Complexity: O(1) - We use constant extra space.
 */

class Solution {
    public int maxProduct(int[] nums) {
        // Edge case: empty array
        if (nums.length == 0) {
            return 0;
        }
        
        // Initialize variables to track the maximum product ending at the current position
        // and the minimum product ending at the current position (needed for negative numbers)
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        
        // Initialize the result to the first element
        int result = nums[0];
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            // If the current element is negative, swapping max and min is optimal
            // because multiplying a negative with a negative (minSoFar) could give a large positive
            if (nums[i] < 0) {
                int temp = maxSoFar;
                maxSoFar = minSoFar;
                minSoFar = temp;
            }
            
            // Update maxSoFar and minSoFar for the current position
            // maxSoFar = max(current element, current element * maxSoFar)
            // minSoFar = min(current element, current element * minSoFar)
            maxSoFar = Math.max(nums[i], maxSoFar * nums[i]);
            minSoFar = Math.min(nums[i], minSoFar * nums[i]);
            
            // Update the result if we found a larger product
            result = Math.max(result, maxSoFar);
        }
        
        return result;
    }
}