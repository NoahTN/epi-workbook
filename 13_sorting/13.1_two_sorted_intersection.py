# O(m+n), O(1)

def two_sorted_intersection(A, B):
   inter = []
   i, j = 0, 0

   while i < len(A) and j < len(B):
      if A[i] == B[j]:
         if i == 0 or A[i] != A[i-1]:
            inter.append(A[i])
         i+=1
         j+=1
      elif A[i] < B[j]:
         i += 1
      else:
         j += 1

   return inter