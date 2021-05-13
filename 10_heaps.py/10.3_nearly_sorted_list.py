# https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0#
# O(nlogk), O(k)

import heapq

cases = int(input())

for i in range(cases):
   result = []
   min_heap = []
   n, k = map(int, input().split())
   nums = list(map(int, input().split()))
   # Add first k elements 
   for j in range(k):
      heapq.heappush(min_heap, nums[j])
   # The correct position for the smallest element has to be within k
   # So add and get smallest element out of heap
   for j in range(k, len(nums)):
      smallest = heapq.heappushpop(min_heap, nums[j])
      result.append(smallest)
   # Add remaining elements
   while min_heap:
      smallest = heapq.heappop(min_heap)
      result.append(smallest)
   
   print(' '.join(map(str, result)))