# https://leetcode.com/problems/kth-largest-element-in-an-array/
# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained
# O(n), O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      if not nums: 
         return None
      
      pivot = random.choice(nums)
      greater =  [x for x in nums if x > pivot]
      equal  =  [x for x in nums if x == pivot]
      less = [x for x in nums if x < pivot]
      # Target is in numbers greater than pivot, recurse
      if k <= len(greater):
         return self.findKthLargest(greater, k)
      # Target is in numbers less than pivot, recurse
      elif k > len(greater) + len(equal):
         return self.findKthLargest(less, k - len(greater) - len(equal))
      # Target found
      else:
         return equal[0]