def square_root(n):
   left, right = 0, n
   
   while left <= right:
      mid = (left+right)//2
      if m*m <= n:
         left = mid+1
      else:
         right = mid-1

   return left-1