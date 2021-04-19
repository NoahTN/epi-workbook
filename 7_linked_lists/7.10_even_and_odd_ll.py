# https://leetcode.com/problems/odd-even-linked-list/
# O(n). O)1

class Solution:
   def oddEvenList(self, head: ListNode) -> ListNode:
      if not head:
         return None
      
      odd, even = head, head.next
      eHead = even
      
      # Even will reach end first, so iterate using it
      while even and even.next:
         odd.next = odd.next.next
         even.next = even.next.next
         
         odd = odd.next
         even = even.next
      
      odd.next = eHead
      
      return head