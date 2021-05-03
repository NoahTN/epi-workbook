# https://leetcode.com/problems/symmetric-tree
# O(n), O(1), O(h)

class Solution:
   def isSymmetric(self, root: TreeNode) -> bool:
      if not root:
         return True
      
      def compare(left, right):
         if not left and not right:
            return True
         if not left or not right:
            return False
         if left.val != right.val:
            return False
         
         l_sym = compare(left.left, right.right)
         r_sym = compare(left.right, right.left)
         return l_sym and r_sym
      
      return compare(root.left, root.right)