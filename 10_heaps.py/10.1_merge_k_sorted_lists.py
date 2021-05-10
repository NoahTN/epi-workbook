# https://leetcode.com/problems/merge-k-sorted-lists/
# https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513/108ms-python-solution-with-heapq-and-avoid-changing-heap-size/347413
# O(knlog(kn)), O(nk)

class Solution:
   def mergeKLists(self, lists: List[ListNode]) -> ListNode:
      heap = []
      head = curr = ListNode(None)
      # Add all elements into heap
      for l in lists:
         while l:
            heappush(heap, l.val)
            l = l.next
      # Add all heap elements to result list
      while heap:
         curr.next = ListNode(heappop(heap))
         curr = curr.next
      return head.next