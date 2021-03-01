# https://leetcode.com/problems/reverse-bits/
# O(32), O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        # Use bit manipulation to compare and move
        for i in range(32):
            result <<= 1
            result |= n & 1
            
            n >>= 1
        return result