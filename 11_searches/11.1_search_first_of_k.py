# O(logn), O(1)

def search_first_of_k(A, k):
   left, right = 0, len(A)-1
   result = -1

   while left <= right:
      mid = (left+right)//2
      # k found, search for any earlier occurences by updating right
      if A[mid] == k:
         result = mid
         right = mid-1
      elif A[mid] > k:
         right = mid-1
      else:
         left = mid+1
   return result