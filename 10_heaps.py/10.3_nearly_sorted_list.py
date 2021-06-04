# https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0#
# O(nlogk), O(k)

import heapq

cases = int(input())

for i in range(cases):
   result = []
   min_heap = []
   n, k = map(int, input().split())
   nums = list(map(int, input().split()))

   for j in range(n):
        heapq.heappush(min_heap, nums[j])
        # Element has to be within k distance, add to result
        if(len(min_heap) == k):
            result.append(heapq.heappop(min_heap))
   # Add remaining elements         
   while min_heap:
      result.append(heapq.heappop(min_heap))
      
   print(' '.join(map(str, result)))