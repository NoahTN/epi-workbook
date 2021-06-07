# O(n), O(n)

def longest_contained_interval(arr):
   result = 0
   num_set = set(arr)

   while num_set:
      num = num_set.pop()

      lower = num-1
      while lower in num_set:
         num_set.remove(lower)
         lower -= 1
      
      upper = num+1
      while upper in num_set:
         num_set.remove(upper)
         upper += 1
      
      result = max(result, upper-lower-1)

   return result
      