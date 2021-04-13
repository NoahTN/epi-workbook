# https://leetcode.com/problems/merge-two-sorted-lists
# O(n+m), O(1)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      result = cur = ListNode()
      
      while l1 and l2:
         if l1.val < l2.val:
               cur.next = l1
               l1 = l1.next
         else:
               cur.next = l2
               l2 = l2.next
         cur = cur.next
         
      cur.next = l1 or l2
      return result.next