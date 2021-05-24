# https://leetcode.com/problems/kth-largest-element-in-an-array/
# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained
# O(n), O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      if not nums: 
         return None
      
      pivot = random.choice(nums)
      left =  [x for x in nums if x > pivot]
      mid  =  [x for x in nums if x == pivot]
      right = [x for x in nums if x < pivot]
      # Target is in numbers greater than pivot, recurse
      if k <= len(left):
         return self.findKthLargest(left, k)
      # Target is in numbers less than pivot, recurse
      elif k > len(left) + len(mid):
         return self.findKthLargest(right, k - len(left) - len(mid))
      # Target found
      else:
         return mid[0]