# O(m+n), O(1)

def merge_two_sorted_arrays(A, B, end_idx):
   i, j = end_idx, len(B)-1
   pos = i+j+1

   while i and j:
      if A[i] > A[j]:
         A[pos] = A[i]
         i -= 1
      else:
         A[pos] = B[j]
         j -= 1
      pos -= 1
      
   A[0] = A[0] if i > 0 else B[0]
   return A
