# https://leetcode.com/problems/reverse-integer/
# O(n), O(1)

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        remain = abs(x)
        
        while remain != 0:
            # Multiply the current result and add remain (reverse)
            result = result*10 + remain%10
            remain //= 10
            # Edge case for going beyond 32 bit integer range
            if result > pow(2, 31):
                return 0
            
        return result if x >= 0 else -result 