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

// Helper function for qsort comparison
int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    // Initialize return size to 0
    *returnSize = 0;
    
    // Edge case handling
    if (nums == NULL || numsSize < 3) {
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    // Sort the array to allow for two-pointer technique and duplicate skipping
    qsort(nums, numsSize, sizeof(int), cmp);
    
    // Allocate memory for result - max possible triplets is O(n²)
    int maxTriplets = numsSize * numsSize;
    int** result = (int**)malloc(maxTriplets * sizeof(int*));
    *returnColumnSizes = (int*)malloc(maxTriplets * sizeof(int));
    
    // For each element as the first number in the triplet
    for (int i = 0; i < numsSize - 2; i++) {
        // Skip duplicates for the first element
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        
        // If the smallest possible sum (nums[i] + nums[i+1] + nums[i+2]) is > 0, break
        if (nums[i] > 0) {
            break;
        }
        
        // If the current element + the largest two elements is < 0, this element can't be used
        if (nums[i] + nums[numsSize - 2] + nums[numsSize - 1] < 0) {
            continue;
        }
        
        // Two pointers: one starting after the current element, one at the end
        int left = i + 1;
        int right = numsSize - 1;
        int target = -nums[i];  // Target sum for the two pointers
        
        while (left < right) {
            int currentSum = nums[left] + nums[right];
            
            if (currentSum < target) {
                left++;  // Sum too small, move left pointer right
            } else if (currentSum > target) {
                right--;  // Sum too large, move right pointer left
            } else {
                // Found a triplet - allocate memory for it
                result[*returnSize] = (int*)malloc(3 * sizeof(int));
                result[*returnSize][0] = nums[i];
                result[*returnSize][1] = nums[left];
                result[*returnSize][2] = nums[right];
                (*returnColumnSizes)[*returnSize] = 3;
                (*returnSize)++;
                
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
    
    // Resize the result and columnSizes arrays to the actual size
    result = (int**)realloc(result, (*returnSize) * sizeof(int*));
    *returnColumnSizes = (int*)realloc(*returnColumnSizes, (*returnSize) * sizeof(int));
    
    return result;
}