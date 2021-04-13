# https://leetcode.com/problems/linked-list-cycle-ii/
# O(n+k), O(1)


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
      slow, fast = head, head
      
      while fast and fast.next:
         slow = slow.next
         fast = fast.next.next
         # Loop detected
         if slow == fast:
            fast = head
            # Move the distance needed to find where loop started
            while slow != fast:
               slow = slow.next
               fast = fast.next
            return slow  