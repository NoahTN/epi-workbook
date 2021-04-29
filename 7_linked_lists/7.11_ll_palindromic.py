# https://leetcode.com/problems/palindrome-linked-list


class Solution:
   # O(n), O(1)
   # Modifies the linked list
   def isPalindrome(self, head: ListNode) -> bool:
      slow = fast = head
      # Split into halves
      while fast and fast.next:
         fast, slow = fast.next.next, slow.next
      
      # Reverse second half
      prev = None
      while slow:
         slow.next, prev, slow = prev, slow, slow.next

      # Iterate and compare first half vs reversed second   
      curr = head
      while prev:
         if prev.val != curr.val:
            return False
         prev = prev.next
         curr = curr.next
      
      return True
   
   # O(n), O(n)
   # Doesn't modify the linked list
   def isPalindromeSafe(self, head: ListNode) -> bool:
      nodes = []
      curr = head
      
      while curr:
         nodes.append(curr.val)
         curr = curr.next
         
      return nodes == nodes[::-1]