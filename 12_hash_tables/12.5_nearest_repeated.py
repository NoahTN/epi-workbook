# O(n), O(n)

def nearest_repeated(arr):
   result = float('inf')
   pos_dict = {}

   for i in range(len(arr)):
      if arr[i] in pos_dict:
         result = min(result, i-pos_dict[arr[i]])
      pos_dict[arr[i]] = i

   return result if result != float('inf') else -1