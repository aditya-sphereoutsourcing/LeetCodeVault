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
public:
    int maxProduct(vector<int>& nums) {
        // Edge case: empty array
        if (nums.empty()) {
            return 0;
        }
        
        // Initialize variables to track the maximum product ending at the current position
        // and the minimum product ending at the current position (needed for negative numbers)
        int max_so_far = nums[0];
        int min_so_far = nums[0];
        
        // Initialize the result to the first element
        int result = nums[0];
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.size(); ++i) {
            // If the current element is negative, swapping max and min is optimal
            // because multiplying a negative with a negative (min_so_far) could give a large positive
            if (nums[i] < 0) {
                swap(max_so_far, min_so_far);
            }
            
            // Update max_so_far and min_so_far for the current position
            // max_so_far = max(current element, current element * max_so_far)
            // min_so_far = min(current element, current element * min_so_far)
            max_so_far = max(nums[i], max_so_far * nums[i]);
            min_so_far = min(nums[i], min_so_far * nums[i]);
            
            // Update the result if we found a larger product
            result = max(result, max_so_far);
        }
        
        return result;
    }
};