# O(n), O(n)

def partition_repeated_entry_array(arr):
   pos_dict = {}
   result = []

   for i in range(len(arr)):
      pos_dict[arr[i]] = pos_dict.get(arr[i], []) + [i]
   for k in pos_dict.keys():
      for p in pos_dict[k]:
         result.append(arr[p])
   return result