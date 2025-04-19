"""
LeetCode Problem #50: Pow(x, n)
https://leetcode.com/problems/powx-n/

Date: March 1, 2025

Problem Description:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Time Complexity: O(log n) - We halve the value of n with each recursive call.
Space Complexity: O(log n) - The recursion stack can grow to a depth of log n.
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle edge cases
        if n == 0:
            return 1
        
        # Handle negative exponents: x^(-n) = 1/(x^n)
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # Fast power algorithm using binary exponentiation (recursive approach)
        # If n is even, x^n = (x^(n/2))^2
        # If n is odd, x^n = x * (x^(n//2))^2
        if n % 2 == 0:
            # n is even
            half_pow = self.myPow(x, n // 2)
            return half_pow * half_pow
        else:
            # n is odd
            half_pow = self.myPow(x, n // 2)
            return x * half_pow * half_pow
            
        # Iterative approach (commented out but included for reference)
        """
        if n < 0:
            x = 1 / x
            n = -n
            
        result = 1
        current_product = x
        
        # Binary exponentiation (iterative)
        # Think of the binary representation of n
        # We multiply result by x^(2^k) if the kth bit of n is 1
        while n > 0:
            # If current bit is 1, multiply result by current_product
            if n % 2 == 1:
                result *= current_product
                
            # Square the current_product for the next bit
            current_product *= current_product
            
            # Move to the next bit
            n //= 2
            
        return result
        """