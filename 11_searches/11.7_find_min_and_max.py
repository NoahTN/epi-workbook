def find_min_max(nums):
   def min_max(a, b):
      return (a, b) if a < b else (b, a)

   if len(nums) <= 1:
      return (nums[0], nums[0])
   result = min_max(nums[0], nums[1])

   # Process two at a time
   for i in range(2, len(nums)-1, 2):
      curr = min_max(nums[i], nums[i+1])
      result = (
         min(result[0], curr[0]),
         max(result[1], curr[1]))
   # Account for odd length
   if len(nums)%2:
      result = (
         min(result[0], nums[-1]),
         max(result[1], nums[-1])) 
   return result