# https://leetcode.com/problems/reverse-linked-list
# O(n), O(1)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      # Prev will act as the new head
      curr, prev = head, None
      # Prev "moves back" as curr is set to it
      while curr:
         curr.next, prev, curr = prev, curr, curr.next
      return prev