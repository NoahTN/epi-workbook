# https://leetcode.com/problems/sort-colors/
# O(n), O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
      white, blue = 0, 0
      
      for n in nums:
         # Is red, update possible positions for white and blue
         if n == 0:
               white += 1
               blue += 1
         # is white, update possible position for blue
         elif n == 1:
               blue += 1
      
      # Set color based on position
      for i in range(len(nums)):
         if i < white:
               nums[i] = 0
         elif i < blue:
               nums[i] = 1
         else:
               nums[i] = 2
      