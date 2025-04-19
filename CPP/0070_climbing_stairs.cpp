/**
 * LeetCode Problem #70: Climbing Stairs
 * https://leetcode.com/problems/climbing-stairs/
 * 
 * Date: February 8, 2025
 *
 * Problem Description:
 * You are climbing a staircase. It takes n steps to reach the top.
 * Each time you can either climb 1 or 2 steps. In how many distinct 
 * ways can you climb to the top?
 *
 * Time Complexity: O(n) - We calculate each step exactly once.
 * Space Complexity: O(1) - We only use two variables to track previous results.
 */

class Solution {
public:
    int climbStairs(int n) {
        // Base cases
        if (n <= 2) {
            return n;
        }
        
        // Variables to track the previous two steps
        int oneStepBefore = 2;  // Ways to climb to step 2
        int twoStepsBefore = 1; // Ways to climb to step 1
        int currentWays = 0;
        
        // Calculate ways for each step from 3 to n
        for (int i = 3; i <= n; i++) {
            // Current ways = ways to reach one step before + ways to reach two steps before
            currentWays = oneStepBefore + twoStepsBefore;
            
            // Update previous steps for next iteration
            twoStepsBefore = oneStepBefore;
            oneStepBefore = currentWays;
        }
        
        return currentWays;
    }
};