# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# O(n), O(1)

class Solution:
   def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      fast, slow = head, head
      
      for i in range(n):
         fast = fast.next

      # Occurs when deleting the first element   
      if not fast:
         return slow.next
      
      # When fast reaches end, slow is n nodes behind it
      while fast.next:
         fast = fast.next
         slow = slow.next
      
      slow.next = slow.next.next
      return head