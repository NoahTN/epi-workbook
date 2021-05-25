# O(logn), O(1)
import math

def real_sqrt(x):
   # Account for values less than 1
   left, right = (x, 1.0) if x < 1.0 else (1.0, x)

   while not math.isclose(left, right):
      # Avoid overflow
      mid = left+(right-left)/2
      if mid**2 < x:
         left = mid
      else: 
         right = mid
   return left