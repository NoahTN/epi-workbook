# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# O(n), O(1)

class Solution:
   def removeDuplicates(self, nums: List[int]) -> int:
      end = 0
      # update end to set the length of unique integers
      for i in range(len(nums)):
         if nums[i] != nums[end]:
               end += 1
               nums[end] = nums[i]
               
      return end+1