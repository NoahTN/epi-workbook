# https://leetcode.com/problems/intersection-of-two-linked-lists
# O(n+m), O(1)

class Solution:
   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      nodeA = headA
      nodeB = headB
      
      # Works with no intersection because of the common ending of None
      while nodeA is not nodeB:
         nodeA = nodeA.next if nodeA else headB
         nodeB = nodeB.next if nodeB else headA
         
      return nodeA