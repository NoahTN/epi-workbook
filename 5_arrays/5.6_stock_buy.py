# https://leetcode.com/problems/sort-colors/
# O(n), O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      result = 0
      min_p = float('inf')
      for p in prices:
         # Update the smallest price
         min_p = min(min_p, p)
         # Update the maximum profit
         result = max(result, p-min_p)
      return result