/**
 * LeetCode Problem #121: Best Time to Buy and Sell Stock
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 * 
 * Date: February 9, 2025
 *
 * Problem Description:
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 * You want to maximize your profit by choosing a single day to buy one stock and choosing a 
 * different day in the future to sell that stock.
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
 * profit, return 0.
 *
 * Time Complexity: O(n) - We scan through the array once.
 * Space Complexity: O(1) - We use constant extra space.
 */

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Edge case: empty array or just one day
        if (prices.size() <= 1) {
            return 0;
        }
        
        int minPrice = prices[0]; // Track the minimum price seen so far
        int maxProfit = 0;        // Track the maximum profit achievable
        
        // Iterate through the prices starting from day 2
        for (int i = 1; i < prices.size(); i++) {
            // Update the minimum price seen so far
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } 
            // Calculate profit if selling on the current day and update max profit if higher
            else {
                int currentProfit = prices[i] - minPrice;
                maxProfit = max(maxProfit, currentProfit);
            }
        }
        
        return maxProfit;
    }
};