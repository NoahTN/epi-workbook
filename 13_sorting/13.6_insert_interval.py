# https://leetcode.com/problems/insert-interval
# O(n), O(1)

class Solution:
   def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      first, second = newInterval
      left, right = [], []

      for i in intervals:
         if i[1] < first:
            left.append(i)
         elif i[0] > second:
            right.append(i)
         else: # Mergeable interval found
            first = min(first, i[0])
            second = max(second, i[1])
      return left + [[first, second]] + right