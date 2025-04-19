/**
 * LeetCode Problem #15: 3Sum
 * https://leetcode.com/problems/3sum/
 * 
 * Date: February 12, 2025
 *
 * Problem Description:
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
 * i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 *
 * Notice that the solution set must not contain duplicate triplets.
 *
 * Time Complexity: O(n²) - We sort the array (O(n log n)) and then use a two-pointer technique 
 * which takes O(n²), resulting in an overall O(n²) time complexity.
 * Space Complexity: O(1) - Ignoring the space required for the output, we use constant extra space.
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Sort the array to allow for two-pointer technique and duplicate skipping
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;
        
        // For each element as the first number in the triplet
        for (int i = 0; i < n - 2; i++) {
            // Skip duplicates for the first element
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // If the smallest possible sum (nums[i] + nums[i+1] + nums[i+2]) is > 0, break
            if (nums[i] > 0) {
                break;
            }
            
            // If the current element + the largest two elements is < 0, this element can't be used
            if (nums[i] + nums[n - 2] + nums[n - 1] < 0) {
                continue;
            }
            
            // Two pointers: one starting after the current element, one at the end
            int left = i + 1;
            int right = n - 1;
            int target = -nums[i];  // Target sum for the two pointers
            
            while (left < right) {
                int currentSum = nums[left] + nums[right];
                
                if (currentSum < target) {
                    left++;  // Sum too small, move left pointer right
                } else if (currentSum > target) {
                    right--;  // Sum too large, move right pointer left
                } else {
                    // Found a triplet
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Skip duplicates for the second element
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    
                    // Skip duplicates for the third element
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
                    // Move both pointers
                    left++;
                    right--;
                }
            }
        }
        
        return result;
    }
}